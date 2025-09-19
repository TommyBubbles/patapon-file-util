from pytest import fixture
import sys
sys.path.insert(0, ".\\src")
from patapon.filedata.p1.param import UnitLayoutParamE
from patapon.filedata.p1.param.unitlayoutparam_e import (
    UnitLayoutParamEHeader,
    TroopAddingParamElement,
    SquadAddingParamElement
)
from patapon.filedata.p1.param.generic import (
    GenericParamHeaderPartitionInfo
)
from patapon.filedata.patapon_data_class import PataponDataIO



@fixture
def squad_ctrl_func_param_header() -> UnitLayoutParamEHeader:
    return UnitLayoutParamEHeader(
        b'YGF_GFP\x00',
        0x40,
        0.800000011920929,
        0x3,
        [0,0,0],
        [
            GenericParamHeaderPartitionInfo(0x1, 0x80),
            GenericParamHeaderPartitionInfo(0x116, 0xA0),
            GenericParamHeaderPartitionInfo(0x0, 0x40)
        ],
        b'\x00\x00\x00\x00' * 2
    )


@fixture
def troop_adding_param_element() -> TroopAddingParamElement:
    return TroopAddingParamElement(
        b'Enemy\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00'.decode(),
        0,
        278,
        500.0,
        [0, 0, 0, 0, 0],
        b'FlagUnit\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00'.decode(),
        0,
        1,
        0,
        1,
        0,
        0,
        0,
        0,
    )


@fixture
def squad_adding_param_last_element() -> SquadAddingParamElement:
    return SquadAddingParamElement(
        b'277\x81F\x95\xe0\x95\xba\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00'.decode("shift-jis"),
        277,
        6,
        6,
        0,
        1,
        3,
        1,
        26,
        0,
        [0, 0, 0, 0, 0, 0],
        9750.0,
        0.0,
        0.0,
        300.0,
        b'UnitParam_277\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00'.decode(),
        120,
        [0, 0, 0],
        1,
        [0, 0, 0],
    )



def test_verify_datafield_pos():
    assert UnitLayoutParamE.verify_datafield_pos()


def test_get_byte_size(
        squad_ctrl_func_param_header: UnitLayoutParamEHeader,
        troop_adding_param_element: TroopAddingParamElement,
        squad_adding_param_last_element: SquadAddingParamElement
        ):
    assert squad_ctrl_func_param_header.get_byte_size() == 0x40
    assert troop_adding_param_element.get_byte_size() == 0x80
    assert squad_adding_param_last_element.get_byte_size() == 0xA0


def test_from_bytes(
        squad_ctrl_func_param_header: UnitLayoutParamEHeader,
        troop_adding_param_element: TroopAddingParamElement,
        squad_adding_param_last_element: SquadAddingParamElement
        ):
    file_name = "D:\\Patapon\\Patapon Stuff\\Patapon 1 US\\@DATA_CMN\\loadinggroup\\@gamedata\\@default\\@loadinggroupcmn\\@paramlist\\unitlayoutparam_e.dat"
    with open(file_name, "rb") as file:
        raw = file.read()
        data_stream = PataponDataIO(raw)
        actual: UnitLayoutParamE = UnitLayoutParamE.from_bytes(data_stream)
        assert UnitLayoutParamE.verify_filler(actual)


    assert actual.header.get_byte_size() == 0x40
    assert actual.header == squad_ctrl_func_param_header

    assert len(actual.troop_adding_params.param_list) == 0x1
    assert actual.troop_adding_params.param_list[-1].get_byte_size() == 0x80
    assert actual.troop_adding_params.param_list[-1] == troop_adding_param_element

    assert len(actual.squad_adding_params.param_list) == 0x116
    assert actual.squad_adding_params.param_list[-1].get_byte_size() == 0xA0
    assert actual.squad_adding_params.param_list[-1] == squad_adding_param_last_element