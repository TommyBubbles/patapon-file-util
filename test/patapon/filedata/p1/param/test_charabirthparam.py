from pytest import fixture
import sys
sys.path.insert(0, ".\\src")
from patapon.filedata.p1.param import CharaBirthParam, DamageParam
from patapon.filedata.p1.param.charabirthparam import (
    CharaBirthParamHeader,
    BirthParamElement,
    AdjustDamageParamElement
)
from patapon.filedata.p1.param.generic import (
     GenericParamHeaderPartitionInfo
)


@fixture
def chara_birth_param_header() -> CharaBirthParamHeader:
    return CharaBirthParamHeader(
        b'YGF_GFP\x00'.decode(),
        0x40,
        0.800000011920929,
        0x2,
        [0,0,0],
        [
            GenericParamHeaderPartitionInfo(0x80, 0x80),
            GenericParamHeaderPartitionInfo(0x5D, 0x120)
        ],
        b'\x00\x00\x00\x00' * 4
    )


@fixture
def birth_param_last_element() -> BirthParamElement:
    return BirthParamElement(
        127,
        13,
        7,
        b'unit008_01_01\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00'.decode(),
        b'\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00'.decode(),
        [190, 254, 205, 255],
        [151, 175, -1],
        [0, 1, 0],
        [48, 40],
        2100,
        [0, 0, 0, 0],
    )


@fixture
def adjust_damage_param_last_element() -> AdjustDamageParamElement:
    return AdjustDamageParamElement(
        b'\x83\x81\x83K\x83|\x83\x93\x95\xe2\x90\xb3\x82P\x82Q\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00'.decode("shift-jis"),
        DamageParam(
            0.0,
            0.0,
            1.0,
            0.0,
            1.0,
            0.0,
            1.0,
            0,
            0.0,
            -1,
            0.0,
            0.0,
            0.0,
            -1,
            -1,
            0,
            [0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 1.0, 1.0],
            b'14\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00'.decode(),
            [1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 0.0],
            [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 1.0],
            [0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 1.0, 1.0],
            [-1, -1, -1, -1, -1, -1, -1, -1]
        ),
    )



def test_verify_datafield_pos():
    assert CharaBirthParam.verify_datafield_pos()


def test_get_byte_size(
        chara_birth_param_header: CharaBirthParamHeader,
        birth_param_last_element: BirthParamElement,
        adjust_damage_param_last_element: AdjustDamageParamElement
    ):
    assert chara_birth_param_header.get_byte_size() == 0x40
    assert birth_param_last_element.get_byte_size() == 0x80
    assert adjust_damage_param_last_element.get_byte_size() == 0x120


def test_from_bytes(
        chara_birth_param_header: CharaBirthParamHeader,
        birth_param_last_element: BirthParamElement,
        adjust_damage_param_last_element: AdjustDamageParamElement
        ):
    file_name = "D:\\Patapon\\Patapon Stuff\\Patapon 1 US\\@DATA_CMN\\loadinggroup\\@systemdata\\@default\\@loadinggroupcmn\\@paramlist\\charabirthparam.dat"
    with open(file_name, "rb") as file:
        raw = file.read()
        actual: CharaBirthParam = CharaBirthParam.from_bytes(raw)
        assert CharaBirthParam.verify_filler(actual)

    assert actual.header.get_byte_size() == 0x40
    assert actual.header == chara_birth_param_header

    assert len(actual.birth_params.param_list) == 0x80
    assert actual.birth_params.param_list[-1].get_byte_size() == 0x80
    assert actual.birth_params.param_list[-1] == birth_param_last_element

    assert len(actual.adjust_damage_params.param_list) == 0x5D
    assert actual.adjust_damage_params.param_list[-1].get_byte_size() == 0x120
    assert actual.adjust_damage_params.param_list[-1] == adjust_damage_param_last_element