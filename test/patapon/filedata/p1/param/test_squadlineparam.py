from pytest import fixture
import sys
sys.path.insert(0, ".\\src")
from patapon.filedata.p1.param import SquadLineParam
from patapon.filedata.p1.param.squadlineparam import (
    SquadLineParamHeader,
    EachCharaParam,
    ActivityTableParam,
    TierLevelParam
)
from patapon.filedata.p1.param.generic import (
    GenericParamHeaderPartitionInfo
)
from patapon.filedata.patapon_data_class import PataponDataIO



@fixture
def sound_param_header() -> SquadLineParamHeader:
    return SquadLineParamHeader(
        b'YGF_GFP\x00',
        0x40,
        0.800000011920929,
        0x1,
        [0,0,0],
        [
            GenericParamHeaderPartitionInfo(0x1, 0x2900),
        ],
        b'\x00\x00\x00\x00' * 6
    )


@fixture
def each_chara_param_last_element() -> EachCharaParam:
    return EachCharaParam(
        b'\x97\\\x96\xf1\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00'.decode("shift-jis"),
        TierLevelParam(0,0,10,0),
        TierLevelParam(7,2,-3,0),
        TierLevelParam(0,0,0,0),
        TierLevelParam(0,0,0,0),
        TierLevelParam(0,0,0,0),
        TierLevelParam(0,0,0,0),
        TierLevelParam(0,0,0,0),
        TierLevelParam(0,0,0,0),
        b'0\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00'.decode(),
        b'0\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00'.decode(),
        b'0\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00'.decode(),
    )


@fixture
def activity_table_param_last_element() -> ActivityTableParam:
    return ActivityTableParam(
        b'\x97\\\x96\xf1_\x83`\x83\x83\x81[\x83WLv3\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00'.decode("shift-jis"),
        TierLevelParam(0,0,0,0),
        TierLevelParam(0,0,0,0),
        [TierLevelParam(0,0,0,0),TierLevelParam(0,0,0,0),TierLevelParam(0,0,0,0),TierLevelParam(0,0,0,0),TierLevelParam(0,0,0,0)],
        TierLevelParam(0,0,0,0),
        b'0\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00'.decode(),
        b'0\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00'.decode(),
        b'0\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00'.decode(),
    )



def test_verify_datafield_pos():
    assert SquadLineParam.verify_datafield_pos()


def test_get_byte_size(
        sound_param_header: SquadLineParamHeader,
        each_chara_param_last_element: EachCharaParam,
        activity_table_param_last_element: ActivityTableParam
        ):
    assert sound_param_header.get_byte_size() == 0x40
    assert each_chara_param_last_element.get_byte_size() == 0x100
    assert activity_table_param_last_element.get_byte_size() == 0x100


def test_from_bytes(
        sound_param_header: SquadLineParamHeader,
        each_chara_param_last_element: EachCharaParam,
        activity_table_param_last_element: ActivityTableParam
        ):
    file_name = "D:\\Patapon\\Patapon Stuff\\Patapon 1 US\\@DATA_CMN\\loadinggroup\\@systemdata\\@default\\@loadinggroupcmn\\@paramlist\\squadlineparam.dat"
    with open(file_name, "rb") as file:
        raw = file.read()
        data_stream = PataponDataIO(raw)
        actual: SquadLineParam = SquadLineParam.from_bytes(data_stream)
        assert SquadLineParam.verify_filler(actual)

    assert actual.get_byte_size() == 0x2940

    assert actual.header.get_byte_size() == 0x40
    assert actual.header == sound_param_header

    assert len(actual.squad_line_params.param_list) == 0x1
    assert actual.squad_line_params.param_list[0].get_byte_size() == 0x2900

    assert len(actual.squad_line_params.param_list[0].eachCharaData) == 0x8
    assert actual.squad_line_params.param_list[0].eachCharaData[-1].get_byte_size() == 0x100
    assert actual.squad_line_params.param_list[0].eachCharaData[-1] == each_chara_param_last_element
    
    assert len(actual.squad_line_params.param_list[0].activityTable) == 0x20
    assert actual.squad_line_params.param_list[0].activityTable[-1].get_byte_size() == 0x100
    assert actual.squad_line_params.param_list[0].activityTable[-1] == activity_table_param_last_element

    