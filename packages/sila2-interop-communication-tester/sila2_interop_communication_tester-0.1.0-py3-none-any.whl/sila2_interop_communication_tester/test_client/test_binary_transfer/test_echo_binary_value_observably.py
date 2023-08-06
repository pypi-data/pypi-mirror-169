import time
import uuid
from datetime import datetime

from sila2_interop_communication_tester.grpc_stubs.BinaryTransferTest_pb2 import EchoBinariesObservably_Parameters
from sila2_interop_communication_tester.grpc_stubs.SiLAFramework_pb2 import Binary, CommandExecutionUUID, ExecutionInfo
from sila2_interop_communication_tester.helpers.utils import string_is_uuid
from sila2_interop_communication_tester.test_client.helpers.binary_transfer import download_binary, upload_binary
from sila2_interop_communication_tester.test_client.helpers.error_handling import (
    raises_command_execution_not_finished_error,
    raises_invalid_command_execution_uuid_error,
    raises_validation_error,
)


def test_echo_binary_value_observably_rejects_empty_binary_message(
    binarytransfertest_stub,
):
    with raises_validation_error(
        "org.silastandard/test/BinaryTransferTest/v1/Command/EchoBinariesObservably/Parameter/Binaries"
    ):
        binarytransfertest_stub.EchoBinariesObservably(EchoBinariesObservably_Parameters(Binaries=[Binary()]))


def test_echo_binary_value_observably_rejects_invalid_binary_uuid_strings(
    binarytransfertest_stub,
):
    with raises_validation_error(
        "org.silastandard/test/BinaryTransferTest/v1/Command/EchoBinariesObservably/Parameter/Binaries"
    ):
        binarytransfertest_stub.EchoBinariesObservably(
            EchoBinariesObservably_Parameters(Binaries=[Binary(binaryTransferUUID="abc")])
        )


def test_echo_binaries_observably_rejects_unknown_binary_uuids(binarytransfertest_stub):
    with raises_validation_error(
        "org.silastandard/test/BinaryTransferTest/v1/Command/EchoBinariesObservably/Parameter/Binaries"
    ):
        binarytransfertest_stub.EchoBinariesObservably(
            EchoBinariesObservably_Parameters(Binaries=[Binary(binaryTransferUUID=str(uuid.uuid4()))])
        )


def test_echo_binaries_observably_info_rejects_empty_parameter(binarytransfertest_stub):
    info_stream = binarytransfertest_stub.EchoBinariesObservably_Info(CommandExecutionUUID())
    with raises_invalid_command_execution_uuid_error():
        next(info_stream)


def test_echo_binaries_observably_info_rejects_invalid_uuid_strings(
    binarytransfertest_stub,
):
    info_stream = binarytransfertest_stub.EchoBinariesObservably_Info(CommandExecutionUUID(value="abc"))
    with raises_invalid_command_execution_uuid_error():
        next(info_stream)


def test_echo_binaries_observably_info_rejects_unknown_uuids(binarytransfertest_stub):
    info_stream = binarytransfertest_stub.EchoBinariesObservably_Info(CommandExecutionUUID(value=str(uuid.uuid4())))
    with raises_invalid_command_execution_uuid_error():
        next(info_stream)


def test_echo_binaries_observably_intermediate_rejects_empty_parameter(
    binarytransfertest_stub,
):
    intermediate_stream = binarytransfertest_stub.EchoBinariesObservably_Intermediate(CommandExecutionUUID())
    with raises_invalid_command_execution_uuid_error():
        next(intermediate_stream)


def test_echo_binaries_observably_intermediate_rejects_invalid_uuid_strings(
    binarytransfertest_stub,
):
    intermediate_stream = binarytransfertest_stub.EchoBinariesObservably_Intermediate(CommandExecutionUUID(value="abc"))
    with raises_invalid_command_execution_uuid_error():
        next(intermediate_stream)


def test_echo_binaries_observably_intermediate_rejects_unknown_uuids(
    binarytransfertest_stub,
):
    intermediate_stream = binarytransfertest_stub.EchoBinariesObservably_Intermediate(
        CommandExecutionUUID(value=str(uuid.uuid4()))
    )
    with raises_invalid_command_execution_uuid_error():
        next(intermediate_stream)


def test_echo_binaries_observably_result_rejects_empty_parameter(
    binarytransfertest_stub,
):
    with raises_invalid_command_execution_uuid_error():
        binarytransfertest_stub.EchoBinariesObservably_Result(CommandExecutionUUID())


def test_echo_binaries_observably_result_rejects_invalid_uuid_strings(
    binarytransfertest_stub,
):
    with raises_invalid_command_execution_uuid_error():
        binarytransfertest_stub.EchoBinariesObservably_Result(CommandExecutionUUID(value="abc"))


def test_echo_binaries_observably_result_rejects_unknown_uuids(binarytransfertest_stub):
    with raises_invalid_command_execution_uuid_error():
        binarytransfertest_stub.EchoBinariesObservably_Result(CommandExecutionUUID(value=str(uuid.uuid4())))


def test_echo_binaries_observably_returns_valid_uuid_string(binarytransfertest_stub):
    info = binarytransfertest_stub.EchoBinariesObservably(
        EchoBinariesObservably_Parameters(Binaries=[Binary(value=b"abc"), Binary(value=b"def")])
    )
    assert string_is_uuid(info.commandExecutionUUID.value)


def test_echo_binaries_observably_result_throws_if_not_finished(
    binarytransfertest_stub,
):
    info = binarytransfertest_stub.EchoBinariesObservably(
        EchoBinariesObservably_Parameters(Binaries=[Binary(value=b"abc"), Binary(value=b"def")])
    )

    with raises_command_execution_not_finished_error():
        binarytransfertest_stub.EchoBinariesObservably_Result(info.commandExecutionUUID)


def test_echo_binaries_observably_info_works_after_command_finished(
    binarytransfertest_stub,
):
    info = binarytransfertest_stub.EchoBinariesObservably(
        EchoBinariesObservably_Parameters(Binaries=[Binary(value=b"def")])
    )
    time.sleep(2)
    info_stream = binarytransfertest_stub.EchoBinariesObservably_Info(info.commandExecutionUUID)
    infos = list(info_stream)
    assert infos, "EchoBinariesObservably_Info did not send any responses when subscribing after command finished"
    assert all(
        info.commandStatus == ExecutionInfo.CommandStatus.finishedSuccessfully for info in infos
    ), "EchoBinariesObservably_Info reported other status than finishedSuccessfully after command finished"


def test_echo_binaries_observably_intermediate_works_after_command_finished(
    binarytransfertest_stub,
):
    info = binarytransfertest_stub.EchoBinariesObservably(
        EchoBinariesObservably_Parameters(Binaries=[Binary(value=b"def")])
    )
    time.sleep(2)
    intermediate_stream = binarytransfertest_stub.EchoBinariesObservably_Intermediate(info.commandExecutionUUID)
    intermediates = list(intermediate_stream)
    assert len(intermediates) <= 1, (
        "EchoBinariesObservably_Intermediate returned multiple intermediate responses "
        "upon subscription after command finished. Expected either none, or the last one."
    )


def test_echo_binaries_observably_works(binarytransfertest_stub, binary_upload_stub, binary_download_stub):
    # upload parameter
    large_binary_id = upload_binary(
        binary_upload_stub,
        b"abc" * 1_000_000,
        "org.silastandard/test/BinaryTransferTest/v1/Command/EchoBinariesObservably/Parameter/Binaries",
    )

    # initialize command
    start_timestamp = datetime.now()
    info = binarytransfertest_stub.EchoBinariesObservably(
        EchoBinariesObservably_Parameters(
            Binaries=[
                Binary(value=b"abc"),
                Binary(binaryTransferUUID=str(large_binary_id)),
                Binary(value=b"SiLA2_Test_String_Value"),
            ]
        )
    )

    # subscribe to streams
    info_stream = binarytransfertest_stub.EchoBinariesObservably_Info(info.commandExecutionUUID)
    intermediate_stream = binarytransfertest_stub.EchoBinariesObservably_Intermediate(info.commandExecutionUUID)

    # stream consumption blocks until stream ends
    infos = list(info_stream)
    intermediates = list(intermediate_stream)
    end_timestamp = datetime.now()

    assert (
        2 < (end_timestamp - start_timestamp).total_seconds() < 5
    ), "EchoBinariesObservably with 3 parameters took <2 or >5 seconds"

    # check result
    result_message = binarytransfertest_stub.EchoBinariesObservably_Result(info.commandExecutionUUID)
    result_binary = download_binary(binary_download_stub, uuid.UUID(result_message.JointBinary.binaryTransferUUID))
    assert result_binary == b"abc" * 1_000_001 + b"SiLA2_Test_String_Value"

    # check infos
    assert infos, "EchoBinariesObservably did not yield any ExecutionInfos"
    assert infos[-1].commandStatus == ExecutionInfo.CommandStatus.finishedSuccessfully
    assert infos[0].commandStatus in (ExecutionInfo.CommandStatus.waiting, ExecutionInfo.CommandStatus.running)

    # check intermediates
    assert len(intermediates) == 3, (
        f"EchoBinariesObservably with 3 parameters yielded {len(intermediates)} intermediate responses "
        f"when subscription started immediately after command initiation. Expected 3."
    )
    assert intermediates[0].Binary.value == b"abc", "First intermediate response was not 'abc'"
    assert (
        download_binary(binary_download_stub, uuid.UUID(intermediates[1].Binary.binaryTransferUUID))
        == b"abc" * 1_000_000
    ), "Second intermediate response was not 'abc' repeated 1,000,000 times"
    assert (
        intermediates[2].Binary.value == b"SiLA2_Test_String_Value"
    ), "Third intermediate response was not 'SiLA2_Test_String_Value'"
