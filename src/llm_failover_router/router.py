from dataclasses import dataclass, field
from typing import List, Optional
import requests
import logging

logger = logging.getLogger("llm_failover_router")

@dataclass
class ProviderConfig:
    name: str
    api_key: str = ""
    model: str = ""
    endpoint: str = ""

@dataclass
class RouterResponse:
    content: str
    provider_used: str
    status: str = "success"
    errors: List[str] = field(default_factory=list)

class LLMRouter:
    """
    Automatic multi-provider LLM failover router.
    """
    def __init__(self, providers: List[ProviderConfig], timeout_seconds: float = 8.0):
        self.providers = providers
        self.timeout_seconds = timeout_seconds

    def generate(self, prompt: str) -> RouterResponse:
        errors = []
        for p in self.providers:
            try:
                content = self._call_provider(p, prompt)
                if content:
                    return RouterResponse(content=content, provider_used=p.name, errors=errors)
            except Exception as e:
                err_msg = f"Provider {p.name} failed: {str(e)}"
                logger.warning(err_msg)
                errors.append(err_msg)
                
        raise RuntimeError(f"All LLM providers failed. Errors: {'; '.join(errors)}")

    def _call_provider(self, provider: ProviderConfig, prompt: str) -> str:
        name = provider.name.lower()
        
        if "deepseek" in name or "openai" in name:
            url = provider.endpoint or ("https://api.deepseek.com/v1/chat/completions" if "deepseek" in name else "https://api.openai.com/v1/chat/completions")
            headers = {"Authorization": f"Bearer {provider.api_key}", "Content-Type": "application/json"}
            payload = {
                "model": provider.model or ("deepseek-chat" if "deepseek" in name else "gpt-4o-mini"),
                "messages": [{"role": "user", "content": prompt}]
            }
            r = requests.post(url, headers=headers, json=payload, timeout=self.timeout_seconds)
            r.raise_for_status()
            return r.json()["choices"][0]["message"]["content"]
            
        elif "ollama" in name:
            url = provider.endpoint or "http://localhost:11434/api/generate"
            payload = {"model": provider.model or "llama3", "prompt": prompt, "stream": False}
            r = requests.post(url, json=payload, timeout=self.timeout_seconds)
            r.raise_for_status()
            return r.json().get("response", "")
            
        else:
            raise ValueError(f"Unsupported provider: {provider.name}")
