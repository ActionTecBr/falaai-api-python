import pathlib

from setuptools import find_packages, setup

here = pathlib.Path(__file__).parent.resolve()
long_description = (here / "README.md").read_text(encoding="utf-8")

setup(
    name="falaai-api",
    version="1.21.49",
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
    packages=find_packages(exclude=["tests", "tests.*"]),
    python_requires=">=3.11, <4",
    install_requires=["urllib3 >= 1.25.3, < 3.0.0", "python-dateutil >= 2.8.2", "pydantic >= 2", "typing-extensions >= 4.7.1"],
    package_data={"falaai_api": ["py.typed"]},
)
