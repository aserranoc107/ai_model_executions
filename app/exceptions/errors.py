class AppError(Exception):
    def __init__(self, message: str):
        self.message = message
        super().__init__(message)

class DataServiceError(AppError):
    pass

class ExternalServiceError(AppError):
    pass

class LogicServiceError(AppError):
    pass

class LLMServiceError(AppError):
    pass