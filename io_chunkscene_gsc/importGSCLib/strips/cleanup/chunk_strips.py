from struct import unpack, pack
import os
import bpy
import math
#from io import BytesIO as bio

#TODO



def wholeChunk1_none(f, filepath):
    vertices=[]
    normals=[]
    uvs=[]
    vcolors=[]
    faces=[]
    materialsOBJ=[]
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
                if vertexCount == 0:
                    pass        
                elif vertexCount == 1:
                    pass
                elif vertexCount == 2:
                    pass
                elif vertexCount == 3:
                    
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
                        vertices.append([vx1,vz1,vy1])
                        vertices.append([vx2,vz2,vy2])
                        vertices.append([vx3,vz3,vy3])
                                                            

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
                        vertices.append([vx9,vz9,vy9])
                        vertices.append([vx10,vz10,vy10])
                        vertices.append([vx11,vz11,vy11])
                        vertices.append([vx12,vz12,vy12])
                        vertices.append([vx13,vz13,vy13])

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

                elif vertexCount == 19:
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
                        vx168 = unpack("<f", f.read(4))[0]
                        vy168 = unpack("<f", f.read(4))[0]
                        vz168 = unpack("<f", f.read(4))[0]
                        type168 = unpack("B", f.read(1))[0]
                        value1a168 = unpack("B", f.read(1))[0]
                        normalZ_168 = unpack("<h", f.read(2))[0]
                        vx169 = unpack("<f", f.read(4))[0]
                        vy169 = unpack("<f", f.read(4))[0]
                        vz169 = unpack("<f", f.read(4))[0]
                        type169 = unpack("B", f.read(1))[0]
                        value1a169 = unpack("B", f.read(1))[0]
                        normalZ_169 = unpack("<h", f.read(2))[0]
                        vx170 = unpack("<f", f.read(4))[0]
                        vy170 = unpack("<f", f.read(4))[0]
                        vz170 = unpack("<f", f.read(4))[0]
                        type170 = unpack("B", f.read(1))[0]
                        value1a170 = unpack("B", f.read(1))[0]
                        normalZ_170 = unpack("<h", f.read(2))[0]
                        vx171 = unpack("<f", f.read(4))[0]
                        vy171 = unpack("<f", f.read(4))[0]
                        vz171 = unpack("<f", f.read(4))[0]
                        type171 = unpack("B", f.read(1))[0]
                        value1a171 = unpack("B", f.read(1))[0]
                        normalZ_171 = unpack("<h", f.read(2))[0]
                        vx172 = unpack("<f", f.read(4))[0]
                        vy172 = unpack("<f", f.read(4))[0]
                        vz172 = unpack("<f", f.read(4))[0]
                        type172 = unpack("B", f.read(1))[0]
                        value1a172 = unpack("B", f.read(1))[0]
                        normalZ_172 = unpack("<h", f.read(2))[0]
                        vx173 = unpack("<f", f.read(4))[0]
                        vy173 = unpack("<f", f.read(4))[0]
                        vz173 = unpack("<f", f.read(4))[0]
                        type173 = unpack("B", f.read(1))[0]
                        value1a173 = unpack("B", f.read(1))[0]
                        normalZ_173 = unpack("<h", f.read(2))[0]
                        vx174 = unpack("<f", f.read(4))[0]
                        vy174 = unpack("<f", f.read(4))[0]
                        vz174 = unpack("<f", f.read(4))[0]
                        type174 = unpack("B", f.read(1))[0]
                        value1a174 = unpack("B", f.read(1))[0]
                        normalZ_174 = unpack("<h", f.read(2))[0]
                        vx175 = unpack("<f", f.read(4))[0]
                        vy175 = unpack("<f", f.read(4))[0]
                        vz175 = unpack("<f", f.read(4))[0]
                        type175 = unpack("B", f.read(1))[0]
                        value1a175 = unpack("B", f.read(1))[0]
                        normalZ_175 = unpack("<h", f.read(2))[0]
                        vx176 = unpack("<f", f.read(4))[0]
                        vy176 = unpack("<f", f.read(4))[0]
                        vz176 = unpack("<f", f.read(4))[0]
                        type176 = unpack("B", f.read(1))[0]
                        value1a176 = unpack("B", f.read(1))[0]
                        normalZ_176 = unpack("<h", f.read(2))[0]
                        vx177 = unpack("<f", f.read(4))[0]
                        vy177 = unpack("<f", f.read(4))[0]
                        vz177 = unpack("<f", f.read(4))[0]
                        type177 = unpack("B", f.read(1))[0]
                        value1a177 = unpack("B", f.read(1))[0]
                        normalZ_177 = unpack("<h", f.read(2))[0]
                        vx178 = unpack("<f", f.read(4))[0]
                        vy178 = unpack("<f", f.read(4))[0]
                        vz178 = unpack("<f", f.read(4))[0]
                        type178 = unpack("B", f.read(1))[0]
                        value1a178 = unpack("B", f.read(1))[0]
                        normalZ_178 = unpack("<h", f.read(2))[0]
                        vx179 = unpack("<f", f.read(4))[0]
                        vy179 = unpack("<f", f.read(4))[0]
                        vz179 = unpack("<f", f.read(4))[0]
                        type179 = unpack("B", f.read(1))[0]
                        value1a179 = unpack("B", f.read(1))[0]
                        normalZ_179 = unpack("<h", f.read(2))[0]
                        vx180 = unpack("<f", f.read(4))[0]
                        vy180 = unpack("<f", f.read(4))[0]
                        vz180 = unpack("<f", f.read(4))[0]
                        type180 = unpack("B", f.read(1))[0]
                        value1a180 = unpack("B", f.read(1))[0]
                        normalZ_180 = unpack("<h", f.read(2))[0]
                        vx181 = unpack("<f", f.read(4))[0]
                        vy181 = unpack("<f", f.read(4))[0]
                        vz181 = unpack("<f", f.read(4))[0]
                        type181 = unpack("B", f.read(1))[0]
                        value1a181 = unpack("B", f.read(1))[0]
                        normalZ_181 = unpack("<h", f.read(2))[0]
                        vx182 = unpack("<f", f.read(4))[0]
                        vy182 = unpack("<f", f.read(4))[0]
                        vz182 = unpack("<f", f.read(4))[0]
                        type182 = unpack("B", f.read(1))[0]
                        value1a182 = unpack("B", f.read(1))[0]
                        normalZ_182 = unpack("<h", f.read(2))[0]
                        vx183 = unpack("<f", f.read(4))[0]
                        vy183 = unpack("<f", f.read(4))[0]
                        vz183 = unpack("<f", f.read(4))[0]
                        type183 = unpack("B", f.read(1))[0]
                        value1a183 = unpack("B", f.read(1))[0]
                        normalZ_183 = unpack("<h", f.read(2))[0]
                        vx184 = unpack("<f", f.read(4))[0]
                        vy184 = unpack("<f", f.read(4))[0]
                        vz184 = unpack("<f", f.read(4))[0]
                        type184 = unpack("B", f.read(1))[0]
                        value1a184 = unpack("B", f.read(1))[0]
                        normalZ_184 = unpack("<h", f.read(2))[0]
                        vx185 = unpack("<f", f.read(4))[0]
                        vy185 = unpack("<f", f.read(4))[0]
                        vz185 = unpack("<f", f.read(4))[0]
                        type185 = unpack("B", f.read(1))[0]
                        value1a185 = unpack("B", f.read(1))[0]
                        normalZ_185 = unpack("<h", f.read(2))[0]
                        vx186 = unpack("<f", f.read(4))[0]
                        vy186 = unpack("<f", f.read(4))[0]
                        vz186 = unpack("<f", f.read(4))[0]
                        type186 = unpack("B", f.read(1))[0]
                        value1a186 = unpack("B", f.read(1))[0]
                        normalZ_186 = unpack("<h", f.read(2))[0]
                        vertices.append([vx168,vz168,vy168])
                        vertices.append([vx169,vz169,vy169])
                        vertices.append([vx170,vz170,vy170])
                        vertices.append([vx171,vz171,vy171])
                        vertices.append([vx172,vz172,vy172])
                        vertices.append([vx173,vz173,vy173])
                        vertices.append([vx174,vz174,vy174])
                        vertices.append([vx175,vz175,vy175])
                        vertices.append([vx176,vz176,vy176])
                        vertices.append([vx177,vz177,vy177])
                        vertices.append([vx178,vz178,vy178])
                        vertices.append([vx179,vz179,vy179])
                        vertices.append([vx180,vz180,vy180])
                        vertices.append([vx181,vz181,vy181])
                        vertices.append([vx182,vz182,vy182])
                        vertices.append([vx183,vz183,vy183])
                        vertices.append([vx184,vz184,vy184])
                        vertices.append([vx185,vz185,vy185])
                        vertices.append([vx186,vz186,vy186])

                elif vertexCount == 20:
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
                        vx187 = unpack("<f", f.read(4))[0]
                        vy187 = unpack("<f", f.read(4))[0]
                        vz187 = unpack("<f", f.read(4))[0]
                        type187 = unpack("B", f.read(1))[0]
                        value1a187 = unpack("B", f.read(1))[0]
                        normalZ_187 = unpack("<h", f.read(2))[0]
                        vx188 = unpack("<f", f.read(4))[0]
                        vy188 = unpack("<f", f.read(4))[0]
                        vz188 = unpack("<f", f.read(4))[0]
                        type188 = unpack("B", f.read(1))[0]
                        value1a188 = unpack("B", f.read(1))[0]
                        normalZ_188 = unpack("<h", f.read(2))[0]
                        vx189 = unpack("<f", f.read(4))[0]
                        vy189 = unpack("<f", f.read(4))[0]
                        vz189 = unpack("<f", f.read(4))[0]
                        type189 = unpack("B", f.read(1))[0]
                        value1a189 = unpack("B", f.read(1))[0]
                        normalZ_189 = unpack("<h", f.read(2))[0]
                        vx190 = unpack("<f", f.read(4))[0]
                        vy190 = unpack("<f", f.read(4))[0]
                        vz190 = unpack("<f", f.read(4))[0]
                        type190 = unpack("B", f.read(1))[0]
                        value1a190 = unpack("B", f.read(1))[0]
                        normalZ_190 = unpack("<h", f.read(2))[0]
                        vx191 = unpack("<f", f.read(4))[0]
                        vy191 = unpack("<f", f.read(4))[0]
                        vz191 = unpack("<f", f.read(4))[0]
                        type191 = unpack("B", f.read(1))[0]
                        value1a191 = unpack("B", f.read(1))[0]
                        normalZ_191 = unpack("<h", f.read(2))[0]
                        vx192 = unpack("<f", f.read(4))[0]
                        vy192 = unpack("<f", f.read(4))[0]
                        vz192 = unpack("<f", f.read(4))[0]
                        type192 = unpack("B", f.read(1))[0]
                        value1a192 = unpack("B", f.read(1))[0]
                        normalZ_192 = unpack("<h", f.read(2))[0]
                        vx193 = unpack("<f", f.read(4))[0]
                        vy193 = unpack("<f", f.read(4))[0]
                        vz193 = unpack("<f", f.read(4))[0]
                        type193 = unpack("B", f.read(1))[0]
                        value1a193 = unpack("B", f.read(1))[0]
                        normalZ_193 = unpack("<h", f.read(2))[0]
                        vx194 = unpack("<f", f.read(4))[0]
                        vy194 = unpack("<f", f.read(4))[0]
                        vz194 = unpack("<f", f.read(4))[0]
                        type194 = unpack("B", f.read(1))[0]
                        value1a194 = unpack("B", f.read(1))[0]
                        normalZ_194 = unpack("<h", f.read(2))[0]
                        vx195 = unpack("<f", f.read(4))[0]
                        vy195 = unpack("<f", f.read(4))[0]
                        vz195 = unpack("<f", f.read(4))[0]
                        type195 = unpack("B", f.read(1))[0]
                        value1a195 = unpack("B", f.read(1))[0]
                        normalZ_195 = unpack("<h", f.read(2))[0]
                        vx196 = unpack("<f", f.read(4))[0]
                        vy196 = unpack("<f", f.read(4))[0]
                        vz196 = unpack("<f", f.read(4))[0]
                        type196 = unpack("B", f.read(1))[0]
                        value1a196 = unpack("B", f.read(1))[0]
                        normalZ_196 = unpack("<h", f.read(2))[0]
                        vx197 = unpack("<f", f.read(4))[0]
                        vy197 = unpack("<f", f.read(4))[0]
                        vz197 = unpack("<f", f.read(4))[0]
                        type197 = unpack("B", f.read(1))[0]
                        value1a197 = unpack("B", f.read(1))[0]
                        normalZ_197 = unpack("<h", f.read(2))[0]
                        vx198 = unpack("<f", f.read(4))[0]
                        vy198 = unpack("<f", f.read(4))[0]
                        vz198 = unpack("<f", f.read(4))[0]
                        type198 = unpack("B", f.read(1))[0]
                        value1a198 = unpack("B", f.read(1))[0]
                        normalZ_198 = unpack("<h", f.read(2))[0]
                        vx199 = unpack("<f", f.read(4))[0]
                        vy199 = unpack("<f", f.read(4))[0]
                        vz199 = unpack("<f", f.read(4))[0]
                        type199 = unpack("B", f.read(1))[0]
                        value1a199 = unpack("B", f.read(1))[0]
                        normalZ_199 = unpack("<h", f.read(2))[0]
                        vx200 = unpack("<f", f.read(4))[0]
                        vy200 = unpack("<f", f.read(4))[0]
                        vz200 = unpack("<f", f.read(4))[0]
                        type200 = unpack("B", f.read(1))[0]
                        value1a200 = unpack("B", f.read(1))[0]
                        normalZ_200 = unpack("<h", f.read(2))[0]
                        vx201 = unpack("<f", f.read(4))[0]
                        vy201 = unpack("<f", f.read(4))[0]
                        vz201 = unpack("<f", f.read(4))[0]
                        type201 = unpack("B", f.read(1))[0]
                        value1a201 = unpack("B", f.read(1))[0]
                        normalZ_201 = unpack("<h", f.read(2))[0]
                        vx202 = unpack("<f", f.read(4))[0]
                        vy202 = unpack("<f", f.read(4))[0]
                        vz202 = unpack("<f", f.read(4))[0]
                        type202 = unpack("B", f.read(1))[0]
                        value1a202 = unpack("B", f.read(1))[0]
                        normalZ_202 = unpack("<h", f.read(2))[0]
                        vx203 = unpack("<f", f.read(4))[0]
                        vy203 = unpack("<f", f.read(4))[0]
                        vz203 = unpack("<f", f.read(4))[0]
                        type203 = unpack("B", f.read(1))[0]
                        value1a203 = unpack("B", f.read(1))[0]
                        normalZ_203 = unpack("<h", f.read(2))[0]
                        vx204 = unpack("<f", f.read(4))[0]
                        vy204 = unpack("<f", f.read(4))[0]
                        vz204 = unpack("<f", f.read(4))[0]
                        type204 = unpack("B", f.read(1))[0]
                        value1a204 = unpack("B", f.read(1))[0]
                        normalZ_204 = unpack("<h", f.read(2))[0]
                        vx205 = unpack("<f", f.read(4))[0]
                        vy205 = unpack("<f", f.read(4))[0]
                        vz205 = unpack("<f", f.read(4))[0]
                        type205 = unpack("B", f.read(1))[0]
                        value1a205 = unpack("B", f.read(1))[0]
                        normalZ_205 = unpack("<h", f.read(2))[0]
                        vx206 = unpack("<f", f.read(4))[0]
                        vy206 = unpack("<f", f.read(4))[0]
                        vz206 = unpack("<f", f.read(4))[0]
                        type206 = unpack("B", f.read(1))[0]
                        value1a206 = unpack("B", f.read(1))[0]
                        normalZ_206 = unpack("<h", f.read(2))[0]
                        vertices.append([vx187,vz187,vy187])
                        vertices.append([vx188,vz188,vy188])
                        vertices.append([vx189,vz189,vy189])
                        vertices.append([vx190,vz190,vy190])
                        vertices.append([vx191,vz191,vy191])
                        vertices.append([vx192,vz192,vy192])
                        vertices.append([vx193,vz193,vy193])
                        vertices.append([vx194,vz194,vy194])
                        vertices.append([vx195,vz195,vy195])
                        vertices.append([vx196,vz196,vy196])
                        vertices.append([vx197,vz197,vy197])
                        vertices.append([vx198,vz198,vy198])
                        vertices.append([vx199,vz199,vy199])
                        vertices.append([vx200,vz200,vy200])
                        vertices.append([vx201,vz201,vy201])
                        vertices.append([vx202,vz202,vy202])
                        vertices.append([vx203,vz203,vy203])
                        vertices.append([vx204,vz204,vy204])
                        vertices.append([vx205,vz205,vy205])
                        vertices.append([vx206,vz206,vy206])

                elif vertexCount == 21:
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
                        vx207 = unpack("<f", f.read(4))[0]
                        vy207 = unpack("<f", f.read(4))[0]
                        vz207 = unpack("<f", f.read(4))[0]
                        type207 = unpack("B", f.read(1))[0]
                        value1a207 = unpack("B", f.read(1))[0]
                        normalZ_207 = unpack("<h", f.read(2))[0]
                        vx208 = unpack("<f", f.read(4))[0]
                        vy208 = unpack("<f", f.read(4))[0]
                        vz208 = unpack("<f", f.read(4))[0]
                        type208 = unpack("B", f.read(1))[0]
                        value1a208 = unpack("B", f.read(1))[0]
                        normalZ_208 = unpack("<h", f.read(2))[0]
                        vx209 = unpack("<f", f.read(4))[0]
                        vy209 = unpack("<f", f.read(4))[0]
                        vz209 = unpack("<f", f.read(4))[0]
                        type209 = unpack("B", f.read(1))[0]
                        value1a209 = unpack("B", f.read(1))[0]
                        normalZ_209 = unpack("<h", f.read(2))[0]
                        vx210 = unpack("<f", f.read(4))[0]
                        vy210 = unpack("<f", f.read(4))[0]
                        vz210 = unpack("<f", f.read(4))[0]
                        type210 = unpack("B", f.read(1))[0]
                        value1a210 = unpack("B", f.read(1))[0]
                        normalZ_210 = unpack("<h", f.read(2))[0]
                        vx211 = unpack("<f", f.read(4))[0]
                        vy211 = unpack("<f", f.read(4))[0]
                        vz211 = unpack("<f", f.read(4))[0]
                        type211 = unpack("B", f.read(1))[0]
                        value1a211 = unpack("B", f.read(1))[0]
                        normalZ_211 = unpack("<h", f.read(2))[0]
                        vx212 = unpack("<f", f.read(4))[0]
                        vy212 = unpack("<f", f.read(4))[0]
                        vz212 = unpack("<f", f.read(4))[0]
                        type212 = unpack("B", f.read(1))[0]
                        value1a212 = unpack("B", f.read(1))[0]
                        normalZ_212 = unpack("<h", f.read(2))[0]
                        vx213 = unpack("<f", f.read(4))[0]
                        vy213 = unpack("<f", f.read(4))[0]
                        vz213 = unpack("<f", f.read(4))[0]
                        type213 = unpack("B", f.read(1))[0]
                        value1a213 = unpack("B", f.read(1))[0]
                        normalZ_213 = unpack("<h", f.read(2))[0]
                        vx214 = unpack("<f", f.read(4))[0]
                        vy214 = unpack("<f", f.read(4))[0]
                        vz214 = unpack("<f", f.read(4))[0]
                        type214 = unpack("B", f.read(1))[0]
                        value1a214 = unpack("B", f.read(1))[0]
                        normalZ_214 = unpack("<h", f.read(2))[0]
                        vx215 = unpack("<f", f.read(4))[0]
                        vy215 = unpack("<f", f.read(4))[0]
                        vz215 = unpack("<f", f.read(4))[0]
                        type215 = unpack("B", f.read(1))[0]
                        value1a215 = unpack("B", f.read(1))[0]
                        normalZ_215 = unpack("<h", f.read(2))[0]
                        vx216 = unpack("<f", f.read(4))[0]
                        vy216 = unpack("<f", f.read(4))[0]
                        vz216 = unpack("<f", f.read(4))[0]
                        type216 = unpack("B", f.read(1))[0]
                        value1a216 = unpack("B", f.read(1))[0]
                        normalZ_216 = unpack("<h", f.read(2))[0]
                        vx217 = unpack("<f", f.read(4))[0]
                        vy217 = unpack("<f", f.read(4))[0]
                        vz217 = unpack("<f", f.read(4))[0]
                        type217 = unpack("B", f.read(1))[0]
                        value1a217 = unpack("B", f.read(1))[0]
                        normalZ_217 = unpack("<h", f.read(2))[0]
                        vx218 = unpack("<f", f.read(4))[0]
                        vy218 = unpack("<f", f.read(4))[0]
                        vz218 = unpack("<f", f.read(4))[0]
                        type218 = unpack("B", f.read(1))[0]
                        value1a218 = unpack("B", f.read(1))[0]
                        normalZ_218 = unpack("<h", f.read(2))[0]
                        vx219 = unpack("<f", f.read(4))[0]
                        vy219 = unpack("<f", f.read(4))[0]
                        vz219 = unpack("<f", f.read(4))[0]
                        type219 = unpack("B", f.read(1))[0]
                        value1a219 = unpack("B", f.read(1))[0]
                        normalZ_219 = unpack("<h", f.read(2))[0]
                        vx220 = unpack("<f", f.read(4))[0]
                        vy220 = unpack("<f", f.read(4))[0]
                        vz220 = unpack("<f", f.read(4))[0]
                        type220 = unpack("B", f.read(1))[0]
                        value1a220 = unpack("B", f.read(1))[0]
                        normalZ_220 = unpack("<h", f.read(2))[0]
                        vx221 = unpack("<f", f.read(4))[0]
                        vy221 = unpack("<f", f.read(4))[0]
                        vz221 = unpack("<f", f.read(4))[0]
                        type221 = unpack("B", f.read(1))[0]
                        value1a221 = unpack("B", f.read(1))[0]
                        normalZ_221 = unpack("<h", f.read(2))[0]
                        vx222 = unpack("<f", f.read(4))[0]
                        vy222 = unpack("<f", f.read(4))[0]
                        vz222 = unpack("<f", f.read(4))[0]
                        type222 = unpack("B", f.read(1))[0]
                        value1a222 = unpack("B", f.read(1))[0]
                        normalZ_222 = unpack("<h", f.read(2))[0]
                        vx223 = unpack("<f", f.read(4))[0]
                        vy223 = unpack("<f", f.read(4))[0]
                        vz223 = unpack("<f", f.read(4))[0]
                        type223 = unpack("B", f.read(1))[0]
                        value1a223 = unpack("B", f.read(1))[0]
                        normalZ_223 = unpack("<h", f.read(2))[0]
                        vx224 = unpack("<f", f.read(4))[0]
                        vy224 = unpack("<f", f.read(4))[0]
                        vz224 = unpack("<f", f.read(4))[0]
                        type224 = unpack("B", f.read(1))[0]
                        value1a224 = unpack("B", f.read(1))[0]
                        normalZ_224 = unpack("<h", f.read(2))[0]
                        vx225 = unpack("<f", f.read(4))[0]
                        vy225 = unpack("<f", f.read(4))[0]
                        vz225 = unpack("<f", f.read(4))[0]
                        type225 = unpack("B", f.read(1))[0]
                        value1a225 = unpack("B", f.read(1))[0]
                        normalZ_225 = unpack("<h", f.read(2))[0]
                        vx226 = unpack("<f", f.read(4))[0]
                        vy226 = unpack("<f", f.read(4))[0]
                        vz226 = unpack("<f", f.read(4))[0]
                        type226 = unpack("B", f.read(1))[0]
                        value1a226 = unpack("B", f.read(1))[0]
                        normalZ_226 = unpack("<h", f.read(2))[0]
                        vx227 = unpack("<f", f.read(4))[0]
                        vy227 = unpack("<f", f.read(4))[0]
                        vz227 = unpack("<f", f.read(4))[0]
                        type227 = unpack("B", f.read(1))[0]
                        value1a227 = unpack("B", f.read(1))[0]
                        normalZ_227 = unpack("<h", f.read(2))[0]
                        vertices.append([vx207,vz207,vy207])
                        vertices.append([vx208,vz208,vy208])
                        vertices.append([vx209,vz209,vy209])
                        vertices.append([vx210,vz210,vy210])
                        vertices.append([vx211,vz211,vy211])
                        vertices.append([vx212,vz212,vy212])
                        vertices.append([vx213,vz213,vy213])
                        vertices.append([vx214,vz214,vy214])
                        vertices.append([vx215,vz215,vy215])
                        vertices.append([vx216,vz216,vy216])
                        vertices.append([vx217,vz217,vy217])
                        vertices.append([vx218,vz218,vy218])
                        vertices.append([vx219,vz219,vy219])
                        vertices.append([vx220,vz220,vy220])
                        vertices.append([vx221,vz221,vy221])
                        vertices.append([vx222,vz222,vy222])
                        vertices.append([vx223,vz223,vy223])
                        vertices.append([vx224,vz224,vy224])
                        vertices.append([vx225,vz225,vy225])
                        vertices.append([vx226,vz226,vy226])
                        vertices.append([vx227,vz227,vy227])

                elif vertexCount == 22:
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
                        vx228 = unpack("<f", f.read(4))[0]
                        vy228 = unpack("<f", f.read(4))[0]
                        vz228 = unpack("<f", f.read(4))[0]
                        type228 = unpack("B", f.read(1))[0]
                        value1a228 = unpack("B", f.read(1))[0]
                        normalZ_228 = unpack("<h", f.read(2))[0]
                        vx229 = unpack("<f", f.read(4))[0]
                        vy229 = unpack("<f", f.read(4))[0]
                        vz229 = unpack("<f", f.read(4))[0]
                        type229 = unpack("B", f.read(1))[0]
                        value1a229 = unpack("B", f.read(1))[0]
                        normalZ_229 = unpack("<h", f.read(2))[0]
                        vx230 = unpack("<f", f.read(4))[0]
                        vy230 = unpack("<f", f.read(4))[0]
                        vz230 = unpack("<f", f.read(4))[0]
                        type230 = unpack("B", f.read(1))[0]
                        value1a230 = unpack("B", f.read(1))[0]
                        normalZ_230 = unpack("<h", f.read(2))[0]
                        vx231 = unpack("<f", f.read(4))[0]
                        vy231 = unpack("<f", f.read(4))[0]
                        vz231 = unpack("<f", f.read(4))[0]
                        type231 = unpack("B", f.read(1))[0]
                        value1a231 = unpack("B", f.read(1))[0]
                        normalZ_231 = unpack("<h", f.read(2))[0]
                        vx232 = unpack("<f", f.read(4))[0]
                        vy232 = unpack("<f", f.read(4))[0]
                        vz232 = unpack("<f", f.read(4))[0]
                        type232 = unpack("B", f.read(1))[0]
                        value1a232 = unpack("B", f.read(1))[0]
                        normalZ_232 = unpack("<h", f.read(2))[0]
                        vx233 = unpack("<f", f.read(4))[0]
                        vy233 = unpack("<f", f.read(4))[0]
                        vz233 = unpack("<f", f.read(4))[0]
                        type233 = unpack("B", f.read(1))[0]
                        value1a233 = unpack("B", f.read(1))[0]
                        normalZ_233 = unpack("<h", f.read(2))[0]
                        vx234 = unpack("<f", f.read(4))[0]
                        vy234 = unpack("<f", f.read(4))[0]
                        vz234 = unpack("<f", f.read(4))[0]
                        type234 = unpack("B", f.read(1))[0]
                        value1a234 = unpack("B", f.read(1))[0]
                        normalZ_234 = unpack("<h", f.read(2))[0]
                        vx235 = unpack("<f", f.read(4))[0]
                        vy235 = unpack("<f", f.read(4))[0]
                        vz235 = unpack("<f", f.read(4))[0]
                        type235 = unpack("B", f.read(1))[0]
                        value1a235 = unpack("B", f.read(1))[0]
                        normalZ_235 = unpack("<h", f.read(2))[0]
                        vx236 = unpack("<f", f.read(4))[0]
                        vy236 = unpack("<f", f.read(4))[0]
                        vz236 = unpack("<f", f.read(4))[0]
                        type236 = unpack("B", f.read(1))[0]
                        value1a236 = unpack("B", f.read(1))[0]
                        normalZ_236 = unpack("<h", f.read(2))[0]
                        vx237 = unpack("<f", f.read(4))[0]
                        vy237 = unpack("<f", f.read(4))[0]
                        vz237 = unpack("<f", f.read(4))[0]
                        type237 = unpack("B", f.read(1))[0]
                        value1a237 = unpack("B", f.read(1))[0]
                        normalZ_237 = unpack("<h", f.read(2))[0]
                        vx238 = unpack("<f", f.read(4))[0]
                        vy238 = unpack("<f", f.read(4))[0]
                        vz238 = unpack("<f", f.read(4))[0]
                        type238 = unpack("B", f.read(1))[0]
                        value1a238 = unpack("B", f.read(1))[0]
                        normalZ_238 = unpack("<h", f.read(2))[0]
                        vx239 = unpack("<f", f.read(4))[0]
                        vy239 = unpack("<f", f.read(4))[0]
                        vz239 = unpack("<f", f.read(4))[0]
                        type239 = unpack("B", f.read(1))[0]
                        value1a239 = unpack("B", f.read(1))[0]
                        normalZ_239 = unpack("<h", f.read(2))[0]
                        vx240 = unpack("<f", f.read(4))[0]
                        vy240 = unpack("<f", f.read(4))[0]
                        vz240 = unpack("<f", f.read(4))[0]
                        type240 = unpack("B", f.read(1))[0]
                        value1a240 = unpack("B", f.read(1))[0]
                        normalZ_240 = unpack("<h", f.read(2))[0]
                        vx241 = unpack("<f", f.read(4))[0]
                        vy241 = unpack("<f", f.read(4))[0]
                        vz241 = unpack("<f", f.read(4))[0]
                        type241 = unpack("B", f.read(1))[0]
                        value1a241 = unpack("B", f.read(1))[0]
                        normalZ_241 = unpack("<h", f.read(2))[0]
                        vx242 = unpack("<f", f.read(4))[0]
                        vy242 = unpack("<f", f.read(4))[0]
                        vz242 = unpack("<f", f.read(4))[0]
                        type242 = unpack("B", f.read(1))[0]
                        value1a242 = unpack("B", f.read(1))[0]
                        normalZ_242 = unpack("<h", f.read(2))[0]
                        vx243 = unpack("<f", f.read(4))[0]
                        vy243 = unpack("<f", f.read(4))[0]
                        vz243 = unpack("<f", f.read(4))[0]
                        type243 = unpack("B", f.read(1))[0]
                        value1a243 = unpack("B", f.read(1))[0]
                        normalZ_243 = unpack("<h", f.read(2))[0]
                        vx244 = unpack("<f", f.read(4))[0]
                        vy244 = unpack("<f", f.read(4))[0]
                        vz244 = unpack("<f", f.read(4))[0]
                        type244 = unpack("B", f.read(1))[0]
                        value1a244 = unpack("B", f.read(1))[0]
                        normalZ_244 = unpack("<h", f.read(2))[0]
                        vx245 = unpack("<f", f.read(4))[0]
                        vy245 = unpack("<f", f.read(4))[0]
                        vz245 = unpack("<f", f.read(4))[0]
                        type245 = unpack("B", f.read(1))[0]
                        value1a245 = unpack("B", f.read(1))[0]
                        normalZ_245 = unpack("<h", f.read(2))[0]
                        vx246 = unpack("<f", f.read(4))[0]
                        vy246 = unpack("<f", f.read(4))[0]
                        vz246 = unpack("<f", f.read(4))[0]
                        type246 = unpack("B", f.read(1))[0]
                        value1a246 = unpack("B", f.read(1))[0]
                        normalZ_246 = unpack("<h", f.read(2))[0]
                        vx247 = unpack("<f", f.read(4))[0]
                        vy247 = unpack("<f", f.read(4))[0]
                        vz247 = unpack("<f", f.read(4))[0]
                        type247 = unpack("B", f.read(1))[0]
                        value1a247 = unpack("B", f.read(1))[0]
                        normalZ_247 = unpack("<h", f.read(2))[0]
                        vx248 = unpack("<f", f.read(4))[0]
                        vy248 = unpack("<f", f.read(4))[0]
                        vz248 = unpack("<f", f.read(4))[0]
                        type248 = unpack("B", f.read(1))[0]
                        value1a248 = unpack("B", f.read(1))[0]
                        normalZ_248 = unpack("<h", f.read(2))[0]
                        vx249 = unpack("<f", f.read(4))[0]
                        vy249 = unpack("<f", f.read(4))[0]
                        vz249 = unpack("<f", f.read(4))[0]
                        type249 = unpack("B", f.read(1))[0]
                        value1a249 = unpack("B", f.read(1))[0]
                        normalZ_249 = unpack("<h", f.read(2))[0]
                        vertices.append([vx228,vz228,vy228])
                        vertices.append([vx229,vz229,vy229])
                        vertices.append([vx230,vz230,vy230])
                        vertices.append([vx231,vz231,vy231])
                        vertices.append([vx232,vz232,vy232])
                        vertices.append([vx233,vz233,vy233])
                        vertices.append([vx234,vz234,vy234])
                        vertices.append([vx235,vz235,vy235])
                        vertices.append([vx236,vz236,vy236])
                        vertices.append([vx237,vz237,vy237])
                        vertices.append([vx238,vz238,vy238])
                        vertices.append([vx239,vz239,vy239])
                        vertices.append([vx240,vz240,vy240])
                        vertices.append([vx241,vz241,vy241])
                        vertices.append([vx242,vz242,vy242])
                        vertices.append([vx243,vz243,vy243])
                        vertices.append([vx244,vz244,vy244])
                        vertices.append([vx245,vz245,vy245])
                        vertices.append([vx246,vz246,vy246])
                        vertices.append([vx247,vz247,vy247])
                        vertices.append([vx248,vz248,vy248])
                        vertices.append([vx249,vz249,vy249])

                elif vertexCount == 23:
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
                        vx250 = unpack("<f", f.read(4))[0]
                        vy250 = unpack("<f", f.read(4))[0]
                        vz250 = unpack("<f", f.read(4))[0]
                        type250 = unpack("B", f.read(1))[0]
                        value1a250 = unpack("B", f.read(1))[0]
                        normalZ_250 = unpack("<h", f.read(2))[0]
                        vx251 = unpack("<f", f.read(4))[0]
                        vy251 = unpack("<f", f.read(4))[0]
                        vz251 = unpack("<f", f.read(4))[0]
                        type251 = unpack("B", f.read(1))[0]
                        value1a251 = unpack("B", f.read(1))[0]
                        normalZ_251 = unpack("<h", f.read(2))[0]
                        vx252 = unpack("<f", f.read(4))[0]
                        vy252 = unpack("<f", f.read(4))[0]
                        vz252 = unpack("<f", f.read(4))[0]
                        type252 = unpack("B", f.read(1))[0]
                        value1a252 = unpack("B", f.read(1))[0]
                        normalZ_252 = unpack("<h", f.read(2))[0]
                        vx253 = unpack("<f", f.read(4))[0]
                        vy253 = unpack("<f", f.read(4))[0]
                        vz253 = unpack("<f", f.read(4))[0]
                        type253 = unpack("B", f.read(1))[0]
                        value1a253 = unpack("B", f.read(1))[0]
                        normalZ_253 = unpack("<h", f.read(2))[0]
                        vx254 = unpack("<f", f.read(4))[0]
                        vy254 = unpack("<f", f.read(4))[0]
                        vz254 = unpack("<f", f.read(4))[0]
                        type254 = unpack("B", f.read(1))[0]
                        value1a254 = unpack("B", f.read(1))[0]
                        normalZ_254 = unpack("<h", f.read(2))[0]
                        vx255 = unpack("<f", f.read(4))[0]
                        vy255 = unpack("<f", f.read(4))[0]
                        vz255 = unpack("<f", f.read(4))[0]
                        type255 = unpack("B", f.read(1))[0]
                        value1a255 = unpack("B", f.read(1))[0]
                        normalZ_255 = unpack("<h", f.read(2))[0]
                        vx256 = unpack("<f", f.read(4))[0]
                        vy256 = unpack("<f", f.read(4))[0]
                        vz256 = unpack("<f", f.read(4))[0]
                        type256 = unpack("B", f.read(1))[0]
                        value1a256 = unpack("B", f.read(1))[0]
                        normalZ_256 = unpack("<h", f.read(2))[0]
                        vx257 = unpack("<f", f.read(4))[0]
                        vy257 = unpack("<f", f.read(4))[0]
                        vz257 = unpack("<f", f.read(4))[0]
                        type257 = unpack("B", f.read(1))[0]
                        value1a257 = unpack("B", f.read(1))[0]
                        normalZ_257 = unpack("<h", f.read(2))[0]
                        vx258 = unpack("<f", f.read(4))[0]
                        vy258 = unpack("<f", f.read(4))[0]
                        vz258 = unpack("<f", f.read(4))[0]
                        type258 = unpack("B", f.read(1))[0]
                        value1a258 = unpack("B", f.read(1))[0]
                        normalZ_258 = unpack("<h", f.read(2))[0]
                        vx259 = unpack("<f", f.read(4))[0]
                        vy259 = unpack("<f", f.read(4))[0]
                        vz259 = unpack("<f", f.read(4))[0]
                        type259 = unpack("B", f.read(1))[0]
                        value1a259 = unpack("B", f.read(1))[0]
                        normalZ_259 = unpack("<h", f.read(2))[0]
                        vx260 = unpack("<f", f.read(4))[0]
                        vy260 = unpack("<f", f.read(4))[0]
                        vz260 = unpack("<f", f.read(4))[0]
                        type260 = unpack("B", f.read(1))[0]
                        value1a260 = unpack("B", f.read(1))[0]
                        normalZ_260 = unpack("<h", f.read(2))[0]
                        vx261 = unpack("<f", f.read(4))[0]
                        vy261 = unpack("<f", f.read(4))[0]
                        vz261 = unpack("<f", f.read(4))[0]
                        type261 = unpack("B", f.read(1))[0]
                        value1a261 = unpack("B", f.read(1))[0]
                        normalZ_261 = unpack("<h", f.read(2))[0]
                        vx262 = unpack("<f", f.read(4))[0]
                        vy262 = unpack("<f", f.read(4))[0]
                        vz262 = unpack("<f", f.read(4))[0]
                        type262 = unpack("B", f.read(1))[0]
                        value1a262 = unpack("B", f.read(1))[0]
                        normalZ_262 = unpack("<h", f.read(2))[0]
                        vx263 = unpack("<f", f.read(4))[0]
                        vy263 = unpack("<f", f.read(4))[0]
                        vz263 = unpack("<f", f.read(4))[0]
                        type263 = unpack("B", f.read(1))[0]
                        value1a263 = unpack("B", f.read(1))[0]
                        normalZ_263 = unpack("<h", f.read(2))[0]
                        vx264 = unpack("<f", f.read(4))[0]
                        vy264 = unpack("<f", f.read(4))[0]
                        vz264 = unpack("<f", f.read(4))[0]
                        type264 = unpack("B", f.read(1))[0]
                        value1a264 = unpack("B", f.read(1))[0]
                        normalZ_264 = unpack("<h", f.read(2))[0]
                        vx265 = unpack("<f", f.read(4))[0]
                        vy265 = unpack("<f", f.read(4))[0]
                        vz265 = unpack("<f", f.read(4))[0]
                        type265 = unpack("B", f.read(1))[0]
                        value1a265 = unpack("B", f.read(1))[0]
                        normalZ_265 = unpack("<h", f.read(2))[0]
                        vx266 = unpack("<f", f.read(4))[0]
                        vy266 = unpack("<f", f.read(4))[0]
                        vz266 = unpack("<f", f.read(4))[0]
                        type266 = unpack("B", f.read(1))[0]
                        value1a266 = unpack("B", f.read(1))[0]
                        normalZ_266 = unpack("<h", f.read(2))[0]
                        vx267 = unpack("<f", f.read(4))[0]
                        vy267 = unpack("<f", f.read(4))[0]
                        vz267 = unpack("<f", f.read(4))[0]
                        type267 = unpack("B", f.read(1))[0]
                        value1a267 = unpack("B", f.read(1))[0]
                        normalZ_267 = unpack("<h", f.read(2))[0]
                        vx268 = unpack("<f", f.read(4))[0]
                        vy268 = unpack("<f", f.read(4))[0]
                        vz268 = unpack("<f", f.read(4))[0]
                        type268 = unpack("B", f.read(1))[0]
                        value1a268 = unpack("B", f.read(1))[0]
                        normalZ_268 = unpack("<h", f.read(2))[0]
                        vx269 = unpack("<f", f.read(4))[0]
                        vy269 = unpack("<f", f.read(4))[0]
                        vz269 = unpack("<f", f.read(4))[0]
                        type269 = unpack("B", f.read(1))[0]
                        value1a269 = unpack("B", f.read(1))[0]
                        normalZ_269 = unpack("<h", f.read(2))[0]
                        vx270 = unpack("<f", f.read(4))[0]
                        vy270 = unpack("<f", f.read(4))[0]
                        vz270 = unpack("<f", f.read(4))[0]
                        type270 = unpack("B", f.read(1))[0]
                        value1a270 = unpack("B", f.read(1))[0]
                        normalZ_270 = unpack("<h", f.read(2))[0]
                        vx271 = unpack("<f", f.read(4))[0]
                        vy271 = unpack("<f", f.read(4))[0]
                        vz271 = unpack("<f", f.read(4))[0]
                        type271 = unpack("B", f.read(1))[0]
                        value1a271 = unpack("B", f.read(1))[0]
                        normalZ_271 = unpack("<h", f.read(2))[0]
                        vx272 = unpack("<f", f.read(4))[0]
                        vy272 = unpack("<f", f.read(4))[0]
                        vz272 = unpack("<f", f.read(4))[0]
                        type272 = unpack("B", f.read(1))[0]
                        value1a272 = unpack("B", f.read(1))[0]
                        normalZ_272 = unpack("<h", f.read(2))[0]
                        vertices.append([vx250,vz250,vy250])
                        vertices.append([vx251,vz251,vy251])
                        vertices.append([vx252,vz252,vy252])
                        vertices.append([vx253,vz253,vy253])
                        vertices.append([vx254,vz254,vy254])
                        vertices.append([vx255,vz255,vy255])
                        vertices.append([vx256,vz256,vy256])
                        vertices.append([vx257,vz257,vy257])
                        vertices.append([vx258,vz258,vy258])
                        vertices.append([vx259,vz259,vy259])
                        vertices.append([vx260,vz260,vy260])
                        vertices.append([vx261,vz261,vy261])
                        vertices.append([vx262,vz262,vy262])
                        vertices.append([vx263,vz263,vy263])
                        vertices.append([vx264,vz264,vy264])
                        vertices.append([vx265,vz265,vy265])
                        vertices.append([vx266,vz266,vy266])
                        vertices.append([vx267,vz267,vy267])
                        vertices.append([vx268,vz268,vy268])
                        vertices.append([vx269,vz269,vy269])
                        vertices.append([vx270,vz270,vy270])
                        vertices.append([vx271,vz271,vy271])
                        vertices.append([vx272,vz272,vy272])

                elif vertexCount == 24:
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
                        vx273 = unpack("<f", f.read(4))[0]
                        vy273 = unpack("<f", f.read(4))[0]
                        vz273 = unpack("<f", f.read(4))[0]
                        type273 = unpack("B", f.read(1))[0]
                        value1a273 = unpack("B", f.read(1))[0]
                        normalZ_273 = unpack("<h", f.read(2))[0]
                        vx274 = unpack("<f", f.read(4))[0]
                        vy274 = unpack("<f", f.read(4))[0]
                        vz274 = unpack("<f", f.read(4))[0]
                        type274 = unpack("B", f.read(1))[0]
                        value1a274 = unpack("B", f.read(1))[0]
                        normalZ_274 = unpack("<h", f.read(2))[0]
                        vx275 = unpack("<f", f.read(4))[0]
                        vy275 = unpack("<f", f.read(4))[0]
                        vz275 = unpack("<f", f.read(4))[0]
                        type275 = unpack("B", f.read(1))[0]
                        value1a275 = unpack("B", f.read(1))[0]
                        normalZ_275 = unpack("<h", f.read(2))[0]
                        vx276 = unpack("<f", f.read(4))[0]
                        vy276 = unpack("<f", f.read(4))[0]
                        vz276 = unpack("<f", f.read(4))[0]
                        type276 = unpack("B", f.read(1))[0]
                        value1a276 = unpack("B", f.read(1))[0]
                        normalZ_276 = unpack("<h", f.read(2))[0]
                        vx277 = unpack("<f", f.read(4))[0]
                        vy277 = unpack("<f", f.read(4))[0]
                        vz277 = unpack("<f", f.read(4))[0]
                        type277 = unpack("B", f.read(1))[0]
                        value1a277 = unpack("B", f.read(1))[0]
                        normalZ_277 = unpack("<h", f.read(2))[0]
                        vx278 = unpack("<f", f.read(4))[0]
                        vy278 = unpack("<f", f.read(4))[0]
                        vz278 = unpack("<f", f.read(4))[0]
                        type278 = unpack("B", f.read(1))[0]
                        value1a278 = unpack("B", f.read(1))[0]
                        normalZ_278 = unpack("<h", f.read(2))[0]
                        vx279 = unpack("<f", f.read(4))[0]
                        vy279 = unpack("<f", f.read(4))[0]
                        vz279 = unpack("<f", f.read(4))[0]
                        type279 = unpack("B", f.read(1))[0]
                        value1a279 = unpack("B", f.read(1))[0]
                        normalZ_279 = unpack("<h", f.read(2))[0]
                        vx280 = unpack("<f", f.read(4))[0]
                        vy280 = unpack("<f", f.read(4))[0]
                        vz280 = unpack("<f", f.read(4))[0]
                        type280 = unpack("B", f.read(1))[0]
                        value1a280 = unpack("B", f.read(1))[0]
                        normalZ_280 = unpack("<h", f.read(2))[0]
                        vx281 = unpack("<f", f.read(4))[0]
                        vy281 = unpack("<f", f.read(4))[0]
                        vz281 = unpack("<f", f.read(4))[0]
                        type281 = unpack("B", f.read(1))[0]
                        value1a281 = unpack("B", f.read(1))[0]
                        normalZ_281 = unpack("<h", f.read(2))[0]
                        vx282 = unpack("<f", f.read(4))[0]
                        vy282 = unpack("<f", f.read(4))[0]
                        vz282 = unpack("<f", f.read(4))[0]
                        type282 = unpack("B", f.read(1))[0]
                        value1a282 = unpack("B", f.read(1))[0]
                        normalZ_282 = unpack("<h", f.read(2))[0]
                        vx283 = unpack("<f", f.read(4))[0]
                        vy283 = unpack("<f", f.read(4))[0]
                        vz283 = unpack("<f", f.read(4))[0]
                        type283 = unpack("B", f.read(1))[0]
                        value1a283 = unpack("B", f.read(1))[0]
                        normalZ_283 = unpack("<h", f.read(2))[0]
                        vx284 = unpack("<f", f.read(4))[0]
                        vy284 = unpack("<f", f.read(4))[0]
                        vz284 = unpack("<f", f.read(4))[0]
                        type284 = unpack("B", f.read(1))[0]
                        value1a284 = unpack("B", f.read(1))[0]
                        normalZ_284 = unpack("<h", f.read(2))[0]
                        vx285 = unpack("<f", f.read(4))[0]
                        vy285 = unpack("<f", f.read(4))[0]
                        vz285 = unpack("<f", f.read(4))[0]
                        type285 = unpack("B", f.read(1))[0]
                        value1a285 = unpack("B", f.read(1))[0]
                        normalZ_285 = unpack("<h", f.read(2))[0]
                        vx286 = unpack("<f", f.read(4))[0]
                        vy286 = unpack("<f", f.read(4))[0]
                        vz286 = unpack("<f", f.read(4))[0]
                        type286 = unpack("B", f.read(1))[0]
                        value1a286 = unpack("B", f.read(1))[0]
                        normalZ_286 = unpack("<h", f.read(2))[0]
                        vx287 = unpack("<f", f.read(4))[0]
                        vy287 = unpack("<f", f.read(4))[0]
                        vz287 = unpack("<f", f.read(4))[0]
                        type287 = unpack("B", f.read(1))[0]
                        value1a287 = unpack("B", f.read(1))[0]
                        normalZ_287 = unpack("<h", f.read(2))[0]
                        vx288 = unpack("<f", f.read(4))[0]
                        vy288 = unpack("<f", f.read(4))[0]
                        vz288 = unpack("<f", f.read(4))[0]
                        type288 = unpack("B", f.read(1))[0]
                        value1a288 = unpack("B", f.read(1))[0]
                        normalZ_288 = unpack("<h", f.read(2))[0]
                        vx289 = unpack("<f", f.read(4))[0]
                        vy289 = unpack("<f", f.read(4))[0]
                        vz289 = unpack("<f", f.read(4))[0]
                        type289 = unpack("B", f.read(1))[0]
                        value1a289 = unpack("B", f.read(1))[0]
                        normalZ_289 = unpack("<h", f.read(2))[0]
                        vx290 = unpack("<f", f.read(4))[0]
                        vy290 = unpack("<f", f.read(4))[0]
                        vz290 = unpack("<f", f.read(4))[0]
                        type290 = unpack("B", f.read(1))[0]
                        value1a290 = unpack("B", f.read(1))[0]
                        normalZ_290 = unpack("<h", f.read(2))[0]
                        vx291 = unpack("<f", f.read(4))[0]
                        vy291 = unpack("<f", f.read(4))[0]
                        vz291 = unpack("<f", f.read(4))[0]
                        type291 = unpack("B", f.read(1))[0]
                        value1a291 = unpack("B", f.read(1))[0]
                        normalZ_291 = unpack("<h", f.read(2))[0]
                        vx292 = unpack("<f", f.read(4))[0]
                        vy292 = unpack("<f", f.read(4))[0]
                        vz292 = unpack("<f", f.read(4))[0]
                        type292 = unpack("B", f.read(1))[0]
                        value1a292 = unpack("B", f.read(1))[0]
                        normalZ_292 = unpack("<h", f.read(2))[0]
                        vx293 = unpack("<f", f.read(4))[0]
                        vy293 = unpack("<f", f.read(4))[0]
                        vz293 = unpack("<f", f.read(4))[0]
                        type293 = unpack("B", f.read(1))[0]
                        value1a293 = unpack("B", f.read(1))[0]
                        normalZ_293 = unpack("<h", f.read(2))[0]
                        vx294 = unpack("<f", f.read(4))[0]
                        vy294 = unpack("<f", f.read(4))[0]
                        vz294 = unpack("<f", f.read(4))[0]
                        type294 = unpack("B", f.read(1))[0]
                        value1a294 = unpack("B", f.read(1))[0]
                        normalZ_294 = unpack("<h", f.read(2))[0]
                        vx295 = unpack("<f", f.read(4))[0]
                        vy295 = unpack("<f", f.read(4))[0]
                        vz295 = unpack("<f", f.read(4))[0]
                        type295 = unpack("B", f.read(1))[0]
                        value1a295 = unpack("B", f.read(1))[0]
                        normalZ_295 = unpack("<h", f.read(2))[0]
                        vx296 = unpack("<f", f.read(4))[0]
                        vy296 = unpack("<f", f.read(4))[0]
                        vz296 = unpack("<f", f.read(4))[0]
                        type296 = unpack("B", f.read(1))[0]
                        value1a296 = unpack("B", f.read(1))[0]
                        normalZ_296 = unpack("<h", f.read(2))[0]
                        vertices.append([vx273,vz273,vy273])
                        vertices.append([vx274,vz274,vy274])
                        vertices.append([vx275,vz275,vy275])
                        vertices.append([vx276,vz276,vy276])
                        vertices.append([vx277,vz277,vy277])
                        vertices.append([vx278,vz278,vy278])
                        vertices.append([vx279,vz279,vy279])
                        vertices.append([vx280,vz280,vy280])
                        vertices.append([vx281,vz281,vy281])
                        vertices.append([vx282,vz282,vy282])
                        vertices.append([vx283,vz283,vy283])
                        vertices.append([vx284,vz284,vy284])
                        vertices.append([vx285,vz285,vy285])
                        vertices.append([vx286,vz286,vy286])
                        vertices.append([vx287,vz287,vy287])
                        vertices.append([vx288,vz288,vy288])
                        vertices.append([vx289,vz289,vy289])
                        vertices.append([vx290,vz290,vy290])
                        vertices.append([vx291,vz291,vy291])
                        vertices.append([vx292,vz292,vy292])
                        vertices.append([vx293,vz293,vy293])
                        vertices.append([vx294,vz294,vy294])
                        vertices.append([vx295,vz295,vy295])
                        vertices.append([vx296,vz296,vy296])

                elif vertexCount == 25:
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
                        vx297 = unpack("<f", f.read(4))[0]
                        vy297 = unpack("<f", f.read(4))[0]
                        vz297 = unpack("<f", f.read(4))[0]
                        type297 = unpack("B", f.read(1))[0]
                        value1a297 = unpack("B", f.read(1))[0]
                        normalZ_297 = unpack("<h", f.read(2))[0]
                        vx298 = unpack("<f", f.read(4))[0]
                        vy298 = unpack("<f", f.read(4))[0]
                        vz298 = unpack("<f", f.read(4))[0]
                        type298 = unpack("B", f.read(1))[0]
                        value1a298 = unpack("B", f.read(1))[0]
                        normalZ_298 = unpack("<h", f.read(2))[0]
                        vx299 = unpack("<f", f.read(4))[0]
                        vy299 = unpack("<f", f.read(4))[0]
                        vz299 = unpack("<f", f.read(4))[0]
                        type299 = unpack("B", f.read(1))[0]
                        value1a299 = unpack("B", f.read(1))[0]
                        normalZ_299 = unpack("<h", f.read(2))[0]
                        vx300 = unpack("<f", f.read(4))[0]
                        vy300 = unpack("<f", f.read(4))[0]
                        vz300 = unpack("<f", f.read(4))[0]
                        type300 = unpack("B", f.read(1))[0]
                        value1a300 = unpack("B", f.read(1))[0]
                        normalZ_300 = unpack("<h", f.read(2))[0]
                        vx301 = unpack("<f", f.read(4))[0]
                        vy301 = unpack("<f", f.read(4))[0]
                        vz301 = unpack("<f", f.read(4))[0]
                        type301 = unpack("B", f.read(1))[0]
                        value1a301 = unpack("B", f.read(1))[0]
                        normalZ_301 = unpack("<h", f.read(2))[0]
                        vx302 = unpack("<f", f.read(4))[0]
                        vy302 = unpack("<f", f.read(4))[0]
                        vz302 = unpack("<f", f.read(4))[0]
                        type302 = unpack("B", f.read(1))[0]
                        value1a302 = unpack("B", f.read(1))[0]
                        normalZ_302 = unpack("<h", f.read(2))[0]
                        vx303 = unpack("<f", f.read(4))[0]
                        vy303 = unpack("<f", f.read(4))[0]
                        vz303 = unpack("<f", f.read(4))[0]
                        type303 = unpack("B", f.read(1))[0]
                        value1a303 = unpack("B", f.read(1))[0]
                        normalZ_303 = unpack("<h", f.read(2))[0]
                        vx304 = unpack("<f", f.read(4))[0]
                        vy304 = unpack("<f", f.read(4))[0]
                        vz304 = unpack("<f", f.read(4))[0]
                        type304 = unpack("B", f.read(1))[0]
                        value1a304 = unpack("B", f.read(1))[0]
                        normalZ_304 = unpack("<h", f.read(2))[0]
                        vx305 = unpack("<f", f.read(4))[0]
                        vy305 = unpack("<f", f.read(4))[0]
                        vz305 = unpack("<f", f.read(4))[0]
                        type305 = unpack("B", f.read(1))[0]
                        value1a305 = unpack("B", f.read(1))[0]
                        normalZ_305 = unpack("<h", f.read(2))[0]
                        vx306 = unpack("<f", f.read(4))[0]
                        vy306 = unpack("<f", f.read(4))[0]
                        vz306 = unpack("<f", f.read(4))[0]
                        type306 = unpack("B", f.read(1))[0]
                        value1a306 = unpack("B", f.read(1))[0]
                        normalZ_306 = unpack("<h", f.read(2))[0]
                        vx307 = unpack("<f", f.read(4))[0]
                        vy307 = unpack("<f", f.read(4))[0]
                        vz307 = unpack("<f", f.read(4))[0]
                        type307 = unpack("B", f.read(1))[0]
                        value1a307 = unpack("B", f.read(1))[0]
                        normalZ_307 = unpack("<h", f.read(2))[0]
                        vx308 = unpack("<f", f.read(4))[0]
                        vy308 = unpack("<f", f.read(4))[0]
                        vz308 = unpack("<f", f.read(4))[0]
                        type308 = unpack("B", f.read(1))[0]
                        value1a308 = unpack("B", f.read(1))[0]
                        normalZ_308 = unpack("<h", f.read(2))[0]
                        vx309 = unpack("<f", f.read(4))[0]
                        vy309 = unpack("<f", f.read(4))[0]
                        vz309 = unpack("<f", f.read(4))[0]
                        type309 = unpack("B", f.read(1))[0]
                        value1a309 = unpack("B", f.read(1))[0]
                        normalZ_309 = unpack("<h", f.read(2))[0]
                        vx310 = unpack("<f", f.read(4))[0]
                        vy310 = unpack("<f", f.read(4))[0]
                        vz310 = unpack("<f", f.read(4))[0]
                        type310 = unpack("B", f.read(1))[0]
                        value1a310 = unpack("B", f.read(1))[0]
                        normalZ_310 = unpack("<h", f.read(2))[0]
                        vx311 = unpack("<f", f.read(4))[0]
                        vy311 = unpack("<f", f.read(4))[0]
                        vz311 = unpack("<f", f.read(4))[0]
                        type311 = unpack("B", f.read(1))[0]
                        value1a311 = unpack("B", f.read(1))[0]
                        normalZ_311 = unpack("<h", f.read(2))[0]
                        vx312 = unpack("<f", f.read(4))[0]
                        vy312 = unpack("<f", f.read(4))[0]
                        vz312 = unpack("<f", f.read(4))[0]
                        type312 = unpack("B", f.read(1))[0]
                        value1a312 = unpack("B", f.read(1))[0]
                        normalZ_312 = unpack("<h", f.read(2))[0]
                        vx313 = unpack("<f", f.read(4))[0]
                        vy313 = unpack("<f", f.read(4))[0]
                        vz313 = unpack("<f", f.read(4))[0]
                        type313 = unpack("B", f.read(1))[0]
                        value1a313 = unpack("B", f.read(1))[0]
                        normalZ_313 = unpack("<h", f.read(2))[0]
                        vx314 = unpack("<f", f.read(4))[0]
                        vy314 = unpack("<f", f.read(4))[0]
                        vz314 = unpack("<f", f.read(4))[0]
                        type314 = unpack("B", f.read(1))[0]
                        value1a314 = unpack("B", f.read(1))[0]
                        normalZ_314 = unpack("<h", f.read(2))[0]
                        vx315 = unpack("<f", f.read(4))[0]
                        vy315 = unpack("<f", f.read(4))[0]
                        vz315 = unpack("<f", f.read(4))[0]
                        type315 = unpack("B", f.read(1))[0]
                        value1a315 = unpack("B", f.read(1))[0]
                        normalZ_315 = unpack("<h", f.read(2))[0]
                        vx316 = unpack("<f", f.read(4))[0]
                        vy316 = unpack("<f", f.read(4))[0]
                        vz316 = unpack("<f", f.read(4))[0]
                        type316 = unpack("B", f.read(1))[0]
                        value1a316 = unpack("B", f.read(1))[0]
                        normalZ_316 = unpack("<h", f.read(2))[0]
                        vx317 = unpack("<f", f.read(4))[0]
                        vy317 = unpack("<f", f.read(4))[0]
                        vz317 = unpack("<f", f.read(4))[0]
                        type317 = unpack("B", f.read(1))[0]
                        value1a317 = unpack("B", f.read(1))[0]
                        normalZ_317 = unpack("<h", f.read(2))[0]
                        vx318 = unpack("<f", f.read(4))[0]
                        vy318 = unpack("<f", f.read(4))[0]
                        vz318 = unpack("<f", f.read(4))[0]
                        type318 = unpack("B", f.read(1))[0]
                        value1a318 = unpack("B", f.read(1))[0]
                        normalZ_318 = unpack("<h", f.read(2))[0]
                        vx319 = unpack("<f", f.read(4))[0]
                        vy319 = unpack("<f", f.read(4))[0]
                        vz319 = unpack("<f", f.read(4))[0]
                        type319 = unpack("B", f.read(1))[0]
                        value1a319 = unpack("B", f.read(1))[0]
                        normalZ_319 = unpack("<h", f.read(2))[0]
                        vx320 = unpack("<f", f.read(4))[0]
                        vy320 = unpack("<f", f.read(4))[0]
                        vz320 = unpack("<f", f.read(4))[0]
                        type320 = unpack("B", f.read(1))[0]
                        value1a320 = unpack("B", f.read(1))[0]
                        normalZ_320 = unpack("<h", f.read(2))[0]
                        vx321 = unpack("<f", f.read(4))[0]
                        vy321 = unpack("<f", f.read(4))[0]
                        vz321 = unpack("<f", f.read(4))[0]
                        type321 = unpack("B", f.read(1))[0]
                        value1a321 = unpack("B", f.read(1))[0]
                        normalZ_321 = unpack("<h", f.read(2))[0]
                        vertices.append([vx297,vz297,vy297])
                        vertices.append([vx298,vz298,vy298])
                        vertices.append([vx299,vz299,vy299])
                        vertices.append([vx300,vz300,vy300])
                        vertices.append([vx301,vz301,vy301])
                        vertices.append([vx302,vz302,vy302])
                        vertices.append([vx303,vz303,vy303])
                        vertices.append([vx304,vz304,vy304])
                        vertices.append([vx305,vz305,vy305])
                        vertices.append([vx306,vz306,vy306])
                        vertices.append([vx307,vz307,vy307])
                        vertices.append([vx308,vz308,vy308])
                        vertices.append([vx309,vz309,vy309])
                        vertices.append([vx310,vz310,vy310])
                        vertices.append([vx311,vz311,vy311])
                        vertices.append([vx312,vz312,vy312])
                        vertices.append([vx313,vz313,vy313])
                        vertices.append([vx314,vz314,vy314])
                        vertices.append([vx315,vz315,vy315])
                        vertices.append([vx316,vz316,vy316])
                        vertices.append([vx317,vz317,vy317])
                        vertices.append([vx318,vz318,vy318])
                        vertices.append([vx319,vz319,vy319])
                        vertices.append([vx320,vz320,vy320])
                        vertices.append([vx321,vz321,vy321])
                elif vertexCount == 26:
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
                        vx322 = unpack("<f", f.read(4))[0]
                        vy322 = unpack("<f", f.read(4))[0]
                        vz322 = unpack("<f", f.read(4))[0]
                        type322 = unpack("B", f.read(1))[0]
                        value1a322 = unpack("B", f.read(1))[0]
                        normalZ_322 = unpack("<h", f.read(2))[0]
                        vx323 = unpack("<f", f.read(4))[0]
                        vy323 = unpack("<f", f.read(4))[0]
                        vz323 = unpack("<f", f.read(4))[0]
                        type323 = unpack("B", f.read(1))[0]
                        value1a323 = unpack("B", f.read(1))[0]
                        normalZ_323 = unpack("<h", f.read(2))[0]
                        vx324 = unpack("<f", f.read(4))[0]
                        vy324 = unpack("<f", f.read(4))[0]
                        vz324 = unpack("<f", f.read(4))[0]
                        type324 = unpack("B", f.read(1))[0]
                        value1a324 = unpack("B", f.read(1))[0]
                        normalZ_324 = unpack("<h", f.read(2))[0]
                        vx325 = unpack("<f", f.read(4))[0]
                        vy325 = unpack("<f", f.read(4))[0]
                        vz325 = unpack("<f", f.read(4))[0]
                        type325 = unpack("B", f.read(1))[0]
                        value1a325 = unpack("B", f.read(1))[0]
                        normalZ_325 = unpack("<h", f.read(2))[0]
                        vx326 = unpack("<f", f.read(4))[0]
                        vy326 = unpack("<f", f.read(4))[0]
                        vz326 = unpack("<f", f.read(4))[0]
                        type326 = unpack("B", f.read(1))[0]
                        value1a326 = unpack("B", f.read(1))[0]
                        normalZ_326 = unpack("<h", f.read(2))[0]
                        vx327 = unpack("<f", f.read(4))[0]
                        vy327 = unpack("<f", f.read(4))[0]
                        vz327 = unpack("<f", f.read(4))[0]
                        type327 = unpack("B", f.read(1))[0]
                        value1a327 = unpack("B", f.read(1))[0]
                        normalZ_327 = unpack("<h", f.read(2))[0]
                        vx328 = unpack("<f", f.read(4))[0]
                        vy328 = unpack("<f", f.read(4))[0]
                        vz328 = unpack("<f", f.read(4))[0]
                        type328 = unpack("B", f.read(1))[0]
                        value1a328 = unpack("B", f.read(1))[0]
                        normalZ_328 = unpack("<h", f.read(2))[0]
                        vx329 = unpack("<f", f.read(4))[0]
                        vy329 = unpack("<f", f.read(4))[0]
                        vz329 = unpack("<f", f.read(4))[0]
                        type329 = unpack("B", f.read(1))[0]
                        value1a329 = unpack("B", f.read(1))[0]
                        normalZ_329 = unpack("<h", f.read(2))[0]
                        vx330 = unpack("<f", f.read(4))[0]
                        vy330 = unpack("<f", f.read(4))[0]
                        vz330 = unpack("<f", f.read(4))[0]
                        type330 = unpack("B", f.read(1))[0]
                        value1a330 = unpack("B", f.read(1))[0]
                        normalZ_330 = unpack("<h", f.read(2))[0]
                        vx331 = unpack("<f", f.read(4))[0]
                        vy331 = unpack("<f", f.read(4))[0]
                        vz331 = unpack("<f", f.read(4))[0]
                        type331 = unpack("B", f.read(1))[0]
                        value1a331 = unpack("B", f.read(1))[0]
                        normalZ_331 = unpack("<h", f.read(2))[0]
                        vx332 = unpack("<f", f.read(4))[0]
                        vy332 = unpack("<f", f.read(4))[0]
                        vz332 = unpack("<f", f.read(4))[0]
                        type332 = unpack("B", f.read(1))[0]
                        value1a332 = unpack("B", f.read(1))[0]
                        normalZ_332 = unpack("<h", f.read(2))[0]
                        vx333 = unpack("<f", f.read(4))[0]
                        vy333 = unpack("<f", f.read(4))[0]
                        vz333 = unpack("<f", f.read(4))[0]
                        type333 = unpack("B", f.read(1))[0]
                        value1a333 = unpack("B", f.read(1))[0]
                        normalZ_333 = unpack("<h", f.read(2))[0]
                        vx334 = unpack("<f", f.read(4))[0]
                        vy334 = unpack("<f", f.read(4))[0]
                        vz334 = unpack("<f", f.read(4))[0]
                        type334 = unpack("B", f.read(1))[0]
                        value1a334 = unpack("B", f.read(1))[0]
                        normalZ_334 = unpack("<h", f.read(2))[0]
                        vx335 = unpack("<f", f.read(4))[0]
                        vy335 = unpack("<f", f.read(4))[0]
                        vz335 = unpack("<f", f.read(4))[0]
                        type335 = unpack("B", f.read(1))[0]
                        value1a335 = unpack("B", f.read(1))[0]
                        normalZ_335 = unpack("<h", f.read(2))[0]
                        vx336 = unpack("<f", f.read(4))[0]
                        vy336 = unpack("<f", f.read(4))[0]
                        vz336 = unpack("<f", f.read(4))[0]
                        type336 = unpack("B", f.read(1))[0]
                        value1a336 = unpack("B", f.read(1))[0]
                        normalZ_336 = unpack("<h", f.read(2))[0]
                        vx337 = unpack("<f", f.read(4))[0]
                        vy337 = unpack("<f", f.read(4))[0]
                        vz337 = unpack("<f", f.read(4))[0]
                        type337 = unpack("B", f.read(1))[0]
                        value1a337 = unpack("B", f.read(1))[0]
                        normalZ_337 = unpack("<h", f.read(2))[0]
                        vx338 = unpack("<f", f.read(4))[0]
                        vy338 = unpack("<f", f.read(4))[0]
                        vz338 = unpack("<f", f.read(4))[0]
                        type338 = unpack("B", f.read(1))[0]
                        value1a338 = unpack("B", f.read(1))[0]
                        normalZ_338 = unpack("<h", f.read(2))[0]
                        vx339 = unpack("<f", f.read(4))[0]
                        vy339 = unpack("<f", f.read(4))[0]
                        vz339 = unpack("<f", f.read(4))[0]
                        type339 = unpack("B", f.read(1))[0]
                        value1a339 = unpack("B", f.read(1))[0]
                        normalZ_339 = unpack("<h", f.read(2))[0]
                        vx340 = unpack("<f", f.read(4))[0]
                        vy340 = unpack("<f", f.read(4))[0]
                        vz340 = unpack("<f", f.read(4))[0]
                        type340 = unpack("B", f.read(1))[0]
                        value1a340 = unpack("B", f.read(1))[0]
                        normalZ_340 = unpack("<h", f.read(2))[0]
                        vx340 = unpack("<f", f.read(4))[0]
                        vy340 = unpack("<f", f.read(4))[0]
                        vz340 = unpack("<f", f.read(4))[0]
                        type340 = unpack("B", f.read(1))[0]
                        value1a340 = unpack("B", f.read(1))[0]
                        normalZ_340 = unpack("<h", f.read(2))[0]
                        vx341 = unpack("<f", f.read(4))[0]
                        vy341 = unpack("<f", f.read(4))[0]
                        vz341 = unpack("<f", f.read(4))[0]
                        type341 = unpack("B", f.read(1))[0]
                        value1a341 = unpack("B", f.read(1))[0]
                        normalZ_341 = unpack("<h", f.read(2))[0]
                        vx342 = unpack("<f", f.read(4))[0]
                        vy342 = unpack("<f", f.read(4))[0]
                        vz342 = unpack("<f", f.read(4))[0]
                        type342 = unpack("B", f.read(1))[0]
                        value1a342 = unpack("B", f.read(1))[0]
                        normalZ_342 = unpack("<h", f.read(2))[0]
                        vx343 = unpack("<f", f.read(4))[0]
                        vy343 = unpack("<f", f.read(4))[0]
                        vz343 = unpack("<f", f.read(4))[0]
                        type343 = unpack("B", f.read(1))[0]
                        value1a343 = unpack("B", f.read(1))[0]
                        normalZ_343 = unpack("<h", f.read(2))[0]
                        vx344 = unpack("<f", f.read(4))[0]
                        vy344 = unpack("<f", f.read(4))[0]
                        vz344 = unpack("<f", f.read(4))[0]
                        type344 = unpack("B", f.read(1))[0]
                        value1a344 = unpack("B", f.read(1))[0]
                        normalZ_344 = unpack("<h", f.read(2))[0]
                        vx345 = unpack("<f", f.read(4))[0]
                        vy345 = unpack("<f", f.read(4))[0]
                        vz345 = unpack("<f", f.read(4))[0]
                        type345 = unpack("B", f.read(1))[0]
                        value1a345 = unpack("B", f.read(1))[0]
                        normalZ_345 = unpack("<h", f.read(2))[0]
                        vx346 = unpack("<f", f.read(4))[0]
                        vy346 = unpack("<f", f.read(4))[0]
                        vz346 = unpack("<f", f.read(4))[0]
                        type346 = unpack("B", f.read(1))[0]
                        value1a346 = unpack("B", f.read(1))[0]
                        normalZ_346 = unpack("<h", f.read(2))[0]
                        vx347 = unpack("<f", f.read(4))[0]
                        vy347 = unpack("<f", f.read(4))[0]
                        vz347 = unpack("<f", f.read(4))[0]
                        type347 = unpack("B", f.read(1))[0]
                        value1a347 = unpack("B", f.read(1))[0]
                        normalZ_347 = unpack("<h", f.read(2))[0]
                        vertices.append([vx322,vz322,vy322])
                        vertices.append([vx323,vz323,vy323])
                        vertices.append([vx324,vz324,vy324])
                        vertices.append([vx325,vz325,vy325])
                        vertices.append([vx326,vz326,vy326])
                        vertices.append([vx327,vz327,vy327])
                        vertices.append([vx328,vz328,vy328])
                        vertices.append([vx329,vz329,vy329])
                        vertices.append([vx330,vz330,vy330])
                        vertices.append([vx331,vz331,vy331])
                        vertices.append([vx332,vz332,vy332])
                        vertices.append([vx333,vz333,vy333])
                        vertices.append([vx334,vz334,vy334])
                        vertices.append([vx335,vz335,vy335])
                        vertices.append([vx336,vz336,vy336])
                        vertices.append([vx337,vz337,vy337])
                        vertices.append([vx338,vz338,vy338])
                        vertices.append([vx339,vz339,vy339])
                        vertices.append([vx340,vz340,vy340])
                        vertices.append([vx341,vz341,vy341])
                        vertices.append([vx342,vz342,vy342])
                        vertices.append([vx343,vz343,vy343])
                        vertices.append([vx344,vz344,vy344])
                        vertices.append([vx345,vz345,vy345])
                        vertices.append([vx346,vz346,vy346])
                        vertices.append([vx347,vz347,vy347])
                elif vertexCount == 27:
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
                        vx348 = unpack("<f", f.read(4))[0]
                        vy348 = unpack("<f", f.read(4))[0]
                        vz348 = unpack("<f", f.read(4))[0]
                        type348 = unpack("B", f.read(1))[0]
                        value1a348 = unpack("B", f.read(1))[0]
                        normalZ_348 = unpack("<h", f.read(2))[0]
                        vx349 = unpack("<f", f.read(4))[0]
                        vy349 = unpack("<f", f.read(4))[0]
                        vz349 = unpack("<f", f.read(4))[0]
                        type349 = unpack("B", f.read(1))[0]
                        value1a349 = unpack("B", f.read(1))[0]
                        normalZ_349 = unpack("<h", f.read(2))[0]
                        vx350 = unpack("<f", f.read(4))[0]
                        vy350 = unpack("<f", f.read(4))[0]
                        vz350 = unpack("<f", f.read(4))[0]
                        type350 = unpack("B", f.read(1))[0]
                        value1a350 = unpack("B", f.read(1))[0]
                        normalZ_350 = unpack("<h", f.read(2))[0]
                        vx351 = unpack("<f", f.read(4))[0]
                        vy351 = unpack("<f", f.read(4))[0]
                        vz351 = unpack("<f", f.read(4))[0]
                        type351 = unpack("B", f.read(1))[0]
                        value1a351 = unpack("B", f.read(1))[0]
                        normalZ_351 = unpack("<h", f.read(2))[0]
                        vx352 = unpack("<f", f.read(4))[0]
                        vy352 = unpack("<f", f.read(4))[0]
                        vz352 = unpack("<f", f.read(4))[0]
                        type352 = unpack("B", f.read(1))[0]
                        value1a352 = unpack("B", f.read(1))[0]
                        normalZ_352 = unpack("<h", f.read(2))[0]
                        vx353 = unpack("<f", f.read(4))[0]
                        vy353 = unpack("<f", f.read(4))[0]
                        vz353 = unpack("<f", f.read(4))[0]
                        type353 = unpack("B", f.read(1))[0]
                        value1a353 = unpack("B", f.read(1))[0]
                        normalZ_353 = unpack("<h", f.read(2))[0]
                        vx354 = unpack("<f", f.read(4))[0]
                        vy354 = unpack("<f", f.read(4))[0]
                        vz354 = unpack("<f", f.read(4))[0]
                        type354 = unpack("B", f.read(1))[0]
                        value1a354 = unpack("B", f.read(1))[0]
                        normalZ_354 = unpack("<h", f.read(2))[0]
                        vx355 = unpack("<f", f.read(4))[0]
                        vy355 = unpack("<f", f.read(4))[0]
                        vz355 = unpack("<f", f.read(4))[0]
                        type355 = unpack("B", f.read(1))[0]
                        value1a355 = unpack("B", f.read(1))[0]
                        normalZ_355 = unpack("<h", f.read(2))[0]
                        vx356 = unpack("<f", f.read(4))[0]
                        vy356 = unpack("<f", f.read(4))[0]
                        vz356 = unpack("<f", f.read(4))[0]
                        type356 = unpack("B", f.read(1))[0]
                        value1a356 = unpack("B", f.read(1))[0]
                        normalZ_356 = unpack("<h", f.read(2))[0]
                        vx357 = unpack("<f", f.read(4))[0]
                        vy357 = unpack("<f", f.read(4))[0]
                        vz357 = unpack("<f", f.read(4))[0]
                        type357 = unpack("B", f.read(1))[0]
                        value1a357 = unpack("B", f.read(1))[0]
                        normalZ_357 = unpack("<h", f.read(2))[0]
                        vx358 = unpack("<f", f.read(4))[0]
                        vy358 = unpack("<f", f.read(4))[0]
                        vz358 = unpack("<f", f.read(4))[0]
                        type358 = unpack("B", f.read(1))[0]
                        value1a358 = unpack("B", f.read(1))[0]
                        normalZ_358 = unpack("<h", f.read(2))[0]
                        vx359 = unpack("<f", f.read(4))[0]
                        vy359 = unpack("<f", f.read(4))[0]
                        vz359 = unpack("<f", f.read(4))[0]
                        type359 = unpack("B", f.read(1))[0]
                        value1a359 = unpack("B", f.read(1))[0]
                        normalZ_359 = unpack("<h", f.read(2))[0]
                        vx360 = unpack("<f", f.read(4))[0]
                        vy360 = unpack("<f", f.read(4))[0]
                        vz360 = unpack("<f", f.read(4))[0]
                        type360 = unpack("B", f.read(1))[0]
                        value1a360 = unpack("B", f.read(1))[0]
                        normalZ_360 = unpack("<h", f.read(2))[0]
                        vx361 = unpack("<f", f.read(4))[0]
                        vy361 = unpack("<f", f.read(4))[0]
                        vz361 = unpack("<f", f.read(4))[0]
                        type361 = unpack("B", f.read(1))[0]
                        value1a361 = unpack("B", f.read(1))[0]
                        normalZ_361 = unpack("<h", f.read(2))[0]
                        vx362 = unpack("<f", f.read(4))[0]
                        vy362 = unpack("<f", f.read(4))[0]
                        vz362 = unpack("<f", f.read(4))[0]
                        type362 = unpack("B", f.read(1))[0]
                        value1a362 = unpack("B", f.read(1))[0]
                        normalZ_362 = unpack("<h", f.read(2))[0]
                        vx363 = unpack("<f", f.read(4))[0]
                        vy363 = unpack("<f", f.read(4))[0]
                        vz363 = unpack("<f", f.read(4))[0]
                        type363 = unpack("B", f.read(1))[0]
                        value1a363 = unpack("B", f.read(1))[0]
                        normalZ_363 = unpack("<h", f.read(2))[0]
                        vx364 = unpack("<f", f.read(4))[0]
                        vy364 = unpack("<f", f.read(4))[0]
                        vz364 = unpack("<f", f.read(4))[0]
                        type364 = unpack("B", f.read(1))[0]
                        value1a364 = unpack("B", f.read(1))[0]
                        normalZ_364 = unpack("<h", f.read(2))[0]
                        vx365 = unpack("<f", f.read(4))[0]
                        vy365 = unpack("<f", f.read(4))[0]
                        vz365 = unpack("<f", f.read(4))[0]
                        type365 = unpack("B", f.read(1))[0]
                        value1a365 = unpack("B", f.read(1))[0]
                        normalZ_365 = unpack("<h", f.read(2))[0]
                        vx366 = unpack("<f", f.read(4))[0]
                        vy366 = unpack("<f", f.read(4))[0]
                        vz366 = unpack("<f", f.read(4))[0]
                        type366 = unpack("B", f.read(1))[0]
                        value1a366 = unpack("B", f.read(1))[0]
                        normalZ_366 = unpack("<h", f.read(2))[0]
                        vx367 = unpack("<f", f.read(4))[0]
                        vy367 = unpack("<f", f.read(4))[0]
                        vz367 = unpack("<f", f.read(4))[0]
                        type367 = unpack("B", f.read(1))[0]
                        value1a367 = unpack("B", f.read(1))[0]
                        normalZ_367 = unpack("<h", f.read(2))[0]
                        vx368 = unpack("<f", f.read(4))[0]
                        vy368 = unpack("<f", f.read(4))[0]
                        vz368 = unpack("<f", f.read(4))[0]
                        type368 = unpack("B", f.read(1))[0]
                        value1a368 = unpack("B", f.read(1))[0]
                        normalZ_368 = unpack("<h", f.read(2))[0]
                        vx369 = unpack("<f", f.read(4))[0]
                        vy369 = unpack("<f", f.read(4))[0]
                        vz369 = unpack("<f", f.read(4))[0]
                        type369 = unpack("B", f.read(1))[0]
                        value1a369 = unpack("B", f.read(1))[0]
                        normalZ_369 = unpack("<h", f.read(2))[0]
                        vx370 = unpack("<f", f.read(4))[0]
                        vy370 = unpack("<f", f.read(4))[0]
                        vz370 = unpack("<f", f.read(4))[0]
                        type370 = unpack("B", f.read(1))[0]
                        value1a370 = unpack("B", f.read(1))[0]
                        normalZ_370 = unpack("<h", f.read(2))[0]
                        vx371 = unpack("<f", f.read(4))[0]
                        vy371 = unpack("<f", f.read(4))[0]
                        vz371 = unpack("<f", f.read(4))[0]
                        type371 = unpack("B", f.read(1))[0]
                        value1a371 = unpack("B", f.read(1))[0]
                        normalZ_371 = unpack("<h", f.read(2))[0]
                        vx372 = unpack("<f", f.read(4))[0]
                        vy372 = unpack("<f", f.read(4))[0]
                        vz372 = unpack("<f", f.read(4))[0]
                        type372 = unpack("B", f.read(1))[0]
                        value1a372 = unpack("B", f.read(1))[0]
                        normalZ_372 = unpack("<h", f.read(2))[0]
                        vx373 = unpack("<f", f.read(4))[0]
                        vy373 = unpack("<f", f.read(4))[0]
                        vz373 = unpack("<f", f.read(4))[0]
                        type373 = unpack("B", f.read(1))[0]
                        value1a373 = unpack("B", f.read(1))[0]
                        normalZ_373 = unpack("<h", f.read(2))[0]
                        vx374 = unpack("<f", f.read(4))[0]
                        vy374 = unpack("<f", f.read(4))[0]
                        vz374 = unpack("<f", f.read(4))[0]
                        type374 = unpack("B", f.read(1))[0]
                        value1a374 = unpack("B", f.read(1))[0]
                        normalZ_374 = unpack("<h", f.read(2))[0]
                        vertices.append([vx348,vz348,vy348])
                        vertices.append([vx349,vz349,vy349])
                        vertices.append([vx350,vz350,vy350])
                        vertices.append([vx351,vz351,vy351])
                        vertices.append([vx352,vz352,vy352])
                        vertices.append([vx353,vz353,vy353])
                        vertices.append([vx354,vz354,vy354])
                        vertices.append([vx355,vz355,vy355])
                        vertices.append([vx356,vz356,vy356])
                        vertices.append([vx357,vz357,vy357])
                        vertices.append([vx358,vz358,vy358])
                        vertices.append([vx359,vz359,vy359])
                        vertices.append([vx360,vz360,vy360])
                        vertices.append([vx361,vz361,vy361])
                        vertices.append([vx362,vz362,vy362])
                        vertices.append([vx363,vz363,vy363])
                        vertices.append([vx364,vz364,vy364])
                        vertices.append([vx365,vz365,vy365])
                        vertices.append([vx366,vz366,vy366])
                        vertices.append([vx367,vz367,vy367])
                        vertices.append([vx368,vz368,vy368])
                        vertices.append([vx369,vz369,vy369])
                        vertices.append([vx370,vz370,vy370])
                        vertices.append([vx371,vz371,vy371])
                        vertices.append([vx372,vz372,vy372])
                        vertices.append([vx373,vz373,vy373])
                        vertices.append([vx374,vz374,vy374])

                elif vertexCount == 28:
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
                        vx375 = unpack("<f", f.read(4))[0]
                        vy375 = unpack("<f", f.read(4))[0]
                        vz375 = unpack("<f", f.read(4))[0]
                        type375 = unpack("B", f.read(1))[0]
                        value1a375 = unpack("B", f.read(1))[0]
                        normalZ_375 = unpack("<h", f.read(2))[0]
                        vx376 = unpack("<f", f.read(4))[0]
                        vy376 = unpack("<f", f.read(4))[0]
                        vz376 = unpack("<f", f.read(4))[0]
                        type376 = unpack("B", f.read(1))[0]
                        value1a376 = unpack("B", f.read(1))[0]
                        normalZ_376 = unpack("<h", f.read(2))[0]
                        vx377 = unpack("<f", f.read(4))[0]
                        vy377 = unpack("<f", f.read(4))[0]
                        vz377 = unpack("<f", f.read(4))[0]
                        type377 = unpack("B", f.read(1))[0]
                        value1a377 = unpack("B", f.read(1))[0]
                        normalZ_377 = unpack("<h", f.read(2))[0]
                        vx378 = unpack("<f", f.read(4))[0]
                        vy378 = unpack("<f", f.read(4))[0]
                        vz378 = unpack("<f", f.read(4))[0]
                        type378 = unpack("B", f.read(1))[0]
                        value1a378 = unpack("B", f.read(1))[0]
                        normalZ_378 = unpack("<h", f.read(2))[0]
                        vx379 = unpack("<f", f.read(4))[0]
                        vy379 = unpack("<f", f.read(4))[0]
                        vz379 = unpack("<f", f.read(4))[0]
                        type379 = unpack("B", f.read(1))[0]
                        value1a379 = unpack("B", f.read(1))[0]
                        normalZ_379 = unpack("<h", f.read(2))[0]
                        vx380 = unpack("<f", f.read(4))[0]
                        vy380 = unpack("<f", f.read(4))[0]
                        vz380 = unpack("<f", f.read(4))[0]
                        type380 = unpack("B", f.read(1))[0]
                        value1a380 = unpack("B", f.read(1))[0]
                        normalZ_380 = unpack("<h", f.read(2))[0]
                        vx381 = unpack("<f", f.read(4))[0]
                        vy381 = unpack("<f", f.read(4))[0]
                        vz381 = unpack("<f", f.read(4))[0]
                        type381 = unpack("B", f.read(1))[0]
                        value1a381 = unpack("B", f.read(1))[0]
                        normalZ_381 = unpack("<h", f.read(2))[0]
                        vx382 = unpack("<f", f.read(4))[0]
                        vy382 = unpack("<f", f.read(4))[0]
                        vz382 = unpack("<f", f.read(4))[0]
                        type382 = unpack("B", f.read(1))[0]
                        value1a382 = unpack("B", f.read(1))[0]
                        normalZ_382 = unpack("<h", f.read(2))[0]
                        vx383 = unpack("<f", f.read(4))[0]
                        vy383 = unpack("<f", f.read(4))[0]
                        vz383 = unpack("<f", f.read(4))[0]
                        type383 = unpack("B", f.read(1))[0]
                        value1a383 = unpack("B", f.read(1))[0]
                        normalZ_383 = unpack("<h", f.read(2))[0]
                        vx384 = unpack("<f", f.read(4))[0]
                        vy384 = unpack("<f", f.read(4))[0]
                        vz384 = unpack("<f", f.read(4))[0]
                        type384 = unpack("B", f.read(1))[0]
                        value1a384 = unpack("B", f.read(1))[0]
                        normalZ_384 = unpack("<h", f.read(2))[0]
                        vx385 = unpack("<f", f.read(4))[0]
                        vy385 = unpack("<f", f.read(4))[0]
                        vz385 = unpack("<f", f.read(4))[0]
                        type385 = unpack("B", f.read(1))[0]
                        value1a385 = unpack("B", f.read(1))[0]
                        normalZ_385 = unpack("<h", f.read(2))[0]
                        vx386 = unpack("<f", f.read(4))[0]
                        vy386 = unpack("<f", f.read(4))[0]
                        vz386 = unpack("<f", f.read(4))[0]
                        type386 = unpack("B", f.read(1))[0]
                        value1a386 = unpack("B", f.read(1))[0]
                        normalZ_386 = unpack("<h", f.read(2))[0]
                        vx387 = unpack("<f", f.read(4))[0]
                        vy387 = unpack("<f", f.read(4))[0]
                        vz387 = unpack("<f", f.read(4))[0]
                        type387 = unpack("B", f.read(1))[0]
                        value1a387 = unpack("B", f.read(1))[0]
                        normalZ_387 = unpack("<h", f.read(2))[0]
                        vx388 = unpack("<f", f.read(4))[0]
                        vy388 = unpack("<f", f.read(4))[0]
                        vz388 = unpack("<f", f.read(4))[0]
                        type388 = unpack("B", f.read(1))[0]
                        value1a388 = unpack("B", f.read(1))[0]
                        normalZ_388 = unpack("<h", f.read(2))[0]
                        vx389 = unpack("<f", f.read(4))[0]
                        vy389 = unpack("<f", f.read(4))[0]
                        vz389 = unpack("<f", f.read(4))[0]
                        type389 = unpack("B", f.read(1))[0]
                        value1a389 = unpack("B", f.read(1))[0]
                        normalZ_389 = unpack("<h", f.read(2))[0]
                        vx390 = unpack("<f", f.read(4))[0]
                        vy390 = unpack("<f", f.read(4))[0]
                        vz390 = unpack("<f", f.read(4))[0]
                        type390 = unpack("B", f.read(1))[0]
                        value1a390 = unpack("B", f.read(1))[0]
                        normalZ_390 = unpack("<h", f.read(2))[0]
                        vx391 = unpack("<f", f.read(4))[0]
                        vy391 = unpack("<f", f.read(4))[0]
                        vz391 = unpack("<f", f.read(4))[0]
                        type391 = unpack("B", f.read(1))[0]
                        value1a391 = unpack("B", f.read(1))[0]
                        normalZ_391 = unpack("<h", f.read(2))[0]
                        vx392 = unpack("<f", f.read(4))[0]
                        vy392 = unpack("<f", f.read(4))[0]
                        vz392 = unpack("<f", f.read(4))[0]
                        type392 = unpack("B", f.read(1))[0]
                        value1a392 = unpack("B", f.read(1))[0]
                        normalZ_392 = unpack("<h", f.read(2))[0]
                        vx393 = unpack("<f", f.read(4))[0]
                        vy393 = unpack("<f", f.read(4))[0]
                        vz393 = unpack("<f", f.read(4))[0]
                        type393 = unpack("B", f.read(1))[0]
                        value1a393 = unpack("B", f.read(1))[0]
                        normalZ_393 = unpack("<h", f.read(2))[0]
                        vx394 = unpack("<f", f.read(4))[0]
                        vy394 = unpack("<f", f.read(4))[0]
                        vz394 = unpack("<f", f.read(4))[0]
                        type394 = unpack("B", f.read(1))[0]
                        value1a394 = unpack("B", f.read(1))[0]
                        normalZ_394 = unpack("<h", f.read(2))[0]
                        vx395 = unpack("<f", f.read(4))[0]
                        vy395 = unpack("<f", f.read(4))[0]
                        vz395 = unpack("<f", f.read(4))[0]
                        type395 = unpack("B", f.read(1))[0]
                        value1a395 = unpack("B", f.read(1))[0]
                        normalZ_395 = unpack("<h", f.read(2))[0]
                        vx396 = unpack("<f", f.read(4))[0]
                        vy396 = unpack("<f", f.read(4))[0]
                        vz396 = unpack("<f", f.read(4))[0]
                        type396 = unpack("B", f.read(1))[0]
                        value1a396 = unpack("B", f.read(1))[0]
                        normalZ_396 = unpack("<h", f.read(2))[0]
                        vx397 = unpack("<f", f.read(4))[0]
                        vy397 = unpack("<f", f.read(4))[0]
                        vz397 = unpack("<f", f.read(4))[0]
                        type397 = unpack("B", f.read(1))[0]
                        value1a397 = unpack("B", f.read(1))[0]
                        normalZ_397 = unpack("<h", f.read(2))[0]
                        vx398 = unpack("<f", f.read(4))[0]
                        vy398 = unpack("<f", f.read(4))[0]
                        vz398 = unpack("<f", f.read(4))[0]
                        type398 = unpack("B", f.read(1))[0]
                        value1a398 = unpack("B", f.read(1))[0]
                        normalZ_398 = unpack("<h", f.read(2))[0]
                        vx399 = unpack("<f", f.read(4))[0]
                        vy399 = unpack("<f", f.read(4))[0]
                        vz399 = unpack("<f", f.read(4))[0]
                        type399 = unpack("B", f.read(1))[0]
                        value1a399 = unpack("B", f.read(1))[0]
                        normalZ_399 = unpack("<h", f.read(2))[0]
                        vx400 = unpack("<f", f.read(4))[0]
                        vy400 = unpack("<f", f.read(4))[0]
                        vz400 = unpack("<f", f.read(4))[0]
                        type400 = unpack("B", f.read(1))[0]
                        value1a400 = unpack("B", f.read(1))[0]
                        normalZ_400 = unpack("<h", f.read(2))[0]
                        vx401 = unpack("<f", f.read(4))[0]
                        vy401 = unpack("<f", f.read(4))[0]
                        vz401 = unpack("<f", f.read(4))[0]
                        type401 = unpack("B", f.read(1))[0]
                        value1a401 = unpack("B", f.read(1))[0]
                        normalZ_401 = unpack("<h", f.read(2))[0]
                        vx402 = unpack("<f", f.read(4))[0]
                        vy402 = unpack("<f", f.read(4))[0]
                        vz402 = unpack("<f", f.read(4))[0]
                        type402 = unpack("B", f.read(1))[0]
                        value1a402 = unpack("B", f.read(1))[0]
                        normalZ_402 = unpack("<h", f.read(2))[0]
                        vertices.append([vx375,vz375,vy375])
                        vertices.append([vx376,vz376,vy376])
                        vertices.append([vx377,vz377,vy377])
                        vertices.append([vx378,vz378,vy378])
                        vertices.append([vx379,vz379,vy379])
                        vertices.append([vx380,vz380,vy380])
                        vertices.append([vx381,vz381,vy381])
                        vertices.append([vx382,vz382,vy382])
                        vertices.append([vx383,vz383,vy383])
                        vertices.append([vx384,vz384,vy384])
                        vertices.append([vx385,vz385,vy385])
                        vertices.append([vx386,vz386,vy386])
                        vertices.append([vx387,vz387,vy387])
                        vertices.append([vx388,vz388,vy388])
                        vertices.append([vx389,vz389,vy389])
                        vertices.append([vx390,vz390,vy390])
                        vertices.append([vx391,vz391,vy391])
                        vertices.append([vx392,vz392,vy392])
                        vertices.append([vx393,vz393,vy393])
                        vertices.append([vx394,vz394,vy394])
                        vertices.append([vx395,vz395,vy395])
                        vertices.append([vx396,vz396,vy396])
                        vertices.append([vx397,vz397,vy397])
                        vertices.append([vx398,vz398,vy398])
                        vertices.append([vx399,vz399,vy399])
                        vertices.append([vx400,vz400,vy400])
                        vertices.append([vx401,vz401,vy401])
                        vertices.append([vx402,vz402,vy402])

                elif vertexCount == 29:
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
                        vx403 = unpack("<f", f.read(4))[0]
                        vy403 = unpack("<f", f.read(4))[0]
                        vz403 = unpack("<f", f.read(4))[0]
                        type403 = unpack("B", f.read(1))[0]
                        value1a403 = unpack("B", f.read(1))[0]
                        normalZ_403 = unpack("<h", f.read(2))[0]
                        vx404 = unpack("<f", f.read(4))[0]
                        vy404 = unpack("<f", f.read(4))[0]
                        vz404 = unpack("<f", f.read(4))[0]
                        type404 = unpack("B", f.read(1))[0]
                        value1a404 = unpack("B", f.read(1))[0]
                        normalZ_404 = unpack("<h", f.read(2))[0]
                        vx405 = unpack("<f", f.read(4))[0]
                        vy405 = unpack("<f", f.read(4))[0]
                        vz405 = unpack("<f", f.read(4))[0]
                        type405 = unpack("B", f.read(1))[0]
                        value1a405 = unpack("B", f.read(1))[0]
                        normalZ_405 = unpack("<h", f.read(2))[0]
                        vx406 = unpack("<f", f.read(4))[0]
                        vy406 = unpack("<f", f.read(4))[0]
                        vz406 = unpack("<f", f.read(4))[0]
                        type406 = unpack("B", f.read(1))[0]
                        value1a406 = unpack("B", f.read(1))[0]
                        normalZ_406 = unpack("<h", f.read(2))[0]
                        vx407 = unpack("<f", f.read(4))[0]
                        vy407 = unpack("<f", f.read(4))[0]
                        vz407 = unpack("<f", f.read(4))[0]
                        type407 = unpack("B", f.read(1))[0]
                        value1a407 = unpack("B", f.read(1))[0]
                        normalZ_407 = unpack("<h", f.read(2))[0]
                        vx408 = unpack("<f", f.read(4))[0]
                        vy408 = unpack("<f", f.read(4))[0]
                        vz408 = unpack("<f", f.read(4))[0]
                        type408 = unpack("B", f.read(1))[0]
                        value1a408 = unpack("B", f.read(1))[0]
                        normalZ_408 = unpack("<h", f.read(2))[0]
                        vx409 = unpack("<f", f.read(4))[0]
                        vy409 = unpack("<f", f.read(4))[0]
                        vz409 = unpack("<f", f.read(4))[0]
                        type409 = unpack("B", f.read(1))[0]
                        value1a409 = unpack("B", f.read(1))[0]
                        normalZ_409 = unpack("<h", f.read(2))[0]
                        vx410 = unpack("<f", f.read(4))[0]
                        vy410 = unpack("<f", f.read(4))[0]
                        vz410 = unpack("<f", f.read(4))[0]
                        type410 = unpack("B", f.read(1))[0]
                        value1a410 = unpack("B", f.read(1))[0]
                        normalZ_410 = unpack("<h", f.read(2))[0]
                        vx411 = unpack("<f", f.read(4))[0]
                        vy411 = unpack("<f", f.read(4))[0]
                        vz411 = unpack("<f", f.read(4))[0]
                        type411 = unpack("B", f.read(1))[0]
                        value1a411 = unpack("B", f.read(1))[0]
                        normalZ_411 = unpack("<h", f.read(2))[0]
                        vx412 = unpack("<f", f.read(4))[0]
                        vy412 = unpack("<f", f.read(4))[0]
                        vz412 = unpack("<f", f.read(4))[0]
                        type412 = unpack("B", f.read(1))[0]
                        value1a412 = unpack("B", f.read(1))[0]
                        normalZ_412 = unpack("<h", f.read(2))[0]
                        vx413 = unpack("<f", f.read(4))[0]
                        vy413 = unpack("<f", f.read(4))[0]
                        vz413 = unpack("<f", f.read(4))[0]
                        type413 = unpack("B", f.read(1))[0]
                        value1a413 = unpack("B", f.read(1))[0]
                        normalZ_413 = unpack("<h", f.read(2))[0]
                        vx414 = unpack("<f", f.read(4))[0]
                        vy414 = unpack("<f", f.read(4))[0]
                        vz414 = unpack("<f", f.read(4))[0]
                        type414 = unpack("B", f.read(1))[0]
                        value1a414 = unpack("B", f.read(1))[0]
                        normalZ_414 = unpack("<h", f.read(2))[0]
                        vx415 = unpack("<f", f.read(4))[0]
                        vy415 = unpack("<f", f.read(4))[0]
                        vz415 = unpack("<f", f.read(4))[0]
                        type415 = unpack("B", f.read(1))[0]
                        value1a415 = unpack("B", f.read(1))[0]
                        normalZ_415 = unpack("<h", f.read(2))[0]
                        vx416 = unpack("<f", f.read(4))[0]
                        vy416 = unpack("<f", f.read(4))[0]
                        vz416 = unpack("<f", f.read(4))[0]
                        type416 = unpack("B", f.read(1))[0]
                        value1a416 = unpack("B", f.read(1))[0]
                        normalZ_416 = unpack("<h", f.read(2))[0]
                        vx417 = unpack("<f", f.read(4))[0]
                        vy417 = unpack("<f", f.read(4))[0]
                        vz417 = unpack("<f", f.read(4))[0]
                        type417 = unpack("B", f.read(1))[0]
                        value1a417 = unpack("B", f.read(1))[0]
                        normalZ_417 = unpack("<h", f.read(2))[0]
                        vx418 = unpack("<f", f.read(4))[0]
                        vy418 = unpack("<f", f.read(4))[0]
                        vz418 = unpack("<f", f.read(4))[0]
                        type418 = unpack("B", f.read(1))[0]
                        value1a418 = unpack("B", f.read(1))[0]
                        normalZ_418 = unpack("<h", f.read(2))[0]
                        vx419 = unpack("<f", f.read(4))[0]
                        vy419 = unpack("<f", f.read(4))[0]
                        vz419 = unpack("<f", f.read(4))[0]
                        type419 = unpack("B", f.read(1))[0]
                        value1a419 = unpack("B", f.read(1))[0]
                        normalZ_419 = unpack("<h", f.read(2))[0]
                        vx420 = unpack("<f", f.read(4))[0]
                        vy420 = unpack("<f", f.read(4))[0]
                        vz420 = unpack("<f", f.read(4))[0]
                        type420 = unpack("B", f.read(1))[0]
                        value1a420 = unpack("B", f.read(1))[0]
                        normalZ_420 = unpack("<h", f.read(2))[0]
                        vx421 = unpack("<f", f.read(4))[0]
                        vy421 = unpack("<f", f.read(4))[0]
                        vz421 = unpack("<f", f.read(4))[0]
                        type421 = unpack("B", f.read(1))[0]
                        value1a421 = unpack("B", f.read(1))[0]
                        normalZ_421 = unpack("<h", f.read(2))[0]
                        vx422 = unpack("<f", f.read(4))[0]
                        vy422 = unpack("<f", f.read(4))[0]
                        vz422 = unpack("<f", f.read(4))[0]
                        type422 = unpack("B", f.read(1))[0]
                        value1a422 = unpack("B", f.read(1))[0]
                        normalZ_422 = unpack("<h", f.read(2))[0]
                        vx423 = unpack("<f", f.read(4))[0]
                        vy423 = unpack("<f", f.read(4))[0]
                        vz423 = unpack("<f", f.read(4))[0]
                        type423 = unpack("B", f.read(1))[0]
                        value1a423 = unpack("B", f.read(1))[0]
                        normalZ_423 = unpack("<h", f.read(2))[0]
                        vx424 = unpack("<f", f.read(4))[0]
                        vy424 = unpack("<f", f.read(4))[0]
                        vz424 = unpack("<f", f.read(4))[0]
                        type424 = unpack("B", f.read(1))[0]
                        value1a424 = unpack("B", f.read(1))[0]
                        normalZ_424 = unpack("<h", f.read(2))[0]
                        vx425 = unpack("<f", f.read(4))[0]
                        vy425 = unpack("<f", f.read(4))[0]
                        vz425 = unpack("<f", f.read(4))[0]
                        type425 = unpack("B", f.read(1))[0]
                        value1a425 = unpack("B", f.read(1))[0]
                        normalZ_425 = unpack("<h", f.read(2))[0]
                        vx426 = unpack("<f", f.read(4))[0]
                        vy426 = unpack("<f", f.read(4))[0]
                        vz426 = unpack("<f", f.read(4))[0]
                        type426 = unpack("B", f.read(1))[0]
                        value1a426 = unpack("B", f.read(1))[0]
                        normalZ_426 = unpack("<h", f.read(2))[0]
                        vx427 = unpack("<f", f.read(4))[0]
                        vy427 = unpack("<f", f.read(4))[0]
                        vz427 = unpack("<f", f.read(4))[0]
                        type427 = unpack("B", f.read(1))[0]
                        value1a427 = unpack("B", f.read(1))[0]
                        normalZ_427 = unpack("<h", f.read(2))[0]
                        vx428 = unpack("<f", f.read(4))[0]
                        vy428 = unpack("<f", f.read(4))[0]
                        vz428 = unpack("<f", f.read(4))[0]
                        type428 = unpack("B", f.read(1))[0]
                        value1a428 = unpack("B", f.read(1))[0]
                        normalZ_428 = unpack("<h", f.read(2))[0]
                        vx429 = unpack("<f", f.read(4))[0]
                        vy429 = unpack("<f", f.read(4))[0]
                        vz429 = unpack("<f", f.read(4))[0]
                        type429 = unpack("B", f.read(1))[0]
                        value1a429 = unpack("B", f.read(1))[0]
                        normalZ_429 = unpack("<h", f.read(2))[0]
                        vx430 = unpack("<f", f.read(4))[0]
                        vy430 = unpack("<f", f.read(4))[0]
                        vz430 = unpack("<f", f.read(4))[0]
                        type430 = unpack("B", f.read(1))[0]
                        value1a430 = unpack("B", f.read(1))[0]
                        normalZ_430 = unpack("<h", f.read(2))[0]
                        vx431 = unpack("<f", f.read(4))[0]
                        vy431 = unpack("<f", f.read(4))[0]
                        vz431 = unpack("<f", f.read(4))[0]
                        type431 = unpack("B", f.read(1))[0]
                        value1a431 = unpack("B", f.read(1))[0]
                        normalZ_431 = unpack("<h", f.read(2))[0]
                        vertices.append([vx403,vz403,vy403])
                        vertices.append([vx404,vz404,vy404])
                        vertices.append([vx405,vz405,vy405])
                        vertices.append([vx406,vz406,vy406])
                        vertices.append([vx407,vz407,vy407])
                        vertices.append([vx408,vz408,vy408])
                        vertices.append([vx409,vz409,vy409])
                        vertices.append([vx410,vz410,vy410])
                        vertices.append([vx411,vz411,vy411])
                        vertices.append([vx412,vz412,vy412])
                        vertices.append([vx413,vz413,vy413])
                        vertices.append([vx414,vz414,vy414])
                        vertices.append([vx415,vz415,vy415])
                        vertices.append([vx416,vz416,vy416])
                        vertices.append([vx417,vz417,vy417])
                        vertices.append([vx418,vz418,vy418])
                        vertices.append([vx419,vz419,vy419])
                        vertices.append([vx420,vz420,vy420])
                        vertices.append([vx421,vz421,vy421])
                        vertices.append([vx422,vz422,vy422])
                        vertices.append([vx423,vz423,vy423])
                        vertices.append([vx424,vz424,vy424])
                        vertices.append([vx425,vz425,vy425])
                        vertices.append([vx426,vz426,vy426])
                        vertices.append([vx427,vz427,vy427])
                        vertices.append([vx428,vz428,vy428])
                        vertices.append([vx429,vz429,vy429])
                        vertices.append([vx430,vz430,vy430])
                        vertices.append([vx431,vz431,vy431])

                elif vertexCount == 30:
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
                        vx432 = unpack("<f", f.read(4))[0]
                        vy432 = unpack("<f", f.read(4))[0]
                        vz432 = unpack("<f", f.read(4))[0]
                        type432 = unpack("B", f.read(1))[0]
                        value1a432 = unpack("B", f.read(1))[0]
                        normalZ_432 = unpack("<h", f.read(2))[0]
                        vx433 = unpack("<f", f.read(4))[0]
                        vy433 = unpack("<f", f.read(4))[0]
                        vz433 = unpack("<f", f.read(4))[0]
                        type433 = unpack("B", f.read(1))[0]
                        value1a433 = unpack("B", f.read(1))[0]
                        normalZ_433 = unpack("<h", f.read(2))[0]
                        vx434 = unpack("<f", f.read(4))[0]
                        vy434 = unpack("<f", f.read(4))[0]
                        vz434 = unpack("<f", f.read(4))[0]
                        type434 = unpack("B", f.read(1))[0]
                        value1a434 = unpack("B", f.read(1))[0]
                        normalZ_434 = unpack("<h", f.read(2))[0]
                        vx435 = unpack("<f", f.read(4))[0]
                        vy435 = unpack("<f", f.read(4))[0]
                        vz435 = unpack("<f", f.read(4))[0]
                        type435 = unpack("B", f.read(1))[0]
                        value1a435 = unpack("B", f.read(1))[0]
                        normalZ_435 = unpack("<h", f.read(2))[0]
                        vx436 = unpack("<f", f.read(4))[0]
                        vy436 = unpack("<f", f.read(4))[0]
                        vz436 = unpack("<f", f.read(4))[0]
                        type436 = unpack("B", f.read(1))[0]
                        value1a436 = unpack("B", f.read(1))[0]
                        normalZ_436 = unpack("<h", f.read(2))[0]
                        vx437 = unpack("<f", f.read(4))[0]
                        vy437 = unpack("<f", f.read(4))[0]
                        vz437 = unpack("<f", f.read(4))[0]
                        type437 = unpack("B", f.read(1))[0]
                        value1a437 = unpack("B", f.read(1))[0]
                        normalZ_437 = unpack("<h", f.read(2))[0]
                        vx438 = unpack("<f", f.read(4))[0]
                        vy438 = unpack("<f", f.read(4))[0]
                        vz438 = unpack("<f", f.read(4))[0]
                        type438 = unpack("B", f.read(1))[0]
                        value1a438 = unpack("B", f.read(1))[0]
                        normalZ_438 = unpack("<h", f.read(2))[0]
                        vx439 = unpack("<f", f.read(4))[0]
                        vy439 = unpack("<f", f.read(4))[0]
                        vz439 = unpack("<f", f.read(4))[0]
                        type439 = unpack("B", f.read(1))[0]
                        value1a439 = unpack("B", f.read(1))[0]
                        normalZ_439 = unpack("<h", f.read(2))[0]
                        vx440 = unpack("<f", f.read(4))[0]
                        vy440 = unpack("<f", f.read(4))[0]
                        vz440 = unpack("<f", f.read(4))[0]
                        type440 = unpack("B", f.read(1))[0]
                        value1a440 = unpack("B", f.read(1))[0]
                        normalZ_440 = unpack("<h", f.read(2))[0]
                        vx441 = unpack("<f", f.read(4))[0]
                        vy441 = unpack("<f", f.read(4))[0]
                        vz441 = unpack("<f", f.read(4))[0]
                        type441 = unpack("B", f.read(1))[0]
                        value1a441 = unpack("B", f.read(1))[0]
                        normalZ_441 = unpack("<h", f.read(2))[0]
                        vx442 = unpack("<f", f.read(4))[0]
                        vy442 = unpack("<f", f.read(4))[0]
                        vz442 = unpack("<f", f.read(4))[0]
                        type442 = unpack("B", f.read(1))[0]
                        value1a442 = unpack("B", f.read(1))[0]
                        normalZ_442 = unpack("<h", f.read(2))[0]
                        vx443 = unpack("<f", f.read(4))[0]
                        vy443 = unpack("<f", f.read(4))[0]
                        vz443 = unpack("<f", f.read(4))[0]
                        type443 = unpack("B", f.read(1))[0]
                        value1a443 = unpack("B", f.read(1))[0]
                        normalZ_443 = unpack("<h", f.read(2))[0]
                        vx444 = unpack("<f", f.read(4))[0]
                        vy444 = unpack("<f", f.read(4))[0]
                        vz444 = unpack("<f", f.read(4))[0]
                        type444 = unpack("B", f.read(1))[0]
                        value1a444 = unpack("B", f.read(1))[0]
                        normalZ_444 = unpack("<h", f.read(2))[0]
                        vx445 = unpack("<f", f.read(4))[0]
                        vy445 = unpack("<f", f.read(4))[0]
                        vz445 = unpack("<f", f.read(4))[0]
                        type445 = unpack("B", f.read(1))[0]
                        value1a445 = unpack("B", f.read(1))[0]
                        normalZ_445 = unpack("<h", f.read(2))[0]
                        vx446 = unpack("<f", f.read(4))[0]
                        vy446 = unpack("<f", f.read(4))[0]
                        vz446 = unpack("<f", f.read(4))[0]
                        type446 = unpack("B", f.read(1))[0]
                        value1a446 = unpack("B", f.read(1))[0]
                        normalZ_446 = unpack("<h", f.read(2))[0]
                        vx447 = unpack("<f", f.read(4))[0]
                        vy447 = unpack("<f", f.read(4))[0]
                        vz447 = unpack("<f", f.read(4))[0]
                        type447 = unpack("B", f.read(1))[0]
                        value1a447 = unpack("B", f.read(1))[0]
                        normalZ_447 = unpack("<h", f.read(2))[0]
                        vx448 = unpack("<f", f.read(4))[0]
                        vy448 = unpack("<f", f.read(4))[0]
                        vz448 = unpack("<f", f.read(4))[0]
                        type448 = unpack("B", f.read(1))[0]
                        value1a448 = unpack("B", f.read(1))[0]
                        normalZ_448 = unpack("<h", f.read(2))[0]
                        vx449 = unpack("<f", f.read(4))[0]
                        vy449 = unpack("<f", f.read(4))[0]
                        vz449 = unpack("<f", f.read(4))[0]
                        type449 = unpack("B", f.read(1))[0]
                        value1a449 = unpack("B", f.read(1))[0]
                        normalZ_449 = unpack("<h", f.read(2))[0]
                        vx450 = unpack("<f", f.read(4))[0]
                        vy450 = unpack("<f", f.read(4))[0]
                        vz450 = unpack("<f", f.read(4))[0]
                        type450 = unpack("B", f.read(1))[0]
                        value1a450 = unpack("B", f.read(1))[0]
                        normalZ_450 = unpack("<h", f.read(2))[0]
                        vx451 = unpack("<f", f.read(4))[0]
                        vy451 = unpack("<f", f.read(4))[0]
                        vz451 = unpack("<f", f.read(4))[0]
                        type451 = unpack("B", f.read(1))[0]
                        value1a451 = unpack("B", f.read(1))[0]
                        normalZ_451 = unpack("<h", f.read(2))[0]
                        vx452 = unpack("<f", f.read(4))[0]
                        vy452 = unpack("<f", f.read(4))[0]
                        vz452 = unpack("<f", f.read(4))[0]
                        type452 = unpack("B", f.read(1))[0]
                        value1a452 = unpack("B", f.read(1))[0]
                        normalZ_452 = unpack("<h", f.read(2))[0]
                        vx453 = unpack("<f", f.read(4))[0]
                        vy453 = unpack("<f", f.read(4))[0]
                        vz453 = unpack("<f", f.read(4))[0]
                        type453 = unpack("B", f.read(1))[0]
                        value1a453 = unpack("B", f.read(1))[0]
                        normalZ_453 = unpack("<h", f.read(2))[0]
                        vx454 = unpack("<f", f.read(4))[0]
                        vy454 = unpack("<f", f.read(4))[0]
                        vz454 = unpack("<f", f.read(4))[0]
                        type454 = unpack("B", f.read(1))[0]
                        value1a454 = unpack("B", f.read(1))[0]
                        normalZ_454 = unpack("<h", f.read(2))[0]
                        vx455 = unpack("<f", f.read(4))[0]
                        vy455 = unpack("<f", f.read(4))[0]
                        vz455 = unpack("<f", f.read(4))[0]
                        type455 = unpack("B", f.read(1))[0]
                        value1a455 = unpack("B", f.read(1))[0]
                        normalZ_455 = unpack("<h", f.read(2))[0]
                        vx456 = unpack("<f", f.read(4))[0]
                        vy456 = unpack("<f", f.read(4))[0]
                        vz456 = unpack("<f", f.read(4))[0]
                        type456 = unpack("B", f.read(1))[0]
                        value1a456 = unpack("B", f.read(1))[0]
                        normalZ_456 = unpack("<h", f.read(2))[0]
                        vx457 = unpack("<f", f.read(4))[0]
                        vy457 = unpack("<f", f.read(4))[0]
                        vz457 = unpack("<f", f.read(4))[0]
                        type457 = unpack("B", f.read(1))[0]
                        value1a457 = unpack("B", f.read(1))[0]
                        normalZ_457 = unpack("<h", f.read(2))[0]
                        vx458 = unpack("<f", f.read(4))[0]
                        vy458 = unpack("<f", f.read(4))[0]
                        vz458 = unpack("<f", f.read(4))[0]
                        type458 = unpack("B", f.read(1))[0]
                        value1a458 = unpack("B", f.read(1))[0]
                        normalZ_458 = unpack("<h", f.read(2))[0]
                        vx459 = unpack("<f", f.read(4))[0]
                        vy459 = unpack("<f", f.read(4))[0]
                        vz459 = unpack("<f", f.read(4))[0]
                        type459 = unpack("B", f.read(1))[0]
                        value1a459 = unpack("B", f.read(1))[0]
                        normalZ_459 = unpack("<h", f.read(2))[0]
                        vx460 = unpack("<f", f.read(4))[0]
                        vy460 = unpack("<f", f.read(4))[0]
                        vz460 = unpack("<f", f.read(4))[0]
                        type460 = unpack("B", f.read(1))[0]
                        value1a460 = unpack("B", f.read(1))[0]
                        normalZ_460 = unpack("<h", f.read(2))[0]
                        vx461 = unpack("<f", f.read(4))[0]
                        vy461 = unpack("<f", f.read(4))[0]
                        vz461 = unpack("<f", f.read(4))[0]
                        type461 = unpack("B", f.read(1))[0]
                        value1a461 = unpack("B", f.read(1))[0]
                        normalZ_461 = unpack("<h", f.read(2))[0]
                        vertices.append([vx432,vz432,vy432])
                        vertices.append([vx433,vz433,vy433])
                        vertices.append([vx434,vz434,vy434])
                        vertices.append([vx435,vz435,vy435])
                        vertices.append([vx436,vz436,vy436])
                        vertices.append([vx437,vz437,vy437])
                        vertices.append([vx438,vz438,vy438])
                        vertices.append([vx439,vz439,vy439])
                        vertices.append([vx440,vz440,vy440])
                        vertices.append([vx441,vz441,vy441])
                        vertices.append([vx442,vz442,vy442])
                        vertices.append([vx443,vz443,vy443])
                        vertices.append([vx444,vz444,vy444])
                        vertices.append([vx445,vz445,vy445])
                        vertices.append([vx446,vz446,vy446])
                        vertices.append([vx447,vz447,vy447])
                        vertices.append([vx448,vz448,vy448])
                        vertices.append([vx449,vz449,vy449])
                        vertices.append([vx450,vz450,vy450])
                        vertices.append([vx451,vz451,vy451])
                        vertices.append([vx452,vz452,vy452])
                        vertices.append([vx453,vz453,vy453])
                        vertices.append([vx454,vz454,vy454])
                        vertices.append([vx455,vz455,vy455])
                        vertices.append([vx456,vz456,vy456])
                        vertices.append([vx457,vz457,vy457])
                        vertices.append([vx458,vz458,vy458])
                        vertices.append([vx459,vz459,vy459])
                        vertices.append([vx460,vz460,vy460])
                        vertices.append([vx461,vz461,vy461])


                elif vertexCount == 31:
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
                        vx462 = unpack("<f", f.read(4))[0]
                        vy462 = unpack("<f", f.read(4))[0]
                        vz462 = unpack("<f", f.read(4))[0]
                        type462 = unpack("B", f.read(1))[0]
                        value1a462 = unpack("B", f.read(1))[0]
                        normalZ_462 = unpack("<h", f.read(2))[0]
                        vx463 = unpack("<f", f.read(4))[0]
                        vy463 = unpack("<f", f.read(4))[0]
                        vz463 = unpack("<f", f.read(4))[0]
                        type463 = unpack("B", f.read(1))[0]
                        value1a463 = unpack("B", f.read(1))[0]
                        normalZ_463 = unpack("<h", f.read(2))[0]
                        vx464 = unpack("<f", f.read(4))[0]
                        vy464 = unpack("<f", f.read(4))[0]
                        vz464 = unpack("<f", f.read(4))[0]
                        type464 = unpack("B", f.read(1))[0]
                        value1a464 = unpack("B", f.read(1))[0]
                        normalZ_464 = unpack("<h", f.read(2))[0]
                        vx465 = unpack("<f", f.read(4))[0]
                        vy465 = unpack("<f", f.read(4))[0]
                        vz465 = unpack("<f", f.read(4))[0]
                        type465 = unpack("B", f.read(1))[0]
                        value1a465 = unpack("B", f.read(1))[0]
                        normalZ_465 = unpack("<h", f.read(2))[0]
                        vx466 = unpack("<f", f.read(4))[0]
                        vy466 = unpack("<f", f.read(4))[0]
                        vz466 = unpack("<f", f.read(4))[0]
                        type466 = unpack("B", f.read(1))[0]
                        value1a466 = unpack("B", f.read(1))[0]
                        normalZ_466 = unpack("<h", f.read(2))[0]
                        vx467 = unpack("<f", f.read(4))[0]
                        vy467 = unpack("<f", f.read(4))[0]
                        vz467 = unpack("<f", f.read(4))[0]
                        type467 = unpack("B", f.read(1))[0]
                        value1a467 = unpack("B", f.read(1))[0]
                        normalZ_467 = unpack("<h", f.read(2))[0]
                        vx468 = unpack("<f", f.read(4))[0]
                        vy468 = unpack("<f", f.read(4))[0]
                        vz468 = unpack("<f", f.read(4))[0]
                        type468 = unpack("B", f.read(1))[0]
                        value1a468 = unpack("B", f.read(1))[0]
                        normalZ_468 = unpack("<h", f.read(2))[0]
                        vx469 = unpack("<f", f.read(4))[0]
                        vy469 = unpack("<f", f.read(4))[0]
                        vz469 = unpack("<f", f.read(4))[0]
                        type469 = unpack("B", f.read(1))[0]
                        value1a469 = unpack("B", f.read(1))[0]
                        normalZ_469 = unpack("<h", f.read(2))[0]
                        vx470 = unpack("<f", f.read(4))[0]
                        vy470 = unpack("<f", f.read(4))[0]
                        vz470 = unpack("<f", f.read(4))[0]
                        type470 = unpack("B", f.read(1))[0]
                        value1a470 = unpack("B", f.read(1))[0]
                        normalZ_470 = unpack("<h", f.read(2))[0]
                        vx471 = unpack("<f", f.read(4))[0]
                        vy471 = unpack("<f", f.read(4))[0]
                        vz471 = unpack("<f", f.read(4))[0]
                        type471 = unpack("B", f.read(1))[0]
                        value1a471 = unpack("B", f.read(1))[0]
                        normalZ_471 = unpack("<h", f.read(2))[0]
                        vx472 = unpack("<f", f.read(4))[0]
                        vy472 = unpack("<f", f.read(4))[0]
                        vz472 = unpack("<f", f.read(4))[0]
                        type472 = unpack("B", f.read(1))[0]
                        value1a472 = unpack("B", f.read(1))[0]
                        normalZ_472 = unpack("<h", f.read(2))[0]
                        vx473 = unpack("<f", f.read(4))[0]
                        vy473 = unpack("<f", f.read(4))[0]
                        vz473 = unpack("<f", f.read(4))[0]
                        type473 = unpack("B", f.read(1))[0]
                        value1a473 = unpack("B", f.read(1))[0]
                        normalZ_473 = unpack("<h", f.read(2))[0]
                        vx474 = unpack("<f", f.read(4))[0]
                        vy474 = unpack("<f", f.read(4))[0]
                        vz474 = unpack("<f", f.read(4))[0]
                        type474 = unpack("B", f.read(1))[0]
                        value1a474 = unpack("B", f.read(1))[0]
                        normalZ_474 = unpack("<h", f.read(2))[0]
                        vx475 = unpack("<f", f.read(4))[0]
                        vy475 = unpack("<f", f.read(4))[0]
                        vz475 = unpack("<f", f.read(4))[0]
                        type475 = unpack("B", f.read(1))[0]
                        value1a475 = unpack("B", f.read(1))[0]
                        normalZ_475 = unpack("<h", f.read(2))[0]
                        vx476 = unpack("<f", f.read(4))[0]
                        vy476 = unpack("<f", f.read(4))[0]
                        vz476 = unpack("<f", f.read(4))[0]
                        type476 = unpack("B", f.read(1))[0]
                        value1a476 = unpack("B", f.read(1))[0]
                        normalZ_476 = unpack("<h", f.read(2))[0]
                        vx477 = unpack("<f", f.read(4))[0]
                        vy477 = unpack("<f", f.read(4))[0]
                        vz477 = unpack("<f", f.read(4))[0]
                        type477 = unpack("B", f.read(1))[0]
                        value1a477 = unpack("B", f.read(1))[0]
                        normalZ_477 = unpack("<h", f.read(2))[0]
                        vx478 = unpack("<f", f.read(4))[0]
                        vy478 = unpack("<f", f.read(4))[0]
                        vz478 = unpack("<f", f.read(4))[0]
                        type478 = unpack("B", f.read(1))[0]
                        value1a478 = unpack("B", f.read(1))[0]
                        normalZ_478 = unpack("<h", f.read(2))[0]
                        vx479 = unpack("<f", f.read(4))[0]
                        vy479 = unpack("<f", f.read(4))[0]
                        vz479 = unpack("<f", f.read(4))[0]
                        type479 = unpack("B", f.read(1))[0]
                        value1a479 = unpack("B", f.read(1))[0]
                        normalZ_479 = unpack("<h", f.read(2))[0]
                        vx480 = unpack("<f", f.read(4))[0]
                        vy480 = unpack("<f", f.read(4))[0]
                        vz480 = unpack("<f", f.read(4))[0]
                        type480 = unpack("B", f.read(1))[0]
                        value1a480 = unpack("B", f.read(1))[0]
                        normalZ_480 = unpack("<h", f.read(2))[0]
                        vx481 = unpack("<f", f.read(4))[0]
                        vy481 = unpack("<f", f.read(4))[0]
                        vz481 = unpack("<f", f.read(4))[0]
                        type481 = unpack("B", f.read(1))[0]
                        value1a481 = unpack("B", f.read(1))[0]
                        normalZ_481 = unpack("<h", f.read(2))[0]
                        vx482 = unpack("<f", f.read(4))[0]
                        vy482 = unpack("<f", f.read(4))[0]
                        vz482 = unpack("<f", f.read(4))[0]
                        type482 = unpack("B", f.read(1))[0]
                        value1a482 = unpack("B", f.read(1))[0]
                        normalZ_482 = unpack("<h", f.read(2))[0]
                        vx483 = unpack("<f", f.read(4))[0]
                        vy483 = unpack("<f", f.read(4))[0]
                        vz483 = unpack("<f", f.read(4))[0]
                        type483 = unpack("B", f.read(1))[0]
                        value1a483 = unpack("B", f.read(1))[0]
                        normalZ_483 = unpack("<h", f.read(2))[0]
                        vx484 = unpack("<f", f.read(4))[0]
                        vy484 = unpack("<f", f.read(4))[0]
                        vz484 = unpack("<f", f.read(4))[0]
                        type484 = unpack("B", f.read(1))[0]
                        value1a484 = unpack("B", f.read(1))[0]
                        normalZ_484 = unpack("<h", f.read(2))[0]
                        vx485 = unpack("<f", f.read(4))[0]
                        vy485 = unpack("<f", f.read(4))[0]
                        vz485 = unpack("<f", f.read(4))[0]
                        type485 = unpack("B", f.read(1))[0]
                        value1a485 = unpack("B", f.read(1))[0]
                        normalZ_485 = unpack("<h", f.read(2))[0]
                        vx486 = unpack("<f", f.read(4))[0]
                        vy486 = unpack("<f", f.read(4))[0]
                        vz486 = unpack("<f", f.read(4))[0]
                        type486 = unpack("B", f.read(1))[0]
                        value1a486 = unpack("B", f.read(1))[0]
                        normalZ_486 = unpack("<h", f.read(2))[0]
                        vx487 = unpack("<f", f.read(4))[0]
                        vy487 = unpack("<f", f.read(4))[0]
                        vz487 = unpack("<f", f.read(4))[0]
                        type487 = unpack("B", f.read(1))[0]
                        value1a487 = unpack("B", f.read(1))[0]
                        normalZ_487 = unpack("<h", f.read(2))[0]
                        vx488 = unpack("<f", f.read(4))[0]
                        vy488 = unpack("<f", f.read(4))[0]
                        vz488 = unpack("<f", f.read(4))[0]
                        type488 = unpack("B", f.read(1))[0]
                        value1a488 = unpack("B", f.read(1))[0]
                        normalZ_488 = unpack("<h", f.read(2))[0]
                        vx489 = unpack("<f", f.read(4))[0]
                        vy489 = unpack("<f", f.read(4))[0]
                        vz489 = unpack("<f", f.read(4))[0]
                        type489 = unpack("B", f.read(1))[0]
                        value1a489 = unpack("B", f.read(1))[0]
                        normalZ_489 = unpack("<h", f.read(2))[0]
                        vx490 = unpack("<f", f.read(4))[0]
                        vy490 = unpack("<f", f.read(4))[0]
                        vz490 = unpack("<f", f.read(4))[0]
                        type490 = unpack("B", f.read(1))[0]
                        value1a490 = unpack("B", f.read(1))[0]
                        normalZ_490 = unpack("<h", f.read(2))[0]
                        vx491 = unpack("<f", f.read(4))[0]
                        vy491 = unpack("<f", f.read(4))[0]
                        vz491 = unpack("<f", f.read(4))[0]
                        type491 = unpack("B", f.read(1))[0]
                        value1a491 = unpack("B", f.read(1))[0]
                        normalZ_491 = unpack("<h", f.read(2))[0]
                        vx492 = unpack("<f", f.read(4))[0]
                        vy492 = unpack("<f", f.read(4))[0]
                        vz492 = unpack("<f", f.read(4))[0]
                        type492 = unpack("B", f.read(1))[0]
                        value1a492 = unpack("B", f.read(1))[0]
                        normalZ_492 = unpack("<h", f.read(2))[0]
                        vertices.append([vx462,vz462,vy462])
                        vertices.append([vx463,vz463,vy463])
                        vertices.append([vx464,vz464,vy464])
                        vertices.append([vx465,vz465,vy465])
                        vertices.append([vx466,vz466,vy466])
                        vertices.append([vx467,vz467,vy467])
                        vertices.append([vx468,vz468,vy468])
                        vertices.append([vx469,vz469,vy469])
                        vertices.append([vx470,vz470,vy470])
                        vertices.append([vx471,vz471,vy471])
                        vertices.append([vx472,vz472,vy472])
                        vertices.append([vx473,vz473,vy473])
                        vertices.append([vx474,vz474,vy474])
                        vertices.append([vx475,vz475,vy475])
                        vertices.append([vx476,vz476,vy476])
                        vertices.append([vx477,vz477,vy477])
                        vertices.append([vx478,vz478,vy478])
                        vertices.append([vx479,vz479,vy479])
                        vertices.append([vx480,vz480,vy480])
                        vertices.append([vx481,vz481,vy481])
                        vertices.append([vx482,vz482,vy482])
                        vertices.append([vx483,vz483,vy483])
                        vertices.append([vx484,vz484,vy484])
                        vertices.append([vx485,vz485,vy485])
                        vertices.append([vx486,vz486,vy486])
                        vertices.append([vx487,vz487,vy487])
                        vertices.append([vx488,vz488,vy488])
                        vertices.append([vx489,vz489,vy489])
                        vertices.append([vx490,vz490,vy490])
                        vertices.append([vx491,vz491,vy491])
                        vertices.append([vx492,vz492,vy492])


                elif vertexCount == 32:
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
                        vx493 = unpack("<f", f.read(4))[0]
                        vy493 = unpack("<f", f.read(4))[0]
                        vz493 = unpack("<f", f.read(4))[0]
                        type493 = unpack("B", f.read(1))[0]
                        value1a493 = unpack("B", f.read(1))[0]
                        normalZ_493 = unpack("<h", f.read(2))[0]
                        vx494 = unpack("<f", f.read(4))[0]
                        vy494 = unpack("<f", f.read(4))[0]
                        vz494 = unpack("<f", f.read(4))[0]
                        type494 = unpack("B", f.read(1))[0]
                        value1a494 = unpack("B", f.read(1))[0]
                        normalZ_494 = unpack("<h", f.read(2))[0]
                        vx495 = unpack("<f", f.read(4))[0]
                        vy495 = unpack("<f", f.read(4))[0]
                        vz495 = unpack("<f", f.read(4))[0]
                        type495 = unpack("B", f.read(1))[0]
                        value1a495 = unpack("B", f.read(1))[0]
                        normalZ_495 = unpack("<h", f.read(2))[0]
                        vx496 = unpack("<f", f.read(4))[0]
                        vy496 = unpack("<f", f.read(4))[0]
                        vz496 = unpack("<f", f.read(4))[0]
                        type496 = unpack("B", f.read(1))[0]
                        value1a496 = unpack("B", f.read(1))[0]
                        normalZ_496 = unpack("<h", f.read(2))[0]
                        vx497 = unpack("<f", f.read(4))[0]
                        vy497 = unpack("<f", f.read(4))[0]
                        vz497 = unpack("<f", f.read(4))[0]
                        type497 = unpack("B", f.read(1))[0]
                        value1a497 = unpack("B", f.read(1))[0]
                        normalZ_497 = unpack("<h", f.read(2))[0]
                        vx498 = unpack("<f", f.read(4))[0]
                        vy498 = unpack("<f", f.read(4))[0]
                        vz498 = unpack("<f", f.read(4))[0]
                        type498 = unpack("B", f.read(1))[0]
                        value1a498 = unpack("B", f.read(1))[0]
                        normalZ_498 = unpack("<h", f.read(2))[0]
                        vx499 = unpack("<f", f.read(4))[0]
                        vy499 = unpack("<f", f.read(4))[0]
                        vz499 = unpack("<f", f.read(4))[0]
                        type499 = unpack("B", f.read(1))[0]
                        value1a499 = unpack("B", f.read(1))[0]
                        normalZ_499 = unpack("<h", f.read(2))[0]
                        vx500 = unpack("<f", f.read(4))[0]
                        vy500 = unpack("<f", f.read(4))[0]
                        vz500 = unpack("<f", f.read(4))[0]
                        type500 = unpack("B", f.read(1))[0]
                        value1a500 = unpack("B", f.read(1))[0]
                        normalZ_500 = unpack("<h", f.read(2))[0]
                        vx501 = unpack("<f", f.read(4))[0]
                        vy501 = unpack("<f", f.read(4))[0]
                        vz501 = unpack("<f", f.read(4))[0]
                        type501 = unpack("B", f.read(1))[0]
                        value1a501 = unpack("B", f.read(1))[0]
                        normalZ_501 = unpack("<h", f.read(2))[0]
                        vx502 = unpack("<f", f.read(4))[0]
                        vy502 = unpack("<f", f.read(4))[0]
                        vz502 = unpack("<f", f.read(4))[0]
                        type502 = unpack("B", f.read(1))[0]
                        value1a502 = unpack("B", f.read(1))[0]
                        normalZ_502 = unpack("<h", f.read(2))[0]
                        vx503 = unpack("<f", f.read(4))[0]
                        vy503 = unpack("<f", f.read(4))[0]
                        vz503 = unpack("<f", f.read(4))[0]
                        type503 = unpack("B", f.read(1))[0]
                        value1a503 = unpack("B", f.read(1))[0]
                        normalZ_503 = unpack("<h", f.read(2))[0]
                        vx504 = unpack("<f", f.read(4))[0]
                        vy504 = unpack("<f", f.read(4))[0]
                        vz504 = unpack("<f", f.read(4))[0]
                        type504 = unpack("B", f.read(1))[0]
                        value1a504 = unpack("B", f.read(1))[0]
                        normalZ_504 = unpack("<h", f.read(2))[0]
                        vx505 = unpack("<f", f.read(4))[0]
                        vy505 = unpack("<f", f.read(4))[0]
                        vz505 = unpack("<f", f.read(4))[0]
                        type505 = unpack("B", f.read(1))[0]
                        value1a505 = unpack("B", f.read(1))[0]
                        normalZ_505 = unpack("<h", f.read(2))[0]
                        vx506 = unpack("<f", f.read(4))[0]
                        vy506 = unpack("<f", f.read(4))[0]
                        vz506 = unpack("<f", f.read(4))[0]
                        type506 = unpack("B", f.read(1))[0]
                        value1a506 = unpack("B", f.read(1))[0]
                        normalZ_506 = unpack("<h", f.read(2))[0]
                        vx507 = unpack("<f", f.read(4))[0]
                        vy507 = unpack("<f", f.read(4))[0]
                        vz507 = unpack("<f", f.read(4))[0]
                        type507 = unpack("B", f.read(1))[0]
                        value1a507 = unpack("B", f.read(1))[0]
                        normalZ_507 = unpack("<h", f.read(2))[0]
                        vx508 = unpack("<f", f.read(4))[0]
                        vy508 = unpack("<f", f.read(4))[0]
                        vz508 = unpack("<f", f.read(4))[0]
                        type508 = unpack("B", f.read(1))[0]
                        value1a508 = unpack("B", f.read(1))[0]
                        normalZ_508 = unpack("<h", f.read(2))[0]
                        vx509 = unpack("<f", f.read(4))[0]
                        vy509 = unpack("<f", f.read(4))[0]
                        vz509 = unpack("<f", f.read(4))[0]
                        type509 = unpack("B", f.read(1))[0]
                        value1a509 = unpack("B", f.read(1))[0]
                        normalZ_509 = unpack("<h", f.read(2))[0]
                        vx510 = unpack("<f", f.read(4))[0]
                        vy510 = unpack("<f", f.read(4))[0]
                        vz510 = unpack("<f", f.read(4))[0]
                        type510 = unpack("B", f.read(1))[0]
                        value1a510 = unpack("B", f.read(1))[0]
                        normalZ_510 = unpack("<h", f.read(2))[0]
                        vx511 = unpack("<f", f.read(4))[0]
                        vy511 = unpack("<f", f.read(4))[0]
                        vz511 = unpack("<f", f.read(4))[0]
                        type511 = unpack("B", f.read(1))[0]
                        value1a511 = unpack("B", f.read(1))[0]
                        normalZ_511 = unpack("<h", f.read(2))[0]
                        vx512 = unpack("<f", f.read(4))[0]
                        vy512 = unpack("<f", f.read(4))[0]
                        vz512 = unpack("<f", f.read(4))[0]
                        type512 = unpack("B", f.read(1))[0]
                        value1a512 = unpack("B", f.read(1))[0]
                        normalZ_512 = unpack("<h", f.read(2))[0]
                        vx513 = unpack("<f", f.read(4))[0]
                        vy513 = unpack("<f", f.read(4))[0]
                        vz513 = unpack("<f", f.read(4))[0]
                        type513 = unpack("B", f.read(1))[0]
                        value1a513 = unpack("B", f.read(1))[0]
                        normalZ_513 = unpack("<h", f.read(2))[0]
                        vx514 = unpack("<f", f.read(4))[0]
                        vy514 = unpack("<f", f.read(4))[0]
                        vz514 = unpack("<f", f.read(4))[0]
                        type514 = unpack("B", f.read(1))[0]
                        value1a514 = unpack("B", f.read(1))[0]
                        normalZ_514 = unpack("<h", f.read(2))[0]
                        vx515 = unpack("<f", f.read(4))[0]
                        vy515 = unpack("<f", f.read(4))[0]
                        vz515 = unpack("<f", f.read(4))[0]
                        type515 = unpack("B", f.read(1))[0]
                        value1a515 = unpack("B", f.read(1))[0]
                        normalZ_515 = unpack("<h", f.read(2))[0]
                        vx516 = unpack("<f", f.read(4))[0]
                        vy516 = unpack("<f", f.read(4))[0]
                        vz516 = unpack("<f", f.read(4))[0]
                        type516 = unpack("B", f.read(1))[0]
                        value1a516 = unpack("B", f.read(1))[0]
                        normalZ_516 = unpack("<h", f.read(2))[0]
                        vx517 = unpack("<f", f.read(4))[0]
                        vy517 = unpack("<f", f.read(4))[0]
                        vz517 = unpack("<f", f.read(4))[0]
                        type517 = unpack("B", f.read(1))[0]
                        value1a517 = unpack("B", f.read(1))[0]
                        normalZ_517 = unpack("<h", f.read(2))[0]
                        vx518 = unpack("<f", f.read(4))[0]
                        vy518 = unpack("<f", f.read(4))[0]
                        vz518 = unpack("<f", f.read(4))[0]
                        type518 = unpack("B", f.read(1))[0]
                        value1a518 = unpack("B", f.read(1))[0]
                        normalZ_518 = unpack("<h", f.read(2))[0]
                        vx519 = unpack("<f", f.read(4))[0]
                        vy519 = unpack("<f", f.read(4))[0]
                        vz519 = unpack("<f", f.read(4))[0]
                        type519 = unpack("B", f.read(1))[0]
                        value1a519 = unpack("B", f.read(1))[0]
                        normalZ_519 = unpack("<h", f.read(2))[0]
                        vx520 = unpack("<f", f.read(4))[0]
                        vy520 = unpack("<f", f.read(4))[0]
                        vz520 = unpack("<f", f.read(4))[0]
                        type520 = unpack("B", f.read(1))[0]
                        value1a520 = unpack("B", f.read(1))[0]
                        normalZ_520 = unpack("<h", f.read(2))[0]
                        vx521 = unpack("<f", f.read(4))[0]
                        vy521 = unpack("<f", f.read(4))[0]
                        vz521 = unpack("<f", f.read(4))[0]
                        type521 = unpack("B", f.read(1))[0]
                        value1a521 = unpack("B", f.read(1))[0]
                        normalZ_521 = unpack("<h", f.read(2))[0]
                        vx522 = unpack("<f", f.read(4))[0]
                        vy522 = unpack("<f", f.read(4))[0]
                        vz522 = unpack("<f", f.read(4))[0]
                        type522 = unpack("B", f.read(1))[0]
                        value1a522 = unpack("B", f.read(1))[0]
                        normalZ_522 = unpack("<h", f.read(2))[0]
                        vx523 = unpack("<f", f.read(4))[0]
                        vy523 = unpack("<f", f.read(4))[0]
                        vz523 = unpack("<f", f.read(4))[0]
                        type523 = unpack("B", f.read(1))[0]
                        value1a523 = unpack("B", f.read(1))[0]
                        normalZ_523 = unpack("<h", f.read(2))[0]
                        vx524 = unpack("<f", f.read(4))[0]
                        vy524 = unpack("<f", f.read(4))[0]
                        vz524 = unpack("<f", f.read(4))[0]
                        type524 = unpack("B", f.read(1))[0]
                        value1a524 = unpack("B", f.read(1))[0]
                        normalZ_524 = unpack("<h", f.read(2))[0]
                        vertices.append([vx493,vz493,vy493])
                        vertices.append([vx494,vz494,vy494])
                        vertices.append([vx495,vz495,vy495])
                        vertices.append([vx496,vz496,vy496])
                        vertices.append([vx497,vz497,vy497])
                        vertices.append([vx498,vz498,vy498])
                        vertices.append([vx499,vz499,vy499])
                        vertices.append([vx500,vz500,vy500])
                        vertices.append([vx501,vz501,vy501])
                        vertices.append([vx502,vz502,vy502])
                        vertices.append([vx503,vz503,vy503])
                        vertices.append([vx504,vz504,vy504])
                        vertices.append([vx505,vz505,vy505])
                        vertices.append([vx506,vz506,vy506])
                        vertices.append([vx507,vz507,vy507])
                        vertices.append([vx508,vz508,vy508])
                        vertices.append([vx509,vz509,vy509])
                        vertices.append([vx510,vz510,vy510])
                        vertices.append([vx511,vz511,vy511])
                        vertices.append([vx512,vz512,vy512])
                        vertices.append([vx513,vz513,vy513])
                        vertices.append([vx514,vz514,vy514])
                        vertices.append([vx515,vz515,vy515])
                        vertices.append([vx516,vz516,vy516])
                        vertices.append([vx517,vz517,vy517])
                        vertices.append([vx518,vz518,vy518])
                        vertices.append([vx519,vz519,vy519])
                        vertices.append([vx520,vz520,vy520])
                        vertices.append([vx521,vz521,vy521])
                        vertices.append([vx522,vz522,vy522])
                        vertices.append([vx523,vz523,vy523])
                        vertices.append([vx524,vz524,vy524])

                elif vertexCount == 33:
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
                        vx525 = unpack("<f", f.read(4))[0]
                        vy525 = unpack("<f", f.read(4))[0]
                        vz525 = unpack("<f", f.read(4))[0]
                        type525 = unpack("B", f.read(1))[0]
                        value1a525 = unpack("B", f.read(1))[0]
                        normalZ_525 = unpack("<h", f.read(2))[0]
                        vx526 = unpack("<f", f.read(4))[0]
                        vy526 = unpack("<f", f.read(4))[0]
                        vz526 = unpack("<f", f.read(4))[0]
                        type526 = unpack("B", f.read(1))[0]
                        value1a526 = unpack("B", f.read(1))[0]
                        normalZ_526 = unpack("<h", f.read(2))[0]
                        vx527 = unpack("<f", f.read(4))[0]
                        vy527 = unpack("<f", f.read(4))[0]
                        vz527 = unpack("<f", f.read(4))[0]
                        type527 = unpack("B", f.read(1))[0]
                        value1a527 = unpack("B", f.read(1))[0]
                        normalZ_527 = unpack("<h", f.read(2))[0]
                        vx528 = unpack("<f", f.read(4))[0]
                        vy528 = unpack("<f", f.read(4))[0]
                        vz528 = unpack("<f", f.read(4))[0]
                        type528 = unpack("B", f.read(1))[0]
                        value1a528 = unpack("B", f.read(1))[0]
                        normalZ_528 = unpack("<h", f.read(2))[0]
                        vx529 = unpack("<f", f.read(4))[0]
                        vy529 = unpack("<f", f.read(4))[0]
                        vz529 = unpack("<f", f.read(4))[0]
                        type529 = unpack("B", f.read(1))[0]
                        value1a529 = unpack("B", f.read(1))[0]
                        normalZ_529 = unpack("<h", f.read(2))[0]
                        vx530 = unpack("<f", f.read(4))[0]
                        vy530 = unpack("<f", f.read(4))[0]
                        vz530 = unpack("<f", f.read(4))[0]
                        type530 = unpack("B", f.read(1))[0]
                        value1a530 = unpack("B", f.read(1))[0]
                        normalZ_530 = unpack("<h", f.read(2))[0]
                        vx531 = unpack("<f", f.read(4))[0]
                        vy531 = unpack("<f", f.read(4))[0]
                        vz531 = unpack("<f", f.read(4))[0]
                        type531 = unpack("B", f.read(1))[0]
                        value1a531 = unpack("B", f.read(1))[0]
                        normalZ_531 = unpack("<h", f.read(2))[0]
                        vx532 = unpack("<f", f.read(4))[0]
                        vy532 = unpack("<f", f.read(4))[0]
                        vz532 = unpack("<f", f.read(4))[0]
                        type532 = unpack("B", f.read(1))[0]
                        value1a532 = unpack("B", f.read(1))[0]
                        normalZ_532 = unpack("<h", f.read(2))[0]
                        vx533 = unpack("<f", f.read(4))[0]
                        vy533 = unpack("<f", f.read(4))[0]
                        vz533 = unpack("<f", f.read(4))[0]
                        type533 = unpack("B", f.read(1))[0]
                        value1a533 = unpack("B", f.read(1))[0]
                        normalZ_533 = unpack("<h", f.read(2))[0]
                        vx534 = unpack("<f", f.read(4))[0]
                        vy534 = unpack("<f", f.read(4))[0]
                        vz534 = unpack("<f", f.read(4))[0]
                        type534 = unpack("B", f.read(1))[0]
                        value1a534 = unpack("B", f.read(1))[0]
                        normalZ_534 = unpack("<h", f.read(2))[0]
                        vx535 = unpack("<f", f.read(4))[0]
                        vy535 = unpack("<f", f.read(4))[0]
                        vz535 = unpack("<f", f.read(4))[0]
                        type535 = unpack("B", f.read(1))[0]
                        value1a535 = unpack("B", f.read(1))[0]
                        normalZ_535 = unpack("<h", f.read(2))[0]
                        vx536 = unpack("<f", f.read(4))[0]
                        vy536 = unpack("<f", f.read(4))[0]
                        vz536 = unpack("<f", f.read(4))[0]
                        type536 = unpack("B", f.read(1))[0]
                        value1a536 = unpack("B", f.read(1))[0]
                        normalZ_536 = unpack("<h", f.read(2))[0]
                        vx537 = unpack("<f", f.read(4))[0]
                        vy537 = unpack("<f", f.read(4))[0]
                        vz537 = unpack("<f", f.read(4))[0]
                        type537 = unpack("B", f.read(1))[0]
                        value1a537 = unpack("B", f.read(1))[0]
                        normalZ_537 = unpack("<h", f.read(2))[0]
                        vx538 = unpack("<f", f.read(4))[0]
                        vy538 = unpack("<f", f.read(4))[0]
                        vz538 = unpack("<f", f.read(4))[0]
                        type538 = unpack("B", f.read(1))[0]
                        value1a538 = unpack("B", f.read(1))[0]
                        normalZ_538 = unpack("<h", f.read(2))[0]
                        vx539 = unpack("<f", f.read(4))[0]
                        vy539 = unpack("<f", f.read(4))[0]
                        vz539 = unpack("<f", f.read(4))[0]
                        type539 = unpack("B", f.read(1))[0]
                        value1a539 = unpack("B", f.read(1))[0]
                        normalZ_539 = unpack("<h", f.read(2))[0]
                        vx540 = unpack("<f", f.read(4))[0]
                        vy540 = unpack("<f", f.read(4))[0]
                        vz540 = unpack("<f", f.read(4))[0]
                        type540 = unpack("B", f.read(1))[0]
                        value1a540 = unpack("B", f.read(1))[0]
                        normalZ_540 = unpack("<h", f.read(2))[0]
                        vx541 = unpack("<f", f.read(4))[0]
                        vy541 = unpack("<f", f.read(4))[0]
                        vz541 = unpack("<f", f.read(4))[0]
                        type541 = unpack("B", f.read(1))[0]
                        value1a541 = unpack("B", f.read(1))[0]
                        normalZ_541 = unpack("<h", f.read(2))[0]
                        vx542 = unpack("<f", f.read(4))[0]
                        vy542 = unpack("<f", f.read(4))[0]
                        vz542 = unpack("<f", f.read(4))[0]
                        type542 = unpack("B", f.read(1))[0]
                        value1a542 = unpack("B", f.read(1))[0]
                        normalZ_542 = unpack("<h", f.read(2))[0]
                        vx543 = unpack("<f", f.read(4))[0]
                        vy543 = unpack("<f", f.read(4))[0]
                        vz543 = unpack("<f", f.read(4))[0]
                        type543 = unpack("B", f.read(1))[0]
                        value1a543 = unpack("B", f.read(1))[0]
                        normalZ_543 = unpack("<h", f.read(2))[0]
                        vx544 = unpack("<f", f.read(4))[0]
                        vy544 = unpack("<f", f.read(4))[0]
                        vz544 = unpack("<f", f.read(4))[0]
                        type544 = unpack("B", f.read(1))[0]
                        value1a544 = unpack("B", f.read(1))[0]
                        normalZ_544 = unpack("<h", f.read(2))[0]
                        vx545 = unpack("<f", f.read(4))[0]
                        vy545 = unpack("<f", f.read(4))[0]
                        vz545 = unpack("<f", f.read(4))[0]
                        type545 = unpack("B", f.read(1))[0]
                        value1a545 = unpack("B", f.read(1))[0]
                        normalZ_545 = unpack("<h", f.read(2))[0]
                        vx546 = unpack("<f", f.read(4))[0]
                        vy546 = unpack("<f", f.read(4))[0]
                        vz546 = unpack("<f", f.read(4))[0]
                        type546 = unpack("B", f.read(1))[0]
                        value1a546 = unpack("B", f.read(1))[0]
                        normalZ_546 = unpack("<h", f.read(2))[0]
                        vx547 = unpack("<f", f.read(4))[0]
                        vy547 = unpack("<f", f.read(4))[0]
                        vz547 = unpack("<f", f.read(4))[0]
                        type547 = unpack("B", f.read(1))[0]
                        value1a547 = unpack("B", f.read(1))[0]
                        normalZ_547 = unpack("<h", f.read(2))[0]
                        vx548 = unpack("<f", f.read(4))[0]
                        vy548 = unpack("<f", f.read(4))[0]
                        vz548 = unpack("<f", f.read(4))[0]
                        type548 = unpack("B", f.read(1))[0]
                        value1a548 = unpack("B", f.read(1))[0]
                        normalZ_548 = unpack("<h", f.read(2))[0]
                        vx549 = unpack("<f", f.read(4))[0]
                        vy549 = unpack("<f", f.read(4))[0]
                        vz549 = unpack("<f", f.read(4))[0]
                        type549 = unpack("B", f.read(1))[0]
                        value1a549 = unpack("B", f.read(1))[0]
                        normalZ_549 = unpack("<h", f.read(2))[0]
                        vx550 = unpack("<f", f.read(4))[0]
                        vy550 = unpack("<f", f.read(4))[0]
                        vz550 = unpack("<f", f.read(4))[0]
                        type550 = unpack("B", f.read(1))[0]
                        value1a550 = unpack("B", f.read(1))[0]
                        normalZ_550 = unpack("<h", f.read(2))[0]
                        vx551 = unpack("<f", f.read(4))[0]
                        vy551 = unpack("<f", f.read(4))[0]
                        vz551 = unpack("<f", f.read(4))[0]
                        type551 = unpack("B", f.read(1))[0]
                        value1a551 = unpack("B", f.read(1))[0]
                        normalZ_551 = unpack("<h", f.read(2))[0]
                        vx552 = unpack("<f", f.read(4))[0]
                        vy552 = unpack("<f", f.read(4))[0]
                        vz552 = unpack("<f", f.read(4))[0]
                        type552 = unpack("B", f.read(1))[0]
                        value1a552 = unpack("B", f.read(1))[0]
                        normalZ_552 = unpack("<h", f.read(2))[0]
                        vx553 = unpack("<f", f.read(4))[0]
                        vy553 = unpack("<f", f.read(4))[0]
                        vz553 = unpack("<f", f.read(4))[0]
                        type553 = unpack("B", f.read(1))[0]
                        value1a553 = unpack("B", f.read(1))[0]
                        normalZ_553 = unpack("<h", f.read(2))[0]
                        vx554 = unpack("<f", f.read(4))[0]
                        vy554 = unpack("<f", f.read(4))[0]
                        vz554 = unpack("<f", f.read(4))[0]
                        type554 = unpack("B", f.read(1))[0]
                        value1a554 = unpack("B", f.read(1))[0]
                        normalZ_554 = unpack("<h", f.read(2))[0]
                        vx555 = unpack("<f", f.read(4))[0]
                        vy555 = unpack("<f", f.read(4))[0]
                        vz555 = unpack("<f", f.read(4))[0]
                        type555 = unpack("B", f.read(1))[0]
                        value1a555 = unpack("B", f.read(1))[0]
                        normalZ_555 = unpack("<h", f.read(2))[0]
                        vx556 = unpack("<f", f.read(4))[0]
                        vy556 = unpack("<f", f.read(4))[0]
                        vz556 = unpack("<f", f.read(4))[0]
                        type556 = unpack("B", f.read(1))[0]
                        value1a556 = unpack("B", f.read(1))[0]
                        normalZ_556 = unpack("<h", f.read(2))[0]
                        vx557 = unpack("<f", f.read(4))[0]
                        vy557 = unpack("<f", f.read(4))[0]
                        vz557 = unpack("<f", f.read(4))[0]
                        type557 = unpack("B", f.read(1))[0]
                        value1a557 = unpack("B", f.read(1))[0]
                        normalZ_557 = unpack("<h", f.read(2))[0]
                        vertices.append([vx525,vz525,vy525])
                        vertices.append([vx526,vz526,vy526])
                        vertices.append([vx527,vz527,vy527])
                        vertices.append([vx528,vz528,vy528])
                        vertices.append([vx529,vz529,vy529])
                        vertices.append([vx530,vz530,vy530])
                        vertices.append([vx531,vz531,vy531])
                        vertices.append([vx532,vz532,vy532])
                        vertices.append([vx533,vz533,vy533])
                        vertices.append([vx534,vz534,vy534])
                        vertices.append([vx535,vz535,vy535])
                        vertices.append([vx536,vz536,vy536])
                        vertices.append([vx537,vz537,vy537])
                        vertices.append([vx538,vz538,vy538])
                        vertices.append([vx539,vz539,vy539])
                        vertices.append([vx540,vz540,vy540])
                        vertices.append([vx541,vz541,vy541])
                        vertices.append([vx542,vz542,vy542])
                        vertices.append([vx543,vz543,vy543])
                        vertices.append([vx544,vz544,vy544])
                        vertices.append([vx545,vz545,vy545])
                        vertices.append([vx546,vz546,vy546])
                        vertices.append([vx547,vz547,vy547])
                        vertices.append([vx548,vz548,vy548])
                        vertices.append([vx549,vz549,vy549])
                        vertices.append([vx550,vz550,vy550])
                        vertices.append([vx551,vz551,vy551])
                        vertices.append([vx552,vz552,vy552])
                        vertices.append([vx553,vz553,vy553])
                        vertices.append([vx554,vz554,vy554])
                        vertices.append([vx555,vz555,vy555])
                        vertices.append([vx556,vz556,vy556])
                        vertices.append([vx557,vz557,vy557])

                elif vertexCount == 34:
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
                        vx558 = unpack("<f", f.read(4))[0]
                        vy558 = unpack("<f", f.read(4))[0]
                        vz558 = unpack("<f", f.read(4))[0]
                        type558 = unpack("B", f.read(1))[0]
                        value1a558 = unpack("B", f.read(1))[0]
                        normalZ_558 = unpack("<h", f.read(2))[0]
                        vx559 = unpack("<f", f.read(4))[0]
                        vy559 = unpack("<f", f.read(4))[0]
                        vz559 = unpack("<f", f.read(4))[0]
                        type559 = unpack("B", f.read(1))[0]
                        value1a559 = unpack("B", f.read(1))[0]
                        normalZ_559 = unpack("<h", f.read(2))[0]
                        vx560 = unpack("<f", f.read(4))[0]
                        vy560 = unpack("<f", f.read(4))[0]
                        vz560 = unpack("<f", f.read(4))[0]
                        type560 = unpack("B", f.read(1))[0]
                        value1a560 = unpack("B", f.read(1))[0]
                        normalZ_560 = unpack("<h", f.read(2))[0]
                        vx561 = unpack("<f", f.read(4))[0]
                        vy561 = unpack("<f", f.read(4))[0]
                        vz561 = unpack("<f", f.read(4))[0]
                        type561 = unpack("B", f.read(1))[0]
                        value1a561 = unpack("B", f.read(1))[0]
                        normalZ_561 = unpack("<h", f.read(2))[0]
                        vx562 = unpack("<f", f.read(4))[0]
                        vy562 = unpack("<f", f.read(4))[0]
                        vz562 = unpack("<f", f.read(4))[0]
                        type562 = unpack("B", f.read(1))[0]
                        value1a562 = unpack("B", f.read(1))[0]
                        normalZ_562 = unpack("<h", f.read(2))[0]
                        vx563 = unpack("<f", f.read(4))[0]
                        vy563 = unpack("<f", f.read(4))[0]
                        vz563 = unpack("<f", f.read(4))[0]
                        type563 = unpack("B", f.read(1))[0]
                        value1a563 = unpack("B", f.read(1))[0]
                        normalZ_563 = unpack("<h", f.read(2))[0]
                        vx564 = unpack("<f", f.read(4))[0]
                        vy564 = unpack("<f", f.read(4))[0]
                        vz564 = unpack("<f", f.read(4))[0]
                        type564 = unpack("B", f.read(1))[0]
                        value1a564 = unpack("B", f.read(1))[0]
                        normalZ_564 = unpack("<h", f.read(2))[0]
                        vx565 = unpack("<f", f.read(4))[0]
                        vy565 = unpack("<f", f.read(4))[0]
                        vz565 = unpack("<f", f.read(4))[0]
                        type565 = unpack("B", f.read(1))[0]
                        value1a565 = unpack("B", f.read(1))[0]
                        normalZ_565 = unpack("<h", f.read(2))[0]
                        vx566 = unpack("<f", f.read(4))[0]
                        vy566 = unpack("<f", f.read(4))[0]
                        vz566 = unpack("<f", f.read(4))[0]
                        type566 = unpack("B", f.read(1))[0]
                        value1a566 = unpack("B", f.read(1))[0]
                        normalZ_566 = unpack("<h", f.read(2))[0]
                        vx567 = unpack("<f", f.read(4))[0]
                        vy567 = unpack("<f", f.read(4))[0]
                        vz567 = unpack("<f", f.read(4))[0]
                        type567 = unpack("B", f.read(1))[0]
                        value1a567 = unpack("B", f.read(1))[0]
                        normalZ_567 = unpack("<h", f.read(2))[0]
                        vx568 = unpack("<f", f.read(4))[0]
                        vy568 = unpack("<f", f.read(4))[0]
                        vz568 = unpack("<f", f.read(4))[0]
                        type568 = unpack("B", f.read(1))[0]
                        value1a568 = unpack("B", f.read(1))[0]
                        normalZ_568 = unpack("<h", f.read(2))[0]
                        vx569 = unpack("<f", f.read(4))[0]
                        vy569 = unpack("<f", f.read(4))[0]
                        vz569 = unpack("<f", f.read(4))[0]
                        type569 = unpack("B", f.read(1))[0]
                        value1a569 = unpack("B", f.read(1))[0]
                        normalZ_569 = unpack("<h", f.read(2))[0]
                        vx570 = unpack("<f", f.read(4))[0]
                        vy570 = unpack("<f", f.read(4))[0]
                        vz570 = unpack("<f", f.read(4))[0]
                        type570 = unpack("B", f.read(1))[0]
                        value1a570 = unpack("B", f.read(1))[0]
                        normalZ_570 = unpack("<h", f.read(2))[0]
                        vx571 = unpack("<f", f.read(4))[0]
                        vy571 = unpack("<f", f.read(4))[0]
                        vz571 = unpack("<f", f.read(4))[0]
                        type571 = unpack("B", f.read(1))[0]
                        value1a571 = unpack("B", f.read(1))[0]
                        normalZ_571 = unpack("<h", f.read(2))[0]
                        vx572 = unpack("<f", f.read(4))[0]
                        vy572 = unpack("<f", f.read(4))[0]
                        vz572 = unpack("<f", f.read(4))[0]
                        type572 = unpack("B", f.read(1))[0]
                        value1a572 = unpack("B", f.read(1))[0]
                        normalZ_572 = unpack("<h", f.read(2))[0]
                        vx573 = unpack("<f", f.read(4))[0]
                        vy573 = unpack("<f", f.read(4))[0]
                        vz573 = unpack("<f", f.read(4))[0]
                        type573 = unpack("B", f.read(1))[0]
                        value1a573 = unpack("B", f.read(1))[0]
                        normalZ_573 = unpack("<h", f.read(2))[0]
                        vx574 = unpack("<f", f.read(4))[0]
                        vy574 = unpack("<f", f.read(4))[0]
                        vz574 = unpack("<f", f.read(4))[0]
                        type574 = unpack("B", f.read(1))[0]
                        value1a574 = unpack("B", f.read(1))[0]
                        normalZ_574 = unpack("<h", f.read(2))[0]
                        vx575 = unpack("<f", f.read(4))[0]
                        vy575 = unpack("<f", f.read(4))[0]
                        vz575 = unpack("<f", f.read(4))[0]
                        type575 = unpack("B", f.read(1))[0]
                        value1a575 = unpack("B", f.read(1))[0]
                        normalZ_575 = unpack("<h", f.read(2))[0]
                        vx576 = unpack("<f", f.read(4))[0]
                        vy576 = unpack("<f", f.read(4))[0]
                        vz576 = unpack("<f", f.read(4))[0]
                        type576 = unpack("B", f.read(1))[0]
                        value1a576 = unpack("B", f.read(1))[0]
                        normalZ_576 = unpack("<h", f.read(2))[0]
                        vx577 = unpack("<f", f.read(4))[0]
                        vy577 = unpack("<f", f.read(4))[0]
                        vz577 = unpack("<f", f.read(4))[0]
                        type577 = unpack("B", f.read(1))[0]
                        value1a577 = unpack("B", f.read(1))[0]
                        normalZ_577 = unpack("<h", f.read(2))[0]
                        vx578 = unpack("<f", f.read(4))[0]
                        vy578 = unpack("<f", f.read(4))[0]
                        vz578 = unpack("<f", f.read(4))[0]
                        type578 = unpack("B", f.read(1))[0]
                        value1a578 = unpack("B", f.read(1))[0]
                        normalZ_578 = unpack("<h", f.read(2))[0]
                        vx579 = unpack("<f", f.read(4))[0]
                        vy579 = unpack("<f", f.read(4))[0]
                        vz579 = unpack("<f", f.read(4))[0]
                        type579 = unpack("B", f.read(1))[0]
                        value1a579 = unpack("B", f.read(1))[0]
                        normalZ_579 = unpack("<h", f.read(2))[0]
                        vx580 = unpack("<f", f.read(4))[0]
                        vy580 = unpack("<f", f.read(4))[0]
                        vz580 = unpack("<f", f.read(4))[0]
                        type580 = unpack("B", f.read(1))[0]
                        value1a580 = unpack("B", f.read(1))[0]
                        normalZ_580 = unpack("<h", f.read(2))[0]
                        vx581 = unpack("<f", f.read(4))[0]
                        vy581 = unpack("<f", f.read(4))[0]
                        vz581 = unpack("<f", f.read(4))[0]
                        type581 = unpack("B", f.read(1))[0]
                        value1a581 = unpack("B", f.read(1))[0]
                        normalZ_581 = unpack("<h", f.read(2))[0]
                        vx582 = unpack("<f", f.read(4))[0]
                        vy582 = unpack("<f", f.read(4))[0]
                        vz582 = unpack("<f", f.read(4))[0]
                        type582 = unpack("B", f.read(1))[0]
                        value1a582 = unpack("B", f.read(1))[0]
                        normalZ_582 = unpack("<h", f.read(2))[0]
                        vx583 = unpack("<f", f.read(4))[0]
                        vy583 = unpack("<f", f.read(4))[0]
                        vz583 = unpack("<f", f.read(4))[0]
                        type583 = unpack("B", f.read(1))[0]
                        value1a583 = unpack("B", f.read(1))[0]
                        normalZ_583 = unpack("<h", f.read(2))[0]
                        vx584 = unpack("<f", f.read(4))[0]
                        vy584 = unpack("<f", f.read(4))[0]
                        vz584 = unpack("<f", f.read(4))[0]
                        type584 = unpack("B", f.read(1))[0]
                        value1a584 = unpack("B", f.read(1))[0]
                        normalZ_584 = unpack("<h", f.read(2))[0]
                        vx585 = unpack("<f", f.read(4))[0]
                        vy585 = unpack("<f", f.read(4))[0]
                        vz585 = unpack("<f", f.read(4))[0]
                        type585 = unpack("B", f.read(1))[0]
                        value1a585 = unpack("B", f.read(1))[0]
                        normalZ_585 = unpack("<h", f.read(2))[0]
                        vx586 = unpack("<f", f.read(4))[0]
                        vy586 = unpack("<f", f.read(4))[0]
                        vz586 = unpack("<f", f.read(4))[0]
                        type586 = unpack("B", f.read(1))[0]
                        value1a586 = unpack("B", f.read(1))[0]
                        normalZ_586 = unpack("<h", f.read(2))[0]
                        vx587 = unpack("<f", f.read(4))[0]
                        vy587 = unpack("<f", f.read(4))[0]
                        vz587 = unpack("<f", f.read(4))[0]
                        type587 = unpack("B", f.read(1))[0]
                        value1a587 = unpack("B", f.read(1))[0]
                        normalZ_587 = unpack("<h", f.read(2))[0]
                        vx588 = unpack("<f", f.read(4))[0]
                        vy588 = unpack("<f", f.read(4))[0]
                        vz588 = unpack("<f", f.read(4))[0]
                        type588 = unpack("B", f.read(1))[0]
                        value1a588 = unpack("B", f.read(1))[0]
                        normalZ_588 = unpack("<h", f.read(2))[0]
                        vx589 = unpack("<f", f.read(4))[0]
                        vy589 = unpack("<f", f.read(4))[0]
                        vz589 = unpack("<f", f.read(4))[0]
                        type589 = unpack("B", f.read(1))[0]
                        value1a589 = unpack("B", f.read(1))[0]
                        normalZ_589 = unpack("<h", f.read(2))[0]
                        vx590 = unpack("<f", f.read(4))[0]
                        vy590 = unpack("<f", f.read(4))[0]
                        vz590 = unpack("<f", f.read(4))[0]
                        type590 = unpack("B", f.read(1))[0]
                        value1a590 = unpack("B", f.read(1))[0]
                        normalZ_590 = unpack("<h", f.read(2))[0]
                        vx591 = unpack("<f", f.read(4))[0]
                        vy591 = unpack("<f", f.read(4))[0]
                        vz591 = unpack("<f", f.read(4))[0]
                        type591 = unpack("B", f.read(1))[0]
                        value1a591 = unpack("B", f.read(1))[0]
                        normalZ_591 = unpack("<h", f.read(2))[0]
                        vertices.append([vx558,vz558,vy558])
                        vertices.append([vx559,vz559,vy559])
                        vertices.append([vx560,vz560,vy560])
                        vertices.append([vx561,vz561,vy561])
                        vertices.append([vx562,vz562,vy562])
                        vertices.append([vx563,vz563,vy563])
                        vertices.append([vx564,vz564,vy564])
                        vertices.append([vx565,vz565,vy565])
                        vertices.append([vx566,vz566,vy566])
                        vertices.append([vx567,vz567,vy567])
                        vertices.append([vx568,vz568,vy568])
                        vertices.append([vx569,vz569,vy569])
                        vertices.append([vx570,vz570,vy570])
                        vertices.append([vx571,vz571,vy571])
                        vertices.append([vx572,vz572,vy572])
                        vertices.append([vx573,vz573,vy573])
                        vertices.append([vx574,vz574,vy574])
                        vertices.append([vx575,vz575,vy575])
                        vertices.append([vx576,vz576,vy576])
                        vertices.append([vx577,vz577,vy577])
                        vertices.append([vx578,vz578,vy578])
                        vertices.append([vx579,vz579,vy579])
                        vertices.append([vx580,vz580,vy580])
                        vertices.append([vx581,vz581,vy581])
                        vertices.append([vx582,vz582,vy582])
                        vertices.append([vx583,vz583,vy583])
                        vertices.append([vx584,vz584,vy584])
                        vertices.append([vx585,vz585,vy585])
                        vertices.append([vx586,vz586,vy586])
                        vertices.append([vx587,vz587,vy587])
                        vertices.append([vx588,vz588,vy588])
                        vertices.append([vx589,vz589,vy589])
                        vertices.append([vx590,vz590,vy590])
                        vertices.append([vx591,vz591,vy591])

                elif vertexCount == 35:
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
                        vx592 = unpack("<f", f.read(4))[0]
                        vy592 = unpack("<f", f.read(4))[0]
                        vz592 = unpack("<f", f.read(4))[0]
                        type592 = unpack("B", f.read(1))[0]
                        value1a592 = unpack("B", f.read(1))[0]
                        normalZ_592 = unpack("<h", f.read(2))[0]
                        vx593 = unpack("<f", f.read(4))[0]
                        vy593 = unpack("<f", f.read(4))[0]
                        vz593 = unpack("<f", f.read(4))[0]
                        type593 = unpack("B", f.read(1))[0]
                        value1a593 = unpack("B", f.read(1))[0]
                        normalZ_593 = unpack("<h", f.read(2))[0]
                        vx594 = unpack("<f", f.read(4))[0]
                        vy594 = unpack("<f", f.read(4))[0]
                        vz594 = unpack("<f", f.read(4))[0]
                        type594 = unpack("B", f.read(1))[0]
                        value1a594 = unpack("B", f.read(1))[0]
                        normalZ_594 = unpack("<h", f.read(2))[0]
                        vx595 = unpack("<f", f.read(4))[0]
                        vy595 = unpack("<f", f.read(4))[0]
                        vz595 = unpack("<f", f.read(4))[0]
                        type595 = unpack("B", f.read(1))[0]
                        value1a595 = unpack("B", f.read(1))[0]
                        normalZ_595 = unpack("<h", f.read(2))[0]
                        vx596 = unpack("<f", f.read(4))[0]
                        vy596 = unpack("<f", f.read(4))[0]
                        vz596 = unpack("<f", f.read(4))[0]
                        type596 = unpack("B", f.read(1))[0]
                        value1a596 = unpack("B", f.read(1))[0]
                        normalZ_596 = unpack("<h", f.read(2))[0]
                        vx597 = unpack("<f", f.read(4))[0]
                        vy597 = unpack("<f", f.read(4))[0]
                        vz597 = unpack("<f", f.read(4))[0]
                        type597 = unpack("B", f.read(1))[0]
                        value1a597 = unpack("B", f.read(1))[0]
                        normalZ_597 = unpack("<h", f.read(2))[0]
                        vx598 = unpack("<f", f.read(4))[0]
                        vy598 = unpack("<f", f.read(4))[0]
                        vz598 = unpack("<f", f.read(4))[0]
                        type598 = unpack("B", f.read(1))[0]
                        value1a598 = unpack("B", f.read(1))[0]
                        normalZ_598 = unpack("<h", f.read(2))[0]
                        vx599 = unpack("<f", f.read(4))[0]
                        vy599 = unpack("<f", f.read(4))[0]
                        vz599 = unpack("<f", f.read(4))[0]
                        type599 = unpack("B", f.read(1))[0]
                        value1a599 = unpack("B", f.read(1))[0]
                        normalZ_599 = unpack("<h", f.read(2))[0]
                        vx600 = unpack("<f", f.read(4))[0]
                        vy600 = unpack("<f", f.read(4))[0]
                        vz600 = unpack("<f", f.read(4))[0]
                        type600 = unpack("B", f.read(1))[0]
                        value1a600 = unpack("B", f.read(1))[0]
                        normalZ_600 = unpack("<h", f.read(2))[0]
                        vx601 = unpack("<f", f.read(4))[0]
                        vy601 = unpack("<f", f.read(4))[0]
                        vz601 = unpack("<f", f.read(4))[0]
                        type601 = unpack("B", f.read(1))[0]
                        value1a601 = unpack("B", f.read(1))[0]
                        normalZ_601 = unpack("<h", f.read(2))[0]
                        vx602 = unpack("<f", f.read(4))[0]
                        vy602 = unpack("<f", f.read(4))[0]
                        vz602 = unpack("<f", f.read(4))[0]
                        type602 = unpack("B", f.read(1))[0]
                        value1a602 = unpack("B", f.read(1))[0]
                        normalZ_602 = unpack("<h", f.read(2))[0]
                        vx603 = unpack("<f", f.read(4))[0]
                        vy603 = unpack("<f", f.read(4))[0]
                        vz603 = unpack("<f", f.read(4))[0]
                        type603 = unpack("B", f.read(1))[0]
                        value1a603 = unpack("B", f.read(1))[0]
                        normalZ_603 = unpack("<h", f.read(2))[0]
                        vx604 = unpack("<f", f.read(4))[0]
                        vy604 = unpack("<f", f.read(4))[0]
                        vz604 = unpack("<f", f.read(4))[0]
                        type604 = unpack("B", f.read(1))[0]
                        value1a604 = unpack("B", f.read(1))[0]
                        normalZ_604 = unpack("<h", f.read(2))[0]
                        vx605 = unpack("<f", f.read(4))[0]
                        vy605 = unpack("<f", f.read(4))[0]
                        vz605 = unpack("<f", f.read(4))[0]
                        type605 = unpack("B", f.read(1))[0]
                        value1a605 = unpack("B", f.read(1))[0]
                        normalZ_605 = unpack("<h", f.read(2))[0]
                        vx606 = unpack("<f", f.read(4))[0]
                        vy606 = unpack("<f", f.read(4))[0]
                        vz606 = unpack("<f", f.read(4))[0]
                        type606 = unpack("B", f.read(1))[0]
                        value1a606 = unpack("B", f.read(1))[0]
                        normalZ_606 = unpack("<h", f.read(2))[0]
                        vx607 = unpack("<f", f.read(4))[0]
                        vy607 = unpack("<f", f.read(4))[0]
                        vz607 = unpack("<f", f.read(4))[0]
                        type607 = unpack("B", f.read(1))[0]
                        value1a607 = unpack("B", f.read(1))[0]
                        normalZ_607 = unpack("<h", f.read(2))[0]
                        vx608 = unpack("<f", f.read(4))[0]
                        vy608 = unpack("<f", f.read(4))[0]
                        vz608 = unpack("<f", f.read(4))[0]
                        type608 = unpack("B", f.read(1))[0]
                        value1a608 = unpack("B", f.read(1))[0]
                        normalZ_608 = unpack("<h", f.read(2))[0]
                        vx609 = unpack("<f", f.read(4))[0]
                        vy609 = unpack("<f", f.read(4))[0]
                        vz609 = unpack("<f", f.read(4))[0]
                        type609 = unpack("B", f.read(1))[0]
                        value1a609 = unpack("B", f.read(1))[0]
                        normalZ_609 = unpack("<h", f.read(2))[0]
                        vx610 = unpack("<f", f.read(4))[0]
                        vy610 = unpack("<f", f.read(4))[0]
                        vz610 = unpack("<f", f.read(4))[0]
                        type610 = unpack("B", f.read(1))[0]
                        value1a610 = unpack("B", f.read(1))[0]
                        normalZ_610 = unpack("<h", f.read(2))[0]
                        vx611 = unpack("<f", f.read(4))[0]
                        vy611 = unpack("<f", f.read(4))[0]
                        vz611 = unpack("<f", f.read(4))[0]
                        type611 = unpack("B", f.read(1))[0]
                        value1a611 = unpack("B", f.read(1))[0]
                        normalZ_611 = unpack("<h", f.read(2))[0]
                        vx612 = unpack("<f", f.read(4))[0]
                        vy612 = unpack("<f", f.read(4))[0]
                        vz612 = unpack("<f", f.read(4))[0]
                        type612 = unpack("B", f.read(1))[0]
                        value1a612 = unpack("B", f.read(1))[0]
                        normalZ_612 = unpack("<h", f.read(2))[0]
                        vx613 = unpack("<f", f.read(4))[0]
                        vy613 = unpack("<f", f.read(4))[0]
                        vz613 = unpack("<f", f.read(4))[0]
                        type613 = unpack("B", f.read(1))[0]
                        value1a613 = unpack("B", f.read(1))[0]
                        normalZ_613 = unpack("<h", f.read(2))[0]
                        vx614 = unpack("<f", f.read(4))[0]
                        vy614 = unpack("<f", f.read(4))[0]
                        vz614 = unpack("<f", f.read(4))[0]
                        type614 = unpack("B", f.read(1))[0]
                        value1a614 = unpack("B", f.read(1))[0]
                        normalZ_614 = unpack("<h", f.read(2))[0]
                        vx615 = unpack("<f", f.read(4))[0]
                        vy615 = unpack("<f", f.read(4))[0]
                        vz615 = unpack("<f", f.read(4))[0]
                        type615 = unpack("B", f.read(1))[0]
                        value1a615 = unpack("B", f.read(1))[0]
                        normalZ_615 = unpack("<h", f.read(2))[0]
                        vx616 = unpack("<f", f.read(4))[0]
                        vy616 = unpack("<f", f.read(4))[0]
                        vz616 = unpack("<f", f.read(4))[0]
                        type616 = unpack("B", f.read(1))[0]
                        value1a616 = unpack("B", f.read(1))[0]
                        normalZ_616 = unpack("<h", f.read(2))[0]
                        vx617 = unpack("<f", f.read(4))[0]
                        vy617 = unpack("<f", f.read(4))[0]
                        vz617 = unpack("<f", f.read(4))[0]
                        type617 = unpack("B", f.read(1))[0]
                        value1a617 = unpack("B", f.read(1))[0]
                        normalZ_617 = unpack("<h", f.read(2))[0]
                        vx618 = unpack("<f", f.read(4))[0]
                        vy618 = unpack("<f", f.read(4))[0]
                        vz618 = unpack("<f", f.read(4))[0]
                        type618 = unpack("B", f.read(1))[0]
                        value1a618 = unpack("B", f.read(1))[0]
                        normalZ_618 = unpack("<h", f.read(2))[0]
                        vx619 = unpack("<f", f.read(4))[0]
                        vy619 = unpack("<f", f.read(4))[0]
                        vz619 = unpack("<f", f.read(4))[0]
                        type619 = unpack("B", f.read(1))[0]
                        value1a619 = unpack("B", f.read(1))[0]
                        normalZ_619 = unpack("<h", f.read(2))[0]
                        vx620 = unpack("<f", f.read(4))[0]
                        vy620 = unpack("<f", f.read(4))[0]
                        vz620 = unpack("<f", f.read(4))[0]
                        type620 = unpack("B", f.read(1))[0]
                        value1a620 = unpack("B", f.read(1))[0]
                        normalZ_620 = unpack("<h", f.read(2))[0]
                        vx621 = unpack("<f", f.read(4))[0]
                        vy621 = unpack("<f", f.read(4))[0]
                        vz621 = unpack("<f", f.read(4))[0]
                        type621 = unpack("B", f.read(1))[0]
                        value1a621 = unpack("B", f.read(1))[0]
                        normalZ_621 = unpack("<h", f.read(2))[0]
                        vx622 = unpack("<f", f.read(4))[0]
                        vy622 = unpack("<f", f.read(4))[0]
                        vz622 = unpack("<f", f.read(4))[0]
                        type622 = unpack("B", f.read(1))[0]
                        value1a622 = unpack("B", f.read(1))[0]
                        normalZ_622 = unpack("<h", f.read(2))[0]
                        vx623 = unpack("<f", f.read(4))[0]
                        vy623 = unpack("<f", f.read(4))[0]
                        vz623 = unpack("<f", f.read(4))[0]
                        type623 = unpack("B", f.read(1))[0]
                        value1a623 = unpack("B", f.read(1))[0]
                        normalZ_623 = unpack("<h", f.read(2))[0]
                        vx624 = unpack("<f", f.read(4))[0]
                        vy624 = unpack("<f", f.read(4))[0]
                        vz624 = unpack("<f", f.read(4))[0]
                        type624 = unpack("B", f.read(1))[0]
                        value1a624 = unpack("B", f.read(1))[0]
                        normalZ_624 = unpack("<h", f.read(2))[0]
                        vx625 = unpack("<f", f.read(4))[0]
                        vy625 = unpack("<f", f.read(4))[0]
                        vz625 = unpack("<f", f.read(4))[0]
                        type625 = unpack("B", f.read(1))[0]
                        value1a625 = unpack("B", f.read(1))[0]
                        normalZ_625 = unpack("<h", f.read(2))[0]
                        vx626 = unpack("<f", f.read(4))[0]
                        vy626 = unpack("<f", f.read(4))[0]
                        vz626 = unpack("<f", f.read(4))[0]
                        type626 = unpack("B", f.read(1))[0]
                        value1a626 = unpack("B", f.read(1))[0]
                        normalZ_626 = unpack("<h", f.read(2))[0]
                        vertices.append([vx592,vz592,vy592])
                        vertices.append([vx593,vz593,vy593])
                        vertices.append([vx594,vz594,vy594])
                        vertices.append([vx595,vz595,vy595])
                        vertices.append([vx596,vz596,vy596])
                        vertices.append([vx597,vz597,vy597])
                        vertices.append([vx598,vz598,vy598])
                        vertices.append([vx599,vz599,vy599])
                        vertices.append([vx600,vz600,vy600])
                        vertices.append([vx601,vz601,vy601])
                        vertices.append([vx602,vz602,vy602])
                        vertices.append([vx603,vz603,vy603])
                        vertices.append([vx604,vz604,vy604])
                        vertices.append([vx605,vz605,vy605])
                        vertices.append([vx606,vz606,vy606])
                        vertices.append([vx607,vz607,vy607])
                        vertices.append([vx608,vz608,vy608])
                        vertices.append([vx609,vz609,vy609])
                        vertices.append([vx610,vz610,vy610])
                        vertices.append([vx611,vz611,vy611])
                        vertices.append([vx612,vz612,vy612])
                        vertices.append([vx613,vz613,vy613])
                        vertices.append([vx614,vz614,vy614])
                        vertices.append([vx615,vz615,vy615])
                        vertices.append([vx616,vz616,vy616])
                        vertices.append([vx617,vz617,vy617])
                        vertices.append([vx618,vz618,vy618])
                        vertices.append([vx619,vz619,vy619])
                        vertices.append([vx620,vz620,vy620])
                        vertices.append([vx621,vz621,vy621])
                        vertices.append([vx622,vz622,vy622])
                        vertices.append([vx623,vz623,vy623])
                        vertices.append([vx624,vz624,vy624])
                        vertices.append([vx625,vz625,vy625])
                        vertices.append([vx626,vz626,vy626])

                elif vertexCount == 36:
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
                        vx627 = unpack("<f", f.read(4))[0]
                        vy627 = unpack("<f", f.read(4))[0]
                        vz627 = unpack("<f", f.read(4))[0]
                        type627 = unpack("B", f.read(1))[0]
                        value1a627 = unpack("B", f.read(1))[0]
                        normalZ_627 = unpack("<h", f.read(2))[0]
                        vx628 = unpack("<f", f.read(4))[0]
                        vy628 = unpack("<f", f.read(4))[0]
                        vz628 = unpack("<f", f.read(4))[0]
                        type628 = unpack("B", f.read(1))[0]
                        value1a628 = unpack("B", f.read(1))[0]
                        normalZ_628 = unpack("<h", f.read(2))[0]
                        vx629 = unpack("<f", f.read(4))[0]
                        vy629 = unpack("<f", f.read(4))[0]
                        vz629 = unpack("<f", f.read(4))[0]
                        type629 = unpack("B", f.read(1))[0]
                        value1a629 = unpack("B", f.read(1))[0]
                        normalZ_629 = unpack("<h", f.read(2))[0]
                        vx630 = unpack("<f", f.read(4))[0]
                        vy630 = unpack("<f", f.read(4))[0]
                        vz630 = unpack("<f", f.read(4))[0]
                        type630 = unpack("B", f.read(1))[0]
                        value1a630 = unpack("B", f.read(1))[0]
                        normalZ_630 = unpack("<h", f.read(2))[0]
                        vx631 = unpack("<f", f.read(4))[0]
                        vy631 = unpack("<f", f.read(4))[0]
                        vz631 = unpack("<f", f.read(4))[0]
                        type631 = unpack("B", f.read(1))[0]
                        value1a631 = unpack("B", f.read(1))[0]
                        normalZ_631 = unpack("<h", f.read(2))[0]
                        vx632 = unpack("<f", f.read(4))[0]
                        vy632 = unpack("<f", f.read(4))[0]
                        vz632 = unpack("<f", f.read(4))[0]
                        type632 = unpack("B", f.read(1))[0]
                        value1a632 = unpack("B", f.read(1))[0]
                        normalZ_632 = unpack("<h", f.read(2))[0]
                        vx633 = unpack("<f", f.read(4))[0]
                        vy633 = unpack("<f", f.read(4))[0]
                        vz633 = unpack("<f", f.read(4))[0]
                        type633 = unpack("B", f.read(1))[0]
                        value1a633 = unpack("B", f.read(1))[0]
                        normalZ_633 = unpack("<h", f.read(2))[0]
                        vx634 = unpack("<f", f.read(4))[0]
                        vy634 = unpack("<f", f.read(4))[0]
                        vz634 = unpack("<f", f.read(4))[0]
                        type634 = unpack("B", f.read(1))[0]
                        value1a634 = unpack("B", f.read(1))[0]
                        normalZ_634 = unpack("<h", f.read(2))[0]
                        vx635 = unpack("<f", f.read(4))[0]
                        vy635 = unpack("<f", f.read(4))[0]
                        vz635 = unpack("<f", f.read(4))[0]
                        type635 = unpack("B", f.read(1))[0]
                        value1a635 = unpack("B", f.read(1))[0]
                        normalZ_635 = unpack("<h", f.read(2))[0]
                        vx636 = unpack("<f", f.read(4))[0]
                        vy636 = unpack("<f", f.read(4))[0]
                        vz636 = unpack("<f", f.read(4))[0]
                        type636 = unpack("B", f.read(1))[0]
                        value1a636 = unpack("B", f.read(1))[0]
                        normalZ_636 = unpack("<h", f.read(2))[0]
                        vx637 = unpack("<f", f.read(4))[0]
                        vy637 = unpack("<f", f.read(4))[0]
                        vz637 = unpack("<f", f.read(4))[0]
                        type637 = unpack("B", f.read(1))[0]
                        value1a637 = unpack("B", f.read(1))[0]
                        normalZ_637 = unpack("<h", f.read(2))[0]
                        vx638 = unpack("<f", f.read(4))[0]
                        vy638 = unpack("<f", f.read(4))[0]
                        vz638 = unpack("<f", f.read(4))[0]
                        type638 = unpack("B", f.read(1))[0]
                        value1a638 = unpack("B", f.read(1))[0]
                        normalZ_638 = unpack("<h", f.read(2))[0]
                        vx639 = unpack("<f", f.read(4))[0]
                        vy639 = unpack("<f", f.read(4))[0]
                        vz639 = unpack("<f", f.read(4))[0]
                        type639 = unpack("B", f.read(1))[0]
                        value1a639 = unpack("B", f.read(1))[0]
                        normalZ_639 = unpack("<h", f.read(2))[0]
                        vx640 = unpack("<f", f.read(4))[0]
                        vy640 = unpack("<f", f.read(4))[0]
                        vz640 = unpack("<f", f.read(4))[0]
                        type640 = unpack("B", f.read(1))[0]
                        value1a640 = unpack("B", f.read(1))[0]
                        normalZ_640 = unpack("<h", f.read(2))[0]
                        vx641 = unpack("<f", f.read(4))[0]
                        vy641 = unpack("<f", f.read(4))[0]
                        vz641 = unpack("<f", f.read(4))[0]
                        type641 = unpack("B", f.read(1))[0]
                        value1a641 = unpack("B", f.read(1))[0]
                        normalZ_641 = unpack("<h", f.read(2))[0]
                        vx642 = unpack("<f", f.read(4))[0]
                        vy642 = unpack("<f", f.read(4))[0]
                        vz642 = unpack("<f", f.read(4))[0]
                        type642 = unpack("B", f.read(1))[0]
                        value1a642 = unpack("B", f.read(1))[0]
                        normalZ_642 = unpack("<h", f.read(2))[0]
                        vx643 = unpack("<f", f.read(4))[0]
                        vy643 = unpack("<f", f.read(4))[0]
                        vz643 = unpack("<f", f.read(4))[0]
                        type643 = unpack("B", f.read(1))[0]
                        value1a643 = unpack("B", f.read(1))[0]
                        normalZ_643 = unpack("<h", f.read(2))[0]
                        vx644 = unpack("<f", f.read(4))[0]
                        vy644 = unpack("<f", f.read(4))[0]
                        vz644 = unpack("<f", f.read(4))[0]
                        type644 = unpack("B", f.read(1))[0]
                        value1a644 = unpack("B", f.read(1))[0]
                        normalZ_644 = unpack("<h", f.read(2))[0]
                        vx645 = unpack("<f", f.read(4))[0]
                        vy645 = unpack("<f", f.read(4))[0]
                        vz645 = unpack("<f", f.read(4))[0]
                        type645 = unpack("B", f.read(1))[0]
                        value1a645 = unpack("B", f.read(1))[0]
                        normalZ_645 = unpack("<h", f.read(2))[0]
                        vx646 = unpack("<f", f.read(4))[0]
                        vy646 = unpack("<f", f.read(4))[0]
                        vz646 = unpack("<f", f.read(4))[0]
                        type646 = unpack("B", f.read(1))[0]
                        value1a646 = unpack("B", f.read(1))[0]
                        normalZ_646 = unpack("<h", f.read(2))[0]
                        vx647 = unpack("<f", f.read(4))[0]
                        vy647 = unpack("<f", f.read(4))[0]
                        vz647 = unpack("<f", f.read(4))[0]
                        type647 = unpack("B", f.read(1))[0]
                        value1a647 = unpack("B", f.read(1))[0]
                        normalZ_647 = unpack("<h", f.read(2))[0]
                        vx648 = unpack("<f", f.read(4))[0]
                        vy648 = unpack("<f", f.read(4))[0]
                        vz648 = unpack("<f", f.read(4))[0]
                        type648 = unpack("B", f.read(1))[0]
                        value1a648 = unpack("B", f.read(1))[0]
                        normalZ_648 = unpack("<h", f.read(2))[0]
                        vx649 = unpack("<f", f.read(4))[0]
                        vy649 = unpack("<f", f.read(4))[0]
                        vz649 = unpack("<f", f.read(4))[0]
                        type649 = unpack("B", f.read(1))[0]
                        value1a649 = unpack("B", f.read(1))[0]
                        normalZ_649 = unpack("<h", f.read(2))[0]
                        vx650 = unpack("<f", f.read(4))[0]
                        vy650 = unpack("<f", f.read(4))[0]
                        vz650 = unpack("<f", f.read(4))[0]
                        type650 = unpack("B", f.read(1))[0]
                        value1a650 = unpack("B", f.read(1))[0]
                        normalZ_650 = unpack("<h", f.read(2))[0]
                        vx651 = unpack("<f", f.read(4))[0]
                        vy651 = unpack("<f", f.read(4))[0]
                        vz651 = unpack("<f", f.read(4))[0]
                        type651 = unpack("B", f.read(1))[0]
                        value1a651 = unpack("B", f.read(1))[0]
                        normalZ_651 = unpack("<h", f.read(2))[0]
                        vx652 = unpack("<f", f.read(4))[0]
                        vy652 = unpack("<f", f.read(4))[0]
                        vz652 = unpack("<f", f.read(4))[0]
                        type652 = unpack("B", f.read(1))[0]
                        value1a652 = unpack("B", f.read(1))[0]
                        normalZ_652 = unpack("<h", f.read(2))[0]
                        vx653 = unpack("<f", f.read(4))[0]
                        vy653 = unpack("<f", f.read(4))[0]
                        vz653 = unpack("<f", f.read(4))[0]
                        type653 = unpack("B", f.read(1))[0]
                        value1a653 = unpack("B", f.read(1))[0]
                        normalZ_653 = unpack("<h", f.read(2))[0]
                        vx654 = unpack("<f", f.read(4))[0]
                        vy654 = unpack("<f", f.read(4))[0]
                        vz654 = unpack("<f", f.read(4))[0]
                        type654 = unpack("B", f.read(1))[0]
                        value1a654 = unpack("B", f.read(1))[0]
                        normalZ_654 = unpack("<h", f.read(2))[0]
                        vx655 = unpack("<f", f.read(4))[0]
                        vy655 = unpack("<f", f.read(4))[0]
                        vz655 = unpack("<f", f.read(4))[0]
                        type655 = unpack("B", f.read(1))[0]
                        value1a655 = unpack("B", f.read(1))[0]
                        normalZ_655 = unpack("<h", f.read(2))[0]
                        vx656 = unpack("<f", f.read(4))[0]
                        vy656 = unpack("<f", f.read(4))[0]
                        vz656 = unpack("<f", f.read(4))[0]
                        type656 = unpack("B", f.read(1))[0]
                        value1a656 = unpack("B", f.read(1))[0]
                        normalZ_656 = unpack("<h", f.read(2))[0]
                        vx657 = unpack("<f", f.read(4))[0]
                        vy657 = unpack("<f", f.read(4))[0]
                        vz657 = unpack("<f", f.read(4))[0]
                        type657 = unpack("B", f.read(1))[0]
                        value1a657 = unpack("B", f.read(1))[0]
                        normalZ_657 = unpack("<h", f.read(2))[0]
                        vx658 = unpack("<f", f.read(4))[0]
                        vy658 = unpack("<f", f.read(4))[0]
                        vz658 = unpack("<f", f.read(4))[0]
                        type658 = unpack("B", f.read(1))[0]
                        value1a658 = unpack("B", f.read(1))[0]
                        normalZ_658 = unpack("<h", f.read(2))[0]
                        vx659 = unpack("<f", f.read(4))[0]
                        vy659 = unpack("<f", f.read(4))[0]
                        vz659 = unpack("<f", f.read(4))[0]
                        type659 = unpack("B", f.read(1))[0]
                        value1a659 = unpack("B", f.read(1))[0]
                        normalZ_659 = unpack("<h", f.read(2))[0]
                        vx660 = unpack("<f", f.read(4))[0]
                        vy660 = unpack("<f", f.read(4))[0]
                        vz660 = unpack("<f", f.read(4))[0]
                        type660 = unpack("B", f.read(1))[0]
                        value1a660 = unpack("B", f.read(1))[0]
                        normalZ_660 = unpack("<h", f.read(2))[0]
                        vx661 = unpack("<f", f.read(4))[0]
                        vy661 = unpack("<f", f.read(4))[0]
                        vz661 = unpack("<f", f.read(4))[0]
                        type661 = unpack("B", f.read(1))[0]
                        value1a661 = unpack("B", f.read(1))[0]
                        normalZ_661 = unpack("<h", f.read(2))[0]
                        vx662 = unpack("<f", f.read(4))[0]
                        vy662 = unpack("<f", f.read(4))[0]
                        vz662 = unpack("<f", f.read(4))[0]
                        type662 = unpack("B", f.read(1))[0]
                        value1a662 = unpack("B", f.read(1))[0]
                        normalZ_662 = unpack("<h", f.read(2))[0]
                        vertices.append([vx627,vz627,vy627])
                        vertices.append([vx628,vz628,vy628])
                        vertices.append([vx629,vz629,vy629])
                        vertices.append([vx630,vz630,vy630])
                        vertices.append([vx631,vz631,vy631])
                        vertices.append([vx632,vz632,vy632])
                        vertices.append([vx633,vz633,vy633])
                        vertices.append([vx634,vz634,vy634])
                        vertices.append([vx635,vz635,vy635])
                        vertices.append([vx636,vz636,vy636])
                        vertices.append([vx637,vz637,vy637])
                        vertices.append([vx638,vz638,vy638])
                        vertices.append([vx639,vz639,vy639])
                        vertices.append([vx640,vz640,vy640])
                        vertices.append([vx641,vz641,vy641])
                        vertices.append([vx642,vz642,vy642])
                        vertices.append([vx643,vz643,vy643])
                        vertices.append([vx644,vz644,vy644])
                        vertices.append([vx645,vz645,vy645])
                        vertices.append([vx646,vz646,vy646])
                        vertices.append([vx647,vz647,vy647])
                        vertices.append([vx648,vz648,vy648])
                        vertices.append([vx649,vz649,vy649])
                        vertices.append([vx650,vz650,vy650])
                        vertices.append([vx651,vz651,vy651])
                        vertices.append([vx652,vz652,vy652])
                        vertices.append([vx653,vz653,vy653])
                        vertices.append([vx654,vz654,vy654])
                        vertices.append([vx655,vz655,vy655])
                        vertices.append([vx656,vz656,vy656])
                        vertices.append([vx657,vz657,vy657])
                        vertices.append([vx658,vz658,vy658])
                        vertices.append([vx659,vz659,vy659])
                        vertices.append([vx660,vz660,vy660])
                        vertices.append([vx661,vz661,vy661])
                        vertices.append([vx662,vz662,vy662])


                elif vertexCount == 37:
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
                        vx663 = unpack("<f", f.read(4))[0]
                        vy663 = unpack("<f", f.read(4))[0]
                        vz663 = unpack("<f", f.read(4))[0]
                        type663 = unpack("B", f.read(1))[0]
                        value1a663 = unpack("B", f.read(1))[0]
                        normalZ_663 = unpack("<h", f.read(2))[0]
                        vx664 = unpack("<f", f.read(4))[0]
                        vy664 = unpack("<f", f.read(4))[0]
                        vz664 = unpack("<f", f.read(4))[0]
                        type664 = unpack("B", f.read(1))[0]
                        value1a664 = unpack("B", f.read(1))[0]
                        normalZ_664 = unpack("<h", f.read(2))[0]
                        vx665 = unpack("<f", f.read(4))[0]
                        vy665 = unpack("<f", f.read(4))[0]
                        vz665 = unpack("<f", f.read(4))[0]
                        type665 = unpack("B", f.read(1))[0]
                        value1a665 = unpack("B", f.read(1))[0]
                        normalZ_665 = unpack("<h", f.read(2))[0]
                        vx666 = unpack("<f", f.read(4))[0]
                        vy666 = unpack("<f", f.read(4))[0]
                        vz666 = unpack("<f", f.read(4))[0]
                        type666 = unpack("B", f.read(1))[0]
                        value1a666 = unpack("B", f.read(1))[0]
                        normalZ_666 = unpack("<h", f.read(2))[0]
                        vx667 = unpack("<f", f.read(4))[0]
                        vy667 = unpack("<f", f.read(4))[0]
                        vz667 = unpack("<f", f.read(4))[0]
                        type667 = unpack("B", f.read(1))[0]
                        value1a667 = unpack("B", f.read(1))[0]
                        normalZ_667 = unpack("<h", f.read(2))[0]
                        vx668 = unpack("<f", f.read(4))[0]
                        vy668 = unpack("<f", f.read(4))[0]
                        vz668 = unpack("<f", f.read(4))[0]
                        type668 = unpack("B", f.read(1))[0]
                        value1a668 = unpack("B", f.read(1))[0]
                        normalZ_668 = unpack("<h", f.read(2))[0]
                        vx669 = unpack("<f", f.read(4))[0]
                        vy669 = unpack("<f", f.read(4))[0]
                        vz669 = unpack("<f", f.read(4))[0]
                        type669 = unpack("B", f.read(1))[0]
                        value1a669 = unpack("B", f.read(1))[0]
                        normalZ_669 = unpack("<h", f.read(2))[0]
                        vx670 = unpack("<f", f.read(4))[0]
                        vy670 = unpack("<f", f.read(4))[0]
                        vz670 = unpack("<f", f.read(4))[0]
                        type670 = unpack("B", f.read(1))[0]
                        value1a670 = unpack("B", f.read(1))[0]
                        normalZ_670 = unpack("<h", f.read(2))[0]
                        vx671 = unpack("<f", f.read(4))[0]
                        vy671 = unpack("<f", f.read(4))[0]
                        vz671 = unpack("<f", f.read(4))[0]
                        type671 = unpack("B", f.read(1))[0]
                        value1a671 = unpack("B", f.read(1))[0]
                        normalZ_671 = unpack("<h", f.read(2))[0]
                        vx672 = unpack("<f", f.read(4))[0]
                        vy672 = unpack("<f", f.read(4))[0]
                        vz672 = unpack("<f", f.read(4))[0]
                        type672 = unpack("B", f.read(1))[0]
                        value1a672 = unpack("B", f.read(1))[0]
                        normalZ_672 = unpack("<h", f.read(2))[0]
                        vx673 = unpack("<f", f.read(4))[0]
                        vy673 = unpack("<f", f.read(4))[0]
                        vz673 = unpack("<f", f.read(4))[0]
                        type673 = unpack("B", f.read(1))[0]
                        value1a673 = unpack("B", f.read(1))[0]
                        normalZ_673 = unpack("<h", f.read(2))[0]
                        vx674 = unpack("<f", f.read(4))[0]
                        vy674 = unpack("<f", f.read(4))[0]
                        vz674 = unpack("<f", f.read(4))[0]
                        type674 = unpack("B", f.read(1))[0]
                        value1a674 = unpack("B", f.read(1))[0]
                        normalZ_674 = unpack("<h", f.read(2))[0]
                        vx675 = unpack("<f", f.read(4))[0]
                        vy675 = unpack("<f", f.read(4))[0]
                        vz675 = unpack("<f", f.read(4))[0]
                        type675 = unpack("B", f.read(1))[0]
                        value1a675 = unpack("B", f.read(1))[0]
                        normalZ_675 = unpack("<h", f.read(2))[0]
                        vx676 = unpack("<f", f.read(4))[0]
                        vy676 = unpack("<f", f.read(4))[0]
                        vz676 = unpack("<f", f.read(4))[0]
                        type676 = unpack("B", f.read(1))[0]
                        value1a676 = unpack("B", f.read(1))[0]
                        normalZ_676 = unpack("<h", f.read(2))[0]
                        vx677 = unpack("<f", f.read(4))[0]
                        vy677 = unpack("<f", f.read(4))[0]
                        vz677 = unpack("<f", f.read(4))[0]
                        type677 = unpack("B", f.read(1))[0]
                        value1a677 = unpack("B", f.read(1))[0]
                        normalZ_677 = unpack("<h", f.read(2))[0]
                        vx678 = unpack("<f", f.read(4))[0]
                        vy678 = unpack("<f", f.read(4))[0]
                        vz678 = unpack("<f", f.read(4))[0]
                        type678 = unpack("B", f.read(1))[0]
                        value1a678 = unpack("B", f.read(1))[0]
                        normalZ_678 = unpack("<h", f.read(2))[0]
                        vx679 = unpack("<f", f.read(4))[0]
                        vy679 = unpack("<f", f.read(4))[0]
                        vz679 = unpack("<f", f.read(4))[0]
                        type679 = unpack("B", f.read(1))[0]
                        value1a679 = unpack("B", f.read(1))[0]
                        normalZ_679 = unpack("<h", f.read(2))[0]
                        vx680 = unpack("<f", f.read(4))[0]
                        vy680 = unpack("<f", f.read(4))[0]
                        vz680 = unpack("<f", f.read(4))[0]
                        type680 = unpack("B", f.read(1))[0]
                        value1a680 = unpack("B", f.read(1))[0]
                        normalZ_680 = unpack("<h", f.read(2))[0]
                        vx681 = unpack("<f", f.read(4))[0]
                        vy681 = unpack("<f", f.read(4))[0]
                        vz681 = unpack("<f", f.read(4))[0]
                        type681 = unpack("B", f.read(1))[0]
                        value1a681 = unpack("B", f.read(1))[0]
                        normalZ_681 = unpack("<h", f.read(2))[0]
                        vx682 = unpack("<f", f.read(4))[0]
                        vy682 = unpack("<f", f.read(4))[0]
                        vz682 = unpack("<f", f.read(4))[0]
                        type682 = unpack("B", f.read(1))[0]
                        value1a682 = unpack("B", f.read(1))[0]
                        normalZ_682 = unpack("<h", f.read(2))[0]
                        vx683 = unpack("<f", f.read(4))[0]
                        vy683 = unpack("<f", f.read(4))[0]
                        vz683 = unpack("<f", f.read(4))[0]
                        type683 = unpack("B", f.read(1))[0]
                        value1a683 = unpack("B", f.read(1))[0]
                        normalZ_683 = unpack("<h", f.read(2))[0]
                        vx684 = unpack("<f", f.read(4))[0]
                        vy684 = unpack("<f", f.read(4))[0]
                        vz684 = unpack("<f", f.read(4))[0]
                        type684 = unpack("B", f.read(1))[0]
                        value1a684 = unpack("B", f.read(1))[0]
                        normalZ_684 = unpack("<h", f.read(2))[0]
                        vx685 = unpack("<f", f.read(4))[0]
                        vy685 = unpack("<f", f.read(4))[0]
                        vz685 = unpack("<f", f.read(4))[0]
                        type685 = unpack("B", f.read(1))[0]
                        value1a685 = unpack("B", f.read(1))[0]
                        normalZ_685 = unpack("<h", f.read(2))[0]
                        vx686 = unpack("<f", f.read(4))[0]
                        vy686 = unpack("<f", f.read(4))[0]
                        vz686 = unpack("<f", f.read(4))[0]
                        type686 = unpack("B", f.read(1))[0]
                        value1a686 = unpack("B", f.read(1))[0]
                        normalZ_686 = unpack("<h", f.read(2))[0]
                        vx687 = unpack("<f", f.read(4))[0]
                        vy687 = unpack("<f", f.read(4))[0]
                        vz687 = unpack("<f", f.read(4))[0]
                        type687 = unpack("B", f.read(1))[0]
                        value1a687 = unpack("B", f.read(1))[0]
                        normalZ_687 = unpack("<h", f.read(2))[0]
                        vx688 = unpack("<f", f.read(4))[0]
                        vy688 = unpack("<f", f.read(4))[0]
                        vz688 = unpack("<f", f.read(4))[0]
                        type688 = unpack("B", f.read(1))[0]
                        value1a688 = unpack("B", f.read(1))[0]
                        normalZ_688 = unpack("<h", f.read(2))[0]
                        vx689 = unpack("<f", f.read(4))[0]
                        vy689 = unpack("<f", f.read(4))[0]
                        vz689 = unpack("<f", f.read(4))[0]
                        type689 = unpack("B", f.read(1))[0]
                        value1a689 = unpack("B", f.read(1))[0]
                        normalZ_689 = unpack("<h", f.read(2))[0]
                        vx690 = unpack("<f", f.read(4))[0]
                        vy690 = unpack("<f", f.read(4))[0]
                        vz690 = unpack("<f", f.read(4))[0]
                        type690 = unpack("B", f.read(1))[0]
                        value1a690 = unpack("B", f.read(1))[0]
                        normalZ_690 = unpack("<h", f.read(2))[0]
                        vx691 = unpack("<f", f.read(4))[0]
                        vy691 = unpack("<f", f.read(4))[0]
                        vz691 = unpack("<f", f.read(4))[0]
                        type691 = unpack("B", f.read(1))[0]
                        value1a691 = unpack("B", f.read(1))[0]
                        normalZ_691 = unpack("<h", f.read(2))[0]
                        vx692 = unpack("<f", f.read(4))[0]
                        vy692 = unpack("<f", f.read(4))[0]
                        vz692 = unpack("<f", f.read(4))[0]
                        type692 = unpack("B", f.read(1))[0]
                        value1a692 = unpack("B", f.read(1))[0]
                        normalZ_692 = unpack("<h", f.read(2))[0]
                        vx693 = unpack("<f", f.read(4))[0]
                        vy693 = unpack("<f", f.read(4))[0]
                        vz693 = unpack("<f", f.read(4))[0]
                        type693 = unpack("B", f.read(1))[0]
                        value1a693 = unpack("B", f.read(1))[0]
                        normalZ_693 = unpack("<h", f.read(2))[0]
                        vx694 = unpack("<f", f.read(4))[0]
                        vy694 = unpack("<f", f.read(4))[0]
                        vz694 = unpack("<f", f.read(4))[0]
                        type694 = unpack("B", f.read(1))[0]
                        value1a694 = unpack("B", f.read(1))[0]
                        normalZ_694 = unpack("<h", f.read(2))[0]
                        vx695 = unpack("<f", f.read(4))[0]
                        vy695 = unpack("<f", f.read(4))[0]
                        vz695 = unpack("<f", f.read(4))[0]
                        type695 = unpack("B", f.read(1))[0]
                        value1a695 = unpack("B", f.read(1))[0]
                        normalZ_695 = unpack("<h", f.read(2))[0]
                        vx696 = unpack("<f", f.read(4))[0]
                        vy696 = unpack("<f", f.read(4))[0]
                        vz696 = unpack("<f", f.read(4))[0]
                        type696 = unpack("B", f.read(1))[0]
                        value1a696 = unpack("B", f.read(1))[0]
                        normalZ_696 = unpack("<h", f.read(2))[0]
                        vx697 = unpack("<f", f.read(4))[0]
                        vy697 = unpack("<f", f.read(4))[0]
                        vz697 = unpack("<f", f.read(4))[0]
                        type697 = unpack("B", f.read(1))[0]
                        value1a697 = unpack("B", f.read(1))[0]
                        normalZ_697 = unpack("<h", f.read(2))[0]
                        vx698 = unpack("<f", f.read(4))[0]
                        vy698 = unpack("<f", f.read(4))[0]
                        vz698 = unpack("<f", f.read(4))[0]
                        type698 = unpack("B", f.read(1))[0]
                        value1a698 = unpack("B", f.read(1))[0]
                        normalZ_698 = unpack("<h", f.read(2))[0]
                        vx699 = unpack("<f", f.read(4))[0]
                        vy699 = unpack("<f", f.read(4))[0]
                        vz699 = unpack("<f", f.read(4))[0]
                        type699 = unpack("B", f.read(1))[0]
                        value1a699 = unpack("B", f.read(1))[0]
                        normalZ_699 = unpack("<h", f.read(2))[0]
                        vertices.append([vx663,vz663,vy663])
                        vertices.append([vx664,vz664,vy664])
                        vertices.append([vx665,vz665,vy665])
                        vertices.append([vx666,vz666,vy666])
                        vertices.append([vx667,vz667,vy667])
                        vertices.append([vx668,vz668,vy668])
                        vertices.append([vx669,vz669,vy669])
                        vertices.append([vx670,vz670,vy670])
                        vertices.append([vx671,vz671,vy671])
                        vertices.append([vx672,vz672,vy672])
                        vertices.append([vx673,vz673,vy673])
                        vertices.append([vx674,vz674,vy674])
                        vertices.append([vx675,vz675,vy675])
                        vertices.append([vx676,vz676,vy676])
                        vertices.append([vx677,vz677,vy677])
                        vertices.append([vx678,vz678,vy678])
                        vertices.append([vx679,vz679,vy679])
                        vertices.append([vx680,vz680,vy680])
                        vertices.append([vx681,vz681,vy681])
                        vertices.append([vx682,vz682,vy682])
                        vertices.append([vx683,vz683,vy683])
                        vertices.append([vx684,vz684,vy684])
                        vertices.append([vx685,vz685,vy685])
                        vertices.append([vx686,vz686,vy686])
                        vertices.append([vx687,vz687,vy687])
                        vertices.append([vx688,vz688,vy688])
                        vertices.append([vx689,vz689,vy689])
                        vertices.append([vx690,vz690,vy690])
                        vertices.append([vx691,vz691,vy691])
                        vertices.append([vx692,vz692,vy692])
                        vertices.append([vx693,vz693,vy693])
                        vertices.append([vx694,vz694,vy694])
                        vertices.append([vx695,vz695,vy695])
                        vertices.append([vx696,vz696,vy696])
                        vertices.append([vx697,vz697,vy697])
                        vertices.append([vx698,vz698,vy698])
                        vertices.append([vx699,vz699,vy699])


                elif vertexCount == 38:
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
                        vx700 = unpack("<f", f.read(4))[0]
                        vy700 = unpack("<f", f.read(4))[0]
                        vz700 = unpack("<f", f.read(4))[0]
                        type700 = unpack("B", f.read(1))[0]
                        value1a700 = unpack("B", f.read(1))[0]
                        normalZ_700 = unpack("<h", f.read(2))[0]
                        vx701 = unpack("<f", f.read(4))[0]
                        vy701 = unpack("<f", f.read(4))[0]
                        vz701 = unpack("<f", f.read(4))[0]
                        type701 = unpack("B", f.read(1))[0]
                        value1a701 = unpack("B", f.read(1))[0]
                        normalZ_701 = unpack("<h", f.read(2))[0]
                        vx702 = unpack("<f", f.read(4))[0]
                        vy702 = unpack("<f", f.read(4))[0]
                        vz702 = unpack("<f", f.read(4))[0]
                        type702 = unpack("B", f.read(1))[0]
                        value1a702 = unpack("B", f.read(1))[0]
                        normalZ_702 = unpack("<h", f.read(2))[0]
                        vx703 = unpack("<f", f.read(4))[0]
                        vy703 = unpack("<f", f.read(4))[0]
                        vz703 = unpack("<f", f.read(4))[0]
                        type703 = unpack("B", f.read(1))[0]
                        value1a703 = unpack("B", f.read(1))[0]
                        normalZ_703 = unpack("<h", f.read(2))[0]
                        vx704 = unpack("<f", f.read(4))[0]
                        vy704 = unpack("<f", f.read(4))[0]
                        vz704 = unpack("<f", f.read(4))[0]
                        type704 = unpack("B", f.read(1))[0]
                        value1a704 = unpack("B", f.read(1))[0]
                        normalZ_704 = unpack("<h", f.read(2))[0]
                        vx705 = unpack("<f", f.read(4))[0]
                        vy705 = unpack("<f", f.read(4))[0]
                        vz705 = unpack("<f", f.read(4))[0]
                        type705 = unpack("B", f.read(1))[0]
                        value1a705 = unpack("B", f.read(1))[0]
                        normalZ_705 = unpack("<h", f.read(2))[0]
                        vx706 = unpack("<f", f.read(4))[0]
                        vy706 = unpack("<f", f.read(4))[0]
                        vz706 = unpack("<f", f.read(4))[0]
                        type706 = unpack("B", f.read(1))[0]
                        value1a706 = unpack("B", f.read(1))[0]
                        normalZ_706 = unpack("<h", f.read(2))[0]
                        vx707 = unpack("<f", f.read(4))[0]
                        vy707 = unpack("<f", f.read(4))[0]
                        vz707 = unpack("<f", f.read(4))[0]
                        type707 = unpack("B", f.read(1))[0]
                        value1a707 = unpack("B", f.read(1))[0]
                        normalZ_707 = unpack("<h", f.read(2))[0]
                        vx708 = unpack("<f", f.read(4))[0]
                        vy708 = unpack("<f", f.read(4))[0]
                        vz708 = unpack("<f", f.read(4))[0]
                        type708 = unpack("B", f.read(1))[0]
                        value1a708 = unpack("B", f.read(1))[0]
                        normalZ_708 = unpack("<h", f.read(2))[0]
                        vx709 = unpack("<f", f.read(4))[0]
                        vy709 = unpack("<f", f.read(4))[0]
                        vz709 = unpack("<f", f.read(4))[0]
                        type709 = unpack("B", f.read(1))[0]
                        value1a709 = unpack("B", f.read(1))[0]
                        normalZ_709 = unpack("<h", f.read(2))[0]
                        vx710 = unpack("<f", f.read(4))[0]
                        vy710 = unpack("<f", f.read(4))[0]
                        vz710 = unpack("<f", f.read(4))[0]
                        type710 = unpack("B", f.read(1))[0]
                        value1a710 = unpack("B", f.read(1))[0]
                        normalZ_710 = unpack("<h", f.read(2))[0]
                        vx711 = unpack("<f", f.read(4))[0]
                        vy711 = unpack("<f", f.read(4))[0]
                        vz711 = unpack("<f", f.read(4))[0]
                        type711 = unpack("B", f.read(1))[0]
                        value1a711 = unpack("B", f.read(1))[0]
                        normalZ_711 = unpack("<h", f.read(2))[0]
                        vx712 = unpack("<f", f.read(4))[0]
                        vy712 = unpack("<f", f.read(4))[0]
                        vz712 = unpack("<f", f.read(4))[0]
                        type712 = unpack("B", f.read(1))[0]
                        value1a712 = unpack("B", f.read(1))[0]
                        normalZ_712 = unpack("<h", f.read(2))[0]
                        vx713 = unpack("<f", f.read(4))[0]
                        vy713 = unpack("<f", f.read(4))[0]
                        vz713 = unpack("<f", f.read(4))[0]
                        type713 = unpack("B", f.read(1))[0]
                        value1a713 = unpack("B", f.read(1))[0]
                        normalZ_713 = unpack("<h", f.read(2))[0]
                        vx714 = unpack("<f", f.read(4))[0]
                        vy714 = unpack("<f", f.read(4))[0]
                        vz714 = unpack("<f", f.read(4))[0]
                        type714 = unpack("B", f.read(1))[0]
                        value1a714 = unpack("B", f.read(1))[0]
                        normalZ_714 = unpack("<h", f.read(2))[0]
                        vx715 = unpack("<f", f.read(4))[0]
                        vy715 = unpack("<f", f.read(4))[0]
                        vz715 = unpack("<f", f.read(4))[0]
                        type715 = unpack("B", f.read(1))[0]
                        value1a715 = unpack("B", f.read(1))[0]
                        normalZ_715 = unpack("<h", f.read(2))[0]
                        vx716 = unpack("<f", f.read(4))[0]
                        vy716 = unpack("<f", f.read(4))[0]
                        vz716 = unpack("<f", f.read(4))[0]
                        type716 = unpack("B", f.read(1))[0]
                        value1a716 = unpack("B", f.read(1))[0]
                        normalZ_716 = unpack("<h", f.read(2))[0]
                        vx717 = unpack("<f", f.read(4))[0]
                        vy717 = unpack("<f", f.read(4))[0]
                        vz717 = unpack("<f", f.read(4))[0]
                        type717 = unpack("B", f.read(1))[0]
                        value1a717 = unpack("B", f.read(1))[0]
                        normalZ_717 = unpack("<h", f.read(2))[0]
                        vx718 = unpack("<f", f.read(4))[0]
                        vy718 = unpack("<f", f.read(4))[0]
                        vz718 = unpack("<f", f.read(4))[0]
                        type718 = unpack("B", f.read(1))[0]
                        value1a718 = unpack("B", f.read(1))[0]
                        normalZ_718 = unpack("<h", f.read(2))[0]
                        vx719 = unpack("<f", f.read(4))[0]
                        vy719 = unpack("<f", f.read(4))[0]
                        vz719 = unpack("<f", f.read(4))[0]
                        type719 = unpack("B", f.read(1))[0]
                        value1a719 = unpack("B", f.read(1))[0]
                        normalZ_719 = unpack("<h", f.read(2))[0]
                        vx720 = unpack("<f", f.read(4))[0]
                        vy720 = unpack("<f", f.read(4))[0]
                        vz720 = unpack("<f", f.read(4))[0]
                        type720 = unpack("B", f.read(1))[0]
                        value1a720 = unpack("B", f.read(1))[0]
                        normalZ_720 = unpack("<h", f.read(2))[0]
                        vx721 = unpack("<f", f.read(4))[0]
                        vy721 = unpack("<f", f.read(4))[0]
                        vz721 = unpack("<f", f.read(4))[0]
                        type721 = unpack("B", f.read(1))[0]
                        value1a721 = unpack("B", f.read(1))[0]
                        normalZ_721 = unpack("<h", f.read(2))[0]
                        vx722 = unpack("<f", f.read(4))[0]
                        vy722 = unpack("<f", f.read(4))[0]
                        vz722 = unpack("<f", f.read(4))[0]
                        type722 = unpack("B", f.read(1))[0]
                        value1a722 = unpack("B", f.read(1))[0]
                        normalZ_722 = unpack("<h", f.read(2))[0]
                        vx723 = unpack("<f", f.read(4))[0]
                        vy723 = unpack("<f", f.read(4))[0]
                        vz723 = unpack("<f", f.read(4))[0]
                        type723 = unpack("B", f.read(1))[0]
                        value1a723 = unpack("B", f.read(1))[0]
                        normalZ_723 = unpack("<h", f.read(2))[0]
                        vx724 = unpack("<f", f.read(4))[0]
                        vy724 = unpack("<f", f.read(4))[0]
                        vz724 = unpack("<f", f.read(4))[0]
                        type724 = unpack("B", f.read(1))[0]
                        value1a724 = unpack("B", f.read(1))[0]
                        normalZ_724 = unpack("<h", f.read(2))[0]
                        vx725 = unpack("<f", f.read(4))[0]
                        vy725 = unpack("<f", f.read(4))[0]
                        vz725 = unpack("<f", f.read(4))[0]
                        type725 = unpack("B", f.read(1))[0]
                        value1a725 = unpack("B", f.read(1))[0]
                        normalZ_725 = unpack("<h", f.read(2))[0]
                        vx726 = unpack("<f", f.read(4))[0]
                        vy726 = unpack("<f", f.read(4))[0]
                        vz726 = unpack("<f", f.read(4))[0]
                        type726 = unpack("B", f.read(1))[0]
                        value1a726 = unpack("B", f.read(1))[0]
                        normalZ_726 = unpack("<h", f.read(2))[0]
                        vx727 = unpack("<f", f.read(4))[0]
                        vy727 = unpack("<f", f.read(4))[0]
                        vz727 = unpack("<f", f.read(4))[0]
                        type727 = unpack("B", f.read(1))[0]
                        value1a727 = unpack("B", f.read(1))[0]
                        normalZ_727 = unpack("<h", f.read(2))[0]
                        vx728 = unpack("<f", f.read(4))[0]
                        vy728 = unpack("<f", f.read(4))[0]
                        vz728 = unpack("<f", f.read(4))[0]
                        type728 = unpack("B", f.read(1))[0]
                        value1a728 = unpack("B", f.read(1))[0]
                        normalZ_728 = unpack("<h", f.read(2))[0]
                        vx729 = unpack("<f", f.read(4))[0]
                        vy729 = unpack("<f", f.read(4))[0]
                        vz729 = unpack("<f", f.read(4))[0]
                        type729 = unpack("B", f.read(1))[0]
                        value1a729 = unpack("B", f.read(1))[0]
                        normalZ_729 = unpack("<h", f.read(2))[0]
                        vx730 = unpack("<f", f.read(4))[0]
                        vy730 = unpack("<f", f.read(4))[0]
                        vz730 = unpack("<f", f.read(4))[0]
                        type730 = unpack("B", f.read(1))[0]
                        value1a730 = unpack("B", f.read(1))[0]
                        normalZ_730 = unpack("<h", f.read(2))[0]
                        vx731 = unpack("<f", f.read(4))[0]
                        vy731 = unpack("<f", f.read(4))[0]
                        vz731 = unpack("<f", f.read(4))[0]
                        type731 = unpack("B", f.read(1))[0]
                        value1a731 = unpack("B", f.read(1))[0]
                        normalZ_731 = unpack("<h", f.read(2))[0]
                        vx732 = unpack("<f", f.read(4))[0]
                        vy732 = unpack("<f", f.read(4))[0]
                        vz732 = unpack("<f", f.read(4))[0]
                        type732 = unpack("B", f.read(1))[0]
                        value1a732 = unpack("B", f.read(1))[0]
                        normalZ_732 = unpack("<h", f.read(2))[0]
                        vx733 = unpack("<f", f.read(4))[0]
                        vy733 = unpack("<f", f.read(4))[0]
                        vz733 = unpack("<f", f.read(4))[0]
                        type733 = unpack("B", f.read(1))[0]
                        value1a733 = unpack("B", f.read(1))[0]
                        normalZ_733 = unpack("<h", f.read(2))[0]
                        vx734 = unpack("<f", f.read(4))[0]
                        vy734 = unpack("<f", f.read(4))[0]
                        vz734 = unpack("<f", f.read(4))[0]
                        type734 = unpack("B", f.read(1))[0]
                        value1a734 = unpack("B", f.read(1))[0]
                        normalZ_734 = unpack("<h", f.read(2))[0]
                        vx735 = unpack("<f", f.read(4))[0]
                        vy735 = unpack("<f", f.read(4))[0]
                        vz735 = unpack("<f", f.read(4))[0]
                        type735 = unpack("B", f.read(1))[0]
                        value1a735 = unpack("B", f.read(1))[0]
                        normalZ_735 = unpack("<h", f.read(2))[0]
                        vx736 = unpack("<f", f.read(4))[0]
                        vy736 = unpack("<f", f.read(4))[0]
                        vz736 = unpack("<f", f.read(4))[0]
                        type736 = unpack("B", f.read(1))[0]
                        value1a736 = unpack("B", f.read(1))[0]
                        normalZ_736 = unpack("<h", f.read(2))[0]
                        vx737 = unpack("<f", f.read(4))[0]
                        vy737 = unpack("<f", f.read(4))[0]
                        vz737 = unpack("<f", f.read(4))[0]
                        type737 = unpack("B", f.read(1))[0]
                        value1a737 = unpack("B", f.read(1))[0]
                        normalZ_737 = unpack("<h", f.read(2))[0]
                        vertices.append([vx700,vz700,vy700])
                        vertices.append([vx701,vz701,vy701])
                        vertices.append([vx702,vz702,vy702])
                        vertices.append([vx703,vz703,vy703])
                        vertices.append([vx704,vz704,vy704])
                        vertices.append([vx705,vz705,vy705])
                        vertices.append([vx706,vz706,vy706])
                        vertices.append([vx707,vz707,vy707])
                        vertices.append([vx708,vz708,vy708])
                        vertices.append([vx709,vz709,vy709])
                        vertices.append([vx710,vz710,vy710])
                        vertices.append([vx711,vz711,vy711])
                        vertices.append([vx712,vz712,vy712])
                        vertices.append([vx713,vz713,vy713])
                        vertices.append([vx714,vz714,vy714])
                        vertices.append([vx715,vz715,vy715])
                        vertices.append([vx716,vz716,vy716])
                        vertices.append([vx717,vz717,vy717])
                        vertices.append([vx718,vz718,vy718])
                        vertices.append([vx719,vz719,vy719])
                        vertices.append([vx720,vz720,vy720])
                        vertices.append([vx721,vz721,vy721])
                        vertices.append([vx722,vz722,vy722])
                        vertices.append([vx723,vz723,vy723])
                        vertices.append([vx724,vz724,vy724])
                        vertices.append([vx725,vz725,vy725])
                        vertices.append([vx726,vz726,vy726])
                        vertices.append([vx727,vz727,vy727])
                        vertices.append([vx728,vz728,vy728])
                        vertices.append([vx729,vz729,vy729])
                        vertices.append([vx730,vz730,vy730])
                        vertices.append([vx731,vz731,vy731])
                        vertices.append([vx732,vz732,vy732])
                        vertices.append([vx733,vz733,vy733])
                        vertices.append([vx734,vz734,vy734])
                        vertices.append([vx735,vz735,vy735])
                        vertices.append([vx736,vz736,vy736])
                        vertices.append([vx737,vz737,vy737])

                elif vertexCount == 39:
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
                        vx738 = unpack("<f", f.read(4))[0]
                        vy738 = unpack("<f", f.read(4))[0]
                        vz738 = unpack("<f", f.read(4))[0]
                        type738 = unpack("B", f.read(1))[0]
                        value1a738 = unpack("B", f.read(1))[0]
                        normalZ_738 = unpack("<h", f.read(2))[0]
                        vx739 = unpack("<f", f.read(4))[0]
                        vy739 = unpack("<f", f.read(4))[0]
                        vz739 = unpack("<f", f.read(4))[0]
                        type739 = unpack("B", f.read(1))[0]
                        value1a739 = unpack("B", f.read(1))[0]
                        normalZ_739 = unpack("<h", f.read(2))[0]
                        vx740 = unpack("<f", f.read(4))[0]
                        vy740 = unpack("<f", f.read(4))[0]
                        vz740 = unpack("<f", f.read(4))[0]
                        type740 = unpack("B", f.read(1))[0]
                        value1a740 = unpack("B", f.read(1))[0]
                        normalZ_740 = unpack("<h", f.read(2))[0]
                        vx741 = unpack("<f", f.read(4))[0]
                        vy741 = unpack("<f", f.read(4))[0]
                        vz741 = unpack("<f", f.read(4))[0]
                        type741 = unpack("B", f.read(1))[0]
                        value1a741 = unpack("B", f.read(1))[0]
                        normalZ_741 = unpack("<h", f.read(2))[0]
                        vx742 = unpack("<f", f.read(4))[0]
                        vy742 = unpack("<f", f.read(4))[0]
                        vz742 = unpack("<f", f.read(4))[0]
                        type742 = unpack("B", f.read(1))[0]
                        value1a742 = unpack("B", f.read(1))[0]
                        normalZ_742 = unpack("<h", f.read(2))[0]
                        vx743 = unpack("<f", f.read(4))[0]
                        vy743 = unpack("<f", f.read(4))[0]
                        vz743 = unpack("<f", f.read(4))[0]
                        type743 = unpack("B", f.read(1))[0]
                        value1a743 = unpack("B", f.read(1))[0]
                        normalZ_743 = unpack("<h", f.read(2))[0]
                        vx744 = unpack("<f", f.read(4))[0]
                        vy744 = unpack("<f", f.read(4))[0]
                        vz744 = unpack("<f", f.read(4))[0]
                        type744 = unpack("B", f.read(1))[0]
                        value1a744 = unpack("B", f.read(1))[0]
                        normalZ_744 = unpack("<h", f.read(2))[0]
                        vx745 = unpack("<f", f.read(4))[0]
                        vy745 = unpack("<f", f.read(4))[0]
                        vz745 = unpack("<f", f.read(4))[0]
                        type745 = unpack("B", f.read(1))[0]
                        value1a745 = unpack("B", f.read(1))[0]
                        normalZ_745 = unpack("<h", f.read(2))[0]
                        vx746 = unpack("<f", f.read(4))[0]
                        vy746 = unpack("<f", f.read(4))[0]
                        vz746 = unpack("<f", f.read(4))[0]
                        type746 = unpack("B", f.read(1))[0]
                        value1a746 = unpack("B", f.read(1))[0]
                        normalZ_746 = unpack("<h", f.read(2))[0]
                        vx747 = unpack("<f", f.read(4))[0]
                        vy747 = unpack("<f", f.read(4))[0]
                        vz747 = unpack("<f", f.read(4))[0]
                        type747 = unpack("B", f.read(1))[0]
                        value1a747 = unpack("B", f.read(1))[0]
                        normalZ_747 = unpack("<h", f.read(2))[0]
                        vx748 = unpack("<f", f.read(4))[0]
                        vy748 = unpack("<f", f.read(4))[0]
                        vz748 = unpack("<f", f.read(4))[0]
                        type748 = unpack("B", f.read(1))[0]
                        value1a748 = unpack("B", f.read(1))[0]
                        normalZ_748 = unpack("<h", f.read(2))[0]
                        vx749 = unpack("<f", f.read(4))[0]
                        vy749 = unpack("<f", f.read(4))[0]
                        vz749 = unpack("<f", f.read(4))[0]
                        type749 = unpack("B", f.read(1))[0]
                        value1a749 = unpack("B", f.read(1))[0]
                        normalZ_749 = unpack("<h", f.read(2))[0]
                        vx750 = unpack("<f", f.read(4))[0]
                        vy750 = unpack("<f", f.read(4))[0]
                        vz750 = unpack("<f", f.read(4))[0]
                        type750 = unpack("B", f.read(1))[0]
                        value1a750 = unpack("B", f.read(1))[0]
                        normalZ_750 = unpack("<h", f.read(2))[0]
                        vx751 = unpack("<f", f.read(4))[0]
                        vy751 = unpack("<f", f.read(4))[0]
                        vz751 = unpack("<f", f.read(4))[0]
                        type751 = unpack("B", f.read(1))[0]
                        value1a751 = unpack("B", f.read(1))[0]
                        normalZ_751 = unpack("<h", f.read(2))[0]
                        vx752 = unpack("<f", f.read(4))[0]
                        vy752 = unpack("<f", f.read(4))[0]
                        vz752 = unpack("<f", f.read(4))[0]
                        type752 = unpack("B", f.read(1))[0]
                        value1a752 = unpack("B", f.read(1))[0]
                        normalZ_752 = unpack("<h", f.read(2))[0]
                        vx753 = unpack("<f", f.read(4))[0]
                        vy753 = unpack("<f", f.read(4))[0]
                        vz753 = unpack("<f", f.read(4))[0]
                        type753 = unpack("B", f.read(1))[0]
                        value1a753 = unpack("B", f.read(1))[0]
                        normalZ_753 = unpack("<h", f.read(2))[0]
                        vx754 = unpack("<f", f.read(4))[0]
                        vy754 = unpack("<f", f.read(4))[0]
                        vz754 = unpack("<f", f.read(4))[0]
                        type754 = unpack("B", f.read(1))[0]
                        value1a754 = unpack("B", f.read(1))[0]
                        normalZ_754 = unpack("<h", f.read(2))[0]
                        vx755 = unpack("<f", f.read(4))[0]
                        vy755 = unpack("<f", f.read(4))[0]
                        vz755 = unpack("<f", f.read(4))[0]
                        type755 = unpack("B", f.read(1))[0]
                        value1a755 = unpack("B", f.read(1))[0]
                        normalZ_755 = unpack("<h", f.read(2))[0]
                        vx756 = unpack("<f", f.read(4))[0]
                        vy756 = unpack("<f", f.read(4))[0]
                        vz756 = unpack("<f", f.read(4))[0]
                        type756 = unpack("B", f.read(1))[0]
                        value1a756 = unpack("B", f.read(1))[0]
                        normalZ_756 = unpack("<h", f.read(2))[0]
                        vx757 = unpack("<f", f.read(4))[0]
                        vy757 = unpack("<f", f.read(4))[0]
                        vz757 = unpack("<f", f.read(4))[0]
                        type757 = unpack("B", f.read(1))[0]
                        value1a757 = unpack("B", f.read(1))[0]
                        normalZ_757 = unpack("<h", f.read(2))[0]
                        vx758 = unpack("<f", f.read(4))[0]
                        vy758 = unpack("<f", f.read(4))[0]
                        vz758 = unpack("<f", f.read(4))[0]
                        type758 = unpack("B", f.read(1))[0]
                        value1a758 = unpack("B", f.read(1))[0]
                        normalZ_758 = unpack("<h", f.read(2))[0]
                        vx759 = unpack("<f", f.read(4))[0]
                        vy759 = unpack("<f", f.read(4))[0]
                        vz759 = unpack("<f", f.read(4))[0]
                        type759 = unpack("B", f.read(1))[0]
                        value1a759 = unpack("B", f.read(1))[0]
                        normalZ_759 = unpack("<h", f.read(2))[0]
                        vx760 = unpack("<f", f.read(4))[0]
                        vy760 = unpack("<f", f.read(4))[0]
                        vz760 = unpack("<f", f.read(4))[0]
                        type760 = unpack("B", f.read(1))[0]
                        value1a760 = unpack("B", f.read(1))[0]
                        normalZ_760 = unpack("<h", f.read(2))[0]
                        vx761 = unpack("<f", f.read(4))[0]
                        vy761 = unpack("<f", f.read(4))[0]
                        vz761 = unpack("<f", f.read(4))[0]
                        type761 = unpack("B", f.read(1))[0]
                        value1a761 = unpack("B", f.read(1))[0]
                        normalZ_761 = unpack("<h", f.read(2))[0]
                        vx762 = unpack("<f", f.read(4))[0]
                        vy762 = unpack("<f", f.read(4))[0]
                        vz762 = unpack("<f", f.read(4))[0]
                        type762 = unpack("B", f.read(1))[0]
                        value1a762 = unpack("B", f.read(1))[0]
                        normalZ_762 = unpack("<h", f.read(2))[0]
                        vx763 = unpack("<f", f.read(4))[0]
                        vy763 = unpack("<f", f.read(4))[0]
                        vz763 = unpack("<f", f.read(4))[0]
                        type763 = unpack("B", f.read(1))[0]
                        value1a763 = unpack("B", f.read(1))[0]
                        normalZ_763 = unpack("<h", f.read(2))[0]
                        vx764 = unpack("<f", f.read(4))[0]
                        vy764 = unpack("<f", f.read(4))[0]
                        vz764 = unpack("<f", f.read(4))[0]
                        type764 = unpack("B", f.read(1))[0]
                        value1a764 = unpack("B", f.read(1))[0]
                        normalZ_764 = unpack("<h", f.read(2))[0]
                        vx765 = unpack("<f", f.read(4))[0]
                        vy765 = unpack("<f", f.read(4))[0]
                        vz765 = unpack("<f", f.read(4))[0]
                        type765 = unpack("B", f.read(1))[0]
                        value1a765 = unpack("B", f.read(1))[0]
                        normalZ_765 = unpack("<h", f.read(2))[0]
                        vx766 = unpack("<f", f.read(4))[0]
                        vy766 = unpack("<f", f.read(4))[0]
                        vz766 = unpack("<f", f.read(4))[0]
                        type766 = unpack("B", f.read(1))[0]
                        value1a766 = unpack("B", f.read(1))[0]
                        normalZ_766 = unpack("<h", f.read(2))[0]
                        vx767 = unpack("<f", f.read(4))[0]
                        vy767 = unpack("<f", f.read(4))[0]
                        vz767 = unpack("<f", f.read(4))[0]
                        type767 = unpack("B", f.read(1))[0]
                        value1a767 = unpack("B", f.read(1))[0]
                        normalZ_767 = unpack("<h", f.read(2))[0]
                        vx768 = unpack("<f", f.read(4))[0]
                        vy768 = unpack("<f", f.read(4))[0]
                        vz768 = unpack("<f", f.read(4))[0]
                        type768 = unpack("B", f.read(1))[0]
                        value1a768 = unpack("B", f.read(1))[0]
                        normalZ_768 = unpack("<h", f.read(2))[0]
                        vx769 = unpack("<f", f.read(4))[0]
                        vy769 = unpack("<f", f.read(4))[0]
                        vz769 = unpack("<f", f.read(4))[0]
                        type769 = unpack("B", f.read(1))[0]
                        value1a769 = unpack("B", f.read(1))[0]
                        normalZ_769 = unpack("<h", f.read(2))[0]
                        vx770 = unpack("<f", f.read(4))[0]
                        vy770 = unpack("<f", f.read(4))[0]
                        vz770 = unpack("<f", f.read(4))[0]
                        type770 = unpack("B", f.read(1))[0]
                        value1a770 = unpack("B", f.read(1))[0]
                        normalZ_770 = unpack("<h", f.read(2))[0]
                        vx771 = unpack("<f", f.read(4))[0]
                        vy771 = unpack("<f", f.read(4))[0]
                        vz771 = unpack("<f", f.read(4))[0]
                        type771 = unpack("B", f.read(1))[0]
                        value1a771 = unpack("B", f.read(1))[0]
                        normalZ_771 = unpack("<h", f.read(2))[0]
                        vx772 = unpack("<f", f.read(4))[0]
                        vy772 = unpack("<f", f.read(4))[0]
                        vz772 = unpack("<f", f.read(4))[0]
                        type772 = unpack("B", f.read(1))[0]
                        value1a772 = unpack("B", f.read(1))[0]
                        normalZ_772 = unpack("<h", f.read(2))[0]
                        vx773 = unpack("<f", f.read(4))[0]
                        vy773 = unpack("<f", f.read(4))[0]
                        vz773 = unpack("<f", f.read(4))[0]
                        type773 = unpack("B", f.read(1))[0]
                        value1a773 = unpack("B", f.read(1))[0]
                        normalZ_773 = unpack("<h", f.read(2))[0]
                        vx774 = unpack("<f", f.read(4))[0]
                        vy774 = unpack("<f", f.read(4))[0]
                        vz774 = unpack("<f", f.read(4))[0]
                        type774 = unpack("B", f.read(1))[0]
                        value1a774 = unpack("B", f.read(1))[0]
                        normalZ_774 = unpack("<h", f.read(2))[0]
                        vx775 = unpack("<f", f.read(4))[0]
                        vy775 = unpack("<f", f.read(4))[0]
                        vz775 = unpack("<f", f.read(4))[0]
                        type775 = unpack("B", f.read(1))[0]
                        value1a775 = unpack("B", f.read(1))[0]
                        normalZ_775 = unpack("<h", f.read(2))[0]
                        vx776 = unpack("<f", f.read(4))[0]
                        vy776 = unpack("<f", f.read(4))[0]
                        vz776 = unpack("<f", f.read(4))[0]
                        type776 = unpack("B", f.read(1))[0]
                        value1a776 = unpack("B", f.read(1))[0]
                        normalZ_776 = unpack("<h", f.read(2))[0]
                        vertices.append([vx738,vz738,vy738])
                        vertices.append([vx739,vz739,vy739])
                        vertices.append([vx740,vz740,vy740])
                        vertices.append([vx741,vz741,vy741])
                        vertices.append([vx742,vz742,vy742])
                        vertices.append([vx743,vz743,vy743])
                        vertices.append([vx744,vz744,vy744])
                        vertices.append([vx745,vz745,vy745])
                        vertices.append([vx746,vz746,vy746])
                        vertices.append([vx747,vz747,vy747])
                        vertices.append([vx748,vz748,vy748])
                        vertices.append([vx749,vz749,vy749])
                        vertices.append([vx750,vz750,vy750])
                        vertices.append([vx751,vz751,vy751])
                        vertices.append([vx752,vz752,vy752])
                        vertices.append([vx753,vz753,vy753])
                        vertices.append([vx754,vz754,vy754])
                        vertices.append([vx755,vz755,vy755])
                        vertices.append([vx756,vz756,vy756])
                        vertices.append([vx757,vz757,vy757])
                        vertices.append([vx758,vz758,vy758])
                        vertices.append([vx759,vz759,vy759])
                        vertices.append([vx760,vz760,vy760])
                        vertices.append([vx761,vz761,vy761])
                        vertices.append([vx762,vz762,vy762])
                        vertices.append([vx763,vz763,vy763])
                        vertices.append([vx764,vz764,vy764])
                        vertices.append([vx765,vz765,vy765])
                        vertices.append([vx766,vz766,vy766])
                        vertices.append([vx767,vz767,vy767])
                        vertices.append([vx768,vz768,vy768])
                        vertices.append([vx769,vz769,vy769])
                        vertices.append([vx770,vz770,vy770])
                        vertices.append([vx771,vz771,vy771])
                        vertices.append([vx772,vz772,vy772])
                        vertices.append([vx773,vz773,vy773])
                        vertices.append([vx774,vz774,vy774])
                        vertices.append([vx775,vz775,vy775])
                        vertices.append([vx776,vz776,vy776])

                elif vertexCount == 40:
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
                        vx777 = unpack("<f", f.read(4))[0]
                        vy777 = unpack("<f", f.read(4))[0]
                        vz777 = unpack("<f", f.read(4))[0]
                        type777 = unpack("B", f.read(1))[0]
                        value1a777 = unpack("B", f.read(1))[0]
                        normalZ_777 = unpack("<h", f.read(2))[0]
                        vx778 = unpack("<f", f.read(4))[0]
                        vy778 = unpack("<f", f.read(4))[0]
                        vz778 = unpack("<f", f.read(4))[0]
                        type778 = unpack("B", f.read(1))[0]
                        value1a778 = unpack("B", f.read(1))[0]
                        normalZ_778 = unpack("<h", f.read(2))[0]
                        vx779 = unpack("<f", f.read(4))[0]
                        vy779 = unpack("<f", f.read(4))[0]
                        vz779 = unpack("<f", f.read(4))[0]
                        type779 = unpack("B", f.read(1))[0]
                        value1a779 = unpack("B", f.read(1))[0]
                        normalZ_779 = unpack("<h", f.read(2))[0]
                        vx780 = unpack("<f", f.read(4))[0]
                        vy780 = unpack("<f", f.read(4))[0]
                        vz780 = unpack("<f", f.read(4))[0]
                        type780 = unpack("B", f.read(1))[0]
                        value1a780 = unpack("B", f.read(1))[0]
                        normalZ_780 = unpack("<h", f.read(2))[0]
                        vx781 = unpack("<f", f.read(4))[0]
                        vy781 = unpack("<f", f.read(4))[0]
                        vz781 = unpack("<f", f.read(4))[0]
                        type781 = unpack("B", f.read(1))[0]
                        value1a781 = unpack("B", f.read(1))[0]
                        normalZ_781 = unpack("<h", f.read(2))[0]
                        vx782 = unpack("<f", f.read(4))[0]
                        vy782 = unpack("<f", f.read(4))[0]
                        vz782 = unpack("<f", f.read(4))[0]
                        type782 = unpack("B", f.read(1))[0]
                        value1a782 = unpack("B", f.read(1))[0]
                        normalZ_782 = unpack("<h", f.read(2))[0]
                        vx783 = unpack("<f", f.read(4))[0]
                        vy783 = unpack("<f", f.read(4))[0]
                        vz783 = unpack("<f", f.read(4))[0]
                        type783 = unpack("B", f.read(1))[0]
                        value1a783 = unpack("B", f.read(1))[0]
                        normalZ_783 = unpack("<h", f.read(2))[0]
                        vx784 = unpack("<f", f.read(4))[0]
                        vy784 = unpack("<f", f.read(4))[0]
                        vz784 = unpack("<f", f.read(4))[0]
                        type784 = unpack("B", f.read(1))[0]
                        value1a784 = unpack("B", f.read(1))[0]
                        normalZ_784 = unpack("<h", f.read(2))[0]
                        vx785 = unpack("<f", f.read(4))[0]
                        vy785 = unpack("<f", f.read(4))[0]
                        vz785 = unpack("<f", f.read(4))[0]
                        type785 = unpack("B", f.read(1))[0]
                        value1a785 = unpack("B", f.read(1))[0]
                        normalZ_785 = unpack("<h", f.read(2))[0]
                        vx786 = unpack("<f", f.read(4))[0]
                        vy786 = unpack("<f", f.read(4))[0]
                        vz786 = unpack("<f", f.read(4))[0]
                        type786 = unpack("B", f.read(1))[0]
                        value1a786 = unpack("B", f.read(1))[0]
                        normalZ_786 = unpack("<h", f.read(2))[0]
                        vx787 = unpack("<f", f.read(4))[0]
                        vy787 = unpack("<f", f.read(4))[0]
                        vz787 = unpack("<f", f.read(4))[0]
                        type787 = unpack("B", f.read(1))[0]
                        value1a787 = unpack("B", f.read(1))[0]
                        normalZ_787 = unpack("<h", f.read(2))[0]
                        vx788 = unpack("<f", f.read(4))[0]
                        vy788 = unpack("<f", f.read(4))[0]
                        vz788 = unpack("<f", f.read(4))[0]
                        type788 = unpack("B", f.read(1))[0]
                        value1a788 = unpack("B", f.read(1))[0]
                        normalZ_788 = unpack("<h", f.read(2))[0]
                        vx789 = unpack("<f", f.read(4))[0]
                        vy789 = unpack("<f", f.read(4))[0]
                        vz789 = unpack("<f", f.read(4))[0]
                        type789 = unpack("B", f.read(1))[0]
                        value1a789 = unpack("B", f.read(1))[0]
                        normalZ_789 = unpack("<h", f.read(2))[0]
                        vx790 = unpack("<f", f.read(4))[0]
                        vy790 = unpack("<f", f.read(4))[0]
                        vz790 = unpack("<f", f.read(4))[0]
                        type790 = unpack("B", f.read(1))[0]
                        value1a790 = unpack("B", f.read(1))[0]
                        normalZ_790 = unpack("<h", f.read(2))[0]
                        vx791 = unpack("<f", f.read(4))[0]
                        vy791 = unpack("<f", f.read(4))[0]
                        vz791 = unpack("<f", f.read(4))[0]
                        type791 = unpack("B", f.read(1))[0]
                        value1a791 = unpack("B", f.read(1))[0]
                        normalZ_791 = unpack("<h", f.read(2))[0]
                        vx792 = unpack("<f", f.read(4))[0]
                        vy792 = unpack("<f", f.read(4))[0]
                        vz792 = unpack("<f", f.read(4))[0]
                        type792 = unpack("B", f.read(1))[0]
                        value1a792 = unpack("B", f.read(1))[0]
                        normalZ_792 = unpack("<h", f.read(2))[0]
                        vx793 = unpack("<f", f.read(4))[0]
                        vy793 = unpack("<f", f.read(4))[0]
                        vz793 = unpack("<f", f.read(4))[0]
                        type793 = unpack("B", f.read(1))[0]
                        value1a793 = unpack("B", f.read(1))[0]
                        normalZ_793 = unpack("<h", f.read(2))[0]
                        vx794 = unpack("<f", f.read(4))[0]
                        vy794 = unpack("<f", f.read(4))[0]
                        vz794 = unpack("<f", f.read(4))[0]
                        type794 = unpack("B", f.read(1))[0]
                        value1a794 = unpack("B", f.read(1))[0]
                        normalZ_794 = unpack("<h", f.read(2))[0]
                        vx795 = unpack("<f", f.read(4))[0]
                        vy795 = unpack("<f", f.read(4))[0]
                        vz795 = unpack("<f", f.read(4))[0]
                        type795 = unpack("B", f.read(1))[0]
                        value1a795 = unpack("B", f.read(1))[0]
                        normalZ_795 = unpack("<h", f.read(2))[0]
                        vx796 = unpack("<f", f.read(4))[0]
                        vy796 = unpack("<f", f.read(4))[0]
                        vz796 = unpack("<f", f.read(4))[0]
                        type796 = unpack("B", f.read(1))[0]
                        value1a796 = unpack("B", f.read(1))[0]
                        normalZ_796 = unpack("<h", f.read(2))[0]
                        vx797 = unpack("<f", f.read(4))[0]
                        vy797 = unpack("<f", f.read(4))[0]
                        vz797 = unpack("<f", f.read(4))[0]
                        type797 = unpack("B", f.read(1))[0]
                        value1a797 = unpack("B", f.read(1))[0]
                        normalZ_797 = unpack("<h", f.read(2))[0]
                        vx798 = unpack("<f", f.read(4))[0]
                        vy798 = unpack("<f", f.read(4))[0]
                        vz798 = unpack("<f", f.read(4))[0]
                        type798 = unpack("B", f.read(1))[0]
                        value1a798 = unpack("B", f.read(1))[0]
                        normalZ_798 = unpack("<h", f.read(2))[0]
                        vx799 = unpack("<f", f.read(4))[0]
                        vy799 = unpack("<f", f.read(4))[0]
                        vz799 = unpack("<f", f.read(4))[0]
                        type799 = unpack("B", f.read(1))[0]
                        value1a799 = unpack("B", f.read(1))[0]
                        normalZ_799 = unpack("<h", f.read(2))[0]
                        vx800 = unpack("<f", f.read(4))[0]
                        vy800 = unpack("<f", f.read(4))[0]
                        vz800 = unpack("<f", f.read(4))[0]
                        type800 = unpack("B", f.read(1))[0]
                        value1a800 = unpack("B", f.read(1))[0]
                        normalZ_800 = unpack("<h", f.read(2))[0]
                        vx801 = unpack("<f", f.read(4))[0]
                        vy801 = unpack("<f", f.read(4))[0]
                        vz801 = unpack("<f", f.read(4))[0]
                        type801 = unpack("B", f.read(1))[0]
                        value1a801 = unpack("B", f.read(1))[0]
                        normalZ_801 = unpack("<h", f.read(2))[0]
                        vx802 = unpack("<f", f.read(4))[0]
                        vy802 = unpack("<f", f.read(4))[0]
                        vz802 = unpack("<f", f.read(4))[0]
                        type802 = unpack("B", f.read(1))[0]
                        value1a802 = unpack("B", f.read(1))[0]
                        normalZ_802 = unpack("<h", f.read(2))[0]
                        vx803 = unpack("<f", f.read(4))[0]
                        vy803 = unpack("<f", f.read(4))[0]
                        vz803 = unpack("<f", f.read(4))[0]
                        type803 = unpack("B", f.read(1))[0]
                        value1a803 = unpack("B", f.read(1))[0]
                        normalZ_803 = unpack("<h", f.read(2))[0]
                        vx804 = unpack("<f", f.read(4))[0]
                        vy804 = unpack("<f", f.read(4))[0]
                        vz804 = unpack("<f", f.read(4))[0]
                        type804 = unpack("B", f.read(1))[0]
                        value1a804 = unpack("B", f.read(1))[0]
                        normalZ_804 = unpack("<h", f.read(2))[0]
                        vx805 = unpack("<f", f.read(4))[0]
                        vy805 = unpack("<f", f.read(4))[0]
                        vz805 = unpack("<f", f.read(4))[0]
                        type805 = unpack("B", f.read(1))[0]
                        value1a805 = unpack("B", f.read(1))[0]
                        normalZ_805 = unpack("<h", f.read(2))[0]
                        vx806 = unpack("<f", f.read(4))[0]
                        vy806 = unpack("<f", f.read(4))[0]
                        vz806 = unpack("<f", f.read(4))[0]
                        type806 = unpack("B", f.read(1))[0]
                        value1a806 = unpack("B", f.read(1))[0]
                        normalZ_806 = unpack("<h", f.read(2))[0]
                        vx807 = unpack("<f", f.read(4))[0]
                        vy807 = unpack("<f", f.read(4))[0]
                        vz807 = unpack("<f", f.read(4))[0]
                        type807 = unpack("B", f.read(1))[0]
                        value1a807 = unpack("B", f.read(1))[0]
                        normalZ_807 = unpack("<h", f.read(2))[0]
                        vx808 = unpack("<f", f.read(4))[0]
                        vy808 = unpack("<f", f.read(4))[0]
                        vz808 = unpack("<f", f.read(4))[0]
                        type808 = unpack("B", f.read(1))[0]
                        value1a808 = unpack("B", f.read(1))[0]
                        normalZ_808 = unpack("<h", f.read(2))[0]
                        vx809 = unpack("<f", f.read(4))[0]
                        vy809 = unpack("<f", f.read(4))[0]
                        vz809 = unpack("<f", f.read(4))[0]
                        type809 = unpack("B", f.read(1))[0]
                        value1a809 = unpack("B", f.read(1))[0]
                        normalZ_809 = unpack("<h", f.read(2))[0]
                        vx810 = unpack("<f", f.read(4))[0]
                        vy810 = unpack("<f", f.read(4))[0]
                        vz810 = unpack("<f", f.read(4))[0]
                        type810 = unpack("B", f.read(1))[0]
                        value1a810 = unpack("B", f.read(1))[0]
                        normalZ_810 = unpack("<h", f.read(2))[0]
                        vx811 = unpack("<f", f.read(4))[0]
                        vy811 = unpack("<f", f.read(4))[0]
                        vz811 = unpack("<f", f.read(4))[0]
                        type811 = unpack("B", f.read(1))[0]
                        value1a811 = unpack("B", f.read(1))[0]
                        normalZ_811 = unpack("<h", f.read(2))[0]
                        vx812 = unpack("<f", f.read(4))[0]
                        vy812 = unpack("<f", f.read(4))[0]
                        vz812 = unpack("<f", f.read(4))[0]
                        type812 = unpack("B", f.read(1))[0]
                        value1a812 = unpack("B", f.read(1))[0]
                        normalZ_812 = unpack("<h", f.read(2))[0]
                        vx813 = unpack("<f", f.read(4))[0]
                        vy813 = unpack("<f", f.read(4))[0]
                        vz813 = unpack("<f", f.read(4))[0]
                        type813 = unpack("B", f.read(1))[0]
                        value1a813 = unpack("B", f.read(1))[0]
                        normalZ_813 = unpack("<h", f.read(2))[0]
                        vx814 = unpack("<f", f.read(4))[0]
                        vy814 = unpack("<f", f.read(4))[0]
                        vz814 = unpack("<f", f.read(4))[0]
                        type814 = unpack("B", f.read(1))[0]
                        value1a814 = unpack("B", f.read(1))[0]
                        normalZ_814 = unpack("<h", f.read(2))[0]
                        vx815 = unpack("<f", f.read(4))[0]
                        vy815 = unpack("<f", f.read(4))[0]
                        vz815 = unpack("<f", f.read(4))[0]
                        type815 = unpack("B", f.read(1))[0]
                        value1a815 = unpack("B", f.read(1))[0]
                        normalZ_815 = unpack("<h", f.read(2))[0]
                        vx816 = unpack("<f", f.read(4))[0]
                        vy816 = unpack("<f", f.read(4))[0]
                        vz816 = unpack("<f", f.read(4))[0]
                        type816 = unpack("B", f.read(1))[0]
                        value1a816 = unpack("B", f.read(1))[0]
                        normalZ_816 = unpack("<h", f.read(2))[0]
                        vertices.append([vx777,vz777,vy777])
                        vertices.append([vx778,vz778,vy778])
                        vertices.append([vx779,vz779,vy779])
                        vertices.append([vx780,vz780,vy780])
                        vertices.append([vx781,vz781,vy781])
                        vertices.append([vx782,vz782,vy782])
                        vertices.append([vx783,vz783,vy783])
                        vertices.append([vx784,vz784,vy784])
                        vertices.append([vx785,vz785,vy785])
                        vertices.append([vx786,vz786,vy786])
                        vertices.append([vx787,vz787,vy787])
                        vertices.append([vx788,vz788,vy788])
                        vertices.append([vx789,vz789,vy789])
                        vertices.append([vx790,vz790,vy790])
                        vertices.append([vx791,vz791,vy791])
                        vertices.append([vx792,vz792,vy792])
                        vertices.append([vx793,vz793,vy793])
                        vertices.append([vx794,vz794,vy794])
                        vertices.append([vx795,vz795,vy795])
                        vertices.append([vx796,vz796,vy796])
                        vertices.append([vx797,vz797,vy797])
                        vertices.append([vx798,vz798,vy798])
                        vertices.append([vx799,vz799,vy799])
                        vertices.append([vx800,vz800,vy800])
                        vertices.append([vx801,vz801,vy801])
                        vertices.append([vx802,vz802,vy802])
                        vertices.append([vx803,vz803,vy803])
                        vertices.append([vx804,vz804,vy804])
                        vertices.append([vx805,vz805,vy805])
                        vertices.append([vx806,vz806,vy806])
                        vertices.append([vx807,vz807,vy807])
                        vertices.append([vx808,vz808,vy808])
                        vertices.append([vx809,vz809,vy809])
                        vertices.append([vx810,vz810,vy810])
                        vertices.append([vx811,vz811,vy811])
                        vertices.append([vx812,vz812,vy812])
                        vertices.append([vx813,vz813,vy813])
                        vertices.append([vx814,vz814,vy814])
                        vertices.append([vx815,vz815,vy815])
                        vertices.append([vx816,vz816,vy816])

                elif vertexCount == 41:
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
                        vx817 = unpack("<f", f.read(4))[0]
                        vy817 = unpack("<f", f.read(4))[0]
                        vz817 = unpack("<f", f.read(4))[0]
                        type817 = unpack("B", f.read(1))[0]
                        value1a817 = unpack("B", f.read(1))[0]
                        normalZ_817 = unpack("<h", f.read(2))[0]
                        vx818 = unpack("<f", f.read(4))[0]
                        vy818 = unpack("<f", f.read(4))[0]
                        vz818 = unpack("<f", f.read(4))[0]
                        type818 = unpack("B", f.read(1))[0]
                        value1a818 = unpack("B", f.read(1))[0]
                        normalZ_818 = unpack("<h", f.read(2))[0]
                        vx819 = unpack("<f", f.read(4))[0]
                        vy819 = unpack("<f", f.read(4))[0]
                        vz819 = unpack("<f", f.read(4))[0]
                        type819 = unpack("B", f.read(1))[0]
                        value1a819 = unpack("B", f.read(1))[0]
                        normalZ_819 = unpack("<h", f.read(2))[0]
                        vx820 = unpack("<f", f.read(4))[0]
                        vy820 = unpack("<f", f.read(4))[0]
                        vz820 = unpack("<f", f.read(4))[0]
                        type820 = unpack("B", f.read(1))[0]
                        value1a820 = unpack("B", f.read(1))[0]
                        normalZ_820 = unpack("<h", f.read(2))[0]
                        vx821 = unpack("<f", f.read(4))[0]
                        vy821 = unpack("<f", f.read(4))[0]
                        vz821 = unpack("<f", f.read(4))[0]
                        type821 = unpack("B", f.read(1))[0]
                        value1a821 = unpack("B", f.read(1))[0]
                        normalZ_821 = unpack("<h", f.read(2))[0]
                        vx822 = unpack("<f", f.read(4))[0]
                        vy822 = unpack("<f", f.read(4))[0]
                        vz822 = unpack("<f", f.read(4))[0]
                        type822 = unpack("B", f.read(1))[0]
                        value1a822 = unpack("B", f.read(1))[0]
                        normalZ_822 = unpack("<h", f.read(2))[0]
                        vx823 = unpack("<f", f.read(4))[0]
                        vy823 = unpack("<f", f.read(4))[0]
                        vz823 = unpack("<f", f.read(4))[0]
                        type823 = unpack("B", f.read(1))[0]
                        value1a823 = unpack("B", f.read(1))[0]
                        normalZ_823 = unpack("<h", f.read(2))[0]
                        vx824 = unpack("<f", f.read(4))[0]
                        vy824 = unpack("<f", f.read(4))[0]
                        vz824 = unpack("<f", f.read(4))[0]
                        type824 = unpack("B", f.read(1))[0]
                        value1a824 = unpack("B", f.read(1))[0]
                        normalZ_824 = unpack("<h", f.read(2))[0]
                        vx825 = unpack("<f", f.read(4))[0]
                        vy825 = unpack("<f", f.read(4))[0]
                        vz825 = unpack("<f", f.read(4))[0]
                        type825 = unpack("B", f.read(1))[0]
                        value1a825 = unpack("B", f.read(1))[0]
                        normalZ_825 = unpack("<h", f.read(2))[0]
                        vx826 = unpack("<f", f.read(4))[0]
                        vy826 = unpack("<f", f.read(4))[0]
                        vz826 = unpack("<f", f.read(4))[0]
                        type826 = unpack("B", f.read(1))[0]
                        value1a826 = unpack("B", f.read(1))[0]
                        normalZ_826 = unpack("<h", f.read(2))[0]
                        vx827 = unpack("<f", f.read(4))[0]
                        vy827 = unpack("<f", f.read(4))[0]
                        vz827 = unpack("<f", f.read(4))[0]
                        type827 = unpack("B", f.read(1))[0]
                        value1a827 = unpack("B", f.read(1))[0]
                        normalZ_827 = unpack("<h", f.read(2))[0]
                        vx828 = unpack("<f", f.read(4))[0]
                        vy828 = unpack("<f", f.read(4))[0]
                        vz828 = unpack("<f", f.read(4))[0]
                        type828 = unpack("B", f.read(1))[0]
                        value1a828 = unpack("B", f.read(1))[0]
                        normalZ_828 = unpack("<h", f.read(2))[0]
                        vx829 = unpack("<f", f.read(4))[0]
                        vy829 = unpack("<f", f.read(4))[0]
                        vz829 = unpack("<f", f.read(4))[0]
                        type829 = unpack("B", f.read(1))[0]
                        value1a829 = unpack("B", f.read(1))[0]
                        normalZ_829 = unpack("<h", f.read(2))[0]
                        vx830 = unpack("<f", f.read(4))[0]
                        vy830 = unpack("<f", f.read(4))[0]
                        vz830 = unpack("<f", f.read(4))[0]
                        type830 = unpack("B", f.read(1))[0]
                        value1a830 = unpack("B", f.read(1))[0]
                        normalZ_830 = unpack("<h", f.read(2))[0]
                        vx831 = unpack("<f", f.read(4))[0]
                        vy831 = unpack("<f", f.read(4))[0]
                        vz831 = unpack("<f", f.read(4))[0]
                        type831 = unpack("B", f.read(1))[0]
                        value1a831 = unpack("B", f.read(1))[0]
                        normalZ_831 = unpack("<h", f.read(2))[0]
                        vx832 = unpack("<f", f.read(4))[0]
                        vy832 = unpack("<f", f.read(4))[0]
                        vz832 = unpack("<f", f.read(4))[0]
                        type832 = unpack("B", f.read(1))[0]
                        value1a832 = unpack("B", f.read(1))[0]
                        normalZ_832 = unpack("<h", f.read(2))[0]
                        vx833 = unpack("<f", f.read(4))[0]
                        vy833 = unpack("<f", f.read(4))[0]
                        vz833 = unpack("<f", f.read(4))[0]
                        type833 = unpack("B", f.read(1))[0]
                        value1a833 = unpack("B", f.read(1))[0]
                        normalZ_833 = unpack("<h", f.read(2))[0]
                        vx834 = unpack("<f", f.read(4))[0]
                        vy834 = unpack("<f", f.read(4))[0]
                        vz834 = unpack("<f", f.read(4))[0]
                        type834 = unpack("B", f.read(1))[0]
                        value1a834 = unpack("B", f.read(1))[0]
                        normalZ_834 = unpack("<h", f.read(2))[0]
                        vx835 = unpack("<f", f.read(4))[0]
                        vy835 = unpack("<f", f.read(4))[0]
                        vz835 = unpack("<f", f.read(4))[0]
                        type835 = unpack("B", f.read(1))[0]
                        value1a835 = unpack("B", f.read(1))[0]
                        normalZ_835 = unpack("<h", f.read(2))[0]
                        vx836 = unpack("<f", f.read(4))[0]
                        vy836 = unpack("<f", f.read(4))[0]
                        vz836 = unpack("<f", f.read(4))[0]
                        type836 = unpack("B", f.read(1))[0]
                        value1a836 = unpack("B", f.read(1))[0]
                        normalZ_836 = unpack("<h", f.read(2))[0]
                        vx837 = unpack("<f", f.read(4))[0]
                        vy837 = unpack("<f", f.read(4))[0]
                        vz837 = unpack("<f", f.read(4))[0]
                        type837 = unpack("B", f.read(1))[0]
                        value1a837 = unpack("B", f.read(1))[0]
                        normalZ_837 = unpack("<h", f.read(2))[0]
                        vx838 = unpack("<f", f.read(4))[0]
                        vy838 = unpack("<f", f.read(4))[0]
                        vz838 = unpack("<f", f.read(4))[0]
                        type838 = unpack("B", f.read(1))[0]
                        value1a838 = unpack("B", f.read(1))[0]
                        normalZ_838 = unpack("<h", f.read(2))[0]
                        vx839 = unpack("<f", f.read(4))[0]
                        vy839 = unpack("<f", f.read(4))[0]
                        vz839 = unpack("<f", f.read(4))[0]
                        type839 = unpack("B", f.read(1))[0]
                        value1a839 = unpack("B", f.read(1))[0]
                        normalZ_839 = unpack("<h", f.read(2))[0]
                        vx840 = unpack("<f", f.read(4))[0]
                        vy840 = unpack("<f", f.read(4))[0]
                        vz840 = unpack("<f", f.read(4))[0]
                        type840 = unpack("B", f.read(1))[0]
                        value1a840 = unpack("B", f.read(1))[0]
                        normalZ_840 = unpack("<h", f.read(2))[0]
                        vx841 = unpack("<f", f.read(4))[0]
                        vy841 = unpack("<f", f.read(4))[0]
                        vz841 = unpack("<f", f.read(4))[0]
                        type841 = unpack("B", f.read(1))[0]
                        value1a841 = unpack("B", f.read(1))[0]
                        normalZ_841 = unpack("<h", f.read(2))[0]
                        vx842 = unpack("<f", f.read(4))[0]
                        vy842 = unpack("<f", f.read(4))[0]
                        vz842 = unpack("<f", f.read(4))[0]
                        type842 = unpack("B", f.read(1))[0]
                        value1a842 = unpack("B", f.read(1))[0]
                        normalZ_842 = unpack("<h", f.read(2))[0]
                        vx843 = unpack("<f", f.read(4))[0]
                        vy843 = unpack("<f", f.read(4))[0]
                        vz843 = unpack("<f", f.read(4))[0]
                        type843 = unpack("B", f.read(1))[0]
                        value1a843 = unpack("B", f.read(1))[0]
                        normalZ_843 = unpack("<h", f.read(2))[0]
                        vx844 = unpack("<f", f.read(4))[0]
                        vy844 = unpack("<f", f.read(4))[0]
                        vz844 = unpack("<f", f.read(4))[0]
                        type844 = unpack("B", f.read(1))[0]
                        value1a844 = unpack("B", f.read(1))[0]
                        normalZ_844 = unpack("<h", f.read(2))[0]
                        vx845 = unpack("<f", f.read(4))[0]
                        vy845 = unpack("<f", f.read(4))[0]
                        vz845 = unpack("<f", f.read(4))[0]
                        type845 = unpack("B", f.read(1))[0]
                        value1a845 = unpack("B", f.read(1))[0]
                        normalZ_845 = unpack("<h", f.read(2))[0]
                        vx846 = unpack("<f", f.read(4))[0]
                        vy846 = unpack("<f", f.read(4))[0]
                        vz846 = unpack("<f", f.read(4))[0]
                        type846 = unpack("B", f.read(1))[0]
                        value1a846 = unpack("B", f.read(1))[0]
                        normalZ_846 = unpack("<h", f.read(2))[0]
                        vx847 = unpack("<f", f.read(4))[0]
                        vy847 = unpack("<f", f.read(4))[0]
                        vz847 = unpack("<f", f.read(4))[0]
                        type847 = unpack("B", f.read(1))[0]
                        value1a847 = unpack("B", f.read(1))[0]
                        normalZ_847 = unpack("<h", f.read(2))[0]
                        vx848 = unpack("<f", f.read(4))[0]
                        vy848 = unpack("<f", f.read(4))[0]
                        vz848 = unpack("<f", f.read(4))[0]
                        type848 = unpack("B", f.read(1))[0]
                        value1a848 = unpack("B", f.read(1))[0]
                        normalZ_848 = unpack("<h", f.read(2))[0]
                        vx849 = unpack("<f", f.read(4))[0]
                        vy849 = unpack("<f", f.read(4))[0]
                        vz849 = unpack("<f", f.read(4))[0]
                        type849 = unpack("B", f.read(1))[0]
                        value1a849 = unpack("B", f.read(1))[0]
                        normalZ_849 = unpack("<h", f.read(2))[0]
                        vx850 = unpack("<f", f.read(4))[0]
                        vy850 = unpack("<f", f.read(4))[0]
                        vz850 = unpack("<f", f.read(4))[0]
                        type850 = unpack("B", f.read(1))[0]
                        value1a850 = unpack("B", f.read(1))[0]
                        normalZ_850 = unpack("<h", f.read(2))[0]
                        vx851 = unpack("<f", f.read(4))[0]
                        vy851 = unpack("<f", f.read(4))[0]
                        vz851 = unpack("<f", f.read(4))[0]
                        type851 = unpack("B", f.read(1))[0]
                        value1a851 = unpack("B", f.read(1))[0]
                        normalZ_851 = unpack("<h", f.read(2))[0]
                        vx852 = unpack("<f", f.read(4))[0]
                        vy852 = unpack("<f", f.read(4))[0]
                        vz852 = unpack("<f", f.read(4))[0]
                        type852 = unpack("B", f.read(1))[0]
                        value1a852 = unpack("B", f.read(1))[0]
                        normalZ_852 = unpack("<h", f.read(2))[0]
                        vx853 = unpack("<f", f.read(4))[0]
                        vy853 = unpack("<f", f.read(4))[0]
                        vz853 = unpack("<f", f.read(4))[0]
                        type853 = unpack("B", f.read(1))[0]
                        value1a853 = unpack("B", f.read(1))[0]
                        normalZ_853 = unpack("<h", f.read(2))[0]
                        vx854 = unpack("<f", f.read(4))[0]
                        vy854 = unpack("<f", f.read(4))[0]
                        vz854 = unpack("<f", f.read(4))[0]
                        type854 = unpack("B", f.read(1))[0]
                        value1a854 = unpack("B", f.read(1))[0]
                        normalZ_854 = unpack("<h", f.read(2))[0]
                        vx855 = unpack("<f", f.read(4))[0]
                        vy855 = unpack("<f", f.read(4))[0]
                        vz855 = unpack("<f", f.read(4))[0]
                        type855 = unpack("B", f.read(1))[0]
                        value1a855 = unpack("B", f.read(1))[0]
                        normalZ_855 = unpack("<h", f.read(2))[0]
                        vx856 = unpack("<f", f.read(4))[0]
                        vy856 = unpack("<f", f.read(4))[0]
                        vz856 = unpack("<f", f.read(4))[0]
                        type856 = unpack("B", f.read(1))[0]
                        value1a856 = unpack("B", f.read(1))[0]
                        normalZ_856 = unpack("<h", f.read(2))[0]
                        vx857 = unpack("<f", f.read(4))[0]
                        vy857 = unpack("<f", f.read(4))[0]
                        vz857 = unpack("<f", f.read(4))[0]
                        type857 = unpack("B", f.read(1))[0]
                        value1a857 = unpack("B", f.read(1))[0]
                        normalZ_857 = unpack("<h", f.read(2))[0]
                        vertices.append([vx817,vz817,vy817])
                        vertices.append([vx818,vz818,vy818])
                        vertices.append([vx819,vz819,vy819])
                        vertices.append([vx820,vz820,vy820])
                        vertices.append([vx821,vz821,vy821])
                        vertices.append([vx822,vz822,vy822])
                        vertices.append([vx823,vz823,vy823])
                        vertices.append([vx824,vz824,vy824])
                        vertices.append([vx825,vz825,vy825])
                        vertices.append([vx826,vz826,vy826])
                        vertices.append([vx827,vz827,vy827])
                        vertices.append([vx828,vz828,vy828])
                        vertices.append([vx829,vz829,vy829])
                        vertices.append([vx830,vz830,vy830])
                        vertices.append([vx831,vz831,vy831])
                        vertices.append([vx832,vz832,vy832])
                        vertices.append([vx833,vz833,vy833])
                        vertices.append([vx834,vz834,vy834])
                        vertices.append([vx835,vz835,vy835])
                        vertices.append([vx836,vz836,vy836])
                        vertices.append([vx837,vz837,vy837])
                        vertices.append([vx838,vz838,vy838])
                        vertices.append([vx839,vz839,vy839])
                        vertices.append([vx840,vz840,vy840])
                        vertices.append([vx841,vz841,vy841])
                        vertices.append([vx842,vz842,vy842])
                        vertices.append([vx843,vz843,vy843])
                        vertices.append([vx844,vz844,vy844])
                        vertices.append([vx845,vz845,vy845])
                        vertices.append([vx846,vz846,vy846])
                        vertices.append([vx847,vz847,vy847])
                        vertices.append([vx848,vz848,vy848])
                        vertices.append([vx849,vz849,vy849])
                        vertices.append([vx850,vz850,vy850])
                        vertices.append([vx851,vz851,vy851])
                        vertices.append([vx852,vz852,vy852])
                        vertices.append([vx853,vz853,vy853])
                        vertices.append([vx854,vz854,vy854])
                        vertices.append([vx855,vz855,vy855])
                        vertices.append([vx856,vz856,vy856])
                        vertices.append([vx857,vz857,vy857])

                elif vertexCount == 42:
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
                        vx858 = unpack("<f", f.read(4))[0]
                        vy858 = unpack("<f", f.read(4))[0]
                        vz858 = unpack("<f", f.read(4))[0]
                        type858 = unpack("B", f.read(1))[0]
                        value1a858 = unpack("B", f.read(1))[0]
                        normalZ_858 = unpack("<h", f.read(2))[0]
                        vx859 = unpack("<f", f.read(4))[0]
                        vy859 = unpack("<f", f.read(4))[0]
                        vz859 = unpack("<f", f.read(4))[0]
                        type859 = unpack("B", f.read(1))[0]
                        value1a859 = unpack("B", f.read(1))[0]
                        normalZ_859 = unpack("<h", f.read(2))[0]
                        vx860 = unpack("<f", f.read(4))[0]
                        vy860 = unpack("<f", f.read(4))[0]
                        vz860 = unpack("<f", f.read(4))[0]
                        type860 = unpack("B", f.read(1))[0]
                        value1a860 = unpack("B", f.read(1))[0]
                        normalZ_860 = unpack("<h", f.read(2))[0]
                        vx861 = unpack("<f", f.read(4))[0]
                        vy861 = unpack("<f", f.read(4))[0]
                        vz861 = unpack("<f", f.read(4))[0]
                        type861 = unpack("B", f.read(1))[0]
                        value1a861 = unpack("B", f.read(1))[0]
                        normalZ_861 = unpack("<h", f.read(2))[0]
                        vx862 = unpack("<f", f.read(4))[0]
                        vy862 = unpack("<f", f.read(4))[0]
                        vz862 = unpack("<f", f.read(4))[0]
                        type862 = unpack("B", f.read(1))[0]
                        value1a862 = unpack("B", f.read(1))[0]
                        normalZ_862 = unpack("<h", f.read(2))[0]
                        vx863 = unpack("<f", f.read(4))[0]
                        vy863 = unpack("<f", f.read(4))[0]
                        vz863 = unpack("<f", f.read(4))[0]
                        type863 = unpack("B", f.read(1))[0]
                        value1a863 = unpack("B", f.read(1))[0]
                        normalZ_863 = unpack("<h", f.read(2))[0]
                        vx864 = unpack("<f", f.read(4))[0]
                        vy864 = unpack("<f", f.read(4))[0]
                        vz864 = unpack("<f", f.read(4))[0]
                        type864 = unpack("B", f.read(1))[0]
                        value1a864 = unpack("B", f.read(1))[0]
                        normalZ_864 = unpack("<h", f.read(2))[0]
                        vx865 = unpack("<f", f.read(4))[0]
                        vy865 = unpack("<f", f.read(4))[0]
                        vz865 = unpack("<f", f.read(4))[0]
                        type865 = unpack("B", f.read(1))[0]
                        value1a865 = unpack("B", f.read(1))[0]
                        normalZ_865 = unpack("<h", f.read(2))[0]
                        vx866 = unpack("<f", f.read(4))[0]
                        vy866 = unpack("<f", f.read(4))[0]
                        vz866 = unpack("<f", f.read(4))[0]
                        type866 = unpack("B", f.read(1))[0]
                        value1a866 = unpack("B", f.read(1))[0]
                        normalZ_866 = unpack("<h", f.read(2))[0]
                        vx867 = unpack("<f", f.read(4))[0]
                        vy867 = unpack("<f", f.read(4))[0]
                        vz867 = unpack("<f", f.read(4))[0]
                        type867 = unpack("B", f.read(1))[0]
                        value1a867 = unpack("B", f.read(1))[0]
                        normalZ_867 = unpack("<h", f.read(2))[0]
                        vx868 = unpack("<f", f.read(4))[0]
                        vy868 = unpack("<f", f.read(4))[0]
                        vz868 = unpack("<f", f.read(4))[0]
                        type868 = unpack("B", f.read(1))[0]
                        value1a868 = unpack("B", f.read(1))[0]
                        normalZ_868 = unpack("<h", f.read(2))[0]
                        vx869 = unpack("<f", f.read(4))[0]
                        vy869 = unpack("<f", f.read(4))[0]
                        vz869 = unpack("<f", f.read(4))[0]
                        type869 = unpack("B", f.read(1))[0]
                        value1a869 = unpack("B", f.read(1))[0]
                        normalZ_869 = unpack("<h", f.read(2))[0]
                        vx870 = unpack("<f", f.read(4))[0]
                        vy870 = unpack("<f", f.read(4))[0]
                        vz870 = unpack("<f", f.read(4))[0]
                        type870 = unpack("B", f.read(1))[0]
                        value1a870 = unpack("B", f.read(1))[0]
                        normalZ_870 = unpack("<h", f.read(2))[0]
                        vx871 = unpack("<f", f.read(4))[0]
                        vy871 = unpack("<f", f.read(4))[0]
                        vz871 = unpack("<f", f.read(4))[0]
                        type871 = unpack("B", f.read(1))[0]
                        value1a871 = unpack("B", f.read(1))[0]
                        normalZ_871 = unpack("<h", f.read(2))[0]
                        vx872 = unpack("<f", f.read(4))[0]
                        vy872 = unpack("<f", f.read(4))[0]
                        vz872 = unpack("<f", f.read(4))[0]
                        type872 = unpack("B", f.read(1))[0]
                        value1a872 = unpack("B", f.read(1))[0]
                        normalZ_872 = unpack("<h", f.read(2))[0]
                        vx873 = unpack("<f", f.read(4))[0]
                        vy873 = unpack("<f", f.read(4))[0]
                        vz873 = unpack("<f", f.read(4))[0]
                        type873 = unpack("B", f.read(1))[0]
                        value1a873 = unpack("B", f.read(1))[0]
                        normalZ_873 = unpack("<h", f.read(2))[0]
                        vx874 = unpack("<f", f.read(4))[0]
                        vy874 = unpack("<f", f.read(4))[0]
                        vz874 = unpack("<f", f.read(4))[0]
                        type874 = unpack("B", f.read(1))[0]
                        value1a874 = unpack("B", f.read(1))[0]
                        normalZ_874 = unpack("<h", f.read(2))[0]
                        vx875 = unpack("<f", f.read(4))[0]
                        vy875 = unpack("<f", f.read(4))[0]
                        vz875 = unpack("<f", f.read(4))[0]
                        type875 = unpack("B", f.read(1))[0]
                        value1a875 = unpack("B", f.read(1))[0]
                        normalZ_875 = unpack("<h", f.read(2))[0]
                        vx876 = unpack("<f", f.read(4))[0]
                        vy876 = unpack("<f", f.read(4))[0]
                        vz876 = unpack("<f", f.read(4))[0]
                        type876 = unpack("B", f.read(1))[0]
                        value1a876 = unpack("B", f.read(1))[0]
                        normalZ_876 = unpack("<h", f.read(2))[0]
                        vx877 = unpack("<f", f.read(4))[0]
                        vy877 = unpack("<f", f.read(4))[0]
                        vz877 = unpack("<f", f.read(4))[0]
                        type877 = unpack("B", f.read(1))[0]
                        value1a877 = unpack("B", f.read(1))[0]
                        normalZ_877 = unpack("<h", f.read(2))[0]
                        vx878 = unpack("<f", f.read(4))[0]
                        vy878 = unpack("<f", f.read(4))[0]
                        vz878 = unpack("<f", f.read(4))[0]
                        type878 = unpack("B", f.read(1))[0]
                        value1a878 = unpack("B", f.read(1))[0]
                        normalZ_878 = unpack("<h", f.read(2))[0]
                        vx879 = unpack("<f", f.read(4))[0]
                        vy879 = unpack("<f", f.read(4))[0]
                        vz879 = unpack("<f", f.read(4))[0]
                        type879 = unpack("B", f.read(1))[0]
                        value1a879 = unpack("B", f.read(1))[0]
                        normalZ_879 = unpack("<h", f.read(2))[0]
                        vx880 = unpack("<f", f.read(4))[0]
                        vy880 = unpack("<f", f.read(4))[0]
                        vz880 = unpack("<f", f.read(4))[0]
                        type880 = unpack("B", f.read(1))[0]
                        value1a880 = unpack("B", f.read(1))[0]
                        normalZ_880 = unpack("<h", f.read(2))[0]
                        vx881 = unpack("<f", f.read(4))[0]
                        vy881 = unpack("<f", f.read(4))[0]
                        vz881 = unpack("<f", f.read(4))[0]
                        type881 = unpack("B", f.read(1))[0]
                        value1a881 = unpack("B", f.read(1))[0]
                        normalZ_881 = unpack("<h", f.read(2))[0]
                        vx882 = unpack("<f", f.read(4))[0]
                        vy882 = unpack("<f", f.read(4))[0]
                        vz882 = unpack("<f", f.read(4))[0]
                        type882 = unpack("B", f.read(1))[0]
                        value1a882 = unpack("B", f.read(1))[0]
                        normalZ_882 = unpack("<h", f.read(2))[0]
                        vx883 = unpack("<f", f.read(4))[0]
                        vy883 = unpack("<f", f.read(4))[0]
                        vz883 = unpack("<f", f.read(4))[0]
                        type883 = unpack("B", f.read(1))[0]
                        value1a883 = unpack("B", f.read(1))[0]
                        normalZ_883 = unpack("<h", f.read(2))[0]
                        vx884 = unpack("<f", f.read(4))[0]
                        vy884 = unpack("<f", f.read(4))[0]
                        vz884 = unpack("<f", f.read(4))[0]
                        type884 = unpack("B", f.read(1))[0]
                        value1a884 = unpack("B", f.read(1))[0]
                        normalZ_884 = unpack("<h", f.read(2))[0]
                        vx885 = unpack("<f", f.read(4))[0]
                        vy885 = unpack("<f", f.read(4))[0]
                        vz885 = unpack("<f", f.read(4))[0]
                        type885 = unpack("B", f.read(1))[0]
                        value1a885 = unpack("B", f.read(1))[0]
                        normalZ_885 = unpack("<h", f.read(2))[0]
                        vx886 = unpack("<f", f.read(4))[0]
                        vy886 = unpack("<f", f.read(4))[0]
                        vz886 = unpack("<f", f.read(4))[0]
                        type886 = unpack("B", f.read(1))[0]
                        value1a886 = unpack("B", f.read(1))[0]
                        normalZ_886 = unpack("<h", f.read(2))[0]
                        vx887 = unpack("<f", f.read(4))[0]
                        vy887 = unpack("<f", f.read(4))[0]
                        vz887 = unpack("<f", f.read(4))[0]
                        type887 = unpack("B", f.read(1))[0]
                        value1a887 = unpack("B", f.read(1))[0]
                        normalZ_887 = unpack("<h", f.read(2))[0]
                        vx888 = unpack("<f", f.read(4))[0]
                        vy888 = unpack("<f", f.read(4))[0]
                        vz888 = unpack("<f", f.read(4))[0]
                        type888 = unpack("B", f.read(1))[0]
                        value1a888 = unpack("B", f.read(1))[0]
                        normalZ_888 = unpack("<h", f.read(2))[0]
                        vx889 = unpack("<f", f.read(4))[0]
                        vy889 = unpack("<f", f.read(4))[0]
                        vz889 = unpack("<f", f.read(4))[0]
                        type889 = unpack("B", f.read(1))[0]
                        value1a889 = unpack("B", f.read(1))[0]
                        normalZ_889 = unpack("<h", f.read(2))[0]
                        vx890 = unpack("<f", f.read(4))[0]
                        vy890 = unpack("<f", f.read(4))[0]
                        vz890 = unpack("<f", f.read(4))[0]
                        type890 = unpack("B", f.read(1))[0]
                        value1a890 = unpack("B", f.read(1))[0]
                        normalZ_890 = unpack("<h", f.read(2))[0]
                        vx891 = unpack("<f", f.read(4))[0]
                        vy891 = unpack("<f", f.read(4))[0]
                        vz891 = unpack("<f", f.read(4))[0]
                        type891 = unpack("B", f.read(1))[0]
                        value1a891 = unpack("B", f.read(1))[0]
                        normalZ_891 = unpack("<h", f.read(2))[0]
                        vx892 = unpack("<f", f.read(4))[0]
                        vy892 = unpack("<f", f.read(4))[0]
                        vz892 = unpack("<f", f.read(4))[0]
                        type892 = unpack("B", f.read(1))[0]
                        value1a892 = unpack("B", f.read(1))[0]
                        normalZ_892 = unpack("<h", f.read(2))[0]
                        vx893 = unpack("<f", f.read(4))[0]
                        vy893 = unpack("<f", f.read(4))[0]
                        vz893 = unpack("<f", f.read(4))[0]
                        type893 = unpack("B", f.read(1))[0]
                        value1a893 = unpack("B", f.read(1))[0]
                        normalZ_893 = unpack("<h", f.read(2))[0]
                        vx894 = unpack("<f", f.read(4))[0]
                        vy894 = unpack("<f", f.read(4))[0]
                        vz894 = unpack("<f", f.read(4))[0]
                        type894 = unpack("B", f.read(1))[0]
                        value1a894 = unpack("B", f.read(1))[0]
                        normalZ_894 = unpack("<h", f.read(2))[0]
                        vx895 = unpack("<f", f.read(4))[0]
                        vy895 = unpack("<f", f.read(4))[0]
                        vz895 = unpack("<f", f.read(4))[0]
                        type895 = unpack("B", f.read(1))[0]
                        value1a895 = unpack("B", f.read(1))[0]
                        normalZ_895 = unpack("<h", f.read(2))[0]
                        vx896 = unpack("<f", f.read(4))[0]
                        vy896 = unpack("<f", f.read(4))[0]
                        vz896 = unpack("<f", f.read(4))[0]
                        type896 = unpack("B", f.read(1))[0]
                        value1a896 = unpack("B", f.read(1))[0]
                        normalZ_896 = unpack("<h", f.read(2))[0]
                        vx897 = unpack("<f", f.read(4))[0]
                        vy897 = unpack("<f", f.read(4))[0]
                        vz897 = unpack("<f", f.read(4))[0]
                        type897 = unpack("B", f.read(1))[0]
                        value1a897 = unpack("B", f.read(1))[0]
                        normalZ_897 = unpack("<h", f.read(2))[0]
                        vx898 = unpack("<f", f.read(4))[0]
                        vy898 = unpack("<f", f.read(4))[0]
                        vz898 = unpack("<f", f.read(4))[0]
                        type898 = unpack("B", f.read(1))[0]
                        value1a898 = unpack("B", f.read(1))[0]
                        normalZ_898 = unpack("<h", f.read(2))[0]
                        vx899 = unpack("<f", f.read(4))[0]
                        vy899 = unpack("<f", f.read(4))[0]
                        vz899 = unpack("<f", f.read(4))[0]
                        type899 = unpack("B", f.read(1))[0]
                        value1a899 = unpack("B", f.read(1))[0]
                        normalZ_899 = unpack("<h", f.read(2))[0]
                        vertices.append([vx858,vz858,vy858])
                        vertices.append([vx859,vz859,vy859])
                        vertices.append([vx860,vz860,vy860])
                        vertices.append([vx861,vz861,vy861])
                        vertices.append([vx862,vz862,vy862])
                        vertices.append([vx863,vz863,vy863])
                        vertices.append([vx864,vz864,vy864])
                        vertices.append([vx865,vz865,vy865])
                        vertices.append([vx866,vz866,vy866])
                        vertices.append([vx867,vz867,vy867])
                        vertices.append([vx868,vz868,vy868])
                        vertices.append([vx869,vz869,vy869])
                        vertices.append([vx870,vz870,vy870])
                        vertices.append([vx871,vz871,vy871])
                        vertices.append([vx872,vz872,vy872])
                        vertices.append([vx873,vz873,vy873])
                        vertices.append([vx874,vz874,vy874])
                        vertices.append([vx875,vz875,vy875])
                        vertices.append([vx876,vz876,vy876])
                        vertices.append([vx877,vz877,vy877])
                        vertices.append([vx878,vz878,vy878])
                        vertices.append([vx879,vz879,vy879])
                        vertices.append([vx880,vz880,vy880])
                        vertices.append([vx881,vz881,vy881])
                        vertices.append([vx882,vz882,vy882])
                        vertices.append([vx883,vz883,vy883])
                        vertices.append([vx884,vz884,vy884])
                        vertices.append([vx885,vz885,vy885])
                        vertices.append([vx886,vz886,vy886])
                        vertices.append([vx887,vz887,vy887])
                        vertices.append([vx888,vz888,vy888])
                        vertices.append([vx889,vz889,vy889])
                        vertices.append([vx890,vz890,vy890])
                        vertices.append([vx891,vz891,vy891])
                        vertices.append([vx892,vz892,vy892])
                        vertices.append([vx893,vz893,vy893])
                        vertices.append([vx894,vz894,vy894])
                        vertices.append([vx895,vz895,vy895])
                        vertices.append([vx896,vz896,vy896])
                        vertices.append([vx897,vz897,vy897])
                        vertices.append([vx898,vz898,vy898])
                        vertices.append([vx899,vz899,vy899])

                elif vertexCount:
                    raise Exception("must be 3 to 42 only not over")
                                        
                            
        elif Chunk == b"SST0":
            break

    collection = bpy.data.collections.new(os.path.basename(os.path.splitext(filepath)[0]))
    bpy.context.scene.collection.children.link(collection)

    mesh = bpy.data.meshes.new(os.path.basename(os.path.splitext(filepath)[0]))
    mesh.from_pydata(vertices, [], faces)
    objs = bpy.data.objects.new(os.path.basename(os.path.splitext(filepath)[0]), mesh)
    collection.objects.link(objs)

    for matti in materialsOBJ:
        objs.data.materials.append(matti)
        

    """bpy.context.view_layer.objects.active = objs

    bpy.ops.object.select_all(action='SELECT')
    bpy.ops.object.shade_smooth()
    bpy.ops.object.editmode_toggle()
    bpy.ops.mesh.remove_doubles()
    bpy.ops.mesh.normals_make_consistent(inside=False)
    bpy.ops.object.editmode_toggle()"""

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
