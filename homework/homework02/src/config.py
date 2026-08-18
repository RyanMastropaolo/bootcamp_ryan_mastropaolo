import os
from pathlib import Path
from typing import Optional

from dotenv import load_dotenv

def load_env():
    load_dotenv() # looks for a .env file in the current and parent directories

def get_key(name: str, default: Optional[str] = None) -> Optional[str]:
    return os.getenv(name, default)

PROJECT_ROOT = Path.cwd()
DATA_DIR = PROJECT_ROOT / "data"