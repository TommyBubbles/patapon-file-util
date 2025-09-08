from pytest import fixture
import sys
sys.path.insert(0, ".\\src")
from patapon.filedata.p1.param import HitEffectTableParam
from patapon.filedata.p1.param.hiteffecttableparam import (
    HitEffectTableParamHeader,
    BaseParamElement,
    AttackMaterialTableElement
)
from patapon.filedata.p1.param.generic import (
    GenericParamHeaderPartitionInfo
)


@fixture
def hit_effect_table_param_header() -> HitEffectTableParamHeader:
    return HitEffectTableParamHeader(
        b'YGF_GFP\x00'.decode(),
        0x40,
        0.800000011920929,
        0x2,
        [0,0,0],
        [
            GenericParamHeaderPartitionInfo(0x13, 0x40),
            GenericParamHeaderPartitionInfo(0x10, 0x80)
        ],
        b'\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00'
    )



@fixture
def base_param_last_element() -> BaseParamElement:
    return BaseParamElement(
        b'\x83\x81\x83K\x83|\x83\x93\x8dU\x8c\x82Hit\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00'.decode("shift-jis"),
        18,
        [0, 0, 0],
        -1,
        36,
        0,
        0,
    )


@fixture
def attack_material_table_last_element() -> AttackMaterialTableElement:
    return AttackMaterialTableElement(
        b'rsv15\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00'.decode(),
        15,
        [0, 0, 0, 0, 0, 0, 0],
        [-1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1],
    )



def test_verify_datafield_pos_effect_param():
    assert HitEffectTableParam.verify_datafield_pos()


def test_get_byte_size(
        hit_effect_table_param_header: HitEffectTableParamHeader,
        base_param_last_element: BaseParamElement,
        attack_material_table_last_element: AttackMaterialTableElement
        ):
    assert hit_effect_table_param_header.get_byte_size() == 0x40
    assert base_param_last_element.get_byte_size() == 0x40
    assert attack_material_table_last_element.get_byte_size() == 0x80


def test_from_bytes_effect_param(
        hit_effect_table_param_header: HitEffectTableParamHeader,
        base_param_last_element: BaseParamElement,
        attack_material_table_last_element: AttackMaterialTableElement
        ):
    file_name = "D:\\Patapon\\Patapon Stuff\\Patapon 1 US\\@DATA_CMN\\loadinggroup\\@systemdata\\@default\\@loadinggroupcmn\\@paramlist\\hiteffecttableparam.dat"
    with open(file_name, "rb") as file:
        raw = file.read()
        actual: HitEffectTableParam = HitEffectTableParam.from_bytes(raw)
        assert HitEffectTableParam.verify_filler(actual)

    assert actual.header.get_byte_size() == 0x40
    assert actual.header == hit_effect_table_param_header

    assert len(actual.base_params.param_list) == 0x13
    assert actual.base_params.param_list[-1].get_byte_size() == 0x40
    assert actual.base_params.param_list[-1] == base_param_last_element

    assert len(actual.attack_material_table.param_list) == 0x10
    assert actual.attack_material_table.param_list[-1].get_byte_size() == 0x80
    assert actual.attack_material_table.param_list[-1] == attack_material_table_last_element