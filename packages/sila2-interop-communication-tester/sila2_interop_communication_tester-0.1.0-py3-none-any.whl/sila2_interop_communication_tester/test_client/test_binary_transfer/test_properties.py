from uuid import UUID

from sila2_interop_communication_tester.grpc_stubs.BinaryTransferTest_pb2 import (
    Get_BinaryValueDirectly_Parameters,
    Get_BinaryValueDownload_Parameters,
)
from sila2_interop_communication_tester.helpers.utils import string_is_uuid
from sila2_interop_communication_tester.test_client.helpers.binary_transfer import download_binary


def test_read_binary_value_directly(binarytransfertest_stub):
    response = binarytransfertest_stub.Get_BinaryValueDirectly(Get_BinaryValueDirectly_Parameters())
    assert response.HasField("BinaryValueDirectly")
    assert response.BinaryValueDirectly.HasField("value")
    assert response.BinaryValueDirectly.value == b"SiLA2_Test_String_Value"


def test_read_binary_value_download(binarytransfertest_stub, binary_download_stub):
    response = binarytransfertest_stub.Get_BinaryValueDownload(Get_BinaryValueDownload_Parameters())
    assert response.HasField("BinaryValueDownload")
    assert response.BinaryValueDownload.HasField("binaryTransferUUID")

    binary_id = response.BinaryValueDownload.binaryTransferUUID
    assert string_is_uuid(binary_id)
    assert (
        download_binary(binary_download_stub, UUID(binary_id))
        == b"A_slightly_longer_SiLA2_Test_String_Value_used_to_demonstrate_the_binary_download" * 100_000
    )
