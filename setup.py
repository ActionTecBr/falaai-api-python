import pathlib

from setuptools import find_packages, setup

here = pathlib.Path(__file__).parent.resolve()
long_description = (here / "README.md").read_text(encoding="utf-8")

setup(
    name="falaai-api",
    version="1.21.48",
    description="Official Python SDK for the FalaAI API - AI-powered call transcription, diagnosis and compliance auditing.",
    long_description=long_description,
    long_description_content_type="text/markdown",
    author="Action Tec Br",
    author_email="livio@action.tec.br",
    url="https://falaai.action.tec.br/api",
    license="MIT",
    project_urls={
        "Homepage": "https://falaai.action.tec.br/api",
    "Repository": "https://github.com/ActionTecBr/falaai-api-python",
    "Issues": "https://github.com/ActionTecBr/falaai-api-python/issues",
    },
    keywords=["falaai", "api", "sdk", "call-center", "contact-center", "speech-to-text", "transcription", "conversation-intelligence", "sentiment-analysis", "compliance", "audit", "copc", "iso-18295", "lgpd", "omnichannel", "helpdesk", "chatbot", "whatsapp", "crm", "crm-integration"],
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
        "Intended Audience :: Developers",
    ],
    packages=find_packages(),
    python_requires=">=3.11, <4",
    install_requires=["httpx >= 0.23.1, < 0.29.0", "attrs >= 22.2.0"],
    package_data={"falaai_api": ["py.typed"]},
)
