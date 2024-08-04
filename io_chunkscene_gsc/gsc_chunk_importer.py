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
from .importGSCLib.strips.cleanup.chunk_strips import *
    

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

def ColorReach(f, filepath):
    rgba=[]
    obdata = bpy.context.object.data
    f.seek(0)
    ColorRead = f.read()
    ColorFind = ColorRead.find(b"\x00\x00\x00\x05\x05\xC0")
    if ColorRead!=0:
        f.seek(ColorFind, 0)
        f.seek(6,1)
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
            ColorReach(f, filepath)
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
                



