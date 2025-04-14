import os
from dotenv import load_dotenv

load_dotenv()

GEMINI_API_KEY = os.getenv("GEMINI_API_KEY")
FIRMS_MAP_KEY = os.getenv("NASA_API_KEY")