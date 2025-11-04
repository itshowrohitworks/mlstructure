import sys
import logging
from logger import LOG_FILE_PATH
from types import ModuleType

logger = logging.getLogger(__name__)

def error_message_detail(error: Exception, error_detail: ModuleType):
    _, _, exc_tb = error_detail.exc_info()
    if exc_tb is not None:
        file_name = exc_tb.tb_frame.f_code.co_filename
        line_no = exc_tb.tb_lineno
        return f"Error in script '{file_name}' at line {line_no}: {str(error)}"
    else:
        return f"Error Message: {str(error)} (no traceback)"

class CustomException(Exception):
    def __init__(self, error_message, error_detail: ModuleType):
        super().__init__(error_message)
        self.error_message = error_message_detail(error_message, error_detail)
        logger.error(self.error_message, exc_info=True)

    def __str__(self):
        return self.error_message