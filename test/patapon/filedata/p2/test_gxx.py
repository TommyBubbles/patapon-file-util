from pytest import fixture
from struct import unpack
import sys

sys.path.insert(0, ".\\src")
from patapon.filedata.p2 import GXT
from patapon.filedata.p2.gxx import (
    GxxFileHeader,
    GxxUnknown1Header,
    GxxUnknown1Body,
    GxxUnknown2Header,
    GxxUnknown2Body,
    GxxAnimationClipSection,
    GxxAnimationClipElement,
    GxxAnimationClipElementHeader,
    GxxAnimationClipElementBody,
    GxxAnimationInfoSection,
    GxxAnimationInfoHeader,
    GxxFileFooterPointers,
    GxxAnimationInfoTable,
    GxxAnimationInfoElement,
    GxxNodeNameListHeader,
    GxxNodeNameElement,
    GxxNodeNameListBody,
    GxxFileFooter
)

class TestFileOne():
    @fixture
    def file_one(self) -> str:
        return ".\\test\\files\\@unit010_01_01\\@model\\chr01_01_10_1.gxx"


    @fixture
    def file_one_gxx_header(self) -> GxxFileHeader:
        return GxxFileHeader(
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
    def file_one_gxx_unknown_1_header(self) -> GxxUnknown1Header:
        return GxxUnknown1Header()


    @fixture
    def file_one_gxx_unknown_1_body(self) -> GxxUnknown1Body:
        return GxxUnknown1Body()


    @fixture
    def file_one_gxx_unknown_2_header(self) -> GxxUnknown2Header:
        return GxxUnknown2Header(
            0x1,
            0x280,
            0x280,
            [0,0,0,0,0,0,0,0,0,0,0,0,0]
        )
    

    @fixture
    def file_one_gxx_unknown_2_body(self, file_one: str) -> GxxUnknown2Body:
        with open(file_one, "rb") as file:
            file.seek(0x80)
            raw = file.read(0x280)
            fl1 = list(unpack("<160f", raw))
        return GxxUnknown2Body(
            fl1
        )


    @fixture
    def file_one_gxx_animation_clip_section(self, file_one: str) -> GxxAnimationClipSection:
        with open(file_one, "rb") as file:
            file.seek(0x300)
            raw = file.read(0x52680)

            element_list = []
            offset = 0
            while offset < len(raw):
                header_values = unpack("<III13I", raw[offset:offset+0x40])
                header_args = list(header_values[0:3]); header_args.append(list(header_values[3:]))
                header = GxxAnimationClipElementHeader(*header_args)
                offset += 0x40

                body_values = list(unpack(f"<{header.used_size//4}f{header.total_size-header.used_size}x", raw[offset:offset+header.total_size]))
                body_values = body_values if len(body_values) > 1 else body_values[0]
                body = GxxAnimationClipElementBody(body_values, b'\x00' * (header.total_size - header.used_size))
                offset += header.total_size

                element = GxxAnimationClipElement(header, body)
                element_list.append(element)
        
        return GxxAnimationClipSection(element_list)
    

    @fixture
    def file_one_gxx_animation_info_header(self) -> GxxAnimationInfoHeader:
        return GxxAnimationInfoHeader(
            0x3,
            0x0,
            0x529B8,
            0x1,
            0x529BC,
            0x4F,
            0x53764,
            0x9,
            [-18.522415161132812, -1.0000009536743164, -5.009708881378174, 18.522541046142578, 29.0, 3.0000040531158447]
        )
    

    @fixture
    def file_one_gxx_footer_pointers_list(self) -> GxxFileFooterPointers:
        return GxxFileFooterPointers(
            [0x537F0]
        )


    @fixture
    def file_one_gxx_animation_info_table(self, file_one: str) -> GxxAnimationInfoTable:
        with open(file_one, "rb") as file:
            file.seek(0x529BC)
            raw = file.read(0xDA8)
            offset = 0
            
            element_list = []
            for i in range(0x4F):
                element_values = unpack("<IIfI", raw[0x10*i:0x10*i+0x10])
                element = GxxAnimationInfoElement(*element_values)
                element_list.append(element)
            offset += 0x4F * 0x10

            anim_pointer_num = 0x22D
            offset += 0x4

            anim_clip_pointers = list(unpack(f"<{anim_pointer_num}I", raw[offset:offset+4*anim_pointer_num]))

        return GxxAnimationInfoTable(
            element_list,
            anim_pointer_num,
            anim_clip_pointers
        )
    

    @fixture
    def file_one_gxx_node_name_list_header(self) -> GxxNodeNameListHeader:
        return GxxNodeNameListHeader(
            [
                GxxNodeNameElement(0x18, 0x537AC),
                GxxNodeNameElement(0x184, 0x537B0),
                GxxNodeNameElement(0x70, 0x537B5),
                GxxNodeNameElement(0xB8, 0x537BA),
                GxxNodeNameElement(0x1B4, 0x537BE),
                GxxNodeNameElement(0x100, 0x537C5),
                GxxNodeNameElement(0x148, 0x537CC),
                GxxNodeNameElement(0x1E4, 0x537D3),
                GxxNodeNameElement(0x214, 0x537DA),
            ]
        )
    

    @fixture
    def file_one_gxx_node_name_list_body(self) -> GxxNodeNameListBody:
        return GxxNodeNameListBody(
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
    def file_one_gxx_file_footer(self) -> GxxFileFooter:
        return GxxFileFooter(
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
                                            file_one_gxx_animation_info_header: GxxAnimationInfoHeader,
                                            file_one_gxx_footer_pointers_list: GxxFileFooterPointers,
                                            file_one_gxx_animation_info_table: GxxAnimationInfoTable,
                                            file_one_gxx_node_name_list_header: GxxNodeNameListHeader,
                                            file_one_gxx_node_name_list_body: GxxNodeNameListBody,
                                            file_one_gxx_file_footer: GxxFileFooter
                                            ) -> GxxAnimationInfoSection:
        return GxxAnimationInfoSection(
            file_one_gxx_animation_info_header,
            file_one_gxx_footer_pointers_list,
            file_one_gxx_animation_info_table,
            file_one_gxx_node_name_list_header,
            file_one_gxx_node_name_list_body,
            file_one_gxx_file_footer
        )


    def test_from_bytes_gxx_file_header(self, file_one: str, file_one_gxx_header: GxxFileHeader):
        assert GxxFileHeader.verify_datafield_pos()

        with open(file_one, "rb") as file:
            raw = file.read(0x40)
            actual = GxxFileHeader.from_bytes(raw)
            assert GxxFileHeader.verify_filler(actual)

        expected = file_one_gxx_header

        assert actual == expected

    
    def test_from_bytes_gxx_unknown_2_header(self, file_one: str, file_one_gxx_unknown_2_header: GxxUnknown2Header):
        assert GxxUnknown2Header.verify_datafield_pos()

        with open(file_one, "rb") as file:
            file.seek(0x40)
            raw = file.read(0x40)
            actual = GxxUnknown2Header.from_bytes(raw)
            assert GxxUnknown2Header.verify_filler(actual)

        expected = file_one_gxx_unknown_2_header

        assert actual == expected


    def test_from_bytes_gxx_unknown_2_body(self, file_one: str,
                                           file_one_gxx_unknown_2_header: GxxUnknown2Header,
                                           file_one_gxx_unknown_2_body: GxxUnknown2Body):
        assert GxxUnknown2Body.verify_datafield_pos()

        with open(file_one, "rb") as file:
            file.seek(0x80)
            raw = file.read(file_one_gxx_unknown_2_header.total_size)
            actual = GxxUnknown2Body.from_bytes(raw, header=file_one_gxx_unknown_2_header)
            assert GxxUnknown2Body.verify_filler(actual)

        expected = file_one_gxx_unknown_2_body

        assert actual == expected


    def test_from_bytes_gxx_animation_clip_section(self, file_one: str,
                                           file_one_gxx_header: GxxFileHeader,
                                           file_one_gxx_animation_clip_section: GxxAnimationClipSection):
        assert GxxAnimationClipSection.verify_datafield_pos()

        with open(file_one, "rb") as file:
            file.seek(file_one_gxx_header.animation_clips_offset)
            raw = file.read(file_one_gxx_header.animation_clips_size)
            actual = GxxAnimationClipSection.from_bytes(raw, header=file_one_gxx_header)
            assert GxxAnimationClipSection.verify_filler(actual)

        expected = file_one_gxx_animation_clip_section

        assert actual == expected


    def test_from_bytes_gxx_animation_info_header(self, file_one: str,
                                                 file_one_gxx_header: GxxFileHeader,
                                                 file_one_gxx_animation_info_header: GxxAnimationInfoHeader):
        assert GxxAnimationInfoHeader.verify_datafield_pos()

        with open(file_one, "rb") as file:
            file.seek(file_one_gxx_header.footer_offset)
            raw = file.read(GxxAnimationInfoHeader().get_byte_size())
            actual = GxxAnimationInfoHeader.from_bytes(raw)
            assert GxxAnimationInfoHeader.verify_filler(actual)

        expected = file_one_gxx_animation_info_header

        assert actual == expected


    def test_from_bytes_gxx_animation_info_table(self, file_one: str,
                                                 file_one_gxx_animation_info_header: GxxAnimationInfoHeader,
                                                 file_one_gxx_animation_info_table: GxxAnimationInfoTable):
        assert GxxAnimationInfoTable.verify_datafield_pos()



    # def test_from_bytes_gxx_animation_info_section(self, file_one: str,
    #                                                file_one_gxx_header: GxxFileHeader,
    #                                                file_one_gxx_animation_info_section: GxxAnimationInfoSection):
    #     assert GxxAnimationInfoSection.verify_datafield_pos()

    #     with open(file_one, "rb") as file:
    #         file.seek(file_one_gxx_header.footer_offset)
    #         raw = file.read(file_one_gxx_header.footer_size)
    #         actual = GxxAnimationInfoSection.from_bytes(raw, header=file_one_gxx_header)
    #         assert GxxAnimationInfoSection.verify_filler(actual)

    #     expected = file_one_gxx_animation_info_section

    #     assert actual == expected