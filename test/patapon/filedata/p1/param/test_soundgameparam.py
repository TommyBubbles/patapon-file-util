from pytest import fixture
import sys
sys.path.insert(0, ".\\src")
from patapon.filedata.p1.param import SoundGameParam
from patapon.filedata.p1.param.soundgameparam import (
    SoundGameParamHeader,
    SoundGameParamInfoElement
)
from patapon.filedata.p1.param.generic import (
    GenericParamHeaderPartitionInfo
)
from patapon.filedata.patapon_data_class import PataponDataIO



@fixture
def sound_game_param_header() -> SoundGameParamHeader:
    return SoundGameParamHeader(
        b'YGF_GFP\x00',
        0x40,
        0.800000011920929,
        0x1,
        [0,0,0],
        [
            GenericParamHeaderPartitionInfo(0x6, 0x64)
        ],
        b'\x00\x00\x00\x00' * 6
    )


@fixture
def sound_game_param_last_element() -> SoundGameParamInfoElement:
    return SoundGameParamInfoElement(
        b'\x8a\xe2\x82\xcc\x89\xb9\x97V\x82\xd1\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00'.decode("shift-jis"),
        5,
        b'soundgame/soundgame_rock.bnd\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00'.decode(),
    )



def test_verify_datafield_pos():
    assert SoundGameParam.verify_datafield_pos()


def test_get_byte_size(
        sound_game_param_header: SoundGameParamHeader,
        sound_game_param_last_element: SoundGameParamInfoElement
        ):
    assert sound_game_param_header.get_byte_size() == 0x40
    assert sound_game_param_last_element.get_byte_size() == 0x64


def test_from_bytes(
        sound_game_param_header: SoundGameParamHeader,
        sound_game_param_last_element: SoundGameParamInfoElement
        ):
    file_name = "D:\\Patapon\\Patapon Stuff\\Patapon 1 US\\@DATA_CMN\\loadinggroup\\@systemdata\\@default\\@loadinggroupcmn\\@paramlist\\soundgameparam.dat"
    with open(file_name, "rb") as file:
        raw = file.read()
        data_stream = PataponDataIO(raw)
        actual: SoundGameParam = SoundGameParam.from_bytes(data_stream)
        assert SoundGameParam.verify_filler(actual)

    assert actual.get_byte_size() == 0x298

    assert actual.header.get_byte_size() == 0x40
    assert actual.header == sound_game_param_header

    assert len(actual.sound_game_params.param_list) == 0x6
    assert actual.sound_game_params.param_list[-1].get_byte_size() == 0x64
    assert actual.sound_game_params.param_list[-1] == sound_game_param_last_element
