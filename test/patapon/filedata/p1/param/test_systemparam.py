from pytest import fixture
import sys
sys.path.insert(0, ".\\src")
from patapon.filedata.p1.param import SystemParam
from patapon.filedata.p1.param.systemparam import (
    SystemParamHeader,
    Unknown1ParamElement,
    Unknown2ParamElement
)
from patapon.filedata.p1.param.generic import (
    GenericParamHeaderPartitionInfo
)
from patapon.filedata.patapon_data_class import PataponDataIO



@fixture
def system_param_header() -> SystemParamHeader:
    return SystemParamHeader(
        b'YGF_GFP\x00',
        0x40,
        0.800000011920929,
        0x2,
        [0,0,0],
        [
            GenericParamHeaderPartitionInfo(0x4, 0x40),
            GenericParamHeaderPartitionInfo(0x6, 0x40),
        ],
        b'\x00\x00\x00\x00' * 4
    )


@fixture
def unknown_1_param_last_element() -> Unknown1ParamElement:
    return Unknown1ParamElement(
        b'none\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00'.decode(),
        3,
        [0, 0, 0, 0, 0, 0, 0],
    )


@fixture
def unknown_2_param_last_element() -> Unknown2ParamElement:
    return Unknown2ParamElement(
        b'none\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00'.decode(),
        5,
        [0, 0, 0, 0, 0, 0, 0],
    )



def test_verify_datafield_pos():
    assert SystemParam.verify_datafield_pos()


def test_get_byte_size(
        system_param_header: SystemParamHeader,
        unknown_1_param_last_element: Unknown1ParamElement,
        unknown_2_param_last_element: Unknown2ParamElement,
        ):
    assert system_param_header.get_byte_size() == 0x40
    assert unknown_1_param_last_element.get_byte_size() == 0x40
    assert unknown_2_param_last_element.get_byte_size() == 0x40


def test_from_bytes(
        system_param_header: SystemParamHeader,
        unknown_1_param_last_element: Unknown1ParamElement,
        unknown_2_param_last_element: Unknown2ParamElement,
        ):
    file_name = "D:\\Patapon\\Patapon Stuff\\Patapon 1 US\\@DATA_CMN\\loadinggroup\\@systemdata\\@default\\@loadinggroupcmn\\@paramlist\\systemparam.dat"
    with open(file_name, "rb") as file:
        raw = file.read()
        data_stream = PataponDataIO(raw)
        actual: SystemParam = SystemParam.from_bytes(data_stream)
        assert SystemParam.verify_filler(actual)

    assert actual.get_byte_size() == 0x2C0

    assert actual.header.get_byte_size() == 0x40
    assert actual.header == system_param_header

    assert len(actual.unknown_1_params.param_list) == 0x4
    assert actual.unknown_1_params.param_list[-1].get_byte_size() == 0x40
    assert actual.unknown_1_params.param_list[-1] == unknown_1_param_last_element
    
    assert len(actual.unknown_2_params.param_list) == 0x6
    assert actual.unknown_2_params.param_list[-1].get_byte_size() == 0x40
    assert actual.unknown_2_params.param_list[-1] == unknown_2_param_last_element