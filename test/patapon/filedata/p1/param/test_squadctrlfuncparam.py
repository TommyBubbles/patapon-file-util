from pytest import fixture
import sys
sys.path.insert(0, ".\\src")
from patapon.filedata.p1.param import SquadCtrlFuncParam
from patapon.filedata.p1.param.squadctrlfuncparam import (
    SquadCtrlFuncParamHeader,
    BaseParamElement
)
from patapon.filedata.p1.param.generic import (
    GenericParamHeaderPartitionInfo
)
from patapon.filedata.patapon_data_class import PataponDataIO



@fixture
def squad_ctrl_func_param_header() -> SquadCtrlFuncParamHeader:
    return SquadCtrlFuncParamHeader(
        b'YGF_GFP\x00',
        0x40,
        0.800000011920929,
        0x1,
        [0,0,0],
        [
            GenericParamHeaderPartitionInfo(0x29, 0x100)
        ],
        b'\x00\x00\x00\x00' * 6
    )


@fixture
def base_param_last_element() -> BaseParamElement:
    return BaseParamElement(
        b'40\x81FDmy\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00'.decode("shift-jis"),
        40,
        -1,
        [0, 0, 0, 0, 0, 0],
        6,
        1.0,
        0.0,
        0,
        0.0,
        [0, 0, 0],
        -1.0,
        -1,
        0,
        -1,
        -1,
        [-1, -1, -1],
        [-1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1],
        0,
        0.0,
        0.0,
        0,
        0,
        -1,
        [0, 0],
        -1,
        1,
        1,
        [0, 0, 0, 0, 0],
    )



def test_verify_datafield_pos():
    assert SquadCtrlFuncParam.verify_datafield_pos()


def test_get_byte_size(
        squad_ctrl_func_param_header: SquadCtrlFuncParamHeader,
        base_param_last_element: BaseParamElement
        ):
    assert squad_ctrl_func_param_header.get_byte_size() == 0x40
    assert base_param_last_element.get_byte_size() == 0x100


def test_from_bytes(
        squad_ctrl_func_param_header: SquadCtrlFuncParamHeader,
        base_param_last_element: BaseParamElement,
        ):
    file_name = "D:\\Patapon\\Patapon Stuff\\Patapon 1 US\\@DATA_CMN\\loadinggroup\\@gamedata\\@default\\@loadinggroupcmn\\@paramlist\\squadctrlfuncparam.dat"
    with open(file_name, "rb") as file:
        raw = file.read()
        data_stream = PataponDataIO(raw)
        actual: SquadCtrlFuncParam = SquadCtrlFuncParam.from_bytes(data_stream)
        assert SquadCtrlFuncParam.verify_filler(actual)


    assert actual.header.get_byte_size() == 0x40
    assert actual.header == squad_ctrl_func_param_header

    assert len(actual.base_params.param_list) == 0x29
    assert actual.base_params.param_list[-1].get_byte_size() == 0x100
    assert actual.base_params.param_list[-1] == base_param_last_element