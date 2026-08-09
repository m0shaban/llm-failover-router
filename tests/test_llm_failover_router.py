import pytest
from unittest.mock import patch, MagicMock
from llm_failover_router import LLMRouter, ProviderConfig, RouterResponse

def test_router_init():
    p1 = ProviderConfig(name="deepseek", api_key="key1", model="deepseek-chat")
    p2 = ProviderConfig(name="ollama", endpoint="http://localhost:11434")
    router = LLMRouter(providers=[p1, p2], timeout_seconds=10.0)
    assert len(router.providers) == 2
    assert router.timeout_seconds == 10.0

@patch("requests.post")
def test_router_success(mock_post):
    mock_resp = MagicMock()
    mock_resp.json.return_value = {"choices": [{"message": {"content": "Hello from DeepSeek"}}]}
    mock_resp.raise_for_status.return_value = None
    mock_post.return_value = mock_resp

    p1 = ProviderConfig(name="deepseek", api_key="key1", model="deepseek-chat")
    router = LLMRouter(providers=[p1])
    resp = router.generate("Hi")
    assert resp.content == "Hello from DeepSeek"
    assert resp.provider_used == "deepseek"
