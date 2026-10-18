#!/usr/bin/env python3
import os

from falaai_api import ApiClient, Configuration, WhatsappApi

config = Configuration(host=os.environ.get("FALAAI_BASE_URL", "https://api01-falaai.action.tec.br"))
config.access_token = os.environ["FALAAI_API_KEY"]
client = ApiClient(configuration=config)
whatsapp_api = WhatsappApi(client)

# EXTRACAO real (debita creditos) por VARIAS janelas - selecao = UNIAO das sobreposicoes (dedup).
# windows NAO combina com start/end (400 invalid_windows); a 2a janela e um exemplo.
# REQUIRED: file (.zip/.txt export), windows, timezone, date_format + Authorization
# OPTIONAL: gap_minutes (default 720) | min_messages (default 2) | client_reference_id
with open("demo_whatsapp.zip", "rb") as f:
    result = whatsapp_api.extract_conversations_v1_whatsapp_extract_conversations_post(
        file=("demo_whatsapp.zip", f.read()),
        windows='[{"start":"2024-01-01 00:00","end":"2024-12-31 23:59"},{"start":"06/03/2024 09:00","end":"06/03/2024 12:00"}]',
        timezone="-3",
        date_format="day_first",
        gap_minutes=720,
        min_messages=2,
        voice_note=True,
        expression=True,
    )

print(result.model_dump_json(indent=2))
