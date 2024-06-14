from struct import pack, unpack
import os
import bpy
import math

def get_splineset(f):
    ea=-1
    eb=0
    vertices=[]
    edges=[]
    
    f.seek(0)
    splinesetread = f.read()
    splinesearch = splinesetread.find(b"\x53\x53\x54\x30")
    if splinesetread != 0:
        f.seek(splinesearch, 0)
        SST0S = unpack("<I", f.read(4))[0]
        SST0Size = unpack("<I",f.read(4))[0]
        entrycount = unpack("<I",f.read(4))[0]
        f.seek(4,1)
        for i in range(entrycount):
            pointCount = unpack("<I",f.read(4))[0]
            nameOffsets = unpack("<I",f.read(4))[0]
            for j in range(pointCount):
                vx = unpack("<f",f.read(4))[0]
                vy = unpack("<f",f.read(4))[0]
                vz = unpack("<f",f.read(4))[0]
                vertices.append([vx, vz, vy])
            for e in range(pointCount-1):
                ea+=1
                eb+=1
                edges.append([ea+i,eb+i])
        collection = bpy.data.collections.new("SST0")
        bpy.context.scene.collection.children.link(collection)
        mesh = bpy.data.meshes.new("SST0")
        mesh.from_pydata(vertices, edges, [])
        obj2 = bpy.data.objects.new("SST0", mesh)
        bpy.context.collection.objects.link(obj2)
    else:
        raise Exception("no spline found")
