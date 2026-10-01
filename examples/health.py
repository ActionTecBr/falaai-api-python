#!/usr/bin/env python3
import os

from falaai_api import ApiClient, Configuration, HealthApi

config = Configuration(host=os.environ.get("FALAAI_BASE_URL", "https://api01-falaai.action.tec.br"))
client = ApiClient(configuration=config)
health_api = HealthApi(client)

health = health_api.health_check()

print(health.model_dump_json(indent=2))

head = health_api.health_check_head_without_preload_content()
