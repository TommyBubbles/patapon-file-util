from pytest import fixture
import sys
sys.path.insert(0, ".\\src")
from patapon.filedata.p1.param import SquadActivityParam
from patapon.filedata.p1.param.squadactivityparam import (
    SquadActivityParamHeader,
    BaseParamElement,
    MissileParamElement
)
from patapon.filedata.p1.param import DamageParam
from patapon.filedata.p1.param.generic import (
    GenericParamHeaderPartitionInfo
)
from patapon.filedata.patapon_data_class import PataponDataIO



@fixture
def squad_activity_param_header() -> SquadActivityParamHeader:
    return SquadActivityParamHeader(
        b'YGF_GFP\x00',
        0x40,
        0.800000011920929,
        0x2,
        [0,0,0],
        [
            GenericParamHeaderPartitionInfo(0xD5, 0x200),
            GenericParamHeaderPartitionInfo(0x1B, 0x80)
        ],
        b'\x00\x00\x00\x00' * 4
    )


@fixture
def base_param_last_element() -> BaseParamElement:
    return BaseParamElement(
        b'212\x81F\x81\xa6\x97\\\x94\xf5\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00'.decode("shift-jis"),
        212,
        -1,
        10,
        [0, 0, 0, 0, 0],
        1,
        0.0,
        0.0,
        0,
        0.0,
        -10.0,
        -1,
        1,
        b'0\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00'.decode(),
        b'0\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00'.decode(),
        b'0\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00'.decode(),
        b'0\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00'.decode(),
        b'0\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00'.decode(),
        DamageParam(
            0.0,
            0.0,
            1.0,
            0.0,
            1.0,
            0.0,
            1.0,
            0,
            0.0,
            -1,
            0.0,
            0.0,
            0.0,
            1,
            1,
            0,
            [0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 1.0, 1.0],
            b'0\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00'.decode(),
            [1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 0.0],
            [1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0],
            [0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 1.0, 1.0],
            [-1, -1, -1, -1, -1, -1, -1, -1]
        )
    )


@fixture
def missle_param_last_element() -> MissileParamElement:
    return MissileParamElement(
        b'26\x81F\x8b|\x81@\x89\x93\x8dU2\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00'.decode("shift-jis"),
        26,
        [0, 0, 0, 0, 0, 0, 0],
        30.0,
        1.0,
        82.0,
        2.0,
        1.0,
        [0, 0, 0],
        b'0\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00'.decode(),
    )



def test_verify_datafield_pos():
    assert SquadActivityParam.verify_datafield_pos()


def test_get_byte_size(
        squad_activity_param_header: SquadActivityParamHeader,
        base_param_last_element: BaseParamElement,
        missle_param_last_element: MissileParamElement
        ):
    assert squad_activity_param_header.get_byte_size() == 0x40
    assert base_param_last_element.get_byte_size() == 0x200
    assert missle_param_last_element.get_byte_size() == 0x80


def test_from_bytes(
        squad_activity_param_header: SquadActivityParamHeader,
        base_param_last_element: BaseParamElement,
        missle_param_last_element: MissileParamElement
        ):
    file_name = "D:\\Patapon\\Patapon Stuff\\Patapon 1 US\\@DATA_CMN\\loadinggroup\\@gamedata\\@default\\@loadinggroupcmn\\@paramlist\\squadactivityparam.dat"
    with open(file_name, "rb") as file:
        raw = file.read()
        data_stream = PataponDataIO(raw)
        actual: SquadActivityParam = SquadActivityParam.from_bytes(data_stream)
        assert SquadActivityParam.verify_filler(actual)


    assert actual.header.get_byte_size() == 0x40
    assert actual.header == squad_activity_param_header

    assert len(actual.base_params.param_list) == 0xD5
    assert actual.base_params.param_list[-1].get_byte_size() == 0x200
    assert actual.base_params.param_list[-1] == base_param_last_element

    assert len(actual.missile_params.param_list) == 0x1B
    assert actual.missile_params.param_list[-1].get_byte_size() == 0x80
    assert actual.missile_params.param_list[-1] == missle_param_last_element