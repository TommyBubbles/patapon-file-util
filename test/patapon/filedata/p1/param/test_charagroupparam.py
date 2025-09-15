from pytest import fixture
import sys
sys.path.insert(0, ".\\src")
from patapon.filedata.p1.param import CharaGroupParam
from patapon.filedata.p1.param.charagroupparam import (
    CharaGroupParamHeader,
    CharaGroupParamHeader,
    CharaGroupParamInfoElement
)
from patapon.filedata.p1.param.generic import (
     GenericParamHeaderPartitionInfo
)


@fixture
def chara_group_param_header() -> CharaGroupParamHeader:
    return CharaGroupParamHeader(
        b'YGF_GFP\x00'.decode(),
        0x40,
        0.800000011920929,
        0x1,
        [0,0,0],
        [
            GenericParamHeaderPartitionInfo(0xC, 0x80)
        ],
        b'\x00\x00\x00\x00' * 6
    )


@fixture
def chara_group_param_last_element() -> CharaGroupParamInfoElement:
    return CharaGroupParamInfoElement(
        b'11\x81F\x93K\x93\x96\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00'.decode("shift-jis"),
        11,
        11,
        [0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    )



def test_verify_datafield_pos():
    assert CharaGroupParam.verify_datafield_pos()


def test_get_byte_size(
        chara_group_param_header: CharaGroupParamHeader,
        chara_group_param_last_element: CharaGroupParamInfoElement
        ):
    assert chara_group_param_header.get_byte_size() == 0x40
    assert chara_group_param_last_element.get_byte_size() == 0x80


def test_from_bytes(
        chara_group_param_header: CharaGroupParamHeader,
        chara_group_param_last_element: CharaGroupParamInfoElement
        ):
    file_name = "D:\\Patapon\\Patapon Stuff\\Patapon 1 US\\@DATA_CMN\\loadinggroup\\@systemdata\\@default\\@loadinggroupcmn\\@paramlist\\charagroupparam.dat"
    with open(file_name, "rb") as file:
        raw = file.read()
        actual: CharaGroupParam = CharaGroupParam.from_bytes(raw)
        assert CharaGroupParam.verify_filler(actual)

    assert actual.get_byte_size() == 0x640

    assert actual.header.get_byte_size() == 0x40
    assert actual.header == chara_group_param_header

    assert len(actual.chara_group_params.param_list) == 0xC
    assert actual.chara_group_params.param_list[-1].get_byte_size() == 0x80
    assert actual.chara_group_params.param_list[-1] == chara_group_param_last_element