from app.exception.error_code import ErrorCode

class CustomException(Exception):
    def __init__(self, message: str, error_code: ErrorCode):
        self.error_code = error_code
        self.message = message
        super().__init__(f"[{error_code.value}] {message}")
