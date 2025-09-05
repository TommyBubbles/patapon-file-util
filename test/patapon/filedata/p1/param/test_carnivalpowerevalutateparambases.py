from pytest import fixture
import sys
sys.path.insert(0, ".\\src")
from patapon.filedata.p1.param import CarnivalPowerEvalutateParamBases
from patapon.filedata.p1.param.carnivalpowerevalutateparambases import (
    CarnivalPowerEvalutateParamBasesCommonParamElement,
    CarnivalPowerEvalutateParamBasesRegularSettingsElement,
    CarnivalPowerEvalutateParamBasesGlobalSettingsElement,
    CarnivalPowerEvalutateParamBasesUnknown1Element,
    CarnivalPowerEvalutateParamBasesUnknown2Element
)


def test_verify_datafield_pos_carnival_param():
        assert CarnivalPowerEvalutateParamBases.verify_datafield_pos()


class TestFileOne():
    @fixture
    def common_param_last_element(self) -> CarnivalPowerEvalutateParamBasesCommonParamElement:
        return CarnivalPowerEvalutateParamBasesCommonParamElement(
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
    def regular_settings_element(self) -> CarnivalPowerEvalutateParamBasesRegularSettingsElement:
        return CarnivalPowerEvalutateParamBasesRegularSettingsElement(
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
    def global_settings_element(self) -> CarnivalPowerEvalutateParamBasesGlobalSettingsElement:
        return CarnivalPowerEvalutateParamBasesGlobalSettingsElement(
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
    def unknown_1_last_element(self) -> CarnivalPowerEvalutateParamBasesUnknown1Element:
        return CarnivalPowerEvalutateParamBasesUnknown1Element(
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
    def unknown_2_last_element(self) -> CarnivalPowerEvalutateParamBasesUnknown2Element:
        return CarnivalPowerEvalutateParamBasesUnknown2Element(
            b'\x8dU\x8c\x82\x82\xb3\x82\xea\x82\xbd\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00'.decode("shift-jis"),
            0,
            -1.0,
            [0, 0, 0, 0, 0, 0],
        )


    def test_from_bytes_carnival_param(self,
            common_param_last_element: CarnivalPowerEvalutateParamBasesCommonParamElement,
            regular_settings_element: CarnivalPowerEvalutateParamBasesRegularSettingsElement,
            global_settings_element: CarnivalPowerEvalutateParamBasesGlobalSettingsElement,
            unknown_1_last_element: CarnivalPowerEvalutateParamBasesUnknown1Element,
            unknown_2_last_element: CarnivalPowerEvalutateParamBasesUnknown2Element):
        file_name = "D:\\Patapon\\Patapon Stuff\\Patapon 1 US\\@DATA_CMN\\loadinggroup\\@systemdata\\@default\\@loadinggroupcmn\\@paramlist\\carnivalpowerevalutateparambases.dat"
        with open(file_name, "rb") as file:
            raw = file.read()
            actual: CarnivalPowerEvalutateParamBases = CarnivalPowerEvalutateParamBases.from_bytes(raw)
            assert CarnivalPowerEvalutateParamBases.verify_filler(actual)

        assert len(actual.global_settings.settings_list) == 0x1
        assert actual.global_settings.settings_list[0] == global_settings_element

        assert len(actual.regular_settings.settings_list) == 0x1
        assert actual.regular_settings.settings_list[0] == regular_settings_element

        assert len(actual.common_params.param_list) == 0x3
        assert actual.common_params.param_list[-1] == common_param_last_element

        assert len(actual.unknown_1.param_list) == 0x3
        assert actual.unknown_1.param_list[-1] == unknown_1_last_element

        assert len(actual.unknown_2.param_list) == 0x1
        assert actual.unknown_2.param_list[-1] == unknown_2_last_element
