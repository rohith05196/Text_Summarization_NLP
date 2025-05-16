import logging
import sys
import os

loggig_str = "[%(asctime)s: %(levelname)s:  %(module)s:  %(message)s]"

log_dir = "logs"

log_path = os.path.join(log_dir, "log_report.log")

os.makedirs(log_dir, exist_ok=True)

logging.basicConfig(
    level=logging.INFO, 
    format=loggig_str,
    handlers=[
        logging.StreamHandler(sys.stdout),
        logging.FileHandler(log_path) 
    ])

logger = logging.getLogger("TextSummarizer")