import os
from pathlib import Path
from dotenv import load_dotenv

# Load environment variables from .env
load_dotenv()

# --- Database Path ---
# Store DB inside 'data' folder
BASE_DIR = Path(__file__).resolve().parent.parent.parent
DATA_DIR = BASE_DIR / "data"
DATA_DIR.mkdir(exist_ok=True)  # Create if not exists
DB_PATH = DATA_DIR / "infofinder.db"

# --- Encryption ---
ENCRYPTION_PASSWORD = os.getenv("ENCRYPTION_PASSWORD", "ChangeThisPassword!")

# --- Tesseract Path ---
TESSERACT_PATH = os.getenv("TESSERACT_PATH", r"C:\Program Files\Tesseract-OCR\tesseract.exe")

# --- Validate Tesseract ---
if not Path(TESSERACT_PATH).exists():
    raise FileNotFoundError(f"Tesseract not found at {TESSERACT_PATH}. Please check your .env file.")

# --- App Config ---
INDEXED_FOLDERS = []  # Will be updated by API
EXCLUDE_PATTERNS = ["*.tmp", "*.log", "*.cache"]

