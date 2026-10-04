# sdks/python/examples - exemplos python (canonicos)

@version 1.4.0 | criado: 28/09/2026 17:21 | atualizado: 04/10/2026 02:35

## O que e
Os 4 exemplos python (.py) dos endpoints da API, EXPORTADOS DA LANDING PAGE (fonte unica
de verdade). Nunca editados a mao.

## Fonte unica de verdade
- FalaAI_landing/lib/sandbox-examples.ts -> SANDBOX_EXAMPLES[<endpoint>].python
- que INTERPOLA FalaAI_landing/lib/sandbox-json-example.ts (SANDBOX_JSON_EXAMPLE = dados reais).

## Script (ferramenta)
_generate_python_examples.mjs (prefixo _ = ferramenta, nao exemplo)

| Comando                                      | Acao                                                      |
|----------------------------------------------|-----------------------------------------------------------|
| node _generate_python_examples.mjs             | Exporta (escreve os .py a partir da landing + README)     |
| node _generate_python_examples.mjs --check     | Verifica (compara .py x landing; exit 1 se divergir)      |

- Roda de QUALQUER pasta (resolve a landing pelo proprio caminho).
- Pre-requisito: Node (v22+).
- NUNCA edite os .py nem este README a mao: edite a landing e reexecute o script.

## Ordem obrigatoria (regra)
1. Altere a FONTE (landing / SANDBOX_JSON_EXAMPLE).
2. Valide o cURL primeiro:  node _generate_python_examples.mjs --check   (exit 0 = ok)
3. So depois espelhe nas outras linguagens.
4. Cadeia integrada no pipeline: scripts/regenerate_all.py (T11) exporta via node.

## Relatorio da ultima execucao
| Data | Modo | Resultado |
|------|------|-----------|
| 04/10/2026 02:35 | verificacao (--check) | OK - 5 exemplos python 100% conforme a landing. |

| Arquivo | Endpoint | Status | Gerado em |
|---------|----------|--------|-----------|
| health.py | GET  /v1/health | ok | 04/10/2026 02:19 |
| transcribe.py | POST /v1/audio/transcriptions | ok | 04/10/2026 02:19 |
| diagnose.py | POST /v1/analyze/diagnostic | ok | 04/10/2026 02:19 |
| audit.py | POST /v1/analyze/riskAudit | ok | 04/10/2026 02:19 |
| whatsapp.py | whatsapp.py | ok | 04/10/2026 02:19 |

## Datas
- Criacao:     28/09/2026 17:21
- Atualizacao: 04/10/2026 02:35

Gerado automaticamente por _generate_python_examples.mjs - NAO edite a mao.
