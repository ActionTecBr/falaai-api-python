# sdks/python/tests/e2e - Testes de execucao dos exemplos Python

@version 1.0.0 | criado: 27/09/2026 17:24 | atualizado: 27/09/2026 17:24

## O que e
Executa EXATAMENTE os 4 exemplos de ../../examples/*.py contra a API e valida
(exit 0 = OK). Gera um LOG COMPLETO por endpoint em logs/.

## Estrutura
tests/e2e/
  run_examples.py                         (runner)
  logs/<ENDPOINT>/<ENDPOINT>_<ts>.log     (resposta COMPLETA por execucao)
  demo_callcenter.mp3                     (audio copiado da landing - teste de transcribe)

## Como rodar
1. Coloque a chave fai_ valida no run_examples.py (linha 'COLE AQUI').
2. python tests/e2e/run_examples.py health
   (troque 'health' por: all | transcribe | diagnostic | auditoria)
   - API LOCAL: FALAAI_BASE_URL=http://localhost:8002 python tests/e2e/run_examples.py all

## Logs (nome por endpoint)
HEALTH_GET, TRANSCRIPTIONS, DIAGNOSTIC, AUDITORIARISCO

## Regras
- Nunca gravar a chave real nos exemplos (so no proprio run_examples.py).
- Falha = grita (exit 1); o log guarda a resposta completa (inclusive erro).