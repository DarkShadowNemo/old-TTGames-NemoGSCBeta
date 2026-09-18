from struct import unpack, pack
import os
import bpy
import math
from io import BytesIO as bio

def wholeChunk1_default(f):
    fa_def=-3
    fb_def=-2
    fc_def=-1

    fa_def1=-4
    fb_def1=-3
    fc_def1=-2
    fd_def1=-1

    fa_def2=-5
    fb_def2=-4
    fc_def2=-3
    fd_def2=-2
    fe_def2=-1

    verts_def=[]
    faces_def=[]

    verts_def1=[]
    faces_def1=[]

    verts_def2=[]
    faces_def2=[]
    
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
                                        verts_def.append([default_vx,default_vz,default_vy])
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
                            if default_type4_ == 1:
                                if default_type41_ == 1:
                                    if default_type42_ == 0:
                                        if default_type43_ == 0:
                                            verts_def1.append([default_vx_,default_vz_,default_vy_])
                                            verts_def1.append([default_vx1_,default_vz1_,default_vy1_])
                                            verts_def1.append([default_vx2_,default_vz2_,default_vy2_])
                                            verts_def1.append([default_vx3_,default_vz3_,default_vy3_])

                                            fa_def1+=1*4
                                            fb_def1+=1*4
                                            fc_def1+=1*4
                                            fd_def1+=1*4
                                            faces_def1.append([fa_def1,fb_def1,fc_def1])
                                            faces_def1.append([fb_def1,fc_def1,fd_def1])
                elif vertexCount3 == 5:
                    for i in range(1):
                        default_vx_1 = unpack("<f", f.read(4))[0]
                        default_vy_1 = unpack("<f", f.read(4))[0]
                        default_vz_1 = unpack("<f", f.read(4))[0]
                        default_type4_1 = unpack("B", f.read(1))[0]
                        default_value1_1 = unpack("B", f.read(1))[0]
                        default_nz_1 = unpack("<h", f.read(2))[0]
                        default_vx1_2 = unpack("<f", f.read(4))[0]
                        default_vy1_2 = unpack("<f", f.read(4))[0]
                        default_vz1_2 = unpack("<f", f.read(4))[0]
                        default_type41_2 = unpack("B", f.read(1))[0]
                        default_value11_2 = unpack("B", f.read(1))[0]
                        default_nz1_2 = unpack("<h", f.read(2))[0]
                        default_vx2_3 = unpack("<f", f.read(4))[0]
                        default_vy2_3 = unpack("<f", f.read(4))[0]
                        default_vz2_3 = unpack("<f", f.read(4))[0]
                        default_type42_3 = unpack("B", f.read(1))[0]
                        default_value12_3 = unpack("B", f.read(1))[0]
                        default_nz3_3 = unpack("<h", f.read(2))[0]
                        default_vx3_4 = unpack("<f", f.read(4))[0]
                        default_vy3_4 = unpack("<f", f.read(4))[0]
                        default_vz3_4 = unpack("<f", f.read(4))[0]
                        default_type43_4 = unpack("B", f.read(1))[0]
                        default_value13_4 = unpack("B", f.read(1))[0]
                        default_nz3_4 = unpack("<h", f.read(2))[0]
                        default_vx3_5 = unpack("<f", f.read(4))[0]
                        default_vy3_5 = unpack("<f", f.read(4))[0]
                        default_vz3_5 = unpack("<f", f.read(4))[0]
                        default_type44_5 = unpack("B", f.read(1))[0]
                        default_value13_5 = unpack("B", f.read(1))[0]
                        default_nz3_5 = unpack("<h", f.read(2))[0]
                    _00_n_offset3_default2 = unpack("<I", f.read(4))[0]
                    if _00_n_offset3_default2 == 16777473:
                        _00_n_offset4_default2 = unpack("<I", f.read(4))[0]
                        if _00_n_offset4_default2 == 335545088:
                            if default_type4_1 == 1:
                                if default_type41_2 == 1:
                                    if default_type42_3 == 0:
                                        if default_type43_4 == 0:
                                            if default_type44_5 == 0:
                                                verts_def2.append([default_vx_1,default_vz_1,default_vy_1])
                                                verts_def2.append([default_vx1_2,default_vz1_2,default_vy1_2])
                                                verts_def2.append([default_vx2_3,default_vz2_3,default_vy2_3])
                                                verts_def2.append([default_vx3_4,default_vz3_4,default_vy3_4])
                                                verts_def2.append([default_vx3_5,default_vz3_5,default_vy3_5])

                                                fa_def2+=1*5
                                                fb_def2+=1*5
                                                fc_def2+=1*5
                                                fd_def2+=1*5
                                                fe_def2+=1*5
                                                faces_def2.append([fa_def2,fb_def2,fc_def2])
                                                faces_def2.append([fb_def2,fc_def2,fd_def2])
                                                faces_def2.append([fc_def2,fd_def2,fe_def2])

                                
                            
