from pytest import fixture
import sys
sys.path.insert(0, ".\\src")
from patapon.filedata.p1.param import CarnivalPowerEvalutateParamBases
from patapon.filedata.p1.param.carnivalpowerevalutateparambases import (
    CarnivalPowerEvalutateParamBasesHeader,
    GlobalSettingsParamElement,
    RegularSettingsParamElement,
    CommonParamElement,
    Unknown1ParamElement,
    Unknown2ParamElement
)
from patapon.filedata.p1.param.generic import (
     GenericParamHeaderPartitionInfo
)
from patapon.filedata.patapon_data_class import PataponDataIO



@fixture
def carnival_power_evalutate_param_bases_header() -> CarnivalPowerEvalutateParamBasesHeader:
    return CarnivalPowerEvalutateParamBasesHeader(
        b'YGF_GFP\x00',
        0x80,
        0.800000011920929,
        0x5,
        [0,0,0],
        [
            GenericParamHeaderPartitionInfo(0x1, 0x50),
            GenericParamHeaderPartitionInfo(0x1, 0x40),
            GenericParamHeaderPartitionInfo(0x3, 0x50),
            GenericParamHeaderPartitionInfo(0x3, 0x40),
            GenericParamHeaderPartitionInfo(0x1, 0x40),
        ],
        b'\x00\x00\x00\x00' * 14
    )

@fixture
def global_settings_element() -> GlobalSettingsParamElement:
    return GlobalSettingsParamElement(
        b'globalSetting\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00'.decode(),
        0,
        4000,
        3000,
        20000,
        100,
        1.5,
        100,
        100,
        0.20000000298023224,
        1000,
        -1000,
        0,
    )


@fixture
def regular_settings_element() -> RegularSettingsParamElement:
    return RegularSettingsParamElement(
        b'regularSettings\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00'.decode(),
        0,
        1.5,
        100,
        100,
        3,
        0.20000000298023224,
        1000,
        700,
    )


@fixture
def common_param_last_element() -> CommonParamElement:
    return CommonParamElement(
        b'PATAPON\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00'.decode(),
        2,
        3,
        0,
        3,
        3,
        0,
        1,
        0,
        [3, 0, 1, 0, -1, -1, -1, -1],
    )


@fixture
def unknown_1_last_element() -> Unknown1ParamElement:
    return Unknown1ParamElement(
        b'PATAPON\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00'.decode(),
        2,
        3,
        [0, 0],
        1.0,
        1.0,
        1.0,
        1.0,
    )

@fixture
def unknown_2_last_element() -> Unknown2ParamElement:
    return Unknown2ParamElement(
        b'\x8dU\x8c\x82\x82\xb3\x82\xea\x82\xbd\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00'.decode("shift-jis"),
        0,
        -1.0,
        [0, 0, 0, 0, 0, 0],
    )



def test_verify_datafield_pos():
        assert CarnivalPowerEvalutateParamBases.verify_datafield_pos()


def test_get_byte_size(
        carnival_power_evalutate_param_bases_header: CarnivalPowerEvalutateParamBasesHeader,
        global_settings_element: GlobalSettingsParamElement,
        regular_settings_element: RegularSettingsParamElement,
        common_param_last_element: CommonParamElement,
        unknown_1_last_element: Unknown1ParamElement,
        unknown_2_last_element: Unknown2ParamElement
        ):
    assert carnival_power_evalutate_param_bases_header.get_byte_size() == 0x80
    assert global_settings_element.get_byte_size() == 0x50
    assert regular_settings_element.get_byte_size() == 0x40
    assert common_param_last_element.get_byte_size() == 0x50
    assert unknown_1_last_element.get_byte_size() == 0x40
    assert unknown_2_last_element.get_byte_size() == 0x40


def test_from_bytes(
        carnival_power_evalutate_param_bases_header: CarnivalPowerEvalutateParamBasesHeader,
        global_settings_element: GlobalSettingsParamElement,
        regular_settings_element: RegularSettingsParamElement,
        common_param_last_element: CommonParamElement,
        unknown_1_last_element: Unknown1ParamElement,
        unknown_2_last_element: Unknown2ParamElement
        ):
    file_name = "D:\\Patapon\\Patapon Stuff\\Patapon 1 US\\@DATA_CMN\\loadinggroup\\@systemdata\\@default\\@loadinggroupcmn\\@paramlist\\carnivalpowerevalutateparambases.dat"
    with open(file_name, "rb") as file:
        raw = file.read()
        data_stream = PataponDataIO(raw)
        actual: CarnivalPowerEvalutateParamBases = CarnivalPowerEvalutateParamBases.from_bytes(data_stream)
        assert CarnivalPowerEvalutateParamBases.verify_filler(actual)

    assert actual.get_byte_size() == 0x300

    assert actual.header.get_byte_size() == 0x80
    assert actual.header == carnival_power_evalutate_param_bases_header

    assert len(actual.global_settings.settings_list) == 0x1
    assert actual.global_settings.settings_list[0].get_byte_size() == 0x50
    assert actual.global_settings.settings_list[0] == global_settings_element

    assert len(actual.regular_settings.settings_list) == 0x1
    assert actual.regular_settings.settings_list[0].get_byte_size() == 0x40
    assert actual.regular_settings.settings_list[0] == regular_settings_element

    assert len(actual.common_params.param_list) == 0x3
    assert actual.common_params.param_list[-1].get_byte_size() == 0x50
    assert actual.common_params.param_list[-1] == common_param_last_element

    assert len(actual.unknown_1.param_list) == 0x3
    assert actual.unknown_1.param_list[0].get_byte_size() == 0x40
    assert actual.unknown_1.param_list[-1] == unknown_1_last_element

    assert len(actual.unknown_2.param_list) == 0x1
    assert actual.unknown_2.param_list[0].get_byte_size() == 0x40
    assert actual.unknown_2.param_list[-1] == unknown_2_last_element
