from pytest import fixture
import sys
sys.path.insert(0, ".\\src")
from patapon.filedata.p1.param import InstructionCommandParam
from patapon.filedata.p1.param.instructioncommandparam import (
    InstructionCommandParamHeader,
    InstructionCommandParamInfoElement
)
from patapon.filedata.p1.param.generic import (
    GenericParamHeaderPartitionInfo
)


@fixture
def instruction_command_param_header() -> InstructionCommandParamHeader:
    return InstructionCommandParamHeader(
        b'YGF_GFP\x00'.decode(),
        0x40,
        0.800000011920929,
        0x1,
        [0,0,0],
        [
            GenericParamHeaderPartitionInfo(0x1C, 0x80)
        ],
        b'\x00\x00\x00\x00' * 6
    )


@fixture
def instruction_command_param_last_element() -> InstructionCommandParamInfoElement:
    return InstructionCommandParamInfoElement(
        b'27\x81F\x93\xa6\x94\xf0\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00'.decode("shift-jis"),
        27,
        27,
        [0, 0, 0, 0, 0, 0],
        1,
        6,
        1,
        1,
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
    )



def test_verify_datafield_pos_effect_param():
    assert InstructionCommandParam.verify_datafield_pos()


def test_get_byte_size(
        instruction_command_param_header: InstructionCommandParamHeader,
        instruction_command_param_last_element: InstructionCommandParamInfoElement):
    assert instruction_command_param_header.get_byte_size() == 0x40
    assert instruction_command_param_last_element.get_byte_size() == 0x80


def test_from_bytes(
        instruction_command_param_header: InstructionCommandParamHeader,
        instruction_command_param_last_element: InstructionCommandParamInfoElement):
    file_name = "D:\\Patapon\\Patapon Stuff\\Patapon 1 US\\@DATA_CMN\\loadinggroup\\@systemdata\\@default\\@loadinggroupcmn\\@paramlist\\instructioncommandparam.dat"
    with open(file_name, "rb") as file:
        raw = file.read()
        actual: InstructionCommandParam = InstructionCommandParam.from_bytes(raw)
        assert InstructionCommandParam.verify_filler(actual)

    assert actual.header.get_byte_size() == 0x40
    assert actual.header == instruction_command_param_header

    assert len(actual.instruction_command_params.param_list) == 0x1C
    assert actual.instruction_command_params.param_list[-1].get_byte_size() == 0x80
    assert actual.instruction_command_params.param_list[-1] == instruction_command_param_last_element