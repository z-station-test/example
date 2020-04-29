import os

PROJECT_DIR = os.path.dirname(os.path.dirname(__file__))

LOG_DIR = os.path.join(PROJECT_DIR, 'logs')  # PROJECT_DIR/logs/
LOG_PATH = os.path.join(LOG_DIR, 'main.log')  # PROJECT_DIR/logs/main.log
LOG_FORMAT = '%(asctime)s - %(name)s - %(levelname)s - %(message)s'

DEBUG = True
