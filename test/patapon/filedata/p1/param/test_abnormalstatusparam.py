from pytest import fixture
import sys
sys.path.insert(0, ".\\src")
from patapon.filedata.p1.param import AbnormalStatusParam
from patapon.filedata.p1.param.abnormalstatusparam import AbnormalStatusParamInfoElement


@fixture
def abnormal_status_param_last_element() -> AbnormalStatusParamInfoElement:
    return AbnormalStatusParamInfoElement(
        b'3\x81F\x82\xe6\x82\xeb\x82\xdf\x82\xab\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00'.decode("shift-jis"),
        3,
        3,
        [0,0,0,0,0,0],
        2,
        1,
        0,
        0,
        [4,1],
        -1,
        -1,
        '0\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00',
        0,
        0,
        0,
        0,
        [0,0,0,0],
        -1.0,
        0.0,
        0.0,
        0.0,
        0.0,
        0.0,
        0.0,
        0,
        '0\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00'
    )


def test_verify_datafield_pos_actor_param():
    assert AbnormalStatusParam.verify_datafield_pos()


def test_from_bytes_actor_param_file_one(abnormal_status_param_last_element: AbnormalStatusParamInfoElement):
    file_name = "D:\\Patapon\\Patapon Stuff\\Patapon 1 US\\@DATA_CMN\\loadinggroup\\@systemdata\\@default\\@loadinggroupcmn\\@paramlist\\abnormalstatusparam.dat"
    with open(file_name, "rb") as file:
        raw = file.read()
        actual: AbnormalStatusParam = AbnormalStatusParam.from_bytes(raw)
        assert AbnormalStatusParam.verify_filler(actual)

    assert len(actual.params.info_list) == 0x4
    assert actual.params.info_list[-1] == abnormal_status_param_last_element