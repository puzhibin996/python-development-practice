from myExceptionHandler import ExceptionHandler
from myCustomException import CustomException, ConnectionError, InvalidInputError,TimeoutError


def handle_invalid_input(exception):
    print(f"Handling invalid input: {exception}")

def handle_connection_error(exception):
    print(f"Handling connection error: {exception}")

def handle_timeout_error(exception):
    print(f"Handling timeout error: {exception}")

# Create an instance of ExceptionHandler
exception_handler = ExceptionHandler()

# Register exception handlers
exception_handler.register_handler(InvalidInputError, handle_invalid_input)
exception_handler.register_handler(ConnectionError, handle_connection_error)
exception_handler.register_handler(TimeoutError, handle_timeout_error)

# Example usage in code
try:
    raise InvalidInputError("The input value is not valid")
except CustomException as e:
    exception_handler.handle_exception(e)

try:
    raise ConnectionError("Unable to connect to the server")
except CustomException as e:
    exception_handler.handle_exception(e)

try:
    raise TimeoutError("The request timed out")
except CustomException as e:
    exception_handler.handle_exception(e)

try:
    raise CustomException("A general custom exception")
except CustomException as e:
    exception_handler.handle_exception(e)
