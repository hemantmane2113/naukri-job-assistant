"""Shared test setup."""

from __future__ import annotations

import subprocess

import pytest
from sqlalchemy import event
from sqlalchemy.engine import Engine


@pytest.fixture(autouse=True)
def _never_touch_the_real_task_scheduler(monkeypatch):
    """A test must never ask the real Windows Task Scheduler anything, and above all never START the real phone listener.
    Tests that exercise orchestration/phone_control.py replace this with their own fake."""
    from naukri_agent.orchestration import phone_control

    def refuse(args):
        return subprocess.CompletedProcess(["schtasks", *args], returncode=1, stdout="", stderr="blocked in tests")

    monkeypatch.setattr(phone_control, "_run_schtasks", refuse)


@pytest.fixture(autouse=True)
def _close_the_sqlite_connections_a_test_opened():
    """Many tests build their own engine and never dispose it. Python 3.13+ then warns "unclosed database" when the
    connection is garbage-collected (hundreds of warnings per run). Close every SQLite connection a test opened, at its end."""
    opened = []

    def remember(dbapi_connection, _connection_record):
        opened.append(dbapi_connection)

    event.listen(Engine, "connect", remember)
    yield
    event.remove(Engine, "connect", remember)
    for connection in opened:
        try:
            connection.close()
        except Exception:  # noqa: BLE001 - already closed, or opened on another thread; nothing more to do
            pass
