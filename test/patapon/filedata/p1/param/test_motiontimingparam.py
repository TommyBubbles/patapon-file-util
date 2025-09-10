from pytest import fixture
import sys
sys.path.insert(0, ".\\src")
from patapon.filedata.p1.param import MotionTimingParam
from patapon.filedata.p1.param.motiontimingparam import (
    MotionTimingParamHeader,
    BaseParamElement,
    NameListParamElement
)
from patapon.filedata.p1.param.generic import (
    GenericParamHeaderPartitionInfo
)



@fixture
def motion_timing_param_header() -> MotionTimingParamHeader:
    return MotionTimingParamHeader(
        b'YGF_GFP\x00'.decode(),
        0x40,
        0.800000011920929,
        0x2,
        [0,0,0],
        [
            GenericParamHeaderPartitionInfo(0x37, 0x100),
            GenericParamHeaderPartitionInfo(0x8, 0x80),
        ],
        b'\x00\x00\x00\x00' * 4
    )


@fixture
def base_param_element() -> BaseParamElement:
    return BaseParamElement(
        b'54\x81F\x90\xd8\x82\xe8\x8f\xe3\x82\xb0\x82\xe9\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00'.decode("shift-jis"),
        54,
        1,
        [0, 0],
        3,
        [0, 0, 0],
        0,
        0,
        24,
        0,
        2.0,
        [0, 0, 0],
        3,
        0,
        1572864,
        0,
        0,
        0,
        0.0,
        0.0,
        b'0\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00'.decode(),
        b'0\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00'.decode(),
        b'0\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00'.decode(),
        b'0\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00'.decode()
    )


@fixture
def name_list_param_last_element() -> NameListParamElement:
    return NameListParamElement(
        b'7\x81F\x83m\x81[\x83h\x96\xbc\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00'.decode("shift-jis"),
        7,
        [0, 0, 0, 0, 0, 0, 0],
        b'node_name\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00'.decode(),
    )



def test_verify_datafield_pos():
    assert MotionTimingParam.verify_datafield_pos()


def test_get_byte_size(
        motion_timing_param_header: MotionTimingParamHeader,
        base_param_element: BaseParamElement,
        name_list_param_last_element: NameListParamElement,
        ):
    assert motion_timing_param_header.get_byte_size() == 0x40
    assert base_param_element.get_byte_size() == 0x100
    assert name_list_param_last_element.get_byte_size() == 0x80


def test_from_bytes(
        motion_timing_param_header: MotionTimingParamHeader,
        base_param_element: BaseParamElement,
        name_list_param_last_element: NameListParamElement,
        ):
    file_name = "D:\\Patapon\\Patapon Stuff\\Patapon 1 US\\@DATA_CMN\\loadinggroup\\@gamedata\\@default\\@loadinggroupcmn\\@paramlist\\motiontimingparam.dat"
    with open(file_name, "rb") as file:
        raw = file.read()
        actual: MotionTimingParam = MotionTimingParam.from_bytes(raw)
        assert MotionTimingParam.verify_filler(actual)

    assert actual.header.get_byte_size() == 0x40
    assert actual.header == motion_timing_param_header

    assert len(actual.base_params.param_list) == 0x37
    assert actual.base_params.param_list[-1].get_byte_size() == 0x100
    assert actual.base_params.param_list[-1] == base_param_element
    
    assert len(actual.name_list_params.param_list) == 0x8
    assert actual.name_list_params.param_list[-1].get_byte_size() == 0x80
    assert actual.name_list_params.param_list[-1] == name_list_param_last_element