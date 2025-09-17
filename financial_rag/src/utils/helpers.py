"""Helper utilities (minimal)."""

import logging
from pathlib import Path
import yaml

logger = logging.getLogger(__name__)

class ConfigManager:
    def __init__(self, config_path: str = "config/config.yaml"):
        self.config_path = config_path
        self.config = self._load_config()

    def _load_config(self):
        try:
            p = Path(self.config_path)
            if not p.exists():
                return {}
            with open(p, "r", encoding="utf-8") as f:
                return yaml.safe_load(f)
        except Exception as e:
            logger.error(f"Failed to load config: {e}")
            return {}

def setup_logging(config: dict | None = None, level: int = None):
    cfg = config or {}
    log_dir = Path(cfg.get("logging", {}).get("log_dir", "logs"))
    log_dir.mkdir(parents=True, exist_ok=True)
    logging.basicConfig(level=level or logging.INFO)
    return logging.getLogger(__name__)