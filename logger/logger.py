import logging
import os
from datetime import datetime, timezone
from pathlib import Path

from rich.logging import RichHandler

LOG_DIR = str(Path(__file__).parent.parent / "logs")
LATEST_LOG = os.path.join(LOG_DIR, "latest.log")

os.makedirs(LOG_DIR, exist_ok=True)

if os.path.exists(LATEST_LOG):
    mtime = os.path.getmtime(LATEST_LOG)
    stamp = datetime.fromtimestamp(mtime, tz=timezone.utc).strftime("%Y-%m-%d-%H%M%S")
    os.rename(LATEST_LOG, os.path.join(LOG_DIR, f"discord-{stamp}.log"))

logging.basicConfig(
    level=logging.INFO, format="%(message)s", handlers=[RichHandler(rich_tracebacks=True, show_path=False, markup=True)]
)
logger = logging.getLogger("discord")
file_handler = logging.FileHandler(filename=LATEST_LOG, encoding="utf-8", mode="w")
file_handler.setFormatter(logging.Formatter("%(asctime)s:%(levelname)s:%(name)s: %(message)s"))
logger.addHandler(file_handler)
