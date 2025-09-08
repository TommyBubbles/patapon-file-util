from pytest import fixture
import sys
sys.path.insert(0, ".\\src")
from patapon.filedata.p1.param import LaboParam
from patapon.filedata.p1.param.laboparam import (
    LaboParamHeader,
    LaboParamInfoElement
)
from patapon.filedata.p1.param.generic import (
    GenericParamHeaderPartitionInfo
)


@fixture
def labo_param_element() -> LaboParamInfoElement:
    return LaboParamInfoElement(
        b'ThisGameIsLabo\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00'.decode(),
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    )


@fixture
def labo_param_header() -> LaboParamHeader:
    return LaboParamHeader(
        b'YGF_GFP\x00'.decode(),
        0x40,
        0.800000011920929,
        0x1,
        [0,0,0],
        [
            GenericParamHeaderPartitionInfo(0x1, 0x80)
        ],
        b'\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00'
    )


def test_verify_datafield_pos_effect_param():
    assert LaboParam.verify_datafield_pos()


def test_get_byte_size(
        labo_param_element: LaboParamInfoElement,
        labo_param_header: LaboParamHeader
        ):
    assert labo_param_header.get_byte_size() == 0x40
    assert labo_param_element.get_byte_size() == 0x80


def test_from_bytes_effect_param(
        labo_param_element: LaboParamInfoElement,
        labo_param_header: LaboParamHeader
        ):
    file_name = "D:\\Patapon\\Patapon Stuff\\Patapon 1 US\\@DATA_CMN\\loadinggroup\\@systemdata\\@default\\@loadinggroupcmn\\@paramlist\\laboparam.dat"
    with open(file_name, "rb") as file:
        raw = file.read()
        actual: LaboParam = LaboParam.from_bytes(raw)
        assert LaboParam.verify_filler(actual)

    assert actual.header.get_byte_size() == 0x40
    assert actual.header == labo_param_header

    assert len(actual.labo_params.param_list) == 0x1
    assert actual.labo_params.param_list[0].get_byte_size() == 0x80
    assert actual.labo_params.param_list[0] == labo_param_element