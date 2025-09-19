from pytest import fixture
import sys
sys.path.insert(0, ".\\src")
from patapon.filedata.p1.param import FacilityPersonParam
from patapon.filedata.p1.param.facilitypersonparam import (
    ParamHeader,
    ParamElement,
    AuxesisParam,
    ModelParamElement,
    MotionParam,
    AttachParamElement
)
from patapon.filedata.p1.param.generic import (
    GenericParamHeaderPartitionInfo
)
from patapon.filedata.patapon_data_class import PataponDataIO



def test_verify_datafield_pos():
        assert FacilityPersonParam.verify_datafield_pos()


class Test_FacilityParam:
    @fixture
    def facility_param_header(self) -> ParamHeader:
        return ParamHeader(
            b'YGF_GFP\x00',
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
    def param_last_element(self) -> ParamElement:
        return ParamElement(
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
    def model_param_last_element(self) -> ModelParamElement:
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
    def attach_param_last_element(self) -> AttachParamElement:
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



    def test_get_byte_size(self,
            facility_param_header: ParamHeader,
            param_last_element: ParamElement,
            model_param_last_element: ModelParamElement,
            attach_param_last_element: AttachParamElement
            ):
        assert facility_param_header.get_byte_size() == 0x40
        assert param_last_element.get_byte_size() == 0xD8
        assert model_param_last_element.get_byte_size() == 0x174
        assert attach_param_last_element.get_byte_size() == 0x90


    def test_from_bytes(self,
            facility_param_header: ParamHeader,
            param_last_element: ParamElement,
            model_param_last_element: ModelParamElement,
            attach_param_last_element: AttachParamElement
            ):
        file_name = "D:\\Patapon\\Patapon Stuff\\Patapon 1 US\\@DATA_CMN\\loadinggroup\\@basesdata\\@default\\@loadinggroupcmn\\@paramlist\\facilityparam.dat"
        with open(file_name, "rb") as file:
            raw = file.read()
            data_stream = PataponDataIO(raw)
            actual: FacilityPersonParam = FacilityPersonParam.from_bytes(data_stream)
            assert FacilityPersonParam.verify_filler(actual)

        assert actual.header.get_byte_size() == 0x40
        assert actual.header == facility_param_header

        assert len(actual.params.param_list) == 0x18
        assert actual.params.param_list[-1].get_byte_size() == 0xD8
        assert actual.params.param_list[-1] == param_last_element

        assert len(actual.model_params.param_list) == 0x1A
        assert actual.model_params.param_list[-1].get_byte_size() == 0x174
        assert actual.model_params.param_list[-1] == model_param_last_element

        assert len(actual.attach_params.param_list) == 0x8
        assert actual.attach_params.param_list[-1].get_byte_size() == 0x90
        assert actual.attach_params.param_list[-1] == attach_param_last_element


class Test_PersonParam:
    @fixture
    def person_param_header(self) -> ParamHeader:
        return ParamHeader(
            b'YGF_GFP\x00',
            0x40,
            0.800000011920929,
            0x3,
            [0,0,0],
            [
                GenericParamHeaderPartitionInfo(0x11, 0xD8),
                GenericParamHeaderPartitionInfo(0x16, 0x174),
                GenericParamHeaderPartitionInfo(0xF1, 0x90)
            ],
            b'\x00\x00\x00\x00' * 2
        )


    @fixture
    def param_last_element(self) -> ParamElement:
        return ParamElement(
            b'\x83\x81\x83K\x83|\x83\x93\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00'.decode("shift-jis"),
            16,
            3,
            b'\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00'.decode(),
            [
                AuxesisParam(
                    b'unit008_01_01\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00'.decode(),
                    100,
                    1,
                    3
                ),
                AuxesisParam(
                    b'\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00'.decode(),
                    1,
                    1,
                    3
                ),
                AuxesisParam(
                    b'\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00'.decode(),
                    1,
                    1,
                    3
                )
            ],
            1,
            [0, 0],
        )


    @fixture
    def model_param_last_element(self) -> ModelParamElement:
        return ModelParamElement(
            b'OPT001_005\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00'.decode(),
            b'opt001_005\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00'.decode(),
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
            60.0,
            0,
            0,
            [
                MotionParam(0.0, 0.0),
                MotionParam(0.0, 0.0),
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
    def attach_param_last_element(self) -> AttachParamElement:
        return AttachParamElement(
            b'ITM11_003_W\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00'.decode(),
            1,
            b'weapon\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00'.decode(),
            b'itm11_003\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00'.decode(),
            b'\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00'.decode(),
            -1,
            0,
            0,
        )



    def test_get_byte_size(self,
            person_param_header: ParamHeader,
            param_last_element: ParamElement,
            model_param_last_element: ModelParamElement,
            attach_param_last_element: AttachParamElement
            ):
        assert person_param_header.get_byte_size() == 0x40
        assert param_last_element.get_byte_size() == 0xD8
        assert model_param_last_element.get_byte_size() == 0x174
        assert attach_param_last_element.get_byte_size() == 0x90


    def test_from_bytes(self,
            person_param_header: ParamHeader,
            param_last_element: ParamElement,
            model_param_last_element: ModelParamElement,
            attach_param_last_element: AttachParamElement
            ):
        file_name = "D:\\Patapon\\Patapon Stuff\\Patapon 1 US\\@DATA_CMN\\loadinggroup\\@basesdata\\@default\\@loadinggroupcmn\\@paramlist\\personparam.dat"
        with open(file_name, "rb") as file:
            raw = file.read()
            data_stream = PataponDataIO(raw)
            actual: FacilityPersonParam = FacilityPersonParam.from_bytes(data_stream)
            assert FacilityPersonParam.verify_filler(actual)

        assert actual.header.get_byte_size() == 0x40
        assert actual.header == person_param_header

        assert len(actual.params.param_list) == 0x11
        assert actual.params.param_list[-1].get_byte_size() == 0xD8
        assert actual.params.param_list[-1] == param_last_element

        assert len(actual.model_params.param_list) == 0x16
        assert actual.model_params.param_list[-1].get_byte_size() == 0x174
        assert actual.model_params.param_list[-1] == model_param_last_element

        assert len(actual.attach_params.param_list) == 0xF1
        assert actual.attach_params.param_list[-1].get_byte_size() == 0x90
        assert actual.attach_params.param_list[-1] == attach_param_last_element