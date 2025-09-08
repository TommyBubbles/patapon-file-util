from pytest import fixture
import sys
sys.path.insert(0, ".\\src")
from patapon.filedata.p1.param import MiracleParam
from patapon.filedata.p1.param.miracleparam import (
    MiracleParamHeader,
    MiracleParamInfoElement
)
from patapon.filedata.p1.param.generic import (
    GenericParamHeaderPartitionInfo
)


@fixture
def miracle_param_last_element() -> MiracleParamInfoElement:
    return MiracleParamInfoElement(
        b'MIRACLE_QUAKEx\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00'.decode(),
        3,
        8,
        b'miracle_bgm_04.bnd\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00'.decode(),
    )


@fixture
def miracle_param_header() -> MiracleParamHeader:
    return MiracleParamHeader(
        b'YGF_GFP\x00'.decode(),
        0x40,
        0.800000011920929,
        0x1,
        [0,0,0],
        [
            GenericParamHeaderPartitionInfo(0x4, 0x48)
        ],
        b'\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00'
    )


def test_verify_datafield_pos_effect_param():
    assert MiracleParam.verify_datafield_pos()


def test_get_byte_size(
        miracle_param_last_element: MiracleParamInfoElement,
        miracle_param_header: MiracleParamHeader
        ):
    assert miracle_param_header.get_byte_size() == 0x40
    assert miracle_param_last_element.get_byte_size() == 0x48


def test_from_bytes_effect_param(
        miracle_param_last_element: MiracleParamInfoElement,
        miracle_param_header: MiracleParamHeader
        ):
    file_name = "D:\\Patapon\\Patapon Stuff\\Patapon 1 US\\@DATA_CMN\\loadinggroup\\@systemdata\\@default\\@loadinggroupcmn\\@paramlist\\miracleparam.dat"
    with open(file_name, "rb") as file:
        raw = file.read()
        actual: MiracleParam = MiracleParam.from_bytes(raw)
        assert MiracleParam.verify_filler(actual)

    assert actual.header.get_byte_size() == 0x40
    assert actual.header == miracle_param_header

    assert len(actual.miracle_params.param_list) == 0x4
    assert actual.miracle_params.param_list[-1].get_byte_size() == 0x48
    assert actual.miracle_params.param_list[-1] == miracle_param_last_element