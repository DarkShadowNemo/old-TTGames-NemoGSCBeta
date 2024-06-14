from struct import pack, unpack
import os
import bpy
import bmesh
import math
from io import BytesIO as bio

from .importGSCLib.nu_gsc_props.spline.splineset import *
from .importGSCLib.nu_gsc_props.instance.inst_primary import *
from .importGSCLib.nu_gsc_props.instance.inst_secondary import *
from .importGSCLib.nu_gsc_props.bounding.boundingset import *
from .importGSCLib.nu_gsc_props.animationL.AnimationLibrary import *
#from .importGSCLib.nu_combination_mesh.combinations.primary import *
    

def truncate_cstr(s: bytes) -> bytes:
    index = s.find(0)
    if index == -1: return s
    return s[:index]
def fetch_cstr(f: 'filelike') -> bytearray:
    build = bytearray()
    while 1:
        strbyte = f.read(1)
        if strbyte == b'\0' or not strbyte: break
        build += strbyte
    return build

def gsc_texture_utility(f, filepath):
    pass
            

def wholeChunk1_none(f, filepath):
    vertices=[]
    normals=[]
    uvs=[]
    vcolors=[]
    faces=[]
    values=[]
    f.seek(0)
    fa = -1
    fb = 0
    fc = 1
    while 1:
        Chunk = f.read(4)
        if Chunk == b"\x03\x01\x00\x01":
            unknown__ = unpack("B", f.read(1))[0]
            value1 = unpack("B", f.read(1))[0]
            vertexCount = unpack("B", f.read(1))[0]
            flag2 = unpack("B", f.read(1))[0]
            if flag2 == 0x6C:
                if vertexCount == 3:
                    
                    for j in range(vertexCount):
                        vx = unpack("<f", f.read(4))[0]
                        vy = unpack("<f", f.read(4))[0]
                        vz = unpack("<f", f.read(4))[0]
                        type4 = unpack("B", f.read(1))[0]==False
                        value1a = unpack("B", f.read(1))[0]
                        normalZ_ = unpack("<h", f.read(2))[0]
                        
                        nz1 = vz
                        ny1 = vy
                        nx1 = vx
                        nzz1 = normalZ_
                        nyy1 = normalZ_
                        nxx1 = normalZ_
                        nz1*=normalZ_
                        ny1*=normalZ_
                        nx1*=normalZ_
                        normalx = pack("<d", nx1)[0]
                        normaly = pack("<d", ny1)[0]
                        normalz = pack("<d", nz1)[0]
                        normals.append([nx1,ny1,nz1])
                        fa+=1
                        fb+=1
                        fc+=1

                        if type4 > 0:
                            faces.append([j+j+type4-type4-1+fa-j-j-1,j-j+type4-type4+1+fb-2-1,j+type4-type4+fc-j+2-4])

                    for i in range(vertexCount):
                        f.seek(-16,1)

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
                        f.seek(-48,1)
                        vx1_i = unpack("<i", f.read(4))[0]
                        vy1_i = unpack("<i", f.read(4))[0]
                        vz1_i = unpack("<i", f.read(4))[0]
                        f.seek(4,1)
                        vx2_i = unpack("<i", f.read(4))[0]
                        vy2_i = unpack("<i", f.read(4))[0]
                        vz2_i = unpack("<i", f.read(4))[0]
                        f.seek(4,1)
                        vx3_i = unpack("<i", f.read(4))[0]
                        vy3_i = unpack("<i", f.read(4))[0]
                        vz3_i = unpack("<i", f.read(4))[0]
                        f.seek(4,1)
                        vertices.append([vx1,vz1,vy1])
                        vertices.append([vx2,vz2,vy2])
                        vertices.append([vx3,vz3,vy3])
                        if vx1_i == -1056788129:
                            if vy1_i == 1087593491:
                                if vz1_i == -1035103740:
                                    if type1 == 13:
                                        if value1a1 == 220:
                                            if normalZ_1 == -16102:
                                                if vx2_i == -1075838976:
                                                    if vy2_i == -1034874321:
                                                        if vz2_i == 1081764739:
                                                            if type2 == 19:
                                                                if value1a2 == 92:
                                                                    if normalZ_2 == 16595:
                                                                        if vx3_i == -1037697023:
                                                                            if vy3_i == 0:
                                                                                if vz3_i == 0:
                                                                                    if type3 == 1:
                                                                                        if value1a3 == 0:
                                                                                            if normalZ_3 == 0:
                                                                                                pass
                                                            

                elif vertexCount == 4:
                    
                    for j in range(vertexCount):
                        vx = unpack("<f", f.read(4))[0]
                        vy = unpack("<f", f.read(4))[0]
                        vz = unpack("<f", f.read(4))[0]
                        type4 = unpack("B", f.read(1))[0]==False
                        value1a = unpack("B", f.read(1))[0]
                        normalZ_ = unpack("<h", f.read(2))[0]
                        
                        nz1 = vz
                        ny1 = vy
                        nx1 = vx
                        nzz1 = normalZ_
                        nyy1 = normalZ_
                        nxx1 = normalZ_
                        nz1*=normalZ_
                        ny1*=normalZ_
                        nx1*=normalZ_
                        normalx = pack("<d", nx1)[0]
                        normaly = pack("<d", ny1)[0]
                        normalz = pack("<d", nz1)[0]
                        normals.append([nx1,ny1,nz1])
                        fa+=1
                        fb+=1
                        fc+=1

                        if type4 > 0:
                            faces.append([j+j+type4-type4-1+fa-j-j-1,j-j+type4-type4+1+fb-2-1,j+type4-type4+fc-j+2-4])

                    for i in range(vertexCount):
                        f.seek(-16,1)

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
                        vertices.append([vx5,vz5,vy5])
                        vertices.append([vx6,vz6,vy6])
                        vertices.append([vx7,vz7,vy7])
                        vertices.append([vx8,vz8,vy8])
                            

                elif vertexCount == 5:
                    for j in range(vertexCount):
                        vx = unpack("<f", f.read(4))[0]
                        vy = unpack("<f", f.read(4))[0]
                        vz = unpack("<f", f.read(4))[0]
                        type4 = unpack("B", f.read(1))[0]==False
                        value1a = unpack("B", f.read(1))[0]
                        normalZ_ = unpack("<h", f.read(2))[0]
                        
                        nz1 = vz
                        ny1 = vy
                        nx1 = vx
                        nzz1 = normalZ_
                        nyy1 = normalZ_
                        nxx1 = normalZ_
                        nz1*=normalZ_
                        ny1*=normalZ_
                        nx1*=normalZ_
                        normalx = pack("<d", nx1)[0]
                        normaly = pack("<d", ny1)[0]
                        normalz = pack("<d", nz1)[0]
                        normals.append([nx1,ny1,nz1])
                        fa+=1
                        fb+=1
                        fc+=1

                        if type4 > 0:
                            faces.append([j+j+type4-type4-1+fa-j-j-1,j-j+type4-type4+1+fb-2-1,j+type4-type4+fc-j+2-4])

                    for i in range(vertexCount):
                        f.seek(-16,1)

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
                        f.seek(-80,1)
                        vx9_i = unpack("<i", f.read(4))[0]
                        vy9_i = unpack("<i", f.read(4))[0]
                        vz9_i = unpack("<i", f.read(4))[0]
                        f.seek(4,1)
                        vx10_i = unpack("<i", f.read(4))[0]
                        vy10_i = unpack("<i", f.read(4))[0]
                        vz10_i = unpack("<i", f.read(4))[0]
                        f.seek(4,1)
                        vx11_i = unpack("<i", f.read(4))[0]
                        vy11_i = unpack("<i", f.read(4))[0]
                        vz11_i = unpack("<i", f.read(4))[0]
                        f.seek(4,1)
                        vx12_i = unpack("<i", f.read(4))[0]
                        vy12_i = unpack("<i", f.read(4))[0]
                        vz12_i = unpack("<i", f.read(4))[0]
                        f.seek(4,1)
                        vx13_i = unpack("<i", f.read(4))[0]
                        vy13_i = unpack("<i", f.read(4))[0]
                        vz13_i = unpack("<i", f.read(4))[0]
                        f.seek(4,1)
                        vertices.append([vx9,vz9,vy9])
                        vertices.append([vx10,vz10,vy10])
                        vertices.append([vx11,vz11,vy11])
                        vertices.append([vx12,vz12,vy12])
                        vertices.append([vx13,vz13,vy13])
                        if vx9_i == 1077176076:
                            if vy9_i == -1099094344:
                                if vz9_i == 1081601667:
                                    if type9 == 250:
                                        if value1a9 == 211:
                                            if normalZ_9 == -16347:
                                                if vx10_i == -1063365019:
                                                    if vy10_i == 1096127352:
                                                        if vz10_i == 1092572228:
                                                            if type10 == 101:
                                                                if value1a10 == 86:
                                                                    if normalZ_10 == 16542:
                                                                        if vx11_i == 0:
                                                                            if vy11_i == 0:
                                                                                if vz11_i == 1:
                                                                                    if type11 == 0:
                                                                                        if value1a11 == 0:
                                                                                            if normalZ_11 == 0:
                                                                                                if vx12_i == 0:
                                                                                                    if vy12_i == 0:
                                                                                                        if vz12_i == 0:
                                                                                                            if type12 == 1:
                                                                                                                if value1a12 == 0:
                                                                                                                    if normalZ_12 == 0:
                                                                                                                        if vx13_i == 0:
                                                                                                                            if vy13_i == 0:
                                                                                                                                if vz13_i == 0:
                                                                                                                                    if type13 == 66:
                                                                                                                                        if value1a13 == 0:
                                                                                                                                            if normalZ_13 == 0:
                                                                                                                                                #faces.remove([62,63,64])
                                                                                                                                                #faces.remove([104, 105, 106])
                                                                                                                                                pass

                elif vertexCount == 6:
                    for j in range(vertexCount):
                        vx = unpack("<f", f.read(4))[0]
                        vy = unpack("<f", f.read(4))[0]
                        vz = unpack("<f", f.read(4))[0]
                        type4 = unpack("B", f.read(1))[0]==False
                        value1a = unpack("B", f.read(1))[0]
                        normalZ_ = unpack("<h", f.read(2))[0]
                        
                        nz1 = vz
                        ny1 = vy
                        nx1 = vx
                        nzz1 = normalZ_
                        nyy1 = normalZ_
                        nxx1 = normalZ_
                        nz1*=normalZ_
                        ny1*=normalZ_
                        nx1*=normalZ_
                        normalx = pack("<d", nx1)[0]
                        normaly = pack("<d", ny1)[0]
                        normalz = pack("<d", nz1)[0]
                        normals.append([nx1,ny1,nz1])
                        fa+=1
                        fb+=1
                        fc+=1

                        if type4 > 0:
                            faces.append([j+j+type4-type4-1+fa-j-j-1,j-j+type4-type4+1+fb-2-1,j+type4-type4+fc-j+2-4])

                    for i in range(vertexCount):
                        f.seek(-16,1)

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
                        vertices.append([vx14,vz14,vy14])
                        vertices.append([vx15,vz15,vy15])
                        vertices.append([vx16,vz16,vy16])
                        vertices.append([vx17,vz17,vy17])
                        vertices.append([vx18,vz18,vy18])
                        vertices.append([vx19,vz19,vy19])

                elif vertexCount == 7:
                    for j in range(vertexCount):
                        vx = unpack("<f", f.read(4))[0]
                        vy = unpack("<f", f.read(4))[0]
                        vz = unpack("<f", f.read(4))[0]
                        type4 = unpack("B", f.read(1))[0]==False
                        value1a = unpack("B", f.read(1))[0]
                        normalZ_ = unpack("<h", f.read(2))[0]
                        
                        nz1 = vz
                        ny1 = vy
                        nx1 = vx
                        nzz1 = normalZ_
                        nyy1 = normalZ_
                        nxx1 = normalZ_
                        nz1*=normalZ_
                        ny1*=normalZ_
                        nx1*=normalZ_
                        normalx = pack("<d", nx1)[0]
                        normaly = pack("<d", ny1)[0]
                        normalz = pack("<d", nz1)[0]
                        normals.append([nx1,ny1,nz1])
                        fa+=1
                        fb+=1
                        fc+=1

                        if type4 > 0:
                            faces.append([j+j+type4-type4-1+fa-j-j-1,j-j+type4-type4+1+fb-2-1,j+type4-type4+fc-j+2-4])

                    for i in range(vertexCount):
                        f.seek(-16,1)

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
                        vertices.append([vx20,vz20,vy20])
                        vertices.append([vx21,vz21,vy21])
                        vertices.append([vx22,vz22,vy22])
                        vertices.append([vx23,vz23,vy23])
                        vertices.append([vx24,vz24,vy24])
                        vertices.append([vx25,vz25,vy25])
                        vertices.append([vx26,vz26,vy26])

                elif vertexCount == 8:
                    for j in range(vertexCount):
                        vx = unpack("<f", f.read(4))[0]
                        vy = unpack("<f", f.read(4))[0]
                        vz = unpack("<f", f.read(4))[0]
                        type4 = unpack("B", f.read(1))[0]==False
                        value1a = unpack("B", f.read(1))[0]
                        normalZ_ = unpack("<h", f.read(2))[0]
                        
                        nz1 = vz
                        ny1 = vy
                        nx1 = vx
                        nzz1 = normalZ_
                        nyy1 = normalZ_
                        nxx1 = normalZ_
                        nz1*=normalZ_
                        ny1*=normalZ_
                        nx1*=normalZ_
                        normalx = pack("<d", nx1)[0]
                        normaly = pack("<d", ny1)[0]
                        normalz = pack("<d", nz1)[0]
                        normals.append([nx1,ny1,nz1])
                        fa+=1
                        fb+=1
                        fc+=1

                        if type4 > 0:
                            faces.append([j+j+type4-type4-1+fa-j-j-1,j-j+type4-type4+1+fb-2-1,j+type4-type4+fc-j+2-4])

                    for i in range(vertexCount):
                        f.seek(-16,1)

                    for i in range(1):
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
                        vertices.append([vx27,vz27,vy27])
                        vertices.append([vx28,vz28,vy28])
                        vertices.append([vx29,vz29,vy29])
                        vertices.append([vx30,vz30,vy30])
                        vertices.append([vx31,vz31,vy31])
                        vertices.append([vx32,vz32,vy32])
                        vertices.append([vx33,vz33,vy33])
                        vertices.append([vx34,vz34,vy34])

                elif vertexCount == 9:
                    for j in range(vertexCount):
                        vx = unpack("<f", f.read(4))[0]
                        vy = unpack("<f", f.read(4))[0]
                        vz = unpack("<f", f.read(4))[0]
                        type4 = unpack("B", f.read(1))[0]==False
                        value1a = unpack("B", f.read(1))[0]
                        normalZ_ = unpack("<h", f.read(2))[0]
                        
                        nz1 = vz
                        ny1 = vy
                        nx1 = vx
                        nzz1 = normalZ_
                        nyy1 = normalZ_
                        nxx1 = normalZ_
                        nz1*=normalZ_
                        ny1*=normalZ_
                        nx1*=normalZ_
                        normalx = pack("<d", nx1)[0]
                        normaly = pack("<d", ny1)[0]
                        normalz = pack("<d", nz1)[0]
                        normals.append([nx1,ny1,nz1])
                        fa+=1
                        fb+=1
                        fc+=1

                        if type4 > 0:
                            faces.append([j+j+type4-type4-1+fa-j-j-1,j-j+type4-type4+1+fb-2-1,j+type4-type4+fc-j+2-4])

                    for i in range(vertexCount):
                        f.seek(-16,1)

                    for i in range(1):
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
                        vertices.append([vx35,vz35,vy35])
                        vertices.append([vx36,vz36,vy36])
                        vertices.append([vx37,vz37,vy37])
                        vertices.append([vx38,vz38,vy38])
                        vertices.append([vx39,vz39,vy39])
                        vertices.append([vx40,vz40,vy40])
                        vertices.append([vx41,vz41,vy41])
                        vertices.append([vx42,vz42,vy42])
                        vertices.append([vx43,vz43,vy43])

                elif vertexCount == 10:
                    for j in range(vertexCount):
                        vx = unpack("<f", f.read(4))[0]
                        vy = unpack("<f", f.read(4))[0]
                        vz = unpack("<f", f.read(4))[0]
                        type4 = unpack("B", f.read(1))[0]==False
                        value1a = unpack("B", f.read(1))[0]
                        normalZ_ = unpack("<h", f.read(2))[0]
                        
                        nz1 = vz
                        ny1 = vy
                        nx1 = vx
                        nzz1 = normalZ_
                        nyy1 = normalZ_
                        nxx1 = normalZ_
                        nz1*=normalZ_
                        ny1*=normalZ_
                        nx1*=normalZ_
                        normalx = pack("<d", nx1)[0]
                        normaly = pack("<d", ny1)[0]
                        normalz = pack("<d", nz1)[0]
                        normals.append([nx1,ny1,nz1])
                        fa+=1
                        fb+=1
                        fc+=1

                        if type4 > 0:
                            faces.append([j+j+type4-type4-1+fa-j-j-1,j-j+type4-type4+1+fb-2-1,j+type4-type4+fc-j+2-4])

                    for i in range(vertexCount):
                        f.seek(-16,1)

                    for i in range(1):
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
                        vertices.append([vx44,vz44,vy44])
                        vertices.append([vx45,vz45,vy45])
                        vertices.append([vx46,vz46,vy46])
                        vertices.append([vx47,vz47,vy47])
                        vertices.append([vx48,vz48,vy48])
                        vertices.append([vx49,vz49,vy49])
                        vertices.append([vx50,vz50,vy50])
                        vertices.append([vx51,vz51,vy51])
                        vertices.append([vx52,vz52,vy52])
                        vertices.append([vx53,vz53,vy53])

                elif vertexCount == 11:
                    for j in range(vertexCount):
                        vx = unpack("<f", f.read(4))[0]
                        vy = unpack("<f", f.read(4))[0]
                        vz = unpack("<f", f.read(4))[0]
                        type4 = unpack("B", f.read(1))[0]==False
                        value1a = unpack("B", f.read(1))[0]
                        normalZ_ = unpack("<h", f.read(2))[0]
                        
                        nz1 = vz
                        ny1 = vy
                        nx1 = vx
                        nzz1 = normalZ_
                        nyy1 = normalZ_
                        nxx1 = normalZ_
                        nz1*=normalZ_
                        ny1*=normalZ_
                        nx1*=normalZ_
                        normalx = pack("<d", nx1)[0]
                        normaly = pack("<d", ny1)[0]
                        normalz = pack("<d", nz1)[0]
                        normals.append([nx1,ny1,nz1])
                        fa+=1
                        fb+=1
                        fc+=1

                        if type4 > 0:
                            faces.append([j+j+type4-type4-1+fa-j-j-1,j-j+type4-type4+1+fb-2-1,j+type4-type4+fc-j+2-4])

                    for i in range(vertexCount):
                        f.seek(-16,1)

                    for i in range(1):
                        vx54 = unpack("<f", f.read(4))[0]
                        vy54 = unpack("<f", f.read(4))[0]
                        vz54 = unpack("<f", f.read(4))[0]
                        type54 = unpack("B", f.read(1))[0]
                        value1a54 = unpack("B", f.read(1))[0]
                        normalZ_54 = unpack("<h", f.read(2))[0]
                        vx55 = unpack("<f", f.read(4))[0]
                        vy55 = unpack("<f", f.read(4))[0]
                        vz55 = unpack("<f", f.read(4))[0]
                        type55 = unpack("B", f.read(1))[0]
                        value1a55 = unpack("B", f.read(1))[0]
                        normalZ_55 = unpack("<h", f.read(2))[0]
                        vx56 = unpack("<f", f.read(4))[0]
                        vy56 = unpack("<f", f.read(4))[0]
                        vz56 = unpack("<f", f.read(4))[0]
                        type56 = unpack("B", f.read(1))[0]
                        value1a56 = unpack("B", f.read(1))[0]
                        normalZ_56 = unpack("<h", f.read(2))[0]
                        vx57 = unpack("<f", f.read(4))[0]
                        vy57 = unpack("<f", f.read(4))[0]
                        vz57 = unpack("<f", f.read(4))[0]
                        type57 = unpack("B", f.read(1))[0]
                        value1a57 = unpack("B", f.read(1))[0]
                        normalZ_57 = unpack("<h", f.read(2))[0]
                        vx58 = unpack("<f", f.read(4))[0]
                        vy58 = unpack("<f", f.read(4))[0]
                        vz58 = unpack("<f", f.read(4))[0]
                        type58 = unpack("B", f.read(1))[0]
                        value1a58 = unpack("B", f.read(1))[0]
                        normalZ_58 = unpack("<h", f.read(2))[0]
                        vx59 = unpack("<f", f.read(4))[0]
                        vy59 = unpack("<f", f.read(4))[0]
                        vz59 = unpack("<f", f.read(4))[0]
                        type59 = unpack("B", f.read(1))[0]
                        value1a59 = unpack("B", f.read(1))[0]
                        normalZ_59 = unpack("<h", f.read(2))[0]
                        vx60 = unpack("<f", f.read(4))[0]
                        vy60 = unpack("<f", f.read(4))[0]
                        vz60 = unpack("<f", f.read(4))[0]
                        type60 = unpack("B", f.read(1))[0]
                        value1a60 = unpack("B", f.read(1))[0]
                        normalZ_60 = unpack("<h", f.read(2))[0]
                        vx61 = unpack("<f", f.read(4))[0]
                        vy61 = unpack("<f", f.read(4))[0]
                        vz61 = unpack("<f", f.read(4))[0]
                        type61 = unpack("B", f.read(1))[0]
                        value1a61 = unpack("B", f.read(1))[0]
                        normalZ_61 = unpack("<h", f.read(2))[0]
                        vx62 = unpack("<f", f.read(4))[0]
                        vy62 = unpack("<f", f.read(4))[0]
                        vz62 = unpack("<f", f.read(4))[0]
                        type62 = unpack("B", f.read(1))[0]
                        value1a62 = unpack("B", f.read(1))[0]
                        normalZ_62 = unpack("<h", f.read(2))[0]
                        vx63 = unpack("<f", f.read(4))[0]
                        vy63 = unpack("<f", f.read(4))[0]
                        vz63 = unpack("<f", f.read(4))[0]
                        type63 = unpack("B", f.read(1))[0]
                        value1a63 = unpack("B", f.read(1))[0]
                        normalZ_63 = unpack("<h", f.read(2))[0]
                        vx64 = unpack("<f", f.read(4))[0]
                        vy64 = unpack("<f", f.read(4))[0]
                        vz64 = unpack("<f", f.read(4))[0]
                        type64 = unpack("B", f.read(1))[0]
                        value1a64 = unpack("B", f.read(1))[0]
                        normalZ_64 = unpack("<h", f.read(2))[0]
                        vertices.append([vx54,vz54,vy54])
                        vertices.append([vx55,vz55,vy55])
                        vertices.append([vx56,vz56,vy56])
                        vertices.append([vx57,vz57,vy57])
                        vertices.append([vx58,vz58,vy58])
                        vertices.append([vx59,vz59,vy59])
                        vertices.append([vx60,vz60,vy60])
                        vertices.append([vx61,vz61,vy61])
                        vertices.append([vx62,vz62,vy62])
                        vertices.append([vx63,vz63,vy63])
                        vertices.append([vx64,vz64,vy64])

                elif vertexCount == 12:
                    for j in range(vertexCount):
                        vx = unpack("<f", f.read(4))[0]
                        vy = unpack("<f", f.read(4))[0]
                        vz = unpack("<f", f.read(4))[0]
                        type4 = unpack("B", f.read(1))[0]==False
                        value1a = unpack("B", f.read(1))[0]
                        normalZ_ = unpack("<h", f.read(2))[0]
                        
                        nz1 = vz
                        ny1 = vy
                        nx1 = vx
                        nzz1 = normalZ_
                        nyy1 = normalZ_
                        nxx1 = normalZ_
                        nz1*=normalZ_
                        ny1*=normalZ_
                        nx1*=normalZ_
                        normalx = pack("<d", nx1)[0]
                        normaly = pack("<d", ny1)[0]
                        normalz = pack("<d", nz1)[0]
                        normals.append([nx1,ny1,nz1])
                        fa+=1
                        fb+=1
                        fc+=1

                        if type4 > 0:
                            faces.append([j+j+type4-type4-1+fa-j-j-1,j-j+type4-type4+1+fb-2-1,j+type4-type4+fc-j+2-4])

                    for i in range(vertexCount):
                        f.seek(-16,1)

                    for i in range(1):
                        vx65 = unpack("<f", f.read(4))[0]
                        vy65 = unpack("<f", f.read(4))[0]
                        vz65 = unpack("<f", f.read(4))[0]
                        type65 = unpack("B", f.read(1))[0]
                        value1a65 = unpack("B", f.read(1))[0]
                        normalZ_65 = unpack("<h", f.read(2))[0]
                        vx66 = unpack("<f", f.read(4))[0]
                        vy66 = unpack("<f", f.read(4))[0]
                        vz66 = unpack("<f", f.read(4))[0]
                        type66 = unpack("B", f.read(1))[0]
                        value1a66 = unpack("B", f.read(1))[0]
                        normalZ_66 = unpack("<h", f.read(2))[0]
                        vx67 = unpack("<f", f.read(4))[0]
                        vy67 = unpack("<f", f.read(4))[0]
                        vz67 = unpack("<f", f.read(4))[0]
                        type67 = unpack("B", f.read(1))[0]
                        value1a67 = unpack("B", f.read(1))[0]
                        normalZ_67 = unpack("<h", f.read(2))[0]
                        vx68 = unpack("<f", f.read(4))[0]
                        vy68 = unpack("<f", f.read(4))[0]
                        vz68 = unpack("<f", f.read(4))[0]
                        type68 = unpack("B", f.read(1))[0]
                        value1a68 = unpack("B", f.read(1))[0]
                        normalZ_68 = unpack("<h", f.read(2))[0]
                        vx69 = unpack("<f", f.read(4))[0]
                        vy69 = unpack("<f", f.read(4))[0]
                        vz69 = unpack("<f", f.read(4))[0]
                        type69 = unpack("B", f.read(1))[0]
                        value1a69 = unpack("B", f.read(1))[0]
                        normalZ_69 = unpack("<h", f.read(2))[0]
                        vx70 = unpack("<f", f.read(4))[0]
                        vy70 = unpack("<f", f.read(4))[0]
                        vz70 = unpack("<f", f.read(4))[0]
                        type70 = unpack("B", f.read(1))[0]
                        value1a70 = unpack("B", f.read(1))[0]
                        normalZ_70 = unpack("<h", f.read(2))[0]
                        vx71 = unpack("<f", f.read(4))[0]
                        vy71 = unpack("<f", f.read(4))[0]
                        vz71 = unpack("<f", f.read(4))[0]
                        type71 = unpack("B", f.read(1))[0]
                        value1a71 = unpack("B", f.read(1))[0]
                        normalZ_71 = unpack("<h", f.read(2))[0]
                        vx72 = unpack("<f", f.read(4))[0]
                        vy72 = unpack("<f", f.read(4))[0]
                        vz72 = unpack("<f", f.read(4))[0]
                        type72 = unpack("B", f.read(1))[0]
                        value1a72 = unpack("B", f.read(1))[0]
                        normalZ_72 = unpack("<h", f.read(2))[0]
                        vx73 = unpack("<f", f.read(4))[0]
                        vy73 = unpack("<f", f.read(4))[0]
                        vz73 = unpack("<f", f.read(4))[0]
                        type73 = unpack("B", f.read(1))[0]
                        value1a73 = unpack("B", f.read(1))[0]
                        normalZ_73 = unpack("<h", f.read(2))[0]
                        vx74 = unpack("<f", f.read(4))[0]
                        vy74 = unpack("<f", f.read(4))[0]
                        vz74 = unpack("<f", f.read(4))[0]
                        type74 = unpack("B", f.read(1))[0]
                        value1a74 = unpack("B", f.read(1))[0]
                        normalZ_74 = unpack("<h", f.read(2))[0]
                        vx75 = unpack("<f", f.read(4))[0]
                        vy75 = unpack("<f", f.read(4))[0]
                        vz75 = unpack("<f", f.read(4))[0]
                        type75 = unpack("B", f.read(1))[0]
                        value1a75 = unpack("B", f.read(1))[0]
                        normalZ_75 = unpack("<h", f.read(2))[0]
                        vx76 = unpack("<f", f.read(4))[0]
                        vy76 = unpack("<f", f.read(4))[0]
                        vz76 = unpack("<f", f.read(4))[0]
                        type76 = unpack("B", f.read(1))[0]
                        value1a76 = unpack("B", f.read(1))[0]
                        normalZ_76 = unpack("<h", f.read(2))[0]
                        vertices.append([vx65,vz65,vy65])
                        vertices.append([vx66,vz66,vy66])
                        vertices.append([vx67,vz67,vy67])
                        vertices.append([vx68,vz68,vy68])
                        vertices.append([vx69,vz69,vy69])
                        vertices.append([vx70,vz70,vy70])
                        vertices.append([vx71,vz71,vy71])
                        vertices.append([vx72,vz72,vy72])
                        vertices.append([vx73,vz73,vy73])
                        vertices.append([vx74,vz74,vy74])
                        vertices.append([vx75,vz75,vy75])
                        vertices.append([vx76,vz76,vy76])

                elif vertexCount == 13:
                    for j in range(vertexCount):
                        vx = unpack("<f", f.read(4))[0]
                        vy = unpack("<f", f.read(4))[0]
                        vz = unpack("<f", f.read(4))[0]
                        type4 = unpack("B", f.read(1))[0]==False
                        value1a = unpack("B", f.read(1))[0]
                        normalZ_ = unpack("<h", f.read(2))[0]
                        
                        nz1 = vz
                        ny1 = vy
                        nx1 = vx
                        nzz1 = normalZ_
                        nyy1 = normalZ_
                        nxx1 = normalZ_
                        nz1*=normalZ_
                        ny1*=normalZ_
                        nx1*=normalZ_
                        normalx = pack("<d", nx1)[0]
                        normaly = pack("<d", ny1)[0]
                        normalz = pack("<d", nz1)[0]
                        normals.append([nx1,ny1,nz1])
                        fa+=1
                        fb+=1
                        fc+=1

                        if type4 > 0:
                            faces.append([j+j+type4-type4-1+fa-j-j-1,j-j+type4-type4+1+fb-2-1,j+type4-type4+fc-j+2-4])

                    for i in range(vertexCount):
                        f.seek(-16,1)

                    for i in range(1):
                        vx77 = unpack("<f", f.read(4))[0]
                        vy77 = unpack("<f", f.read(4))[0]
                        vz77 = unpack("<f", f.read(4))[0]
                        type77 = unpack("B", f.read(1))[0]
                        value1a77 = unpack("B", f.read(1))[0]
                        normalZ_77 = unpack("<h", f.read(2))[0]
                        vx78 = unpack("<f", f.read(4))[0]
                        vy78 = unpack("<f", f.read(4))[0]
                        vz78 = unpack("<f", f.read(4))[0]
                        type78 = unpack("B", f.read(1))[0]
                        value1a78 = unpack("B", f.read(1))[0]
                        normalZ_78 = unpack("<h", f.read(2))[0]
                        vx79 = unpack("<f", f.read(4))[0]
                        vy79 = unpack("<f", f.read(4))[0]
                        vz79 = unpack("<f", f.read(4))[0]
                        type79 = unpack("B", f.read(1))[0]
                        value1a79 = unpack("B", f.read(1))[0]
                        normalZ_79 = unpack("<h", f.read(2))[0]
                        vx80 = unpack("<f", f.read(4))[0]
                        vy80 = unpack("<f", f.read(4))[0]
                        vz80 = unpack("<f", f.read(4))[0]
                        type80 = unpack("B", f.read(1))[0]
                        value1a80 = unpack("B", f.read(1))[0]
                        normalZ_80 = unpack("<h", f.read(2))[0]
                        vx81 = unpack("<f", f.read(4))[0]
                        vy81 = unpack("<f", f.read(4))[0]
                        vz81 = unpack("<f", f.read(4))[0]
                        type81 = unpack("B", f.read(1))[0]
                        value1a81 = unpack("B", f.read(1))[0]
                        normalZ_81 = unpack("<h", f.read(2))[0]
                        vx82 = unpack("<f", f.read(4))[0]
                        vy82 = unpack("<f", f.read(4))[0]
                        vz82 = unpack("<f", f.read(4))[0]
                        type82 = unpack("B", f.read(1))[0]
                        value1a82 = unpack("B", f.read(1))[0]
                        normalZ_82 = unpack("<h", f.read(2))[0]
                        vx83 = unpack("<f", f.read(4))[0]
                        vy83 = unpack("<f", f.read(4))[0]
                        vz83 = unpack("<f", f.read(4))[0]
                        type83 = unpack("B", f.read(1))[0]
                        value1a83 = unpack("B", f.read(1))[0]
                        normalZ_83 = unpack("<h", f.read(2))[0]
                        vx84 = unpack("<f", f.read(4))[0]
                        vy84 = unpack("<f", f.read(4))[0]
                        vz84 = unpack("<f", f.read(4))[0]
                        type84 = unpack("B", f.read(1))[0]
                        value1a84 = unpack("B", f.read(1))[0]
                        normalZ_84 = unpack("<h", f.read(2))[0]
                        vx85 = unpack("<f", f.read(4))[0]
                        vy85 = unpack("<f", f.read(4))[0]
                        vz85 = unpack("<f", f.read(4))[0]
                        type85 = unpack("B", f.read(1))[0]
                        value1a85 = unpack("B", f.read(1))[0]
                        normalZ_85 = unpack("<h", f.read(2))[0]
                        vx86 = unpack("<f", f.read(4))[0]
                        vy86 = unpack("<f", f.read(4))[0]
                        vz86 = unpack("<f", f.read(4))[0]
                        type86 = unpack("B", f.read(1))[0]
                        value1a86 = unpack("B", f.read(1))[0]
                        normalZ_86 = unpack("<h", f.read(2))[0]
                        vx87 = unpack("<f", f.read(4))[0]
                        vy87 = unpack("<f", f.read(4))[0]
                        vz87 = unpack("<f", f.read(4))[0]
                        type87 = unpack("B", f.read(1))[0]
                        value1a87 = unpack("B", f.read(1))[0]
                        normalZ_87 = unpack("<h", f.read(2))[0]
                        vx88 = unpack("<f", f.read(4))[0]
                        vy88 = unpack("<f", f.read(4))[0]
                        vz88 = unpack("<f", f.read(4))[0]
                        type88 = unpack("B", f.read(1))[0]
                        value1a88 = unpack("B", f.read(1))[0]
                        normalZ_88 = unpack("<h", f.read(2))[0]
                        vx89 = unpack("<f", f.read(4))[0]
                        vy89 = unpack("<f", f.read(4))[0]
                        vz89 = unpack("<f", f.read(4))[0]
                        type89 = unpack("B", f.read(1))[0]
                        value1a89 = unpack("B", f.read(1))[0]
                        normalZ_89 = unpack("<h", f.read(2))[0]
                        vertices.append([vx77,vz77,vy77])
                        vertices.append([vx78,vz78,vy78])
                        vertices.append([vx79,vz79,vy79])
                        vertices.append([vx80,vz80,vy80])
                        vertices.append([vx81,vz81,vy81])
                        vertices.append([vx82,vz82,vy82])
                        vertices.append([vx83,vz83,vy83])
                        vertices.append([vx84,vz84,vy84])
                        vertices.append([vx85,vz85,vy85])
                        vertices.append([vx86,vz86,vy86])
                        vertices.append([vx87,vz87,vy87])
                        vertices.append([vx88,vz88,vy88])
                        vertices.append([vx89,vz89,vy89])

                elif vertexCount == 14:
                    for j in range(vertexCount):
                        vx = unpack("<f", f.read(4))[0]
                        vy = unpack("<f", f.read(4))[0]
                        vz = unpack("<f", f.read(4))[0]
                        type4 = unpack("B", f.read(1))[0]==False
                        value1a = unpack("B", f.read(1))[0]
                        normalZ_ = unpack("<h", f.read(2))[0]
                        
                        nz1 = vz
                        ny1 = vy
                        nx1 = vx
                        nzz1 = normalZ_
                        nyy1 = normalZ_
                        nxx1 = normalZ_
                        nz1*=normalZ_
                        ny1*=normalZ_
                        nx1*=normalZ_
                        normalx = pack("<d", nx1)[0]
                        normaly = pack("<d", ny1)[0]
                        normalz = pack("<d", nz1)[0]
                        normals.append([nx1,ny1,nz1])
                        fa+=1
                        fb+=1
                        fc+=1

                        if type4 > 0:
                            faces.append([j+j+type4-type4-1+fa-j-j-1,j-j+type4-type4+1+fb-2-1,j+type4-type4+fc-j+2-4])

                    for i in range(vertexCount):
                        f.seek(-16,1)

                    for i in range(1):
                        vx90 = unpack("<f", f.read(4))[0]
                        vy90 = unpack("<f", f.read(4))[0]
                        vz90 = unpack("<f", f.read(4))[0]
                        type90 = unpack("B", f.read(1))[0]
                        value1a90 = unpack("B", f.read(1))[0]
                        normalZ_90 = unpack("<h", f.read(2))[0]
                        vx91 = unpack("<f", f.read(4))[0]
                        vy91 = unpack("<f", f.read(4))[0]
                        vz91 = unpack("<f", f.read(4))[0]
                        type91 = unpack("B", f.read(1))[0]
                        value1a91 = unpack("B", f.read(1))[0]
                        normalZ_91 = unpack("<h", f.read(2))[0]
                        vx92 = unpack("<f", f.read(4))[0]
                        vy92 = unpack("<f", f.read(4))[0]
                        vz92 = unpack("<f", f.read(4))[0]
                        type92 = unpack("B", f.read(1))[0]
                        value1a92 = unpack("B", f.read(1))[0]
                        normalZ_92 = unpack("<h", f.read(2))[0]
                        vx93 = unpack("<f", f.read(4))[0]
                        vy93 = unpack("<f", f.read(4))[0]
                        vz93 = unpack("<f", f.read(4))[0]
                        type93 = unpack("B", f.read(1))[0]
                        value1a93 = unpack("B", f.read(1))[0]
                        normalZ_93 = unpack("<h", f.read(2))[0]
                        vx94 = unpack("<f", f.read(4))[0]
                        vy94 = unpack("<f", f.read(4))[0]
                        vz94 = unpack("<f", f.read(4))[0]
                        type94 = unpack("B", f.read(1))[0]
                        value1a94 = unpack("B", f.read(1))[0]
                        normalZ_94 = unpack("<h", f.read(2))[0]
                        vx95 = unpack("<f", f.read(4))[0]
                        vy95 = unpack("<f", f.read(4))[0]
                        vz95 = unpack("<f", f.read(4))[0]
                        type95 = unpack("B", f.read(1))[0]
                        value1a95 = unpack("B", f.read(1))[0]
                        normalZ_95 = unpack("<h", f.read(2))[0]
                        vx96 = unpack("<f", f.read(4))[0]
                        vy96 = unpack("<f", f.read(4))[0]
                        vz96 = unpack("<f", f.read(4))[0]
                        type96 = unpack("B", f.read(1))[0]
                        value1a96 = unpack("B", f.read(1))[0]
                        normalZ_96 = unpack("<h", f.read(2))[0]
                        vx97 = unpack("<f", f.read(4))[0]
                        vy97 = unpack("<f", f.read(4))[0]
                        vz97 = unpack("<f", f.read(4))[0]
                        type97 = unpack("B", f.read(1))[0]
                        value1a97 = unpack("B", f.read(1))[0]
                        normalZ_97 = unpack("<h", f.read(2))[0]
                        vx98 = unpack("<f", f.read(4))[0]
                        vy98 = unpack("<f", f.read(4))[0]
                        vz98 = unpack("<f", f.read(4))[0]
                        type98 = unpack("B", f.read(1))[0]
                        value1a98 = unpack("B", f.read(1))[0]
                        normalZ_98 = unpack("<h", f.read(2))[0]
                        vx99 = unpack("<f", f.read(4))[0]
                        vy99 = unpack("<f", f.read(4))[0]
                        vz99 = unpack("<f", f.read(4))[0]
                        type99 = unpack("B", f.read(1))[0]
                        value1a99 = unpack("B", f.read(1))[0]
                        normalZ_99 = unpack("<h", f.read(2))[0]
                        vx100 = unpack("<f", f.read(4))[0]
                        vy100 = unpack("<f", f.read(4))[0]
                        vz100 = unpack("<f", f.read(4))[0]
                        type100 = unpack("B", f.read(1))[0]
                        value1a100 = unpack("B", f.read(1))[0]
                        normalZ_100 = unpack("<h", f.read(2))[0]
                        vx101 = unpack("<f", f.read(4))[0]
                        vy101 = unpack("<f", f.read(4))[0]
                        vz101 = unpack("<f", f.read(4))[0]
                        type101 = unpack("B", f.read(1))[0]
                        value1a101 = unpack("B", f.read(1))[0]
                        normalZ_101 = unpack("<h", f.read(2))[0]
                        vx102 = unpack("<f", f.read(4))[0]
                        vy102 = unpack("<f", f.read(4))[0]
                        vz102 = unpack("<f", f.read(4))[0]
                        type102 = unpack("B", f.read(1))[0]
                        value1a102 = unpack("B", f.read(1))[0]
                        normalZ_102 = unpack("<h", f.read(2))[0]
                        vx103 = unpack("<f", f.read(4))[0]
                        vy103 = unpack("<f", f.read(4))[0]
                        vz103 = unpack("<f", f.read(4))[0]
                        type103 = unpack("B", f.read(1))[0]
                        value1a103 = unpack("B", f.read(1))[0]
                        normalZ_103 = unpack("<h", f.read(2))[0]
                        vertices.append([vx90,vz90,vy90])
                        vertices.append([vx91,vz91,vy91])
                        vertices.append([vx92,vz92,vy92])
                        vertices.append([vx93,vz93,vy93])
                        vertices.append([vx94,vz94,vy94])
                        vertices.append([vx95,vz95,vy95])
                        vertices.append([vx96,vz96,vy96])
                        vertices.append([vx97,vz97,vy97])
                        vertices.append([vx98,vz98,vy98])
                        vertices.append([vx99,vz99,vy99])
                        vertices.append([vx100,vz100,vy100])
                        vertices.append([vx101,vz101,vy101])
                        vertices.append([vx102,vz102,vy102])
                        vertices.append([vx103,vz103,vy103])

                elif vertexCount == 15:
                    for j in range(vertexCount):
                        vx = unpack("<f", f.read(4))[0]
                        vy = unpack("<f", f.read(4))[0]
                        vz = unpack("<f", f.read(4))[0]
                        type4 = unpack("B", f.read(1))[0]==False
                        value1a = unpack("B", f.read(1))[0]
                        normalZ_ = unpack("<h", f.read(2))[0]
                        
                        nz1 = vz
                        ny1 = vy
                        nx1 = vx
                        nzz1 = normalZ_
                        nyy1 = normalZ_
                        nxx1 = normalZ_
                        nz1*=normalZ_
                        ny1*=normalZ_
                        nx1*=normalZ_
                        normalx = pack("<d", nx1)[0]
                        normaly = pack("<d", ny1)[0]
                        normalz = pack("<d", nz1)[0]
                        normals.append([nx1,ny1,nz1])
                        fa+=1
                        fb+=1
                        fc+=1

                        if type4 > 0:
                            faces.append([j+j+type4-type4-1+fa-j-j-1,j-j+type4-type4+1+fb-2-1,j+type4-type4+fc-j+2-4])

                    for i in range(vertexCount):
                        f.seek(-16,1)

                    for i in range(1):
                        vx104 = unpack("<f", f.read(4))[0]
                        vy104 = unpack("<f", f.read(4))[0]
                        vz104 = unpack("<f", f.read(4))[0]
                        type104 = unpack("B", f.read(1))[0]
                        value1a104 = unpack("B", f.read(1))[0]
                        normalZ_104 = unpack("<h", f.read(2))[0]
                        vx105 = unpack("<f", f.read(4))[0]
                        vy105 = unpack("<f", f.read(4))[0]
                        vz105 = unpack("<f", f.read(4))[0]
                        type105 = unpack("B", f.read(1))[0]
                        value1a105 = unpack("B", f.read(1))[0]
                        normalZ_105 = unpack("<h", f.read(2))[0]
                        vx106 = unpack("<f", f.read(4))[0]
                        vy106 = unpack("<f", f.read(4))[0]
                        vz106 = unpack("<f", f.read(4))[0]
                        type106 = unpack("B", f.read(1))[0]
                        value1a106 = unpack("B", f.read(1))[0]
                        normalZ_106 = unpack("<h", f.read(2))[0]
                        vx107 = unpack("<f", f.read(4))[0]
                        vy107 = unpack("<f", f.read(4))[0]
                        vz107 = unpack("<f", f.read(4))[0]
                        type107 = unpack("B", f.read(1))[0]
                        value1a107 = unpack("B", f.read(1))[0]
                        normalZ_107 = unpack("<h", f.read(2))[0]
                        vx108 = unpack("<f", f.read(4))[0]
                        vy108 = unpack("<f", f.read(4))[0]
                        vz108 = unpack("<f", f.read(4))[0]
                        type108 = unpack("B", f.read(1))[0]
                        value1a108 = unpack("B", f.read(1))[0]
                        normalZ_108 = unpack("<h", f.read(2))[0]
                        vx109 = unpack("<f", f.read(4))[0]
                        vy109 = unpack("<f", f.read(4))[0]
                        vz109 = unpack("<f", f.read(4))[0]
                        type109 = unpack("B", f.read(1))[0]
                        value1a109 = unpack("B", f.read(1))[0]
                        normalZ_109 = unpack("<h", f.read(2))[0]
                        vx110 = unpack("<f", f.read(4))[0]
                        vy110 = unpack("<f", f.read(4))[0]
                        vz110 = unpack("<f", f.read(4))[0]
                        type110 = unpack("B", f.read(1))[0]
                        value1a110 = unpack("B", f.read(1))[0]
                        normalZ_110 = unpack("<h", f.read(2))[0]
                        vx111 = unpack("<f", f.read(4))[0]
                        vy111 = unpack("<f", f.read(4))[0]
                        vz111 = unpack("<f", f.read(4))[0]
                        type111 = unpack("B", f.read(1))[0]
                        value1a111 = unpack("B", f.read(1))[0]
                        normalZ_111 = unpack("<h", f.read(2))[0]
                        vx112 = unpack("<f", f.read(4))[0]
                        vy112 = unpack("<f", f.read(4))[0]
                        vz112 = unpack("<f", f.read(4))[0]
                        type112 = unpack("B", f.read(1))[0]
                        value1a112 = unpack("B", f.read(1))[0]
                        normalZ_112 = unpack("<h", f.read(2))[0]
                        vx113 = unpack("<f", f.read(4))[0]
                        vy113 = unpack("<f", f.read(4))[0]
                        vz113 = unpack("<f", f.read(4))[0]
                        type113 = unpack("B", f.read(1))[0]
                        value1a113 = unpack("B", f.read(1))[0]
                        normalZ_113 = unpack("<h", f.read(2))[0]
                        vx114 = unpack("<f", f.read(4))[0]
                        vy114 = unpack("<f", f.read(4))[0]
                        vz114 = unpack("<f", f.read(4))[0]
                        type114 = unpack("B", f.read(1))[0]
                        value1a114 = unpack("B", f.read(1))[0]
                        normalZ_114 = unpack("<h", f.read(2))[0]
                        vx115 = unpack("<f", f.read(4))[0]
                        vy115 = unpack("<f", f.read(4))[0]
                        vz115 = unpack("<f", f.read(4))[0]
                        type115 = unpack("B", f.read(1))[0]
                        value1a115 = unpack("B", f.read(1))[0]
                        normalZ_115 = unpack("<h", f.read(2))[0]
                        vx116 = unpack("<f", f.read(4))[0]
                        vy116 = unpack("<f", f.read(4))[0]
                        vz116 = unpack("<f", f.read(4))[0]
                        type116 = unpack("B", f.read(1))[0]
                        value1a116 = unpack("B", f.read(1))[0]
                        normalZ_116 = unpack("<h", f.read(2))[0]
                        vx117 = unpack("<f", f.read(4))[0]
                        vy117 = unpack("<f", f.read(4))[0]
                        vz117 = unpack("<f", f.read(4))[0]
                        type117 = unpack("B", f.read(1))[0]
                        value1a117 = unpack("B", f.read(1))[0]
                        normalZ_117 = unpack("<h", f.read(2))[0]
                        vx117a = unpack("<f", f.read(4))[0]
                        vy117a = unpack("<f", f.read(4))[0]
                        vz117a = unpack("<f", f.read(4))[0]
                        type117a = unpack("B", f.read(1))[0]
                        value1a117a = unpack("B", f.read(1))[0]
                        normalZ_117a = unpack("<h", f.read(2))[0]
                        vertices.append([vx104,vz104,vy104])
                        vertices.append([vx105,vz105,vy105])
                        vertices.append([vx106,vz106,vy106])
                        vertices.append([vx107,vz107,vy107])
                        vertices.append([vx108,vz108,vy108])
                        vertices.append([vx109,vz109,vy109])
                        vertices.append([vx110,vz110,vy110])
                        vertices.append([vx111,vz111,vy111])
                        vertices.append([vx112,vz112,vy112])
                        vertices.append([vx113,vz113,vy113])
                        vertices.append([vx114,vz114,vy114])
                        vertices.append([vx115,vz115,vy115])
                        vertices.append([vx116,vz116,vy116])
                        vertices.append([vx117,vz117,vy117])
                        vertices.append([vx117a,vz117a,vy117a])

                elif vertexCount == 16:
                    for j in range(vertexCount):
                        vx = unpack("<f", f.read(4))[0]
                        vy = unpack("<f", f.read(4))[0]
                        vz = unpack("<f", f.read(4))[0]
                        type4 = unpack("B", f.read(1))[0]==False
                        value1a = unpack("B", f.read(1))[0]
                        normalZ_ = unpack("<h", f.read(2))[0]
                        
                        nz1 = vz
                        ny1 = vy
                        nx1 = vx
                        nzz1 = normalZ_
                        nyy1 = normalZ_
                        nxx1 = normalZ_
                        nz1*=normalZ_
                        ny1*=normalZ_
                        nx1*=normalZ_
                        normalx = pack("<d", nx1)[0]
                        normaly = pack("<d", ny1)[0]
                        normalz = pack("<d", nz1)[0]
                        normals.append([nx1,ny1,nz1])
                        fa+=1
                        fb+=1
                        fc+=1

                        if type4 > 0:
                            faces.append([j+j+type4-type4-1+fa-j-j-1,j-j+type4-type4+1+fb-2-1,j+type4-type4+fc-j+2-4])

                    for i in range(vertexCount):
                        f.seek(-16,1)

                    for i in range(1):
                        vx118 = unpack("<f", f.read(4))[0]
                        vy118 = unpack("<f", f.read(4))[0]
                        vz118 = unpack("<f", f.read(4))[0]
                        type118 = unpack("B", f.read(1))[0]
                        value1a118 = unpack("B", f.read(1))[0]
                        normalZ_118 = unpack("<h", f.read(2))[0]
                        vx119 = unpack("<f", f.read(4))[0]
                        vy119 = unpack("<f", f.read(4))[0]
                        vz119 = unpack("<f", f.read(4))[0]
                        type119 = unpack("B", f.read(1))[0]
                        value1a119 = unpack("B", f.read(1))[0]
                        normalZ_119 = unpack("<h", f.read(2))[0]
                        vx120 = unpack("<f", f.read(4))[0]
                        vy120 = unpack("<f", f.read(4))[0]
                        vz120 = unpack("<f", f.read(4))[0]
                        type120 = unpack("B", f.read(1))[0]
                        value1a120 = unpack("B", f.read(1))[0]
                        normalZ_120 = unpack("<h", f.read(2))[0]
                        vx121 = unpack("<f", f.read(4))[0]
                        vy121 = unpack("<f", f.read(4))[0]
                        vz121 = unpack("<f", f.read(4))[0]
                        type121 = unpack("B", f.read(1))[0]
                        value1a121 = unpack("B", f.read(1))[0]
                        normalZ_121 = unpack("<h", f.read(2))[0]
                        vx122 = unpack("<f", f.read(4))[0]
                        vy122 = unpack("<f", f.read(4))[0]
                        vz122 = unpack("<f", f.read(4))[0]
                        type122 = unpack("B", f.read(1))[0]
                        value1a122 = unpack("B", f.read(1))[0]
                        normalZ_122 = unpack("<h", f.read(2))[0]
                        vx123 = unpack("<f", f.read(4))[0]
                        vy123 = unpack("<f", f.read(4))[0]
                        vz123 = unpack("<f", f.read(4))[0]
                        type123 = unpack("B", f.read(1))[0]
                        value1a123 = unpack("B", f.read(1))[0]
                        normalZ_123 = unpack("<h", f.read(2))[0]
                        vx124 = unpack("<f", f.read(4))[0]
                        vy124 = unpack("<f", f.read(4))[0]
                        vz124 = unpack("<f", f.read(4))[0]
                        type124 = unpack("B", f.read(1))[0]
                        value1a124 = unpack("B", f.read(1))[0]
                        normalZ_124 = unpack("<h", f.read(2))[0]
                        vx125 = unpack("<f", f.read(4))[0]
                        vy125 = unpack("<f", f.read(4))[0]
                        vz125 = unpack("<f", f.read(4))[0]
                        type12511 = unpack("B", f.read(1))[0]
                        value1a125 = unpack("B", f.read(1))[0]
                        normalZ_125 = unpack("<h", f.read(2))[0]
                        vx126 = unpack("<f", f.read(4))[0]
                        vy126 = unpack("<f", f.read(4))[0]
                        vz126 = unpack("<f", f.read(4))[0]
                        type126 = unpack("B", f.read(1))[0]
                        value1a126 = unpack("B", f.read(1))[0]
                        normalZ_126 = unpack("<h", f.read(2))[0]
                        vx127 = unpack("<f", f.read(4))[0]
                        vy127 = unpack("<f", f.read(4))[0]
                        vz127 = unpack("<f", f.read(4))[0]
                        type127 = unpack("B", f.read(1))[0]
                        value1a127 = unpack("B", f.read(1))[0]
                        normalZ_127 = unpack("<h", f.read(2))[0]
                        vx128 = unpack("<f", f.read(4))[0]
                        vy128 = unpack("<f", f.read(4))[0]
                        vz128 = unpack("<f", f.read(4))[0]
                        type128 = unpack("B", f.read(1))[0]
                        value1a128 = unpack("B", f.read(1))[0]
                        normalZ_128 = unpack("<h", f.read(2))[0]
                        vx129 = unpack("<f", f.read(4))[0]
                        vy129 = unpack("<f", f.read(4))[0]
                        vz129 = unpack("<f", f.read(4))[0]
                        type129 = unpack("B", f.read(1))[0]
                        value1a129 = unpack("B", f.read(1))[0]
                        normalZ_129 = unpack("<h", f.read(2))[0]
                        vx130 = unpack("<f", f.read(4))[0]
                        vy130 = unpack("<f", f.read(4))[0]
                        vz130 = unpack("<f", f.read(4))[0]
                        type130 = unpack("B", f.read(1))[0]
                        value1a130 = unpack("B", f.read(1))[0]
                        normalZ_130 = unpack("<h", f.read(2))[0]
                        vx131 = unpack("<f", f.read(4))[0]
                        vy131 = unpack("<f", f.read(4))[0]
                        vz131 = unpack("<f", f.read(4))[0]
                        type131 = unpack("B", f.read(1))[0]
                        value1a131 = unpack("B", f.read(1))[0]
                        normalZ_131 = unpack("<h", f.read(2))[0]
                        vx132 = unpack("<f", f.read(4))[0]
                        vy132 = unpack("<f", f.read(4))[0]
                        vz132 = unpack("<f", f.read(4))[0]
                        type132 = unpack("B", f.read(1))[0]
                        value1a132 = unpack("B", f.read(1))[0]
                        normalZ_132 = unpack("<h", f.read(2))[0]
                        vx132a = unpack("<f", f.read(4))[0]
                        vy132a = unpack("<f", f.read(4))[0]
                        vz132a = unpack("<f", f.read(4))[0]
                        type132a = unpack("B", f.read(1))[0]
                        value1a132a = unpack("B", f.read(1))[0]
                        normalZ_132a = unpack("<h", f.read(2))[0]
                        vertices.append([vx118,vz118,vy118])
                        vertices.append([vx119,vz119,vy119])
                        vertices.append([vx120,vz120,vy120])
                        vertices.append([vx121,vz121,vy121])
                        vertices.append([vx122,vz122,vy122])
                        vertices.append([vx123,vz123,vy123])
                        vertices.append([vx124,vz124,vy124])
                        vertices.append([vx125,vz125,vy125])
                        vertices.append([vx126,vz126,vy126])
                        vertices.append([vx127,vz127,vy127])
                        vertices.append([vx128,vz128,vy128])
                        vertices.append([vx129,vz129,vy129])
                        vertices.append([vx130,vz130,vy130])
                        vertices.append([vx131,vz131,vy131])
                        vertices.append([vx132,vz132,vy132])
                        vertices.append([vx132a,vz132a,vy132a])

                elif vertexCount == 17:
                    for j in range(vertexCount):
                        vx = unpack("<f", f.read(4))[0]
                        vy = unpack("<f", f.read(4))[0]
                        vz = unpack("<f", f.read(4))[0]
                        type4 = unpack("B", f.read(1))[0]==False
                        value1a = unpack("B", f.read(1))[0]
                        normalZ_ = unpack("<h", f.read(2))[0]
                        
                        nz1 = vz
                        ny1 = vy
                        nx1 = vx
                        nzz1 = normalZ_
                        nyy1 = normalZ_
                        nxx1 = normalZ_
                        nz1*=normalZ_
                        ny1*=normalZ_
                        nx1*=normalZ_
                        normalx = pack("<d", nx1)[0]
                        normaly = pack("<d", ny1)[0]
                        normalz = pack("<d", nz1)[0]
                        normals.append([nx1,ny1,nz1])
                        fa+=1
                        fb+=1
                        fc+=1

                        if type4 > 0:
                            faces.append([j+j+type4-type4-1+fa-j-j-1,j-j+type4-type4+1+fb-2-1,j+type4-type4+fc-j+2-4])

                    for i in range(vertexCount):
                        f.seek(-16,1)

                    for i in range(1):
                        vx133 = unpack("<f", f.read(4))[0]
                        vy133 = unpack("<f", f.read(4))[0]
                        vz133 = unpack("<f", f.read(4))[0]
                        type133 = unpack("B", f.read(1))[0]
                        value1a133 = unpack("B", f.read(1))[0]
                        normalZ_133 = unpack("<h", f.read(2))[0]
                        vx134 = unpack("<f", f.read(4))[0]
                        vy134 = unpack("<f", f.read(4))[0]
                        vz134 = unpack("<f", f.read(4))[0]
                        type134 = unpack("B", f.read(1))[0]
                        value1a134 = unpack("B", f.read(1))[0]
                        normalZ_134 = unpack("<h", f.read(2))[0]
                        vx135 = unpack("<f", f.read(4))[0]
                        vy135 = unpack("<f", f.read(4))[0]
                        vz135 = unpack("<f", f.read(4))[0]
                        type135 = unpack("B", f.read(1))[0]
                        value1a135 = unpack("B", f.read(1))[0]
                        normalZ_135 = unpack("<h", f.read(2))[0]
                        vx136 = unpack("<f", f.read(4))[0]
                        vy136 = unpack("<f", f.read(4))[0]
                        vz136 = unpack("<f", f.read(4))[0]
                        type136 = unpack("B", f.read(1))[0]
                        value1a136 = unpack("B", f.read(1))[0]
                        normalZ_136 = unpack("<h", f.read(2))[0]
                        vx137 = unpack("<f", f.read(4))[0]
                        vy137 = unpack("<f", f.read(4))[0]
                        vz137 = unpack("<f", f.read(4))[0]
                        type137 = unpack("B", f.read(1))[0]
                        value1a137 = unpack("B", f.read(1))[0]
                        normalZ_137 = unpack("<h", f.read(2))[0]
                        vx138 = unpack("<f", f.read(4))[0]
                        vy138 = unpack("<f", f.read(4))[0]
                        vz138 = unpack("<f", f.read(4))[0]
                        type138 = unpack("B", f.read(1))[0]
                        value1a138 = unpack("B", f.read(1))[0]
                        normalZ_138 = unpack("<h", f.read(2))[0]
                        vx139 = unpack("<f", f.read(4))[0]
                        vy139 = unpack("<f", f.read(4))[0]
                        vz139 = unpack("<f", f.read(4))[0]
                        type139 = unpack("B", f.read(1))[0]
                        value1a139 = unpack("B", f.read(1))[0]
                        normalZ_139 = unpack("<h", f.read(2))[0]
                        vx140 = unpack("<f", f.read(4))[0]
                        vy140 = unpack("<f", f.read(4))[0]
                        vz140 = unpack("<f", f.read(4))[0]
                        type140 = unpack("B", f.read(1))[0]
                        value1a140 = unpack("B", f.read(1))[0]
                        normalZ_140 = unpack("<h", f.read(2))[0]
                        vx141 = unpack("<f", f.read(4))[0]
                        vy141 = unpack("<f", f.read(4))[0]
                        vz141 = unpack("<f", f.read(4))[0]
                        type141 = unpack("B", f.read(1))[0]
                        value1a141 = unpack("B", f.read(1))[0]
                        normalZ_141 = unpack("<h", f.read(2))[0]
                        vx142 = unpack("<f", f.read(4))[0]
                        vy142 = unpack("<f", f.read(4))[0]
                        vz142 = unpack("<f", f.read(4))[0]
                        type142 = unpack("B", f.read(1))[0]
                        value1a142 = unpack("B", f.read(1))[0]
                        normalZ_142 = unpack("<h", f.read(2))[0]
                        vx143 = unpack("<f", f.read(4))[0]
                        vy143 = unpack("<f", f.read(4))[0]
                        vz143 = unpack("<f", f.read(4))[0]
                        type143 = unpack("B", f.read(1))[0]
                        value1a143 = unpack("B", f.read(1))[0]
                        normalZ_143 = unpack("<h", f.read(2))[0]
                        vx144 = unpack("<f", f.read(4))[0]
                        vy144 = unpack("<f", f.read(4))[0]
                        vz144 = unpack("<f", f.read(4))[0]
                        type144 = unpack("B", f.read(1))[0]
                        value1a144 = unpack("B", f.read(1))[0]
                        normalZ_144 = unpack("<h", f.read(2))[0]
                        vx145 = unpack("<f", f.read(4))[0]
                        vy145 = unpack("<f", f.read(4))[0]
                        vz145 = unpack("<f", f.read(4))[0]
                        type145 = unpack("B", f.read(1))[0]
                        value1a145 = unpack("B", f.read(1))[0]
                        normalZ_145 = unpack("<h", f.read(2))[0]
                        vx146 = unpack("<f", f.read(4))[0]
                        vy146 = unpack("<f", f.read(4))[0]
                        vz146 = unpack("<f", f.read(4))[0]
                        type146 = unpack("B", f.read(1))[0]
                        value1a146 = unpack("B", f.read(1))[0]
                        normalZ_146 = unpack("<h", f.read(2))[0]
                        vx147 = unpack("<f", f.read(4))[0]
                        vy147 = unpack("<f", f.read(4))[0]
                        vz147 = unpack("<f", f.read(4))[0]
                        type147 = unpack("B", f.read(1))[0]
                        value1a147 = unpack("B", f.read(1))[0]
                        normalZ_147 = unpack("<h", f.read(2))[0]
                        vx148 = unpack("<f", f.read(4))[0]
                        vy148 = unpack("<f", f.read(4))[0]
                        vz148 = unpack("<f", f.read(4))[0]
                        type148 = unpack("B", f.read(1))[0]
                        value1a148 = unpack("B", f.read(1))[0]
                        normalZ_148 = unpack("<h", f.read(2))[0]
                        vx149 = unpack("<f", f.read(4))[0]
                        vy149 = unpack("<f", f.read(4))[0]
                        vz149 = unpack("<f", f.read(4))[0]
                        type149 = unpack("B", f.read(1))[0]
                        value1a149 = unpack("B", f.read(1))[0]
                        normalZ_149 = unpack("<h", f.read(2))[0]
                        vertices.append([vx133,vz133,vy133])
                        vertices.append([vx134,vz134,vy134])
                        vertices.append([vx135,vz135,vy135])
                        vertices.append([vx136,vz136,vy136])
                        vertices.append([vx137,vz137,vy137])
                        vertices.append([vx138,vz138,vy138])
                        vertices.append([vx139,vz139,vy139])
                        vertices.append([vx140,vz140,vy140])
                        vertices.append([vx141,vz141,vy141])
                        vertices.append([vx142,vz142,vy142])
                        vertices.append([vx143,vz143,vy143])
                        vertices.append([vx144,vz144,vy144])
                        vertices.append([vx145,vz145,vy145])
                        vertices.append([vx146,vz146,vy146])
                        vertices.append([vx147,vz147,vy147])
                        vertices.append([vx148,vz148,vy148])
                        vertices.append([vx149,vz149,vy149])

                elif vertexCount == 18:
                    for j in range(vertexCount):
                        vx = unpack("<f", f.read(4))[0]
                        vy = unpack("<f", f.read(4))[0]
                        vz = unpack("<f", f.read(4))[0]
                        type4 = unpack("B", f.read(1))[0]==False
                        value1a = unpack("B", f.read(1))[0]
                        normalZ_ = unpack("<h", f.read(2))[0]
                        
                        nz1 = vz
                        ny1 = vy
                        nx1 = vx
                        nzz1 = normalZ_
                        nyy1 = normalZ_
                        nxx1 = normalZ_
                        nz1*=normalZ_
                        ny1*=normalZ_
                        nx1*=normalZ_
                        normalx = pack("<d", nx1)[0]
                        normaly = pack("<d", ny1)[0]
                        normalz = pack("<d", nz1)[0]
                        normals.append([nx1,ny1,nz1])
                        fa+=1
                        fb+=1
                        fc+=1

                        if type4 > 0:
                            faces.append([j+j+type4-type4-1+fa-j-j-1,j-j+type4-type4+1+fb-2-1,j+type4-type4+fc-j+2-4])

                    for i in range(vertexCount):
                        f.seek(-16,1)

                    for i in range(1):
                        vx150 = unpack("<f", f.read(4))[0]
                        vy150 = unpack("<f", f.read(4))[0]
                        vz150 = unpack("<f", f.read(4))[0]
                        type150 = unpack("B", f.read(1))[0]
                        value1a150 = unpack("B", f.read(1))[0]
                        normalZ_150 = unpack("<h", f.read(2))[0]
                        vx151 = unpack("<f", f.read(4))[0]
                        vy151 = unpack("<f", f.read(4))[0]
                        vz151 = unpack("<f", f.read(4))[0]
                        type151 = unpack("B", f.read(1))[0]
                        value1a151 = unpack("B", f.read(1))[0]
                        normalZ_151 = unpack("<h", f.read(2))[0]
                        vx152 = unpack("<f", f.read(4))[0]
                        vy152 = unpack("<f", f.read(4))[0]
                        vz152 = unpack("<f", f.read(4))[0]
                        type152 = unpack("B", f.read(1))[0]
                        value1a152 = unpack("B", f.read(1))[0]
                        normalZ_152 = unpack("<h", f.read(2))[0]
                        vx153 = unpack("<f", f.read(4))[0]
                        vy153 = unpack("<f", f.read(4))[0]
                        vz153 = unpack("<f", f.read(4))[0]
                        type153 = unpack("B", f.read(1))[0]
                        value1a153 = unpack("B", f.read(1))[0]
                        normalZ_153 = unpack("<h", f.read(2))[0]
                        vx154 = unpack("<f", f.read(4))[0]
                        vy154 = unpack("<f", f.read(4))[0]
                        vz154 = unpack("<f", f.read(4))[0]
                        type154 = unpack("B", f.read(1))[0]
                        value1a154 = unpack("B", f.read(1))[0]
                        normalZ_154 = unpack("<h", f.read(2))[0]
                        vx155 = unpack("<f", f.read(4))[0]
                        vy155 = unpack("<f", f.read(4))[0]
                        vz155 = unpack("<f", f.read(4))[0]
                        type155 = unpack("B", f.read(1))[0]
                        value1a155 = unpack("B", f.read(1))[0]
                        normalZ_155 = unpack("<h", f.read(2))[0]
                        vx156 = unpack("<f", f.read(4))[0]
                        vy156 = unpack("<f", f.read(4))[0]
                        vz156 = unpack("<f", f.read(4))[0]
                        type156 = unpack("B", f.read(1))[0]
                        value1a156 = unpack("B", f.read(1))[0]
                        normalZ_156 = unpack("<h", f.read(2))[0]
                        vx157 = unpack("<f", f.read(4))[0]
                        vy157 = unpack("<f", f.read(4))[0]
                        vz157 = unpack("<f", f.read(4))[0]
                        type157 = unpack("B", f.read(1))[0]
                        value1a157 = unpack("B", f.read(1))[0]
                        normalZ_157 = unpack("<h", f.read(2))[0]
                        vx158 = unpack("<f", f.read(4))[0]
                        vy158 = unpack("<f", f.read(4))[0]
                        vz158 = unpack("<f", f.read(4))[0]
                        type158 = unpack("B", f.read(1))[0]
                        value1a158 = unpack("B", f.read(1))[0]
                        normalZ_158 = unpack("<h", f.read(2))[0]
                        vx159 = unpack("<f", f.read(4))[0]
                        vy159 = unpack("<f", f.read(4))[0]
                        vz159 = unpack("<f", f.read(4))[0]
                        type159 = unpack("B", f.read(1))[0]
                        value1a159 = unpack("B", f.read(1))[0]
                        normalZ_159 = unpack("<h", f.read(2))[0]
                        vx160 = unpack("<f", f.read(4))[0]
                        vy160 = unpack("<f", f.read(4))[0]
                        vz160 = unpack("<f", f.read(4))[0]
                        type160 = unpack("B", f.read(1))[0]
                        value1a160 = unpack("B", f.read(1))[0]
                        normalZ_160 = unpack("<h", f.read(2))[0]
                        vx161 = unpack("<f", f.read(4))[0]
                        vy161 = unpack("<f", f.read(4))[0]
                        vz161 = unpack("<f", f.read(4))[0]
                        type161 = unpack("B", f.read(1))[0]
                        value1a161 = unpack("B", f.read(1))[0]
                        normalZ_161 = unpack("<h", f.read(2))[0]
                        vx162 = unpack("<f", f.read(4))[0]
                        vy162 = unpack("<f", f.read(4))[0]
                        vz162 = unpack("<f", f.read(4))[0]
                        type162 = unpack("B", f.read(1))[0]
                        value1a162 = unpack("B", f.read(1))[0]
                        normalZ_162 = unpack("<h", f.read(2))[0]
                        vx163 = unpack("<f", f.read(4))[0]
                        vy163 = unpack("<f", f.read(4))[0]
                        vz163 = unpack("<f", f.read(4))[0]
                        type163 = unpack("B", f.read(1))[0]
                        value1a163 = unpack("B", f.read(1))[0]
                        normalZ_163 = unpack("<h", f.read(2))[0]
                        vx164 = unpack("<f", f.read(4))[0]
                        vy164 = unpack("<f", f.read(4))[0]
                        vz164 = unpack("<f", f.read(4))[0]
                        type164 = unpack("B", f.read(1))[0]
                        value1a164 = unpack("B", f.read(1))[0]
                        normalZ_164 = unpack("<h", f.read(2))[0]
                        vx165 = unpack("<f", f.read(4))[0]
                        vy165 = unpack("<f", f.read(4))[0]
                        vz165 = unpack("<f", f.read(4))[0]
                        type165 = unpack("B", f.read(1))[0]
                        value1a165 = unpack("B", f.read(1))[0]
                        normalZ_165 = unpack("<h", f.read(2))[0]
                        vx166 = unpack("<f", f.read(4))[0]
                        vy166 = unpack("<f", f.read(4))[0]
                        vz166 = unpack("<f", f.read(4))[0]
                        type166 = unpack("B", f.read(1))[0]
                        value1a166 = unpack("B", f.read(1))[0]
                        normalZ_166 = unpack("<h", f.read(2))[0]
                        vx167 = unpack("<f", f.read(4))[0]
                        vy167 = unpack("<f", f.read(4))[0]
                        vz167 = unpack("<f", f.read(4))[0]
                        type167 = unpack("B", f.read(1))[0]
                        value1a167 = unpack("B", f.read(1))[0]
                        normalZ_167 = unpack("<h", f.read(2))[0]
                        vertices.append([vx150,vz150,vy150])
                        vertices.append([vx151,vz151,vy151])
                        vertices.append([vx152,vz152,vy152])
                        vertices.append([vx153,vz153,vy153])
                        vertices.append([vx154,vz154,vy154])
                        vertices.append([vx155,vz155,vy155])
                        vertices.append([vx156,vz156,vy156])
                        vertices.append([vx157,vz157,vy157])
                        vertices.append([vx158,vz158,vy158])
                        vertices.append([vx159,vz159,vy159])
                        vertices.append([vx160,vz160,vy160])
                        vertices.append([vx161,vz161,vy161])
                        vertices.append([vx162,vz162,vy162])
                        vertices.append([vx163,vz163,vy163])
                        vertices.append([vx164,vz164,vy164])
                        vertices.append([vx165,vz165,vy165])
                        vertices.append([vx166,vz166,vy166])
                        vertices.append([vx167,vz167,vy167])
                                        
                            
        elif Chunk == b"SST0":
            break

    collection = bpy.data.collections.new(os.path.basename(os.path.splitext(filepath)[0]))
    bpy.context.scene.collection.children.link(collection)

    mesh = bpy.data.meshes.new(os.path.basename(os.path.splitext(filepath)[0]))
    mesh.from_pydata(vertices, [], faces)
    objs = bpy.data.objects.new(os.path.basename(os.path.splitext(filepath)[0]), mesh)
    collection.objects.link(objs)

    bpy.context.view_layer.objects.active = objs

    bpy.ops.object.select_all(action='SELECT')
    bpy.ops.object.shade_smooth()
    bpy.ops.object.editmode_toggle()
    bpy.ops.mesh.remove_doubles()
    bpy.ops.mesh.normals_make_consistent(inside=False)
    bpy.ops.object.editmode_toggle()

    NU_MIX_MODE = 'ShaderNodeMixRGB'
    NU_RGBA_VERT = 'ShaderNodeVertexColor'
    mats = bpy.data.materials.new(os.path.basename(os.path.splitext(filepath)[0]))
    objs.data.materials.append(mats)

    previous_mix = None
    previous_rgba = None

    BSDF = "Principled BSDF"

    for i, mat in enumerate(bpy.data.materials):
        mat.use_nodes = True
        mat.blend_method = "HASHED"

    try:
        

        vindex = 0

        for vertex in mesh.vertices:
            vertex.normal = normals[vindex] # where "normals" is a list of normals
            vindex += 1
    except:
        AttributeError

def get_objects_with_uvs_rgba_all(f, filepath):
    f.seek(0)
    vertices=[]
    faces=[]
    fa=-1
    fb=0
    fc=1
    uvs=[]
    rgba=[]
    allOBJread = f.read()
    readallobjfirst = allOBJread.find(b"\x03\x01\x00\x01")
    if allOBJread != 0:
        f.seek(readallobjfirst,0)
        f.seek(4,1)
        offset1 = unpack("B", f.read(1))[0]
        if offset1 == int(1):
            f.seek(4,1)
            value1 = unpack("B", f.read(1))[0]
            stripcount = unpack("B", f.read(1))[0]
            flag__s = unpack("B", f.read(1))[0]
            if flag__s == 0x6D:
                for j in range(stripcount):
                    vx = unpack("<h", f.read(2))[0]/4096
                    vy = unpack("<h", f.read(2))[0]/4096
                    vz = unpack("<h", f.read(2))[0]/4096
                    type4 = unpack("B", f.read(1))[0]==False
                    value1 = unpack("B", f.read(1))[0]
                    vertices.append([vx,vz,vy])
                    fa+=1
                    fb+=1
                    fc+=1
                    if type4 > 0:
                        faces.append([j+j+type4-type4-1+fa-j-j-1,j-j+type4-type4+1+fb-2-1,j+type4-type4+fc-j+2-4])
                type5 = unpack("B", f.read(1))[0]
                if type5 == int(4):
                    value1 = unpack("B", f.read(1))[0]
                    uvcount = unpack("B", f.read(1))[0]
                    flagUV = unpack("B", f.read(1))[0]
                    if flagUV == 0x65:
                        for i in range(uvcount):
                            uvx = unpack("<h", f.read(2))[0]/4096
                            uvy = unpack("<h", f.read(2))[0]/4096
                            uvs.append([+uvx,-uvy])
                    elif flagUV == 0x6D:
                        for i in range(uvcount):
                            uvx = unpack("<h", f.read(2))[0]/4096
                            uvy = unpack("<h", f.read(2))[0]/4096
                            f.seek(4,1)
                            uvs.append([+uvx,-uvy])
                elif type5 == int(5):
                    value1 = unpack("B", f.read(1))[0]
                    vertexcolor = unpack("B", f.read(1))[0]
                    vc_Flags = unpack("B", f.read(1))[0]
                    if vc_Flags == 0x6E:
                        for i in range(vertexcolor):
                            r = unpack("B", f.read(1))[0]/127
                            g = unpack("B", f.read(1))[0]/127
                            b = unpack("B", f.read(1))[0]/127
                            a = unpack("B", f.read(1))[0]/127
                            rgba.append([r,g,b,a])
                    elif vc_Flags == 0x70:
                        for i in range(vertexcolor):
                            d = f.read(3)
                            rgb = unpack("<I", d + b"\x00")[0] / 16777215
                            

                            rgba.append([rgb,rgb,rgb,1])

                            
                elif type5 == int(0):
                    f.seek(3,1)
                    type_a = unpack("B", f.read(1))[0]
                    if type_a == int(4):
                        
                        value1 = unpack("B", f.read(1))[0]
                        uvcount = unpack("B", f.read(1))[0]
                        uvsflags = unpack("B", f.read(1))[0]
                        if uvsflags == 0x65:
                            for i in range(uvcount):
                                uvx = unpack("<h", f.read(2))[0]/4096
                                uvy = unpack("<h", f.read(2))[0]/4096
                                uvs.append([+uvx,-uvy])
                        elif uvflags == 0x6D:
                            for i in range(uvcount):
                                uvx = unpack("<h", f.read(2))[0]/4096
                                uvy = unpack("<h", f.read(2))[0]/4096
                                f.seek(4,1)
                                uvs.append([+uvx,-uvy])

                elif type5 == int(1):
                    f.seek(3,1)
                    type_b = unpack("B", f.read(1))[0]
                    if type_b == int(4):
                        value1 = unpack("B", f.read(1))[0]
                        uvcount = unpack("B", f.read(1))[0]
                        uvsflags = unpack("B", f.read(1))[0]
                        if uvsflags == 0x65:
                            for i in range(uvcount):
                                uvx = unpack("<h", f.read(2))[0]/4096
                                uvy = unpack("<h", f.read(2))[0]/4096
                                uvs.append([+uvx,-uvy])
                        elif uvflags == 0x6D:
                            for i in range(uvcount):
                                uvx = unpack("<h", f.read(2))[0]/4096
                                uvy = unpack("<h", f.read(2))[0]/4096
                                f.seek(4,1)
                                uvs.append([+uvx,-uvy])
        elif offset1 == int(3):
            value1 = unpack("B", f.read(1))[0]
            stripcount = unpack("B", f.read(1))[0]
            flag_Ss = unpack("B", f.read(1))[0]
            if flag_Ss == 0x6C:
                for j in range(stripcount):
                    vx = unpack("<f", f.read(4))[0]
                    vy = unpack("<f", f.read(4))[0]
                    vz = unpack("<f", f.read(4))[0]
                    type4 = unpack("B", f.read(1))[0]==False
                    value1 = unpack("B", f.read(1))[0]
                    f.seek(2,1)
                    vertices.append([vx,vz,vy])
                    fa+=1
                    fb+=1
                    fc+=1
                    if type4 > 0:
                        faces.append([j+j+type4-type4-1+fa-j-j-1,j-j+type4-type4+1+fb-2-1,j+type4-type4+fc-j+2-4])
                type5a = unpack("B", f.read(1))[0]
                if type5a == int(4):
                    value1 = unpack("B", f.read(1))[0]
                    uvcount = unpack("B", f.read(1))[0]
                    flagUV = unpack("B", f.read(1))[0]
                    if flagUV == 0x65:
                        for i in range(uvcount):
                            uvx = unpack("<h", f.read(2))[0]/4096
                            uvy = unpack("<h", f.read(2))[0]/4096
                            uvs.append([+uvx,-uvy])
                    elif flagUV == 0x6D:
                        for i in range(uvcount):
                            uvx = unpack("<h", f.read(2))[0]/4096
                            uvy = unpack("<h", f.read(2))[0]/4096
                            f.seek(4,1)
                            uvs.append([+uvx,-uvy])


                elif type5a == int(5):
                    value1 = unpack("B", f.read(1))[0]
                    vertexcolor = unpack("B", f.read(1))[0]
                    vc_Flags = unpack("B", f.read(1))[0]
                    if vc_Flags == 0x6E:
                        for i in range(vertexcolor):
                            r = unpack("B", f.read(1))[0]/127
                            g = unpack("B", f.read(1))[0]/127
                            b = unpack("B", f.read(1))[0]/127
                            a = unpack("B", f.read(1))[0]/127
                            rgba.append([r,g,b,a])
                    elif vc_Flags == 0x70:
                        for i in range(vertexcolor):
                            r = int(abs(unpack("B", f.read(1))[0]))
                            g = int(abs(unpack("B", f.read(1))[0]))
                            b = int(abs(unpack("B", f.read(1))[0]))
                            a = int(abs(unpack("B", f.read(1))[0]))

                            new_r = r
                            new_g = g
                            new_b = b
                            new_a = a

                            new_r*int(255/255/255)
                            new_g*int(255/255/255)
                            new_b*int(255/255/255)
                            new_a!=False
                            rgba.append([new_r,new_g,new_b,new_a])
                    

def get_5thobjects_with_uvs_and_rgba(f, filepath):
    f.seek(0)
    vertices=[]
    faces=[]
    normals=[]
    fa=-1
    fb=0
    fc=1
    uvs=[]
    rgba=[]
    firstOBJread = f.read()
    readobjfirst = firstOBJread.find(b"\x03\x01\x00\x01\x01\x00\x00\x05\x03\x80")
    if firstOBJread != 0:
        f.seek(readobjfirst,0)
        f.seek(10,1)
        vertexCount = unpack("B", f.read(1))[0]
        flags = unpack("B", f.read(1))[0]
        if flags == 0x6D:
            
            for j in range(vertexCount):
                vx = unpack("<h", f.read(2))[0] / 4096
                vy = unpack("<h", f.read(2))[0] / 4096
                vz = unpack("<h", f.read(2))[0] / 4096
                type4 = unpack("B", f.read(1))[0]==False
                value1 = unpack("B", f.read(1))[0]
                vertices.append([vx,vz,vy])
                fa+=1
                fb+=1
                fc+=1
                if type4 > 0:
                    faces.append([j+j+type4-type4-1+fa-j-j-1,j-j+type4-type4+1+fb-2-1,j+type4-type4+fc-j+2-4])
            f.seek(6,1)
            uvcount = unpack("B", f.read(1))[0]
            flags = unpack("B", f.read(1))[0]
            if flags == 0x65:
                for i in range(uvcount):
                    uvx = unpack("<h", f.read(2))[0] / 4096
                    uvy = unpack("<h", f.read(2))[0] / 4096
                    uvs.append([+uvx,-uvy])
                f.seek(2,1)
                rgbacount = unpack("B", f.read(1))[0]
                flags = unpack("B", f.read(1))[0]
                if flags == 0x6E:
                    for c in range(rgbacount):
                        r = unpack("B", f.read(1))[0] / 127.0
                        g = unpack("B", f.read(1))[0] / 127.0
                        b = unpack("B", f.read(1))[0] / 127.0
                        a = unpack("B", f.read(1))[0] / 127.0
                        rgba.append([r,g,b,a])

        collection = bpy.data.collections.new(os.path.basename(os.path.splitext(filepath)[0]))
        bpy.context.scene.collection.children.link(collection)
        mesh = bpy.data.meshes.new(os.path.basename(os.path.splitext(filepath)[0]))
        mesh.from_pydata(vertices, [], faces)
        object = bpy.data.objects.new(os.path.basename(os.path.splitext(filepath)[0]), mesh)
        collection.objects.link(object)
            
        for fac in mesh.polygons:
            fac.use_smooth = True

        uv_tex = mesh.uv_layers.new()
        uv_layer = mesh.uv_layers[0].data
        vert_loops = {}
        for l in mesh.loops:
            vert_loops.setdefault(l.vertex_index, []).append(l.index)
        for i, coord in enumerate(uvs):
            for li in vert_loops[i]:
                uv_layer[li].uv = coord

        obj = bpy.data.objects[os.path.basename(os.path.splitext(filepath)[0])]
        bpy.context.view_layer.objects.active = obj

        colname = "GSC_VERTEXCOLORS"

        colattr = obj.data.color_attributes.new(
            name=colname,
            type='FLOAT_COLOR',
            domain='POINT',
        )

        for v_index in range(len(obj.data.vertices)):
            colattr.data[v_index].color = rgba[v_index]

def get_4thobjects_with_uvs_and_rgba(f, filepath):
    f.seek(0)
    vertices=[]
    faces=[]
    normals=[]
    fa=-1
    fb=0
    fc=1
    uvs=[]
    rgba=[]
    firstOBJread = f.read()
    readobjfirst = firstOBJread.find(b"\x03\x01\x00\x01\x03\x80")
    if firstOBJread != 0:
        f.seek(readobjfirst,0)
        f.seek(6,1)
        vertexCount = unpack("B", f.read(1))[0]
        f.seek(1,1)
        for j in range(vertexCount):
            vx = unpack("<f", f.read(4))[0]
            vy = unpack("<f", f.read(4))[0]
            vz = unpack("<f", f.read(4))[0]
            type4 = unpack("B", f.read(1))[0]==False
            value1 = unpack("B", f.read(1))[0]
            f.seek(2,1)
            vertices.append([vx,vz,vy])
            fa+=1
            fb+=1
            fc+=1
            if type4 > 0:
                faces.append([j+j+type4-type4-1+fa-j-j-1,j-j+type4-type4+1+fb-2-1,j+type4-type4+fc-j+2-4])
                
        f.seek(1,1)
        value1 = unpack("B", f.read(1))[0]
        uvcount = unpack("B", f.read(1))[0]
        flags = unpack("B", f.read(1))[0]
        if flags == 0x6D:
            
            for i in range(uvcount):
                ux = unpack("<h", f.read(2))[0] / 4096.0
                uy = unpack("<h", f.read(2))[0] / 4096.0
                f.seek(4,1)
                uvs.append([+ux,-uy])
            f.seek(2, 1)
            rgbacount = unpack("B", f.read(1))[0]
            flags_ = unpack("B", f.read(1))[0]
            if flags_ == 0x6E:
                
                for c in range(rgbacount):
                    r = unpack("B", f.read(1))[0] / 127.0
                    g = unpack("B", f.read(1))[0] / 127.0
                    b = unpack("B", f.read(1))[0] / 127.0
                    a = unpack("B", f.read(1))[0] / 127.0
                    rgba.append([r,g,b,a])

        collection = bpy.data.collections.new(os.path.basename(os.path.splitext(filepath)[0]))
        bpy.context.scene.collection.children.link(collection)
        mesh = bpy.data.meshes.new(os.path.basename(os.path.splitext(filepath)[0]))
        mesh.from_pydata(vertices, [], faces)
        obj = bpy.data.objects.new(os.path.basename(os.path.splitext(filepath)[0]), mesh)
        collection.objects.link(obj)
            
        for fac in mesh.polygons:
            fac.use_smooth = True

        uv_tex = mesh.uv_layers.new()
        uv_layer = mesh.uv_layers[0].data
        vert_loops = {}
        for l in mesh.loops:
            vert_loops.setdefault(l.vertex_index, []).append(l.index)
        for i, coord in enumerate(uvs):
            for li in vert_loops[i]:
                uv_layer[li].uv = coord

        obj = bpy.data.objects[os.path.basename(os.path.splitext(filepath)[0])]
        bpy.context.view_layer.objects.active = obj

        colname = "GSC_VERTEXCOLORS"

        colattr = obj.data.color_attributes.new(
            name=colname,
            type='FLOAT_COLOR',
            domain='POINT',
        )

        for v_index in range(len(obj.data.vertices)):
            colattr.data[v_index].color = rgba[v_index]

def get_3rdobjects_with_uvs_and_rgba(f, filepath):
    f.seek(0)
    vertices=[]
    faces=[]
    normals=[]
    fa=-1
    fb=0
    fc=1
    uvs=[]
    rgba=[]
    chunks=0
    paddingwhere=0
    firstOBJread = f.read()
    readobjfirst = firstOBJread.find(b"\x03\x01\x00\x01\x03\x80")
    if firstOBJread != 0:
        f.seek(readobjfirst,0)
        f.seek(6,1)
        vertexCount = unpack("B", f.read(1))[0]
        f.seek(1,1)
        f.seek(seek_,1)
        for i in range(vertexCount):
            vx = unpack("<f", f.read(4))[0]
            vy = unpack("<f", f.read(4))[0]
            vz = unpack("<f", f.read(4))[0]
            vw = unpack("<f", f.read(4))[0]
            vertices.append([vx,vz,vy])
            normals.append([0,0,1])
        for i in range(vertexCount-2):
            faces.append([i-i%2+1,i+i%2,i+2])
            faces.append([i+i%2,i-i%2+1,i+2])
        f.seek(2, 1)
        uvcount = unpack("b", f.read(1))[0]
        f.seek(1,1)
        for i in range(uvcount):
            ux = unpack("<h", f.read(2))[0] / 4096.0
            uy = unpack("<h", f.read(2))[0] / 4096.0
            uvs.append([+ux,-uy])
        f.seek(2, 1)
        rgbacount = unpack("b", f.read(1))[0]
        f.seek(1,1)
        for c in range(rgbacount):
            r = unpack("B", f.read(1))[0] / 127.0
            g = unpack("B", f.read(1))[0] / 127.0
            b = unpack("B", f.read(1))[0] / 127.0
            a = unpack("B", f.read(1))[0] / 127.0
            rgba.append([r,g,b,a])

        collection = bpy.data.collections.new(os.path.basename(os.path.splitext(filepath)[0]))
        bpy.context.scene.collection.children.link(collection)
        mesh = bpy.data.meshes.new(os.path.basename(os.path.splitext(filepath)[0]))
        mesh.from_pydata(vertices, [], faces)
        object = bpy.data.objects.new(os.path.basename(os.path.splitext(filepath)[0]), mesh)
        collection.objects.link(object)
            
        for fac in mesh.polygons:
            fac.use_smooth = True

        uv_tex = mesh.uv_layers.new()
        uv_layer = mesh.uv_layers[0].data
        vert_loops = {}
        for l in mesh.loops:
            vert_loops.setdefault(l.vertex_index, []).append(l.index)
        for i, coord in enumerate(uvs):
            for li in vert_loops[i]:
                uv_layer[li].uv = coord

        obj = bpy.data.objects[os.path.basename(os.path.splitext(filepath)[0])]
        bpy.context.view_layer.objects.active = obj

        colname = "GSC_VERTEXCOLORS"

        colattr = obj.data.color_attributes.new(
            name=colname,
            type='FLOAT_COLOR',
            domain='POINT',
        )

        for v_index in range(len(obj.data.vertices)):
            colattr.data[v_index].color = rgba[v_index]

def get_2ndobjects_with_uvs_and_rgba(f, filepath):
    f.seek(0)
    fa=-1
    fb=0
    fc=1
    vertices=[]
    faces=[]
    normals=[]
    uvs=[]
    rgba=[]
    chunks=0
    paddingWhere=0
    firstOBJread = f.read()
    readobjfirst = firstOBJread.find(b"\x03\x01\x00\x01\x03\x80")
    if firstOBJread != 0:
        f.seek(readobjfirst,0)
        f.seek(6,1)
        vertexCount = unpack("b", f.read(1))[0]
        f.seek(1,1)
        for i in range(vertexCount):
            vx = unpack("<f", f.read(4))[0]
            vy = unpack("<f", f.read(4))[0]
            vz = unpack("<f", f.read(4))[0]
            vw = unpack("<f", f.read(4))[0]
            vertices.append([vx,vz,vy])
            normals.append([0,0,1])
        for i in range(vertexCount-2):
            faces.append([i-i%2+1,i+i%2,i+2])
            faces.append([i+i%2,i-i%2+1,i+2])
        f.seek(6, 1)
        uvcount = unpack("b", f.read(1))[0]
        f.seek(1,1)
        for i in range(uvcount):
            ux = unpack("<h", f.read(2))[0] / 4096.0
            uy = unpack("<h", f.read(2))[0] / 4096.0
            uvs.append([+ux,-uy])
        f.seek(6, 1)
        rgbacount = unpack("b", f.read(1))[0]
        f.seek(1,1)
        for c in range(rgbacount):
            r = unpack("B", f.read(1))[0] / 127.0
            g = unpack("B", f.read(1))[0] / 127.0
            b = unpack("B", f.read(1))[0] / 127.0
            a = unpack("B", f.read(1))[0] / 127.0
            rgba.append([r,g,b,a])

        collection = bpy.data.collections.new(os.path.basename(os.path.splitext(filepath)[0]))
        bpy.context.scene.collection.children.link(collection)
        mesh = bpy.data.meshes.new(os.path.basename(os.path.splitext(filepath)[0]))
        mesh.from_pydata(vertices, [], faces)
        object = bpy.data.objects.new(os.path.basename(os.path.splitext(filepath)[0]), mesh)
        collection.objects.link(object)
            
        for fac in mesh.polygons:
            fac.use_smooth = True

        uv_tex = mesh.uv_layers.new()
        uv_layer = mesh.uv_layers[0].data
        vert_loops = {}
        for l in mesh.loops:
            vert_loops.setdefault(l.vertex_index, []).append(l.index)
        for i, coord in enumerate(uvs):
            for li in vert_loops[i]:
                uv_layer[li].uv = coord

        obj = bpy.data.objects[os.path.basename(os.path.splitext(filepath)[0])]
        bpy.context.view_layer.objects.active = obj

        colname = "GSC_VERTEXCOLORS"

        colattr = obj.data.color_attributes.new(
            name=colname,
            type='FLOAT_COLOR',
            domain='POINT',
        )

        for v_index in range(len(obj.data.vertices)):
            colattr.data[v_index].color = rgba[v_index]

def get_1stobjects_with_uvs_and_rgba(f, filepath):
    f.seek(0)
    fa=-1
    fb=0
    fc=1
    vertices=[]
    faces=[]
    normals=[]
    uvs=[]
    rgba=[]
    chunks=0
    paddingWhere=0
    firstOBJread = f.read()
    readobjfirst = firstOBJread.find(b"\x03\x01\x00\x01\x03\x80")
    if firstOBJread != 0:
        f.seek(readobjfirst,0)
        f.seek(6,1)
        vertexCount = unpack("b", f.read(1))[0]
        f.seek(1,1)
        for i in range(vertexCount):
            vx = unpack("<f", f.read(4))[0]
            vy = unpack("<f", f.read(4))[0]
            vz = unpack("<f", f.read(4))[0]
            vw = unpack("<f", f.read(4))[0]
            vertices.append([vx,vz,vy])
        for i in range(vertexCount-2):
            faces.append([i-i%2+1,i+i%2,i+2])
            faces.append([i+i%2,i-i%2+1,i+2])
        f.seek(6, 1)
        uvcount = unpack("B", f.read(1))[0]
        f.seek(1,1)
        for i in range(uvcount):
            ux = unpack("<h", f.read(2))[0] / 4096.0
            uy = unpack("<h", f.read(2))[0] / 4096.0
            f.seek(4,1)
            uvs.append([+ux,-uy])
        f.seek(6, 1)
        rgbacount = unpack("b", f.read(1))[0]
        f.seek(1,1)
        for c in range(rgbacount):
            r = unpack("B", f.read(1))[0] / 127.0
            g = unpack("B", f.read(1))[0] / 127.0
            b = unpack("B", f.read(1))[0] / 127.0
            a = unpack("B", f.read(1))[0] / 127.0
            rgba.append([r,g,b,a])

        collection = bpy.data.collections.new(os.path.basename(os.path.splitext(filepath)[0]))
        bpy.context.scene.collection.children.link(collection)
        mesh = bpy.data.meshes.new(os.path.basename(os.path.splitext(filepath)[0]))
        mesh.from_pydata(vertices, [], faces)
        object = bpy.data.objects.new(os.path.basename(os.path.splitext(filepath)[0]), mesh)
        collection.objects.link(object)
            
        for fac in mesh.polygons:
            fac.use_smooth = True

        uv_tex = mesh.uv_layers.new()
        uv_layer = mesh.uv_layers[0].data
        vert_loops = {}
        for l in mesh.loops:
            vert_loops.setdefault(l.vertex_index, []).append(l.index)
        for i, coord in enumerate(uvs):
            for li in vert_loops[i]:
                uv_layer[li].uv = coord

        obj = bpy.data.objects[os.path.basename(os.path.splitext(filepath)[0])]
        bpy.context.view_layer.objects.active = obj

        colname = "GSC_VERTEXCOLORS"

        colattr = obj.data.color_attributes.new(
            name=colname,
            type='FLOAT_COLOR',
            domain='POINT',
        )

        for v_index in range(len(obj.data.vertices)):
            colattr.data[v_index].color = rgba[v_index]

def ColorReach(f, rgba=[]):
    obdata = bpy.context.object.data
    f.seek(0)
    ColorRead = f.read()
    ColorFind = ColorRead.find(b"\x00\x05\x05\xC0")
    if ColorRead!=0:
        f.seek(ColorFind, 0)
        f.seek(4,1)
        ColCount = unpack("B", f.read(1))[0]
        ColCount_ = unpack("B", f.read(1))[0]
        for i in range(ColCount):
            red     = unpack("B", f.read(1))[0] / 127.0
            green   = unpack("B", f.read(1))[0] / 127.0
            blue    = unpack("B", f.read(1))[0] / 127.0
            alpha   = unpack("B", f.read(1))[0] / 127.0
            rgba.append([red,green,blue,alpha])

        obj = bpy.data.objects[os.path.basename(os.path.splitext(filepath)[0])]
        bpy.context.view_layer.objects.active = obj

        colname = "GSC_VERTEXCOLORS"

        colattr = obj.data.color_attributes.new(
            name=colname,
            type='FLOAT_COLOR',
            domain='POINT',
        )

        for v_index in range(len(obj.data.vertices)):
            colattr.data[v_index].color = rgba[v_index]

def DIFOffset_one(f, filepath):
    f.seek(0)
    vertices=[]
    faces=[]
    uvs=[]
    vcolors=[]
    fa=-1
    fb=0
    fc=1
    QTRead = f.read()
    QTLoc = QTRead.find(b"\x03\x01\x00\x01")
    if QTRead != 0:
        f.seek(QTLoc, 0)
        f.seek(4,1)
        flag1 = unpack("B", f.read(1))[0]
        if flag1 == 1:
            f.seek(5,1)
            VertexCount = unpack("B", f.read(1))[0]
            flag = unpack("B", f.read(1))[0]
            for j in range(VertexCount):
                vx = unpack("<h", f.read(2))[0] / 4096.0
                vy = unpack("<h", f.read(2))[0] / 4096.0
                vz = unpack("<h", f.read(2))[0] / 4096.0
                type4 = unpack("B", f.read(1))[0]==False
                value1 = unpack("B", f.read(1))[0]
                vertices.append([vx,vz,vy])
                fa+=1
                fb+=1
                fc+=1
                if type4 > 0:
                    faces.append([j+j+type4-type4-1+fa-j-j-1,j-j+type4-type4+1+fb-2-1,j+type4-type4+fc-j+2-4])
            uvcount = unpack("B", f.read(1))[0]
            if uvcount == 1:
               f.seek(2,1)
               f.seek(2,1)
               value1 = unpack("B", f.read(1))[0]
               uvcounts = unpack("B", f.read(1))[0]
               flag_1 = unpack("B", f.read(1))[0]
               if flag_1 == 0x6D:
                   for i in range(uvcounts):
                       uvx = unpack("<h", f.read(2))[0] / 4096
                       uvy = unpack("<h", f.read(2))[0] / 4096
                       f.seek(4,1)
                       uvs.append([+uvx,-uvy])
                   coloroffset = unpack("B", f.read(1))[0]
                   if coloroffset == 0:
                       f.seek(2,1)
                       f.seek(1,1)
                       offfset = unpack("B", f.read(1))[0]
                       if offfset == 5:
                           f.seek(1,1)
                           colorcount = unpack("B", f.read(1))[0]
                           flag_2 = unpack("B", f.read(1))[0]
                           if flag_2 == 0x6E:
                               for i in range(colorcount):
                                   r = unpack("B", f.read(1))[0] / 127
                                   g = unpack("B", f.read(1))[0] / 127
                                   b = unpack("B", f.read(1))[0] / 127
                                   a = unpack("B", f.read(1))[0] / 127
                                   vcolors.append([r,g,b,a])
                   elif coloroffset == 1:
                       f.seek(2,1)
                       f.seek(1,1)
                       offfset = unpack("B", f.read(1))[0]
                       if offfset == 5:
                           f.seek(1,1)
                           colorcount = unpack("B", f.read(1))[0]
                           flag_2 = unpack("B", f.read(1))[0]
                           if flag_2 == 0x6E:
                               for i in range(colorcount):
                                   r = unpack("B", f.read(1))[0] / 127
                                   g = unpack("B", f.read(1))[0] / 127
                                   b = unpack("B", f.read(1))[0] / 127
                                   a = unpack("B", f.read(1))[0] / 127
                                   vcolors.append([r,g,b,a])
               elif flag_1 == 0x65:
                   for i in range(uvcounts):
                       uvx = unpack("<h", f.read(2))[0] / 4096
                       uvy = unpack("<h", f.read(2))[0] / 4096
                       uvs.append([+uvx,-uvy])
                   coloroffset = unpack("B", f.read(1))[0]
                   if coloroffset == 0:
                       f.seek(2,1)
                       f.seek(1,1)
                       offfset = unpack("B", f.read(1))[0]
                       if offfset == 5:
                           f.seek(1,1)
                           colorcount = unpack("B", f.read(1))[0]
                           flag_2 = unpack("B", f.read(1))[0]
                           if flag_2 == 0x6E:
                               for i in range(colorcount):
                                   r = unpack("B", f.read(1))[0] / 127
                                   g = unpack("B", f.read(1))[0] / 127
                                   b = unpack("B", f.read(1))[0] / 127
                                   a = unpack("B", f.read(1))[0] / 127
                                   vcolors.append([r,g,b,a])
                   elif coloroffset == 1:
                       f.seek(2,1)
                       f.seek(1,1)
                       offfset = unpack("B", f.read(1))[0]
                       if offfset == 5:
                           f.seek(1,1)
                           colorcount = unpack("B", f.read(1))[0]
                           flag_2 = unpack("B", f.read(1))[0]
                           if flag_2 == 0x6E:
                               for i in range(colorcount):
                                   r = unpack("B", f.read(1))[0] / 127
                                   g = unpack("B", f.read(1))[0] / 127
                                   b = unpack("B", f.read(1))[0] / 127
                                   a = unpack("B", f.read(1))[0] / 127
                                   vcolors.append([r,g,b,a])
            elif uvcount == 4:
                flag_1 = unpack("B", f.read(1))[0]
                if flag_1 == 0x65:
                    for i in range(uvcount):
                        uvx = unpack("<h", f.read(1))[0] / 4096
                        uvy = unpack("<h", f.read(2))[0] / 4096
                        uvs.append([+uvx,-uvy])
                    coloroffset = unpack("B", f.read(1))[0]
                    if coloroffset == 0:
                        f.seek(2,1)
                        f.seek(1,1)
                        offfset = unpack("B", f.read(1))[0]
                        if offfset == 5:
                            f.seek(1,1)
                            colorcount = unpack("B", f.read(1))[0]
                            flag_2 = unpack("B", f.read(1))[0]
                            if flag_2 == 0x6E:
                                for i in range(colorcount):
                                    r = unpack("B", f.read(1))[0] / 127
                                    g = unpack("B", f.read(1))[0] / 127
                                    b = unpack("B", f.read(1))[0] / 127
                                    a = unpack("B", f.read(1))[0] / 127
                                    vcolors.append([r,g,b,a])
                    elif coloroffset == 1:
                        f.seek(2,1)
                        f.seek(1,1)
                        offfset = unpack("B", f.read(1))[0]
                        if offfset == 5:
                            f.seek(1,1)
                            colorcount = unpack("B", f.read(1))[0]
                            flag_2 = unpack("B", f.read(1))[0]
                            if flag_2 == 0x6E:
                                for i in range(colorcount):
                                    r = unpack("B", f.read(1))[0] / 127
                                    g = unpack("B", f.read(1))[0] / 127
                                    b = unpack("B", f.read(1))[0] / 127
                                    a = unpack("B", f.read(1))[0] / 127
                                    vcolors.append([r,g,b,a])
                elif flag_1 == 0x6D:
                    for i in range(uvcount):
                        uvx = unpack("<h", f.read(1))[0] / 4096
                        uvy = unpack("<h", f.read(2))[0] / 4096
                        f.seek(4,1)
                        uvs.append([+uvx,-uvy])
                    coloroffset = unpack("B", f.read(1))[0]
                    if coloroffset == 0:
                        f.seek(2,1)
                        f.seek(1,1)
                        offfset = unpack("B", f.read(1))[0]
                        if offfset == 5:
                            f.seek(1,1)
                            colorcount = unpack("B", f.read(1))[0]
                            flag_2 = unpack("B", f.read(1))[0]
                            if flag_2 == 0x6E:
                                for i in range(colorcount):
                                    r = unpack("B", f.read(1))[0] / 127
                                    g = unpack("B", f.read(1))[0] / 127
                                    b = unpack("B", f.read(1))[0] / 127
                                    a = unpack("B", f.read(1))[0] / 127
                                    vcolors.append([r,g,b,a])
                    elif coloroffset == 1:
                        f.seek(2,1)
                        f.seek(1,1)
                        offfset = unpack("B", f.read(1))[0]
                        if offfset == 5:
                            f.seek(1,1)
                            colorcount = unpack("B", f.read(1))[0]
                            flag_2 = unpack("B", f.read(1))[0]
                            if flag_2 == 0x6E:
                                for i in range(colorcount):
                                    r = unpack("B", f.read(1))[0] / 127
                                    g = unpack("B", f.read(1))[0] / 127
                                    b = unpack("B", f.read(1))[0] / 127
                                    a = unpack("B", f.read(1))[0] / 127
                                    vcolors.append([r,g,b,a])
                    
            elif uvcount == 0:
                f.seek(2,1)
                f.seek(2,1)
                value1 = unpack("B", f.read(1))[0]
                uvcounts = unpack("B", f.read(1))[0]
                flag_1 = unpack("B", f.read(1))[0]
                if flag_1 == 0x65:
                    for i in range(uvcounts):
                        
                        uvx = unpack("<h", f.read(2))[0] / 4096
                        uvy = unpack("<h", f.read(2))[0] / 4096
                        uvs.append([+uvx,-uvy])
                    coloroffset = unpack("B", f.read(1))[0]
                    if coloroffset == 0:
                        f.seek(2,1)
                        f.seek(1,1)
                        offfset = unpack("B", f.read(1))[0]
                        if offfset == 5:
                            f.seek(1,1)
                            colorcount = unpack("B", f.read(1))[0]
                            flag_2 = unpack("B", f.read(1))[0]
                            if flag_2 == 0x6E:
                                for i in range(colorcount):
                                    r = unpack("B", f.read(1))[0] / 127
                                    g = unpack("B", f.read(1))[0] / 127
                                    b = unpack("B", f.read(1))[0] / 127
                                    a = unpack("B", f.read(1))[0] / 127
                                    vcolors.append([r,g,b,a])
                    elif coloroffset == 1:
                        f.seek(2,1)
                        f.seek(1,1)
                        offfset = unpack("B", f.read(1))[0]
                        if offfset == 5:
                            f.seek(1,1)
                            colorcount = unpack("B", f.read(1))[0]
                            flag_2 = unpack("B", f.read(1))[0]
                            if flag_2 == 0x6E:
                                for i in range(colorcount):
                                    r = unpack("B", f.read(1))[0] / 127
                                    g = unpack("B", f.read(1))[0] / 127
                                    b = unpack("B", f.read(1))[0] / 127
                                    a = unpack("B", f.read(1))[0] / 127
                                    vcolors.append([r,g,b,a])
                    elif coloroffset == 5:
                        f.seek(1,1)
                        colorcount = unpack("B", f.read(1))[0]
                        flag_2 = unpack("B", f.read(1))[0]
                        if flag_2 == 0x6E:
                            for i in range(colorcount):
                                r = unpack("B", f.read(1))[0] / 127
                                g = unpack("B", f.read(1))[0] / 127
                                b = unpack("B", f.read(1))[0] / 127
                                a = unpack("B", f.read(1))[0] / 127
                                vcolors.append([r,g,b,a])
                elif flag_1 == 0x6D:
                    for i in range(uvcounts):
                        uvx = unpack("<h", f.read(2))[0] / 4096
                        uvy = unpack("<h", f.read(2))[0] / 4096
                        f.seek(4,1)
                        uvs.append([+uvx,-uvy])
                    coloroffset = unpack("B", f.read(1))[0]
                    if coloroffset == 0:
                        f.seek(2,1)
                        f.seek(1,1)
                        offfset = unpack("B", f.read(1))[0]
                        if offfset == 5:
                            f.seek(1,1)
                            colorcount = unpack("B", f.read(1))[0]
                            flag_2 = unpack("B", f.read(1))[0]
                            if flag_2 == 0x6E:
                                for i in range(colorcount):
                                    r = unpack("B", f.read(1))[0] / 127
                                    g = unpack("B", f.read(1))[0] / 127
                                    b = unpack("B", f.read(1))[0] / 127
                                    a = unpack("B", f.read(1))[0] / 127
                                    vcolors.append([r,g,b,a])
                    elif coloroffset == 1:
                        f.seek(2,1)
                        f.seek(1,1)
                        offfset = unpack("B", f.read(1))[0]
                        if offfset == 5:
                            f.seek(1,1)
                            colorcount = unpack("B", f.read(1))[0]
                            flag_2 = unpack("B", f.read(1))[0]
                            if flag_2 == 0x6E:
                                for i in range(colorcount):
                                    r = unpack("B", f.read(1))[0] / 127
                                    g = unpack("B", f.read(1))[0] / 127
                                    b = unpack("B", f.read(1))[0] / 127
                                    a = unpack("B", f.read(1))[0] / 127
                                    vcolors.append([r,g,b,a])
                    elif coloroffset == 5:
                        f.seek(1,1)
                        colorcount = unpack("B", f.read(1))[0]
                        flag_2 = unpack("B", f.read(1))[0]
                        if flag_2 == 0x6E:
                            for i in range(colorcount):
                                r = unpack("B", f.read(1))[0] / 127
                                g = unpack("B", f.read(1))[0] / 127
                                b = unpack("B", f.read(1))[0] / 127
                                a = unpack("B", f.read(1))[0] / 127
                                vcolors.append([r,g,b,a])
                                        

    if flag == 0x6D:
        

        collection = bpy.data.collections.new(os.path.basename(os.path.splitext(filepath)[0]))
        bpy.context.scene.collection.children.link(collection)
        mesh = bpy.data.meshes.new(os.path.basename(os.path.splitext(filepath)[0]))
        mesh.from_pydata(vertices, [], faces)
        obj = bpy.data.objects.new(os.path.basename(os.path.splitext(filepath)[0]), mesh)
        collection.objects.link(obj)

        for fac in mesh.polygons:
            fac.use_smooth = True

        if flag_1 == 0x6D or 0x65:

            uv_tex = mesh.uv_layers.new()
            uv_layer = mesh.uv_layers[0].data
            vert_loops = {}
            for l in mesh.loops:
                vert_loops.setdefault(l.vertex_index, []).append(l.index)
            for i, coord in enumerate(uvs):
                for li in vert_loops[i]:
                    uv_layer[li].uv = coord
                    
            if flag_2 == 0x6E:
                bpy.context.view_layer.objects.active = obj

                colname = "GSC_VERTEXCOLORS"

                colattr = obj.data.color_attributes.new(
                    name=colname,
                    type='FLOAT_COLOR',
                    domain='POINT',
                )

                for v_index in range(len(obj.data.vertices)):
                    colattr.data[v_index].color = vcolors[v_index]

def BatchHashVertexColor1(f, filepath):

    vertices=[]
    faces=[]
    normals=[]
    uvs=[]
    rgba=[]

    fa=-1
    fb=0
    fc=1
    f.seek(0)
    
    while 1:
        Chunk = f.read(4)
        if Chunk == b"NU20":
            negativefilesize = unpack("<I", f.read(4))[0]
            primtype = unpack("<I", f.read(4))[0]
            unk = unpack("<I", f.read(4))[0]
        elif Chunk == b"NTBL":
            NTBLSize1 = unpack("<I", f.read(4))[0]
            NTBLSize2 = unpack("<I", f.read(4))[0]
            f.seek(NTBLSize1-12,1)
        elif Chunk == b"\x03\x01\x00\x01":
            f.seek(2,1)
            vertexCount = unpack("B", f.read(1))[0]
            f.seek(1,1)
            for i in range(vertexCount):
                type1 = unpack("<f", f.read(4))[0]
                type2 = unpack("<f", f.read(4))[0]
                type3 = unpack("<f", f.read(4))[0]
                nz = unpack("<f", f.read(4))[0]
                
                
                
                vertices.append([type1,type2,type3])
                normals.append([0,0,nz])

            for i in range(vertexCount-2):
                fa+=1
                fb+=1
                fc+=1
                faces.append([fa,fb,fc])

            f.seek(6, 1)
            uvcount = unpack("b", f.read(1))[0]
            f.seek(1,1)
            for i in range(uvcount):
                ux = unpack("<h", f.read(2))[0] / 4096.0
                uy = unpack("<h", f.read(2))[0] / 4096.0
                f.seek(4,1)
                uvs.append([+ux,-uy])
            f.seek(6,1)
            ColCount = unpack("B", f.read(1))[0]
            ColCount_ = unpack("B", f.read(1))[0]
            for i in range(ColCount):
                red     = unpack("B", f.read(1))[0] / 127.0
                green   = unpack("B", f.read(1))[0] / 127.0
                blue    = unpack("B", f.read(1))[0] / 127.0
                alpha   = unpack("B", f.read(1))[0] / 127.0
                rgba.append([red,green,blue,alpha])
        elif Chunk == b"SST0":
            break

    obj = bpy.data.objects[os.path.basename(os.path.splitext(filepath)[0])]
    bpy.context.view_layer.objects.active = obj

    colname = "GSC_VERTEXCOLORS"

    colattr = obj.data.color_attributes.new(
        name=colname,
        type='FLOAT_COLOR',
        domain='POINT',
    )

    for v_index in range(len(obj.data.vertices)):
        colattr.data[v_index].color = rgba[v_index]

def BatchUVS1(f, vertices=[], faces=[], normals=[], uvs=[], rgba=[], fa=-1, fb=0, fc=1):
    f.seek(0)
    obdata = bpy.context.object.data
    while 1:
        Chunk = f.read(4)
        if Chunk == b"NU20":
            negativefilesize = unpack("<I", f.read(4))[0]
            primtype = unpack("<I", f.read(4))[0]
            unk = unpack("<I", f.read(4))[0]
        elif Chunk == b"NTBL":
            NTBLSize1 = unpack("<I", f.read(4))[0]
            NTBLSize2 = unpack("<I", f.read(4))[0]
            f.seek(NTBLSize1-12,1)
        elif Chunk == b"\x03\x01\x00\x01":
            f.seek(2,1)
            vertexCount = unpack("B", f.read(1))[0]
            f.seek(1,1)
            for i in range(vertexCount):
                type1 = unpack("<f", f.read(4))[0]
                type2 = unpack("<f", f.read(4))[0]
                type3 = unpack("<f", f.read(4))[0]
                nz = unpack("<f", f.read(4))[0]
                
                
                
                vertices.append([type1,type2,type3])
                normals.append([0,0,nz])

            for i in range(vertexCount-2):
                fa+=1
                fb+=1
                fc+=1
                faces.append([fa,fb,fc])

            f.seek(6, 1)
            uvcount = unpack("b", f.read(1))[0]
            f.seek(1,1)
            for i in range(uvcount):
                ux = unpack("<h", f.read(2))[0] / 4096.0
                uy = unpack("<h", f.read(2))[0] / 4096.0
                f.seek(4,1)
                uvs.append([+ux,-uy])
            f.seek(6,1)
            ColCount = unpack("B", f.read(1))[0]
            ColCount_ = unpack("B", f.read(1))[0]
            for i in range(ColCount):
                red     = unpack("B", f.read(1))[0] / 127.0
                green   = unpack("B", f.read(1))[0] / 127.0
                blue    = unpack("B", f.read(1))[0] / 127.0
                alpha   = unpack("B", f.read(1))[0] / 127.0
                rgba.append([red,green,blue,alpha])
        elif Chunk == b"SST0":
            break

    uv_tex = obdata.uv_layers.new()
    uv_layer = obdata.uv_layers[0].data
    vert_loops = {}
    for l in obdata.loops:
        vert_loops.setdefault(l.vertex_index, []).append(l.index)
    for i, coord in enumerate(uvs):
        for li in vert_loops[i]:
            uv_layer[li].uv = coord

def selectUVFourth(f, uvs=[]):
    f.seek(0)
    uvthirdmatchread = f.read()
    uvthifind = uvthirdmatchread.find(b"\x03\x01\x00\x01\x03\x80")
    #match this offset to get the uv target since it's not possible with this offset
    if uvthirdmatchread != 0:
        f.seek(uvthifind, 0)
        f.seek(6, 1)
        vertexcount = unpack("B", f.read(1))[0]
        f.seek(1,1)
        for i in range(vertexcount):
            f.seek(4, 1)
            f.seek(4, 1)
            f.seek(4, 1)
            f.seek(4, 1)
        f.seek(2, 1)
        uvcount = unpack("B", f.read(1))[0]
        f.seek(1,1)
        for i in range(uvcount):
            ux = unpack("<h", f.read(2))[0] / 4096.0
            uy = unpack("<h", f.read(2))[0] / 4096.0
            f.seek(4,1)
            uvs.append([+ux,-uy])
        obdata = bpy.context.object.data
        uv_tex = obdata.uv_layers.new()
        uv_layer = obdata.uv_layers[0].data
        vert_loops = {}
        for l in obdata.loops:
            vert_loops.setdefault(l.vertex_index, []).append(l.index)
        for i, coord in enumerate(uvs):
            for li in vert_loops[i]:
                uv_layer[li].uv = coord
    #some or most 0x0480XX6D

def selectUVThird(f, uvs=[]):
    f.seek(0)
    uvthirdmatchread = f.read()
    uvthifind = uvthirdmatchread.find(b"\x03\x01\x00\x01\x03\x80")
    #match this offset to get the uv target since it's not possible with this offset
    if uvthirdmatchread != 0:
        f.seek(uvthifind, 0)
        f.seek(6, 1)
        vertexcount = unpack("b", f.read(1))[0]
        f.seek(1,1)
        for i in range(vertexcount):
            f.seek(4, 1)
            f.seek(4, 1)
            f.seek(4, 1)
            f.seek(4, 1)
        f.seek(2, 1)
        uvcount = unpack("b", f.read(1))[0]
        f.seek(1,1)
        for i in range(uvcount):
            ux = unpack("<h", f.read(2))[0] / 4096.0
            uy = unpack("<h", f.read(2))[0] / 4096.0
            uvs.append([+ux,-uy])
        obdata = bpy.context.object.data
        uv_tex = obdata.uv_layers.new()
        uv_layer = obdata.uv_layers[0].data
        vert_loops = {}
        for l in obdata.loops:
            vert_loops.setdefault(l.vertex_index, []).append(l.index)
        for i, coord in enumerate(uvs):
            for li in vert_loops[i]:
                uv_layer[li].uv = coord
    #whale chase mouth 0x0480XX65

def select2ndUV(f, uvs=[]):

    f.seek(0)
    uvsecondread = f.read()
    uvsecondfind = uvsecondread.find(b"\x01\x00\x00\x05\x04\x80")
    if uvsecondread != 0:
        f.seek(uvsecondfind, 0)
        f.seek(6, 1)
        uvcount = unpack("b", f.read(1))[0]
        f.seek(1,1) #0x65 in a row
        for i in range(uvcount):
            ux = unpack("<h", f.read(2))[0] / 4096.0
            uy = unpack("<h", f.read(2))[0] / 4096.0
            uvs.append([+ux,-uy])
        obdata = bpy.context.object.data
        uv_tex = obdata.uv_layers.new()
        uv_layer = obdata.uv_layers[0].data
        vert_loops = {}
        for l in obdata.loops:
            vert_loops.setdefault(l.vertex_index, []).append(l.index)
        for i, coord in enumerate(uvs):
            for li in vert_loops[i]:
                uv_layer[li].uv = coord
        

def selectUV(f, uvs=[]):

    f.seek(0)
    uvfirstread = f.read()
    uvfirstfind = uvfirstread.find(b"\x01\x00\x00\x05\x04\x80")
    if uvfirstread != 0:
        f.seek(uvfirstfind, 0)
        f.seek(6, 1)
        uvcount = unpack("b", f.read(1))[0]
        f.seek(1,1)
        for i in range(uvcount):
            ux = unpack("<h", f.read(2))[0] / 4096.0
            uy = unpack("<h", f.read(2))[0] / 4096.0
            f.seek(4, 1)
            uvs.append([+ux,-uy])
        obdata = bpy.context.object.data
        uv_tex = obdata.uv_layers.new()
        uv_layer = obdata.uv_layers[0].data
        vert_loops = {}
        for l in obdata.loops:
            vert_loops.setdefault(l.vertex_index, []).append(l.index)
        for i, coord in enumerate(uvs):
            for li in vert_loops[i]:
                uv_layer[li].uv = coord
    

def get_1stobjects(f, filepath):
    fa=-1
    fb=0
    fc=1
    vertices=[]
    faces=[]
    uvs=[]
    rgba=[]
    f.seek(0)
    firstOBJread = f.read()
    readobjfirst = firstOBJread.find(b"\x03\x01\x00\x01\x03\x80")
    if firstOBJread != 0:
        f.seek(readobjfirst,0)
        f.seek(6,1)
        vertexCount = unpack("B", f.read(1))[0]
        flags = unpack("B", f.read(1))[0]
        if flags == 0x6C:
            
            for j in range(vertexCount):
                vx = unpack("<f", f.read(4))[0]
                vy = unpack("<f", f.read(4))[0]
                vz = unpack("<f", f.read(4))[0]
                type4 = unpack("B", f.read(1))[0]==False
                value1 = unpack("B", f.read(1))[0]
                f.seek(2,1)
                fa+=1
                fb+=1
                fc+=1
                vertices.append([vx,vz,vy])
                if type4 > 0:
                    faces.append([j+j+type4-type4-1+fa-j-j-1,j-j+type4-type4+1+fb-2-1,j+type4-type4+fc-j+2-4])
            
        collection = bpy.data.collections.new(os.path.basename(os.path.splitext(filepath)[0]))
        bpy.context.scene.collection.children.link(collection)
        mesh = bpy.data.meshes.new(os.path.basename(os.path.splitext(filepath)[0]))
        mesh.from_pydata(vertices, [], faces)
        object = bpy.data.objects.new(os.path.basename(os.path.splitext(filepath)[0]), mesh)
        collection.objects.link(object)
            
        for fac in mesh.polygons:
            fac.use_smooth = True

def get_SPEC(f, emptytime2=[]):
    f.seek(0)
    SPECread = f.read()
    SPECfound = SPECread.find(b"\x53\x50\x45\x43")
    if SPECread != 0:
        f.seek(SPECfound,0)
        SPECS = unpack("<i", f.read(4))[0]
        SPECSsize = unpack("<i", f.read(4))[0]
        SPECcount = unpack("<i", f.read(4))[0]
        unk01 = unpack("<i", f.read(4))[0]
        for i in range(SPECcount):
            SPECScaleX = unpack("<f", f.read(4))[0]
            f.seek(16,1)
            SPECScaleY = unpack("<f", f.read(4))[0]
            f.seek(16,1)
            SPECScaleZ = unpack("<f", f.read(4))[0]
            f.seek(4,1)
            SPECxTrans = unpack("<f", f.read(4))[0]
            SPECyTrans = unpack("<f", f.read(4))[0]
            SPECzTrans = unpack("<f", f.read(4))[0]
            SPECUNKFloat = unpack("<f", f.read(4))[0]
            f.seek(16, 1)
            bpy.ops.object.empty_add(type='CUBE', align='WORLD', location=([SPECxTrans, SPECzTrans,SPECyTrans]), scale=([SPECScaleX, SPECScaleY, SPECScaleZ]))

def get_SPEC_ANIMATION_BLOCK(f, emptytime3=[]):
    f.seek(0)
    IABLread = f.read()
    IABLsearch = IABLread.find(b"\x49\x41\x42\x4C")
    if IABLread != 0:
        f.seek(IABLsearch,0)
        IABLS_ram = unpack("<i", f.read(4))[0]
        IABLS_size = unpack("<i", f.read(4))[0]
        IABLcount = unpack("<i", f.read(4))[0]
        unk01 = unpack("<i", f.read(4))[0]
        for i in range(IABLcount):
            IABLScaleX = unpack("<f", f.read(4))[0]
            f.seek(16,1)
            IABLScaleY = unpack("<f", f.read(4))[0]
            f.seek(16,1)
            IABLScaleZ = unpack("<f", f.read(4))[0]
            f.seek(4,1)
            IABLxTrans = unpack("<f", f.read(4))[0]
            IABLyTrans = unpack("<f", f.read(4))[0]
            IABLzTrans = unpack("<f", f.read(4))[0]
            IABLUNKFloat = unpack("<f", f.read(4))[0]
            f.seek(32, 1)
            bpy.ops.object.empty_add(type='CUBE', align='WORLD', location=([IABLxTrans, IABLzTrans,IABLyTrans]), scale=([IABLScaleX, IABLScaleY, IABLScaleZ]))
            
        
        

def parse_gsc(filepath, pointOne=False, Triangle_Strips_with_uvs_and_rgba=1, Triangle_StripsTwo=False, Triangle_Strips=False, ONE_CHUNK_OFFSET1=False, SST=False, SPEC=False, INST_prim=False,INST_seco=False, IABL=False, BoundingSet=False, ALIB=False, SelectOnlyUVMesh=False, SelectOnly2ndUVMesh=False, SelectOnly3rdUVMesh=False, SelectOnly4thUVMesh=False,BatchHashVertexColors=False, BatchUVSS=False, RGBAColors=False):
    with open(filepath, "rb") as f:
        if Triangle_Strips:
            wholeChunk1_none(f, filepath)
        if ONE_CHUNK_OFFSET1:
            get_1stobjects(f, filepath)
        if INST_prim:
            get_INST_1st(f)
        if INST_seco:
            get_INST_2nd(f)
        if SPEC:
            get_SPEC(f, emptytime2=[])
        if IABL:
            get_SPEC_ANIMATION_BLOCK(f, emptytime3=[])
        if SST:
            get_splineset(f)
        if ALIB:
           get_Animation_LIBRARY(f) 
        if SelectOnlyUVMesh:
            selectUV(f, uvs=[])
        if SelectOnly2ndUVMesh:
            select2ndUV(f, uvs=[])
        if SelectOnly3rdUVMesh:
            selectUVThird(f, uvs=[])
        if SelectOnly4thUVMesh:
            selectUVFourth(f, uvs=[])
        if BoundingSet:
            get_BoundsSet1(f)
        if BatchHashVertexColors:
            BatchHashVertexColor1(f, filepath)
        if Triangle_StripsTwo:
            DIFOffset_one(f, filepath)
        if RGBAColors:
            ColorReach(f, colors=[])
        if Triangle_Strips_with_uvs_and_rgba == 1:
            get_1stobjects_with_uvs_and_rgba(f, filepath)
        if Triangle_Strips_with_uvs_and_rgba == 2:
            get_2ndobjects_with_uvs_and_rgba(f, filepath)
        if Triangle_Strips_with_uvs_and_rgba == 3:
            get_3rdobjects_with_uvs_and_rgba(f, filepath)
        if Triangle_Strips_with_uvs_and_rgba == 4:
            get_4thobjects_with_uvs_and_rgba(f, filepath)
        if Triangle_Strips_with_uvs_and_rgba == 5:
            get_5thobjects_with_uvs_and_rgba(f, filepath)

        if BatchUVSS:
            BatchUVS1(f, vertices=[], faces=[], normals=[], uvs=[], rgba=[], fa=-1, fb=0, fc=1)

        if pointOne:
            one_point(f, filepath)
                



