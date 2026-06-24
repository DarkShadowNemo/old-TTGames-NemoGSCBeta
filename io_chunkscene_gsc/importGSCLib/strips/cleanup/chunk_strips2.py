from struct import unpack, pack
import os
import bpy
import math
from io import BytesIO as bio

def wholeChunk1_default(f):
    fa_a=-3
    fb_a=-2
    fc_a=-1
    verticesA=[]
    facesA=[]
    uvsA=[]
    vcolA=[]
    fa_b=-4
    fb_b=-3
    fc_b=-2
    fa_c=-3
    fb_c=-2
    fc_c=-1
    verticesB=[]
    facesB=[]
    uvsB=[]
    vcolB=[]
    fa_d=-5
    fb_d=-4
    fc_d=-3
    fa_e=-4
    fb_e=-3
    fc_e=-2
    fa_f=-3
    fb_f=-2
    fc_f=-1
    verticesC=[]
    facesC=[]
    uvsC=[]
    vcolC=[]
    fa_g=-6
    fb_g=-5
    fc_g=-4
    fa_g__=-3
    fb_g__=-2
    fc_g__=-1
    verticesDD=[]
    facesDD=[]
    uvsDD=[]
    vcolDD=[]
    fa_gg=-6
    fb_gg=-5
    fc_gg=-4
    fa_hh=-5
    fb_hh=-4
    fc_hh=-3
    fa_ii=-4
    fb_ii=-3
    fc_ii=-2
    fa_jj=-3
    fb_jj=-2
    fc_jj=-1
    verticesDDD=[]
    facesDDD=[]
    uvsDDD=[]
    vcolDDD=[]
    fa_k_aa=-7
    fb_k_aa=-6
    fc_k_aa=-5
    fa_l_aa=-6
    fb_l_aa=-5
    fc_l_aa=-4
    fa_m_aa=-3
    fb_m_aa=-2
    fc_m_aa=-1
    verticesEE1__=[]
    facesEE1__=[]
    uvsEE1__=[]
    vcolEE1__=[]
    fa_k_a=-7
    fb_k_a=-6
    fc_k_a=-5
    fa_l_a=-4
    fb_l_a=-3
    fc_l_a=-2
    fa_m_a=-2
    fb_m_a=-2
    fc_m_a=-1
    verticesEE1_=[]
    facesEE1_=[]
    uvsEE1_=[]
    vcolEE1_=[]
    fa_k=-7
    fb_k=-6
    fc_k=-5
    fa_l=-6
    fb_l=-5
    fc_l=-4
    fa_m=-5
    fb_m=-4
    fc_m=-3
    fa_n=-4
    fb_n=-3
    fc_n=-2
    fa_o=-3
    fb_o=-2
    fc_o=-1
    verticesE=[]
    facesE=[]
    uvsE=[]
    vcolE=[]
    f.seek(0)
    whileChunk = f.read()
    f.seek(0)
    #change while 1 to ftell to stop it from freezing
    while f.tell() < len(whileChunk):
        Chunk = f.read(4)
            
        if Chunk == b"\x03\x01\x00\x01":
            unknown__ = unpack("B", f.read(1))[0]
            value1 = unpack("B", f.read(1))[0]
            vertexCount = unpack("B", f.read(1))[0]
            flag2 = unpack("B", f.read(1))[0]
            if flag2 == 0x6C:
                if vertexCount == 0:
                    pass        
                elif vertexCount == 1:
                    pass
                elif vertexCount == 2:
                    pass
                elif vertexCount == 3:

                    for jj in range(1):
                        vx1 = unpack("<f", f.read(4))[0]
                        vy1 = unpack("<f", f.read(4))[0]
                        vz1 = unpack("<f", f.read(4))[0]
                        type1 = unpack("B", f.read(1))[0]
                        value1a1 = unpack("B", f.read(1))[0]
                        normalZ_1 = unpack("<h", f.read(2))[0]
                        vx2 = unpack("<f", f.read(4))[0]
                        vy2 = unpack("<f", f.read(4))[0]
                        vz2 = unpack("<f", f.read(4))[0]
                        type2 = unpack("B", f.read(1))[0]
                        value1a2 = unpack("B", f.read(1))[0]
                        normalZ_2 = unpack("<h", f.read(2))[0]
                        vx3 = unpack("<f", f.read(4))[0]
                        vy3 = unpack("<f", f.read(4))[0]
                        vz3 = unpack("<f", f.read(4))[0]
                        type3 = unpack("B", f.read(1))[0]
                        value1a3 = unpack("B", f.read(1))[0]
                        normalZ_3 = unpack("<h", f.read(2))[0]

                    offset1_a = unpack("<I", f.read(4))[0]
                    if offset1_a == 83886081:
                        offset1_b = unpack("<I", f.read(4))[0]
                        if offset1_b == 1828945924:
                            for i in range(1):
                                uvx_aa1_1 = unpack("<h", f.read(2))[0] / 4096
                                uvy_aa1_1 = unpack("<h", f.read(2))[0] / 4096
                                f.seek(4,1)
                                uvx_aa2_1 = unpack("<h", f.read(2))[0] / 4096
                                uvy_aa2_1 = unpack("<h", f.read(2))[0] / 4096
                                f.seek(4,1)
                                uvx_aa3_1 = unpack("<h", f.read(2))[0] / 4096
                                uvy_aa3_1 = unpack("<h", f.read(2))[0] / 4096
                                f.seek(4,1)
                            offset1c = unpack("<I", f.read(4))[0]
                            if offset1c == 83886080:
                                offset1d = unpack("<I", f.read(4))[0]
                                if offset1d == 1845739525:
                                    for i in range(1):
                                        r1_aa1_1 = unpack("B", f.read(1))[0] / 127
                                        g1_aa1_1 = unpack("B", f.read(1))[0] / 127
                                        b1_aa1_1 = unpack("B", f.read(1))[0] / 127
                                        a1_aa1_1 = unpack("B", f.read(1))[0] / 127
                                        r1_aa2_1 = unpack("B", f.read(1))[0] / 127
                                        g1_aa2_1 = unpack("B", f.read(1))[0] / 127
                                        b1_aa2_1 = unpack("B", f.read(1))[0] / 127
                                        a1_aa2_1 = unpack("B", f.read(1))[0] / 127
                                        r1_aa3_1 = unpack("B", f.read(1))[0] / 127
                                        g1_aa3_1 = unpack("B", f.read(1))[0] / 127
                                        b1_aa3_1 = unpack("B", f.read(1))[0] / 127
                                        a1_aa3_1 = unpack("B", f.read(1))[0] / 127
                                    offset1e = unpack("<I", f.read(4))[0]
                                    if offset1e == 16777473:
                                        offset3f = unpack("<I", f.read(4))[0]
                                        if offset3f == 335545088:
                                            if type1 == 1:
                                                if type2 == 1:
                                                    if type3 == 0:
                                                        verticesA.append([vx1,vz1,vy1])
                                                        verticesA.append([vx2,vz2,vy2])
                                                        verticesA.append([vx3,vz3,vy3])
                                                        fa_a+=1*3
                                                        fb_a+=1*3
                                                        fc_a+=1*3
                                                        facesA.append([fa_a,fb_a,fc_a])
                                                        uvsA.append([uvx_aa1_1,-uvy_aa1_1])
                                                        uvsA.append([uvx_aa2_1,-uvy_aa2_1])
                                                        uvsA.append([uvx_aa3_1,-uvy_aa3_1])
                                                        vcolA.append([r1_aa1_1,g1_aa1_1,b1_aa1_1,a1_aa1_1])
                                                        vcolA.append([r1_aa2_1,g1_aa2_1,b1_aa2_1,a1_aa2_1])
                                                        vcolA.append([r1_aa3_1,g1_aa3_1,b1_aa3_1,a1_aa3_1])

                            
                                                            

                elif vertexCount == 4:

                    for jj in range(1):
                        vx5 = unpack("<f", f.read(4))[0]
                        vy5 = unpack("<f", f.read(4))[0]
                        vz5 = unpack("<f", f.read(4))[0]
                        type5 = unpack("B", f.read(1))[0]
                        value1a1 = unpack("B", f.read(1))[0]
                        normalZ_1 = unpack("<h", f.read(2))[0]
                        vx6 = unpack("<f", f.read(4))[0]
                        vy6 = unpack("<f", f.read(4))[0]
                        vz6 = unpack("<f", f.read(4))[0]
                        type6 = unpack("B", f.read(1))[0]
                        value1a2 = unpack("B", f.read(1))[0]
                        normalZ_2 = unpack("<h", f.read(2))[0]
                        vx7 = unpack("<f", f.read(4))[0]
                        vy7 = unpack("<f", f.read(4))[0]
                        vz7 = unpack("<f", f.read(4))[0]
                        type7 = unpack("B", f.read(1))[0]
                        value1a3 = unpack("B", f.read(1))[0]
                        normalZ_3 = unpack("<h", f.read(2))[0]
                        vx8 = unpack("<f", f.read(4))[0]
                        vy8 = unpack("<f", f.read(4))[0]
                        vz8 = unpack("<f", f.read(4))[0]
                        type8 = unpack("B", f.read(1))[0]
                        value1a4 = unpack("B", f.read(1))[0]
                        normalZ_4 = unpack("<h", f.read(2))[0]
                        

                    offset1_a_ = unpack("<I", f.read(4))[0]
                    if offset1_a_ == 83886081:
                        offset1_b_ = unpack("<I", f.read(4))[0]
                        if offset1_b_ == 1829011460:
                            for i in range(1):
                                uvx_aa1_2 = unpack("<h", f.read(2))[0] / 4096
                                uvy_aa1_2 = unpack("<h", f.read(2))[0] / 4096
                                f.seek(4,1)
                                uvx_aa2_2 = unpack("<h", f.read(2))[0] / 4096
                                uvy_aa2_2 = unpack("<h", f.read(2))[0] / 4096
                                f.seek(4,1)
                                uvx_aa3_2 = unpack("<h", f.read(2))[0] / 4096
                                uvy_aa3_2 = unpack("<h", f.read(2))[0] / 4096
                                f.seek(4,1)
                                uvx_aa4_2 = unpack("<h", f.read(2))[0] / 4096
                                uvy_aa4_2 = unpack("<h", f.read(2))[0] / 4096
                                f.seek(4,1)
                            offset1c_ = unpack("<I", f.read(4))[0]
                            if offset1c_ == 83886080:
                                offset1d_ = unpack("<I", f.read(4))[0]
                                if offset1d_ == 1845805061:
                                    for i in range(1):
                                        r1_aa1_2 = unpack("B", f.read(1))[0] / 127
                                        g1_aa1_2 = unpack("B", f.read(1))[0] / 127
                                        b1_aa1_2 = unpack("B", f.read(1))[0] / 127
                                        a1_aa1_2 = unpack("B", f.read(1))[0] / 127
                                        r1_aa2_2 = unpack("B", f.read(1))[0] / 127
                                        g1_aa2_2 = unpack("B", f.read(1))[0] / 127
                                        b1_aa2_2 = unpack("B", f.read(1))[0] / 127
                                        a1_aa2_2 = unpack("B", f.read(1))[0] / 127
                                        r1_aa3_2 = unpack("B", f.read(1))[0] / 127
                                        g1_aa3_2 = unpack("B", f.read(1))[0] / 127
                                        b1_aa3_2 = unpack("B", f.read(1))[0] / 127
                                        a1_aa3_2 = unpack("B", f.read(1))[0] / 127
                                        r1_aa4_2 = unpack("B", f.read(1))[0] / 127
                                        g1_aa4_2 = unpack("B", f.read(1))[0] / 127
                                        b1_aa4_2 = unpack("B", f.read(1))[0] / 127
                                        a1_aa4_2 = unpack("B", f.read(1))[0] / 127
                                    offset1e_ = unpack("<I", f.read(4))[0]
                                    if offset1e_ == 16777473:
                                        offset3f_ = unpack("<I", f.read(4))[0]
                                        if offset3f_ == 335545088:
                                                
                                            if type5 == 1:
                                                if type6 == 1:
                                                    if type7 == 0:
                                                        if type8 == 0:
                                                            verticesB.append([vx5,vz5,vy5])
                                                            verticesB.append([vx6,vz6,vy6])
                                                            verticesB.append([vx7,vz7,vy7])
                                                            verticesB.append([vx8,vz8,vy8])
                                                            fa_b+=1*4
                                                            fb_b+=1*4
                                                            fc_b+=1*4
                                                            fa_c+=1*4
                                                            fb_c+=1*4
                                                            fc_c+=1*4
                                                            facesB.append([fa_b,fb_b,fc_b])
                                                            facesB.append([fa_c,fb_c,fc_c])
                                                            uvsB.append([uvx_aa1_2,-uvy_aa1_2])
                                                            uvsB.append([uvx_aa2_2,-uvy_aa2_2])
                                                            uvsB.append([uvx_aa3_2,-uvy_aa3_2])
                                                            uvsB.append([uvx_aa4_2,-uvy_aa4_2])
                                                            vcolB.append([r1_aa1_2,g1_aa1_2,b1_aa1_2,a1_aa1_2])
                                                            vcolB.append([r1_aa2_2,g1_aa2_2,b1_aa2_2,a1_aa2_2])
                                                            vcolB.append([r1_aa3_2,g1_aa3_2,b1_aa3_2,a1_aa3_2])
                                                            vcolB.append([r1_aa4_2,g1_aa4_2,b1_aa4_2,a1_aa4_2])
                            

                elif vertexCount == 5:
                    for jjj in range(1):
                        vx9 = unpack("<f", f.read(4))[0]
                        vy9 = unpack("<f", f.read(4))[0]
                        vz9 = unpack("<f", f.read(4))[0]
                        type9 = unpack("B", f.read(1))[0]
                        value1a9 = unpack("B", f.read(1))[0]
                        normalZ_9 = unpack("<h", f.read(2))[0]
                        vx10 = unpack("<f", f.read(4))[0]
                        vy10 = unpack("<f", f.read(4))[0]
                        vz10 = unpack("<f", f.read(4))[0]
                        type10 = unpack("B", f.read(1))[0]
                        value1a10 = unpack("B", f.read(1))[0]
                        normalZ_10 = unpack("<h", f.read(2))[0]
                        vx11 = unpack("<f", f.read(4))[0]
                        vy11 = unpack("<f", f.read(4))[0]
                        vz11 = unpack("<f", f.read(4))[0]
                        type11 = unpack("B", f.read(1))[0]
                        value1a11 = unpack("B", f.read(1))[0]
                        normalZ_11 = unpack("<h", f.read(2))[0]
                        vx12 = unpack("<f", f.read(4))[0]
                        vy12 = unpack("<f", f.read(4))[0]
                        vz12 = unpack("<f", f.read(4))[0]
                        type12 = unpack("B", f.read(1))[0]
                        value1a12 = unpack("B", f.read(1))[0]
                        normalZ_12 = unpack("<h", f.read(2))[0]
                        vx13 = unpack("<f", f.read(4))[0]
                        vy13 = unpack("<f", f.read(4))[0]
                        vz13 = unpack("<f", f.read(4))[0]
                        type13 = unpack("B", f.read(1))[0]
                        value1a13 = unpack("B", f.read(1))[0]
                        normalZ_13 = unpack("<h", f.read(2))[0]

                    offset1_a__ = unpack("<I", f.read(4))[0]
                    if offset1_a__ == 83886081:
                        offset1_b__ = unpack("<I", f.read(4))[0]
                        if offset1_b__ == 1829076996:
                            for i in range(1):
                                uvx_aa1_3 = unpack("<h", f.read(2))[0] / 4096
                                uvy_aa1_3 = unpack("<h", f.read(2))[0] / 4096
                                f.seek(4,1)
                                uvx_aa2_3 = unpack("<h", f.read(2))[0] / 4096
                                uvy_aa2_3 = unpack("<h", f.read(2))[0] / 4096
                                f.seek(4,1)
                                uvx_aa3_3 = unpack("<h", f.read(2))[0] / 4096
                                uvy_aa3_3 = unpack("<h", f.read(2))[0] / 4096
                                f.seek(4,1)
                                uvx_aa4_3 = unpack("<h", f.read(2))[0] / 4096
                                uvy_aa4_3 = unpack("<h", f.read(2))[0] / 4096
                                f.seek(4,1)
                                uvx_aa5_3 = unpack("<h", f.read(2))[0] / 4096
                                uvy_aa5_3 = unpack("<h", f.read(2))[0] / 4096
                                f.seek(4,1)
                            offset1c__ = unpack("<I", f.read(4))[0]
                            if offset1c__ == 83886080:
                                offset1d__ = unpack("<I", f.read(4))[0]
                                if offset1d__ == 1845870597:
                                    for i in range(1):
                                        r1_aa1_3 = unpack("B", f.read(1))[0] / 127
                                        g1_aa1_3 = unpack("B", f.read(1))[0] / 127
                                        b1_aa1_3 = unpack("B", f.read(1))[0] / 127
                                        a1_aa1_3 = unpack("B", f.read(1))[0] / 127
                                        r1_aa2_3 = unpack("B", f.read(1))[0] / 127
                                        g1_aa2_3 = unpack("B", f.read(1))[0] / 127
                                        b1_aa2_3 = unpack("B", f.read(1))[0] / 127
                                        a1_aa2_3 = unpack("B", f.read(1))[0] / 127
                                        r1_aa3_3 = unpack("B", f.read(1))[0] / 127
                                        g1_aa3_3 = unpack("B", f.read(1))[0] / 127
                                        b1_aa3_3 = unpack("B", f.read(1))[0] / 127
                                        a1_aa3_3 = unpack("B", f.read(1))[0] / 127
                                        r1_aa4_3 = unpack("B", f.read(1))[0] / 127
                                        g1_aa4_3 = unpack("B", f.read(1))[0] / 127
                                        b1_aa4_3 = unpack("B", f.read(1))[0] / 127
                                        a1_aa4_3 = unpack("B", f.read(1))[0] / 127
                                        r1_aa5_3 = unpack("B", f.read(1))[0] / 127
                                        g1_aa5_3 = unpack("B", f.read(1))[0] / 127
                                        b1_aa5_3 = unpack("B", f.read(1))[0] / 127
                                        a1_aa5_3 = unpack("B", f.read(1))[0] / 127
                                    offset1e__ = unpack("<I", f.read(4))[0]
                                    if offset1e__ == 16777473:
                                        offset3f__ = unpack("<I", f.read(4))[0]
                                        if offset3f__ == 335545088:
                                            if type9 == 1:
                                                if type10 == 1:
                                                    if type11 == 0:
                                                        if type12 == 0:
                                                            if type13 == 0:
                                                                verticesC.append([vx9,vz9,vy9])
                                                                verticesC.append([vx10,vz10,vy10])
                                                                verticesC.append([vx11,vz11,vy11])
                                                                verticesC.append([vx12,vz12,vy12])
                                                                verticesC.append([vx13,vz13,vy13])
                                                                fa_d+=1*5
                                                                fb_d+=1*5
                                                                fc_d+=1*5
                                                                fa_e+=1*5
                                                                fb_e+=1*5
                                                                fc_e+=1*5
                                                                fa_f+=1*5
                                                                fb_f+=1*5
                                                                fc_f+=1*5
                                                                facesC.append([fa_d,fb_d,fc_d])
                                                                facesC.append([fa_e,fb_e,fc_e])
                                                                facesC.append([fa_f,fb_f,fc_f])
                                                                uvsC.append([uvx_aa1_3,-uvy_aa1_3])
                                                                uvsC.append([uvx_aa2_3,-uvy_aa2_3])
                                                                uvsC.append([uvx_aa3_3,-uvy_aa3_3])
                                                                uvsC.append([uvx_aa4_3,-uvy_aa4_3])
                                                                uvsC.append([uvx_aa5_3,-uvy_aa5_3])
                                                                vcolC.append([r1_aa1_3,g1_aa1_3,b1_aa1_3,a1_aa1_3])
                                                                vcolC.append([r1_aa2_3,g1_aa2_3,b1_aa2_3,a1_aa2_3])
                                                                vcolC.append([r1_aa3_3,g1_aa3_3,b1_aa3_3,a1_aa3_3])
                                                                vcolC.append([r1_aa4_3,g1_aa4_3,b1_aa4_3,a1_aa4_3])
                                                                vcolC.append([r1_aa5_3,g1_aa5_3,b1_aa5_3,a1_aa5_3])

                elif vertexCount == 6:
                    for jjjj in range(1):
                        vx14 = unpack("<f", f.read(4))[0]
                        vy14 = unpack("<f", f.read(4))[0]
                        vz14 = unpack("<f", f.read(4))[0]
                        type14 = unpack("B", f.read(1))[0]
                        value1a14 = unpack("B", f.read(1))[0]
                        normalZ_14 = unpack("<h", f.read(2))[0]
                        vx15 = unpack("<f", f.read(4))[0]
                        vy15 = unpack("<f", f.read(4))[0]
                        vz15 = unpack("<f", f.read(4))[0]
                        type15 = unpack("B", f.read(1))[0]
                        value1a15 = unpack("B", f.read(1))[0]
                        normalZ_15 = unpack("<h", f.read(2))[0]
                        vx16 = unpack("<f", f.read(4))[0]
                        vy16 = unpack("<f", f.read(4))[0]
                        vz16 = unpack("<f", f.read(4))[0]
                        type16 = unpack("B", f.read(1))[0]
                        value1a16 = unpack("B", f.read(1))[0]
                        normalZ_16 = unpack("<h", f.read(2))[0]
                        vx17 = unpack("<f", f.read(4))[0]
                        vy17 = unpack("<f", f.read(4))[0]
                        vz17 = unpack("<f", f.read(4))[0]
                        type17 = unpack("B", f.read(1))[0]
                        value1a17 = unpack("B", f.read(1))[0]
                        normalZ_17 = unpack("<h", f.read(2))[0]
                        vx18 = unpack("<f", f.read(4))[0]
                        vy18 = unpack("<f", f.read(4))[0]
                        vz18 = unpack("<f", f.read(4))[0]
                        type18 = unpack("B", f.read(1))[0]
                        value1a18 = unpack("B", f.read(1))[0]
                        normalZ_18 = unpack("<h", f.read(2))[0]
                        vx19 = unpack("<f", f.read(4))[0]
                        vy19 = unpack("<f", f.read(4))[0]
                        vz19 = unpack("<f", f.read(4))[0]
                        type19 = unpack("B", f.read(1))[0]
                        value1a19 = unpack("B", f.read(1))[0]
                        normalZ_19 = unpack("<h", f.read(2))[0]
                    for i in range(vertexCount):
                        f.seek(-16,1)
                    for jjjj_ in range(1):
                        vx14_ = unpack("<f", f.read(4))[0]
                        vy14_ = unpack("<f", f.read(4))[0]
                        vz14_ = unpack("<f", f.read(4))[0]
                        type14_ = unpack("B", f.read(1))[0]
                        value1a14_ = unpack("B", f.read(1))[0]
                        normalZ_14_ = unpack("<h", f.read(2))[0]
                        vx15_ = unpack("<f", f.read(4))[0]
                        vy15_ = unpack("<f", f.read(4))[0]
                        vz15_ = unpack("<f", f.read(4))[0]
                        type15_ = unpack("B", f.read(1))[0]
                        value1a15_ = unpack("B", f.read(1))[0]
                        normalZ_15_ = unpack("<h", f.read(2))[0]
                        vx16_ = unpack("<f", f.read(4))[0]
                        vy16_ = unpack("<f", f.read(4))[0]
                        vz16_ = unpack("<f", f.read(4))[0]
                        type16_ = unpack("B", f.read(1))[0]
                        value1a16_ = unpack("B", f.read(1))[0]
                        normalZ_16_ = unpack("<h", f.read(2))[0]
                        vx17_ = unpack("<f", f.read(4))[0]
                        vy17_ = unpack("<f", f.read(4))[0]
                        vz17_ = unpack("<f", f.read(4))[0]
                        type17_ = unpack("B", f.read(1))[0]
                        value1a17_ = unpack("B", f.read(1))[0]
                        normalZ_17_ = unpack("<h", f.read(2))[0]
                        vx18_ = unpack("<f", f.read(4))[0]
                        vy18_ = unpack("<f", f.read(4))[0]
                        vz18_ = unpack("<f", f.read(4))[0]
                        type18_ = unpack("B", f.read(1))[0]
                        value1a18_ = unpack("B", f.read(1))[0]
                        normalZ_18_ = unpack("<h", f.read(2))[0]
                        vx19_ = unpack("<f", f.read(4))[0]
                        vy19_ = unpack("<f", f.read(4))[0]
                        vz19_ = unpack("<f", f.read(4))[0]
                        type19_ = unpack("B", f.read(1))[0]
                        value1a19_ = unpack("B", f.read(1))[0]
                        normalZ_19_ = unpack("<h", f.read(2))[0]

                    offset1_a___ = unpack("<I", f.read(4))[0]
                    if offset1_a___ == 83886081:
                        offset1_b___ = unpack("<I", f.read(4))[0]
                        if offset1_b___ == 1829142532:
                            for i in range(1):
                                uvx_aa1_4 = unpack("<h", f.read(2))[0] / 4096
                                uvy_aa1_4 = unpack("<h", f.read(2))[0] / 4096
                                f.seek(4,1)
                                uvx_aa2_4 = unpack("<h", f.read(2))[0] / 4096
                                uvy_aa2_4 = unpack("<h", f.read(2))[0] / 4096
                                f.seek(4,1)
                                uvx_aa3_4 = unpack("<h", f.read(2))[0] / 4096
                                uvy_aa3_4 = unpack("<h", f.read(2))[0] / 4096
                                f.seek(4,1)
                                uvx_aa4_4 = unpack("<h", f.read(2))[0] / 4096
                                uvy_aa4_4 = unpack("<h", f.read(2))[0] / 4096
                                f.seek(4,1)
                                uvx_aa5_4 = unpack("<h", f.read(2))[0] / 4096
                                uvy_aa5_4 = unpack("<h", f.read(2))[0] / 4096
                                f.seek(4,1)
                                uvx_aa6_4 = unpack("<h", f.read(2))[0] / 4096
                                uvy_aa6_4 = unpack("<h", f.read(2))[0] / 4096
                                f.seek(4,1)
                            for i in range(1):
                                f.seek(-48,1)
                            for i in range(1):
                                uvx_aa1_4a = unpack("<h", f.read(2))[0] / 4096
                                uvy_aa1_4a = unpack("<h", f.read(2))[0] / 4096
                                f.seek(4,1)
                                uvx_aa2_4a = unpack("<h", f.read(2))[0] / 4096
                                uvy_aa2_4a = unpack("<h", f.read(2))[0] / 4096
                                f.seek(4,1)
                                uvx_aa3_4a = unpack("<h", f.read(2))[0] / 4096
                                uvy_aa3_4a = unpack("<h", f.read(2))[0] / 4096
                                f.seek(4,1)
                                uvx_aa4_4a = unpack("<h", f.read(2))[0] / 4096
                                uvy_aa4_4a = unpack("<h", f.read(2))[0] / 4096
                                f.seek(4,1)
                                uvx_aa5_4a = unpack("<h", f.read(2))[0] / 4096
                                uvy_aa5_4a = unpack("<h", f.read(2))[0] / 4096
                                f.seek(4,1)
                                uvx_aa6_4a = unpack("<h", f.read(2))[0] / 4096
                                uvy_aa6_4a = unpack("<h", f.read(2))[0] / 4096
                                f.seek(4,1)
                            offset1c___ = unpack("<I", f.read(4))[0]
                            if offset1c___ == 83886080:
                                offset1d___ = unpack("<I", f.read(4))[0]
                                if offset1d___ == 1845936133:
                                    for i in range(1):
                                        r1_aa1_4 = unpack("B", f.read(1))[0] / 127
                                        g1_aa1_4 = unpack("B", f.read(1))[0] / 127
                                        b1_aa1_4 = unpack("B", f.read(1))[0] / 127
                                        a1_aa1_4 = unpack("B", f.read(1))[0] / 127
                                        r1_aa2_4 = unpack("B", f.read(1))[0] / 127
                                        g1_aa2_4 = unpack("B", f.read(1))[0] / 127
                                        b1_aa2_4 = unpack("B", f.read(1))[0] / 127
                                        a1_aa2_4 = unpack("B", f.read(1))[0] / 127
                                        r1_aa3_4 = unpack("B", f.read(1))[0] / 127
                                        g1_aa3_4 = unpack("B", f.read(1))[0] / 127
                                        b1_aa3_4 = unpack("B", f.read(1))[0] / 127
                                        a1_aa3_4 = unpack("B", f.read(1))[0] / 127
                                        r1_aa4_4 = unpack("B", f.read(1))[0] / 127
                                        g1_aa4_4 = unpack("B", f.read(1))[0] / 127
                                        b1_aa4_4 = unpack("B", f.read(1))[0] / 127
                                        a1_aa4_4 = unpack("B", f.read(1))[0] / 127
                                        r1_aa5_4 = unpack("B", f.read(1))[0] / 127
                                        g1_aa5_4 = unpack("B", f.read(1))[0] / 127
                                        b1_aa5_4 = unpack("B", f.read(1))[0] / 127
                                        a1_aa5_4 = unpack("B", f.read(1))[0] / 127
                                        r1_aa6_4 = unpack("B", f.read(1))[0] / 127
                                        g1_aa6_4 = unpack("B", f.read(1))[0] / 127
                                        b1_aa6_4 = unpack("B", f.read(1))[0] / 127
                                        a1_aa6_4 = unpack("B", f.read(1))[0] / 127
                                    for i in range(1):
                                        f.seek(-24,1)
                                    for i in range(1):
                                        r1_aa1_4a = unpack("B", f.read(1))[0] / 127
                                        g1_aa1_4a = unpack("B", f.read(1))[0] / 127
                                        b1_aa1_4a = unpack("B", f.read(1))[0] / 127
                                        a1_aa1_4a = unpack("B", f.read(1))[0] / 127
                                        r1_aa2_4a = unpack("B", f.read(1))[0] / 127
                                        g1_aa2_4a = unpack("B", f.read(1))[0] / 127
                                        b1_aa2_4a = unpack("B", f.read(1))[0] / 127
                                        a1_aa2_4a = unpack("B", f.read(1))[0] / 127
                                        r1_aa3_4a = unpack("B", f.read(1))[0] / 127
                                        g1_aa3_4a = unpack("B", f.read(1))[0] / 127
                                        b1_aa3_4a = unpack("B", f.read(1))[0] / 127
                                        a1_aa3_4a = unpack("B", f.read(1))[0] / 127
                                        r1_aa4_4a = unpack("B", f.read(1))[0] / 127
                                        g1_aa4_4a = unpack("B", f.read(1))[0] / 127
                                        b1_aa4_4a = unpack("B", f.read(1))[0] / 127
                                        a1_aa4_4a = unpack("B", f.read(1))[0] / 127
                                        r1_aa5_4a = unpack("B", f.read(1))[0] / 127
                                        g1_aa5_4a = unpack("B", f.read(1))[0] / 127
                                        b1_aa5_4a = unpack("B", f.read(1))[0] / 127
                                        a1_aa5_4a = unpack("B", f.read(1))[0] / 127
                                        r1_aa6_4a = unpack("B", f.read(1))[0] / 127
                                        g1_aa6_4a = unpack("B", f.read(1))[0] / 127
                                        b1_aa6_4a = unpack("B", f.read(1))[0] / 127
                                        a1_aa6_4a = unpack("B", f.read(1))[0] / 127
                                    offset1e___ = unpack("<I", f.read(4))[0]
                                    if offset1e___ == 16777473:
                                        offset3f___ = unpack("<I", f.read(4))[0]
                                        if offset3f___ == 335545088:
                                            if type14 == 1:
                                                if type15 == 1:
                                                    if type16 == 0:
                                                        if type17 == 1:
                                                            if type18 == 1:
                                                                if type19 == 0:
                                                                    verticesDD.append([vx14,vz14,vy14])
                                                                    verticesDD.append([vx15,vz15,vy15])
                                                                    verticesDD.append([vx16,vz16,vy16])
                                                                    verticesDD.append([vx17,vz17,vy17])
                                                                    verticesDD.append([vx18,vz18,vy18])
                                                                    verticesDD.append([vx19,vz19,vy19])
                                                                    fa_g+=1*6
                                                                    fb_g+=1*6
                                                                    fc_g+=1*6
                                                                    fa_g__+=1*6
                                                                    fb_g__+=1*6
                                                                    fc_g__+=1*6
                                                                    
                                                                    facesDD.append([fa_g,fb_g,fc_g])
                                                                    facesDD.append([fa_g__,fb_g__,fc_g__])
                                                                    uvsDD.append([uvx_aa1_4,-uvy_aa1_4])
                                                                    uvsDD.append([uvx_aa2_4,-uvy_aa2_4])
                                                                    uvsDD.append([uvx_aa3_4,-uvy_aa3_4])
                                                                    uvsDD.append([uvx_aa4_4,-uvy_aa4_4])
                                                                    uvsDD.append([uvx_aa5_4,-uvy_aa5_4])
                                                                    uvsDD.append([uvx_aa6_4,-uvy_aa6_4])
                                                                    vcolDD.append([r1_aa1_4,g1_aa1_4,b1_aa1_4,a1_aa1_4])
                                                                    vcolDD.append([r1_aa2_4,g1_aa2_4,b1_aa2_4,a1_aa2_4])
                                                                    vcolDD.append([r1_aa3_4,g1_aa3_4,b1_aa3_4,a1_aa3_4])
                                                                    vcolDD.append([r1_aa4_4,g1_aa4_4,b1_aa4_4,a1_aa4_4])
                                                                    vcolDD.append([r1_aa5_4,g1_aa5_4,b1_aa5_4,a1_aa5_4])
                                                                    vcolDD.append([r1_aa6_4,g1_aa6_4,b1_aa6_4,a1_aa6_4])
                                            if type14_ == 1:
                                                if type15_ == 1:
                                                    if type16_ == 0:
                                                        if type17_ == 0:
                                                            if type18_ == 0:
                                                                if type19_ == 0:
                                                                    verticesDDD.append([vx14_,vz14_,vy14_])
                                                                    verticesDDD.append([vx15_,vz15_,vy15_])
                                                                    verticesDDD.append([vx16_,vz16_,vy16_])
                                                                    verticesDDD.append([vx17_,vz17_,vy17_])
                                                                    verticesDDD.append([vx18_,vz18_,vy18_])
                                                                    verticesDDD.append([vx19_,vz19_,vy19_])
                                                                    fa_gg+=1*6
                                                                    fb_gg+=1*6
                                                                    fc_gg+=1*6
                                                                    fa_hh+=1*6
                                                                    fb_hh+=1*6
                                                                    fc_hh+=1*6
                                                                    fa_ii+=1*6
                                                                    fb_ii+=1*6
                                                                    fc_ii+=1*6
                                                                    fa_jj+=1*6
                                                                    fb_jj+=1*6
                                                                    fc_jj+=1*6
                                                                    facesDDD.append([fa_gg,fb_gg,fc_gg])
                                                                    facesDDD.append([fa_hh,fb_hh,fc_hh])
                                                                    facesDDD.append([fa_ii,fb_ii,fc_ii])
                                                                    facesDDD.append([fa_jj,fb_jj,fc_jj])
                                                                    uvsDDD.append([uvx_aa1_4a,-uvy_aa1_4a])
                                                                    uvsDDD.append([uvx_aa2_4a,-uvy_aa2_4a])
                                                                    uvsDDD.append([uvx_aa3_4a,-uvy_aa3_4a])
                                                                    uvsDDD.append([uvx_aa4_4a,-uvy_aa4_4a])
                                                                    uvsDDD.append([uvx_aa5_4a,-uvy_aa5_4a])
                                                                    uvsDDD.append([uvx_aa6_4a,-uvy_aa6_4a])
                                                                    vcolDDD.append([r1_aa1_4a,g1_aa1_4a,b1_aa1_4a,a1_aa1_4a])
                                                                    vcolDDD.append([r1_aa2_4a,g1_aa2_4a,b1_aa2_4a,a1_aa2_4a])
                                                                    vcolDDD.append([r1_aa3_4a,g1_aa3_4a,b1_aa3_4a,a1_aa3_4a])
                                                                    vcolDDD.append([r1_aa4_4a,g1_aa4_4a,b1_aa4_4a,a1_aa4_4a])
                                                                    vcolDDD.append([r1_aa5_4a,g1_aa5_4a,b1_aa5_4a,a1_aa5_4a])
                                                                    vcolDDD.append([r1_aa6_4a,g1_aa6_4a,b1_aa6_4a,a1_aa6_4a])
                                                        

                elif vertexCount == 7:

                    for jjjj in range(1):
                        vx20 = unpack("<f", f.read(4))[0]
                        vy20 = unpack("<f", f.read(4))[0]
                        vz20 = unpack("<f", f.read(4))[0]
                        type20 = unpack("B", f.read(1))[0]
                        value1a20 = unpack("B", f.read(1))[0]
                        normalZ_20 = unpack("<h", f.read(2))[0]
                        vx21 = unpack("<f", f.read(4))[0]
                        vy21 = unpack("<f", f.read(4))[0]
                        vz21 = unpack("<f", f.read(4))[0]
                        type21 = unpack("B", f.read(1))[0]
                        value1a21 = unpack("B", f.read(1))[0]
                        normalZ_21 = unpack("<h", f.read(2))[0]
                        vx22 = unpack("<f", f.read(4))[0]
                        vy22 = unpack("<f", f.read(4))[0]
                        vz22 = unpack("<f", f.read(4))[0]
                        type22 = unpack("B", f.read(1))[0]
                        value1a22 = unpack("B", f.read(1))[0]
                        normalZ_22 = unpack("<h", f.read(2))[0]
                        vx23 = unpack("<f", f.read(4))[0]
                        vy23 = unpack("<f", f.read(4))[0]
                        vz23 = unpack("<f", f.read(4))[0]
                        type23 = unpack("B", f.read(1))[0]
                        value1a23 = unpack("B", f.read(1))[0]
                        normalZ_23 = unpack("<h", f.read(2))[0]
                        vx24 = unpack("<f", f.read(4))[0]
                        vy24 = unpack("<f", f.read(4))[0]
                        vz24 = unpack("<f", f.read(4))[0]
                        type24 = unpack("B", f.read(1))[0]
                        value1a24 = unpack("B", f.read(1))[0]
                        normalZ_24 = unpack("<h", f.read(2))[0]
                        vx25 = unpack("<f", f.read(4))[0]
                        vy25 = unpack("<f", f.read(4))[0]
                        vz25 = unpack("<f", f.read(4))[0]
                        type25 = unpack("B", f.read(1))[0]
                        value1a25 = unpack("B", f.read(1))[0]
                        normalZ_25 = unpack("<h", f.read(2))[0]
                        vx26 = unpack("<f", f.read(4))[0]
                        vy26 = unpack("<f", f.read(4))[0]
                        vz26 = unpack("<f", f.read(4))[0]
                        type26 = unpack("B", f.read(1))[0]
                        value1a26 = unpack("B", f.read(1))[0]
                        normalZ_26 = unpack("<h", f.read(2))[0]
                    for jjjj_ in range(vertexCount):
                        f.seek(-16,1)
                    for jjjj in range(1):
                        vx20_ = unpack("<f", f.read(4))[0]
                        vy20_ = unpack("<f", f.read(4))[0]
                        vz20_ = unpack("<f", f.read(4))[0]
                        type20_ = unpack("B", f.read(1))[0]
                        value1a20_ = unpack("B", f.read(1))[0]
                        normalZ_20_ = unpack("<h", f.read(2))[0]
                        vx21_ = unpack("<f", f.read(4))[0]
                        vy21_ = unpack("<f", f.read(4))[0]
                        vz21_ = unpack("<f", f.read(4))[0]
                        type21_ = unpack("B", f.read(1))[0]
                        value1a21_ = unpack("B", f.read(1))[0]
                        normalZ_21_ = unpack("<h", f.read(2))[0]
                        vx22_ = unpack("<f", f.read(4))[0]
                        vy22_ = unpack("<f", f.read(4))[0]
                        vz22_ = unpack("<f", f.read(4))[0]
                        type22_ = unpack("B", f.read(1))[0]
                        value1a22_ = unpack("B", f.read(1))[0]
                        normalZ_22_ = unpack("<h", f.read(2))[0]
                        vx23_ = unpack("<f", f.read(4))[0]
                        vy23_ = unpack("<f", f.read(4))[0]
                        vz23_ = unpack("<f", f.read(4))[0]
                        type23_ = unpack("B", f.read(1))[0]
                        value1a23_ = unpack("B", f.read(1))[0]
                        normalZ_23_ = unpack("<h", f.read(2))[0]
                        vx24_ = unpack("<f", f.read(4))[0]
                        vy24_ = unpack("<f", f.read(4))[0]
                        vz24_ = unpack("<f", f.read(4))[0]
                        type24_ = unpack("B", f.read(1))[0]
                        value1a24_ = unpack("B", f.read(1))[0]
                        normalZ_24_ = unpack("<h", f.read(2))[0]
                        vx25_ = unpack("<f", f.read(4))[0]
                        vy25_ = unpack("<f", f.read(4))[0]
                        vz25_ = unpack("<f", f.read(4))[0]
                        type25_ = unpack("B", f.read(1))[0]
                        value1a25_ = unpack("B", f.read(1))[0]
                        normalZ_25_ = unpack("<h", f.read(2))[0]
                        vx26_ = unpack("<f", f.read(4))[0]
                        vy26_ = unpack("<f", f.read(4))[0]
                        vz26_ = unpack("<f", f.read(4))[0]
                        type26_ = unpack("B", f.read(1))[0]
                        value1a26_ = unpack("B", f.read(1))[0]
                        normalZ_26_ = unpack("<h", f.read(2))[0]

                    for jjjj_ in range(vertexCount):
                        f.seek(-16,1)
                    for jjjj in range(1):
                        vx20__ = unpack("<f", f.read(4))[0]
                        vy20__ = unpack("<f", f.read(4))[0]
                        vz20__ = unpack("<f", f.read(4))[0]
                        type20__ = unpack("B", f.read(1))[0]
                        value1a20__ = unpack("B", f.read(1))[0]
                        normalZ_20__ = unpack("<h", f.read(2))[0]
                        vx21__ = unpack("<f", f.read(4))[0]
                        vy21__ = unpack("<f", f.read(4))[0]
                        vz21__ = unpack("<f", f.read(4))[0]
                        type21__ = unpack("B", f.read(1))[0]
                        value1a21__ = unpack("B", f.read(1))[0]
                        normalZ_21__ = unpack("<h", f.read(2))[0]
                        vx22__ = unpack("<f", f.read(4))[0]
                        vy22__ = unpack("<f", f.read(4))[0]
                        vz22__ = unpack("<f", f.read(4))[0]
                        type22__ = unpack("B", f.read(1))[0]
                        value1a22__ = unpack("B", f.read(1))[0]
                        normalZ_22__ = unpack("<h", f.read(2))[0]
                        vx23__ = unpack("<f", f.read(4))[0]
                        vy23__ = unpack("<f", f.read(4))[0]
                        vz23__ = unpack("<f", f.read(4))[0]
                        type23__ = unpack("B", f.read(1))[0]
                        value1a23__ = unpack("B", f.read(1))[0]
                        normalZ_23__ = unpack("<h", f.read(2))[0]
                        vx24__ = unpack("<f", f.read(4))[0]
                        vy24__ = unpack("<f", f.read(4))[0]
                        vz24__ = unpack("<f", f.read(4))[0]
                        type24__ = unpack("B", f.read(1))[0]
                        value1a24__ = unpack("B", f.read(1))[0]
                        normalZ_24__ = unpack("<h", f.read(2))[0]
                        vx25__ = unpack("<f", f.read(4))[0]
                        vy25__ = unpack("<f", f.read(4))[0]
                        vz25__ = unpack("<f", f.read(4))[0]
                        type25__ = unpack("B", f.read(1))[0]
                        value1a25__ = unpack("B", f.read(1))[0]
                        normalZ_25__ = unpack("<h", f.read(2))[0]
                        vx26__ = unpack("<f", f.read(4))[0]
                        vy26__ = unpack("<f", f.read(4))[0]
                        vz26__ = unpack("<f", f.read(4))[0]
                        type26__ = unpack("B", f.read(1))[0]
                        value1a26__ = unpack("B", f.read(1))[0]
                        normalZ_26__ = unpack("<h", f.read(2))[0]

                    offset1_a____ = unpack("<I", f.read(4))[0]
                    if offset1_a____ == 83886081:
                        offset1_b____ = unpack("<I", f.read(4))[0]
                        if offset1_b____ == 1829208068:
                            for i in range(1):
                                uvx_aa1_5 = unpack("<h", f.read(2))[0] / 4096
                                uvy_aa1_5 = unpack("<h", f.read(2))[0] / 4096
                                f.seek(4,1)
                                uvx_aa2_5 = unpack("<h", f.read(2))[0] / 4096
                                uvy_aa2_5 = unpack("<h", f.read(2))[0] / 4096
                                f.seek(4,1)
                                uvx_aa3_5 = unpack("<h", f.read(2))[0] / 4096
                                uvy_aa3_5 = unpack("<h", f.read(2))[0] / 4096
                                f.seek(4,1)
                                uvx_aa4_5 = unpack("<h", f.read(2))[0] / 4096
                                uvy_aa4_5 = unpack("<h", f.read(2))[0] / 4096
                                f.seek(4,1)
                                uvx_aa5_5 = unpack("<h", f.read(2))[0] / 4096
                                uvy_aa5_5 = unpack("<h", f.read(2))[0] / 4096
                                f.seek(4,1)
                                uvx_aa6_5 = unpack("<h", f.read(2))[0] / 4096
                                uvy_aa6_5 = unpack("<h", f.read(2))[0] / 4096
                                f.seek(4,1)
                                uvx_aa7_5 = unpack("<h", f.read(2))[0] / 4096
                                uvy_aa7_5 = unpack("<h", f.read(2))[0] / 4096
                                f.seek(4,1)
                            for i in range(1):
                                f.seek(-56,1)
                            for i in range(1):
                                uvx_aa1_5_ = unpack("<h", f.read(2))[0] / 4096
                                uvy_aa1_5_ = unpack("<h", f.read(2))[0] / 4096
                                f.seek(4,1)
                                uvx_aa2_5_ = unpack("<h", f.read(2))[0] / 4096
                                uvy_aa2_5_ = unpack("<h", f.read(2))[0] / 4096
                                f.seek(4,1)
                                uvx_aa3_5_ = unpack("<h", f.read(2))[0] / 4096
                                uvy_aa3_5_ = unpack("<h", f.read(2))[0] / 4096
                                f.seek(4,1)
                                uvx_aa4_5_ = unpack("<h", f.read(2))[0] / 4096
                                uvy_aa4_5_ = unpack("<h", f.read(2))[0] / 4096
                                f.seek(4,1)
                                uvx_aa5_5_ = unpack("<h", f.read(2))[0] / 4096
                                uvy_aa5_5_ = unpack("<h", f.read(2))[0] / 4096
                                f.seek(4,1)
                                uvx_aa6_5_ = unpack("<h", f.read(2))[0] / 4096
                                uvy_aa6_5_ = unpack("<h", f.read(2))[0] / 4096
                                f.seek(4,1)
                                uvx_aa7_5_ = unpack("<h", f.read(2))[0] / 4096
                                uvy_aa7_5_ = unpack("<h", f.read(2))[0] / 4096
                                f.seek(4,1)
                            for i in range(1):
                                f.seek(-56,1)
                            for i in range(1):
                                uvx_aa1_5__ = unpack("<h", f.read(2))[0] / 4096
                                uvy_aa1_5__ = unpack("<h", f.read(2))[0] / 4096
                                f.seek(4,1)
                                uvx_aa2_5__ = unpack("<h", f.read(2))[0] / 4096
                                uvy_aa2_5__ = unpack("<h", f.read(2))[0] / 4096
                                f.seek(4,1)
                                uvx_aa3_5__ = unpack("<h", f.read(2))[0] / 4096
                                uvy_aa3_5__ = unpack("<h", f.read(2))[0] / 4096
                                f.seek(4,1)
                                uvx_aa4_5__ = unpack("<h", f.read(2))[0] / 4096
                                uvy_aa4_5__ = unpack("<h", f.read(2))[0] / 4096
                                f.seek(4,1)
                                uvx_aa5_5__ = unpack("<h", f.read(2))[0] / 4096
                                uvy_aa5_5__ = unpack("<h", f.read(2))[0] / 4096
                                f.seek(4,1)
                                uvx_aa6_5__ = unpack("<h", f.read(2))[0] / 4096
                                uvy_aa6_5__ = unpack("<h", f.read(2))[0] / 4096
                                f.seek(4,1)
                                uvx_aa7_5__ = unpack("<h", f.read(2))[0] / 4096
                                uvy_aa7_5__ = unpack("<h", f.read(2))[0] / 4096
                                f.seek(4,1)
                            offset1c____ = unpack("<I", f.read(4))[0]
                            if offset1c____ == 83886080:
                                offset1d____ = unpack("<I", f.read(4))[0]
                                if offset1d____ == 1846001669:
                                    for i in range(1):
                                        r1_aa1_5 = unpack("B", f.read(1))[0] / 127
                                        g1_aa1_5 = unpack("B", f.read(1))[0] / 127
                                        b1_aa1_5 = unpack("B", f.read(1))[0] / 127
                                        a1_aa1_5 = unpack("B", f.read(1))[0] / 127
                                        r1_aa2_5 = unpack("B", f.read(1))[0] / 127
                                        g1_aa2_5 = unpack("B", f.read(1))[0] / 127
                                        b1_aa2_5 = unpack("B", f.read(1))[0] / 127
                                        a1_aa2_5 = unpack("B", f.read(1))[0] / 127
                                        r1_aa3_5 = unpack("B", f.read(1))[0] / 127
                                        g1_aa3_5 = unpack("B", f.read(1))[0] / 127
                                        b1_aa3_5 = unpack("B", f.read(1))[0] / 127
                                        a1_aa3_5 = unpack("B", f.read(1))[0] / 127
                                        r1_aa4_5 = unpack("B", f.read(1))[0] / 127
                                        g1_aa4_5 = unpack("B", f.read(1))[0] / 127
                                        b1_aa4_5 = unpack("B", f.read(1))[0] / 127
                                        a1_aa4_5 = unpack("B", f.read(1))[0] / 127
                                        r1_aa5_5 = unpack("B", f.read(1))[0] / 127
                                        g1_aa5_5 = unpack("B", f.read(1))[0] / 127
                                        b1_aa5_5 = unpack("B", f.read(1))[0] / 127
                                        a1_aa5_5 = unpack("B", f.read(1))[0] / 127
                                        r1_aa6_5 = unpack("B", f.read(1))[0] / 127
                                        g1_aa6_5 = unpack("B", f.read(1))[0] / 127
                                        b1_aa6_5 = unpack("B", f.read(1))[0] / 127
                                        a1_aa6_5 = unpack("B", f.read(1))[0] / 127
                                        r1_aa7_5 = unpack("B", f.read(1))[0] / 127
                                        g1_aa7_5 = unpack("B", f.read(1))[0] / 127
                                        b1_aa7_5 = unpack("B", f.read(1))[0] / 127
                                        a1_aa7_5 = unpack("B", f.read(1))[0] / 127
                                    for i in range(1):
                                        f.seek(-28,1)
                                    for i in range(1):
                                        r1_aa1_5_ = unpack("B", f.read(1))[0] / 127
                                        g1_aa1_5_ = unpack("B", f.read(1))[0] / 127
                                        b1_aa1_5_ = unpack("B", f.read(1))[0] / 127
                                        a1_aa1_5_ = unpack("B", f.read(1))[0] / 127
                                        r1_aa2_5_ = unpack("B", f.read(1))[0] / 127
                                        g1_aa2_5_ = unpack("B", f.read(1))[0] / 127
                                        b1_aa2_5_ = unpack("B", f.read(1))[0] / 127
                                        a1_aa2_5_ = unpack("B", f.read(1))[0] / 127
                                        r1_aa3_5_ = unpack("B", f.read(1))[0] / 127
                                        g1_aa3_5_ = unpack("B", f.read(1))[0] / 127
                                        b1_aa3_5_ = unpack("B", f.read(1))[0] / 127
                                        a1_aa3_5_ = unpack("B", f.read(1))[0] / 127
                                        r1_aa4_5_ = unpack("B", f.read(1))[0] / 127
                                        g1_aa4_5_ = unpack("B", f.read(1))[0] / 127
                                        b1_aa4_5_ = unpack("B", f.read(1))[0] / 127
                                        a1_aa4_5_ = unpack("B", f.read(1))[0] / 127
                                        r1_aa5_5_ = unpack("B", f.read(1))[0] / 127
                                        g1_aa5_5_ = unpack("B", f.read(1))[0] / 127
                                        b1_aa5_5_ = unpack("B", f.read(1))[0] / 127
                                        a1_aa5_5_ = unpack("B", f.read(1))[0] / 127
                                        r1_aa6_5_ = unpack("B", f.read(1))[0] / 127
                                        g1_aa6_5_ = unpack("B", f.read(1))[0] / 127
                                        b1_aa6_5_ = unpack("B", f.read(1))[0] / 127
                                        a1_aa6_5_ = unpack("B", f.read(1))[0] / 127
                                        r1_aa7_5_ = unpack("B", f.read(1))[0] / 127
                                        g1_aa7_5_ = unpack("B", f.read(1))[0] / 127
                                        b1_aa7_5_ = unpack("B", f.read(1))[0] / 127
                                        a1_aa7_5_ = unpack("B", f.read(1))[0] / 127
                                    for i in range(1):
                                        f.seek(-28,1)
                                    for i in range(1):
                                        r1_aa1_5__ = unpack("B", f.read(1))[0] / 127
                                        g1_aa1_5__ = unpack("B", f.read(1))[0] / 127
                                        b1_aa1_5__ = unpack("B", f.read(1))[0] / 127
                                        a1_aa1_5__ = unpack("B", f.read(1))[0] / 127
                                        r1_aa2_5__ = unpack("B", f.read(1))[0] / 127
                                        g1_aa2_5__ = unpack("B", f.read(1))[0] / 127
                                        b1_aa2_5__ = unpack("B", f.read(1))[0] / 127
                                        a1_aa2_5__ = unpack("B", f.read(1))[0] / 127
                                        r1_aa3_5__ = unpack("B", f.read(1))[0] / 127
                                        g1_aa3_5__ = unpack("B", f.read(1))[0] / 127
                                        b1_aa3_5__ = unpack("B", f.read(1))[0] / 127
                                        a1_aa3_5__ = unpack("B", f.read(1))[0] / 127
                                        r1_aa4_5__ = unpack("B", f.read(1))[0] / 127
                                        g1_aa4_5__ = unpack("B", f.read(1))[0] / 127
                                        b1_aa4_5__ = unpack("B", f.read(1))[0] / 127
                                        a1_aa4_5__ = unpack("B", f.read(1))[0] / 127
                                        r1_aa5_5__ = unpack("B", f.read(1))[0] / 127
                                        g1_aa5_5__ = unpack("B", f.read(1))[0] / 127
                                        b1_aa5_5__ = unpack("B", f.read(1))[0] / 127
                                        a1_aa5_5__ = unpack("B", f.read(1))[0] / 127
                                        r1_aa6_5__ = unpack("B", f.read(1))[0] / 127
                                        g1_aa6_5__ = unpack("B", f.read(1))[0] / 127
                                        b1_aa6_5__ = unpack("B", f.read(1))[0] / 127
                                        a1_aa6_5__ = unpack("B", f.read(1))[0] / 127
                                        r1_aa7_5__ = unpack("B", f.read(1))[0] / 127
                                        g1_aa7_5__ = unpack("B", f.read(1))[0] / 127
                                        b1_aa7_5__ = unpack("B", f.read(1))[0] / 127
                                        a1_aa7_5__ = unpack("B", f.read(1))[0] / 127
                                        
                                    offset1e____ = unpack("<I", f.read(4))[0]
                                    if offset1e____ == 16777473:
                                        offset3f____ = unpack("<I", f.read(4))[0]
                                        if offset3f____ == 335545088:
                                            if type20__ == 1:
                                                if type21__ == 1:
                                                    if type22__ == 0:
                                                        if type23__ == 0:
                                                            if type24__ == 1:
                                                                if type25__ == 1:
                                                                    if type26__ == 0:
                                                                        verticesEE1__.append([vx20__,vz20__,vy20__])
                                                                        verticesEE1__.append([vx21__,vz21__,vy21__])
                                                                        verticesEE1__.append([vx22__,vz22__,vy22__])
                                                                        verticesEE1__.append([vx23__,vz23__,vy23__])
                                                                        verticesEE1__.append([vx24__,vz24__,vy24__])
                                                                        verticesEE1__.append([vx25__,vz25__,vy25__])
                                                                        verticesEE1__.append([vx26__,vz26__,vy26__])
                                                                        fa_k_aa+=1*7#7
                                                                        fb_k_aa+=1*7#6
                                                                        fc_k_aa+=1*7#5
                                                                        fa_l_aa+=1*7#6
                                                                        fb_l_aa+=1*7#5
                                                                        fc_l_aa+=1*7#4
                                                                        fa_m_aa+=1*7#3
                                                                        fb_m_aa+=1*7#2
                                                                        fc_m_aa+=1*7#1
                                                                        facesEE1__.append([fa_k_aa,fb_k_aa,fc_k_aa])
                                                                        facesEE1__.append([fa_l_aa,fb_l_aa,fc_l_aa])
                                                                        facesEE1__.append([fa_m_aa,fb_m_aa,fc_m_aa])
                                                                        uvsEE1__.append([uvx_aa1_5__,-uvy_aa1_5__])
                                                                        uvsEE1__.append([uvx_aa2_5__,-uvy_aa2_5__])
                                                                        uvsEE1__.append([uvx_aa3_5__,-uvy_aa3_5__])
                                                                        uvsEE1__.append([uvx_aa4_5__,-uvy_aa4_5__])
                                                                        uvsEE1__.append([uvx_aa5_5__,-uvy_aa5_5__])
                                                                        uvsEE1__.append([uvx_aa6_5__,-uvy_aa6_5__])
                                                                        uvsEE1__.append([uvx_aa7_5__,-uvy_aa7_5__])
                                                                        vcolEE1__.append([r1_aa1_5__,g1_aa1_5__,b1_aa1_5__,a1_aa1_5__])
                                                                        vcolEE1__.append([r1_aa2_5__,g1_aa2_5__,b1_aa2_5__,a1_aa2_5__])
                                                                        vcolEE1__.append([r1_aa3_5__,g1_aa3_5__,b1_aa3_5__,a1_aa3_5__])
                                                                        vcolEE1__.append([r1_aa4_5__,g1_aa4_5__,b1_aa4_5__,a1_aa4_5__])
                                                                        vcolEE1__.append([r1_aa5_5__,g1_aa5_5__,b1_aa5_5__,a1_aa5_5__])
                                                                        vcolEE1__.append([r1_aa6_5__,g1_aa6_5__,b1_aa6_5__,a1_aa6_5__])
                                                                        vcolEE1__.append([r1_aa7_5__,g1_aa7_5__,b1_aa7_5__,a1_aa7_5__])
                                            if type20_ == 1:
                                                if type21_ == 1:
                                                    if type22_ == 0:
                                                        if type23_ == 1:
                                                            if type24_ == 1:
                                                                if type25_ == 0:
                                                                    if type26_ == 0:
                                                                        verticesEE1_.append([vx20_,vz20_,vy20_])
                                                                        verticesEE1_.append([vx21_,vz21_,vy21_])
                                                                        verticesEE1_.append([vx22_,vz22_,vy22_])
                                                                        verticesEE1_.append([vx23_,vz23_,vy23_])
                                                                        verticesEE1_.append([vx24_,vz24_,vy24_])
                                                                        verticesEE1_.append([vx25_,vz25_,vy25_])
                                                                        verticesEE1_.append([vx26_,vz26_,vy26_])
                                                                        fa_k_a+=1*7#7
                                                                        fb_k_a+=1*7#6
                                                                        fc_k_a+=1*7#5
                                                                        fa_l_a+=1*7#4
                                                                        fb_l_a+=1*7#3
                                                                        fc_l_a+=1*7#2
                                                                        fa_m_a+=1*7#3
                                                                        fb_m_a+=1*7#2
                                                                        fc_m_a+=1*7#1
                                                                        facesEE1_.append([fa_k_a,fb_k_a,fc_k_a])
                                                                        facesEE1_.append([fa_l_a,fb_l_a,fc_l_a])
                                                                        facesEE1_.append([fa_m_a,fb_m_a,fc_m_a])
                                                                        uvsEE1_.append([uvx_aa1_5_,-uvy_aa1_5_])
                                                                        uvsEE1_.append([uvx_aa2_5_,-uvy_aa2_5_])
                                                                        uvsEE1_.append([uvx_aa3_5_,-uvy_aa3_5_])
                                                                        uvsEE1_.append([uvx_aa4_5_,-uvy_aa4_5_])
                                                                        uvsEE1_.append([uvx_aa5_5_,-uvy_aa5_5_])
                                                                        uvsEE1_.append([uvx_aa6_5_,-uvy_aa6_5_])
                                                                        uvsEE1_.append([uvx_aa7_5_,-uvy_aa7_5_])
                                                                        vcolEE1_.append([r1_aa1_5_,g1_aa1_5_,b1_aa1_5_,a1_aa1_5_])
                                                                        vcolEE1_.append([r1_aa2_5_,g1_aa2_5_,b1_aa2_5_,a1_aa2_5_])
                                                                        vcolEE1_.append([r1_aa3_5_,g1_aa3_5_,b1_aa3_5_,a1_aa3_5_])
                                                                        vcolEE1_.append([r1_aa4_5_,g1_aa4_5_,b1_aa4_5_,a1_aa4_5_])
                                                                        vcolEE1_.append([r1_aa5_5_,g1_aa5_5_,b1_aa5_5_,a1_aa5_5_])
                                                                        vcolEE1_.append([r1_aa6_5_,g1_aa6_5_,b1_aa6_5_,a1_aa6_5_])
                                                                        vcolEE1_.append([r1_aa7_5_,g1_aa7_5_,b1_aa7_5_,a1_aa7_5_])
                                            if type20 == 1:
                                                if type21 == 1:
                                                    if type22 == 0:
                                                        if type23 == 0:
                                                            if type24 == 0:
                                                                if type25 == 0:
                                                                    if type26 == 0:
                                                                        verticesE.append([vx20,vz20,vy20])
                                                                        verticesE.append([vx21,vz21,vy21])
                                                                        verticesE.append([vx22,vz22,vy22])
                                                                        verticesE.append([vx23,vz23,vy23])
                                                                        verticesE.append([vx24,vz24,vy24])
                                                                        verticesE.append([vx25,vz25,vy25])
                                                                        verticesE.append([vx26,vz26,vy26])
                                                                        fa_k+=1*7
                                                                        fb_k+=1*7
                                                                        fc_k+=1*7
                                                                        fa_l+=1*7
                                                                        fb_l+=1*7
                                                                        fc_l+=1*7
                                                                        fa_m+=1*7
                                                                        fb_m+=1*7
                                                                        fc_m+=1*7
                                                                        fa_n+=1*7
                                                                        fb_n+=1*7
                                                                        fc_n+=1*7
                                                                        fa_o+=1*7
                                                                        fb_o+=1*7
                                                                        fc_o+=1*7
                                                                        facesE.append([fa_k,fb_k,fc_k])
                                                                        facesE.append([fa_l,fb_l,fc_l])
                                                                        facesE.append([fa_m,fb_m,fc_m])
                                                                        facesE.append([fa_n,fb_n,fc_n])
                                                                        facesE.append([fa_o,fb_o,fc_o])
                                                                        uvsE.append([uvx_aa1_5,-uvy_aa1_5])
                                                                        uvsE.append([uvx_aa2_5,-uvy_aa2_5])
                                                                        uvsE.append([uvx_aa3_5,-uvy_aa3_5])
                                                                        uvsE.append([uvx_aa4_5,-uvy_aa4_5])
                                                                        uvsE.append([uvx_aa5_5,-uvy_aa5_5])
                                                                        uvsE.append([uvx_aa6_5,-uvy_aa6_5])
                                                                        uvsE.append([uvx_aa7_5,-uvy_aa7_5])
                                                                        vcolE.append([r1_aa1_5,g1_aa1_5,b1_aa1_5,a1_aa1_5])
                                                                        vcolE.append([r1_aa2_5,g1_aa2_5,b1_aa2_5,a1_aa2_5])
                                                                        vcolE.append([r1_aa3_5,g1_aa3_5,b1_aa3_5,a1_aa3_5])
                                                                        vcolE.append([r1_aa4_5,g1_aa4_5,b1_aa4_5,a1_aa4_5])
                                                                        vcolE.append([r1_aa5_5,g1_aa5_5,b1_aa5_5,a1_aa5_5])
                                                                        vcolE.append([r1_aa6_5,g1_aa6_5,b1_aa6_5,a1_aa6_5])
                                                                        vcolE.append([r1_aa7_5,g1_aa7_5,b1_aa7_5,a1_aa7_5])

                elif vertexCount == 8:
                    for jjjj in range(1):
                        vx27 = unpack("<f", f.read(4))[0]
                        vy27 = unpack("<f", f.read(4))[0]
                        vz27 = unpack("<f", f.read(4))[0]
                        type27 = unpack("B", f.read(1))[0]
                        value1a27 = unpack("B", f.read(1))[0]
                        normalZ_27 = unpack("<h", f.read(2))[0]
                        vx28 = unpack("<f", f.read(4))[0]
                        vy28 = unpack("<f", f.read(4))[0]
                        vz28 = unpack("<f", f.read(4))[0]
                        type28 = unpack("B", f.read(1))[0]
                        value1a28 = unpack("B", f.read(1))[0]
                        normalZ_28 = unpack("<h", f.read(2))[0]
                        vx29 = unpack("<f", f.read(4))[0]
                        vy29 = unpack("<f", f.read(4))[0]
                        vz29 = unpack("<f", f.read(4))[0]
                        type29 = unpack("B", f.read(1))[0]
                        value1a29 = unpack("B", f.read(1))[0]
                        normalZ_29 = unpack("<h", f.read(2))[0]
                        vx30 = unpack("<f", f.read(4))[0]
                        vy30 = unpack("<f", f.read(4))[0]
                        vz30 = unpack("<f", f.read(4))[0]
                        type30 = unpack("B", f.read(1))[0]
                        value1a30 = unpack("B", f.read(1))[0]
                        normalZ_30 = unpack("<h", f.read(2))[0]
                        vx31 = unpack("<f", f.read(4))[0]
                        vy31 = unpack("<f", f.read(4))[0]
                        vz31 = unpack("<f", f.read(4))[0]
                        type31 = unpack("B", f.read(1))[0]
                        value1a31 = unpack("B", f.read(1))[0]
                        normalZ_31 = unpack("<h", f.read(2))[0]
                        vx32 = unpack("<f", f.read(4))[0]
                        vy32 = unpack("<f", f.read(4))[0]
                        vz32 = unpack("<f", f.read(4))[0]
                        type32 = unpack("B", f.read(1))[0]
                        value1a32 = unpack("B", f.read(1))[0]
                        normalZ_32 = unpack("<h", f.read(2))[0]
                        vx33 = unpack("<f", f.read(4))[0]
                        vy33 = unpack("<f", f.read(4))[0]
                        vz33 = unpack("<f", f.read(4))[0]
                        type33 = unpack("B", f.read(1))[0]
                        value1a33 = unpack("B", f.read(1))[0]
                        normalZ_33 = unpack("<h", f.read(2))[0]
                        vx34 = unpack("<f", f.read(4))[0]
                        vy34 = unpack("<f", f.read(4))[0]
                        vz34 = unpack("<f", f.read(4))[0]
                        type34 = unpack("B", f.read(1))[0]
                        value1a34 = unpack("B", f.read(1))[0]
                        normalZ_34 = unpack("<h", f.read(2))[0]
                    for jjjj in range(vertexCount):
                        f.seek(-16,1)
                    for jjjj in range(1):
                        vx27a = unpack("<f", f.read(4))[0]
                        vy27a = unpack("<f", f.read(4))[0]
                        vz27a = unpack("<f", f.read(4))[0]
                        type27a = unpack("B", f.read(1))[0]
                        value1a27a = unpack("B", f.read(1))[0]
                        normalZ_27a = unpack("<h", f.read(2))[0]
                        vx28a = unpack("<f", f.read(4))[0]
                        vy28a = unpack("<f", f.read(4))[0]
                        vz28a = unpack("<f", f.read(4))[0]
                        type28a = unpack("B", f.read(1))[0]
                        value1a28a = unpack("B", f.read(1))[0]
                        normalZ_28a = unpack("<h", f.read(2))[0]
                        vx29a = unpack("<f", f.read(4))[0]
                        vy29a = unpack("<f", f.read(4))[0]
                        vz29a = unpack("<f", f.read(4))[0]
                        type29a = unpack("B", f.read(1))[0]
                        value1a29a = unpack("B", f.read(1))[0]
                        normalZ_29a = unpack("<h", f.read(2))[0]
                        vx30a = unpack("<f", f.read(4))[0]
                        vy30a = unpack("<f", f.read(4))[0]
                        vz30a = unpack("<f", f.read(4))[0]
                        type30a = unpack("B", f.read(1))[0]
                        value1a30a = unpack("B", f.read(1))[0]
                        normalZ_30a = unpack("<h", f.read(2))[0]
                        vx31a = unpack("<f", f.read(4))[0]
                        vy31a = unpack("<f", f.read(4))[0]
                        vz31a = unpack("<f", f.read(4))[0]
                        type31a = unpack("B", f.read(1))[0]
                        value1a31a = unpack("B", f.read(1))[0]
                        normalZ_31a = unpack("<h", f.read(2))[0]
                        vx32a = unpack("<f", f.read(4))[0]
                        vy32a = unpack("<f", f.read(4))[0]
                        vz32a = unpack("<f", f.read(4))[0]
                        type32a = unpack("B", f.read(1))[0]
                        value1a32a = unpack("B", f.read(1))[0]
                        normalZ_32a = unpack("<h", f.read(2))[0]
                        vx33a = unpack("<f", f.read(4))[0]
                        vy33a = unpack("<f", f.read(4))[0]
                        vz33a = unpack("<f", f.read(4))[0]
                        type33a = unpack("B", f.read(1))[0]
                        value1a33a = unpack("B", f.read(1))[0]
                        normalZ_33a = unpack("<h", f.read(2))[0]
                        vx34a = unpack("<f", f.read(4))[0]
                        vy34a = unpack("<f", f.read(4))[0]
                        vz34a = unpack("<f", f.read(4))[0]
                        type34a = unpack("B", f.read(1))[0]
                        value1a34a = unpack("B", f.read(1))[0]
                        normalZ_34a = unpack("<h", f.read(2))[0]
                    for jjjj in range(vertexCount):
                        f.seek(-16,1)
                    for jjjj in range(1):
                        vx27b = unpack("<f", f.read(4))[0]
                        vy27b = unpack("<f", f.read(4))[0]
                        vz27b = unpack("<f", f.read(4))[0]
                        type27b = unpack("B", f.read(1))[0]
                        value1a27b = unpack("B", f.read(1))[0]
                        normalZ_27b = unpack("<h", f.read(2))[0]
                        vx28b = unpack("<f", f.read(4))[0]
                        vy28b = unpack("<f", f.read(4))[0]
                        vz28b = unpack("<f", f.read(4))[0]
                        type28b = unpack("B", f.read(1))[0]
                        value1a28b = unpack("B", f.read(1))[0]
                        normalZ_28b = unpack("<h", f.read(2))[0]
                        vx29b = unpack("<f", f.read(4))[0]
                        vy29b = unpack("<f", f.read(4))[0]
                        vz29b = unpack("<f", f.read(4))[0]
                        type29b = unpack("B", f.read(1))[0]
                        value1a29b = unpack("B", f.read(1))[0]
                        normalZ_29b = unpack("<h", f.read(2))[0]
                        vx30b = unpack("<f", f.read(4))[0]
                        vy30b = unpack("<f", f.read(4))[0]
                        vz30b = unpack("<f", f.read(4))[0]
                        type30b = unpack("B", f.read(1))[0]
                        value1a30b = unpack("B", f.read(1))[0]
                        normalZ_30b = unpack("<h", f.read(2))[0]
                        vx31b = unpack("<f", f.read(4))[0]
                        vy31b = unpack("<f", f.read(4))[0]
                        vz31b = unpack("<f", f.read(4))[0]
                        type31b = unpack("B", f.read(1))[0]
                        value1a31b = unpack("B", f.read(1))[0]
                        normalZ_31b = unpack("<h", f.read(2))[0]
                        vx32b = unpack("<f", f.read(4))[0]
                        vy32b = unpack("<f", f.read(4))[0]
                        vz32b = unpack("<f", f.read(4))[0]
                        type32b = unpack("B", f.read(1))[0]
                        value1a32b = unpack("B", f.read(1))[0]
                        normalZ_32b = unpack("<h", f.read(2))[0]
                        vx33b = unpack("<f", f.read(4))[0]
                        vy33b = unpack("<f", f.read(4))[0]
                        vz33b = unpack("<f", f.read(4))[0]
                        type33b = unpack("B", f.read(1))[0]
                        value1a33b = unpack("B", f.read(1))[0]
                        normalZ_33b = unpack("<h", f.read(2))[0]
                        vx34b = unpack("<f", f.read(4))[0]
                        vy34b = unpack("<f", f.read(4))[0]
                        vz34b = unpack("<f", f.read(4))[0]
                        type34b = unpack("B", f.read(1))[0]
                        value1a34b = unpack("B", f.read(1))[0]
                        normalZ_34b = unpack("<h", f.read(2))[0]
                    for jjjj in range(vertexCount):
                        f.seek(-16,1)
                    for jjjj in range(1):
                        vx27c = unpack("<f", f.read(4))[0]
                        vy27c = unpack("<f", f.read(4))[0]
                        vz27c = unpack("<f", f.read(4))[0]
                        type27c = unpack("B", f.read(1))[0]
                        value1a27c = unpack("B", f.read(1))[0]
                        normalZ_27c = unpack("<h", f.read(2))[0]
                        vx28c = unpack("<f", f.read(4))[0]
                        vy28c = unpack("<f", f.read(4))[0]
                        vz28c = unpack("<f", f.read(4))[0]
                        type28c = unpack("B", f.read(1))[0]
                        value1a28c = unpack("B", f.read(1))[0]
                        normalZ_28c = unpack("<h", f.read(2))[0]
                        vx29c = unpack("<f", f.read(4))[0]
                        vy29c = unpack("<f", f.read(4))[0]
                        vz29c = unpack("<f", f.read(4))[0]
                        type29c = unpack("B", f.read(1))[0]
                        value1a29c = unpack("B", f.read(1))[0]
                        normalZ_29c = unpack("<h", f.read(2))[0]
                        vx30c = unpack("<f", f.read(4))[0]
                        vy30c = unpack("<f", f.read(4))[0]
                        vz30c = unpack("<f", f.read(4))[0]
                        type30c = unpack("B", f.read(1))[0]
                        value1a30c = unpack("B", f.read(1))[0]
                        normalZ_30c = unpack("<h", f.read(2))[0]
                        vx31c = unpack("<f", f.read(4))[0]
                        vy31c = unpack("<f", f.read(4))[0]
                        vz31c = unpack("<f", f.read(4))[0]
                        type31c = unpack("B", f.read(1))[0]
                        value1a31c = unpack("B", f.read(1))[0]
                        normalZ_31c = unpack("<h", f.read(2))[0]
                        vx32c = unpack("<f", f.read(4))[0]
                        vy32c = unpack("<f", f.read(4))[0]
                        vz32c = unpack("<f", f.read(4))[0]
                        type32c = unpack("B", f.read(1))[0]
                        value1a32c = unpack("B", f.read(1))[0]
                        normalZ_32c = unpack("<h", f.read(2))[0]
                        vx33c = unpack("<f", f.read(4))[0]
                        vy33c = unpack("<f", f.read(4))[0]
                        vz33c = unpack("<f", f.read(4))[0]
                        type33c = unpack("B", f.read(1))[0]
                        value1a33c = unpack("B", f.read(1))[0]
                        normalZ_33c = unpack("<h", f.read(2))[0]
                        vx34c = unpack("<f", f.read(4))[0]
                        vy34c = unpack("<f", f.read(4))[0]
                        vz34c = unpack("<f", f.read(4))[0]
                        type34c = unpack("B", f.read(1))[0]
                        value1a34c = unpack("B", f.read(1))[0]
                        normalZ_34c = unpack("<h", f.read(2))[0]
                        
                    offset1_ae____ = unpack("<I", f.read(4))[0]
                    if offset1_ae____ == 83886081:
                        offset1_be____ = unpack("<I", f.read(4))[0]
                        if offset1_be____ == 1829273604:
                            for i in range(1):
                                uvx_aa1_6 = unpack("<h", f.read(2))[0] / 4096
                                uvy_aa1_6 = unpack("<h", f.read(2))[0] / 4096
                                f.seek(4,1)
                                uvx_aa2_6 = unpack("<h", f.read(2))[0] / 4096
                                uvy_aa2_6 = unpack("<h", f.read(2))[0] / 4096
                                f.seek(4,1)
                                uvx_aa3_6 = unpack("<h", f.read(2))[0] / 4096
                                uvy_aa3_6 = unpack("<h", f.read(2))[0] / 4096
                                f.seek(4,1)
                                uvx_aa4_6 = unpack("<h", f.read(2))[0] / 4096
                                uvy_aa4_6 = unpack("<h", f.read(2))[0] / 4096
                                f.seek(4,1)
                                uvx_aa5_6 = unpack("<h", f.read(2))[0] / 4096
                                uvy_aa5_6 = unpack("<h", f.read(2))[0] / 4096
                                f.seek(4,1)
                                uvx_aa6_6 = unpack("<h", f.read(2))[0] / 4096
                                uvy_aa6_6 = unpack("<h", f.read(2))[0] / 4096
                                f.seek(4,1)
                                uvx_aa7_6 = unpack("<h", f.read(2))[0] / 4096
                                uvy_aa7_6 = unpack("<h", f.read(2))[0] / 4096
                                f.seek(4,1)
                                uvx_aa8_6 = unpack("<h", f.read(2))[0] / 4096
                                uvy_aa8_6 = unpack("<h", f.read(2))[0] / 4096
                                f.seek(4,1)
                            for i in range(1):
                                f.seek(-64,1)
                            for i in range(1):
                                uvx_aa1_6a = unpack("<h", f.read(2))[0] / 4096
                                uvy_aa1_6a = unpack("<h", f.read(2))[0] / 4096
                                f.seek(4,1)
                                uvx_aa2_6a = unpack("<h", f.read(2))[0] / 4096
                                uvy_aa2_6a = unpack("<h", f.read(2))[0] / 4096
                                f.seek(4,1)
                                uvx_aa3_6a = unpack("<h", f.read(2))[0] / 4096
                                uvy_aa3_6a = unpack("<h", f.read(2))[0] / 4096
                                f.seek(4,1)
                                uvx_aa4_6a = unpack("<h", f.read(2))[0] / 4096
                                uvy_aa4_6a = unpack("<h", f.read(2))[0] / 4096
                                f.seek(4,1)
                                uvx_aa5_6a = unpack("<h", f.read(2))[0] / 4096
                                uvy_aa5_6a = unpack("<h", f.read(2))[0] / 4096
                                f.seek(4,1)
                                uvx_aa6_6a = unpack("<h", f.read(2))[0] / 4096
                                uvy_aa6_6a = unpack("<h", f.read(2))[0] / 4096
                                f.seek(4,1)
                                uvx_aa7_6a = unpack("<h", f.read(2))[0] / 4096
                                uvy_aa7_6a = unpack("<h", f.read(2))[0] / 4096
                                f.seek(4,1)
                                uvx_aa8_6a = unpack("<h", f.read(2))[0] / 4096
                                uvy_aa8_6a = unpack("<h", f.read(2))[0] / 4096
                                f.seek(4,1)
                            for i in range(1):
                                f.seek(-64,1)
                            for i in range(1):
                                uvx_aa1_6b = unpack("<h", f.read(2))[0] / 4096
                                uvy_aa1_6b = unpack("<h", f.read(2))[0] / 4096
                                f.seek(4,1)
                                uvx_aa2_6b = unpack("<h", f.read(2))[0] / 4096
                                uvy_aa2_6b = unpack("<h", f.read(2))[0] / 4096
                                f.seek(4,1)
                                uvx_aa3_6b = unpack("<h", f.read(2))[0] / 4096
                                uvy_aa3_6b = unpack("<h", f.read(2))[0] / 4096
                                f.seek(4,1)
                                uvx_aa4_6b = unpack("<h", f.read(2))[0] / 4096
                                uvy_aa4_6b = unpack("<h", f.read(2))[0] / 4096
                                f.seek(4,1)
                                uvx_aa5_6b = unpack("<h", f.read(2))[0] / 4096
                                uvy_aa5_6b = unpack("<h", f.read(2))[0] / 4096
                                f.seek(4,1)
                                uvx_aa6_6b = unpack("<h", f.read(2))[0] / 4096
                                uvy_aa6_6b = unpack("<h", f.read(2))[0] / 4096
                                f.seek(4,1)
                                uvx_aa7_6b = unpack("<h", f.read(2))[0] / 4096
                                uvy_aa7_6b = unpack("<h", f.read(2))[0] / 4096
                                f.seek(4,1)
                                uvx_aa8_6b = unpack("<h", f.read(2))[0] / 4096
                                uvy_aa8_6b = unpack("<h", f.read(2))[0] / 4096
                                f.seek(4,1)
                            for i in range(1):
                                f.seek(-64,1)
                            for i in range(1):
                                uvx_aa1_6c = unpack("<h", f.read(2))[0] / 4096
                                uvy_aa1_6c = unpack("<h", f.read(2))[0] / 4096
                                f.seek(4,1)
                                uvx_aa2_6c = unpack("<h", f.read(2))[0] / 4096
                                uvy_aa2_6c = unpack("<h", f.read(2))[0] / 4096
                                f.seek(4,1)
                                uvx_aa3_6c = unpack("<h", f.read(2))[0] / 4096
                                uvy_aa3_6c = unpack("<h", f.read(2))[0] / 4096
                                f.seek(4,1)
                                uvx_aa4_6c = unpack("<h", f.read(2))[0] / 4096
                                uvy_aa4_6c = unpack("<h", f.read(2))[0] / 4096
                                f.seek(4,1)
                                uvx_aa5_6c = unpack("<h", f.read(2))[0] / 4096
                                uvy_aa5_6c = unpack("<h", f.read(2))[0] / 4096
                                f.seek(4,1)
                                uvx_aa6_6c = unpack("<h", f.read(2))[0] / 4096
                                uvy_aa6_6c = unpack("<h", f.read(2))[0] / 4096
                                f.seek(4,1)
                                uvx_aa7_6c = unpack("<h", f.read(2))[0] / 4096
                                uvy_aa7_6c = unpack("<h", f.read(2))[0] / 4096
                                f.seek(4,1)
                                uvx_aa8_6c = unpack("<h", f.read(2))[0] / 4096
                                uvy_aa8_6c = unpack("<h", f.read(2))[0] / 4096
                                f.seek(4,1)
                                
                            offset1ca____ = unpack("<I", f.read(4))[0]
                            if offset1ca____ == 83886080:
                                offset1da____ = unpack("<I", f.read(4))[0]
                                if offset1da____ == 1846067205:
                                    for i in range(1):
                                        r1_aa1_6 = unpack("B", f.read(1))[0] / 127
                                        g1_aa1_6 = unpack("B", f.read(1))[0] / 127
                                        b1_aa1_6 = unpack("B", f.read(1))[0] / 127
                                        a1_aa1_6 = unpack("B", f.read(1))[0] / 127
                                        r1_aa2_6 = unpack("B", f.read(1))[0] / 127
                                        g1_aa2_6 = unpack("B", f.read(1))[0] / 127
                                        b1_aa2_6 = unpack("B", f.read(1))[0] / 127
                                        a1_aa2_6 = unpack("B", f.read(1))[0] / 127
                                        r1_aa3_6 = unpack("B", f.read(1))[0] / 127
                                        g1_aa3_6 = unpack("B", f.read(1))[0] / 127
                                        b1_aa3_6 = unpack("B", f.read(1))[0] / 127
                                        a1_aa3_6 = unpack("B", f.read(1))[0] / 127
                                        r1_aa4_6 = unpack("B", f.read(1))[0] / 127
                                        g1_aa4_6 = unpack("B", f.read(1))[0] / 127
                                        b1_aa4_6 = unpack("B", f.read(1))[0] / 127
                                        a1_aa4_6 = unpack("B", f.read(1))[0] / 127
                                        r1_aa5_6 = unpack("B", f.read(1))[0] / 127
                                        g1_aa5_6 = unpack("B", f.read(1))[0] / 127
                                        b1_aa5_6 = unpack("B", f.read(1))[0] / 127
                                        a1_aa5_6 = unpack("B", f.read(1))[0] / 127
                                        r1_aa6_6 = unpack("B", f.read(1))[0] / 127
                                        g1_aa6_6 = unpack("B", f.read(1))[0] / 127
                                        b1_aa6_6 = unpack("B", f.read(1))[0] / 127
                                        a1_aa6_6 = unpack("B", f.read(1))[0] / 127
                                        r1_aa7_6 = unpack("B", f.read(1))[0] / 127
                                        g1_aa7_6 = unpack("B", f.read(1))[0] / 127
                                        b1_aa7_6 = unpack("B", f.read(1))[0] / 127
                                        a1_aa7_6 = unpack("B", f.read(1))[0] / 127
                                        r1_aa8_6 = unpack("B", f.read(1))[0] / 127
                                        g1_aa8_6 = unpack("B", f.read(1))[0] / 127
                                        b1_aa8_6 = unpack("B", f.read(1))[0] / 127
                                        a1_aa8_6 = unpack("B", f.read(1))[0] / 127
                                    for i in range(1):
                                        f.seek(-32,1)
                                    for i in range(1):
                                        r1_aa1_6a = unpack("B", f.read(1))[0] / 127
                                        g1_aa1_6a = unpack("B", f.read(1))[0] / 127
                                        b1_aa1_6a = unpack("B", f.read(1))[0] / 127
                                        a1_aa1_6a = unpack("B", f.read(1))[0] / 127
                                        r1_aa2_6a = unpack("B", f.read(1))[0] / 127
                                        g1_aa2_6a = unpack("B", f.read(1))[0] / 127
                                        b1_aa2_6a = unpack("B", f.read(1))[0] / 127
                                        a1_aa2_6a = unpack("B", f.read(1))[0] / 127
                                        r1_aa3_6a = unpack("B", f.read(1))[0] / 127
                                        g1_aa3_6a = unpack("B", f.read(1))[0] / 127
                                        b1_aa3_6a = unpack("B", f.read(1))[0] / 127
                                        a1_aa3_6a = unpack("B", f.read(1))[0] / 127
                                        r1_aa4_6a = unpack("B", f.read(1))[0] / 127
                                        g1_aa4_6a = unpack("B", f.read(1))[0] / 127
                                        b1_aa4_6a = unpack("B", f.read(1))[0] / 127
                                        a1_aa4_6a = unpack("B", f.read(1))[0] / 127
                                        r1_aa5_6a = unpack("B", f.read(1))[0] / 127
                                        g1_aa5_6a = unpack("B", f.read(1))[0] / 127
                                        b1_aa5_6a = unpack("B", f.read(1))[0] / 127
                                        a1_aa5_6a = unpack("B", f.read(1))[0] / 127
                                        r1_aa6_6a = unpack("B", f.read(1))[0] / 127
                                        g1_aa6_6a = unpack("B", f.read(1))[0] / 127
                                        b1_aa6_6a = unpack("B", f.read(1))[0] / 127
                                        a1_aa6_6a = unpack("B", f.read(1))[0] / 127
                                        r1_aa7_6a = unpack("B", f.read(1))[0] / 127
                                        g1_aa7_6a = unpack("B", f.read(1))[0] / 127
                                        b1_aa7_6a = unpack("B", f.read(1))[0] / 127
                                        a1_aa7_6a = unpack("B", f.read(1))[0] / 127
                                        r1_aa8_6a = unpack("B", f.read(1))[0] / 127
                                        g1_aa8_6a = unpack("B", f.read(1))[0] / 127
                                        b1_aa8_6a = unpack("B", f.read(1))[0] / 127
                                        a1_aa8_6a = unpack("B", f.read(1))[0] / 127
                                    for i in range(1):
                                        f.seek(-32,1)
                                    for i in range(1):
                                        r1_aa1_6b = unpack("B", f.read(1))[0] / 127
                                        g1_aa1_6b = unpack("B", f.read(1))[0] / 127
                                        b1_aa1_6b = unpack("B", f.read(1))[0] / 127
                                        a1_aa1_6b = unpack("B", f.read(1))[0] / 127
                                        r1_aa2_6b = unpack("B", f.read(1))[0] / 127
                                        g1_aa2_6b = unpack("B", f.read(1))[0] / 127
                                        b1_aa2_6b = unpack("B", f.read(1))[0] / 127
                                        a1_aa2_6b = unpack("B", f.read(1))[0] / 127
                                        r1_aa3_6b = unpack("B", f.read(1))[0] / 127
                                        g1_aa3_6b = unpack("B", f.read(1))[0] / 127
                                        b1_aa3_6b = unpack("B", f.read(1))[0] / 127
                                        a1_aa3_6b = unpack("B", f.read(1))[0] / 127
                                        r1_aa4_6b = unpack("B", f.read(1))[0] / 127
                                        g1_aa4_6b = unpack("B", f.read(1))[0] / 127
                                        b1_aa4_6b = unpack("B", f.read(1))[0] / 127
                                        a1_aa4_6b = unpack("B", f.read(1))[0] / 127
                                        r1_aa5_6b = unpack("B", f.read(1))[0] / 127
                                        g1_aa5_6b = unpack("B", f.read(1))[0] / 127
                                        b1_aa5_6b = unpack("B", f.read(1))[0] / 127
                                        a1_aa5_6b = unpack("B", f.read(1))[0] / 127
                                        r1_aa6_6b = unpack("B", f.read(1))[0] / 127
                                        g1_aa6_6b = unpack("B", f.read(1))[0] / 127
                                        b1_aa6_6b = unpack("B", f.read(1))[0] / 127
                                        a1_aa6_6b = unpack("B", f.read(1))[0] / 127
                                        r1_aa7_6b = unpack("B", f.read(1))[0] / 127
                                        g1_aa7_6b = unpack("B", f.read(1))[0] / 127
                                        b1_aa7_6b = unpack("B", f.read(1))[0] / 127
                                        a1_aa7_6b = unpack("B", f.read(1))[0] / 127
                                        r1_aa8_6b = unpack("B", f.read(1))[0] / 127
                                        g1_aa8_6b = unpack("B", f.read(1))[0] / 127
                                        b1_aa8_6b = unpack("B", f.read(1))[0] / 127
                                        a1_aa8_6b = unpack("B", f.read(1))[0] / 127
                                    for i in range(1):
                                        f.seek(-32,1)
                                    for i in range(1):
                                        r1_aa1_6c = unpack("B", f.read(1))[0] / 127
                                        g1_aa1_6c = unpack("B", f.read(1))[0] / 127
                                        b1_aa1_6c = unpack("B", f.read(1))[0] / 127
                                        a1_aa1_6c = unpack("B", f.read(1))[0] / 127
                                        r1_aa2_6c = unpack("B", f.read(1))[0] / 127
                                        g1_aa2_6c = unpack("B", f.read(1))[0] / 127
                                        b1_aa2_6c = unpack("B", f.read(1))[0] / 127
                                        a1_aa2_6c = unpack("B", f.read(1))[0] / 127
                                        r1_aa3_6c = unpack("B", f.read(1))[0] / 127
                                        g1_aa3_6c = unpack("B", f.read(1))[0] / 127
                                        b1_aa3_6c = unpack("B", f.read(1))[0] / 127
                                        a1_aa3_6c = unpack("B", f.read(1))[0] / 127
                                        r1_aa4_6c = unpack("B", f.read(1))[0] / 127
                                        g1_aa4_6c = unpack("B", f.read(1))[0] / 127
                                        b1_aa4_6c = unpack("B", f.read(1))[0] / 127
                                        a1_aa4_6c = unpack("B", f.read(1))[0] / 127
                                        r1_aa5_6c = unpack("B", f.read(1))[0] / 127
                                        g1_aa5_6c = unpack("B", f.read(1))[0] / 127
                                        b1_aa5_6c = unpack("B", f.read(1))[0] / 127
                                        a1_aa5_6c = unpack("B", f.read(1))[0] / 127
                                        r1_aa6_6c = unpack("B", f.read(1))[0] / 127
                                        g1_aa6_6c = unpack("B", f.read(1))[0] / 127
                                        b1_aa6_6c = unpack("B", f.read(1))[0] / 127
                                        a1_aa6_6c = unpack("B", f.read(1))[0] / 127
                                        r1_aa7_6c = unpack("B", f.read(1))[0] / 127
                                        g1_aa7_6c = unpack("B", f.read(1))[0] / 127
                                        b1_aa7_6c = unpack("B", f.read(1))[0] / 127
                                        a1_aa7_6c = unpack("B", f.read(1))[0] / 127
                                        r1_aa8_6c = unpack("B", f.read(1))[0] / 127
                                        g1_aa8_6c = unpack("B", f.read(1))[0] / 127
                                        b1_aa8_6c = unpack("B", f.read(1))[0] / 127
                                        a1_aa8_6c = unpack("B", f.read(1))[0] / 127
                                        
                                    offset1ea____ = unpack("<I", f.read(4))[0]
                                    if offset1ea____ == 16777473:
                                        offset3fa____ = unpack("<I", f.read(4))[0]
                                        if offset3fa____ == 335545088:
                                            if type27c == 1:
                                                if type28c == 1:
                                                    if type29c == 0:
                                                        if type30c == 0:
                                                            if type31c == 0:
                                                                if type32c == 1:
                                                                    if type33c == 1:
                                                                        if type34c == 0:
                                                                            verticesE2aaaa.append([vx27c,vz27c,vy27c])
                                                                            verticesE2aaaa.append([vx28c,vz28c,vy28c])
                                                                            verticesE2aaaa.append([vx29c,vz29c,vy29c])
                                                                            verticesE2aaaa.append([vx30c,vz30c,vy30c])
                                                                            verticesE2aaaa.append([vx31c,vz31c,vy31c])
                                                                            verticesE2aaaa.append([vx32c,vz32c,vy32c])
                                                                            verticesE2aaaa.append([vx33c,vz33c,vy33c])
                                                                            verticesE2aaaa.append([vx34c,vz34c,vy34c])
                                                                            fa_paaa+=1*8#8
                                                                            fb_paaa+=1*8#7
                                                                            fc_paaa+=1*8#6
                                                                            fa_qaaa+=1*8#7
                                                                            fb_qaaa+=1*8#6
                                                                            fc_qaaa+=1*8#5
                                                                            fa_raaa+=1*8#6
                                                                            fb_raaa+=1*8#5
                                                                            fc_raaa+=1*8#4
                                                                            fa_saaa+=1*8#3
                                                                            fb_saaa+=1*8#2
                                                                            fc_saaa+=1*8#1
                                                                            
                                                                            facesE2aaaa.append([fa_paaa,fb_paaa,fc_paaa])
                                                                            facesE2aaaa.append([fa_qaaa,fb_qaaa,fc_qaaa])
                                                                            facesE2aaaa.append([fa_raaa,fb_raaa,fc_raaa])
                                                                            facesE2aaaa.append([fa_saaa,fb_saaa,fc_saaa])
                                                                            uvsE2aaaa.append([uvx_aa1_6c,-uvy_aa1_6c])
                                                                            uvsE2aaaa.append([uvx_aa2_6c,-uvy_aa2_6c])
                                                                            uvsE2aaaa.append([uvx_aa3_6c,-uvy_aa3_6c])
                                                                            uvsE2aaaa.append([uvx_aa4_6c,-uvy_aa4_6c])
                                                                            uvsE2aaaa.append([uvx_aa5_6c,-uvy_aa5_6c])
                                                                            uvsE2aaaa.append([uvx_aa6_6c,-uvy_aa6_6c])
                                                                            uvsE2aaaa.append([uvx_aa7_6c,-uvy_aa7_6c])
                                                                            uvsE2aaaa.append([uvx_aa8_6c,-uvy_aa8_6c])
                                                                            vcolE2aaaa.append([r1_aa1_6c,g1_aa1_6c,b1_aa1_6c,a1_aa1_6c])
                                                                            vcolE2aaaa.append([r1_aa2_6c,g1_aa2_6c,b1_aa2_6c,a1_aa2_6c])
                                                                            vcolE2aaaa.append([r1_aa3_6c,g1_aa3_6c,b1_aa3_6c,a1_aa3_6c])
                                                                            vcolE2aaaa.append([r1_aa4_6c,g1_aa4_6c,b1_aa4_6c,a1_aa4_6c])
                                                                            vcolE2aaaa.append([r1_aa5_6c,g1_aa5_6c,b1_aa5_6c,a1_aa5_6c])
                                                                            vcolE2aaaa.append([r1_aa6_6c,g1_aa6_6c,b1_aa6_6c,a1_aa6_6c])
                                                                            vcolE2aaaa.append([r1_aa7_6c,g1_aa7_6c,b1_aa7_6c,a1_aa7_6c])
                                                                            vcolE2aaaa.append([r1_aa8_6c,g1_aa8_6c,b1_aa8_6c,a1_aa8_6c])
                                            if type27b == 1:
                                                if type28b == 1:
                                                    if type29b == 0:
                                                        if type30b == 0:
                                                            if type31b == 1:
                                                                if type32b == 1:
                                                                    if type33b == 0:
                                                                        if type34b == 0:
                                                                            verticesE2aaa.append([vx27b,vz27b,vy27b])
                                                                            verticesE2aaa.append([vx28b,vz28b,vy28b])
                                                                            verticesE2aaa.append([vx29b,vz29b,vy29b])
                                                                            verticesE2aaa.append([vx30b,vz30b,vy30b])
                                                                            verticesE2aaa.append([vx31b,vz31b,vy31b])
                                                                            verticesE2aaa.append([vx32b,vz32b,vy32b])
                                                                            verticesE2aaa.append([vx33b,vz33b,vy33b])
                                                                            verticesE2aaa.append([vx34b,vz34b,vy34b])
                                                                            fa_paa+=1*8#8
                                                                            fb_paa+=1*8#7
                                                                            fc_paa+=1*8#6
                                                                            fa_qaa+=1*8#7
                                                                            fb_qaa+=1*8#6
                                                                            fc_qaa+=1*8#5
                                                                            fa_raa+=1*8#4
                                                                            fb_raa+=1*8#3
                                                                            fc_raa+=1*8#2
                                                                            fa_saa+=1*8#3
                                                                            fb_saa+=1*8#2
                                                                            fc_saa+=1*8#1
                                                                            
                                                                            facesE2aaa.append([fa_paa,fb_paa,fc_paa])
                                                                            facesE2aaa.append([fa_qaa,fb_qaa,fc_qaa])
                                                                            facesE2aaa.append([fa_raa,fb_raa,fc_raa])
                                                                            facesE2aaa.append([fa_saa,fb_saa,fc_saa])
                                                                            uvsE2aaa.append([uvx_aa1_6b,-uvy_aa1_6b])
                                                                            uvsE2aaa.append([uvx_aa2_6b,-uvy_aa2_6b])
                                                                            uvsE2aaa.append([uvx_aa3_6b,-uvy_aa3_6b])
                                                                            uvsE2aaa.append([uvx_aa4_6b,-uvy_aa4_6b])
                                                                            uvsE2aaa.append([uvx_aa5_6b,-uvy_aa5_6b])
                                                                            uvsE2aaa.append([uvx_aa6_6b,-uvy_aa6_6b])
                                                                            uvsE2aaa.append([uvx_aa7_6b,-uvy_aa7_6b])
                                                                            uvsE2aaa.append([uvx_aa8_6b,-uvy_aa8_6b])
                                                                            vcolE2aaa.append([r1_aa1_6b,g1_aa1_6b,b1_aa1_6b,a1_aa1_6b])
                                                                            vcolE2aaa.append([r1_aa2_6b,g1_aa2_6b,b1_aa2_6b,a1_aa2_6b])
                                                                            vcolE2aaa.append([r1_aa3_6b,g1_aa3_6b,b1_aa3_6b,a1_aa3_6b])
                                                                            vcolE2aaa.append([r1_aa4_6b,g1_aa4_6b,b1_aa4_6b,a1_aa4_6b])
                                                                            vcolE2aaa.append([r1_aa5_6b,g1_aa5_6b,b1_aa5_6b,a1_aa5_6b])
                                                                            vcolE2aaa.append([r1_aa6_6b,g1_aa6_6b,b1_aa6_6b,a1_aa6_6b])
                                                                            vcolE2aaa.append([r1_aa7_6b,g1_aa7_6b,b1_aa7_6b,a1_aa7_6b])
                                                                            vcolE2aaa.append([r1_aa8_6b,g1_aa8_6b,b1_aa8_6b,a1_aa8_6b])
                                            if type27a == 1:
                                                if type28a == 1:
                                                    if type29a == 0:
                                                        if type30a == 1:
                                                            if type31a == 1:
                                                                if type32a == 0:
                                                                    if type33a == 0:
                                                                        if type34a == 0:
                                                                            verticesE2aa.append([vx27a,vz27a,vy27a])
                                                                            verticesE2aa.append([vx28a,vz28a,vy28a])
                                                                            verticesE2aa.append([vx29a,vz29a,vy29a])
                                                                            verticesE2aa.append([vx30a,vz30a,vy30a])
                                                                            verticesE2aa.append([vx31a,vz31a,vy31a])
                                                                            verticesE2aa.append([vx32a,vz32a,vy32a])
                                                                            verticesE2aa.append([vx33a,vz33a,vy33a])
                                                                            verticesE2aa.append([vx34a,vz34a,vy34a])
                                                                            fa_pa+=1*8#8
                                                                            fb_pa+=1*8#7
                                                                            fc_pa+=1*8#6
                                                                            fa_qa+=1*8#5
                                                                            fb_qa+=1*8#4
                                                                            fc_qa+=1*8#3
                                                                            fa_ra+=1*8#4
                                                                            fb_ra+=1*8#3
                                                                            fc_ra+=1*8#2
                                                                            fa_sa+=1*8#3
                                                                            fb_sa+=1*8#2
                                                                            fc_sa+=1*8#1
                                                                            
                                                                            facesE2aa.append([fa_pa,fb_pa,fc_pa])
                                                                            facesE2aa.append([fa_qa,fb_qa,fc_qa])
                                                                            facesE2aa.append([fa_ra,fb_ra,fc_ra])
                                                                            facesE2aa.append([fa_sa,fb_sa,fc_sa])
                                                                            uvsE2aa.append([uvx_aa1_6a,-uvy_aa1_6a])
                                                                            uvsE2aa.append([uvx_aa2_6a,-uvy_aa2_6a])
                                                                            uvsE2aa.append([uvx_aa3_6a,-uvy_aa3_6a])
                                                                            uvsE2aa.append([uvx_aa4_6a,-uvy_aa4_6a])
                                                                            uvsE2aa.append([uvx_aa5_6a,-uvy_aa5_6a])
                                                                            uvsE2aa.append([uvx_aa6_6a,-uvy_aa6_6a])
                                                                            uvsE2aa.append([uvx_aa7_6a,-uvy_aa7_6a])
                                                                            uvsE2aa.append([uvx_aa8_6a,-uvy_aa8_6a])
                                                                            vcolE2aa.append([r1_aa1_6a,g1_aa1_6a,b1_aa1_6a,a1_aa1_6a])
                                                                            vcolE2aa.append([r1_aa2_6a,g1_aa2_6a,b1_aa2_6a,a1_aa2_6a])
                                                                            vcolE2aa.append([r1_aa3_6a,g1_aa3_6a,b1_aa3_6a,a1_aa3_6a])
                                                                            vcolE2aa.append([r1_aa4_6a,g1_aa4_6a,b1_aa4_6a,a1_aa4_6a])
                                                                            vcolE2aa.append([r1_aa5_6a,g1_aa5_6a,b1_aa5_6a,a1_aa5_6a])
                                                                            vcolE2aa.append([r1_aa6_6a,g1_aa6_6a,b1_aa6_6a,a1_aa6_6a])
                                                                            vcolE2aa.append([r1_aa7_6a,g1_aa7_6a,b1_aa7_6a,a1_aa7_6a])
                                                                            vcolE2aa.append([r1_aa8_6a,g1_aa8_6a,b1_aa8_6a,a1_aa8_6a])
                                            if type27 == 1:
                                                if type28 == 1:
                                                    if type29 == 0:
                                                        if type30 == 0:
                                                            if type31 == 0:
                                                                if type32 == 0:
                                                                    if type33 == 0:
                                                                        if type34 == 0:
                                                                            verticesE2a.append([vx27,vz27,vy27])
                                                                            verticesE2a.append([vx28,vz28,vy28])
                                                                            verticesE2a.append([vx29,vz29,vy29])
                                                                            verticesE2a.append([vx30,vz30,vy30])
                                                                            verticesE2a.append([vx31,vz31,vy31])
                                                                            verticesE2a.append([vx32,vz32,vy32])
                                                                            verticesE2a.append([vx33,vz33,vy33])
                                                                            verticesE2a.append([vx34,vz34,vy34])
                                                                            fa_p+=1*8
                                                                            fb_p+=1*8
                                                                            fc_p+=1*8
                                                                            fa_q+=1*8
                                                                            fb_q+=1*8
                                                                            fc_q+=1*8
                                                                            fa_r+=1*8
                                                                            fb_r+=1*8
                                                                            fc_r+=1*8
                                                                            fa_s+=1*8
                                                                            fb_s+=1*8
                                                                            fc_s+=1*8
                                                                            fa_t+=1*8
                                                                            fb_t+=1*8
                                                                            fc_t+=1*8
                                                                            fa_u+=1*8
                                                                            fb_u+=1*8
                                                                            fc_u+=1*8
                                                                            facesE2a.append([fa_p,fb_p,fc_p])
                                                                            facesE2a.append([fa_q,fb_q,fc_q])
                                                                            facesE2a.append([fa_r,fb_r,fc_r])
                                                                            facesE2a.append([fa_s,fb_s,fc_s])
                                                                            facesE2a.append([fa_t,fb_t,fc_t])
                                                                            facesE2a.append([fa_u,fb_u,fc_u])
                                                                            uvsE2a.append([uvx_aa1_6,-uvy_aa1_6])
                                                                            uvsE2a.append([uvx_aa2_6,-uvy_aa2_6])
                                                                            uvsE2a.append([uvx_aa3_6,-uvy_aa3_6])
                                                                            uvsE2a.append([uvx_aa4_6,-uvy_aa4_6])
                                                                            uvsE2a.append([uvx_aa5_6,-uvy_aa5_6])
                                                                            uvsE2a.append([uvx_aa6_6,-uvy_aa6_6])
                                                                            uvsE2a.append([uvx_aa7_6,-uvy_aa7_6])
                                                                            uvsE2a.append([uvx_aa8_6,-uvy_aa8_6])
                                                                            vcolE2a.append([r1_aa1_6,g1_aa1_6,b1_aa1_6,a1_aa1_6])
                                                                            vcolE2a.append([r1_aa2_6,g1_aa2_6,b1_aa2_6,a1_aa2_6])
                                                                            vcolE2a.append([r1_aa3_6,g1_aa3_6,b1_aa3_6,a1_aa3_6])
                                                                            vcolE2a.append([r1_aa4_6,g1_aa4_6,b1_aa4_6,a1_aa4_6])
                                                                            vcolE2a.append([r1_aa5_6,g1_aa5_6,b1_aa5_6,a1_aa5_6])
                                                                            vcolE2a.append([r1_aa6_6,g1_aa6_6,b1_aa6_6,a1_aa6_6])
                                                                            vcolE2a.append([r1_aa7_6,g1_aa7_6,b1_aa7_6,a1_aa7_6])
                                                                            vcolE2a.append([r1_aa8_6,g1_aa8_6,b1_aa8_6,a1_aa8_6])

                elif vertexCount == 9:
                    for jjjj in range(1):
                        vx35 = unpack("<f", f.read(4))[0]
                        vy35 = unpack("<f", f.read(4))[0]
                        vz35 = unpack("<f", f.read(4))[0]
                        type35 = unpack("B", f.read(1))[0]
                        value1a35 = unpack("B", f.read(1))[0]
                        normalZ_35 = unpack("<h", f.read(2))[0]
                        vx36 = unpack("<f", f.read(4))[0]
                        vy36 = unpack("<f", f.read(4))[0]
                        vz36 = unpack("<f", f.read(4))[0]
                        type36 = unpack("B", f.read(1))[0]
                        value1a36 = unpack("B", f.read(1))[0]
                        normalZ_36 = unpack("<h", f.read(2))[0]
                        vx37 = unpack("<f", f.read(4))[0]
                        vy37 = unpack("<f", f.read(4))[0]
                        vz37 = unpack("<f", f.read(4))[0]
                        type37 = unpack("B", f.read(1))[0]
                        value1a37 = unpack("B", f.read(1))[0]
                        normalZ_37 = unpack("<h", f.read(2))[0]
                        vx38 = unpack("<f", f.read(4))[0]
                        vy38 = unpack("<f", f.read(4))[0]
                        vz38 = unpack("<f", f.read(4))[0]
                        type38 = unpack("B", f.read(1))[0]
                        value1a38 = unpack("B", f.read(1))[0]
                        normalZ_38 = unpack("<h", f.read(2))[0]
                        vx39 = unpack("<f", f.read(4))[0]
                        vy39 = unpack("<f", f.read(4))[0]
                        vz39 = unpack("<f", f.read(4))[0]
                        type39 = unpack("B", f.read(1))[0]
                        value1a39 = unpack("B", f.read(1))[0]
                        normalZ_39 = unpack("<h", f.read(2))[0]
                        vx40 = unpack("<f", f.read(4))[0]
                        vy40 = unpack("<f", f.read(4))[0]
                        vz40 = unpack("<f", f.read(4))[0]
                        type40 = unpack("B", f.read(1))[0]
                        value1a40 = unpack("B", f.read(1))[0]
                        normalZ_40 = unpack("<h", f.read(2))[0]
                        vx41 = unpack("<f", f.read(4))[0]
                        vy41 = unpack("<f", f.read(4))[0]
                        vz41 = unpack("<f", f.read(4))[0]
                        type41 = unpack("B", f.read(1))[0]
                        value1a41 = unpack("B", f.read(1))[0]
                        normalZ_41 = unpack("<h", f.read(2))[0]
                        vx42 = unpack("<f", f.read(4))[0]
                        vy42 = unpack("<f", f.read(4))[0]
                        vz42 = unpack("<f", f.read(4))[0]
                        type42 = unpack("B", f.read(1))[0]
                        value1a42 = unpack("B", f.read(1))[0]
                        normalZ_42 = unpack("<h", f.read(2))[0]
                        vx43 = unpack("<f", f.read(4))[0]
                        vy43 = unpack("<f", f.read(4))[0]
                        vz43 = unpack("<f", f.read(4))[0]
                        type43 = unpack("B", f.read(1))[0]
                        value1a43 = unpack("B", f.read(1))[0]
                        normalZ_43 = unpack("<h", f.read(2))[0]
                    for jjjj in range(vertexCount):
                        f.seek(-16,1)
                    for jjjj in range(1):
                        vx35a = unpack("<f", f.read(4))[0]
                        vy35a = unpack("<f", f.read(4))[0]
                        vz35a = unpack("<f", f.read(4))[0]
                        type35a = unpack("B", f.read(1))[0]
                        value1a35a = unpack("B", f.read(1))[0]
                        normalZ_35a = unpack("<h", f.read(2))[0]
                        vx36a = unpack("<f", f.read(4))[0]
                        vy36a = unpack("<f", f.read(4))[0]
                        vz36a = unpack("<f", f.read(4))[0]
                        type36a = unpack("B", f.read(1))[0]
                        value1a36a = unpack("B", f.read(1))[0]
                        normalZ_36a = unpack("<h", f.read(2))[0]
                        vx37a = unpack("<f", f.read(4))[0]
                        vy37a = unpack("<f", f.read(4))[0]
                        vz37a = unpack("<f", f.read(4))[0]
                        type37a = unpack("B", f.read(1))[0]
                        value1a37a = unpack("B", f.read(1))[0]
                        normalZ_37a = unpack("<h", f.read(2))[0]
                        vx38a = unpack("<f", f.read(4))[0]
                        vy38a = unpack("<f", f.read(4))[0]
                        vz38a = unpack("<f", f.read(4))[0]
                        type38a = unpack("B", f.read(1))[0]
                        value1a38a = unpack("B", f.read(1))[0]
                        normalZ_38a = unpack("<h", f.read(2))[0]
                        vx39a = unpack("<f", f.read(4))[0]
                        vy39a = unpack("<f", f.read(4))[0]
                        vz39a = unpack("<f", f.read(4))[0]
                        type39a = unpack("B", f.read(1))[0]
                        value1a39a = unpack("B", f.read(1))[0]
                        normalZ_39a = unpack("<h", f.read(2))[0]
                        vx40a = unpack("<f", f.read(4))[0]
                        vy40a = unpack("<f", f.read(4))[0]
                        vz40a = unpack("<f", f.read(4))[0]
                        type40a = unpack("B", f.read(1))[0]
                        value1a40a = unpack("B", f.read(1))[0]
                        normalZ_40a = unpack("<h", f.read(2))[0]
                        vx41a = unpack("<f", f.read(4))[0]
                        vy41a = unpack("<f", f.read(4))[0]
                        vz41a = unpack("<f", f.read(4))[0]
                        type41a = unpack("B", f.read(1))[0]
                        value1a41a = unpack("B", f.read(1))[0]
                        normalZ_41a = unpack("<h", f.read(2))[0]
                        vx42a = unpack("<f", f.read(4))[0]
                        vy42a = unpack("<f", f.read(4))[0]
                        vz42a = unpack("<f", f.read(4))[0]
                        type42a = unpack("B", f.read(1))[0]
                        value1a42a = unpack("B", f.read(1))[0]
                        normalZ_42a = unpack("<h", f.read(2))[0]
                        vx43a = unpack("<f", f.read(4))[0]
                        vy43a = unpack("<f", f.read(4))[0]
                        vz43a = unpack("<f", f.read(4))[0]
                        type43a = unpack("B", f.read(1))[0]
                        value1a43a = unpack("B", f.read(1))[0]
                        normalZ_43a = unpack("<h", f.read(2))[0]
                    for jjjj in range(vertexCount):
                        f.seek(-16,1)
                    for jjjj in range(1):
                        vx35b = unpack("<f", f.read(4))[0]
                        vy35b = unpack("<f", f.read(4))[0]
                        vz35b = unpack("<f", f.read(4))[0]
                        type35b = unpack("B", f.read(1))[0]
                        value1a35b = unpack("B", f.read(1))[0]
                        normalZ_35b = unpack("<h", f.read(2))[0]
                        vx36b = unpack("<f", f.read(4))[0]
                        vy36b = unpack("<f", f.read(4))[0]
                        vz36b = unpack("<f", f.read(4))[0]
                        type36b = unpack("B", f.read(1))[0]
                        value1a36b = unpack("B", f.read(1))[0]
                        normalZ_36b = unpack("<h", f.read(2))[0]
                        vx37b = unpack("<f", f.read(4))[0]
                        vy37b = unpack("<f", f.read(4))[0]
                        vz37b = unpack("<f", f.read(4))[0]
                        type37b = unpack("B", f.read(1))[0]
                        value1a37b = unpack("B", f.read(1))[0]
                        normalZ_37b = unpack("<h", f.read(2))[0]
                        vx38b = unpack("<f", f.read(4))[0]
                        vy38b = unpack("<f", f.read(4))[0]
                        vz38b = unpack("<f", f.read(4))[0]
                        type38b = unpack("B", f.read(1))[0]
                        value1a38b = unpack("B", f.read(1))[0]
                        normalZ_38b = unpack("<h", f.read(2))[0]
                        vx39b = unpack("<f", f.read(4))[0]
                        vy39b = unpack("<f", f.read(4))[0]
                        vz39b = unpack("<f", f.read(4))[0]
                        type39b = unpack("B", f.read(1))[0]
                        value1a39b = unpack("B", f.read(1))[0]
                        normalZ_39b = unpack("<h", f.read(2))[0]
                        vx40b = unpack("<f", f.read(4))[0]
                        vy40b = unpack("<f", f.read(4))[0]
                        vz40b = unpack("<f", f.read(4))[0]
                        type40b = unpack("B", f.read(1))[0]
                        value1a40b = unpack("B", f.read(1))[0]
                        normalZ_40b = unpack("<h", f.read(2))[0]
                        vx41b = unpack("<f", f.read(4))[0]
                        vy41b = unpack("<f", f.read(4))[0]
                        vz41b = unpack("<f", f.read(4))[0]
                        type41b = unpack("B", f.read(1))[0]
                        value1a41b = unpack("B", f.read(1))[0]
                        normalZ_41b = unpack("<h", f.read(2))[0]
                        vx42b = unpack("<f", f.read(4))[0]
                        vy42b = unpack("<f", f.read(4))[0]
                        vz42b = unpack("<f", f.read(4))[0]
                        type42b = unpack("B", f.read(1))[0]
                        value1a42b = unpack("B", f.read(1))[0]
                        normalZ_42b = unpack("<h", f.read(2))[0]
                        vx43b = unpack("<f", f.read(4))[0]
                        vy43b = unpack("<f", f.read(4))[0]
                        vz43b = unpack("<f", f.read(4))[0]
                        type43b = unpack("B", f.read(1))[0]
                        value1a43b = unpack("B", f.read(1))[0]
                        normalZ_43b = unpack("<h", f.read(2))[0]
                    for jjjj in range(vertexCount):
                        f.seek(-16,1)
                    for jjjj in range(1):
                        vx35c = unpack("<f", f.read(4))[0]
                        vy35c = unpack("<f", f.read(4))[0]
                        vz35c = unpack("<f", f.read(4))[0]
                        type35c = unpack("B", f.read(1))[0]
                        value1a35c = unpack("B", f.read(1))[0]
                        normalZ_35c = unpack("<h", f.read(2))[0]
                        vx36c = unpack("<f", f.read(4))[0]
                        vy36c = unpack("<f", f.read(4))[0]
                        vz36c = unpack("<f", f.read(4))[0]
                        type36c = unpack("B", f.read(1))[0]
                        value1a36c = unpack("B", f.read(1))[0]
                        normalZ_36c = unpack("<h", f.read(2))[0]
                        vx37c = unpack("<f", f.read(4))[0]
                        vy37c = unpack("<f", f.read(4))[0]
                        vz37c = unpack("<f", f.read(4))[0]
                        type37c = unpack("B", f.read(1))[0]
                        value1a37c = unpack("B", f.read(1))[0]
                        normalZ_37c = unpack("<h", f.read(2))[0]
                        vx38c = unpack("<f", f.read(4))[0]
                        vy38c = unpack("<f", f.read(4))[0]
                        vz38c = unpack("<f", f.read(4))[0]
                        type38c = unpack("B", f.read(1))[0]
                        value1a38c = unpack("B", f.read(1))[0]
                        normalZ_38c = unpack("<h", f.read(2))[0]
                        vx39c = unpack("<f", f.read(4))[0]
                        vy39c = unpack("<f", f.read(4))[0]
                        vz39c = unpack("<f", f.read(4))[0]
                        type39c = unpack("B", f.read(1))[0]
                        value1a39c = unpack("B", f.read(1))[0]
                        normalZ_39c = unpack("<h", f.read(2))[0]
                        vx40c = unpack("<f", f.read(4))[0]
                        vy40c = unpack("<f", f.read(4))[0]
                        vz40c = unpack("<f", f.read(4))[0]
                        type40c = unpack("B", f.read(1))[0]
                        value1a40c = unpack("B", f.read(1))[0]
                        normalZ_40c = unpack("<h", f.read(2))[0]
                        vx41c = unpack("<f", f.read(4))[0]
                        vy41c = unpack("<f", f.read(4))[0]
                        vz41c = unpack("<f", f.read(4))[0]
                        type41c = unpack("B", f.read(1))[0]
                        value1a41c = unpack("B", f.read(1))[0]
                        normalZ_41c = unpack("<h", f.read(2))[0]
                        vx42c = unpack("<f", f.read(4))[0]
                        vy42c = unpack("<f", f.read(4))[0]
                        vz42c = unpack("<f", f.read(4))[0]
                        type42c = unpack("B", f.read(1))[0]
                        value1a42c = unpack("B", f.read(1))[0]
                        normalZ_42c = unpack("<h", f.read(2))[0]
                        vx43c = unpack("<f", f.read(4))[0]
                        vy43c = unpack("<f", f.read(4))[0]
                        vz43c = unpack("<f", f.read(4))[0]
                        type43c = unpack("B", f.read(1))[0]
                        value1a43c = unpack("B", f.read(1))[0]
                        normalZ_43c = unpack("<h", f.read(2))[0]
                    for jjjj in range(vertexCount):
                        f.seek(-16,1)
                    for jjjj in range(1):
                        vx35d = unpack("<f", f.read(4))[0]
                        vy35d = unpack("<f", f.read(4))[0]
                        vz35d = unpack("<f", f.read(4))[0]
                        type35d = unpack("B", f.read(1))[0]
                        value1a35d = unpack("B", f.read(1))[0]
                        normalZ_35d = unpack("<h", f.read(2))[0]
                        vx36d = unpack("<f", f.read(4))[0]
                        vy36d = unpack("<f", f.read(4))[0]
                        vz36d = unpack("<f", f.read(4))[0]
                        type36d = unpack("B", f.read(1))[0]
                        value1a36d = unpack("B", f.read(1))[0]
                        normalZ_36d = unpack("<h", f.read(2))[0]
                        vx37d = unpack("<f", f.read(4))[0]
                        vy37d = unpack("<f", f.read(4))[0]
                        vz37d = unpack("<f", f.read(4))[0]
                        type37d = unpack("B", f.read(1))[0]
                        value1a37d = unpack("B", f.read(1))[0]
                        normalZ_37d = unpack("<h", f.read(2))[0]
                        vx38d = unpack("<f", f.read(4))[0]
                        vy38d = unpack("<f", f.read(4))[0]
                        vz38d = unpack("<f", f.read(4))[0]
                        type38d = unpack("B", f.read(1))[0]
                        value1a38d = unpack("B", f.read(1))[0]
                        normalZ_38d = unpack("<h", f.read(2))[0]
                        vx39d = unpack("<f", f.read(4))[0]
                        vy39d = unpack("<f", f.read(4))[0]
                        vz39d = unpack("<f", f.read(4))[0]
                        type39d = unpack("B", f.read(1))[0]
                        value1a39d = unpack("B", f.read(1))[0]
                        normalZ_39d = unpack("<h", f.read(2))[0]
                        vx40d = unpack("<f", f.read(4))[0]
                        vy40d = unpack("<f", f.read(4))[0]
                        vz40d = unpack("<f", f.read(4))[0]
                        type40d = unpack("B", f.read(1))[0]
                        value1a40d = unpack("B", f.read(1))[0]
                        normalZ_40d = unpack("<h", f.read(2))[0]
                        vx41d = unpack("<f", f.read(4))[0]
                        vy41d = unpack("<f", f.read(4))[0]
                        vz41d = unpack("<f", f.read(4))[0]
                        type41d = unpack("B", f.read(1))[0]
                        value1a41d = unpack("B", f.read(1))[0]
                        normalZ_41d = unpack("<h", f.read(2))[0]
                        vx42d = unpack("<f", f.read(4))[0]
                        vy42d = unpack("<f", f.read(4))[0]
                        vz42d = unpack("<f", f.read(4))[0]
                        type42d = unpack("B", f.read(1))[0]
                        value1a42d = unpack("B", f.read(1))[0]
                        normalZ_42d = unpack("<h", f.read(2))[0]
                        vx43d = unpack("<f", f.read(4))[0]
                        vy43d = unpack("<f", f.read(4))[0]
                        vz43d = unpack("<f", f.read(4))[0]
                        type43d = unpack("B", f.read(1))[0]
                        value1a43d = unpack("B", f.read(1))[0]
                        normalZ_43d = unpack("<h", f.read(2))[0]
                    for jjjj in range(vertexCount):
                        f.seek(-16,1)
                    for jjjj in range(1):
                        vx35e = unpack("<f", f.read(4))[0]
                        vy35e = unpack("<f", f.read(4))[0]
                        vz35e = unpack("<f", f.read(4))[0]
                        type35e = unpack("B", f.read(1))[0]
                        value1a35e = unpack("B", f.read(1))[0]
                        normalZ_35e = unpack("<h", f.read(2))[0]
                        vx36e = unpack("<f", f.read(4))[0]
                        vy36e = unpack("<f", f.read(4))[0]
                        vz36e = unpack("<f", f.read(4))[0]
                        type36e = unpack("B", f.read(1))[0]
                        value1a36e = unpack("B", f.read(1))[0]
                        normalZ_36e = unpack("<h", f.read(2))[0]
                        vx37e = unpack("<f", f.read(4))[0]
                        vy37e = unpack("<f", f.read(4))[0]
                        vz37e = unpack("<f", f.read(4))[0]
                        type37e = unpack("B", f.read(1))[0]
                        value1a37e = unpack("B", f.read(1))[0]
                        normalZ_37e = unpack("<h", f.read(2))[0]
                        vx38e = unpack("<f", f.read(4))[0]
                        vy38e = unpack("<f", f.read(4))[0]
                        vz38e = unpack("<f", f.read(4))[0]
                        type38e = unpack("B", f.read(1))[0]
                        value1a38e = unpack("B", f.read(1))[0]
                        normalZ_38e = unpack("<h", f.read(2))[0]
                        vx39e = unpack("<f", f.read(4))[0]
                        vy39e = unpack("<f", f.read(4))[0]
                        vz39e = unpack("<f", f.read(4))[0]
                        type39e = unpack("B", f.read(1))[0]
                        value1a39e = unpack("B", f.read(1))[0]
                        normalZ_39e = unpack("<h", f.read(2))[0]
                        vx40e = unpack("<f", f.read(4))[0]
                        vy40e = unpack("<f", f.read(4))[0]
                        vz40e = unpack("<f", f.read(4))[0]
                        type40e = unpack("B", f.read(1))[0]
                        value1a40e = unpack("B", f.read(1))[0]
                        normalZ_40e = unpack("<h", f.read(2))[0]
                        vx41e = unpack("<f", f.read(4))[0]
                        vy41e = unpack("<f", f.read(4))[0]
                        vz41e = unpack("<f", f.read(4))[0]
                        type41e = unpack("B", f.read(1))[0]
                        value1a41e = unpack("B", f.read(1))[0]
                        normalZ_41e = unpack("<h", f.read(2))[0]
                        vx42e = unpack("<f", f.read(4))[0]
                        vy42e = unpack("<f", f.read(4))[0]
                        vz42e = unpack("<f", f.read(4))[0]
                        type42e = unpack("B", f.read(1))[0]
                        value1a42e = unpack("B", f.read(1))[0]
                        normalZ_42e = unpack("<h", f.read(2))[0]
                        vx43e = unpack("<f", f.read(4))[0]
                        vy43e = unpack("<f", f.read(4))[0]
                        vz43e = unpack("<f", f.read(4))[0]
                        type43e = unpack("B", f.read(1))[0]
                        value1a43e = unpack("B", f.read(1))[0]
                        normalZ_43e = unpack("<h", f.read(2))[0]
                        
                    offset1ea_____ = unpack("<I", f.read(4))[0]
                    if offset1ea_____ == 83886081:
                        offset3fa_____ = unpack("<I", f.read(4))[0]
                        if offset3fa_____ == 1829339140:
                            for i in range(1):
                                uvx_aa1_7 = unpack("<h", f.read(2))[0] / 4096
                                uvy_aa1_7 = unpack("<h", f.read(2))[0] / 4096
                                f.seek(4,1)
                                uvx_aa2_7 = unpack("<h", f.read(2))[0] / 4096
                                uvy_aa2_7 = unpack("<h", f.read(2))[0] / 4096
                                f.seek(4,1)
                                uvx_aa3_7 = unpack("<h", f.read(2))[0] / 4096
                                uvy_aa3_7 = unpack("<h", f.read(2))[0] / 4096
                                f.seek(4,1)
                                uvx_aa4_7 = unpack("<h", f.read(2))[0] / 4096
                                uvy_aa4_7 = unpack("<h", f.read(2))[0] / 4096
                                f.seek(4,1)
                                uvx_aa5_7 = unpack("<h", f.read(2))[0] / 4096
                                uvy_aa5_7 = unpack("<h", f.read(2))[0] / 4096
                                f.seek(4,1)
                                uvx_aa6_7 = unpack("<h", f.read(2))[0] / 4096
                                uvy_aa6_7 = unpack("<h", f.read(2))[0] / 4096
                                f.seek(4,1)
                                uvx_aa7_7 = unpack("<h", f.read(2))[0] / 4096
                                uvy_aa7_7 = unpack("<h", f.read(2))[0] / 4096
                                f.seek(4,1)
                                uvx_aa8_7 = unpack("<h", f.read(2))[0] / 4096
                                uvy_aa8_7 = unpack("<h", f.read(2))[0] / 4096
                                f.seek(4,1)
                                uvx_aa9_7 = unpack("<h", f.read(2))[0] / 4096
                                uvy_aa9_7 = unpack("<h", f.read(2))[0] / 4096
                                f.seek(4,1)
                            for i in range(9):
                                f.seek(-8,1)
                            for i in range(1):
                                uvx_aa1_7a = unpack("<h", f.read(2))[0] / 4096
                                uvy_aa1_7a = unpack("<h", f.read(2))[0] / 4096
                                f.seek(4,1)
                                uvx_aa2_7a = unpack("<h", f.read(2))[0] / 4096
                                uvy_aa2_7a = unpack("<h", f.read(2))[0] / 4096
                                f.seek(4,1)
                                uvx_aa3_7a = unpack("<h", f.read(2))[0] / 4096
                                uvy_aa3_7a = unpack("<h", f.read(2))[0] / 4096
                                f.seek(4,1)
                                uvx_aa4_7a = unpack("<h", f.read(2))[0] / 4096
                                uvy_aa4_7a = unpack("<h", f.read(2))[0] / 4096
                                f.seek(4,1)
                                uvx_aa5_7a = unpack("<h", f.read(2))[0] / 4096
                                uvy_aa5_7a = unpack("<h", f.read(2))[0] / 4096
                                f.seek(4,1)
                                uvx_aa6_7a = unpack("<h", f.read(2))[0] / 4096
                                uvy_aa6_7a = unpack("<h", f.read(2))[0] / 4096
                                f.seek(4,1)
                                uvx_aa7_7a = unpack("<h", f.read(2))[0] / 4096
                                uvy_aa7_7a = unpack("<h", f.read(2))[0] / 4096
                                f.seek(4,1)
                                uvx_aa8_7a = unpack("<h", f.read(2))[0] / 4096
                                uvy_aa8_7a = unpack("<h", f.read(2))[0] / 4096
                                f.seek(4,1)
                                uvx_aa9_7a = unpack("<h", f.read(2))[0] / 4096
                                uvy_aa9_7a = unpack("<h", f.read(2))[0] / 4096
                                f.seek(4,1)
                            for i in range(9):
                                f.seek(-8,1)
                            for i in range(1):
                                uvx_aa1_7b = unpack("<h", f.read(2))[0] / 4096
                                uvy_aa1_7b = unpack("<h", f.read(2))[0] / 4096
                                f.seek(4,1)
                                uvx_aa2_7b = unpack("<h", f.read(2))[0] / 4096
                                uvy_aa2_7b = unpack("<h", f.read(2))[0] / 4096
                                f.seek(4,1)
                                uvx_aa3_7b = unpack("<h", f.read(2))[0] / 4096
                                uvy_aa3_7b = unpack("<h", f.read(2))[0] / 4096
                                f.seek(4,1)
                                uvx_aa4_7b = unpack("<h", f.read(2))[0] / 4096
                                uvy_aa4_7b = unpack("<h", f.read(2))[0] / 4096
                                f.seek(4,1)
                                uvx_aa5_7b = unpack("<h", f.read(2))[0] / 4096
                                uvy_aa5_7b = unpack("<h", f.read(2))[0] / 4096
                                f.seek(4,1)
                                uvx_aa6_7b = unpack("<h", f.read(2))[0] / 4096
                                uvy_aa6_7b = unpack("<h", f.read(2))[0] / 4096
                                f.seek(4,1)
                                uvx_aa7_7b = unpack("<h", f.read(2))[0] / 4096
                                uvy_aa7_7b = unpack("<h", f.read(2))[0] / 4096
                                f.seek(4,1)
                                uvx_aa8_7b = unpack("<h", f.read(2))[0] / 4096
                                uvy_aa8_7b = unpack("<h", f.read(2))[0] / 4096
                                f.seek(4,1)
                                uvx_aa9_7b = unpack("<h", f.read(2))[0] / 4096
                                uvy_aa9_7b = unpack("<h", f.read(2))[0] / 4096
                                f.seek(4,1)
                            for i in range(9):
                                f.seek(-8,1)
                            for i in range(1):
                                uvx_aa1_7c = unpack("<h", f.read(2))[0] / 4096
                                uvy_aa1_7c = unpack("<h", f.read(2))[0] / 4096
                                f.seek(4,1)
                                uvx_aa2_7c = unpack("<h", f.read(2))[0] / 4096
                                uvy_aa2_7c = unpack("<h", f.read(2))[0] / 4096
                                f.seek(4,1)
                                uvx_aa3_7c = unpack("<h", f.read(2))[0] / 4096
                                uvy_aa3_7c = unpack("<h", f.read(2))[0] / 4096
                                f.seek(4,1)
                                uvx_aa4_7c = unpack("<h", f.read(2))[0] / 4096
                                uvy_aa4_7c = unpack("<h", f.read(2))[0] / 4096
                                f.seek(4,1)
                                uvx_aa5_7c = unpack("<h", f.read(2))[0] / 4096
                                uvy_aa5_7c = unpack("<h", f.read(2))[0] / 4096
                                f.seek(4,1)
                                uvx_aa6_7c = unpack("<h", f.read(2))[0] / 4096
                                uvy_aa6_7c = unpack("<h", f.read(2))[0] / 4096
                                f.seek(4,1)
                                uvx_aa7_7c = unpack("<h", f.read(2))[0] / 4096
                                uvy_aa7_7c = unpack("<h", f.read(2))[0] / 4096
                                f.seek(4,1)
                                uvx_aa8_7c = unpack("<h", f.read(2))[0] / 4096
                                uvy_aa8_7c = unpack("<h", f.read(2))[0] / 4096
                                f.seek(4,1)
                                uvx_aa9_7c = unpack("<h", f.read(2))[0] / 4096
                                uvy_aa9_7c = unpack("<h", f.read(2))[0] / 4096
                                f.seek(4,1)
                            for i in range(9):
                                f.seek(-8,1)
                            for i in range(1):
                                uvx_aa1_7d = unpack("<h", f.read(2))[0] / 4096
                                uvy_aa1_7d = unpack("<h", f.read(2))[0] / 4096
                                f.seek(4,1)
                                uvx_aa2_7d = unpack("<h", f.read(2))[0] / 4096
                                uvy_aa2_7d = unpack("<h", f.read(2))[0] / 4096
                                f.seek(4,1)
                                uvx_aa3_7d = unpack("<h", f.read(2))[0] / 4096
                                uvy_aa3_7d = unpack("<h", f.read(2))[0] / 4096
                                f.seek(4,1)
                                uvx_aa4_7d = unpack("<h", f.read(2))[0] / 4096
                                uvy_aa4_7d = unpack("<h", f.read(2))[0] / 4096
                                f.seek(4,1)
                                uvx_aa5_7d = unpack("<h", f.read(2))[0] / 4096
                                uvy_aa5_7d = unpack("<h", f.read(2))[0] / 4096
                                f.seek(4,1)
                                uvx_aa6_7d = unpack("<h", f.read(2))[0] / 4096
                                uvy_aa6_7d = unpack("<h", f.read(2))[0] / 4096
                                f.seek(4,1)
                                uvx_aa7_7d = unpack("<h", f.read(2))[0] / 4096
                                uvy_aa7_7d = unpack("<h", f.read(2))[0] / 4096
                                f.seek(4,1)
                                uvx_aa8_7d = unpack("<h", f.read(2))[0] / 4096
                                uvy_aa8_7d = unpack("<h", f.read(2))[0] / 4096
                                f.seek(4,1)
                                uvx_aa9_7d = unpack("<h", f.read(2))[0] / 4096
                                uvy_aa9_7d = unpack("<h", f.read(2))[0] / 4096
                                f.seek(4,1)
                            for i in range(9):
                                f.seek(-8,1)
                            for i in range(1):
                                uvx_aa1_7e = unpack("<h", f.read(2))[0] / 4096
                                uvy_aa1_7e = unpack("<h", f.read(2))[0] / 4096
                                f.seek(4,1)
                                uvx_aa2_7e = unpack("<h", f.read(2))[0] / 4096
                                uvy_aa2_7e = unpack("<h", f.read(2))[0] / 4096
                                f.seek(4,1)
                                uvx_aa3_7e = unpack("<h", f.read(2))[0] / 4096
                                uvy_aa3_7e = unpack("<h", f.read(2))[0] / 4096
                                f.seek(4,1)
                                uvx_aa4_7e = unpack("<h", f.read(2))[0] / 4096
                                uvy_aa4_7e = unpack("<h", f.read(2))[0] / 4096
                                f.seek(4,1)
                                uvx_aa5_7e = unpack("<h", f.read(2))[0] / 4096
                                uvy_aa5_7e = unpack("<h", f.read(2))[0] / 4096
                                f.seek(4,1)
                                uvx_aa6_7e = unpack("<h", f.read(2))[0] / 4096
                                uvy_aa6_7e = unpack("<h", f.read(2))[0] / 4096
                                f.seek(4,1)
                                uvx_aa7_7e = unpack("<h", f.read(2))[0] / 4096
                                uvy_aa7_7e = unpack("<h", f.read(2))[0] / 4096
                                f.seek(4,1)
                                uvx_aa8_7e = unpack("<h", f.read(2))[0] / 4096
                                uvy_aa8_7e = unpack("<h", f.read(2))[0] / 4096
                                f.seek(4,1)
                                uvx_aa9_7e = unpack("<h", f.read(2))[0] / 4096
                                uvy_aa9_7e = unpack("<h", f.read(2))[0] / 4096
                                f.seek(4,1)
                            offset1ca_____ = unpack("<I", f.read(4))[0]
                            if offset1ca_____ == 83886080:
                                offset1da_____ = unpack("<I", f.read(4))[0]
                                if offset1da_____ == 1846132741:
                                    for i in range(1):
                                        r1_aa1_7 = unpack("B", f.read(1))[0] / 127
                                        g1_aa1_7 = unpack("B", f.read(1))[0] / 127
                                        b1_aa1_7 = unpack("B", f.read(1))[0] / 127
                                        a1_aa1_7 = unpack("B", f.read(1))[0] / 127
                                        r1_aa2_7 = unpack("B", f.read(1))[0] / 127
                                        g1_aa2_7 = unpack("B", f.read(1))[0] / 127
                                        b1_aa2_7 = unpack("B", f.read(1))[0] / 127
                                        a1_aa2_7 = unpack("B", f.read(1))[0] / 127
                                        r1_aa3_7 = unpack("B", f.read(1))[0] / 127
                                        g1_aa3_7 = unpack("B", f.read(1))[0] / 127
                                        b1_aa3_7 = unpack("B", f.read(1))[0] / 127
                                        a1_aa3_7 = unpack("B", f.read(1))[0] / 127
                                        r1_aa4_7 = unpack("B", f.read(1))[0] / 127
                                        g1_aa4_7 = unpack("B", f.read(1))[0] / 127
                                        b1_aa4_7 = unpack("B", f.read(1))[0] / 127
                                        a1_aa4_7 = unpack("B", f.read(1))[0] / 127
                                        r1_aa5_7 = unpack("B", f.read(1))[0] / 127
                                        g1_aa5_7 = unpack("B", f.read(1))[0] / 127
                                        b1_aa5_7 = unpack("B", f.read(1))[0] / 127
                                        a1_aa5_7 = unpack("B", f.read(1))[0] / 127
                                        r1_aa6_7 = unpack("B", f.read(1))[0] / 127
                                        g1_aa6_7 = unpack("B", f.read(1))[0] / 127
                                        b1_aa6_7 = unpack("B", f.read(1))[0] / 127
                                        a1_aa6_7 = unpack("B", f.read(1))[0] / 127
                                        r1_aa7_7 = unpack("B", f.read(1))[0] / 127
                                        g1_aa7_7 = unpack("B", f.read(1))[0] / 127
                                        b1_aa7_7 = unpack("B", f.read(1))[0] / 127
                                        a1_aa7_7 = unpack("B", f.read(1))[0] / 127
                                        r1_aa8_7 = unpack("B", f.read(1))[0] / 127
                                        g1_aa8_7 = unpack("B", f.read(1))[0] / 127
                                        b1_aa8_7 = unpack("B", f.read(1))[0] / 127
                                        a1_aa8_7 = unpack("B", f.read(1))[0] / 127
                                        r1_aa9_7 = unpack("B", f.read(1))[0] / 127
                                        g1_aa9_7 = unpack("B", f.read(1))[0] / 127
                                        b1_aa9_7 = unpack("B", f.read(1))[0] / 127
                                        a1_aa9_7 = unpack("B", f.read(1))[0] / 127
                                    for i in range(9):
                                        f.seek(-4,1)
                                    for i in range(1):
                                        r1_aa1_7a = unpack("B", f.read(1))[0] / 127
                                        g1_aa1_7a = unpack("B", f.read(1))[0] / 127
                                        b1_aa1_7a = unpack("B", f.read(1))[0] / 127
                                        a1_aa1_7a = unpack("B", f.read(1))[0] / 127
                                        r1_aa2_7a = unpack("B", f.read(1))[0] / 127
                                        g1_aa2_7a = unpack("B", f.read(1))[0] / 127
                                        b1_aa2_7a = unpack("B", f.read(1))[0] / 127
                                        a1_aa2_7a = unpack("B", f.read(1))[0] / 127
                                        r1_aa3_7a = unpack("B", f.read(1))[0] / 127
                                        g1_aa3_7a = unpack("B", f.read(1))[0] / 127
                                        b1_aa3_7a = unpack("B", f.read(1))[0] / 127
                                        a1_aa3_7a = unpack("B", f.read(1))[0] / 127
                                        r1_aa4_7a = unpack("B", f.read(1))[0] / 127
                                        g1_aa4_7a = unpack("B", f.read(1))[0] / 127
                                        b1_aa4_7a = unpack("B", f.read(1))[0] / 127
                                        a1_aa4_7a = unpack("B", f.read(1))[0] / 127
                                        r1_aa5_7a = unpack("B", f.read(1))[0] / 127
                                        g1_aa5_7a = unpack("B", f.read(1))[0] / 127
                                        b1_aa5_7a = unpack("B", f.read(1))[0] / 127
                                        a1_aa5_7a = unpack("B", f.read(1))[0] / 127
                                        r1_aa6_7a = unpack("B", f.read(1))[0] / 127
                                        g1_aa6_7a = unpack("B", f.read(1))[0] / 127
                                        b1_aa6_7a = unpack("B", f.read(1))[0] / 127
                                        a1_aa6_7a = unpack("B", f.read(1))[0] / 127
                                        r1_aa7_7a = unpack("B", f.read(1))[0] / 127
                                        g1_aa7_7a = unpack("B", f.read(1))[0] / 127
                                        b1_aa7_7a = unpack("B", f.read(1))[0] / 127
                                        a1_aa7_7a = unpack("B", f.read(1))[0] / 127
                                        r1_aa8_7a = unpack("B", f.read(1))[0] / 127
                                        g1_aa8_7a = unpack("B", f.read(1))[0] / 127
                                        b1_aa8_7a = unpack("B", f.read(1))[0] / 127
                                        a1_aa8_7a = unpack("B", f.read(1))[0] / 127
                                        r1_aa9_7a = unpack("B", f.read(1))[0] / 127
                                        g1_aa9_7a = unpack("B", f.read(1))[0] / 127
                                        b1_aa9_7a = unpack("B", f.read(1))[0] / 127
                                        a1_aa9_7a = unpack("B", f.read(1))[0] / 127
                                    for i in range(9):
                                        f.seek(-4,1)
                                    for i in range(1):
                                        r1_aa1_7b = unpack("B", f.read(1))[0] / 127
                                        g1_aa1_7b = unpack("B", f.read(1))[0] / 127
                                        b1_aa1_7b = unpack("B", f.read(1))[0] / 127
                                        a1_aa1_7b = unpack("B", f.read(1))[0] / 127
                                        r1_aa2_7b = unpack("B", f.read(1))[0] / 127
                                        g1_aa2_7b = unpack("B", f.read(1))[0] / 127
                                        b1_aa2_7b = unpack("B", f.read(1))[0] / 127
                                        a1_aa2_7b = unpack("B", f.read(1))[0] / 127
                                        r1_aa3_7b = unpack("B", f.read(1))[0] / 127
                                        g1_aa3_7b = unpack("B", f.read(1))[0] / 127
                                        b1_aa3_7b = unpack("B", f.read(1))[0] / 127
                                        a1_aa3_7b = unpack("B", f.read(1))[0] / 127
                                        r1_aa4_7b = unpack("B", f.read(1))[0] / 127
                                        g1_aa4_7b = unpack("B", f.read(1))[0] / 127
                                        b1_aa4_7b = unpack("B", f.read(1))[0] / 127
                                        a1_aa4_7b = unpack("B", f.read(1))[0] / 127
                                        r1_aa5_7b = unpack("B", f.read(1))[0] / 127
                                        g1_aa5_7b = unpack("B", f.read(1))[0] / 127
                                        b1_aa5_7b = unpack("B", f.read(1))[0] / 127
                                        a1_aa5_7b = unpack("B", f.read(1))[0] / 127
                                        r1_aa6_7b = unpack("B", f.read(1))[0] / 127
                                        g1_aa6_7b = unpack("B", f.read(1))[0] / 127
                                        b1_aa6_7b = unpack("B", f.read(1))[0] / 127
                                        a1_aa6_7b = unpack("B", f.read(1))[0] / 127
                                        r1_aa7_7b = unpack("B", f.read(1))[0] / 127
                                        g1_aa7_7b = unpack("B", f.read(1))[0] / 127
                                        b1_aa7_7b = unpack("B", f.read(1))[0] / 127
                                        a1_aa7_7b = unpack("B", f.read(1))[0] / 127
                                        r1_aa8_7b = unpack("B", f.read(1))[0] / 127
                                        g1_aa8_7b = unpack("B", f.read(1))[0] / 127
                                        b1_aa8_7b = unpack("B", f.read(1))[0] / 127
                                        a1_aa8_7b = unpack("B", f.read(1))[0] / 127
                                        r1_aa9_7b = unpack("B", f.read(1))[0] / 127
                                        g1_aa9_7b = unpack("B", f.read(1))[0] / 127
                                        b1_aa9_7b = unpack("B", f.read(1))[0] / 127
                                        a1_aa9_7b = unpack("B", f.read(1))[0] / 127
                                    for i in range(9):
                                        f.seek(-4,1)
                                    for i in range(1):
                                        r1_aa1_7c = unpack("B", f.read(1))[0] / 127
                                        g1_aa1_7c = unpack("B", f.read(1))[0] / 127
                                        b1_aa1_7c = unpack("B", f.read(1))[0] / 127
                                        a1_aa1_7c = unpack("B", f.read(1))[0] / 127
                                        r1_aa2_7c = unpack("B", f.read(1))[0] / 127
                                        g1_aa2_7c = unpack("B", f.read(1))[0] / 127
                                        b1_aa2_7c = unpack("B", f.read(1))[0] / 127
                                        a1_aa2_7c = unpack("B", f.read(1))[0] / 127
                                        r1_aa3_7c = unpack("B", f.read(1))[0] / 127
                                        g1_aa3_7c = unpack("B", f.read(1))[0] / 127
                                        b1_aa3_7c = unpack("B", f.read(1))[0] / 127
                                        a1_aa3_7c = unpack("B", f.read(1))[0] / 127
                                        r1_aa4_7c = unpack("B", f.read(1))[0] / 127
                                        g1_aa4_7c = unpack("B", f.read(1))[0] / 127
                                        b1_aa4_7c = unpack("B", f.read(1))[0] / 127
                                        a1_aa4_7c = unpack("B", f.read(1))[0] / 127
                                        r1_aa5_7c = unpack("B", f.read(1))[0] / 127
                                        g1_aa5_7c = unpack("B", f.read(1))[0] / 127
                                        b1_aa5_7c = unpack("B", f.read(1))[0] / 127
                                        a1_aa5_7c = unpack("B", f.read(1))[0] / 127
                                        r1_aa6_7c = unpack("B", f.read(1))[0] / 127
                                        g1_aa6_7c = unpack("B", f.read(1))[0] / 127
                                        b1_aa6_7c = unpack("B", f.read(1))[0] / 127
                                        a1_aa6_7c = unpack("B", f.read(1))[0] / 127
                                        r1_aa7_7c = unpack("B", f.read(1))[0] / 127
                                        g1_aa7_7c = unpack("B", f.read(1))[0] / 127
                                        b1_aa7_7c = unpack("B", f.read(1))[0] / 127
                                        a1_aa7_7c = unpack("B", f.read(1))[0] / 127
                                        r1_aa8_7c = unpack("B", f.read(1))[0] / 127
                                        g1_aa8_7c = unpack("B", f.read(1))[0] / 127
                                        b1_aa8_7c = unpack("B", f.read(1))[0] / 127
                                        a1_aa8_7c = unpack("B", f.read(1))[0] / 127
                                        r1_aa9_7c = unpack("B", f.read(1))[0] / 127
                                        g1_aa9_7c = unpack("B", f.read(1))[0] / 127
                                        b1_aa9_7c = unpack("B", f.read(1))[0] / 127
                                        a1_aa9_7c = unpack("B", f.read(1))[0] / 127
                                    for i in range(9):
                                        f.seek(-4,1)
                                    for i in range(1):
                                        r1_aa1_7d = unpack("B", f.read(1))[0] / 127
                                        g1_aa1_7d = unpack("B", f.read(1))[0] / 127
                                        b1_aa1_7d = unpack("B", f.read(1))[0] / 127
                                        a1_aa1_7d = unpack("B", f.read(1))[0] / 127
                                        r1_aa2_7d = unpack("B", f.read(1))[0] / 127
                                        g1_aa2_7d = unpack("B", f.read(1))[0] / 127
                                        b1_aa2_7d = unpack("B", f.read(1))[0] / 127
                                        a1_aa2_7d = unpack("B", f.read(1))[0] / 127
                                        r1_aa3_7d = unpack("B", f.read(1))[0] / 127
                                        g1_aa3_7d = unpack("B", f.read(1))[0] / 127
                                        b1_aa3_7d = unpack("B", f.read(1))[0] / 127
                                        a1_aa3_7d = unpack("B", f.read(1))[0] / 127
                                        r1_aa4_7d = unpack("B", f.read(1))[0] / 127
                                        g1_aa4_7d = unpack("B", f.read(1))[0] / 127
                                        b1_aa4_7d = unpack("B", f.read(1))[0] / 127
                                        a1_aa4_7d = unpack("B", f.read(1))[0] / 127
                                        r1_aa5_7d = unpack("B", f.read(1))[0] / 127
                                        g1_aa5_7d = unpack("B", f.read(1))[0] / 127
                                        b1_aa5_7d = unpack("B", f.read(1))[0] / 127
                                        a1_aa5_7d = unpack("B", f.read(1))[0] / 127
                                        r1_aa6_7d = unpack("B", f.read(1))[0] / 127
                                        g1_aa6_7d = unpack("B", f.read(1))[0] / 127
                                        b1_aa6_7d = unpack("B", f.read(1))[0] / 127
                                        a1_aa6_7d = unpack("B", f.read(1))[0] / 127
                                        r1_aa7_7d = unpack("B", f.read(1))[0] / 127
                                        g1_aa7_7d = unpack("B", f.read(1))[0] / 127
                                        b1_aa7_7d = unpack("B", f.read(1))[0] / 127
                                        a1_aa7_7d = unpack("B", f.read(1))[0] / 127
                                        r1_aa8_7d = unpack("B", f.read(1))[0] / 127
                                        g1_aa8_7d = unpack("B", f.read(1))[0] / 127
                                        b1_aa8_7d = unpack("B", f.read(1))[0] / 127
                                        a1_aa8_7d = unpack("B", f.read(1))[0] / 127
                                        r1_aa9_7d = unpack("B", f.read(1))[0] / 127
                                        g1_aa9_7d = unpack("B", f.read(1))[0] / 127
                                        b1_aa9_7d = unpack("B", f.read(1))[0] / 127
                                        a1_aa9_7d = unpack("B", f.read(1))[0] / 127
                                    for i in range(9):
                                        f.seek(-4,1)
                                    for i in range(1):
                                        r1_aa1_7e = unpack("B", f.read(1))[0] / 127
                                        g1_aa1_7e = unpack("B", f.read(1))[0] / 127
                                        b1_aa1_7e = unpack("B", f.read(1))[0] / 127
                                        a1_aa1_7e = unpack("B", f.read(1))[0] / 127
                                        r1_aa2_7e = unpack("B", f.read(1))[0] / 127
                                        g1_aa2_7e = unpack("B", f.read(1))[0] / 127
                                        b1_aa2_7e = unpack("B", f.read(1))[0] / 127
                                        a1_aa2_7e = unpack("B", f.read(1))[0] / 127
                                        r1_aa3_7e = unpack("B", f.read(1))[0] / 127
                                        g1_aa3_7e = unpack("B", f.read(1))[0] / 127
                                        b1_aa3_7e = unpack("B", f.read(1))[0] / 127
                                        a1_aa3_7e = unpack("B", f.read(1))[0] / 127
                                        r1_aa4_7e = unpack("B", f.read(1))[0] / 127
                                        g1_aa4_7e = unpack("B", f.read(1))[0] / 127
                                        b1_aa4_7e = unpack("B", f.read(1))[0] / 127
                                        a1_aa4_7e = unpack("B", f.read(1))[0] / 127
                                        r1_aa5_7e = unpack("B", f.read(1))[0] / 127
                                        g1_aa5_7e = unpack("B", f.read(1))[0] / 127
                                        b1_aa5_7e = unpack("B", f.read(1))[0] / 127
                                        a1_aa5_7e = unpack("B", f.read(1))[0] / 127
                                        r1_aa6_7e = unpack("B", f.read(1))[0] / 127
                                        g1_aa6_7e = unpack("B", f.read(1))[0] / 127
                                        b1_aa6_7e = unpack("B", f.read(1))[0] / 127
                                        a1_aa6_7e = unpack("B", f.read(1))[0] / 127
                                        r1_aa7_7e = unpack("B", f.read(1))[0] / 127
                                        g1_aa7_7e = unpack("B", f.read(1))[0] / 127
                                        b1_aa7_7e = unpack("B", f.read(1))[0] / 127
                                        a1_aa7_7e = unpack("B", f.read(1))[0] / 127
                                        r1_aa8_7e = unpack("B", f.read(1))[0] / 127
                                        g1_aa8_7e = unpack("B", f.read(1))[0] / 127
                                        b1_aa8_7e = unpack("B", f.read(1))[0] / 127
                                        a1_aa8_7e = unpack("B", f.read(1))[0] / 127
                                        r1_aa9_7e = unpack("B", f.read(1))[0] / 127
                                        g1_aa9_7e = unpack("B", f.read(1))[0] / 127
                                        b1_aa9_7e = unpack("B", f.read(1))[0] / 127
                                        a1_aa9_7e = unpack("B", f.read(1))[0] / 127
                                    offset1ea_____ = unpack("<I", f.read(4))[0]
                                    if offset1ea_____ == 16777473:
                                        offset3fa_____ = unpack("<I", f.read(4))[0]
                                        if offset3fa_____ == 335545088:
                                            if type35e == 1:
                                                if type36e == 1:
                                                    if type37e == 0:
                                                        if type38e == 1:
                                                            if type39e == 1:
                                                                if type40e == 0:
                                                                    if type41e == 1:
                                                                        if type42e == 1:
                                                                            if type43e == 0:
                                                                                verticesE2aaaaaaaaaz.append([vx35e,vz35e,vy35e])
                                                                                verticesE2aaaaaaaaaz.append([vx36e,vz36e,vy36e])
                                                                                verticesE2aaaaaaaaaz.append([vx37e,vz37e,vy37e])
                                                                                verticesE2aaaaaaaaaz.append([vx38e,vz38e,vy38e])
                                                                                verticesE2aaaaaaaaaz.append([vx39e,vz39e,vy39e])
                                                                                verticesE2aaaaaaaaaz.append([vx40e,vz40e,vy40e])
                                                                                verticesE2aaaaaaaaaz.append([vx41e,vz41e,vy41e])
                                                                                verticesE2aaaaaaaaaz.append([vx42e,vz42e,vy42e])
                                                                                verticesE2aaaaaaaaaz.append([vx43e,vz43e,vy43e])
                                                                                fa_pamamanz+=1*9#9
                                                                                fb_pamamanz+=1*9#8
                                                                                fc_pamamanz+=1*9#7
                                                                                fa_qamamanz+=1*9#6
                                                                                fb_qamamanz+=1*9#5
                                                                                fc_qamamanz+=1*9#4
                                                                                fa_ramamanz+=1*9#3
                                                                                fb_ramamanz+=1*9#2
                                                                                fc_ramamanz+=1*9#1
                                                                                facesE2aaaaaaaaaz.append([fa_pamamanz,fb_pamamanz,fc_pamamanz])
                                                                                facesE2aaaaaaaaaz.append([fa_qamamanz,fb_qamamanz,fc_qamamanz])
                                                                                facesE2aaaaaaaaaz.append([fa_ramamanz,fb_ramamanz,fc_ramamanz])
                                                                                uvsE2aaaaaaaaaz.append([uvx_aa1_7e,-uvy_aa1_7e])
                                                                                uvsE2aaaaaaaaaz.append([uvx_aa2_7e,-uvy_aa2_7e])
                                                                                uvsE2aaaaaaaaaz.append([uvx_aa3_7e,-uvy_aa3_7e])
                                                                                uvsE2aaaaaaaaaz.append([uvx_aa4_7e,-uvy_aa4_7e])
                                                                                uvsE2aaaaaaaaaz.append([uvx_aa5_7e,-uvy_aa5_7e])
                                                                                uvsE2aaaaaaaaaz.append([uvx_aa6_7e,-uvy_aa6_7e])
                                                                                uvsE2aaaaaaaaaz.append([uvx_aa7_7e,-uvy_aa7_7e])
                                                                                uvsE2aaaaaaaaaz.append([uvx_aa8_7e,-uvy_aa8_7e])
                                                                                uvsE2aaaaaaaaaz.append([uvx_aa9_7e,-uvy_aa9_7e])
                                                                                vcolE2aaaaaaaaaz.append([r1_aa1_7e,g1_aa1_7e,b1_aa1_7e,a1_aa1_7e])
                                                                                vcolE2aaaaaaaaaz.append([r1_aa2_7e,g1_aa2_7e,b1_aa2_7e,a1_aa2_7e])
                                                                                vcolE2aaaaaaaaaz.append([r1_aa3_7e,g1_aa3_7e,b1_aa3_7e,a1_aa3_7e])
                                                                                vcolE2aaaaaaaaaz.append([r1_aa4_7e,g1_aa4_7e,b1_aa4_7e,a1_aa4_7e])
                                                                                vcolE2aaaaaaaaaz.append([r1_aa5_7e,g1_aa5_7e,b1_aa5_7e,a1_aa5_7e])
                                                                                vcolE2aaaaaaaaaz.append([r1_aa6_7e,g1_aa6_7e,b1_aa6_7e,a1_aa6_7e])
                                                                                vcolE2aaaaaaaaaz.append([r1_aa7_7e,g1_aa7_7e,b1_aa7_7e,a1_aa7_7e])
                                                                                vcolE2aaaaaaaaaz.append([r1_aa8_7e,g1_aa8_7e,b1_aa8_7e,a1_aa8_7e])
                                                                                vcolE2aaaaaaaaaz.append([r1_aa9_7e,g1_aa9_7e,b1_aa9_7e,a1_aa9_7e])
                                            if type35d == 1:
                                                if type36d == 1:
                                                    if type37d == 0:
                                                        if type38d == 0:
                                                            if type39d == 0:
                                                                if type40d == 0:
                                                                    if type41d == 1:
                                                                        if type42d == 1:
                                                                            if type43d == 0:
                                                                                verticesE2aaaaaaaaa.append([vx35d,vz35d,vy35d])
                                                                                verticesE2aaaaaaaaa.append([vx36d,vz36d,vy36d])
                                                                                verticesE2aaaaaaaaa.append([vx37d,vz37d,vy37d])
                                                                                verticesE2aaaaaaaaa.append([vx38d,vz38d,vy38d])
                                                                                verticesE2aaaaaaaaa.append([vx39d,vz39d,vy39d])
                                                                                verticesE2aaaaaaaaa.append([vx40d,vz40d,vy40d])
                                                                                verticesE2aaaaaaaaa.append([vx41d,vz41d,vy41d])
                                                                                verticesE2aaaaaaaaa.append([vx42d,vz42d,vy42d])
                                                                                verticesE2aaaaaaaaa.append([vx43d,vz43d,vy43d])
                                                                                fa_pamaman+=1*9#9
                                                                                fb_pamaman+=1*9#8
                                                                                fc_pamaman+=1*9#7
                                                                                fa_qamaman+=1*9#8
                                                                                fb_qamaman+=1*9#7
                                                                                fc_qamaman+=1*9#6
                                                                                fa_ramaman+=1*9#7
                                                                                fb_ramaman+=1*9#6
                                                                                fc_ramaman+=1*9#5
                                                                                fa_samaman+=1*9#6
                                                                                fb_samaman+=1*9#5
                                                                                fc_samaman+=1*9#4
                                                                                fa_tamaman+=1*9#3
                                                                                fb_tamaman+=1*9#2
                                                                                fc_tamaman+=1*9#1
                                                                                facesE2aaaaaaaaa.append([fa_pamaman,fb_pamaman,fc_pamaman])
                                                                                facesE2aaaaaaaaa.append([fa_qamaman,fb_qamaman,fc_qamaman])
                                                                                facesE2aaaaaaaaa.append([fa_ramaman,fb_ramaman,fc_ramaman])
                                                                                facesE2aaaaaaaaa.append([fa_samaman,fb_samaman,fc_samaman])
                                                                                facesE2aaaaaaaaa.append([fa_tamaman,fb_tamaman,fc_tamaman])
                                                                                uvsE2aaaaaaaaa.append([uvx_aa1_7d,-uvy_aa1_7d])
                                                                                uvsE2aaaaaaaaa.append([uvx_aa2_7d,-uvy_aa2_7d])
                                                                                uvsE2aaaaaaaaa.append([uvx_aa3_7d,-uvy_aa3_7d])
                                                                                uvsE2aaaaaaaaa.append([uvx_aa4_7d,-uvy_aa4_7d])
                                                                                uvsE2aaaaaaaaa.append([uvx_aa5_7d,-uvy_aa5_7d])
                                                                                uvsE2aaaaaaaaa.append([uvx_aa6_7d,-uvy_aa6_7d])
                                                                                uvsE2aaaaaaaaa.append([uvx_aa7_7d,-uvy_aa7_7d])
                                                                                uvsE2aaaaaaaaa.append([uvx_aa8_7d,-uvy_aa8_7d])
                                                                                uvsE2aaaaaaaaa.append([uvx_aa9_7d,-uvy_aa9_7d])
                                                                                vcolE2aaaaaaaaa.append([r1_aa1_7d,g1_aa1_7d,b1_aa1_7d,a1_aa1_7d])
                                                                                vcolE2aaaaaaaaa.append([r1_aa2_7d,g1_aa2_7d,b1_aa2_7d,a1_aa2_7d])
                                                                                vcolE2aaaaaaaaa.append([r1_aa3_7d,g1_aa3_7d,b1_aa3_7d,a1_aa3_7d])
                                                                                vcolE2aaaaaaaaa.append([r1_aa4_7d,g1_aa4_7d,b1_aa4_7d,a1_aa4_7d])
                                                                                vcolE2aaaaaaaaa.append([r1_aa5_7d,g1_aa5_7d,b1_aa5_7d,a1_aa5_7d])
                                                                                vcolE2aaaaaaaaa.append([r1_aa6_7d,g1_aa6_7d,b1_aa6_7d,a1_aa6_7d])
                                                                                vcolE2aaaaaaaaa.append([r1_aa7_7d,g1_aa7_7d,b1_aa7_7d,a1_aa7_7d])
                                                                                vcolE2aaaaaaaaa.append([r1_aa8_7d,g1_aa8_7d,b1_aa8_7d,a1_aa8_7d])
                                                                                vcolE2aaaaaaaaa.append([r1_aa9_7d,g1_aa9_7d,b1_aa9_7d,a1_aa9_7d])
                                            if type35c == 1:
                                                if type36c == 1:
                                                    if type37c == 0:
                                                        if type38c == 0:
                                                            if type39c == 0:
                                                                if type40c == 1:
                                                                    if type41c == 1:
                                                                        if type42c == 0:
                                                                            if type43c == 0:
                                                                                verticesE2aaaaaaaa.append([vx35c,vz35c,vy35c])
                                                                                verticesE2aaaaaaaa.append([vx36c,vz36c,vy36c])
                                                                                verticesE2aaaaaaaa.append([vx37c,vz37c,vy37c])
                                                                                verticesE2aaaaaaaa.append([vx38c,vz38c,vy38c])
                                                                                verticesE2aaaaaaaa.append([vx39c,vz39c,vy39c])
                                                                                verticesE2aaaaaaaa.append([vx40c,vz40c,vy40c])
                                                                                verticesE2aaaaaaaa.append([vx41c,vz41c,vy41c])
                                                                                verticesE2aaaaaaaa.append([vx42c,vz42c,vy42c])
                                                                                verticesE2aaaaaaaa.append([vx43c,vz43c,vy43c])
                                                                                fa_pamama+=1*9#9
                                                                                fb_pamama+=1*9#8
                                                                                fc_pamama+=1*9#7
                                                                                fa_qamama+=1*9#8
                                                                                fb_qamama+=1*9#7
                                                                                fc_qamama+=1*9#6
                                                                                fa_ramama+=1*9#7
                                                                                fb_ramama+=1*9#6
                                                                                fc_ramama+=1*9#5
                                                                                fa_samama+=1*9#4
                                                                                fb_samama+=1*9#3
                                                                                fc_samama+=1*9#2
                                                                                fa_tamama+=1*9#3
                                                                                fb_tamama+=1*9#2
                                                                                fc_tamama+=1*9#1
                                                                                facesE2aaaaaaaa.append([fa_pamama,fb_pamama,fc_pamama])
                                                                                facesE2aaaaaaaa.append([fa_qamama,fb_qamama,fc_qamama])
                                                                                facesE2aaaaaaaa.append([fa_ramama,fb_ramama,fc_ramama])
                                                                                facesE2aaaaaaaa.append([fa_samama,fb_samama,fc_samama])
                                                                                facesE2aaaaaaaa.append([fa_tamama,fb_tamama,fc_tamama])
                                                                                uvsE2aaaaaaaa.append([uvx_aa1_7c,-uvy_aa1_7c])
                                                                                uvsE2aaaaaaaa.append([uvx_aa2_7c,-uvy_aa2_7c])
                                                                                uvsE2aaaaaaaa.append([uvx_aa3_7c,-uvy_aa3_7c])
                                                                                uvsE2aaaaaaaa.append([uvx_aa4_7c,-uvy_aa4_7c])
                                                                                uvsE2aaaaaaaa.append([uvx_aa5_7c,-uvy_aa5_7c])
                                                                                uvsE2aaaaaaaa.append([uvx_aa6_7c,-uvy_aa6_7c])
                                                                                uvsE2aaaaaaaa.append([uvx_aa7_7c,-uvy_aa7_7c])
                                                                                uvsE2aaaaaaaa.append([uvx_aa8_7c,-uvy_aa8_7c])
                                                                                uvsE2aaaaaaaa.append([uvx_aa9_7c,-uvy_aa9_7c])
                                                                                vcolE2aaaaaaaa.append([r1_aa1_7c,g1_aa1_7c,b1_aa1_7c,a1_aa1_7c])
                                                                                vcolE2aaaaaaaa.append([r1_aa2_7c,g1_aa2_7c,b1_aa2_7c,a1_aa2_7c])
                                                                                vcolE2aaaaaaaa.append([r1_aa3_7c,g1_aa3_7c,b1_aa3_7c,a1_aa3_7c])
                                                                                vcolE2aaaaaaaa.append([r1_aa4_7c,g1_aa4_7c,b1_aa4_7c,a1_aa4_7c])
                                                                                vcolE2aaaaaaaa.append([r1_aa5_7c,g1_aa5_7c,b1_aa5_7c,a1_aa5_7c])
                                                                                vcolE2aaaaaaaa.append([r1_aa6_7c,g1_aa6_7c,b1_aa6_7c,a1_aa6_7c])
                                                                                vcolE2aaaaaaaa.append([r1_aa7_7c,g1_aa7_7c,b1_aa7_7c,a1_aa7_7c])
                                                                                vcolE2aaaaaaaa.append([r1_aa8_7c,g1_aa8_7c,b1_aa8_7c,a1_aa8_7c])
                                                                                vcolE2aaaaaaaa.append([r1_aa9_7c,g1_aa9_7c,b1_aa9_7c,a1_aa9_7c])
                                            if type35b == 1:
                                                if type36b == 1:
                                                    if type37b == 0:
                                                        if type38b == 0:
                                                            if type39b == 1:
                                                                if type40b == 1:
                                                                    if type41b == 0:
                                                                        if type42b == 0:
                                                                            if type43b == 0:
                                                                                verticesE2aaaaaaa.append([vx35b,vz35b,vy35b])
                                                                                verticesE2aaaaaaa.append([vx36b,vz36b,vy36b])
                                                                                verticesE2aaaaaaa.append([vx37b,vz37b,vy37b])
                                                                                verticesE2aaaaaaa.append([vx38b,vz38b,vy38b])
                                                                                verticesE2aaaaaaa.append([vx39b,vz39b,vy39b])
                                                                                verticesE2aaaaaaa.append([vx40b,vz40b,vy40b])
                                                                                verticesE2aaaaaaa.append([vx41b,vz41b,vy41b])
                                                                                verticesE2aaaaaaa.append([vx42b,vz42b,vy42b])
                                                                                verticesE2aaaaaaa.append([vx43b,vz43b,vy43b])
                                                                                fa_pamam+=1*9#9
                                                                                fb_pamam+=1*9#8
                                                                                fc_pamam+=1*9#7
                                                                                fa_qamam+=1*9#8
                                                                                fb_qamam+=1*9#7
                                                                                fc_qamam+=1*9#6
                                                                                fa_ramam+=1*9#5
                                                                                fb_ramam+=1*9#4
                                                                                fc_ramam+=1*9#3
                                                                                fa_samam+=1*9#4
                                                                                fb_samam+=1*9#3
                                                                                fc_samam+=1*9#2
                                                                                fa_tamam+=1*9#3
                                                                                fb_tamam+=1*9#2
                                                                                fc_tamam+=1*9#1
                                                                                facesE2aaaaaaa.append([fa_pamam,fb_pamam,fc_pamam])
                                                                                facesE2aaaaaaa.append([fa_qamam,fb_qamam,fc_qamam])
                                                                                facesE2aaaaaaa.append([fa_ramam,fb_ramam,fc_ramam])
                                                                                facesE2aaaaaaa.append([fa_samam,fb_samam,fc_samam])
                                                                                facesE2aaaaaaa.append([fa_tamam,fb_tamam,fc_tamam])
                                                                                uvsE2aaaaaaa.append([uvx_aa1_7b,-uvy_aa1_7b])
                                                                                uvsE2aaaaaaa.append([uvx_aa2_7b,-uvy_aa2_7b])
                                                                                uvsE2aaaaaaa.append([uvx_aa3_7b,-uvy_aa3_7b])
                                                                                uvsE2aaaaaaa.append([uvx_aa4_7b,-uvy_aa4_7b])
                                                                                uvsE2aaaaaaa.append([uvx_aa5_7b,-uvy_aa5_7b])
                                                                                uvsE2aaaaaaa.append([uvx_aa6_7b,-uvy_aa6_7b])
                                                                                uvsE2aaaaaaa.append([uvx_aa7_7b,-uvy_aa7_7b])
                                                                                uvsE2aaaaaaa.append([uvx_aa8_7b,-uvy_aa8_7b])
                                                                                uvsE2aaaaaaa.append([uvx_aa9_7b,-uvy_aa9_7b])
                                                                                vcolE2aaaaaaa.append([r1_aa1_7b,g1_aa1_7b,b1_aa1_7b,a1_aa1_7b])
                                                                                vcolE2aaaaaaa.append([r1_aa2_7b,g1_aa2_7b,b1_aa2_7b,a1_aa2_7b])
                                                                                vcolE2aaaaaaa.append([r1_aa3_7b,g1_aa3_7b,b1_aa3_7b,a1_aa3_7b])
                                                                                vcolE2aaaaaaa.append([r1_aa4_7b,g1_aa4_7b,b1_aa4_7b,a1_aa4_7b])
                                                                                vcolE2aaaaaaa.append([r1_aa5_7b,g1_aa5_7b,b1_aa5_7b,a1_aa5_7b])
                                                                                vcolE2aaaaaaa.append([r1_aa6_7b,g1_aa6_7b,b1_aa6_7b,a1_aa6_7b])
                                                                                vcolE2aaaaaaa.append([r1_aa7_7b,g1_aa7_7b,b1_aa7_7b,a1_aa7_7b])
                                                                                vcolE2aaaaaaa.append([r1_aa8_7b,g1_aa8_7b,b1_aa8_7b,a1_aa8_7b])
                                                                                vcolE2aaaaaaa.append([r1_aa9_7b,g1_aa9_7b,b1_aa9_7b,a1_aa9_7b])
                                            if type35a == 1:
                                                if type36a == 1:
                                                    if type37a == 0:
                                                        if type38a == 1:
                                                            if type39a == 1:
                                                                if type40a == 0:
                                                                    if type41a == 0:
                                                                        if type42a == 0:
                                                                            if type43a == 0:
                                                                                verticesE2aaaaaa.append([vx35a,vz35a,vy35a])
                                                                                verticesE2aaaaaa.append([vx36a,vz36a,vy36a])
                                                                                verticesE2aaaaaa.append([vx37a,vz37a,vy37a])
                                                                                verticesE2aaaaaa.append([vx38a,vz38a,vy38a])
                                                                                verticesE2aaaaaa.append([vx39a,vz39a,vy39a])
                                                                                verticesE2aaaaaa.append([vx40a,vz40a,vy40a])
                                                                                verticesE2aaaaaa.append([vx41a,vz41a,vy41a])
                                                                                verticesE2aaaaaa.append([vx42a,vz42a,vy42a])
                                                                                verticesE2aaaaaa.append([vx43a,vz43a,vy43a])
                                                                                fa_pama+=1*9#9
                                                                                fb_pama+=1*9#8
                                                                                fc_pama+=1*9#7
                                                                                fa_qama+=1*9#6
                                                                                fb_qama+=1*9#5
                                                                                fc_qama+=1*9#4
                                                                                fa_rama+=1*9#5
                                                                                fb_rama+=1*9#4
                                                                                fc_rama+=1*9#3
                                                                                fa_sama+=1*9#4
                                                                                fb_sama+=1*9#3
                                                                                fc_sama+=1*9#2
                                                                                fa_tama+=1*9#3
                                                                                fb_tama+=1*9#2
                                                                                fc_tama+=1*9#1
                                                                                facesE2aaaaaa.append([fa_pama,fb_pama,fc_pama])
                                                                                facesE2aaaaaa.append([fa_qama,fb_qama,fc_qama])
                                                                                facesE2aaaaaa.append([fa_rama,fb_rama,fc_rama])
                                                                                facesE2aaaaaa.append([fa_sama,fb_sama,fc_sama])
                                                                                facesE2aaaaaa.append([fa_tama,fb_tama,fc_tama])
                                                                                uvsE2aaaaaa.append([uvx_aa1_7a,-uvy_aa1_7a])
                                                                                uvsE2aaaaaa.append([uvx_aa2_7a,-uvy_aa2_7a])
                                                                                uvsE2aaaaaa.append([uvx_aa3_7a,-uvy_aa3_7a])
                                                                                uvsE2aaaaaa.append([uvx_aa4_7a,-uvy_aa4_7a])
                                                                                uvsE2aaaaaa.append([uvx_aa5_7a,-uvy_aa5_7a])
                                                                                uvsE2aaaaaa.append([uvx_aa6_7a,-uvy_aa6_7a])
                                                                                uvsE2aaaaaa.append([uvx_aa7_7a,-uvy_aa7_7a])
                                                                                uvsE2aaaaaa.append([uvx_aa8_7a,-uvy_aa8_7a])
                                                                                uvsE2aaaaaa.append([uvx_aa9_7a,-uvy_aa9_7a])
                                                                                vcolE2aaaaaa.append([r1_aa1_7a,g1_aa1_7a,b1_aa1_7a,a1_aa1_7a])
                                                                                vcolE2aaaaaa.append([r1_aa2_7a,g1_aa2_7a,b1_aa2_7a,a1_aa2_7a])
                                                                                vcolE2aaaaaa.append([r1_aa3_7a,g1_aa3_7a,b1_aa3_7a,a1_aa3_7a])
                                                                                vcolE2aaaaaa.append([r1_aa4_7a,g1_aa4_7a,b1_aa4_7a,a1_aa4_7a])
                                                                                vcolE2aaaaaa.append([r1_aa5_7a,g1_aa5_7a,b1_aa5_7a,a1_aa5_7a])
                                                                                vcolE2aaaaaa.append([r1_aa6_7a,g1_aa6_7a,b1_aa6_7a,a1_aa6_7a])
                                                                                vcolE2aaaaaa.append([r1_aa7_7a,g1_aa7_7a,b1_aa7_7a,a1_aa7_7a])
                                                                                vcolE2aaaaaa.append([r1_aa8_7a,g1_aa8_7a,b1_aa8_7a,a1_aa8_7a])
                                                                                vcolE2aaaaaa.append([r1_aa9_7a,g1_aa9_7a,b1_aa9_7a,a1_aa9_7a])
                                            if type35 == 1:
                                                if type36 == 1:
                                                    if type37 == 0:
                                                        if type38 == 0:
                                                            if type39 == 0:
                                                                if type40 == 0:
                                                                    if type41 == 0:
                                                                        if type42 == 0:
                                                                            if type43 == 0:
                                                                                verticesE2aaaaa.append([vx35,vz35,vy35])
                                                                                verticesE2aaaaa.append([vx36,vz36,vy36])
                                                                                verticesE2aaaaa.append([vx37,vz37,vy37])
                                                                                verticesE2aaaaa.append([vx38,vz38,vy38])
                                                                                verticesE2aaaaa.append([vx39,vz39,vy39])
                                                                                verticesE2aaaaa.append([vx40,vz40,vy40])
                                                                                verticesE2aaaaa.append([vx41,vz41,vy41])
                                                                                verticesE2aaaaa.append([vx42,vz42,vy42])
                                                                                verticesE2aaaaa.append([vx43,vz43,vy43])
                                                                                fa_pam+=1*9
                                                                                fb_pam+=1*9
                                                                                fc_pam+=1*9
                                                                                fa_qam+=1*9
                                                                                fb_qam+=1*9
                                                                                fc_qam+=1*9
                                                                                fa_ram+=1*9
                                                                                fb_ram+=1*9
                                                                                fc_ram+=1*9
                                                                                fa_sam+=1*9
                                                                                fb_sam+=1*9
                                                                                fc_sam+=1*9
                                                                                fa_tam+=1*9
                                                                                fb_tam+=1*9
                                                                                fc_tam+=1*9
                                                                                fa_uam+=1*9
                                                                                fb_uam+=1*9
                                                                                fc_uam+=1*9
                                                                                fa_vam+=1*9
                                                                                fb_vam+=1*9
                                                                                fc_vam+=1*9
                                                                                facesE2aaaaa.append([fa_pam,fb_pam,fc_pam])
                                                                                facesE2aaaaa.append([fa_qam,fb_qam,fc_qam])
                                                                                facesE2aaaaa.append([fa_ram,fb_ram,fc_ram])
                                                                                facesE2aaaaa.append([fa_sam,fb_sam,fc_sam])
                                                                                facesE2aaaaa.append([fa_tam,fb_tam,fc_tam])
                                                                                facesE2aaaaa.append([fa_uam,fb_uam,fc_uam])
                                                                                facesE2aaaaa.append([fa_vam,fb_vam,fc_vam])
                                                                                uvsE2aaaaa.append([uvx_aa1_7,-uvy_aa1_7])
                                                                                uvsE2aaaaa.append([uvx_aa2_7,-uvy_aa2_7])
                                                                                uvsE2aaaaa.append([uvx_aa3_7,-uvy_aa3_7])
                                                                                uvsE2aaaaa.append([uvx_aa4_7,-uvy_aa4_7])
                                                                                uvsE2aaaaa.append([uvx_aa5_7,-uvy_aa5_7])
                                                                                uvsE2aaaaa.append([uvx_aa6_7,-uvy_aa6_7])
                                                                                uvsE2aaaaa.append([uvx_aa7_7,-uvy_aa7_7])
                                                                                uvsE2aaaaa.append([uvx_aa8_7,-uvy_aa8_7])
                                                                                uvsE2aaaaa.append([uvx_aa9_7,-uvy_aa9_7])
                                                                                vcolE2aaaaa.append([r1_aa1_7,g1_aa1_7,b1_aa1_7,a1_aa1_7])
                                                                                vcolE2aaaaa.append([r1_aa2_7,g1_aa2_7,b1_aa2_7,a1_aa2_7])
                                                                                vcolE2aaaaa.append([r1_aa3_7,g1_aa3_7,b1_aa3_7,a1_aa3_7])
                                                                                vcolE2aaaaa.append([r1_aa4_7,g1_aa4_7,b1_aa4_7,a1_aa4_7])
                                                                                vcolE2aaaaa.append([r1_aa5_7,g1_aa5_7,b1_aa5_7,a1_aa5_7])
                                                                                vcolE2aaaaa.append([r1_aa6_7,g1_aa6_7,b1_aa6_7,a1_aa6_7])
                                                                                vcolE2aaaaa.append([r1_aa7_7,g1_aa7_7,b1_aa7_7,a1_aa7_7])
                                                                                vcolE2aaaaa.append([r1_aa8_7,g1_aa8_7,b1_aa8_7,a1_aa8_7])
                                                                                vcolE2aaaaa.append([r1_aa9_7,g1_aa9_7,b1_aa9_7,a1_aa9_7])

                elif vertexCount == 10:
                    for jjjj in range(1):
                        vx44 = unpack("<f", f.read(4))[0]
                        vy44 = unpack("<f", f.read(4))[0]
                        vz44 = unpack("<f", f.read(4))[0]
                        type44 = unpack("B", f.read(1))[0]
                        value1a44 = unpack("B", f.read(1))[0]
                        normalZ_44 = unpack("<h", f.read(2))[0]
                        vx45 = unpack("<f", f.read(4))[0]
                        vy45 = unpack("<f", f.read(4))[0]
                        vz45 = unpack("<f", f.read(4))[0]
                        type45 = unpack("B", f.read(1))[0]
                        value1a45 = unpack("B", f.read(1))[0]
                        normalZ_45 = unpack("<h", f.read(2))[0]
                        vx46 = unpack("<f", f.read(4))[0]
                        vy46 = unpack("<f", f.read(4))[0]
                        vz46 = unpack("<f", f.read(4))[0]
                        type46 = unpack("B", f.read(1))[0]
                        value1a46 = unpack("B", f.read(1))[0]
                        normalZ_46 = unpack("<h", f.read(2))[0]
                        vx47 = unpack("<f", f.read(4))[0]
                        vy47 = unpack("<f", f.read(4))[0]
                        vz47 = unpack("<f", f.read(4))[0]
                        type47 = unpack("B", f.read(1))[0]
                        value1a47 = unpack("B", f.read(1))[0]
                        normalZ_47 = unpack("<h", f.read(2))[0]
                        vx48 = unpack("<f", f.read(4))[0]
                        vy48 = unpack("<f", f.read(4))[0]
                        vz48 = unpack("<f", f.read(4))[0]
                        type48 = unpack("B", f.read(1))[0]
                        value1a48 = unpack("B", f.read(1))[0]
                        normalZ_48 = unpack("<h", f.read(2))[0]
                        vx49 = unpack("<f", f.read(4))[0]
                        vy49 = unpack("<f", f.read(4))[0]
                        vz49 = unpack("<f", f.read(4))[0]
                        type49 = unpack("B", f.read(1))[0]
                        value1a49 = unpack("B", f.read(1))[0]
                        normalZ_49 = unpack("<h", f.read(2))[0]
                        vx50 = unpack("<f", f.read(4))[0]
                        vy50 = unpack("<f", f.read(4))[0]
                        vz50 = unpack("<f", f.read(4))[0]
                        type50 = unpack("B", f.read(1))[0]
                        value1a50 = unpack("B", f.read(1))[0]
                        normalZ_50 = unpack("<h", f.read(2))[0]
                        vx51 = unpack("<f", f.read(4))[0]
                        vy51 = unpack("<f", f.read(4))[0]
                        vz51 = unpack("<f", f.read(4))[0]
                        type51 = unpack("B", f.read(1))[0]
                        value1a51 = unpack("B", f.read(1))[0]
                        normalZ_51 = unpack("<h", f.read(2))[0]
                        vx52 = unpack("<f", f.read(4))[0]
                        vy52 = unpack("<f", f.read(4))[0]
                        vz52 = unpack("<f", f.read(4))[0]
                        type52 = unpack("B", f.read(1))[0]
                        value1a52 = unpack("B", f.read(1))[0]
                        normalZ_52 = unpack("<h", f.read(2))[0]
                        vx53 = unpack("<f", f.read(4))[0]
                        vy53 = unpack("<f", f.read(4))[0]
                        vz53 = unpack("<f", f.read(4))[0]
                        type53 = unpack("B", f.read(1))[0]
                        value1a53 = unpack("B", f.read(1))[0]
                        normalZ_53 = unpack("<h", f.read(2))[0]
                    for jjjj in range(vertexCount):
                        f.seek(-16,1)
                    for jjjj in range(1):
                        vx44a = unpack("<f", f.read(4))[0]
                        vy44a = unpack("<f", f.read(4))[0]
                        vz44a = unpack("<f", f.read(4))[0]
                        type44a = unpack("B", f.read(1))[0]
                        value1a44a = unpack("B", f.read(1))[0]
                        normalZ_44a = unpack("<h", f.read(2))[0]
                        vx45a = unpack("<f", f.read(4))[0]
                        vy45a = unpack("<f", f.read(4))[0]
                        vz45a = unpack("<f", f.read(4))[0]
                        type45a = unpack("B", f.read(1))[0]
                        value1a45a = unpack("B", f.read(1))[0]
                        normalZ_45a = unpack("<h", f.read(2))[0]
                        vx46a = unpack("<f", f.read(4))[0]
                        vy46a = unpack("<f", f.read(4))[0]
                        vz46a = unpack("<f", f.read(4))[0]
                        type46a = unpack("B", f.read(1))[0]
                        value1a46a = unpack("B", f.read(1))[0]
                        normalZ_46a = unpack("<h", f.read(2))[0]
                        vx47a = unpack("<f", f.read(4))[0]
                        vy47a = unpack("<f", f.read(4))[0]
                        vz47a = unpack("<f", f.read(4))[0]
                        type47a = unpack("B", f.read(1))[0]
                        value1a47a = unpack("B", f.read(1))[0]
                        normalZ_47a = unpack("<h", f.read(2))[0]
                        vx48a = unpack("<f", f.read(4))[0]
                        vy48a = unpack("<f", f.read(4))[0]
                        vz48a = unpack("<f", f.read(4))[0]
                        type48a = unpack("B", f.read(1))[0]
                        value1a48a = unpack("B", f.read(1))[0]
                        normalZ_48a = unpack("<h", f.read(2))[0]
                        vx49a = unpack("<f", f.read(4))[0]
                        vy49a = unpack("<f", f.read(4))[0]
                        vz49a = unpack("<f", f.read(4))[0]
                        type49a = unpack("B", f.read(1))[0]
                        value1a49a = unpack("B", f.read(1))[0]
                        normalZ_49a = unpack("<h", f.read(2))[0]
                        vx50a = unpack("<f", f.read(4))[0]
                        vy50a = unpack("<f", f.read(4))[0]
                        vz50a = unpack("<f", f.read(4))[0]
                        type50a = unpack("B", f.read(1))[0]
                        value1a50a = unpack("B", f.read(1))[0]
                        normalZ_50a = unpack("<h", f.read(2))[0]
                        vx51a = unpack("<f", f.read(4))[0]
                        vy51a = unpack("<f", f.read(4))[0]
                        vz51a = unpack("<f", f.read(4))[0]
                        type51a = unpack("B", f.read(1))[0]
                        value1a51a = unpack("B", f.read(1))[0]
                        normalZ_51a = unpack("<h", f.read(2))[0]
                        vx52a = unpack("<f", f.read(4))[0]
                        vy52a = unpack("<f", f.read(4))[0]
                        vz52a = unpack("<f", f.read(4))[0]
                        type52a = unpack("B", f.read(1))[0]
                        value1a52a = unpack("B", f.read(1))[0]
                        normalZ_52a = unpack("<h", f.read(2))[0]
                        vx53a = unpack("<f", f.read(4))[0]
                        vy53a = unpack("<f", f.read(4))[0]
                        vz53a = unpack("<f", f.read(4))[0]
                        type53a = unpack("B", f.read(1))[0]
                        value1a53a = unpack("B", f.read(1))[0]
                        normalZ_53a = unpack("<h", f.read(2))[0]
                    offset1cac_____ = unpack("<I", f.read(4))[0]
                    if offset1cac_____ == 83886081:
                        offset1_bee____ = unpack("<I", f.read(4))[0]
                        if offset1_bee____ == 1829404676:
                            for i in range(1):
                                uvx_aa1_8 = unpack("<h", f.read(2))[0] / 4096
                                uvy_aa1_8 = unpack("<h", f.read(2))[0] / 4096
                                f.seek(4,1)
                                uvx_aa2_8 = unpack("<h", f.read(2))[0] / 4096
                                uvy_aa2_8 = unpack("<h", f.read(2))[0] / 4096
                                f.seek(4,1)
                                uvx_aa3_8 = unpack("<h", f.read(2))[0] / 4096
                                uvy_aa3_8 = unpack("<h", f.read(2))[0] / 4096
                                f.seek(4,1)
                                uvx_aa4_8 = unpack("<h", f.read(2))[0] / 4096
                                uvy_aa4_8 = unpack("<h", f.read(2))[0] / 4096
                                f.seek(4,1)
                                uvx_aa5_8 = unpack("<h", f.read(2))[0] / 4096
                                uvy_aa5_8 = unpack("<h", f.read(2))[0] / 4096
                                f.seek(4,1)
                                uvx_aa6_8 = unpack("<h", f.read(2))[0] / 4096
                                uvy_aa6_8 = unpack("<h", f.read(2))[0] / 4096
                                f.seek(4,1)
                                uvx_aa7_8 = unpack("<h", f.read(2))[0] / 4096
                                uvy_aa7_8 = unpack("<h", f.read(2))[0] / 4096
                                f.seek(4,1)
                                uvx_aa8_8 = unpack("<h", f.read(2))[0] / 4096
                                uvy_aa8_8 = unpack("<h", f.read(2))[0] / 4096
                                f.seek(4,1)
                                uvx_aa9_8 = unpack("<h", f.read(2))[0] / 4096
                                uvy_aa9_8 = unpack("<h", f.read(2))[0] / 4096
                                f.seek(4,1)
                                uvx_aa10_8 = unpack("<h", f.read(2))[0] / 4096
                                uvy_aa10_8 = unpack("<h", f.read(2))[0] / 4096
                                f.seek(4,1)
                            for i in range(10):
                                f.seek(-8,1)
                            for i in range(1):
                                uvx_aa1_8a = unpack("<h", f.read(2))[0] / 4096
                                uvy_aa1_8a = unpack("<h", f.read(2))[0] / 4096
                                f.seek(4,1)
                                uvx_aa2_8a = unpack("<h", f.read(2))[0] / 4096
                                uvy_aa2_8a = unpack("<h", f.read(2))[0] / 4096
                                f.seek(4,1)
                                uvx_aa3_8a = unpack("<h", f.read(2))[0] / 4096
                                uvy_aa3_8a = unpack("<h", f.read(2))[0] / 4096
                                f.seek(4,1)
                                uvx_aa4_8a = unpack("<h", f.read(2))[0] / 4096
                                uvy_aa4_8a = unpack("<h", f.read(2))[0] / 4096
                                f.seek(4,1)
                                uvx_aa5_8a = unpack("<h", f.read(2))[0] / 4096
                                uvy_aa5_8a = unpack("<h", f.read(2))[0] / 4096
                                f.seek(4,1)
                                uvx_aa6_8a = unpack("<h", f.read(2))[0] / 4096
                                uvy_aa6_8a = unpack("<h", f.read(2))[0] / 4096
                                f.seek(4,1)
                                uvx_aa7_8a = unpack("<h", f.read(2))[0] / 4096
                                uvy_aa7_8a = unpack("<h", f.read(2))[0] / 4096
                                f.seek(4,1)
                                uvx_aa8_8a = unpack("<h", f.read(2))[0] / 4096
                                uvy_aa8_8a = unpack("<h", f.read(2))[0] / 4096
                                f.seek(4,1)
                                uvx_aa9_8a = unpack("<h", f.read(2))[0] / 4096
                                uvy_aa9_8a = unpack("<h", f.read(2))[0] / 4096
                                f.seek(4,1)
                                uvx_aa10_8a = unpack("<h", f.read(2))[0] / 4096
                                uvy_aa10_8a = unpack("<h", f.read(2))[0] / 4096
                                f.seek(4,1)
                            offset1ca_c____ = unpack("<I", f.read(4))[0]
                            if offset1ca_c____ == 83886080:
                                offset1da_c____ = unpack("<I", f.read(4))[0]
                                if offset1da_c____ == 1846198277:
                                    for i in range(1):
                                        r1_aa1_8 = unpack("B", f.read(1))[0] / 127
                                        g1_aa1_8 = unpack("B", f.read(1))[0] / 127
                                        b1_aa1_8 = unpack("B", f.read(1))[0] / 127
                                        a1_aa1_8 = unpack("B", f.read(1))[0] / 127
                                        r1_aa2_8 = unpack("B", f.read(1))[0] / 127
                                        g1_aa2_8 = unpack("B", f.read(1))[0] / 127
                                        b1_aa2_8 = unpack("B", f.read(1))[0] / 127
                                        a1_aa2_8 = unpack("B", f.read(1))[0] / 127
                                        r1_aa3_8 = unpack("B", f.read(1))[0] / 127
                                        g1_aa3_8 = unpack("B", f.read(1))[0] / 127
                                        b1_aa3_8 = unpack("B", f.read(1))[0] / 127
                                        a1_aa3_8 = unpack("B", f.read(1))[0] / 127
                                        r1_aa4_8 = unpack("B", f.read(1))[0] / 127
                                        g1_aa4_8 = unpack("B", f.read(1))[0] / 127
                                        b1_aa4_8 = unpack("B", f.read(1))[0] / 127
                                        a1_aa4_8 = unpack("B", f.read(1))[0] / 127
                                        r1_aa5_8 = unpack("B", f.read(1))[0] / 127
                                        g1_aa5_8 = unpack("B", f.read(1))[0] / 127
                                        b1_aa5_8 = unpack("B", f.read(1))[0] / 127
                                        a1_aa5_8 = unpack("B", f.read(1))[0] / 127
                                        r1_aa6_8 = unpack("B", f.read(1))[0] / 127
                                        g1_aa6_8 = unpack("B", f.read(1))[0] / 127
                                        b1_aa6_8 = unpack("B", f.read(1))[0] / 127
                                        a1_aa6_8 = unpack("B", f.read(1))[0] / 127
                                        r1_aa7_8 = unpack("B", f.read(1))[0] / 127
                                        g1_aa7_8 = unpack("B", f.read(1))[0] / 127
                                        b1_aa7_8 = unpack("B", f.read(1))[0] / 127
                                        a1_aa7_8 = unpack("B", f.read(1))[0] / 127
                                        r1_aa8_8 = unpack("B", f.read(1))[0] / 127
                                        g1_aa8_8 = unpack("B", f.read(1))[0] / 127
                                        b1_aa8_8 = unpack("B", f.read(1))[0] / 127
                                        a1_aa8_8 = unpack("B", f.read(1))[0] / 127
                                        r1_aa9_8 = unpack("B", f.read(1))[0] / 127
                                        g1_aa9_8 = unpack("B", f.read(1))[0] / 127
                                        b1_aa9_8 = unpack("B", f.read(1))[0] / 127
                                        a1_aa9_8 = unpack("B", f.read(1))[0] / 127
                                        r1_aa10_8 = unpack("B", f.read(1))[0] / 127
                                        g1_aa10_8 = unpack("B", f.read(1))[0] / 127
                                        b1_aa10_8 = unpack("B", f.read(1))[0] / 127
                                        a1_aa10_8 = unpack("B", f.read(1))[0] / 127
                                    for i in range(10):
                                        f.seek(-4,1)
                                    for i in range(1):
                                        r1_aa1_8a = unpack("B", f.read(1))[0] / 127
                                        g1_aa1_8a = unpack("B", f.read(1))[0] / 127
                                        b1_aa1_8a = unpack("B", f.read(1))[0] / 127
                                        a1_aa1_8a = unpack("B", f.read(1))[0] / 127
                                        r1_aa2_8a = unpack("B", f.read(1))[0] / 127
                                        g1_aa2_8a = unpack("B", f.read(1))[0] / 127
                                        b1_aa2_8a = unpack("B", f.read(1))[0] / 127
                                        a1_aa2_8a = unpack("B", f.read(1))[0] / 127
                                        r1_aa3_8a = unpack("B", f.read(1))[0] / 127
                                        g1_aa3_8a = unpack("B", f.read(1))[0] / 127
                                        b1_aa3_8a = unpack("B", f.read(1))[0] / 127
                                        a1_aa3_8a = unpack("B", f.read(1))[0] / 127
                                        r1_aa4_8a = unpack("B", f.read(1))[0] / 127
                                        g1_aa4_8a = unpack("B", f.read(1))[0] / 127
                                        b1_aa4_8a = unpack("B", f.read(1))[0] / 127
                                        a1_aa4_8a = unpack("B", f.read(1))[0] / 127
                                        r1_aa5_8a = unpack("B", f.read(1))[0] / 127
                                        g1_aa5_8a = unpack("B", f.read(1))[0] / 127
                                        b1_aa5_8a = unpack("B", f.read(1))[0] / 127
                                        a1_aa5_8a = unpack("B", f.read(1))[0] / 127
                                        r1_aa6_8a = unpack("B", f.read(1))[0] / 127
                                        g1_aa6_8a = unpack("B", f.read(1))[0] / 127
                                        b1_aa6_8a = unpack("B", f.read(1))[0] / 127
                                        a1_aa6_8a = unpack("B", f.read(1))[0] / 127
                                        r1_aa7_8a = unpack("B", f.read(1))[0] / 127
                                        g1_aa7_8a = unpack("B", f.read(1))[0] / 127
                                        b1_aa7_8a = unpack("B", f.read(1))[0] / 127
                                        a1_aa7_8a = unpack("B", f.read(1))[0] / 127
                                        r1_aa8_8a = unpack("B", f.read(1))[0] / 127
                                        g1_aa8_8a = unpack("B", f.read(1))[0] / 127
                                        b1_aa8_8a = unpack("B", f.read(1))[0] / 127
                                        a1_aa8_8a = unpack("B", f.read(1))[0] / 127
                                        r1_aa9_8a = unpack("B", f.read(1))[0] / 127
                                        g1_aa9_8a = unpack("B", f.read(1))[0] / 127
                                        b1_aa9_8a = unpack("B", f.read(1))[0] / 127
                                        a1_aa9_8a = unpack("B", f.read(1))[0] / 127
                                        r1_aa10_8a = unpack("B", f.read(1))[0] / 127
                                        g1_aa10_8a = unpack("B", f.read(1))[0] / 127
                                        b1_aa10_8a = unpack("B", f.read(1))[0] / 127
                                        a1_aa10_8a = unpack("B", f.read(1))[0] / 127
                                    offset1ea_e____ = unpack("<I", f.read(4))[0]
                                    if offset1ea_e____ == 16777473:
                                        offset3fa_a____ = unpack("<I", f.read(4))[0]
                                        if offset3fa_a____ == 335545088:
                                            if type44a == 1:
                                                if type45a == 1:
                                                    if type46a == 0:
                                                        if type47a == 1:
                                                            if type48a == 1:
                                                                if type49a == 0:
                                                                    if type50a == 0:
                                                                        if type51a == 0:
                                                                            if type52a == 0:
                                                                                if type53a == 0:
                                                                                    verticesE2aaaaazz.append([vx44a,vz44a,vy44a])
                                                                                    verticesE2aaaaazz.append([vx45a,vz45a,vy45a])
                                                                                    verticesE2aaaaazz.append([vx46a,vz46a,vy46a])
                                                                                    verticesE2aaaaazz.append([vx47a,vz47a,vy47a])
                                                                                    verticesE2aaaaazz.append([vx48a,vz48a,vy48a])
                                                                                    verticesE2aaaaazz.append([vx49a,vz49a,vy49a])
                                                                                    verticesE2aaaaazz.append([vx50a,vz50a,vy50a])
                                                                                    verticesE2aaaaazz.append([vx51a,vz51a,vy51a])
                                                                                    verticesE2aaaaazz.append([vx52a,vz52a,vy52a])
                                                                                    verticesE2aaaaazz.append([vx53a,vz53a,vy53a])
                                                                                    fa_pamzz+=1*10#10
                                                                                    fb_pamzz+=1*10#9
                                                                                    fc_pamzz+=1*10#8
                                                                                    fa_qamzz+=1*10#7
                                                                                    fb_qamzz+=1*10#6
                                                                                    fc_qamzz+=1*10#5
                                                                                    fa_ramzz+=1*10#6
                                                                                    fb_ramzz+=1*10#5
                                                                                    fc_ramzz+=1*10#4
                                                                                    fa_samzz+=1*10#5
                                                                                    fb_samzz+=1*10#4
                                                                                    fc_samzz+=1*10#3
                                                                                    fa_tamzz+=1*10#4
                                                                                    fb_tamzz+=1*10#3
                                                                                    fc_tamzz+=1*10#2
                                                                                    fa_uamzz+=1*10#3
                                                                                    fb_uamzz+=1*10#2
                                                                                    fc_uamzz+=1*10#1
                                                                                    facesE2aaaaazz.append([fa_pamzz,fb_pamzz,fc_pamzz])
                                                                                    facesE2aaaaazz.append([fa_qamzz,fb_qamzz,fc_qamzz])
                                                                                    facesE2aaaaazz.append([fa_ramzz,fb_ramzz,fc_ramzz])
                                                                                    facesE2aaaaazz.append([fa_samzz,fb_samzz,fc_samzz])
                                                                                    facesE2aaaaazz.append([fa_tamzz,fb_tamzz,fc_tamzz])
                                                                                    facesE2aaaaazz.append([fa_uamzz,fb_uamzz,fc_uamzz])
                                                                                    uvsE2aaaaazz.append([uvx_aa1_8a,-uvy_aa1_8a])
                                                                                    uvsE2aaaaazz.append([uvx_aa2_8a,-uvy_aa2_8a])
                                                                                    uvsE2aaaaazz.append([uvx_aa3_8a,-uvy_aa3_8a])
                                                                                    uvsE2aaaaazz.append([uvx_aa4_8a,-uvy_aa4_8a])
                                                                                    uvsE2aaaaazz.append([uvx_aa5_8a,-uvy_aa5_8a])
                                                                                    uvsE2aaaaazz.append([uvx_aa6_8a,-uvy_aa6_8a])
                                                                                    uvsE2aaaaazz.append([uvx_aa7_8a,-uvy_aa7_8a])
                                                                                    uvsE2aaaaazz.append([uvx_aa8_8a,-uvy_aa8_8a])
                                                                                    uvsE2aaaaazz.append([uvx_aa9_8a,-uvy_aa9_8a])
                                                                                    uvsE2aaaaazz.append([uvx_aa10_8a,-uvy_aa10_8a])
                                                                                    vcolE2aaaaazz.append([r1_aa1_8a,g1_aa1_8a,b1_aa1_8a,a1_aa1_8a])
                                                                                    vcolE2aaaaazz.append([r1_aa2_8a,g1_aa2_8a,b1_aa2_8a,a1_aa2_8a])
                                                                                    vcolE2aaaaazz.append([r1_aa3_8a,g1_aa3_8a,b1_aa3_8a,a1_aa3_8a])
                                                                                    vcolE2aaaaazz.append([r1_aa4_8a,g1_aa4_8a,b1_aa4_8a,a1_aa4_8a])
                                                                                    vcolE2aaaaazz.append([r1_aa5_8a,g1_aa5_8a,b1_aa5_8a,a1_aa5_8a])
                                                                                    vcolE2aaaaazz.append([r1_aa6_8a,g1_aa6_8a,b1_aa6_8a,a1_aa6_8a])
                                                                                    vcolE2aaaaazz.append([r1_aa7_8a,g1_aa7_8a,b1_aa7_8a,a1_aa7_8a])
                                                                                    vcolE2aaaaazz.append([r1_aa8_8a,g1_aa8_8a,b1_aa8_8a,a1_aa8_8a])
                                                                                    vcolE2aaaaazz.append([r1_aa9_8a,g1_aa9_8a,b1_aa9_8a,a1_aa9_8a])
                                                                                    vcolE2aaaaazz.append([r1_aa10_8a,g1_aa10_8a,b1_aa10_8a,a1_aa10_8a])
                                            if type44 == 1:
                                                if type45 == 1:
                                                    if type46 == 0:
                                                        if type47 == 0:
                                                            if type48 == 0:
                                                                if type49 == 0:
                                                                    if type50 == 0:
                                                                        if type51 == 0:
                                                                            if type52 == 0:
                                                                                if type53 == 0:
                                                                                    verticesE2aaaaaz.append([vx44,vz44,vy44])
                                                                                    verticesE2aaaaaz.append([vx45,vz45,vy45])
                                                                                    verticesE2aaaaaz.append([vx46,vz46,vy46])
                                                                                    verticesE2aaaaaz.append([vx47,vz47,vy47])
                                                                                    verticesE2aaaaaz.append([vx48,vz48,vy48])
                                                                                    verticesE2aaaaaz.append([vx49,vz49,vy49])
                                                                                    verticesE2aaaaaz.append([vx50,vz50,vy50])
                                                                                    verticesE2aaaaaz.append([vx51,vz51,vy51])
                                                                                    verticesE2aaaaaz.append([vx52,vz52,vy52])
                                                                                    verticesE2aaaaaz.append([vx53,vz53,vy53])
                                                                                    fa_pamz+=1*10#10
                                                                                    fb_pamz+=1*10#9
                                                                                    fc_pamz+=1*10#8
                                                                                    fa_qamz+=1*10#9
                                                                                    fb_qamz+=1*10#8
                                                                                    fc_qamz+=1*10#7
                                                                                    fa_ramz+=1*10#8
                                                                                    fb_ramz+=1*10#7
                                                                                    fc_ramz+=1*10#6
                                                                                    fa_samz+=1*10#7
                                                                                    fb_samz+=1*10#6
                                                                                    fc_samz+=1*10#5
                                                                                    fa_tamz+=1*10#6
                                                                                    fb_tamz+=1*10#5
                                                                                    fc_tamz+=1*10#4
                                                                                    fa_uamz+=1*10#5
                                                                                    fb_uamz+=1*10#4
                                                                                    fc_uamz+=1*10#3
                                                                                    fa_vamz+=1*10#4
                                                                                    fb_vamz+=1*10#3
                                                                                    fc_vamz+=1*10#2
                                                                                    fa_wamz+=1*10#3
                                                                                    fb_wamz+=1*10#2
                                                                                    fc_wamz+=1*10#1
                                                                                    facesE2aaaaaz.append([fa_pamz,fb_pamz,fc_pamz])
                                                                                    facesE2aaaaaz.append([fa_qamz,fb_qamz,fc_qamz])
                                                                                    facesE2aaaaaz.append([fa_ramz,fb_ramz,fc_ramz])
                                                                                    facesE2aaaaaz.append([fa_samz,fb_samz,fc_samz])
                                                                                    facesE2aaaaaz.append([fa_tamz,fb_tamz,fc_tamz])
                                                                                    facesE2aaaaaz.append([fa_uamz,fb_uamz,fc_uamz])
                                                                                    facesE2aaaaaz.append([fa_vamz,fb_vamz,fc_vamz])
                                                                                    facesE2aaaaaz.append([fa_wamz,fb_wamz,fc_wamz])
                                                                                    uvsE2aaaaaz.append([uvx_aa1_8,-uvy_aa1_8])
                                                                                    uvsE2aaaaaz.append([uvx_aa2_8,-uvy_aa2_8])
                                                                                    uvsE2aaaaaz.append([uvx_aa3_8,-uvy_aa3_8])
                                                                                    uvsE2aaaaaz.append([uvx_aa4_8,-uvy_aa4_8])
                                                                                    uvsE2aaaaaz.append([uvx_aa5_8,-uvy_aa5_8])
                                                                                    uvsE2aaaaaz.append([uvx_aa6_8,-uvy_aa6_8])
                                                                                    uvsE2aaaaaz.append([uvx_aa7_8,-uvy_aa7_8])
                                                                                    uvsE2aaaaaz.append([uvx_aa8_8,-uvy_aa8_8])
                                                                                    uvsE2aaaaaz.append([uvx_aa9_8,-uvy_aa9_8])
                                                                                    uvsE2aaaaaz.append([uvx_aa10_8,-uvy_aa10_8])
                                                                                    vcolE2aaaaaz.append([r1_aa1_8,g1_aa1_8,b1_aa1_8,a1_aa1_8])
                                                                                    vcolE2aaaaaz.append([r1_aa2_8,g1_aa2_8,b1_aa2_8,a1_aa2_8])
                                                                                    vcolE2aaaaaz.append([r1_aa3_8,g1_aa3_8,b1_aa3_8,a1_aa3_8])
                                                                                    vcolE2aaaaaz.append([r1_aa4_8,g1_aa4_8,b1_aa4_8,a1_aa4_8])
                                                                                    vcolE2aaaaaz.append([r1_aa5_8,g1_aa5_8,b1_aa5_8,a1_aa5_8])
                                                                                    vcolE2aaaaaz.append([r1_aa6_8,g1_aa6_8,b1_aa6_8,a1_aa6_8])
                                                                                    vcolE2aaaaaz.append([r1_aa7_8,g1_aa7_8,b1_aa7_8,a1_aa7_8])
                                                                                    vcolE2aaaaaz.append([r1_aa8_8,g1_aa8_8,b1_aa8_8,a1_aa8_8])
                                                                                    vcolE2aaaaaz.append([r1_aa9_8,g1_aa9_8,b1_aa9_8,a1_aa9_8])
                                                                                    vcolE2aaaaaz.append([r1_aa10_8,g1_aa10_8,b1_aa10_8,a1_aa10_8])
                                        
                                                                            

    collection = bpy.data.collections.new(os.path.basename(os.path.splitext(filepath)[0]))
    bpy.context.scene.collection.children.link(collection)

    mes15_ = bpy.data.meshes.new(os.path.basename(os.path.splitext(filepath)[0]))
    mes15_.from_pydata(verticesE2aaaaazz, [], facesE2aaaaazz)
    #mes4_.normals_split_custom_set_from_vertices(normalsE2a)
    obj15_ = bpy.data.objects.new(os.path.basename(os.path.splitext(filepath)[0]), mes15_)
    collection.objects.link(obj15_)

    _0_uv_texE2aaaaazz = mes15_.uv_layers.new()
    _0_uv_layerE2aaaaazz = mes15_.uv_layers[0].data
    _0_vert_loopsE2aaaaazz = {}
    for l in mes15_.loops:
        _0_vert_loopsE2aaaaazz.setdefault(l.vertex_index, []).append(l.index)
    for i, coord in enumerate(uvsE2aaaaazz):
        for li in _0_vert_loopsE2aaaaazz[i]:
            _0_uv_layerE2aaaaazz[li].uv = coord

    bpy.context.view_layer.objects.active = obj15_
