import json
from pathlib import Path
from typing import Any


def _load_yaml_if_available(path: Path) -> dict[str, Any]:
    try:
        import yaml  # type: ignore
    except ModuleNotFoundError as exc:
        raise RuntimeError(
            "YAML config requested but PyYAML is not installed. "
            "Use JSON config or install pyyaml."
        ) from exc

    with path.open("r", encoding="utf-8") as f:
        return yaml.safe_load(f) or {}


def load_config(config_path: str) -> dict[str, Any]:
    path = Path(config_path)
    if not path.exists():
        raise FileNotFoundError(f"Config not found: {config_path}")

    if path.suffix.lower() == ".json":
        return json.loads(path.read_text(encoding="utf-8"))

    if path.suffix.lower() in {".yaml", ".yml"}:
        return _load_yaml_if_available(path)

    raise ValueError("Unsupported config extension. Use .json/.yaml/.yml")
