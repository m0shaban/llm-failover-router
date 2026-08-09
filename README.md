# LLM Failover Router (`llm-failover-router`)

<div align="center">

[![PyPI version](https://img.shields.io/pypi/v/llm-failover-router.svg?style=flat-square&color=blue)](https://pypi.org/project/llm-failover-router/)
[![Python Versions](https://img.shields.io/pypi/pyversions/llm-failover-router.svg?style=flat-square)](https://pypi.org/project/llm-failover-router/)
[![License: MIT](https://img.shields.io/badge/License-MIT-green.svg?style=flat-square)](https://opensource.org/licenses/MIT)
[![Code style: ruff](https://img.shields.io/badge/code%20style-ruff-000000.svg?style=flat-square)](https://github.com/astral-sh/ruff)
[![Type Checked: mypy](https://img.shields.io/badge/type%20checked-mypy-blue.svg?style=flat-square)](https://mypy-lang.org/)
[![Nesronix Ecosystem](https://img.shields.io/badge/Nesronix-Ecosystem-blueviolet.svg?style=flat-square)](https://nesronix.org)

**Resilient Multi-Provider LLM Fallback Router (DeepSeek, OpenAI, Ollama Local) for High Availability**

[Nesronix Community](https://nesronix.org) • [PyPI Package](https://pypi.org/project/llm-failover-router/) • [Author Portfolio](https://msalatmani.org)

</div>

---

## ⚡ Overview & Value Proposition

`llm-failover-router` is a production-ready, enterprise-grade Python library developed as part of the **Nesronix & RoboVAI** open-source AI infrastructure ecosystem.

Built with strict performance benchmarks, comprehensive type safety (`py.typed`), and zero unnecessary runtime dependencies, `llm-failover-router` enables developers to build scalable, resilient AI and backend applications with minimal boilerplate.

```
┌────────────────────────────────────────────────────────┐
│               Application Layer (FastAPI / Streamlit / CLI) │
└───────────────────────────┬────────────────────────────┘
                            │
              ▼───────────────────────────▼
              │      LLM Failover Router      │
              │  (Async-Ready • Type-Safe • Modular Core)│
              ▲───────────────────────────▲
                            │
┌───────────────────────────┴────────────────────────────┐
│      Production Infrastructure (Cloud / Docker / Edge)  │
└────────────────────────────────────────────────────────┘
```

---

## 🚀 Key Features

- **High-Availability LLM Routing**: Never suffer outages due to single-provider downtime or rate limits (429/503).
- **Dynamic Tiered Fallback**: Automatically tries Provider 1 -> Provider 2 -> Local Ollama.
- **Unified Response Interface**: Standardized `RouterResponse` regardless of upstream provider schema.
- **Latency & Timeout Guards**: Configurable per-provider timeouts to prevent stalled requests.
- **Auditing & Telemetry**: Full error capturing and fallback audit logs.

---

## 📦 Installation

Install the package directly from **PyPI**:

```bash
# Using pip
pip install llm-failover-router

# Using uv (High speed package manager)
uv add llm-failover-router

# Using poetry
poetry add llm-failover-router
```

---

## 💡 Quickstart

```python
from llm_failover_router import LLMRouter, ProviderConfig

# Configure provider fallback priority list
providers = [
    ProviderConfig(name="deepseek", api_key="sk-...", model="deepseek-chat"),
    ProviderConfig(name="openai", api_key="sk-...", model="gpt-4o-mini"),
    ProviderConfig(name="ollama", endpoint="http://localhost:11434/api/generate", model="llama3")
]

router = LLMRouter(providers=providers, timeout_seconds=8.0)
# response = router.generate("What is the capital of Egypt?")
# print(f"Used: {response.provider_used} | Output: {response.content}")
```

---

## 🛠️ Enterprise Architecture & Verification

All packages in the Nesronix ecosystem adhere to strict software quality assurance guidelines:

- **100% Type-Checked:** Complete PEP 561 compliance with `py.typed` embedded.
- **Automated CI/CD:** Cross-platform multi-Python matrix testing (Python 3.8 through 3.13) via GitHub Actions.
- **Modern Packaging:** Full PEP 517 / PEP 621 compliance (`pyproject.toml`).

---

## 🤝 Contributing

Contributions are welcome! Please read our [CONTRIBUTING.md](CONTRIBUTING.md) guide and submit pull requests to the main repository.

1. Fork the Project
2. Create your Feature Branch (`git checkout -b feature/AmazingFeature`)
3. Run the Test Suite (`pytest`)
4. Commit your Changes (`git commit -m 'feat: Add some AmazingFeature'`)
5. Push to the Branch (`git push origin feature/AmazingFeature`)
6. Open a Pull Request

---

## 📄 License & Authors

Distributed under the **MIT License**. See [LICENSE](LICENSE) for more information.

- **Author & Architect:** [Mohamed Shaban (محمد شعبان العتماني)](https://github.com/m0shaban) — *Applied AI Engineer* ([msalatmani.org](https://msalatmani.org))
- **Community:** [Nesronix Community](https://nesronix.org) • [GitHub @Nesronix](https://github.com/Nesronix)
