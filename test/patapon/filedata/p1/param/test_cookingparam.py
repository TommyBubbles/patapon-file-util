from pytest import fixture
import sys
sys.path.insert(0, ".\\src")
from patapon.filedata.p1.param import CookingParam, DamageParam
from patapon.filedata.p1.param.cookingparam import (
    CookingParamHeader,
    CookingParamInfoElement
)
from patapon.filedata.p1.param.generic import (
     GenericParamHeaderPartitionInfo
)
from patapon.filedata.patapon_data_class import PataponDataIO



@fixture
def cooking_param_header() -> CookingParamHeader:
    return CookingParamHeader(
        b'YGF_GFP\x00',
        0x40,
        0.800000011920929,
        0x1,
        [0,0,0],
        [
            GenericParamHeaderPartitionInfo(0x4, 0x128)
        ],
        b'\x00\x00\x00\x00' * 6
    )


@fixture
def cooking_param_last_element() -> CookingParamInfoElement:
    return CookingParamInfoElement(
        b'COOKINGID_STEW_04x\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00'.decode(),
        3,
        52,
        DamageParam(
            100.0,
            14.0,
            1.0,
            1.0,
            1.0,
            0.0,
            1.0,
            0,
            5.0,
            -1,
            5.0,
            0.0,
            0.0,
            -1,
            -1,
            0,
            [0.20000000298023224, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.0, 0.0, 0.0],
            b'0\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00'.decode(),
            [0.8999999761581421, 0.8999999761581421, 0.8999999761581421, 0.8999999761581421, 0.8999999761581421, 0.8999999761581421, 0.8999999761581421, 0.0],
            [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0],
            [0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.0, 0.0, 0.0],
            [-1, -1, -1, -1, -1, -1, -1, 0],
        )
    )



def test_verify_datafield_pos():
    assert CookingParam.verify_datafield_pos()


def test_get_byte_size(
        cooking_param_header: CookingParamHeader,
        cooking_param_last_element: CookingParamInfoElement
        ):
    assert cooking_param_header.get_byte_size() == 0x40
    assert cooking_param_last_element.get_byte_size() == 0x128


def test_from_bytes(
        cooking_param_header: CookingParamHeader,
        cooking_param_last_element: CookingParam
        ):
    file_name = "D:\\Patapon\\Patapon Stuff\\Patapon 1 US\\@DATA_CMN\\loadinggroup\\@systemdata\\@default\\@loadinggroupcmn\\@paramlist\\cookingparam.dat"
    with open(file_name, "rb") as file:
        raw = file.read()
        data_stream = PataponDataIO(raw)
        actual: CookingParam = CookingParam.from_bytes(data_stream)
        assert CookingParam.verify_filler(actual)

    assert actual.get_byte_size() == 0x4E0

    assert actual.header.get_byte_size() == 0x40
    assert actual.header == cooking_param_header

    assert len(actual.chara_group_params.param_list) == 0x4
    assert actual.chara_group_params.param_list[-1].get_byte_size() == 0x128
    assert actual.chara_group_params.param_list[-1] == cooking_param_last_element