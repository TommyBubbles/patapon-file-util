from pytest import fixture
import sys
sys.path.insert(0, ".\\src")
from patapon.filedata.p1.effectkey import (
    EffectKey,
    EffectKeyHeader,
    EffectKeySectionElement,
    EffectKeyData,
    RectangleUC,
    ParticleParamElement,
    ParticleParam
)


class Test_FileOne:
    @fixture
    def filepath(self):
        return "D:\\Patapon\\Patapon Stuff\\Patapon 1 US\\@DATA_CMN\\loadinggroup\\@systemdata\\@default\\@effect\\unknown_0.bnd"


    @fixture
    def effect_key_header(self) -> EffectKeyHeader:
        return EffectKeyHeader(
            b'EFFECT2\x00'.decode(),
            464,
            2,
            464,
        )


    @fixture
    def effect_key_data(self) -> EffectKeyData:
        return EffectKeyData(
            1184,
            0,
            0,
            256,
            256,
            0,
            0,
            1,
            [
                RectangleUC(128,32,143,47),
                RectangleUC(0,0,0,0),
                RectangleUC(0,0,0,0),
                RectangleUC(0,0,0,0),
                RectangleUC(0,0,0,0),
                RectangleUC(0,0,0,0),
                RectangleUC(0,0,0,0),
                RectangleUC(0,0,0,0),
                RectangleUC(0,0,0,0),
                RectangleUC(0,0,0,0),
                RectangleUC(0,0,0,0),
                RectangleUC(0,0,0,0),
                RectangleUC(0,0,0,0),
                RectangleUC(0,0,0,0),
                RectangleUC(0,0,0,0),
                RectangleUC(0,0,0,0),
            ],
            b'\x00\x00\x00\x00\x00\x00',
            0,
            [0, 0],
        )


    @fixture
    def particle_param_first_element(self):
        return ParticleParamElement(
            b'2\x08\x00\x00\x02\x07\x12\x88',
            0,
            1,
            0,
            0,
            30,
            20,
            500,
            0,
            2500,
            200,
            0,
            0,
            1000,
            0,
            1000,
            1000,
            0,
            0,
            0,
            0,
            0,
            0,
            0,
            0,
            0,
            0,
            0,
            -10,
            0,
            12,
            0,
            0,
            2000,
            1000,
            1000,
            0,
            0,
            b'\x00\x00\x002',
            0,
            0,
            0,
            2,
            0,
            0,
            1024,
            2000,
            5,
            0,
            50,
            0,
            1,
            0,
            b'\x00\x00',
            0,
            0,
        )



    def test_verify_datafield_pos(self):
        assert EffectKey.verify_datafield_pos()


    def test_get_byte_size(self,
            effect_key_header: EffectKeyHeader,
            effect_key_data: EffectKeyData,
            particle_param_first_element: ParticleParamElement
            ):
        assert effect_key_header.get_byte_size() == 0x10
        assert effect_key_data.get_byte_size() == 0x60
        assert particle_param_first_element.get_byte_size() == 0x80


    def test_from_bytes(self,
                        filepath: str,
            effect_key_header: EffectKeyHeader,
            effect_key_data: EffectKeyData,
            particle_param_first_element: ParticleParamElement
            ):
        with open(filepath, "rb") as file:
            raw = file.read()
            actual: EffectKey = EffectKey.from_bytes(raw)
            assert EffectKey.verify_filler(actual)

        assert actual.get_byte_size() == 0x1D0

        assert actual.header.get_byte_size() == 0x10
        assert actual.header == effect_key_header

        assert len(actual.effect_key_sections.key_data_section_list) == 2
        assert actual.effect_key_sections.key_data_section_list[-1].key_data.get_byte_size() == 0x60
        assert actual.effect_key_sections.key_data_section_list[-1].key_data == effect_key_data

        assert len(actual.effect_key_sections.key_data_section_list[-1].particle_params.param_list) == 1
        assert actual.effect_key_sections.key_data_section_list[-1].particle_params.param_list[-1].get_byte_size() == 0x80
        assert actual.effect_key_sections.key_data_section_list[-1].particle_params.param_list[-1] == particle_param_first_element
