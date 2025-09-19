from pytest import fixture
import sys
sys.path.insert(0, ".\\src")
from patapon.filedata.p1.param import SceneLayoutParam
from patapon.filedata.p1.param.scenelayoutparam import (
    SceneLayoutParamHeader,
    LayoutParamElement,
    AnimationParamElement,
    TextureRectanleParamElement,
    Unknown1ParamElement,
    Unknown2ParamElement
)
from patapon.filedata.p1.param.generic import (
    GenericParamHeaderPartitionInfo
)
from patapon.filedata.patapon_data_class import PataponDataIO



@fixture
def scene_layout_param_header() -> SceneLayoutParamHeader:
    return SceneLayoutParamHeader(
        b'YGF_GFP\x00',
        0x40,
        0.800000011920929,
        0x4,
        [0,0,0],
        [
            GenericParamHeaderPartitionInfo(0x18, 0x80),
            GenericParamHeaderPartitionInfo(0x7, 0x80),
            GenericParamHeaderPartitionInfo(0x6, 0x80),
            GenericParamHeaderPartitionInfo(0x2, 0x80),
        ]
    )


@fixture
def layout_param_last_element() -> LayoutParamElement:
    return LayoutParamElement(
        b'test_7\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00'.decode(),
        23,
        0,
        0.0,
        0.0,
        100.0,
        100.0,
        10.0,
        10.0,
        0,
        0,
        0,
        0,
        1,
        0,
        0,
        1,
        -1,
        0,
        1,
        [0, 0, 0, 0, 0],
    )


@fixture
def animation_param_last_element() -> AnimationParamElement:
    return AnimationParamElement(
        b'\x8c\x88\x92\xe8\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00'.decode("shift-jis"),
        6,
        0,
        0.0,
        0.0,
        2.0,
        2.0,
        0.0,
        1.0,
        1,
        1,
        0,
        0.10000000149011612,
        -1,
        0,
        0.5,
        0,
        0.0,
        0.0,
        0.0,
        0.0,
        0.0,
        0.0,
        0,
        0,
    )


@fixture
def texture_rectangle_param_last_element() -> TextureRectanleParamElement:
    return TextureRectanleParamElement(
        b'NL_Eye\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00'.decode(),
        5,
        0,
        0,
        5,
        36.0,
        183.0,
        10.0,
        10.0,
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    )


@fixture
def unknown_1_param_last_element() -> Unknown1ParamElement:
    return Unknown1ParamElement(
        b'Cursol01\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00'.decode(),
        1,
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    )


@fixture
def unknown_2_param_last_element() -> Unknown2ParamElement:
    return Unknown2ParamElement(
        b'Effect01\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00'.decode(),
        1,
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    )



def test_verify_datafield_pos():
    assert SceneLayoutParam.verify_datafield_pos()


def test_get_byte_size(
        scene_layout_param_header: SceneLayoutParamHeader,
        layout_param_last_element: LayoutParamElement,
        animation_param_last_element: AnimationParamElement,
        texture_rectangle_param_last_element: TextureRectanleParamElement,
        unknown_1_param_last_element: Unknown1ParamElement,
        unknown_2_param_last_element: Unknown2ParamElement
        ):
    print(scene_layout_param_header)
    assert scene_layout_param_header.get_byte_size() == 0x40
    assert layout_param_last_element.get_byte_size() == 0x80
    assert animation_param_last_element.get_byte_size() == 0x80
    assert texture_rectangle_param_last_element.get_byte_size() == 0x80
    assert unknown_1_param_last_element.get_byte_size() == 0x80
    assert unknown_2_param_last_element.get_byte_size() == 0x80


def test_from_bytes(
        scene_layout_param_header: SceneLayoutParamHeader,
        layout_param_last_element: LayoutParamElement,
        animation_param_last_element: AnimationParamElement,
        texture_rectangle_param_last_element: TextureRectanleParamElement,
        unknown_1_param_last_element: Unknown1ParamElement,
        unknown_2_param_last_element: Unknown2ParamElement
        ):
    file_name = "D:\\Patapon\\Patapon Stuff\\Patapon 1 US\\@DATA_CMN\\loadinggroup\\@systemdata\\@default\\@loadinggroupcmn\\@layoutlist\\scenelayoutparam00.dat"
    with open(file_name, "rb") as file:
        raw = file.read()
        data_stream = PataponDataIO(raw)
        actual: SceneLayoutParam = SceneLayoutParam.from_bytes(data_stream)
        assert SceneLayoutParam.verify_filler(actual)

    assert actual.get_byte_size() == 0x14C0

    assert actual.header.get_byte_size() == 0x40
    assert actual.header == scene_layout_param_header

    assert len(actual.layout_params.info_list) == 0x18
    assert actual.layout_params.info_list[-1].get_byte_size() == 0x80
    assert actual.layout_params.info_list[-1] == layout_param_last_element

    assert len(actual.animation_params.info_list) == 0x7
    assert actual.animation_params.info_list[-1].get_byte_size() == 0x80
    assert actual.animation_params.info_list[-1] == animation_param_last_element

    assert len(actual.texture_rectangle_params.info_list) == 0x6
    assert actual.texture_rectangle_params.info_list[-1].get_byte_size() == 0x80
    assert actual.texture_rectangle_params.info_list[-1] == texture_rectangle_param_last_element

    assert len(actual.unknown_1_params.info_list) == 0x2
    assert actual.unknown_1_params.info_list[-1].get_byte_size() == 0x80
    assert actual.unknown_1_params.info_list[-1] == unknown_1_param_last_element

    assert len(actual.unknown_2_params.info_list) == 0x2
    assert actual.unknown_2_params.info_list[-1].get_byte_size() == 0x80
    assert actual.unknown_2_params.info_list[-1] == unknown_2_param_last_element