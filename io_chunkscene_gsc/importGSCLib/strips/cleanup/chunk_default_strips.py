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
                for j in range(vertexCount3):
                    vx = unpack("<f", f.read(4))[0]
                    vy = unpack("<f", f.read(4))[0]
                    vz = unpack("<f", f.read(4))[0]
                    type4 = unpack("B", f.read(1))[0]==False
                    value1 = unpack("B", f.read(1))[0]
                    f.seek(2,1)

                    verts_def.append([vx,vz,vy])
                    
                    fa_def+=1
                    fb_def+=1
                    fc_def+=1
                    if type4 > 0:
                        faces_def.append([j+j+type4-type4-1+fa_def-j-j-1+j%2,j-j+type4-type4+1+fb_def-2-1+j-j-j%2,j+type4-type4+fc_def-j+2-4])
                        
                offset1 = unpack("<I", f.read(4))[0]
                if offset1 == 16777473:
                    offset2 = unpack("<I", f.read(4))[0]
                    if offset2 == 335545088:
                        collection = bpy.data.collections.new("default")
                        bpy.context.scene.collection.children.link(collection)
                        meshW1 = bpy.data.meshes.new("default")
                        meshW1.from_pydata(verts_def, [], faces_def)
                        object1W1 = bpy.data.objects.new("default", meshW1)
                        collection.objects.link(object1W1)
