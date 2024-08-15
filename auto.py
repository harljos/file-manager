import os
from dotenv import load_dotenv

load_dotenv

source_dir = os.getenv('SOURCE_DIR')

with os.scandir(source_dir) as entries:
    for entry in entries:
        print(entry.name)