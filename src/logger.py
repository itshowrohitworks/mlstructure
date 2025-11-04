import logging
import os
from datetime import datetime

LOG_DIR = "logs"
LOG_FILE = f"{datetime.now().strftime('%Y%m%d_%H%M%S')}.log"

os.makedirs(LOG_DIR, exist_ok=True)

LOG_FILE_PATH = os.path.join(LOG_DIR, LOG_FILE)

logging.basicConfig(
    filename=LOG_FILE_PATH,
    format="[ %(asctime)s ] %(name)s - %(levelname)s - %(lineno)d - %(message)s",
    level=logging.INFO,
)

if __name__ == "__main__":
    logger = logging.getLogger(__name__)
    print(f"Logger test running...\nLog file created at: {LOG_FILE_PATH}")

    logger.info("✅ Logger is working correctly and writing to the file.")

    print("Done. Check your 'logs' folder for the new log file.")
