import json
from datetime import datetime
from pathlib import Path

LOG_DIR = Path(__file__).resolve().parent / "logs"
LOG_DIR.mkdir(exist_ok=True)


def _json(obj):
    try:
        if hasattr(obj, "to_dict"):
            return json.dumps(obj.to_dict(), ensure_ascii=False, indent=2, default=str)
        return json.dumps(obj, ensure_ascii=False, indent=2, default=str)
    except Exception as e:
        return f"<nao serializavel: {e}>"


def log_test(name, method, path, payload, response, result, status_code=None):
    ts = datetime.now().strftime("%Y%m%d_%H%M%S")
    safe = name.upper().replace("/", "_").replace(" ", "_").replace("{", "").replace("}", "")
    folder = LOG_DIR / safe
    folder.mkdir(exist_ok=True)
    fname = f"{safe}_{ts}.log"
    lines = []
    lines.append("=" * 70)
    lines.append(f"TESTE: {method} {path}")
    lines.append(f"DATA: {datetime.now().isoformat()}")
    lines.append("=" * 70)
    lines.append("")
    lines.append("--- PAYLOAD (enviado) ---")
    lines.append(_json(payload) if payload is not None else "(sem payload)")
    lines.append("")
    lines.append("--- RESPOSTA (saida do SDK) ---")
    if status_code is not None:
        lines.append(f"HTTP: {status_code}")
    lines.append(_json(response) if response is not None else "(sem resposta)")
    lines.append("")
    lines.append("--- RESULTADO ---")
    lines.append(str(result))
    lines.append("")
    (folder / fname).write_text("\n".join(lines), encoding="utf-8")
    return folder / fname