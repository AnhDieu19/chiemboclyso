import sys
import os
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

import unittest
from google import genai
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

API_KEY = os.environ.get('GEMINI_API_KEY')
if not API_KEY:
    raise ValueError(
        "GEMINI_API_KEY environment variable is not set. "
        "Please create a .env file with your API key."
    )

if __name__ == "__main__":
    print("Listing models...")
    with open("test_log.txt", "w", encoding="utf-8") as f:
        try:
            client = genai.Client(api_key=API_KEY)
            # List all models
            for m in client.models.list():
                f.write(f"FOUND: {m.name}\n")
        except Exception as e:
            f.write(f"Error: {str(e)}\n")
    print("Done. Check test_log.txt")
