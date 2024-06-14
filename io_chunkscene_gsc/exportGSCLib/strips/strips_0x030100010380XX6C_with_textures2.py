from struct import unpack, pack
import bpy
import os
import glob
import math

def vertices_0x030100010380XX6C_with_texture2_(f):
    f.write(b"NU20")
    f.write(pack("<i", -abs(16+16+16)))
    f.write(pack("<I", 6))
    f.write(pack("<I", 0))
    f.write(b"NTBL")
    f.write(pack("<I", 16))
    f.write(pack("<I", 0))
    f.write(pack("<I", 0))
    f.write(b"TST0")
    f.write(pack("<I", 16))
    f.write(pack("<I", len(bpy.data.images)))
    f.write(pack("<I", 0))
    for i, img in enumerate(bpy.data.images):
        if img.size[0] == 16 and img.size[1] == 16:
            f.write(pack("<I", 1200))
            f.write(pack("<I", 56))
            for i in range(56):
                f.write(pack("B", 0))
            f.write(pack("<H", 16))
            f.write(pack("<H", 1))
            f.write(pack("<H", 16))
            f.write(pack("<H", 0))
            f.write(pack("<I", 16))
            f.write(pack("B", 3))
            f.write(pack("B", 0))
            f.write(pack("B", 0))
            f.write(pack("B", 0x81))
            f.write(pack("<I", 1220))
            f.write(pack("<I", 1024))
            f.write(pack("<I", 1))
            f.write(pack("<I", 1))
            f.write(pack("B", 5))
            f.write(pack("B", 4))
            f.write(pack("B", 0))
            f.write(pack("B", 96))
            f.write(pack("<I", 0))
            f.write(pack("<I", 0))
            f.write(pack("B", 5))
            f.write(pack("B", 4))
            f.write(pack("B", 0))
            f.write(pack("B", 80))
            f.write(pack("<I", 32771))
            f.write(pack(">I", 16))
            f.write(pack("<I", 14))
            f.write(pack("<I", 0))
            f.write(pack("<I", 0))
            f.write(pack("<I", 0))
            f.write(pack("<I", 81))
            f.write(pack("<I", 0))
            f.write(pack("<I", 16))
            f.write(pack("<I", 16))
            f.write(pack("<I", 82))
            f.write(pack("<I", 0))
            f.write(pack("<I", 0))
            f.write(pack("<I", 0))
            f.write(pack("<I", 83))
            f.write(pack("<I", 0))
            f.write(pack("<H", 0x8000))
            f.write(pack("<I", 0))
            f.write(pack("<I", 2048))
            f.write(pack("<H", 0))
            f.write(pack("<H", 0))
            f.write(pack("<H", 0))
            idx1 = 0
            idx2 = 1
            idx3 = 2
            idx4 = 3
            for x in range(16):
                for y in range(16):
                    f.write(pack("B", int(255*img.pixels[idx1])))
                    f.write(pack("B", int(255*img.pixels[idx2])))
                    f.write(pack("B", int(255*img.pixels[idx3])))
                    f.write(pack("B", int(127*img.pixels[idx4])))
                    idx1+=4
                    idx2+=4
                    idx3+=4
                    idx4+=4
            for i in range(80):
                f.write(pack("B", 0xCD))
        elif img.size[0] == 32 and img.size[1] == 32:
            f.write(pack("<I", 4272))
            f.write(pack("<I", 56))
            for i in range(56):
                f.write(pack("B", 0))
            f.write(pack("<H", 32))
            f.write(pack("<H", 1))
            f.write(pack("<H", 32))
            f.write(pack("<H", 0))
            f.write(pack("<I", 32))
            f.write(pack("B", 3))
            f.write(pack("B", 0))
            f.write(pack("B", 0))
            f.write(pack("B", 0x81))
            f.write(pack("<I", 4292))
            f.write(pack("<I", 8192))
            f.write(pack("<I", 1))
            f.write(pack("<I", 1))
            f.write(pack("<I", 44))
            for i in range(44):
                f.write(pack("B", 0))
            f.write(pack("<I", 1610612997))
            f.write(pack("<I", 0))
            f.write(pack("<I", 0))
            f.write(pack("<I", 1342177541))
            f.write(pack("<I", 32771))
            f.write(pack(">I", 16))
            f.write(pack("<I", 14))
            f.write(pack("<I", 0))
            f.write(pack("<I", 0))
            f.write(pack("<I", 0))
            f.write(pack("<I", 81))
            f.write(pack("<I", 0))
            f.write(pack("<I", 32))
            f.write(pack("<I", 32))
            f.write(pack("<I", 82))
            f.write(pack("<I", 0))
            f.write(pack("<I", 0))
            f.write(pack("<I", 0))
            f.write(pack("<I", 83))
            f.write(pack("<I", 0))
            f.write(pack("<H", 0x8100))
            f.write(pack("<I", 0))
            f.write(pack("<I", 2048))
            f.write(pack("<H", 0))
            f.write(pack("<H", 0))
            f.write(pack("<H", 0))
            idx1 = 0
            idx2 = 1
            idx3 = 2
            idx4 = 3
            for x in range(32):
                for y in range(32):
                    f.write(pack("B", int(255*img.pixels[idx1])))
                    f.write(pack("B", int(255*img.pixels[idx2])))
                    f.write(pack("B", int(255*img.pixels[idx3])))
                    f.write(pack("B", int(127*img.pixels[idx4])))
                    idx1+=4
                    idx2+=4
                    idx3+=4
                    idx4+=4
            for i in range(80):
                f.write(pack("B", 0xCD))
        elif img.size[0] == 64 and img.size[1] == 64:
            f.write(pack("<I", 16640))
            f.write(pack("<I", 56))
            for i in range(56):
                f.write(pack("B", 0))
            f.write(pack("<H", 64))
            f.write(pack("<H", 1))
            f.write(pack("<H", 64))
            f.write(pack("<H", 0))
            f.write(pack("<I", 64))
            f.write(pack("B", 3))
            f.write(pack("B", 0))
            f.write(pack("B", 0))
            f.write(pack("B", 129))
            f.write(pack("<I", 16580))
            f.write(pack("<I", 16384))
            f.write(pack("<I", 1))
            f.write(pack("<I", 1))
            f.write(pack("<I", 44))
            for i in range(44):
                f.write(pack("B", 0))
            f.write(pack("B", 5))
            f.write(pack("B", 4))
            f.write(pack("B", 0))
            f.write(pack("B", 96))
            f.write(pack("<I", 0))
            f.write(pack("<I", 0))
            f.write(pack("B", 5))
            f.write(pack("B", 4))
            f.write(pack("B", 0))
            f.write(pack("B", 80))
            f.write(pack("<I", 32771))
            f.write(pack(">I", 16))
            f.write(pack("<I", 14))
            f.write(pack("<I", 0))
            f.write(pack("<I", 0))
            f.write(pack("<I", 0))
            f.write(pack("<I", 81))
            f.write(pack("<I", 0))
            f.write(pack("<I", 64))
            f.write(pack("<I", 64))
            f.write(pack("<I", 82))
            f.write(pack("<I", 0))
            f.write(pack("<I", 0))
            f.write(pack("<I", 0))
            f.write(pack("<I", 83))
            f.write(pack("<I", 0))
            f.write(pack("<H", 0x8400))
            f.write(pack("<H", 0))
            f.write(pack("<H", 0))
            f.write(pack("<I", 2048))
            f.write(pack("<H", 0))
            f.write(pack("<H", 0))
            f.write(pack("<H", 0))
            idx1 = 0
            idx2 = 1
            idx3 = 2
            idx4 = 3
            for x in range(64):
                for y in range(64):
                    f.write(pack("B", int(255*img.pixels[idx1])))
                    f.write(pack("B", int(255*img.pixels[idx2])))
                    f.write(pack("B", int(255*img.pixels[idx3])))
                    f.write(pack("B", int(127*img.pixels[idx4])))
                    idx1+=4
                    idx2+=4
                    idx3+=4
                    idx4+=4
            for i in range(80):
                f.write(pack("B", 0xCD))

        elif img.size[0] == 256 and img.size[1] == 256:
            pass
