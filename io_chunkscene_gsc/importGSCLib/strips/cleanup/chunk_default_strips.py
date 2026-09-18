from struct import unpack, pack
import os
import bpy
import math
from io import BytesIO as bio

def wholeChunk1_default(f):
    fa_def=-3
    fb_def=-2
    fc_def=-1

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
                elif vertexCount3 == 1:
                    pass
                elif vertexCount3 == 2:
                    pass
                elif vertexCount3 == 3:
                    
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
                    _00_n_offset3_default = unpack("<I", f.read(4))[0]
                    if _00_n_offset3_default == 16777473:
                        _00_n_offset4_default = unpack("<I", f.read(4))[0]
                        if _00_n_offset4_default == 335545088:
                            if default_type4 == 1:
                                if default_type41 == 1:
                                    if default_type42 == 0:
                                        verts_def.append([default_vx,default_vz,default_vx])
                                        verts_def.append([default_vx1,default_vz1,default_vy1])
                                        verts_def.append([default_vx2,default_vz2,default_vy2])

                                        fa_def+=1*3
                                        fb_def+=1*3
                                        fc_def+=1*3
                                        faces_def.append([fa_def,fb_def,fc_def])
                elif vertexCount3 == 4:
                    for i in range(1):
                        default_vx_ = unpack("<f", f.read(4))[0]
                        default_vy_ = unpack("<f", f.read(4))[0]
                        default_vz_ = unpack("<f", f.read(4))[0]
                        default_type4_ = unpack("B", f.read(1))[0]
                        default_value1_ = unpack("B", f.read(1))[0]
                        default_nz_ = unpack("<h", f.read(2))[0]
                        default_vx1_ = unpack("<f", f.read(4))[0]
                        default_vy1_ = unpack("<f", f.read(4))[0]
                        default_vz1_ = unpack("<f", f.read(4))[0]
                        default_type41_ = unpack("B", f.read(1))[0]
                        default_value11_ = unpack("B", f.read(1))[0]
                        default_nz1_ = unpack("<h", f.read(2))[0]
                        default_vx2_ = unpack("<f", f.read(4))[0]
                        default_vy2_ = unpack("<f", f.read(4))[0]
                        default_vz2_ = unpack("<f", f.read(4))[0]
                        default_type42_ = unpack("B", f.read(1))[0]
                        default_value12_ = unpack("B", f.read(1))[0]
                        default_nz3_ = unpack("<h", f.read(2))[0]
                        default_vx3_ = unpack("<f", f.read(4))[0]
                        default_vy3_ = unpack("<f", f.read(4))[0]
                        default_vz3_ = unpack("<f", f.read(4))[0]
                        default_type43_ = unpack("B", f.read(1))[0]
                        default_value13_ = unpack("B", f.read(1))[0]
                        default_nz3_ = unpack("<h", f.read(2))[0]
                    _00_n_offset3_default1 = unpack("<I", f.read(4))[0]
                    if _00_n_offset3_default1 == 16777473:
                        _00_n_offset4_default1 = unpack("<I", f.read(4))[0]
                        if _00_n_offset4_default1 == 335545088:
                            pass

                                
                            
