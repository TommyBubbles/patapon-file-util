from pytest import fixture
import sys
sys.path.insert(0, ".\\src")
from patapon.filedata.p1.param import SoundParam
from patapon.filedata.p1.param.soundparam import (
    SoundParamHeader,
    MoodSettingParamElement,
    AntecedentDefParamElement,
    RuleDefParamElement
)
from patapon.filedata.p1.param.generic import (
    GenericParamHeaderPartitionInfo
)



@fixture
def sound_param_header() -> SoundParamHeader:
    return SoundParamHeader(
        b'YGF_GFP\x00'.decode(),
        0x40,
        0.800000011920929,
        0x3,
        [0,0,0],
        [
            GenericParamHeaderPartitionInfo(0x1, 0x40),
            GenericParamHeaderPartitionInfo(0x20, 0x40),
            GenericParamHeaderPartitionInfo(0x20, 0x60)
        ],
        b'\x00\x00\x00\x00' * 2
    )


@fixture
def mood_setting_param_element() -> MoodSettingParamElement:
    return MoodSettingParamElement(
        b'MoodSettings\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00'.decode(),
        0,
        [0.10000000149011612, 0.3499999940395355, 1.0],
        [0, 0, 0, 0],
    )


@fixture
def antededent_def_param_last_element() -> AntecedentDefParamElement:
    return AntecedentDefParamElement(
        b'3\x81`3\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00'.decode("shift-jis"),
        31,
        6,
        [3.0, 3.0, 0.0, 0.0],
        [0, 0],
    )


@fixture
def rule_def_param_last_element() -> RuleDefParamElement:
    return RuleDefParamElement(
        b'none\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00'.decode(),
        31,
        [-1, -1, -1, -1, -1, -1],
        [-1, -1],
        [0, 0, 0, 0, 0, 0, 0],
    )



def test_verify_datafield_pos():
    assert SoundParam.verify_datafield_pos()


def test_get_byte_size(
        sound_param_header: SoundParamHeader,
        mood_setting_param_element: MoodSettingParamElement,
        antededent_def_param_last_element: AntecedentDefParamElement,
        rule_def_param_last_element: RuleDefParamElement
        ):
    assert sound_param_header.get_byte_size() == 0x40
    assert mood_setting_param_element.get_byte_size() == 0x40
    assert antededent_def_param_last_element.get_byte_size() == 0x40
    assert rule_def_param_last_element.get_byte_size() == 0x60


def test_from_bytes(
        sound_param_header: SoundParamHeader,
        mood_setting_param_element: MoodSettingParamElement,
        antededent_def_param_last_element: AntecedentDefParamElement,
        rule_def_param_last_element: RuleDefParamElement
        ):
    file_name = "D:\\Patapon\\Patapon Stuff\\Patapon 1 US\\@DATA_CMN\\loadinggroup\\@systemdata\\@default\\@loadinggroupcmn\\@paramlist\\soundparam.dat"
    with open(file_name, "rb") as file:
        raw = file.read()
        actual: SoundParam = SoundParam.from_bytes(raw)
        assert SoundParam.verify_filler(actual)

    assert actual.get_byte_size() == 0x1480

    assert actual.header.get_byte_size() == 0x40
    assert actual.header == sound_param_header

    assert len(actual.mood_setting_params.param_list) == 0x1
    assert actual.mood_setting_params.param_list[-1].get_byte_size() == 0x40
    assert actual.mood_setting_params.param_list[-1] == mood_setting_param_element
    
    assert len(actual.antecedent_def_params.param_list) == 0x20
    assert actual.antecedent_def_params.param_list[-1].get_byte_size() == 0x40
    assert actual.antecedent_def_params.param_list[-1] == antededent_def_param_last_element

    assert len(actual.rule_def_params.param_list) == 0x20
    assert actual.rule_def_params.param_list[-1].get_byte_size() == 0x60
    assert actual.rule_def_params.param_list[-1] == rule_def_param_last_element