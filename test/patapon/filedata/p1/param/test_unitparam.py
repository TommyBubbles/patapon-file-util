from pytest import fixture
import sys
sys.path.insert(0, ".\\src")
from patapon.filedata.p1.param import UnitParam
from patapon.filedata.p1.param.unitparam import (
    UnitParamHeader,
    BaseParamElement,
    TroopTypeParamElement
)
from patapon.filedata.p1.param.generic import (
    GenericParamHeaderPartitionInfo
)
from patapon.filedata.patapon_data_class import PataponDataIO



@fixture
def unit_param_header() -> UnitParamHeader:
    return UnitParamHeader(
        b'YGF_GFP\x00',
        0x40,
        0.800000011920929,
        0x2,
        [0,0,0],
        [
            GenericParamHeaderPartitionInfo(0x1, 0x80),
            GenericParamHeaderPartitionInfo(0x2, 0x80),
        ],
        b'\x00\x00\x00\x00' * 4
    )


@fixture
def base_param_element() -> BaseParamElement:
    return BaseParamElement(
        b'ThisGameIsLabo\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00'.decode(),
        0,
        [0, 0, 0, 0, 0, 0, 0],
        800.0,
        0.9300000071525574,
        0.9900000095367432,
        2.0,
        0.949999988079071,
        0.10000000149011612,
        0.0,
        1,
        0.30000001192092896,
        -8.0,
        8.0,
        0.25,
        3.0,
        [0, 0, 0],
    )


@fixture
def troop_type_param_last_element() -> TroopTypeParamElement:
    return TroopTypeParamElement(
        b'Enemy\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00'.decode(),
        1,
        [0, 0, 0, 0, 0, 0, 0],
        0.0,
        0.0,
        0.0,
        0.0,
        15.0,
        0.5,
        0.0,
        5.0,
        [0, 0, 0, 0, 0, 0, 0, 0],
    )



def test_verify_datafield_pos():
    assert UnitParam.verify_datafield_pos()


def test_get_byte_size(
        unit_param_header: UnitParamHeader,
        base_param_element: BaseParamElement,
        troop_type_param_last_element: TroopTypeParamElement,
        ):
    assert unit_param_header.get_byte_size() == 0x40
    assert base_param_element.get_byte_size() == 0x80
    assert troop_type_param_last_element.get_byte_size() == 0x80


def test_from_bytes(
        unit_param_header: UnitParamHeader,
        base_param_element: BaseParamElement,
        troop_type_param_last_element: TroopTypeParamElement,
        ):
    file_name = "D:\\Patapon\\Patapon Stuff\\Patapon 1 US\\@DATA_CMN\\loadinggroup\\@systemdata\\@default\\@loadinggroupcmn\\@paramlist\\unitparam.dat"
    with open(file_name, "rb") as file:
        raw = file.read()
        data_stream = PataponDataIO(raw)
        actual: UnitParam = UnitParam.from_bytes(data_stream)
        assert UnitParam.verify_filler(actual)

    assert actual.get_byte_size() == 0x1C0

    assert actual.header.get_byte_size() == 0x40
    assert actual.header == unit_param_header

    assert len(actual.base_params.param_list) == 0x1
    assert actual.base_params.param_list[-1].get_byte_size() == 0x80
    assert actual.base_params.param_list[-1] == base_param_element
    
    assert len(actual.troop_type_params.param_list) == 0x2
    assert actual.troop_type_params.param_list[-1].get_byte_size() == 0x80
    assert actual.troop_type_params.param_list[-1] == troop_type_param_last_element