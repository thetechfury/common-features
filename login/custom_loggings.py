import os
from logging.handlers import RotatingFileHandler
from datetime import datetime


class TimestampedRotatingFileHandler(RotatingFileHandler):
    def doRollover(self):
        super().doRollover()
        if self.backupCount > 0:
            timestamp = datetime.now().strftime('%Y%m%d%H%M%S')
            if os.path.exists(self.baseFilename + ".1"):
                new_filename = f"{self.baseFilename}.{timestamp}"
                os.rename(self.baseFilename + ".1", new_filename)
