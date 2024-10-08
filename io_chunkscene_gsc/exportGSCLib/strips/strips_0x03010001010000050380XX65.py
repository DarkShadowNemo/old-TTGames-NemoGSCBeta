from struct import unpack, pack
import bpy
import os
import math

def vertices_0x03010001010000050380XX65(f):
    objmesh3=0
    for i, numesh in enumerate(bpy.data.meshes):
        if len(numesh.vertices) == 3:
            objmesh3+=336
    f.write(b"NU20")
    f.write(pack("<i", -abs(16+16+16+464*len(bpy.data.materials)+16+objmesh3+16+80*len(bpy.data.objects)+16+16)))
    f.write(pack("<I", 6))
    f.write(pack("<I", 0))
    f.write(b"NTBL")
    f.write(pack("<I", 16))
    f.write(pack("<I", 0))
    f.write(pack("<I", 0))
    f.write(b"MS00")
    f.write(pack("<I", len(bpy.data.materials)*464+16))
    f.write(pack("<I", len(bpy.data.materials)))
    f.write(pack("<I", 0))
    MatID=0
    BSDF = "Principled BSDF"
    for i, mat in enumerate(bpy.data.materials):
        f.write(pack("B", 13))
        f.write(pack("B", 0))
        f.write(pack("B", 1))
        f.write(pack("B", 0x60))
        f.write(pack("B", 0))
        f.write(pack("B", 0))
        f.write(pack("B", 0))
        f.write(pack("B", 0))
        f.write(pack("B", 0))
        f.write(pack("B", 0))
        f.write(pack("B", 0))
        f.write(pack("B", 16))
        f.write(pack("B", 8))
        f.write(pack("B", 0))
        f.write(pack("B", 0))
        f.write(pack("B", 0x50))
        f.write(pack("B", 7))
        f.write(pack("B", 0x80))
        f.write(pack("B", 0))
        f.write(pack("B", 0))
        f.write(pack("B", 0))
        f.write(pack("B", 0))
        f.write(pack("B", 0))
        f.write(pack("B", 16))
        f.write(pack("B", 14))
        f.write(pack("B", 0))
        f.write(pack("B", 0))
        f.write(pack("B", 0))
        f.write(pack("B", 0))
        f.write(pack("B", 0))
        f.write(pack("B", 0))
        f.write(pack("B", 0))
        f.write(pack("B", 0x48))
        f.write(pack("B", 0))
        f.write(pack("B", 0))
        f.write(pack("B", 0))
        f.write(pack("B", 0))
        f.write(pack("B", 0))
        f.write(pack("B", 0))
        f.write(pack("B", 0))
        f.write(pack("B", 0x1B))
        f.write(pack("B", 0))
        f.write(pack("B", 0))
        f.write(pack("B", 0))
        f.write(pack("B", 0))
        f.write(pack("B", 0))
        f.write(pack("B", 0))
        f.write(pack("B", 0))
        f.write(pack("B", 0x44))
        f.write(pack("B", 0))
        f.write(pack("B", 0))
        f.write(pack("B", 0))
        f.write(pack("B", 0))
        f.write(pack("B", 0))
        f.write(pack("B", 0))
        f.write(pack("B", 0))
        f.write(pack("B", 0x42))
        f.write(pack("B", 0))
        f.write(pack("B", 0))
        f.write(pack("B", 0))
        f.write(pack("B", 0))
        f.write(pack("B", 0))
        f.write(pack("B", 0))
        f.write(pack("B", 0))
        f.write(pack("B", 0x8C))
        f.write(pack("B", 0))
        f.write(pack("B", 0))
        f.write(pack("B", 1))
        f.write(pack("B", 0))
        f.write(pack("B", 0))
        f.write(pack("B", 0))
        f.write(pack("B", 0))
        f.write(pack("B", 0x4E))
        f.write(pack("B", 0))
        f.write(pack("B", 0))
        f.write(pack("B", 0))
        f.write(pack("B", 0))
        f.write(pack("B", 0))
        f.write(pack("B", 0))
        f.write(pack("B", 0))
        f.write(pack("B", 0xDB))
        f.write(pack("B", 0x37))
        f.write(pack("B", 5))
        f.write(pack("B", 0))
        f.write(pack("B", 0))
        f.write(pack("B", 0))
        f.write(pack("B", 0))
        f.write(pack("B", 0))
        f.write(pack("B", 0x47))
        f.write(pack("B", 0))
        f.write(pack("B", 0))
        f.write(pack("B", 0))
        f.write(pack("B", 0))
        f.write(pack("B", 0))
        f.write(pack("B", 0))
        f.write(pack("B", 0))
        f.write(pack("B", 0))
        f.write(pack("B", 0))
        f.write(pack("B", 0))
        f.write(pack("B", 0))
        f.write(pack("B", 0))
        f.write(pack("B", 0))
        f.write(pack("B", 0))
        f.write(pack("B", 0))
        f.write(pack("B", 0x7F))
        f.write(pack("B", 0))
        f.write(pack("B", 0))
        f.write(pack("B", 0))
        f.write(pack("B", 0))#1
        f.write(pack("B", 0))#2
        f.write(pack("B", 0))#3
        f.write(pack("B", 0))#4
        f.write(pack("B", 1))
        f.write(pack("B", 1))
        f.write(pack("B", 0))
        f.write(pack("B", 1))
        f.write(pack("B", 0x13))
        f.write(pack("B", 0))
        f.write(pack("B", 3))
        f.write(pack("B", 0x6C))
        f.write(pack("<f", 1))
        f.write(pack("<f", 1))
        f.write(pack("<f", 1))
        f.write(pack("<f", 1))
        for i in range(19):
            f.write(pack("B", 0))
        f.write(pack("B", 0x30))
        f.write(pack("B", 0))
        f.write(pack("B", 0))
        f.write(pack("B", 0))
        f.write(pack("B", 0))
        for i in range(128):
            f.write(pack("B", 0))
        f.write(pack("B", 0x19))
        f.write(pack("B", 0))
        f.write(pack("B", 0))
        f.write(pack("B", 0))

        f.write(pack("B", 0))
        f.write(pack("B", 0))
        f.write(pack("B", 0))
        f.write(pack("B", 0))

        f.write(pack("B", 0))
        f.write(pack("B", 0))
        f.write(pack("B", 0))
        f.write(pack("B", 0))

        f.write(pack("B", 0))
        f.write(pack("B", 0))
        f.write(pack("B", 0))
        f.write(pack("B", 0))

        f.write(pack("B", 0))
        f.write(pack("B", 0))
        f.write(pack("B", 0))
        f.write(pack("B", 0))

        f.write(pack("<I", 16384))
        f.write(pack("B", 0xB0))
        f.write(pack("B", 0xE2))
        f.write(pack("B", 0xA3))
        f.write(pack("B", 0))
        f.write(pack("B", 0x80))
        f.write(pack("B", 0x60))
        f.write(pack("B", 0x49))
        f.write(pack("B", 0))
        f.write(pack("B", 0))
        f.write(pack("B", 0))
        f.write(pack("B", 0))
        f.write(pack("B", 0))

        f.write(pack("B", 0))
        f.write(pack("B", 0))
        f.write(pack("B", 0))
        f.write(pack("B", 0))
        f.write(pack("B", 0))
        f.write(pack("B", 0))
        f.write(pack("B", 0))
        f.write(pack("B", 0))
        f.write(pack("B", 0))
        f.write(pack("B", 0))
        f.write(pack("B", 0))
        f.write(pack("B", 0))
        f.write(pack("B", 0))
        f.write(pack("B", 0))
        f.write(pack("B", 0))
        f.write(pack("B", 0))
        f.write(pack("B", 0x3D))
        f.write(pack("B", 0))
        f.write(pack("B", 0))
        f.write(pack("B", 0))
        f.write(pack("B", 0))
        f.write(pack("B", 0))
        f.write(pack("B", 0))
        f.write(pack("B", 0))
        f.write(pack("B", 0x58))
        f.write(pack("B", 0xE3))
        f.write(pack("B", 0xA3))
        f.write(pack("B", 0))
        f.write(pack("B", 0xB0))
        f.write(pack("B", 0xDD))
        f.write(pack("B", 0x87))
        f.write(pack("B", 0))
        f.write(pack("B", 0x60))
        f.write(pack("B", 0x7B))
        f.write(pack("B", 0x98))
        f.write(pack("B", 0))
        f.write(pack("B", 0))
        f.write(pack("B", 0))
        f.write(pack("B", 0))
        f.write(pack("B", 0))
        f.write(pack("<f", 0))
        f.write(pack("B", 0x13))
        f.write(pack("B", 0))
        f.write(pack("B", 0))
        f.write(pack("B", 0))
        f.write(pack("B", 0))
        f.write(pack("B", 0))
        f.write(pack("B", 0))
        f.write(pack("B", 0))
        f.write(pack("B", 0))
        f.write(pack("B", 0))
        f.write(pack("B", 0))
        f.write(pack("B", 0))
        f.write(pack("B", 0))
        f.write(pack("B", 0))
        f.write(pack("B", 0))
        f.write(pack("B", 0))
        f.write(pack("<f", mat.node_tree.nodes[BSDF].inputs[0].default_value[0]))
        f.write(pack("<f", mat.node_tree.nodes[BSDF].inputs[0].default_value[1]))
        f.write(pack("<f", mat.node_tree.nodes[BSDF].inputs[0].default_value[2]))
        f.write(pack("<f", 0))
        f.write(pack("<I", 0))
        f.write(pack("<I", 0))
        f.write(pack("<I", 0))
        f.write(pack("<I", 0))
        f.write(pack("<f", 1))
        f.write(pack("<I", 0))
        f.write(pack("<I", MatID))
        f.write(pack("B", 0xA6))
        f.write(pack("B", 255))
        f.write(pack("B", 0))
        f.write(pack("B", 0))

        f.write(pack("<I", 0))
        f.write(pack("<I", 0))
        f.write(pack("<I", 0))
        f.write(pack("<I", 0))
        f.write(pack("<I", 0))
        f.write(pack("<I", 0))
        f.write(pack("B", 0))
        f.write(pack("B", 0))
        f.write(pack("B", 0))
        f.write(pack("B", 0xFF))
        f.write(pack("B", 0))
        f.write(pack("B", 0))
        f.write(pack("B", 0))
        f.write(pack("B", 0))

        MatID+=1
    f.write(b"OBJ0")
    f.write(pack("<I", objmesh3+16))
    f.write(pack("<I", len(bpy.data.objects)))
    f.write(pack("<I", 0))
    for i, obdata in enumerate(bpy.data.meshes):
        if len(obdata.vertices) == 3:
            
            f.write(pack("<I", 4))
            f.write(pack("<I", 0))
            f.write(pack("<I", 0))
            f.write(pack("<I", 0))
            f.write(pack("<I", 0))
            f.write(pack("<I", 1))
            f.write(pack("<I", 0))
            f.write(pack("<I", 0))
            f.write(pack("<I", 0))
            f.write(pack("<I", 0))
            f.write(pack("<I", 0))
            f.write(pack("<I", 0))
            f.write(pack("<I", 0))
            f.write(pack("<I", 96))
            f.write(pack("<I", 0))
            f.write(pack("<I", 0))
                                
            f.write(pack("<I", 0))
            f.write(pack("<I", 0))
            f.write(pack("<I", 0))
            f.write(pack("<I", 0))
            f.write(pack("<I", 0))
            f.write(pack("<I", 0))
            f.write(pack("<I", 0))
            f.write(pack("<I", 0))
            f.write(pack("<I", 0))
            f.write(pack("<I", 0))
            f.write(pack("<I", 0))
            f.write(pack("<I", 0))
            f.write(pack("<I", 0))
            f.write(pack("<I", 0))
            f.write(pack("<I", 0))
            f.write(pack("<I", 0))
            f.write(pack("<I", 0))
            f.write(pack("<I", 0))
            f.write(pack("<I", 0))
            f.write(pack("<I", 0))
            f.write(pack("<I", 0))
            f.write(pack("<I", 0))
            f.write(pack("<I", 0))
            f.write(pack("<I", 144))
            f.write(pack("<H", len(obdata.vertices)*3))
            f.write(pack("<H", 24581))
            f.write(pack("<I", 0))
            f.write(pack("<I", 0))
            f.write(pack("<I", 0))
            f.write(pack("<H", 86))
            f.write(pack("<H", 27649))
            f.write(pack("<I", 32768))
            f.write(pack("B", 0))
            f.write(pack("<H", 704))
            f.write(pack("B", 0x30))
            f.write(pack("B", 18))
            f.write(pack("B", 5))
            f.write(pack("B", 0))
            f.write(pack("B", 0))
            f.write(pack("<I", 0))
            f.write(pack("B", 0xD2))
            f.write(pack("B", 128))
            f.write(pack("B", 1))
            f.write(pack("B", 108))
            f.write(pack("B", len(obdata.vertices)))
            f.write(pack("<I", 128))
            f.write(pack("B", 64))
            f.write(pack("B", 2))
            f.write(pack("B", 48))
            f.write(pack("<I", 1298))
            f.write(pack("<I", 0))
            f.write(pack("B", 2))
            f.write(pack("B", 128))
            f.write(pack("B", 1))
            f.write(pack("B", 109))
            f.write(pack("<I", len(obdata.vertices)*3))
            f.write(pack("<I", 0))
            f.write(pack("B", 3))
            f.write(pack("B", 1))
            f.write(pack("B", 0))
            f.write(pack("B", 1))
            f.write(pack("B", 1))
            f.write(pack("B", 0))
            f.write(pack("B", 0))
            f.write(pack("B", 5))
            f.write(pack("B", 3))
            f.write(pack("B", 128))
            f.write(pack("B", len(obdata.vertices)))
            f.write(pack("B", 101))
            for v in obdata.vertices:
                f.write(pack("<h", int(4096*v.co.x)))
                f.write(pack("<h", int(4096*v.co.z)))
                f.write(pack("<h", int(4096*v.co.y)))
            f.write(pack("B", 1))
            f.write(pack("B", 1))
            f.write(pack("B", 0))
            f.write(pack("B", 1))
            f.write(pack("B", 0))
            f.write(pack("B", 3))
            f.write(pack("B", 0))
            f.write(pack("B", 20))
            f.write(pack("<I", 0))
            f.write(pack("<I", 0))
            f.write(pack("<I", 0))

            f.write(pack("<I", 0))
            f.write(pack("<I", 0))
            f.write(pack("<I", 0))
            f.write(pack("<I", 0))
            f.write(pack("<I", 0))
            f.write(pack("<H", 0))
            f.write(pack("<I", 0))
            f.write(pack("<f", 1))
            f.write(pack("<f", 1))
            f.write(pack("<f", 1))
            f.write(pack("<f", 1))
            f.write(pack("<f", 1))
            f.write(pack("<f", 1))
            f.write(pack("<f", 1))
            f.write(pack("<f", 1))
    f.write(b"INST")
    f.write(pack("<I", len(bpy.data.objects)*80+16))
    f.write(pack("<I", len(bpy.data.objects)))
    f.write(pack("<I", 0))
    objIndex=0
    for i, obj in enumerate(bpy.data.objects):
        f.write(pack("<f", obj.scale[0]))
        f.write(pack("<f", math.radians(obj.rotation_euler[2])))
        f.write(pack("<f", math.radians(obj.rotation_euler[1])))
        f.write(pack("<f", 0))
        f.write(pack("<f", math.radians(-obj.rotation_euler[2])))
        f.write(pack("<f", obj.scale[1]))
        f.write(pack("<f", math.radians(obj.rotation_euler[0]))) # 28
        f.write(pack("<f", math.radians(-obj.rotation_euler[1]))) # 32
        f.write(pack("<f", 0))
        f.write(pack("<f", math.radians(-obj.rotation_euler[0])))
        f.write(pack("<f", obj.scale[2]))
        f.write(pack("<f", 0))
        f.write(pack("<f", obj.location[0]))
        f.write(pack("<f", obj.location[2]))
        f.write(pack("<f", obj.location[1]))
        f.write(pack("<f", 1))
        f.write(pack("<i", objIndex))
        f.write(pack("<I", 37))
        f.write(pack("<f", 0))
        f.write(pack("<f", 0))
        objIndex+=1
    f.write(b"SST0")
    f.write(pack("<I", 16))
    f.write(pack("<I", 0))
    f.write(pack("<I", 0))
    f.write(b"BNDS")
    f.write(pack("<I", 16))
    f.write(pack("<I", 0))
    f.write(pack("<I", 0))
