from pytest import fixture
import sys
sys.path.insert(0, ".\\src")
from patapon.filedata.p1.param import CharaGroupParam
from patapon.filedata.p1.param.charagroupparam import (
    CharaGroupParamHeader,
    CharaGroupParamInfoElement
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



def test_verify_datafield_pos_chara_group_param():
    assert CharaGroupParam.verify_datafield_pos()


def test_get_byte_size():
    assert CharaGroupParamHeader().get_byte_size() == 0x40
    assert CharaGroupParamInfoElement().get_byte_size() == 0x80


def test_from_bytes_carnival_param(
        chara_group_param_last_element: CharaGroupParamInfoElement):
    file_name = "D:\\Patapon\\Patapon Stuff\\Patapon 1 US\\@DATA_CMN\\loadinggroup\\@systemdata\\@default\\@loadinggroupcmn\\@paramlist\\charagroupparam.dat"
    with open(file_name, "rb") as file:
        raw = file.read()
        actual: CharaGroupParam = CharaGroupParam.from_bytes(raw)
        assert CharaGroupParam.verify_filler(actual)

    assert len(actual.chara_group_params.param_list) == 0xC
    assert actual.chara_group_params.param_list[-1] == chara_group_param_last_element