from myCustomException import CustomException

class ExceptionHandler:
    def __init__(self):
        self.handlers = {}

    def register_handler(self, exception_class, handler):
        """Register a handler for a specific exception class"""
        if not issubclass(exception_class, CustomException):
            raise ValueError("Handler can only be registered for CustomException subclasses")
        self.handlers[exception_class] = handler

    def handle_exception(self, exception):
        """Handle the exception using the registered handler"""
        exception_class = type(exception)
        handler = self.handlers.get(exception_class)
        if handler:
            handler(exception)
        else:
            self.default_handler(exception)

    @staticmethod
    def default_handler(exception):
        """Default exception handler"""
        print(f"Unhandled exception: {exception}")
