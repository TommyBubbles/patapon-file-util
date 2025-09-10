from pytest import fixture
import sys
sys.path.insert(0, ".\\src")
from patapon.filedata.p1.param import MotionTypeParam
from patapon.filedata.p1.param.motiontypeparam import (
    MotionTypeParamHeader,
    BaseParamElement
)
from patapon.filedata.p1.param.generic import (
    GenericParamHeaderPartitionInfo
)



@fixture
def motion_type_param_header() -> MotionTypeParamHeader:
    return MotionTypeParamHeader(
        b'YGF_GFP\x00'.decode(),
        0x40,
        0.800000011920929,
        0x2,
        [0,0,0],
        [
            GenericParamHeaderPartitionInfo(0xA, 0x80),
            GenericParamHeaderPartitionInfo(0,0)
        ],
        b'\x00\x00\x00\x00' * 4
    )


@fixture
def base_param_last_element() -> BaseParamElement:
    return BaseParamElement(
        b'9\x81F\x90Q\x82\xe9\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00'.decode("shift-jis"),
        9,
        9,
        [0, 0, 0],
        -3368449,
        [0, 0],
        7,
        1,
        0,
        [0, 0, 0, 0, 0],
        b'0\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00'.decode(),
    )



def test_verify_datafield_pos():
    assert MotionTypeParam.verify_datafield_pos()


def test_get_byte_size(
        motion_type_param_header: MotionTypeParamHeader,
        base_param_last_element: BaseParamElement
        ):
    assert motion_type_param_header.get_byte_size() == 0x40
    assert base_param_last_element.get_byte_size() == 0x80


def test_from_bytes(
        motion_type_param_header: MotionTypeParamHeader,
        base_param_last_element: BaseParamElement
        ):
    file_name = "D:\\Patapon\\Patapon Stuff\\Patapon 1 US\\@DATA_CMN\\loadinggroup\\@gamedata\\@default\\@loadinggroupcmn\\@paramlist\\motiontypeparam.dat"
    with open(file_name, "rb") as file:
        raw = file.read()
        actual: MotionTypeParam = MotionTypeParam.from_bytes(raw)
        assert MotionTypeParam.verify_filler(actual)

    assert actual.header.get_byte_size() == 0x40
    assert actual.header == motion_type_param_header

    assert len(actual.base_params.param_list) == 0xA
    assert actual.base_params.param_list[-1].get_byte_size() == 0x80
    assert actual.base_params.param_list[-1] == base_param_last_element