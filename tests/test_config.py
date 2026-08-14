from app.core.config import settings


def test_settings_load_from_env():
    assert settings.database_url.startswith("postgresql://")
    assert settings.jwt_algorithm == "HS256"
    assert settings.jwt_expire_minutes > 0
