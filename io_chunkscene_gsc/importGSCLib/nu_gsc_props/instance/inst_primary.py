from struct import pack, unpack
import os
import bpy
import math
import mathutils

def get_INST_1st(f):
    
    f.seek(0)
    INSTread = f.read()
    INSTfound = INSTread.find(b"\x49\x4E\x53\x54")
    if INSTread != 0:
        f.seek(INSTfound, 0)
        f.seek(8,1)
        INSTcount = unpack("<I", f.read(4))[0]
        unk01 = unpack("<I", f.read(4))[0]
        for i in range(INSTcount):
            ScaleX = unpack("<f", f.read(4))[0]
            rotationz = unpack("<f", f.read(4))[0]
            rotationy = unpack("<f", f.read(4))[0]
            null1 = unpack("<f", f.read(4))[0]
            nrotationz = unpack("<f", f.read(4))[0]
            ScaleY = unpack("<f", f.read(4))[0]
            rotationx = unpack("<f", f.read(4))[0]
            nrotationy = unpack("<f", f.read(4))[0]
            null2 = unpack("<f", f.read(4))[0]
            nrotationx = unpack("<f", f.read(4))[0]
            ScaleZ = unpack("<f", f.read(4))[0]
            null3 = unpack("<f", f.read(4))[0]
            posx = unpack("<f", f.read(4))[0]
            posy = unpack("<f", f.read(4))[0]
            posz = unpack("<f", f.read(4))[0]
            ScaleW = unpack("<f", f.read(4))[0]
            f.seek(16,1)
            bpy.ops.object.empty_add(type='CUBE', align='WORLD', location=([posx, posz,posy]), scale=([ScaleX, ScaleY, ScaleZ]))
    else:
        raise Exception("no INST found")
