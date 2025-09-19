from pytest import fixture
import sys
sys.path.insert(0, ".\\src")
from patapon.filedata.p1.param import ParticleParam
from patapon.filedata.p1.param.particleparam import (
    ParticleParamHeader,
    ParticleParamInfoElement
)
from patapon.filedata.p1.param.generic import (
    GenericParamHeaderPartitionInfo
)
from patapon.filedata.patapon_data_class import PataponDataIO



@fixture
def particle_param_header() -> ParticleParamHeader:
    return ParticleParamHeader(
        b'YGF_GFP\x00',
        0x40,
        0.800000011920929,
        0x1,
        [0,0,0],
        [
            GenericParamHeaderPartitionInfo(0x8A, 0x10)
        ],
        b'\x00\x00\x00\x00' * 6
    )


@fixture
def particle_param_last_element() -> ParticleParamInfoElement:
    return ParticleParamInfoElement(
        b'p137\x00\x00\x00\x00'.decode(),
        137,
        2,
    )



def test_verify_datafield_pos():
    assert ParticleParam.verify_datafield_pos()


def test_get_byte_size(
        particle_param_header: ParticleParamHeader,
        particle_param_last_element: ParticleParamInfoElement
        ):
    assert particle_param_header.get_byte_size() == 0x40
    assert particle_param_last_element.get_byte_size() == 0x10


def test_from_bytes(
        particle_param_header: ParticleParamHeader,
        particle_param_last_element: ParticleParamInfoElement
        ):
    file_name = "D:\\Patapon\\Patapon Stuff\\Patapon 1 US\\@DATA_CMN\\loadinggroup\\@systemdata\\@default\\@loadinggroupcmn\\@paramlist\\particleparam.dat"
    with open(file_name, "rb") as file:
        raw = file.read()
        data_stream = PataponDataIO(raw)
        actual: ParticleParam = ParticleParam.from_bytes(data_stream)
        assert ParticleParam.verify_filler(actual)

    assert actual.get_byte_size() == 0x8E0

    assert actual.header.get_byte_size() == 0x40
    assert actual.header == particle_param_header

    assert len(actual.particle_params.param_list) == 0x8A
    assert actual.particle_params.param_list[-1].get_byte_size() == 0x10
    assert actual.particle_params.param_list[-1] == particle_param_last_element
