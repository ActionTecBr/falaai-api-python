#!/usr/bin/env python3
import os

from falaai_api import ApiClient, Configuration, SpeechApi

config = Configuration(host=os.environ.get("FALAAI_BASE_URL", "https://api01-falaai.action.tec.br"))
config.access_token = os.environ["FALAAI_API_KEY"]
client = ApiClient(configuration=config)
speech_api = SpeechApi(client)
# REQUIRED: file (audio) + Authorization (fai_ key)
# OPTIONAL (server defaults): model -> falaai-transcribe-1 | language -> pt | client_reference_id -> (empty)

with open("demo_callcenter.mp3", "rb") as fh:
    transcription = speech_api.create_transcription_v1_audio_transcriptions_post(
        file=("demo_callcenter.mp3", fh.read()),
        model="falaai-transcribe-1",
        language="pt",
        client_reference_id="call_202609271408",
    )

print(transcription.model_dump_json(indent=2))
