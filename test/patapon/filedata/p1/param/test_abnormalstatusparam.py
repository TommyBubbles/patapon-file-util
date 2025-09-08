from pytest import fixture
import sys
sys.path.insert(0, ".\\src")
from patapon.filedata.p1.param import AbnormalStatusParam
from patapon.filedata.p1.param.abnormalstatusparam import (
    AbnormalStatusParamHeader,
    AbnormalStatusParamInfoElement
)
from patapon.filedata.p1.param.generic import (
    GenericParamHeaderPartitionInfo
)


@fixture
def abnormal_status_param_header() -> AbnormalStatusParamHeader:
    return AbnormalStatusParamHeader(
        b'YGF_GFP\x00'.decode(),
        0x40,
        0.800000011920929,
        0x1,
        [0,0,0],
        [
            GenericParamHeaderPartitionInfo(0x4, 0x100),
        ],
        b'\x00\x00\x00\x00' * 6
    )


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



def test_verify_datafield_pos():
    assert AbnormalStatusParam.verify_datafield_pos()


def test_get_byte_size(
        abnormal_status_param_header: AbnormalStatusParamHeader,
        abnormal_status_param_last_element: AbnormalStatusParamInfoElement
        ):
    assert abnormal_status_param_header.get_byte_size() == 0x40
    assert abnormal_status_param_last_element.get_byte_size() == 0x100


def test_from_bytes(
        abnormal_status_param_header: AbnormalStatusParamHeader,
        abnormal_status_param_last_element: AbnormalStatusParamInfoElement
        ):
    file_name = "D:\\Patapon\\Patapon Stuff\\Patapon 1 US\\@DATA_CMN\\loadinggroup\\@systemdata\\@default\\@loadinggroupcmn\\@paramlist\\abnormalstatusparam.dat"
    with open(file_name, "rb") as file:
        raw = file.read()
        actual: AbnormalStatusParam = AbnormalStatusParam.from_bytes(raw)
        assert AbnormalStatusParam.verify_filler(actual)

    assert actual.header.get_byte_size() == 0x40
    assert actual.header == abnormal_status_param_header

    assert len(actual.params.info_list) == 0x4
    assert actual.params.info_list[-1].get_byte_size() == 0x100
    assert actual.params.info_list[-1] == abnormal_status_param_last_element