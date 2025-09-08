from pytest import fixture
import sys
sys.path.insert(0, ".\\src")
from patapon.filedata.p1.param import GameParam
from patapon.filedata.p1.param.gameparam import (
    GameParamHeader,
    GameParamInfoElement
)
from patapon.filedata.p1.param.generic import (
    GenericParamHeaderPartitionInfo
)


@fixture
def game_param_element() -> GameParamInfoElement:
    return GameParamInfoElement(
        b'ThisGameIsLabo\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00'.decode(),
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    )


@fixture
def game_param_header() -> GameParamHeader:
    return GameParamHeader(
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
    assert GameParam.verify_datafield_pos()


def test_get_byte_size(
        game_param_header: GameParamHeader,
        game_param_element: GameParamInfoElement
        ):
    assert game_param_header.get_byte_size() == 0x40
    assert game_param_element.get_byte_size() == 0x80


def test_from_bytes_effect_param(
        game_param_header: GameParamHeader,
        game_param_element: GameParamInfoElement
        ):
    file_name = "D:\\Patapon\\Patapon Stuff\\Patapon 1 US\\@DATA_CMN\\loadinggroup\\@systemdata\\@default\\@loadinggroupcmn\\@paramlist\\gameparam.dat"
    with open(file_name, "rb") as file:
        raw = file.read()
        actual: GameParam = GameParam.from_bytes(raw)
        assert GameParam.verify_filler(actual)

    assert actual.header.get_byte_size() == 0x40
    assert actual.header == game_param_header

    assert len(actual.game_params.param_list) == 0x1
    assert actual.game_params.param_list[0].get_byte_size() == 0x80
    assert actual.game_params.param_list[0] == game_param_element