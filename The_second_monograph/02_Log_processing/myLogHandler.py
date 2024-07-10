import logging
import os
from logging.handlers import RotatingFileHandler

class LogHandler:
    def __init__(self, log_dir='logs', log_file='app.log', level=logging.INFO, max_bytes=10*1024*1024, backup_count=5):
        self.log_dir = log_dir
        self.log_file = log_file
        self.level = level
        self.max_bytes = max_bytes
        self.backup_count = backup_count

        self.logger = logging.getLogger(__name__)
        self.logger.setLevel(self.level)

        self._create_log_dir()
        self._configure_logger()

    def _create_log_dir(self):
        if not os.path.exists(self.log_dir):
            os.makedirs(self.log_dir)

    def _configure_logger(self):
        log_path = os.path.join(self.log_dir, self.log_file)

        # File handler with rotation
        file_handler = RotatingFileHandler(log_path, maxBytes=self.max_bytes, backupCount=self.backup_count)
        file_handler.setLevel(self.level)

        # Console handler
        console_handler = logging.StreamHandler()
        console_handler.setLevel(self.level)

        # Formatter
        formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
        file_handler.setFormatter(formatter)
        console_handler.setFormatter(formatter)

        # Adding handlers to the logger
        self.logger.addHandler(file_handler)
        self.logger.addHandler(console_handler)

    def get_logger(self):
        return self.logger
