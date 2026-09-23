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
    fd_def1=-3
    fe_def1=-2
    ff_def1=-1

    fa_def2=-5
    fb_def2=-4
    fc_def2=-3
    fd_def2=-4
    fe_def2=-3
    ff_def2=-2
    fg_def2=-3
    fh_def2=-2
    fi_def2=-1

    fa_def3=-6
    fb_def3=-5
    fc_def3=-4
    fd_def3=-5
    fe_def3=-4
    ff_def3=-3
    fg_def3=-4
    fh_def3=-3
    fi_def3=-2
    fj_def3=-3
    fk_def3=-2
    fl_def3=-1

    fa_def3a=-6
    fb_def3a=-5
    fc_def3a=-4
    fd_def3a=-3
    fe_def3a=-2
    ff_def3a=-1

    verts_def=[]
    faces_def=[]

    verts_def1=[]
    faces_def1=[]

    verts_def2=[]
    faces_def2=[]

    verts_def3=[]
    faces_def3=[]

    verts_def3a=[]
    faces_def3a=[]

    singleDefault1=1
    singleDefault2=1
    singleDefault3=0
    singleDefault4=1
    
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
                            if default_type4 is 1:
                                if default_type41 is 1:
                                    if default_type42 is 0:
                                        verts_def.append([default_vx,default_vz,default_vy])
                                        verts_def.append([default_vx1,default_vz1,default_vy1])
                                        verts_def.append([default_vx2,default_vz2,default_vy2])

                                        fa_def+=1*3
                                        fb_def+=1*3
                                        fc_def+=1*3
                                        faces_def.append([fa_def,fb_def,fc_def])
                                    else:
                                        if default_type42 is 1:
                                            pass
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
                            if default_type4_ is 1:
                                if default_type41_ is 1:
                                    if default_type42_ is 0:
                                        if default_type43_ is 0:
                                            verts_def1.append([default_vx_,default_vz_,default_vy_])
                                            verts_def1.append([default_vx1_,default_vz1_,default_vy1_])
                                            verts_def1.append([default_vx2_,default_vz2_,default_vy2_])
                                            verts_def1.append([default_vx3_,default_vz3_,default_vy3_])

                                            fa_def1+=1*4
                                            fb_def1+=1*4
                                            fc_def1+=1*4
                                            fd_def1+=1*4
                                            fe_def1+=1*4
                                            ff_def1+=1*4
                                            faces_def1.append([fa_def1,fb_def1,fc_def1])
                                            faces_def1.append([fd_def1,fe_def1,ff_def1])
                                    else:
                                        if default_type42_ is 1:
                                            if default_type43_ is 1:
                                                pass
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
                            if default_type4_1 is 1:
                                if default_type41_2 is 1:
                                    if default_type42_3 is 0:
                                        if default_type43_4 is 0:
                                            if default_type44_5 is 0:
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
                                                ff_def2+=1*5
                                                fg_def2+=1*5
                                                fh_def2+=1*5
                                                fi_def2+=1*5
                                                fj_def2+=1*5
                                                fk_def2+=1*5
                                                fl_def2+=1*5
                                                faces_def2.append([fa_def2,fb_def2,fc_def2])
                                                faces_def2.append([fd_def2,fe_def2,ff_def2])
                                                faces_def2.append([fg_def2,fh_def2,fi_def2])
                                                faces_def2.append([fj_def2,fk_def2,fl_def2])
                                    else:
                                        if default_type42_3 is 1:
                                            if default_type43_4 is 1:
                                                if default_type44_5 is 1:
                                                    pass
                                                
                elif vertexCount3 == 6:
                    for i in range(1):
                        default_vx_1_ = unpack("<f", f.read(4))[0]
                        default_vy_1_ = unpack("<f", f.read(4))[0]
                        default_vz_1_ = unpack("<f", f.read(4))[0]
                        default_type4_1_ = unpack("B", f.read(1))[0]
                        default_value1_1_ = unpack("B", f.read(1))[0]
                        default_nz_1_ = unpack("<h", f.read(2))[0]
                        default_vx1_2_ = unpack("<f", f.read(4))[0]
                        default_vy1_2_ = unpack("<f", f.read(4))[0]
                        default_vz1_2_ = unpack("<f", f.read(4))[0]
                        default_type41_2_ = unpack("B", f.read(1))[0]
                        default_value11_2_ = unpack("B", f.read(1))[0]
                        default_nz1_2_ = unpack("<h", f.read(2))[0]
                        default_vx2_3_ = unpack("<f", f.read(4))[0]
                        default_vy2_3_ = unpack("<f", f.read(4))[0]
                        default_vz2_3_ = unpack("<f", f.read(4))[0]
                        default_type42_3_ = unpack("B", f.read(1))[0]
                        default_value12_3_ = unpack("B", f.read(1))[0]
                        default_nz3_3_ = unpack("<h", f.read(2))[0]
                        default_vx3_4_ = unpack("<f", f.read(4))[0]
                        default_vy3_4_ = unpack("<f", f.read(4))[0]
                        default_vz3_4_ = unpack("<f", f.read(4))[0]
                        default_type43_4_ = unpack("B", f.read(1))[0]
                        default_value13_4_ = unpack("B", f.read(1))[0]
                        default_nz3_4_ = unpack("<h", f.read(2))[0]
                        default_vx3_5_ = unpack("<f", f.read(4))[0]
                        default_vy3_5_ = unpack("<f", f.read(4))[0]
                        default_vz3_5_ = unpack("<f", f.read(4))[0]
                        default_type44_5_ = unpack("B", f.read(1))[0]
                        default_value13_5_ = unpack("B", f.read(1))[0]
                        default_nz3_5_ = unpack("<h", f.read(2))[0]
                        default_vx_6_ = unpack("<f", f.read(4))[0]
                        default_vy_6_ = unpack("<f", f.read(4))[0]
                        default_vz_6_ = unpack("<f", f.read(4))[0]
                        default_type4_6_ = unpack("B", f.read(1))[0]
                        default_value1_6_ = unpack("B", f.read(1))[0]
                        default_nz_6_ = unpack("<h", f.read(2))[0]
                    for i in range(vertexCount3):
                        f.seek(-16,1)
                    for i in range(1):
                        default_vx_1a_ = unpack("<f", f.read(4))[0]
                        default_vy_1a_ = unpack("<f", f.read(4))[0]
                        default_vz_1a_ = unpack("<f", f.read(4))[0]
                        default_type4_1a_ = unpack("B", f.read(1))[0]
                        default_value1_1a_ = unpack("B", f.read(1))[0]
                        default_nz_1a_ = unpack("<h", f.read(2))[0]
                        default_vx1_2a_ = unpack("<f", f.read(4))[0]
                        default_vy1_2a_ = unpack("<f", f.read(4))[0]
                        default_vz1_2a_ = unpack("<f", f.read(4))[0]
                        default_type41_2a_ = unpack("B", f.read(1))[0]
                        default_value11_2a_ = unpack("B", f.read(1))[0]
                        default_nz1_2a_ = unpack("<h", f.read(2))[0]
                        default_vx2_3a_ = unpack("<f", f.read(4))[0]
                        default_vy2_3a_ = unpack("<f", f.read(4))[0]
                        default_vz2_3a_ = unpack("<f", f.read(4))[0]
                        default_type42_3a_ = unpack("B", f.read(1))[0]
                        default_value12_3a_ = unpack("B", f.read(1))[0]
                        default_nz3_3a_ = unpack("<h", f.read(2))[0]
                        default_vx3_4a_ = unpack("<f", f.read(4))[0]
                        default_vy3_4a_ = unpack("<f", f.read(4))[0]
                        default_vz3_4a_ = unpack("<f", f.read(4))[0]
                        default_type43_4a_ = unpack("B", f.read(1))[0]
                        default_value13_4a_ = unpack("B", f.read(1))[0]
                        default_nz3_4a_ = unpack("<h", f.read(2))[0]
                        default_vx3_5a_ = unpack("<f", f.read(4))[0]
                        default_vy3_5a_ = unpack("<f", f.read(4))[0]
                        default_vz3_5a_ = unpack("<f", f.read(4))[0]
                        default_type44_5a_ = unpack("B", f.read(1))[0]
                        default_value13_5a_ = unpack("B", f.read(1))[0]
                        default_nz3_5a_ = unpack("<h", f.read(2))[0]
                        default_vx_6a_ = unpack("<f", f.read(4))[0]
                        default_vy_6a_ = unpack("<f", f.read(4))[0]
                        default_vz_6a_ = unpack("<f", f.read(4))[0]
                        default_type4_6a_ = unpack("B", f.read(1))[0]
                        default_value1_6a_ = unpack("B", f.read(1))[0]
                        default_nz_6a_ = unpack("<h", f.read(2))[0]
                    _00_n_offset3_default3 = unpack("<I", f.read(4))[0]
                    if _00_n_offset3_default3 == 16777473:
                        _00_n_offset4_default3 = unpack("<I", f.read(4))[0]
                        if _00_n_offset4_default3 == 335545088:
                            if default_type4_1a_ is 1:
                                if default_type41_2a_ is 1:
                                    if default_type42_3a_ is 0:
                                        if default_type43_4a_ is 1:
                                            if default_type44_5a_ is 1:
                                                if default_type44_6a_ is 0:
                                                    verts_def3a.append([default_vx_1a_,default_vz_1a_,default_vy_1a_])
                                                    verts_def3a.append([default_vx1_2a_,default_vz1_2a_,default_vy1_2a_])
                                                    verts_def3a.append([default_vx2_3a_,default_vz2_3a_,default_vy2_3a_])
                                                    verts_def3a.append([default_vx3_4a_,default_vz3_4a_,default_vy3_4a_])
                                                    verts_def3a.append([default_vx3_5a_,default_vz3_5a_,default_vy3_5a_])
                                                    verts_def3a.append([default_vx3_6a_,default_vz3_6a_,default_vy3_6a_])
                                                    
                                                    fa_def3a+=1*6
                                                    fb_def3a+=1*6
                                                    fc_def3a+=1*6
                                                    fd_def3a+=1*6
                                                    fe_def3a+=1*6
                                                    ff_def3a+=1*6
                                                    faces_def3a.append([fa_def3a,fb_def3a,fc_def3a])
                                                    faces_def3a.append([fd_def3a,fe_def3a,ff_def3a])
                            if default_type4_1_ is 1:
                                if default_type41_2_ is 1:
                                    if default_type42_3_ is 0:
                                        if default_type43_4_ is 0:
                                            if default_type44_5_ is 0:
                                                if default_type44_6_ is 0:
                                                    verts_def3.append([default_vx_1_,default_vz_1_,default_vy_1_])
                                                    verts_def3.append([default_vx1_2_,default_vz1_2_,default_vy1_2_])
                                                    verts_def3.append([default_vx2_3_,default_vz2_3_,default_vy2_3_])
                                                    verts_def3.append([default_vx3_4_,default_vz3_4_,default_vy3_4_])
                                                    verts_def3.append([default_vx3_5_,default_vz3_5_,default_vy3_5_])
                                                    verts_def3.append([default_vx3_6_,default_vz3_6_,default_vy3_6_])
                                                    
                                                    fa_def3+=1*6
                                                    fb_def3+=1*6
                                                    fc_def3+=1*6
                                                    fd_def3+=1*6
                                                    fe_def3+=1*6
                                                    ff_def3+=1*6
                                                    fg_def3+=1*6
                                                    fh_def3+=1*6
                                                    fi_def3+=1*6
                                                    fj_def3+=1*6
                                                    fk_def3+=1*6
                                                    fl_def3+=1*6
                                                    faces_def3.append([fa_def3,fb_def3,fc_def3])
                                                    faces_def3.append([fd_def3,fe_def3,ff_def3])
                                                    faces_def3.append([fg_def3,fh_def3,fi_def3])
                                                    faces_def3.append([fj_def3,fk_def3,fl_def3])

                                
                            
