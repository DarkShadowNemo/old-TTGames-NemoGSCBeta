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

    fa_auto=-3
    fb_auto=-2
    fc_auto=-1

    
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

    collection = bpy.data.collections.new(os.path.basename(os.path.splitext(filepath)[0]))
    bpy.context.scene.collection.children.link(collection)
    mes15_auto = bpy.data.meshes.new(os.path.basename(os.path.splitext(filepath)[0]))
    mes15_auto.from_pydata(verts_auto, [], faces_auto)
    obj15_auto = bpy.data.objects.new(os.path.basename(os.path.splitext(filepath)[0]), mes15_auto)
    collection.objects.link(obj15_auto)
