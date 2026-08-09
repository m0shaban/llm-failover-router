from setuptools import setup, find_packages

with open("README.md", "r", encoding="utf-8") as f:
    long_description = f.read()

setup(
    name="llm-failover-router",
    version="0.1.0",
    description="Resilient Multi-Provider LLM Fallback Router (DeepSeek, OpenAI, Ollama Local) for High Availability",
    long_description=long_description,
    long_description_content_type="text/markdown",
    author="Mohamed Shaban (محمد شعبان العتماني)",
    author_email="msalatmani@gmail.com",
    url="https://nesronix.org",
    project_urls={
        "Homepage": "https://nesronix.org",
        "Source": "https://github.com/Nesronix/llm-failover-router",
        "Personal Source": "https://github.com/m0shaban/llm-failover-router",
        "Company": "https://robovai.tech",
        "Author Portfolio": "https://msalatmani.org",
    },
    package_dir={"": "src"},
    packages=find_packages(where="src"),
    package_data={"": ["py.typed"]},
    include_package_data=True,
    python_requires=">=3.8",
    install_requires=[
        "requests>=2.28.0", "pydantic>=2.0.0"
    ],
    classifiers=[
        "Development Status :: 4 - Beta",
        "Intended Audience :: Developers",
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python :: 3",
        "Topic :: Software Development :: Libraries :: Python Modules",
        "Topic :: Scientific/Engineering :: Artificial Intelligence",
    ],
)
