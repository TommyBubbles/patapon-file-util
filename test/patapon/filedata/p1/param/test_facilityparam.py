from pytest import fixture
import sys
sys.path.insert(0, ".\\src")
from patapon.filedata.p1.param import FacilityParam
from patapon.filedata.p1.param.facilityparam import (
    FacilityParamHeader,
    FacilityParamElement,
    AuxesisParam,
    ModelParamElement,
    MotionParam,
    AttachParamElement
)
from patapon.filedata.p1.param import DamageParam
from patapon.filedata.p1.param.generic import (
    GenericParamHeaderPartitionInfo
)


@fixture
def facility_param_header() -> FacilityParamHeader:
    return FacilityParamHeader(
        b'YGF_GFP\x00'.decode(),
        0x40,
        0.800000011920929,
        0x3,
        [0,0,0],
        [
            GenericParamHeaderPartitionInfo(0x18, 0xD8),
            GenericParamHeaderPartitionInfo(0x1A, 0x174),
            GenericParamHeaderPartitionInfo(0x8, 0x90)
        ],
        b'\x00\x00\x00\x00' * 2
    )


@fixture
def facility_param_last_element() -> FacilityParamElement:
    return FacilityParamElement(
        b'\x8eR\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00'.decode("shift-jis"),
        23,
        1,
        b'\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00'.decode(),
        [
            AuxesisParam(
                b'MOUNTAIN\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00'.decode(),
                -1,
                0,
                0
            ),
            AuxesisParam(
                b'MOUNTAIN\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00'.decode(),
                -1,
                0,
                0
            ),
            AuxesisParam(
                b'MOUNTAIN\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00'.decode(),
                -1,
                0,
                0
            ),
        ],
        0,
        [0, 0],
    )


@fixture
def model_param_last_element() -> ModelParamElement:
    return ModelParamElement(
        b'MOUNTAIN\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00'.decode(),
        b'cln360\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00'.decode(),
        b'\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00'.decode(),
        b'\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00'.decode(),
        0,
        0,
        [
            b'\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00'.decode(),
            b'\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00'.decode(),
            b'\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00'.decode(),
            b'\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00'.decode(),
            b'\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00'.decode()
        ],
        0.0,
        2,
        0,
        [
            MotionParam(0.0, 1.0),
            MotionParam(1.0, 1.0),
            MotionParam(0.0, 0.0),
            MotionParam(0.0, 0.0),
            MotionParam(0.0, 0.0),
            MotionParam(0.0, 0.0),
            MotionParam(0.0, 0.0),
            MotionParam(0.0, 0.0),
            MotionParam(0.0, 0.0)
        ]
    )


@fixture
def attach_param_last_element() -> AttachParamElement:
    return AttachParamElement(
        b'STABLE_KARID_LV3\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00'.decode(),
        1,
        b'maxsceneroot\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00'.decode(),
        b'\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00'.decode(),
        b'\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00'.decode(),
        -1,
        0,
        0,
    )



def test_verify_datafield_pos_effect_param():
    assert FacilityParam.verify_datafield_pos()


def test_get_byte_size(
        facility_param_header: FacilityParamHeader,
        facility_param_last_element: FacilityParamElement,
        model_param_last_element: ModelParamElement,
        attach_param_last_element: AttachParamElement
        ):
    assert facility_param_header.get_byte_size() == 0x40
    assert facility_param_last_element.get_byte_size() == 0xD8
    assert model_param_last_element.get_byte_size() == 0x174
    assert attach_param_last_element.get_byte_size() == 0x90


def test_from_bytes(
        facility_param_header: FacilityParamHeader,
        facility_param_last_element: FacilityParamElement,
        model_param_last_element: ModelParamElement,
        attach_param_last_element: AttachParamElement
        ):
    file_name = "D:\\Patapon\\Patapon Stuff\\Patapon 1 US\\@DATA_CMN\\loadinggroup\\@basesdata\\@default\\@loadinggroupcmn\\@paramlist\\facilityparam.dat"
    with open(file_name, "rb") as file:
        raw = file.read()
        actual: FacilityParam = FacilityParam.from_bytes(raw)
        assert FacilityParam.verify_filler(actual)

    assert actual.header.get_byte_size() == 0x40
    assert actual.header == facility_param_header

    assert len(actual.facility_params.param_list) == 0x18
    assert actual.facility_params.param_list[-1].get_byte_size() == 0xD8
    assert actual.facility_params.param_list[-1] == facility_param_last_element

    assert len(actual.model_params.param_list) == 0x1A
    assert actual.model_params.param_list[-1].get_byte_size() == 0x174
    assert actual.model_params.param_list[-1] == model_param_last_element

    assert len(actual.attach_params.param_list) == 0x8
    assert actual.attach_params.param_list[-1].get_byte_size() == 0x90
    assert actual.attach_params.param_list[-1] == attach_param_last_element
