# sdks/python/examples - exemplos python (canonicos)

@version 1.4.0 | criado: 15/10/2026 18:44 | atualizado: 18/10/2026 11:17

## O que e
Os 7 exemplos python (.py) - 4 endpoints + 3 variantes do WhatsApp - EXPORTADOS DA LANDING PAGE (fonte unica
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
| 18/10/2026 11:17 | exportacao | OK - 7 exemplos python exportados da landing. |

| Arquivo | Endpoint | Status | Gerado em |
|---------|----------|--------|-----------|
| health.py | GET  /v1/health | exportado (406 chars) | 18/10/2026 11:17 |
| transcribe.py | POST /v1/audio/transcriptions | exportado (823 chars) | 18/10/2026 11:17 |
| diagnose.py | POST /v1/analyze/diagnostic | exportado (5002 chars) | 18/10/2026 11:17 |
| audit.py | POST /v1/analyze/riskAudit | exportado (3784 chars) | 18/10/2026 11:17 |
| whatsapp_preview.py | whatsapp.py | exportado (1085 chars) | 18/10/2026 11:17 |
| whatsapp_periodo.py | whatsapp.py | exportado (1104 chars) | 18/10/2026 11:17 |
| whatsapp_janelas.py | whatsapp.py | exportado (1186 chars) | 18/10/2026 11:17 |

## Datas
- Criacao:     15/10/2026 18:44
- Atualizacao: 18/10/2026 11:17

Gerado automaticamente por _generate_python_examples.mjs - NAO edite a mao.
