#!/usr/bin/env python3
import os

from falaai_api import ApiClient, Configuration, WhatsappApi

config = Configuration(host=os.environ.get("FALAAI_BASE_URL", "https://api01-falaai.action.tec.br"))
config.access_token = os.environ["FALAAI_API_KEY"]
client = ApiClient(configuration=config)
whatsapp_api = WhatsappApi(client)

# PREVIEW (dry_run) - passo GRATIS: valida/segmenta o export e ESTIMA os creditos, SEM IA e SEM debito.
# SEM start/end: a API usa o periodo REAL do export (fora do preview a janela e obrigatoria).
# REQUIRED: file (.zip/.txt export), timezone, date_format + Authorization
# OPTIONAL: gap_minutes (default 720) | min_messages (default 2) | client_reference_id
with open("demo_whatsapp.zip", "rb") as f:
    result = whatsapp_api.extract_conversations_v1_whatsapp_extract_conversations_post(
        file=("demo_whatsapp.zip", f.read()),
        timezone="-3",
        date_format="day_first",
        gap_minutes=720,
        min_messages=2,
        voice_note=True,
        expression=True,
        dry_run=True,
    )

print(result.model_dump_json(indent=2))
