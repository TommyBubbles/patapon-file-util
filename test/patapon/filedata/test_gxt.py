from pytest import fixture
import sys

sys.path.insert(0, ".\\src")
from patapon.filedata import GXT
from patapon.filedata.gxt import (
    GXTFileHeader,
    GXTImageHeader,
    GXTImageBody,
    GXTPaletteHeader,
    GXTPaletteBody,
    GXTUnknown1Header,
    GXTUnknown1Body,
    GXTUnknown2Header,
    GXTUnknown2Body,
    GXTUnknown3Body
)

class TestFileOne():
    @fixture
    def file_one(self) -> str:
        return ".\\test\\files\\@unit010_01_01\\@model\\chr01_01_10_1.gxt"


    @fixture
    def file_one_gxt_header(self) -> GXTFileHeader:
        return GXTFileHeader(
            "XXG.01.0MIG.",
            0x10180,
            [0,0,0],
            0x10180,
            0x80,
            0x10100,
            0x80,
            0x10100,
            0,
            0x40,
            0x100C0
        )


    @fixture
    def file_one_gxt_image_header(self) -> GXTImageHeader:
        return GXTImageHeader(
            0x2,
            0x10000,
            0x10000,
            [0,0,0,0,0,0,0,0,0,0,0,0,0],
        )


    @fixture
    def file_one_gxt_image_body(self, file_one: str) -> GXTImageBody:
        with open(file_one, "rb") as file:
            file.seek(0x80)
            raw_image = file.read(0x10000)
        return GXTImageBody(
            raw_image
        )


    @fixture
    def file_one_gxt_palette_header(self) -> GXTPaletteHeader:
        return GXTPaletteHeader(
            0x2,
            0x40,
            0x40,
            [0,0,0,0,0,0,0,0,0,0,0,0,0],
        )
    

    @fixture
    def file_one_gxt_palette_body(self, file_one: str) -> GXTPaletteBody:
        with open(file_one, "rb") as file:
            file.seek(0x100C0)
            raw_palette = file.read(0x40)
        return GXTPaletteBody(
            list(raw_palette[4*i:4*(i+1)] for i in range(0x10))
        )


    @fixture
    def file_one_gxt_unknown_1_header(self) -> GXTUnknown1Header:
        return GXTUnknown1Header()
    

    @fixture
    def file_one_gxt_unknown_1_body(self) -> GXTUnknown1Body:
        return GXTUnknown1Body()


    @fixture
    def file_one_gxt_unknown_2_header(self) -> GXTUnknown2Header:
        return GXTUnknown2Header(
            0x0,
            0x2C,
            0x40,
            [0,0,0,0,0,0,0,0,0,0,0,0,0],
        )


    @fixture
    def file_one_gxt_unknown_2_body(self) -> GXTUnknown2Body:
        return GXTUnknown2Body(
            [-32.0, -128.00006103515625, -7.105861038469996E-15, -1.0842187160977555E-19, -3.052506144740619E-5, -8388608.0, -2063.938232421875, -1.862645149230957E-9, -4.693099242558674E-10, -512.0001220703125, 2.465190328815662E-32],
            b'\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00'
        )


    @fixture
    def file_one_gxt_unknown_3_body(self) -> GXTUnknown3Body:
        return GXTUnknown3Body(
            0xA,
            0x101C8,
            [0,0],
            0x101B0,
            0x1,
            [0,0],
            0x200,
            0x100,
            0x200,
            0x4,
            0x101C4,
            0x1,
            [0,0],
            0x1,
            0x10140,
            "chr01_01_10_1",
            [0,0,0,0,0,0]
        )


    def test_from_bytes_gxt_file_header_file_one(self, file_one: str, file_one_gxt_header: GXTFileHeader):
        assert GXTFileHeader.verify_datafield_pos()

        with open(file_one, "rb") as file:
            raw = file.read(0x40)
            actual = GXTFileHeader.from_bytes(raw)
            assert GXTFileHeader.verify_filler(actual)
        expected = file_one_gxt_header
        
        assert expected == actual


    def test_from_bytes_gxt_image_header_file_one(self, file_one: str, file_one_gxt_image_header: GXTImageHeader):
        assert GXTImageHeader.verify_datafield_pos()

        with open(file_one, "rb") as file:
            file.seek(0x40)
            raw = file.read(0x40)
            actual = GXTImageHeader.from_bytes(raw)
            assert GXTImageHeader.verify_filler(actual)
        expected = file_one_gxt_image_header

        assert expected == actual


    def test_from_bytes_gxt_palette_header_file_one(self, file_one: str, file_one_gxt_palette_header: GXTPaletteHeader):
        assert GXTPaletteHeader.verify_datafield_pos()

        with open(file_one, "rb") as file:
            file.seek(0x10080)
            raw = file.read(0x40)
            actual = GXTPaletteHeader.from_bytes(raw)
            assert GXTPaletteHeader.verify_filler(actual)
        expected = file_one_gxt_palette_header

        assert expected == actual


    def test_from_bytes_gxt_unknown_2_header_file_one(self, file_one: str, file_one_gxt_unknown_2_header: GXTUnknown2Header):
        assert GXTUnknown2Header.verify_datafield_pos()

        with open(file_one, "rb") as file:
            file.seek(0x10100)
            raw = file.read(0x40)
            actual = GXTUnknown2Header.from_bytes(raw)
            assert GXTUnknown2Header.verify_filler(actual)
        expected = file_one_gxt_unknown_2_header

        assert expected == actual


    def test_from_bytes_gxt_unknown_3_body_file_one(self, file_one: str, file_one_gxt_unknown_3_body: GXTUnknown3Body):
        assert GXTUnknown3Body.verify_datafield_pos()

        with open(file_one, "rb") as file:
            file.seek(0x10180)
            raw = file.read(0x80)
            actual = GXTUnknown3Body.from_bytes(raw)
            assert GXTUnknown3Body.verify_filler(actual)
        expected = file_one_gxt_unknown_3_body

        assert expected == actual


    def test_from_bytes_gxt_file_one(self, file_one: str,
                                    file_one_gxt_header: GXTFileHeader,
                                    file_one_gxt_image_header: GXTImageHeader,
                                    file_one_gxt_image_body: GXTImageBody,
                                    file_one_gxt_palette_header: GXTPaletteHeader,
                                    file_one_gxt_palette_body: GXTPaletteBody,
                                    file_one_gxt_unknown_1_header: GXTUnknown1Header,
                                    file_one_gxt_unknown_1_body: GXTUnknown1Body,
                                    file_one_gxt_unknown_2_header: GXTUnknown2Header,
                                    file_one_gxt_unknown_2_body: GXTUnknown2Body,
                                    file_one_gxt_unknown_3_body: GXTUnknown3Body
                                    ):
        assert GXT.verify_datafield_pos()

        with open(file_one, "rb") as file:
            raw = file.read(0x10200)
            actual = GXT.from_bytes(raw)
            assert GXT.verify_filler(actual)

        expected = GXT(
            file_one_gxt_header,
            file_one_gxt_image_header,
            file_one_gxt_image_body,
            file_one_gxt_palette_header,
            file_one_gxt_palette_body,
            file_one_gxt_unknown_1_header,
            file_one_gxt_unknown_1_body,
            file_one_gxt_unknown_2_header,
            file_one_gxt_unknown_2_body,
            file_one_gxt_unknown_3_body
        )

        assert actual == expected