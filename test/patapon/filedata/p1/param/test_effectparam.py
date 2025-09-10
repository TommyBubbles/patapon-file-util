from pytest import fixture
import sys
sys.path.insert(0, ".\\src")
from patapon.filedata.p1.param import EffectParam, DamageParam
from patapon.filedata.p1.param.effectparam import (
    EffectParamHeader,
    EffectParamInfoElement,
    EffectDamageParamElement
)
from patapon.filedata.p1.param.generic import (
     GenericParamHeaderPartitionInfo
)


@fixture
def effect_param_header() -> EffectParamHeader:
    return EffectParamHeader(
        b'YGF_GFP\x00'.decode(),
        0x40,
        0.800000011920929,
        0x2,
        [0,0,0],
        [
            GenericParamHeaderPartitionInfo(0xD6, 0xBC),
            GenericParamHeaderPartitionInfo(0x14, 0x120)
        ],
        b'\x00\x00\x00\x00' * 4
    )


@fixture
def effect_param_last_element() -> EffectParamInfoElement:
    return EffectParamInfoElement(
        b'EFF_PTCL_M003_003x\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00'.decode(),
        213,
        -1,
        2,
        b'\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00'.decode(),
        0,
        0,
        0,
        0,
        0,
        0,
        0,
        0,
        0.0,
        0,
        0.0,
        0.0,
        0.0,
        1.0,
        0.0,
        0.0,
        0.0,
        -1,
        b'\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00'.decode(),
        138,
        -1,
    )


@fixture
def effect_damage_param_last_element() -> EffectDamageParamElement:
    return EffectDamageParamElement(
        b'DMG_PATAPONS_EYE\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00'.decode(),
        DamageParam(
            0.0,
            15.0,
            1.0,
            1.0,
            0.0,
            0.0,
            1.0,
            0,
            15.0,
            0,
            30.0,
            10.0,
            0.0,
            0,
            0,
            0,
            [0.0, 1.0, 0.0, 0.0, 0.30000001192092896, 0.0, 0.0, 0.0],
            b'0\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00'.decode(),
            [0.8999999761581421, 0.8999999761581421, 0.8999999761581421, 0.8999999761581421, 0.8999999761581421, 0.8999999761581421, 0.8999999761581421, 0.0],
            [0.0, 0.0, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.0, 0.0],
            [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0],
            [0, 0, 0, 0, 0, 0, 0, 0],
        )
    )



def test_verify_datafield_pos():
    assert EffectParam.verify_datafield_pos()


def test_get_byte_size(
        effect_param_header: EffectParamHeader,
        effect_param_last_element: EffectParamInfoElement,
        effect_damage_param_last_element: EffectDamageParamElement
        ):
    assert effect_param_header.get_byte_size() == 0x40
    assert effect_param_last_element.get_byte_size() == 0xBC
    assert effect_damage_param_last_element.get_byte_size() == 0x120


def test_from_bytes(
        effect_param_header: EffectParamHeader,
        effect_param_last_element: EffectParam,
        effect_damage_param_last_element: EffectDamageParamElement
        ):
    file_name = "D:\\Patapon\\Patapon Stuff\\Patapon 1 US\\@DATA_CMN\\loadinggroup\\@systemdata\\@default\\@loadinggroupcmn\\@paramlist\\effectparam.dat"
    with open(file_name, "rb") as file:
        raw = file.read()
        actual: EffectParam = EffectParam.from_bytes(raw)
        assert EffectParam.verify_filler(actual)

    assert actual.header.get_byte_size() == 0x40
    assert actual.header == effect_param_header

    assert len(actual.effect_params.param_list) == 0xD6
    assert actual.effect_params.param_list[-1].get_byte_size() == 0xBC
    assert actual.effect_params.param_list[-1] == effect_param_last_element

    assert len(actual.effect_damage_params.param_list) == 0x14
    assert actual.effect_damage_params.param_list[-1].get_byte_size() == 0x120
    assert actual.effect_damage_params.param_list[-1] == effect_damage_param_last_element