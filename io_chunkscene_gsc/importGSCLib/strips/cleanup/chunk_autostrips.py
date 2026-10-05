from struct import unpack, pack
import os
import bpy
import math
from io import BytesIO as bio

def wholeChunk1_auto(f, filepath):
    f.seek(0)
    autoChunks = f.read()
    f.seek(0)

    verts_auto=[]
    faces_auto=[]

    verts_autoa=[]
    faces_autoa=[]

    verts_autob=[]
    faces_autob=[]

    fa_auto=-3
    fb_auto=-2
    fc_auto=-1

    fa_autoa=-4
    fb_autoa=-3
    fc_autoa=-2
    fd_autoa=-1

    fa_autob=-5
    fb_autob=-4
    fc_autob=-3
    fd_autob=-2
    fe_autob=-1
    

    
    while f.tell() < len(autoChunks):
        autoChunks1 = f.read(4)
        if autoChunks1 == b"\x03\x01\x00\x01":
            f.seek(2,1)
            vertexCountAuto1 = unpack("B", f.read(1))[0]
            flagsssssAuto1 = unpack("B", f.read(1))[0]
            if flagsssssAuto1 == 0x68:
                if vertexCountAuto1 == 0:
                    pass
                elif vertexCountAuto1 == 1:
                    pass
                elif vertexCountAuto1 == 2:
                    pass
                elif vertexCountAuto1 == 3:
                    for i in range(1):
                        auto_vx1 = unpack("<f", f.read(4))[0]
                        auto_vy1 = unpack("<f", f.read(4))[0]
                        auto_vz1 = unpack("<f", f.read(4))[0]
                        auto_vx2 = unpack("<f", f.read(4))[0]
                        auto_vy2 = unpack("<f", f.read(4))[0]
                        auto_vz2 = unpack("<f", f.read(4))[0]
                        auto_vx3 = unpack("<f", f.read(4))[0]
                        auto_vy3 = unpack("<f", f.read(4))[0]
                        auto_vz3 = unpack("<f", f.read(4))[0]
                    auto_offset1 = unpack("<I", f.read(4))[0]
                    if auto_offset1 == 16777473:
                        auto_offset1_ = unpack("<I", f.read(4))[0]
                        if auto_offset1_ == 335545088:
                            verts_auto.append([auto_vx1,auto_vz1,auto_vy1])
                            verts_auto.append([auto_vx2,auto_vz2,auto_vy2])
                            verts_auto.append([auto_vx3,auto_vz3,auto_vy3])

                            fa_auto+=1*3
                            fb_auto+=1*3
                            fc_auto+=1*3
                            faces_auto.append([fa_auto,fb_auto,fc_auto])
                        elif auto_offset1_ == 335545092:
                            pass
                elif vertexCountAuto1 == 4:
                    for i in range(1):
                        auto_vx1a = unpack("<f", f.read(4))[0]
                        auto_vy1a = unpack("<f", f.read(4))[0]
                        auto_vz1a = unpack("<f", f.read(4))[0]
                        auto_vx2a = unpack("<f", f.read(4))[0]
                        auto_vy2a = unpack("<f", f.read(4))[0]
                        auto_vz2a = unpack("<f", f.read(4))[0]
                        auto_vx3a = unpack("<f", f.read(4))[0]
                        auto_vy3a = unpack("<f", f.read(4))[0]
                        auto_vz3a = unpack("<f", f.read(4))[0]
                        auto_vx4a = unpack("<f", f.read(4))[0]
                        auto_vy4a = unpack("<f", f.read(4))[0]
                        auto_vz4a = unpack("<f", f.read(4))[0]
                    auto_offset2 = unpack("<I", f.read(4))[0]
                    if auto_offset2 == 16777473:
                        auto_offset2_ = unpack("<I", f.read(4))[0]
                        if auto_offset2_ == 335545088:
                            verts_autoa.append([auto_vx1a,auto_vz1a,auto_vy1a])
                            verts_autoa.append([auto_vx2a,auto_vz2a,auto_vy2a])
                            verts_autoa.append([auto_vx3a,auto_vz3a,auto_vy3a])
                            verts_autoa.append([auto_vx4a,auto_vz4a,auto_vy4a])

                            fa_autoa+=1*4
                            fb_autoa+=1*4
                            fc_autoa+=1*4
                            fd_autoa+=1*4
                            faces_autoa.append([fa_autoa,fb_autoa,fc_autoa])
                            faces_autoa.append([fb_autoa,fc_autoa,fd_autoa])
                        elif auto_offset2_ == 335545092:
                            pass
                elif vertexCountAuto1 == 5:
                    for i in range(1):
                        auto_vx1b = unpack("<f", f.read(4))[0]
                        auto_vy1b = unpack("<f", f.read(4))[0]
                        auto_vz1b = unpack("<f", f.read(4))[0]
                        auto_vx2b = unpack("<f", f.read(4))[0]
                        auto_vy2b = unpack("<f", f.read(4))[0]
                        auto_vz2b = unpack("<f", f.read(4))[0]
                        auto_vx3b = unpack("<f", f.read(4))[0]
                        auto_vy3b = unpack("<f", f.read(4))[0]
                        auto_vz3b = unpack("<f", f.read(4))[0]
                        auto_vx4b = unpack("<f", f.read(4))[0]
                        auto_vy4b = unpack("<f", f.read(4))[0]
                        auto_vz4b = unpack("<f", f.read(4))[0]
                        auto_vx5b = unpack("<f", f.read(4))[0]
                        auto_vy5b = unpack("<f", f.read(4))[0]
                        auto_vz5b = unpack("<f", f.read(4))[0]
                    auto_offset3 = unpack("<I", f.read(4))[0]
                    if auto_offset3 == 16777473:
                        auto_offset3_ = unpack("<I", f.read(4))[0]
                        if auto_offset3 == 335545088:
                            verts_autob.append([auto_vx1b,auto_vz1b,auto_vy1b])
                            verts_autob.append([auto_vx2b,auto_vz2b,auto_vy2b])
                            verts_autob.append([auto_vx3b,auto_vz3b,auto_vy3b])
                            verts_autob.append([auto_vx4b,auto_vz4b,auto_vy4b])
                            verts_autob.append([auto_vx5b,auto_vz5b,auto_vy5b])

                            fa_autob+=1*5
                            fb_autob+=1*5
                            fc_autob+=1*5
                            fd_autob+=1*5
                            fe_autob+=1*5
                            faces_autob.append([fa_autob,fb_autob,fc_autob])
                            faces_autob.append([fb_autob,fc_autob,fd_autob])
                            faces_autob.append([fc_autob,fd_autob,fe_autob])
                        elif auto_offset3_ == 335545092:
                            pass

    collection = bpy.data.collections.new(os.path.basename(os.path.splitext(filepath)[0]))
    bpy.context.scene.collection.children.link(collection)
    mes15_auto = bpy.data.meshes.new(os.path.basename(os.path.splitext(filepath)[0]))
    mes15_auto.from_pydata(verts_auto, [], faces_auto)
    obj15_auto = bpy.data.objects.new(os.path.basename(os.path.splitext(filepath)[0]), mes15_auto)
    collection.objects.link(obj15_auto)

    mes15_auto1 = bpy.data.meshes.new(os.path.basename(os.path.splitext(filepath)[0]))
    mes15_auto1.from_pydata(verts_autoa, [], faces_autoa)
    obj15_auto1 = bpy.data.objects.new(os.path.basename(os.path.splitext(filepath)[0]), mes15_auto1)
    collection.objects.link(obj15_auto1)

    mes15_auto2 = bpy.data.meshes.new(os.path.basename(os.path.splitext(filepath)[0]))
    mes15_auto2.from_pydata(verts_autob, [], faces_autob)
    obj15_auto2 = bpy.data.objects.new(os.path.basename(os.path.splitext(filepath)[0]), mes15_auto2)
    collection.objects.link(obj15_auto2)
