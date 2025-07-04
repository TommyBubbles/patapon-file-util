from pytest import fixture
from struct import unpack
import sys

sys.path.insert(0, ".\\src")
from patapon.filedata import GXT
from patapon.filedata.gxx import (
    GXXFileHeader,
    GXXUnknown1Header,
    GXXUnknown1Body,
    GXXUnknown2Header,
    GXXUnknown2Body,
    GXXAnimationClipSection,
    GXXAnimationClipElement,
    GXXAnimationClipElementHeader,
    GXXAnimationClipElementBody,
    GXXAnimationInfoSection,
    GXXAnimationInfoHeader,
    GXXFileFooterPointers,
    GXXAnimationInfoTable,
    GXXAnimationInfoElement,
    GXXNodeNameListHeader,
    GXXNodeNameElement,
    GXXNodeNameListBody,
    GXXFileFooter
)

class TestFileOne():
    @fixture
    def file_one(self) -> str:
        return ".\\test\\files\\@unit010_01_01\\@model\\chr01_01_10_1.gxx"


    @fixture
    def file_one_gxx_header(self) -> GXXFileHeader:
        return GXXFileHeader(
            "XXG.01.0OMG.",
            0x52980,
            [0,0,0],
            0x52980,
            0xEC0,
            0x300,
            0x52680,
            0x40,
            0x2C0,
            0x40,
            0x0
        )


    @fixture
    def file_one_gxx_unknown_1_header(self) -> GXXUnknown1Header:
        return GXXUnknown1Header()


    @fixture
    def file_one_gxx_unknown_1_body(self) -> GXXUnknown1Body:
        return GXXUnknown1Body()


    @fixture
    def file_one_gxx_unknown_2_header(self) -> GXXUnknown2Header:
        return GXXUnknown2Header(
            0x1,
            0x280,
            0x280,
            [0,0,0,0,0,0,0,0,0,0,0,0,0]
        )
    

    @fixture
    def file_one_gxx_unknown_2_body(self, file_one: str) -> GXXUnknown2Body:
        with open(file_one, "rb") as file:
            file.seek(0x80)
            raw = file.read(0x280)
            fl1 = list(unpack("<160f", raw))
        return GXXUnknown2Body(
            fl1
        )


    @fixture
    def file_one_gxx_animation_clip_section(self, file_one: str) -> GXXAnimationClipSection:
        with open(file_one, "rb") as file:
            file.seek(0x300)
            raw = file.read(0x52680)

            element_list = []
            offset = 0
            while offset < len(raw):
                header_values = unpack("<III13I", raw[offset:offset+40])
                header = GXXAnimationClipElementHeader(*header_values)
                offset += 0x40

                body_values = list(unpack(f"<{header.used_size//4}f{header.total_size-header.used_size}x", raw[offset:offset+header.total_size]))
                body = GXXAnimationClipElementBody(body_values)
                offset += header.total_size

                element = GXXAnimationClipElement(header, body)
                element_list.append(element)
        
        return GXXAnimationClipSection(element_list)
    

    @fixture
    def file_one_gxx_animation_info_header(self) -> GXXAnimationInfoHeader:
        return GXXAnimationInfoHeader(
            0x3,
            0x0,
            0x529B8,
            0x1,
            0x29BC,
            0x4F,
            0x53764,
            0x9,
            [-18.5224151611328, -1.00000095367432, -5.00970888137817, 18.5225410461426, 29.0, 3.00000405311584]
        )
    

    @fixture
    def file_one_gxx_footer_pointers_list(self) -> GXXFileFooterPointers:
        return GXXFileFooterPointers(
            [0x537F0]
        )


    @fixture
    def file_one_gxx_animation_info_table(self, file_one: str) -> GXXAnimationInfoTable:
        with open(file_one, "rb") as file:
            file.seek(0x529BC)
            raw = file.read(0xDA8)
            offset = 0
            
            element_list = []
            for i in range(0x4F):
                element_values = unpack("<IIfI", raw[0x10*i:0x10*i+0x10])
                element = GXXAnimationInfoElement(*element_values)
                element_list.append(element)
            offset += 0x4F * 0x10

            anim_pointer_num = 0x22D
            offset += 0x4

            anim_clip_pointers = list(unpack(f"<{anim_pointer_num}I", raw[offset:offset+4*anim_pointer_num]))

        return GXXAnimationInfoTable(
            element_list,
            anim_pointer_num,
            anim_clip_pointers
        )
    

    @fixture
    def file_one_gxx_node_name_list_header(self) -> GXXNodeNameListHeader:
        return GXXNodeNameListHeader(
            [
                GXXNodeNameElement(0x18, 0x537AC),
                GXXNodeNameElement(0x184, 0x537B0),
                GXXNodeNameElement(0x70, 0x537B5),
                GXXNodeNameElement(0xB8, 0x537BA),
                GXXNodeNameElement(0x1B4, 0x537BE),
                GXXNodeNameElement(0x100, 0x537C5),
                GXXNodeNameElement(0x148, 0x537CC),
                GXXNodeNameElement(0x1E4, 0x537D3),
                GXXNodeNameElement(0x214, 0x537DA),
            ]
        )
    

    @fixture
    def file_one_gxx_node_name_list_body(self) -> GXXNodeNameListBody:
        return GXXNodeNameListBody(
            [
                "iwa",
                "helm",
                "body",
                "eye",
                "center",
                "r_hand",
                "l_hand",
                "weapon",
                "option"
            ]
        )


    @fixture
    def file_one_gxx_file_footer(self) -> GXXFileFooter:
        return GXXFileFooter(
            0xA,
            0x53828,
            [0,0],
            0x53810,
            0x1,
            [0,0],
            0x53824,
            0x1,
            [0,0],
            0x1,
            0x340,
            "chr01_01_10_1",
            [0,0]
        )


    @fixture
    def file_one_gxx_animation_info_section(self,
                                            file_one_gxx_animation_info_header: GXXAnimationInfoHeader,
                                            file_one_gxx_footer_pointers_list: GXXFileFooterPointers,
                                            file_one_gxx_animation_info_table: GXXAnimationInfoTable,
                                            file_one_gxx_node_name_list_header: GXXNodeNameListHeader,
                                            file_one_gxx_node_name_list_body: GXXNodeNameListBody,
                                            file_one_gxx_file_footer: GXXFileFooter
                                            ) -> GXXAnimationInfoSection:
        return GXXAnimationInfoSection(
            file_one_gxx_animation_info_header,
            file_one_gxx_footer_pointers_list,
            file_one_gxx_animation_info_table,
            file_one_gxx_node_name_list_header,
            file_one_gxx_node_name_list_body,
            file_one_gxx_file_footer
        )


    def test_from_bytes_gxx_file_header(self, file_one: str, file_one_gxx_header: GXXFileHeader):
        assert GXXFileHeader.verify_datafield_pos()

        with open(file_one, "rb") as file:
            raw = file.read(0x40)
            actual = GXXFileHeader.from_bytes(raw)
            assert GXXFileHeader.verify_filler(actual)

        expected = file_one_gxx_header

        print(expected)
        print(actual)

        assert actual == expected