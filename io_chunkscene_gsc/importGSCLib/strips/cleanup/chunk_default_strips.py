from struct import unpack, pack
import os
import bpy
import math
from io import BytesIO as bio

def wholeChunk1_default(f):
    fa_def=-1
    fb_def=0
    fc_def=1

    verts_def=[]
    faces_def=[]
    
    f.seek(0)
    Chunks3 = f.read()
    f.seek(0)
    while f.tell() < len(Chunks3):
        Chunk3 = f.read(4)
        if Chunk3 == b"\x03\x01\x00\x01":
            f.seek(2,1)
            vertexCount3 = unpack("B", f.read(1))[0]
            flagsssss3 = unpack("B", f.read(1))[0]
            if flagsssss3 == 0x6C:
                if vertexCount3 == 0:
                    pass
                if vertexCount3 == 1:
                    pass
                if vertexCount3 == 2:
                    pass
                if vertexCount3 == 3:
                    
                    for j in range(1):
                        default_vx = unpack("<f", f.read(4))[0]
                        default_vy = unpack("<f", f.read(4))[0]
                        default_vz = unpack("<f", f.read(4))[0]
                        default_type4 = unpack("B", f.read(1))[0]
                        default_value1 = unpack("B", f.read(1))[0]
                        default_nz = unpack("<h", f.read(2))[0]
                        default_vx1 = unpack("<f", f.read(4))[0]
                        default_vy1 = unpack("<f", f.read(4))[0]
                        default_vz1 = unpack("<f", f.read(4))[0]
                        default_type41 = unpack("B", f.read(1))[0]
                        default_value11 = unpack("B", f.read(1))[0]
                        default_nz1 = unpack("<h", f.read(2))[0]
                        default_vx2 = unpack("<f", f.read(4))[0]
                        default_vy2 = unpack("<f", f.read(4))[0]
                        default_vz2 = unpack("<f", f.read(4))[0]
                        default_type42 = unpack("B", f.read(1))[0]
                        default_value12 = unpack("B", f.read(1))[0]
                        default_nz2 = unpack("<h", f.read(2))[0]
                        if default_type4 == 1 and default_type41 == 1 and default_type42 == 0:
                            pass
                            
