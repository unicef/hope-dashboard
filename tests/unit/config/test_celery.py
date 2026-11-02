import pytest


def test_celery() -> None:
    try:
        from hope_dashboard.config.celery import app

        assert app.clock
    except ImportError as e:
        pytest.fail(getattr(e, "message", "unknown error"))


def test_init_celery() -> None:
    try:
        from hope_dashboard.config.celery import init_sentry

        init_sentry()
    except ImportError as e:
        pytest.fail(getattr(e, "message", "unknown error"))
