import logging
import os
from datetime import datetime

# Create a log file name with the current date
LOG_FILE = f"{datetime.now().strftime('%Y-%m-%d')}.log"

# Create a logs directory if it does not exist
logs_directory = "logs"
os.makedirs(logs_directory, exist_ok=True)

# Full path to the log file inside the logs directory
LOG_FILE_PATH = os.path.join(logs_directory, LOG_FILE)

# Set up the logging configuration
logging.basicConfig(
    filename=LOG_FILE_PATH,
    format="[%(asctime)s] %(lineno)d %(name)s - %(levelname)s - %(message)s",
    level=logging.INFO,
)

# Example function to test logging
if __name__ == "__main__":
    logger = logging.getLogger(__name__)

    logger.info("Logging has started!")
    try:
        x = 1 / 0  # This will cause an error
    except Exception as e:
        logger.error(f"An error occurred: {e}")
