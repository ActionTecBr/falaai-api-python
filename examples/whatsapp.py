#!/usr/bin/env python3
import os

from falaai_api import ApiClient, Configuration, WhatsappApi

config = Configuration(host=os.environ.get("FALAAI_BASE_URL", "https://api01-falaai.action.tec.br"))
config.access_token = os.environ["FALAAI_API_KEY"]
client = ApiClient(configuration=config)
whatsapp_api = WhatsappApi(client)

# REQUIRED: file (.zip/.txt export), start, end, timezone, date_format + Authorization
# OPTIONAL: gap_minutes (default 720) | min_messages (default 2) | chars_per_minute (default 800) | client_reference_id
with open("demo_whatsapp.zip", "rb") as f:
    result = whatsapp_api.extract_conversations(
        file=f,
        start="2024-01-01T00:00:00",
        end="2024-12-31T23:59:59",
        timezone="-3",
        date_format="day_first",
        gap_minutes=720,
        min_messages=2,
        chars_per_minute=800,
    )

print(result.model_dump_json(indent=2))
