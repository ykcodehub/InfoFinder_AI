import logging
from pathlib import Path

# Log file path
LOG_FILE = Path(__file__).resolve().parent.parent.parent / "data" / "app.log"

# Configure logging
logging.basicConfig(
    level=logging.INFO,  # Default logging level
    format="%(asctime)s [%(levelname)s] %(name)s: %(message)s",
    handlers=[
        logging.FileHandler(LOG_FILE, encoding="utf-8"),  # Save logs to file
        logging.StreamHandler()  # Also print logs in terminal
    ]
)

# Get a logger instance
logger = logging.getLogger("InfoFinderAI")
