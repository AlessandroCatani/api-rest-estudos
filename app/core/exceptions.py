class AppError(Exception):
    code = "APP_ERROR"
    status_code = 400

    def __init__(self, message: str):
        self.message = message
        super().__init__(message)


class NotFoundError(AppError):
    code = "NOT_FOUND"
    status_code = 404


class UnauthorizedError(AppError):
    code = "UNAUTHORIZED"
    status_code = 401


class ConflictError(AppError):
    code = "CONFLICT"
    status_code = 409


class BusinessRuleError(AppError):
    code = "BUSINESS_RULE_ERROR"
    status_code = 400
