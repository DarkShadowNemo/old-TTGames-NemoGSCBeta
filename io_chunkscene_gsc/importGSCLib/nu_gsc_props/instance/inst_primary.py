from struct import pack, unpack
import os
import bpy
import math
import mathutils

def get_INST_1st(f):
    bones_=[]
    coll = bpy.context.collection
    skel = bpy.data.armatures.new('INST Skeleton')
    arma = bpy.data.objects.new('INST Armature', skel)
    coll.objects.link(arma)
    bpy.context.view_layer.objects.active = arma
    bpy.ops.object.mode_set(mode = 'EDIT')
    
    f.seek(0)
    INSTread = f.read()
    INSTfound = INSTread.find(b"\x49\x4E\x53\x54")
    if INSTread != 0:
        f.seek(INSTfound, 0)
        f.seek(8,1)
        INSTcount = unpack("<I", f.read(4))[0]
        unk01 = unpack("<I", f.read(4))[0]
        for i in range(INSTcount):
            ScaleX = unpack("<f", f.read(4))[0]
            rotationz = unpack("<f", f.read(4))[0]
            rotationy = unpack("<f", f.read(4))[0]
            null1 = unpack("<f", f.read(4))[0]
            nrotationz = unpack("<f", f.read(4))[0]
            ScaleY = unpack("<f", f.read(4))[0]
            rotationx = unpack("<f", f.read(4))[0]
            nrotationy = unpack("<f", f.read(4))[0]
            null2 = unpack("<f", f.read(4))[0]
            nrotationx = unpack("<f", f.read(4))[0]
            ScaleZ = unpack("<f", f.read(4))[0]
            null3 = unpack("<f", f.read(4))[0]
            posx = unpack("<f", f.read(4))[0]
            posy = unpack("<f", f.read(4))[0]
            posz = unpack("<f", f.read(4))[0]
            ScaleW = unpack("<f", f.read(4))[0]
            f.seek(16,1)
            m1 = ([ScaleX,rotationz,rotationy,null1])
            m2 = ([nrotationz,ScaleY,rotationx,nrotationy])
            m3 = ([null2,nrotationx,ScaleZ,null3])
            m4 = ([posx,posy,posz,ScaleW])

            matrix = mathutils.Matrix([m1,m3,m2,m4]).to_3x3()

            bone = skel.edit_bones.new("inst_bones")
            
            bone.tail = mathutils.Vector([0,0,0.03])
            
            bone.head = ([
                posx,
                posy,
                posz,
            ])
            
            bone.length = -0.03
            
            bone.transform(matrix)
        bpy.ops.object.mode_set(mode = 'OBJECT')
    else:
        raise Exception("no INST found")
