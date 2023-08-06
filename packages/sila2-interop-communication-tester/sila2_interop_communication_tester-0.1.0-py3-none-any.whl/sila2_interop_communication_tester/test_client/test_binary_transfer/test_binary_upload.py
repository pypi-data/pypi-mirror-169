import uuid

from sila2_interop_communication_tester.grpc_stubs.BinaryTransferTest_pb2 import EchoBinaryValue_Parameters
from sila2_interop_communication_tester.grpc_stubs.SiLABinaryTransfer_pb2 import (
    CreateBinaryRequest,
    DeleteBinaryRequest,
    UploadChunkRequest,
)
from sila2_interop_communication_tester.grpc_stubs.SiLAFramework_pb2 import Binary
from sila2_interop_communication_tester.test_client.helpers.binary_transfer import download_binary, upload_binary
from sila2_interop_communication_tester.test_client.helpers.error_handling import (
    raises_binary_upload_failed_error,
    raises_invalid_binary_transfer_uuid_error,
    raises_validation_error,
)


def test_create_binary_fails_on_non_fully_qualified_parameter_identifier(binary_upload_stub):
    with raises_binary_upload_failed_error():
        binary_upload_stub.CreateBinary(
            CreateBinaryRequest(binarySize=3 * 1024 * 1024, chunkCount=3, parameterIdentifier="Binaries")
        )


def test_create_binary_fails_on_unknown_parameter_identifier(binary_upload_stub):
    with raises_binary_upload_failed_error():
        binary_upload_stub.CreateBinary(
            CreateBinaryRequest(
                binarySize=3 * 1024 * 1024,
                chunkCount=3,
                parameterIdentifier="com.example/unknown/SomeFeature/v1/Command/SomeCommand/Parameter/SomeParameter",
            )
        )


def test_create_binary_fails_on_non_binary_parameter_identifier(binary_upload_stub):
    with raises_binary_upload_failed_error():
        binary_upload_stub.CreateBinary(
            CreateBinaryRequest(
                binarySize=3 * 1024 * 1024,
                chunkCount=3,
                parameterIdentifier="org.silastandard/core/SiLAService/v1/Command/SetServerName/Parameter/ServerName",
            )
        )


def test_create_binary_fails_on_parameter_identifier_with_additional_characters(binary_upload_stub):
    with raises_binary_upload_failed_error():
        binary_upload_stub.CreateBinary(
            CreateBinaryRequest(
                binarySize=3 * 1024 * 1024,
                chunkCount=3,
                parameterIdentifier=(
                    "this is some text and an identifier:"
                    "org.silastandard/core/SiLAService/v1/Command/SetServerName/Parameter/ServerName"
                ),
            )
        )


def test_upload_chunk_rejects_non_uuid_strings(binary_upload_stub):
    call = binary_upload_stub.UploadChunk(
        (UploadChunkRequest(chunkIndex=i, binaryTransferUUID="abc", payload=b"abc") for i in range(2))
    )
    with raises_invalid_binary_transfer_uuid_error():
        next(call)


def test_upload_chunk_rejects_unknown_uuids(binary_upload_stub):
    call = binary_upload_stub.UploadChunk(
        (UploadChunkRequest(chunkIndex=i, binaryTransferUUID=str(uuid.uuid4()), payload=b"abc") for i in range(2))
    )
    with raises_invalid_binary_transfer_uuid_error():
        next(call)


def test_upload_chunk_rejects_too_large_chunk_indices(binary_upload_stub):
    """Server expects 2 chunks with 4 MB combined payload, client sends 2 2 MB chunks with indices 0 and 2"""
    info = binary_upload_stub.CreateBinary(
        CreateBinaryRequest(
            binarySize=4 * 1024 * 1024,
            chunkCount=2,
            parameterIdentifier="org.silastandard/test/BinaryTransferTest/v1/Command/EchoBinaryValue/Parameter/BinaryValue",
        )
    )
    call = binary_upload_stub.UploadChunk(
        (
            UploadChunkRequest(chunkIndex=i, binaryTransferUUID=info.binaryTransferUUID, payload=b"a" * 2 * 1024 * 1024)
            for i in [0, 2]
        )
    )
    next(call)
    with raises_binary_upload_failed_error():
        next(call)


def test_upload_chunk_rejects_too_many_uploaded_bytes(binary_upload_stub):
    """Server expects 3 chunks with 3 MB combined payload, receives 3 chunks with 2 MB payload each"""
    info = binary_upload_stub.CreateBinary(
        CreateBinaryRequest(
            binarySize=3 * 1024 * 1024,
            chunkCount=3,
            parameterIdentifier="org.silastandard/test/BinaryTransferTest/v1/Command/EchoBinaryValue/Parameter/BinaryValue",
        )
    )
    call = binary_upload_stub.UploadChunk(
        (
            UploadChunkRequest(chunkIndex=i, binaryTransferUUID=info.binaryTransferUUID, payload=b"a" * 2 * 1024 * 1024)
            for i in range(3)
        )
    )
    next(call)
    with raises_binary_upload_failed_error():
        next(call)


def test_upload_chunk_rejects_too_few_uploaded_bytes(binary_upload_stub):
    """Server expects 3 chunks with 3 MB combined payload, receives 3 chunks with less MB"""
    info = binary_upload_stub.CreateBinary(
        CreateBinaryRequest(
            binarySize=3 * 1024 * 1024,
            chunkCount=3,
            parameterIdentifier=(
                "org.silastandard/test/BinaryTransferTest/v1/Command/EchoBinaryValue/Parameter/BinaryValue"
            ),
        )
    )
    call = binary_upload_stub.UploadChunk(
        (UploadChunkRequest(chunkIndex=i, binaryTransferUUID=info.binaryTransferUUID, payload=b"abc") for i in range(3))
    )
    with raises_binary_upload_failed_error():
        list(call)


def test_server_handles_multiple_sequential_uploadchunk_streams_for_same_binary(
    binary_upload_stub, binary_download_stub, binarytransfertest_stub
):
    # announce upload of 3 MB in 3 chunks
    info = binary_upload_stub.CreateBinary(
        CreateBinaryRequest(
            binarySize=3 * 1024 * 1024,
            chunkCount=3,
            parameterIdentifier=(
                "org.silastandard/test/BinaryTransferTest/v1/Command/EchoBinaryValue/Parameter/BinaryValue"
            ),
        )
    )

    # upload the three chunks in three separate RPC calls
    requests = [
        UploadChunkRequest(chunkIndex=i, binaryTransferUUID=info.binaryTransferUUID, payload=b"a" * 1024 * 1024)
        for i in range(3)
    ]
    for i in range(3):
        next(binary_upload_stub.UploadChunk(iter((requests[i],))))

    # use binary
    response = binarytransfertest_stub.EchoBinaryValue(
        EchoBinaryValue_Parameters(BinaryValue=Binary(binaryTransferUUID=info.binaryTransferUUID))
    )
    assert (
        download_binary(binary_download_stub, uuid.UUID(response.ReceivedValue.binaryTransferUUID))
        == b"a" * 3 * 1024 * 1024
    )


def test_server_rejects_use_of_incompletely_uploaded_binary(binary_upload_stub, binarytransfertest_stub):
    # announce upload of 3 MB in 3 chunks
    info = binary_upload_stub.CreateBinary(
        CreateBinaryRequest(
            binarySize=3 * 1024 * 1024,
            chunkCount=3,
            parameterIdentifier=(
                "org.silastandard/test/BinaryTransferTest/v1/Command/EchoBinaryValue/Parameter/BinaryValue"
            ),
        )
    )

    # upload 2 chunks of 1 MB each
    call = binary_upload_stub.UploadChunk(
        (
            UploadChunkRequest(chunkIndex=i, binaryTransferUUID=info.binaryTransferUUID, payload=b"a" * 1024 * 1024)
            for i in range(2)
        )
    )
    list(call)

    # try to use incompletely uploaded binary
    with raises_validation_error(
        "org.silastandard/test/BinaryTransferTest/v1/Command/EchoBinaryValue/Parameter/BinaryValue"
    ):
        binarytransfertest_stub.EchoBinaryValue(
            EchoBinaryValue_Parameters(BinaryValue=Binary(binaryTransferUUID=info.binaryTransferUUID))
        )


def test_delete_binary_rejects_non_uuid_strings(binary_upload_stub):
    with raises_invalid_binary_transfer_uuid_error():
        binary_upload_stub.DeleteBinary(DeleteBinaryRequest(binaryTransferUUID="abc"))


def test_delete_binary_rejects_unknown_uuids(binary_upload_stub):
    with raises_invalid_binary_transfer_uuid_error():
        binary_upload_stub.DeleteBinary(DeleteBinaryRequest(binaryTransferUUID=str(uuid.uuid4())))


def test_server_rejects_usage_of_deleted_binary(binary_upload_stub, binarytransfertest_stub):
    upload_id = upload_binary(
        binary_upload_stub,
        b"abc" * 1_000_000,
        "org.silastandard/test/BinaryTransferTest/v1/Command/EchoBinaryValue/Parameter/BinaryValue",
    )
    binary_upload_stub.DeleteBinary(DeleteBinaryRequest(binaryTransferUUID=str(upload_id)))

    with raises_validation_error(
        "org.silastandard/test/BinaryTransferTest/v1/Command/EchoBinaryValue/Parameter/BinaryValue"
    ):
        binarytransfertest_stub.EchoBinaryValue(
            EchoBinaryValue_Parameters(BinaryValue=Binary(binaryTransferUUID=str(upload_id)))
        )


def test_upload_chunk_for_fully_upload_binary_after_use(binary_upload_stub, binarytransfertest_stub):
    upload_id = upload_binary(
        binary_upload_stub,
        b"abc" * 1_000_000,
        "org.silastandard/test/BinaryTransferTest/v1/Command/EchoBinaryValue/Parameter/BinaryValue",
    )

    binarytransfertest_stub.EchoBinaryValue(
        EchoBinaryValue_Parameters(BinaryValue=Binary(binaryTransferUUID=str(upload_id)))
    )

    request = UploadChunkRequest(chunkIndex=0, binaryTransferUUID=str(upload_id), payload=b"a" * 1024**2)
    with raises_binary_upload_failed_error():
        next(binary_upload_stub.UploadChunk(iter((request,))))
