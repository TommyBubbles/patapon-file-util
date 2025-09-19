from pytest import fixture
import sys
sys.path.insert(0, ".\\src")
from patapon.filedata.p1.param import CarnivalPowerEvalutateParam
from patapon.filedata.p1.param.carnivalpowerevalutateparam import (
    CarnivalPowerEvalutateParamHeader,
    CarnivalPowerEvalutateCommonParamElement,
    CarnivalPowerEvalutateRegularSettingsElement,
    CarnivalPowerEvalutateGlobalSettingsElement
)
from patapon.filedata.p1.param.generic import (
     GenericParamHeaderPartitionInfo
)
from patapon.filedata.patapon_data_class import PataponDataIO



@fixture
def carnival_power_evalutate_param_header() -> CarnivalPowerEvalutateParamHeader:
    return CarnivalPowerEvalutateParamHeader(
        b'YGF_GFP\x00',
        0x80,
        0.800000011920929,
        0x3,
        [0,0,0],
        [
            GenericParamHeaderPartitionInfo(0x1, 0x50),
            GenericParamHeaderPartitionInfo(0x1, 0x50),
            GenericParamHeaderPartitionInfo(0x6, 0x50)
        ],
        b'\x00\x00\x00\x00' * 18
    )


@fixture
def global_settings_element() -> CarnivalPowerEvalutateGlobalSettingsElement:
    return CarnivalPowerEvalutateGlobalSettingsElement(
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
def regular_settings_element() -> CarnivalPowerEvalutateRegularSettingsElement:
    return CarnivalPowerEvalutateRegularSettingsElement(
        b'regularSettings\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00'.decode(),
        0,
        1.5,
        100,
        100,
        100,
        3,
        0.20000000298023224,
        1000,
        400,
        4,
        800,
        970,
    )


@fixture
def common_param_last_element() -> CarnivalPowerEvalutateCommonParamElement:
    return CarnivalPowerEvalutateCommonParamElement(
        b'\x83~\x83\x89\x83N\x83\x8b\x82P\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00'.decode("shift-jis"),
        5,
        6,
        0,
        6,
        6,
        6,
        1,
        0,
        [2, 0, 2, 2, 0, 2, 2, -1],
    )



def test_verify_datafield_pos():
        assert CarnivalPowerEvalutateParam.verify_datafield_pos()


def test_get_byte_size(
        carnival_power_evalutate_param_header: CarnivalPowerEvalutateParamHeader,
        global_settings_element: CarnivalPowerEvalutateGlobalSettingsElement,
        regular_settings_element: CarnivalPowerEvalutateRegularSettingsElement,
        common_param_last_element: CarnivalPowerEvalutateCommonParamElement
        ):
    assert carnival_power_evalutate_param_header.get_byte_size() == 0x80
    assert global_settings_element.get_byte_size() == 0x50
    assert regular_settings_element.get_byte_size() == 0x50
    assert common_param_last_element.get_byte_size() == 0x50


def test_from_bytes(
        carnival_power_evalutate_param_header: CarnivalPowerEvalutateParamHeader,
        global_settings_element: CarnivalPowerEvalutateGlobalSettingsElement,
        regular_settings_element: CarnivalPowerEvalutateRegularSettingsElement,
        common_param_last_element: CarnivalPowerEvalutateCommonParamElement
        ):
    file_name = "D:\\Patapon\\Patapon Stuff\\Patapon 1 US\\@DATA_CMN\\loadinggroup\\@systemdata\\@default\\@loadinggroupcmn\\@paramlist\\carnivalpowerevalutateparam.dat"
    with open(file_name, "rb") as file:
        raw = file.read()
        data_stream = PataponDataIO(raw)
        actual: CarnivalPowerEvalutateParam = CarnivalPowerEvalutateParam.from_bytes(data_stream)
        assert CarnivalPowerEvalutateParam.verify_filler(actual)

    assert actual.get_byte_size() == 0x300

    assert actual.header.get_byte_size() == 0x80
    assert actual.header == carnival_power_evalutate_param_header

    assert len(actual.global_settings.settings_list) == 0x1
    assert actual.global_settings.settings_list[0].get_byte_size() == 0x50
    assert actual.global_settings.settings_list[0] == global_settings_element

    assert len(actual.regular_settings.settings_list) == 0x1
    assert actual.regular_settings.settings_list[0].get_byte_size() == 0x50
    assert actual.regular_settings.settings_list[0] == regular_settings_element

    assert len(actual.common_params.param_list) == 0x6
    assert actual.common_params.param_list[-1].get_byte_size() == 0x50
    assert actual.common_params.param_list[-1] == common_param_last_element