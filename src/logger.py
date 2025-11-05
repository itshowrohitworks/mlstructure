import logging
import os
from datetime import datetime


LOG_FILE = f"{datetime.now().strftime('%Y%m%d_%H%M%S')}.log"
LOG_DIR = os.path.join(os.getcwd(),"logs",LOG_FILE)
os.makedirs(LOG_DIR, exist_ok=True)

LOG_FILE_PATH = os.path.join(LOG_DIR, LOG_FILE)

logging.basicConfig(
    filename=LOG_FILE_PATH,
    format="[ %(asctime)s ] %(name)s - %(levelname)s - %(lineno)d - %(message)s",
    level=logging.INFO,
)