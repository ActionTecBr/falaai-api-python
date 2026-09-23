# FalaAI API - Python SDK

[![version](https://img.shields.io/badge/version-1.21.47-blue)](https://pypi.org/project/falaai-api/)
[![license](https://img.shields.io/badge/license-MIT-green)](https://github.com/ActionTecBr/falaai-api-python/blob/main/LICENSE)
[![build](https://github.com/ActionTecBr/falaai-api-python/actions/workflows/ci.yml/badge.svg)](https://github.com/ActionTecBr/falaai-api-python/actions/workflows/ci.yml)

Official Python SDK for the **FalaAI API**.

## What is FalaAI API?

FalaAI API turns conversations into auditable business intelligence, in three steps:

1. **Transcribe** - audio (calls, voice notes, meetings) to text, with speaker separation.
2. **Diagnose** - summary, reason, recommended action, topic and sentiment per conversation.
3. **Audit compliance** - risk score and violations against **COPC CX** and **ISO 18295-1**.

It works with **phone calls and call recordings** (PABX IP, Asterisk, FreePBX, contact center),
**messaging** (WhatsApp, Telegram, web chat, SMS) and email - anything that can be turned into
text. Three REST endpoints, one API key, no setup.

## Who it's for

| Role | What they get |
| --- | --- |
| **Contact Center / Quality** | Audit 100% of conversations instead of a sample |
| **Compliance / Legal** | Forensic, auditable evidence for audits and disputes |
| **CX / Operations** | Risk score, sentiment and reason for every conversation |
| **Developers** | One typed SDK, three REST endpoints, one API key |
| **Data / BI** | Clean, typed JSON ready for your database or BI tool |

## Install

```bash
pip install falaai-api
```

## Quick start

```python
from falaai_api import AuthenticatedClient
from falaai_api.api.speech import create_transcription_v1_audio_transcriptions_post
from falaai_api.models.body_create_transcription_v1_audio_transcriptions_post import (
    BodyCreateTranscriptionV1AudioTranscriptionsPost,
)
from falaai_api.types import File

client = AuthenticatedClient(
    base_url="https://api01-falaai.action.tec.br",
    token="fai_xxxxxx",
)

with open("call.mp3", "rb") as f:
    response = create_transcription_v1_audio_transcriptions_post.sync_detailed(
        client=client,
        body=BodyCreateTranscriptionV1AudioTranscriptionsPost(
            file=File(payload=f, file_name="call.mp3", mime_type="audio/mpeg"),
            model="falaai-transcribe-1",
            language="pt",
        ),
    )

print(response.parsed.text)
```

## Use cases

- Call and voice-note **transcription** with speaker separation
- **Contact center quality assurance (QA)** automation
- **Compliance auditing** against **COPC CX** and **ISO 18295-1**
- **Risk detection** - churn risk, legal threats, escalation
- **WhatsApp, Telegram and chat** conversation analysis
- **CRM and help desk** enrichment
- **LGPD**-aware handling of customer conversations

## Where it fits

Common Python stacks in contact center, CRM and help desk - if you build on any of these, the SDK drops in:

Odoo - ERPNext / Frappe - Django CRMs - LangChain / LlamaIndex - Telethon

> Product names are trademarks of their respective owners, listed as common stacks in this ecosystem. No partnership is implied.

## Endpoints

| Method | Path | Description |
| --- | --- | --- |
| `POST` | `/v1/audio/transcriptions` | Audio to text, with speaker separation |
| `POST` | `/v1/analyze/diagnostic` | Conversation analysis - summary, reason, action, topic, sentiment |
| `POST` | `/v1/analyze/auditoriaRisco` | Compliance audit - risk score and violations |

All endpoints require `Authorization: Bearer fai_xxxxxx`.
Full reference: <https://api01-falaai.action.tec.br/docs>

## Links

- **Product:** <https://falaai.action.tec.br/api>
- **API reference:** <https://api01-falaai.action.tec.br/docs>
- **Get an API key:** <https://falaai.action.tec.br/api/auth>
- **Package (PyPI):** <https://pypi.org/project/falaai-api/>
- **Source:** <https://github.com/ActionTecBr/falaai-api-python>

## License

MIT (c) 2026 Action Tec Br - see [LICENSE](LICENSE).
