from pytest import fixture
import sys
sys.path.insert(0, ".\\src")
from patapon.filedata.p1.param import CarnivalPowerEvalutateParam
from patapon.filedata.p1.param.carnivalpowerevalutateparam import (
    CarnivalPowerEvalutateCommonParamElement,
    CarnivalPowerEvalutateRegularSettingsElement,
    CarnivalPowerEvalutateGlobalSettingsElement
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



def test_verify_datafield_pos_carnival_param():
        assert CarnivalPowerEvalutateParam.verify_datafield_pos()


def test_from_bytes_carnival_param(
        common_param_last_element: CarnivalPowerEvalutateCommonParamElement,
        regular_settings_element: CarnivalPowerEvalutateRegularSettingsElement,
        global_settings_element: CarnivalPowerEvalutateGlobalSettingsElement):
    file_name = "D:\\Patapon\\Patapon Stuff\\Patapon 1 US\\@DATA_CMN\\loadinggroup\\@systemdata\\@default\\@loadinggroupcmn\\@paramlist\\carnivalpowerevalutateparam.dat"
    with open(file_name, "rb") as file:
        raw = file.read()
        actual: CarnivalPowerEvalutateParam = CarnivalPowerEvalutateParam.from_bytes(raw)
        assert CarnivalPowerEvalutateParam.verify_filler(actual)

    assert len(actual.global_settings.settings_list) == 0x1
    assert actual.global_settings.settings_list[0] == global_settings_element

    assert len(actual.regular_settings.settings_list) == 0x1
    assert actual.regular_settings.settings_list[0] == regular_settings_element

    assert len(actual.common_params.param_list) == 0x6
    assert actual.common_params.param_list[-1] == common_param_last_element