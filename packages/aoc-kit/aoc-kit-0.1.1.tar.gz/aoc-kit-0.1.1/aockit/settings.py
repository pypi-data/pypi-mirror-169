import os
from dotenv import load_dotenv

load_dotenv()

AOC_TOKEN = os.environ.get("AOC_TOKEN", "")
INPUT_FOLDER = os.environ.get("INPUT_FOLDER", "./inputs")
