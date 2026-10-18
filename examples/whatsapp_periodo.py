#!/usr/bin/env python3
import os

from falaai_api import ApiClient, Configuration, WhatsappApi

config = Configuration(host=os.environ.get("FALAAI_BASE_URL", "https://api01-falaai.action.tec.br"))
config.access_token = os.environ["FALAAI_API_KEY"]
client = ApiClient(configuration=config)
whatsapp_api = WhatsappApi(client)

# EXTRACAO real (debita creditos) - janela UNICA: start/end OBRIGATORIAS fora do dry_run.
# Datas no formato do date_format (ex. day_first -> 05/03/2024 00:00).
# REQUIRED: file (.zip/.txt export), start, end, timezone, date_format + Authorization
# OPTIONAL: gap_minutes (default 720) | min_messages (default 2) | client_reference_id
with open("demo_whatsapp.zip", "rb") as f:
    result = whatsapp_api.extract_conversations_v1_whatsapp_extract_conversations_post(
        file=("demo_whatsapp.zip", f.read()),
        start="2024-01-01 00:00",
        end="2024-12-31 23:59",
        timezone="-3",
        date_format="day_first",
        gap_minutes=720,
        min_messages=2,
        voice_note=True,
        expression=True,
    )

print(result.model_dump_json(indent=2))
