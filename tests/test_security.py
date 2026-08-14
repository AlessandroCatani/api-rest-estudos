from app.core.security import (
    create_access_token,
    decode_access_token,
    hash_password,
    verify_password,
)


def test_hash_and_verify_password():
    hashed = hash_password("mysecret123")
    assert hashed != "mysecret123"
    assert verify_password("mysecret123", hashed) is True
    assert verify_password("wrongpass", hashed) is False


def test_create_and_decode_access_token():
    token = create_access_token(subject="42")
    assert decode_access_token(token) == "42"


def test_decode_invalid_token_returns_none():
    assert decode_access_token("not-a-real-token") is None
