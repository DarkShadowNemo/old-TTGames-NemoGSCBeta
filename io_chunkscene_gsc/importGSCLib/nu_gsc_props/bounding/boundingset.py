from struct import pack, unpack
import os
import bpy
import math

def get_BoundsSet1(f):
    ea=-1
    eb=0
    vertices=[]
    bounds=[]
    
    f.seek(0)
    boundssetread = f.read()
    boundssearch = boundssetread.find(b"\x42\x4E\x44\x53")
    if boundssetread != 0:
        f.seek(boundssearch, 0)
        BNDS = unpack("<I", f.read(4))[0]
        BNDS_Size = unpack("<I", f.read(4))[0]
        BNDS_Count = unpack("<I", f.read(4))[0]
        BNDS_VertCount = unpack("<I", f.read(4))[0]
        null1 = unpack("<I", f.read(4))[0]
        null2 = unpack("<I", f.read(4))[0]
        for i in range(BNDS_Count):
            
            for k in range(BNDS_VertCount):
                vx = unpack("<f", f.read(4))[0]
                vy = unpack("<f", f.read(4))[0]
                vz = unpack("<f", f.read(4))[0]
                f.seek(36,1)
                vertices.append([vx,vz,vy])
                
            for j in range(BNDS_VertCount-1):
                ea+=1
                eb+=1
                bounds.append([ea+i,eb+i])

        collection = bpy.data.collections.new("BNDS")
        bpy.context.scene.collection.children.link(collection)
        mesh = bpy.data.meshes.new("BNDS")
        mesh.from_pydata(vertices, bounds, [])
        obj2 = bpy.data.objects.new("BNDS", mesh)
        bpy.context.collection.objects.link(obj2)
    else:
        raise Exception("no boundingset found")
