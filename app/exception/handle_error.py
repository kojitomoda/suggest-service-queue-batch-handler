from typing import Callable
from app.exception.custom_exception import CustomException, ErrorCode


class HandleError:
    def __init__(self)-> None:
        self.handlers: dict[ErrorCode, Callable[[CustomException], None]] = {
            ErrorCode.PROXY_CONNECTION_ERROR: self._handle_proxy_connection_error,
            ErrorCode.PROXY_RESTRICTED: self._handle_proxy_restricted,
            ErrorCode.INVALID_PROXY_SERVER_CREDENTIALS: self._handle_invalid_proxy_server_credentials,
        }

    def handle_error(self, e: CustomException):
        handler = self.handlers.get(e.error_code, self._handle_default)
        handler(e)

    def _handle_proxy_connection_error(self, e: CustomException):
        pass

    def _handle_proxy_restricted(self, e: CustomException):
        pass

    def _handle_invalid_proxy_server_credentials(self, e: CustomException):
        pass

    def _handle_default(self, e: CustomException):
        pass