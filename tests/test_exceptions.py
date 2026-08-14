from app.core.exceptions import (
    AppError,
    BusinessRuleError,
    ConflictError,
    NotFoundError,
    UnauthorizedError,
)


def test_not_found_error_has_404_and_code():
    err = NotFoundError("Project not found")
    assert isinstance(err, AppError)
    assert err.status_code == 404
    assert err.code == "NOT_FOUND"
    assert err.message == "Project not found"


def test_error_status_codes_and_names():
    assert UnauthorizedError("x").status_code == 401
    assert ConflictError("x").status_code == 409
    assert BusinessRuleError("x").status_code == 400
