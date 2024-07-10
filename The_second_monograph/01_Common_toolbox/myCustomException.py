class CustomException(Exception):
    """Base class for custom exceptions"""
    def __init__(self, message=None):
        self.message = message or "An error occurred"
        super().__init__(self.message)

class InvalidInputError(CustomException):
    """Exception raised for invalid inputs"""
    def __init__(self, message="Invalid input provided"):
        super().__init__(message)

class ConnectionError(CustomException):
    """Exception raised for connection errors"""
    def __init__(self, message="Failed to connect"):
        super().__init__(message)

class TimeoutError(CustomException):
    """Exception raised for operation timeouts"""
    def __init__(self, message="Operation timed out"):
        super().__init__(message)
