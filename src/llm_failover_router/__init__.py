"""
llm-failover-router: Resilient Multi-Provider LLM Fallback Router.
Author: Mohamed Shaban (msalatmani@gmail.com)
"""

from .router import LLMRouter, ProviderConfig, RouterResponse

__version__ = "0.1.0"
__author__ = "Mohamed Shaban"
__all__ = ["LLMRouter", "ProviderConfig", "RouterResponse"]
