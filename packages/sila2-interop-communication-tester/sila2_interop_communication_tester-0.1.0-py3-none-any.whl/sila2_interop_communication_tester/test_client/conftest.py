"""Pytest configuration file"""

import grpc
import pytest

from sila2_interop_communication_tester.grpc_stubs.SiLABinaryTransfer_pb2_grpc import (
    BinaryDownloadStub,
    BinaryUploadStub,
)
from sila2_interop_communication_tester.helpers.pytest_reporter import NotTruncatingTerminalReporter

# is set in __main__.py
CHANNEL: grpc.Channel = grpc.insecure_channel("127.0.0.1:50052")


@pytest.fixture(scope="session")
def channel() -> grpc.Channel:
    return CHANNEL  # noqa: F821


@pytest.fixture(scope="session")
def binary_download_stub(channel) -> BinaryDownloadStub:
    return BinaryDownloadStub(channel)


@pytest.fixture(scope="session")
def binary_upload_stub(channel) -> BinaryUploadStub:
    return BinaryUploadStub(channel)


@pytest.mark.trylast
def pytest_configure(config):
    vanilla_reporter = config.pluginmanager.getplugin("terminalreporter")
    my_reporter = NotTruncatingTerminalReporter(config)
    config.pluginmanager.unregister(vanilla_reporter)
    config.pluginmanager.register(my_reporter, "terminalreporter")
