from pytest import fixture
import sys
sys.path.insert(0, ".\\src")
from patapon.filedata.p1.param import NodeName, NodeNameParam
from patapon.filedata.p1.param.nodenameparam import (
    NodeNameParamHeader
)
from patapon.filedata.p1.param.generic import (
    GenericParamHeaderPartitionInfo
)


@fixture
def node_name_param_header() -> NodeNameParamHeader:
    return NodeNameParamHeader(
        b'YGF_GFP\x00'.decode(),
        0x40,
        0.800000011920929,
        0x3,
        [0,0,0],
        [
            GenericParamHeaderPartitionInfo(0x32, 0x100),
            GenericParamHeaderPartitionInfo(0x23, 0x100),
            GenericParamHeaderPartitionInfo(0x30, 0x100)
        ],
        b'\x00\x00\x00\x00' * 2
    )


@fixture
def unit_1_param_last_element() -> NodeName:
    return NodeName(
        b'unit003_02_02_H\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00'.decode(),
        49,
        [0, 0, 0],
        3,
        1,
        [0, 0],
        b'0\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00'.decode(),
        b'0\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00'.decode(),
        b'none\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00'.decode(),
        b'unit003_02_02_H\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00'.decode(),
        b'helm\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00'.decode(),
        b'0\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00'.decode(),
    )


@fixture
def unit_2_param_last_element() -> NodeName:
    return NodeName(
        b'unit003_02_02_34\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00'.decode(),
        34,
        [0, 0, 0],
        0,
        1,
        [0, 0],
        b'0\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00'.decode(),
        b'0\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00'.decode(),
        b'none\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00'.decode(),
        b'hlm107_01\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00'.decode(),
        b'0\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00'.decode(),
        b'0\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00'.decode(),
    )


@fixture
def equip_param_last_element() -> NodeName:
    return NodeName(
        b'hlm008_01\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00'.decode(),
        47,
        [0, 0, 0],
        0,
        1,
        [0, 0],
        b'0\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00'.decode(),
        b'0\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00'.decode(),
        b'none\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00'.decode(),
        b'hlm000_0_008\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00'.decode(),
        b'center\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00'.decode(),
        b'0\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00'.decode(),
    )



def test_verify_datafield_pos_effect_param():
    assert NodeNameParam.verify_datafield_pos()


def test_get_byte_size(
        node_name_param_header: NodeNameParamHeader,
        unit_1_param_last_element: NodeName,
        unit_2_param_last_element: NodeName,
        equip_param_last_element: NodeName
        ):
    assert node_name_param_header.get_byte_size() == 0x40
    assert unit_1_param_last_element.get_byte_size() == 0x100
    assert unit_2_param_last_element.get_byte_size() == 0x100
    assert equip_param_last_element.get_byte_size() == 0x100


def test_from_bytes(
        node_name_param_header: NodeNameParamHeader,
        unit_1_param_last_element: NodeName,
        unit_2_param_last_element: NodeName,
        equip_param_last_element: NodeName
        ):
    file_name = "D:\\Patapon\\Patapon Stuff\\Patapon 1 US\\@DATA_CMN\\loadinggroup\\@basesdata\\@default\\@loadinggroupcmn\\@paramlist\\nodenameparam.dat"
    with open(file_name, "rb") as file:
        raw = file.read()
        actual: NodeNameParam = NodeNameParam.from_bytes(raw)
        assert NodeNameParam.verify_filler(actual)

    assert actual.header.get_byte_size() == 0x40
    assert actual.header == node_name_param_header

    assert len(actual.unit_1_params.param_list) == 0x32
    assert actual.unit_1_params.param_list[-1].get_byte_size() == 0x100
    assert actual.unit_1_params.param_list[-1] == unit_1_param_last_element

    assert len(actual.unit_2_params.param_list) == 0x23
    assert actual.unit_2_params.param_list[-1].get_byte_size() == 0x100
    assert actual.unit_2_params.param_list[-1] == unit_2_param_last_element

    assert len(actual.equip_params.param_list) == 0x30
    assert actual.equip_params.param_list[-1].get_byte_size() == 0x100
    assert actual.equip_params.param_list[-1] == equip_param_last_element
