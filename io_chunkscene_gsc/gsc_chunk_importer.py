from struct import pack, unpack
import os
import bpy
import bmesh
import math
from io import BytesIO as bio

texture_pixels = []

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

def one_pallete_memory(f, TEX_OFFSET=0):
    pass

def get_3rdobjects_with_uvs_and_rgba(f, vertexCount=0, seek_=0, vertices=[], faces=[], normals=[], fa=-1, fb=0, fc=1, uvs=[], rgba=[], chunks=0, paddingWhere=0):
    f.seek(0)
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
            nz = unpack("<f", f.read(4))[0]
            vertices.append([vx,vy,vz])
            normals.append([nz,nz,nz])
        for i in range(vertexCount-2):
            #faces = ([i+i%2],[i-i%2+1],[i+2])
            fa += 1
            fb += 1
            fc += 1
            faces.append([fa,fb,fc])
        f.seek(2, 1)
        uvcount = unpack("b", f.read(1))[0]
        f.seek(1,1)
        for i in range(uvcount):
            ux = unpack("<h", f.read(2))[0] / 4096.0
            uy = unpack("<h", f.read(2))[0] / 4096.0
            uvs.append([ux,uy])
        f.seek(2, 1)
        rgbacount = unpack("b", f.read(1))[0]
        f.seek(1,1)
        for c in range(rgbacount):
            r = unpack("B", f.read(1))[0] / 127.0
            g = unpack("B", f.read(1))[0] / 127.0
            b = unpack("B", f.read(1))[0] / 127.0
            a = unpack("B", f.read(1))[0] / 127.0
            rgba.append([r,g,b,a])

        BSDF = "Principled BSDF"
        meshID = len(bpy.data.objects) 
        mesh = bpy.data.meshes.new("dragonjan")
        mesh.from_pydata(vertices, [], faces)
        object = bpy.data.objects.new("dragonjan", mesh)
        bpy.context.collection.objects.link(object)
        bpy.data.materials.new(name="dragonjan_materials")
        mesh.vertex_colors.new()
            
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

        index=0
        for vcol in mesh.vertex_colors[0].data:
            vcol.color = rgba[i]
            index+=i

def get_2ndobjects_with_uvs_and_rgba(f, fa=-1,fb=0,fc=1,vertices=[], faces=[], normals=[], uvs=[], rgba=[], chunks=0, paddingWhere=0):
    f.seek(0)
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
            nz = unpack("<f", f.read(4))[0]
            vertices.append([vx,vy,vz])
            normals.append([nz,nz,nz])
        for i in range(vertexCount-2):
            fa += 1
            fb += 1
            fc += 1
            faces.append([fa,fb,fc])
        f.seek(6, 1)
        uvcount = unpack("b", f.read(1))[0]
        f.seek(1,1)
        for i in range(uvcount):
            ux = unpack("<h", f.read(2))[0] / 4096.0
            uy = unpack("<h", f.read(2))[0] / 4096.0
            uvs.append([ux,uy])
        f.seek(6, 1)
        rgbacount = unpack("b", f.read(1))[0]
        f.seek(1,1)
        for c in range(rgbacount):
            r = unpack("B", f.read(1))[0] / 127.0
            g = unpack("B", f.read(1))[0] / 127.0
            b = unpack("B", f.read(1))[0] / 127.0
            a = unpack("B", f.read(1))[0] / 127.0
            rgba.append([r,g,b,a])

        name=0
        BSDF = "Principled BSDF"
        meshID = len(bpy.data.objects) 
        mesh = bpy.data.meshes.new("dragonjan")
        mesh.from_pydata(vertices, [], faces)
        object = bpy.data.objects.new("dragonjan", mesh)
        bpy.context.collection.objects.link(object)
        mesh.normals_split_custom_set_from_vertices(normals)
        bpy.data.materials.new(name)
        mesh.vertex_colors.new(name=vmesh)
            
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

        index=0
        for vcol in mesh.vertex_colors[0].data:
            vcol.color = rgba[i]
            index+=i

def get_1stobjects_with_uvs_and_rgba(f, fa=-1,fb=0,fc=1,vertices=[], faces=[], normals=[], uvs=[], rgba=[], chunks=0, paddingWhere=0):
    f.seek(0)
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
            nz = unpack("<f", f.read(4))[0]
            vertices.append([vx,vy,vz])
            normals.append([nz,nz,nz])
        for i in range(vertexCount-2):
            fa += 1
            fb += 1
            fc += 1
            faces.append([fa,fb,fc])
        f.seek(6, 1)
        uvcount = unpack("b", f.read(1))[0]
        f.seek(1,1)
        for i in range(uvcount):
            ux = unpack("<h", f.read(2))[0] / 4096.0
            uy = unpack("<h", f.read(2))[0] / 4096.0
            f.seek(4,1)
            uvs.append([ux,uy])
        f.seek(6, 1)
        rgbacount = unpack("b", f.read(1))[0]
        f.seek(1,1)
        for c in range(rgbacount):
            r = unpack("B", f.read(1))[0] / 127.0
            g = unpack("B", f.read(1))[0] / 127.0
            b = unpack("B", f.read(1))[0] / 127.0
            a = unpack("B", f.read(1))[0] / 127.0
            rgba.append([r,g,b,a])

        name = 0
        BSDF = "Principled BSDF"
        meshID = len(bpy.data.objects) 
        mesh = bpy.data.meshes.new("dragonjan")
        mesh.from_pydata(vertices, [], faces)
        object = bpy.data.objects.new("dragonjan", mesh)
        bpy.context.collection.objects.link(object)
        mesh.normals_split_custom_set_from_vertices(normals)
        bpy.data.materials.new("dragonjan")
        meshC = mesh.vertex_colors.new()
            
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

        index=0
        for vcol in mesh.vertex_colors[0].data:
            vcol.color = rgba[i]
            index+=i

        mesh.vertex_colors.active = meshC

def ColorReach(f, colors=[]):
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
            colors.append([red,green,blue,alpha])

        index=0
        for vcol in obdata.vertex_colors[0].data:
            vcol.color = colors[i]
            index+=i

def DIFOffset_one(f, vertices=[], faces=[], fa=-1, fb=0, fc=1):
    f.seek(0)
    QTRead = f.read()
    QTLoc = QTRead.find(b"\x03\x01\x00\x01\x01\x00\x00\x05")
    if QTRead != 0:
        f.seek(QTLoc, 0)
        f.seek(10,1)
        VertexCount = unpack("B", f.read(1))[0]
        Decimal = unpack("B", f.read(1))[0]
        for i in range(VertexCount):
            vx = unpack("<h", f.read(2))[0] / 4096.0
            vy = unpack("<h", f.read(2))[0] / 4096.0
            vz = unpack("<h", f.read(2))[0] / 4096.0
            nz = unpack("<h", f.read(2))[0] / 4096.0
            vertices.append([vx,vy,vz])
        for i in range(VertexCount-2):
            fa += 1
            fb += 1
            fc += 1
            faces.append([fa,fb,fc])
    
    mesh = bpy.data.meshes.new("dragonjan")
    mesh.from_pydata(vertices, [], faces)
    object = bpy.data.objects.new("dragonjan", mesh)
    bpy.context.collection.objects.link(object)

def FinalUnknownNormalChunk(f, vertices=[], faces=[], normals=[], fa=-3, fb=-2,fc=-1):
    f.seek(0)
    while 1:
        Chunk = f.read(4)
        if Chunk == b"\x03\x01\x00\x01":
            f.seek(2,1)
            VertexCount = unpack("B", f.read(1))[0]
            clump = unpack("B", f.read(1))[0]
            if VertexCount == 3:
                
                for i in range(VertexCount):
                    vx = unpack("<f", f.read(4))[0]
                    vy = unpack("<f", f.read(4))[0]
                    vz = unpack("<f", f.read(4))[0]
                    nz = unpack("<f", f.read(4))[0]
                    vertices.append([vx,vy,vz])
                for i in range(VertexCount-2):
                    fa += 1 * 3
                    fb += 1 * 3
                    fc += 1 * 3
                    faces.append([fa,fb,fc])
            
        elif Chunk == b"SST0":
            break

    mesh = bpy.data.meshes.new("dragonjan")
    mesh.from_pydata(vertices, [], faces)
    object = bpy.data.objects.new("dragonjan", mesh)
    bpy.context.collection.objects.link(object)



def FinalUnknownChunk(f, VCountThree=3, vertices=[], faces=[], normals=[], fa=-4, fb=-3,fc=-2,fa_m=-3,fb_m=-2,fc_m=-1):
    f.seek(0)
    while 1:
        Chunk = f.read(4)
        if Chunk == b"\x03\x01\x00\x01":
            f.seek(2,1)
            VertexCount = unpack("B", f.read(1))[0]
            clump = unpack("B", f.read(1))[0]
            for i in range(VertexCount):
                vx = unpack("<f", f.read(4))[0]
                vy = unpack("<f", f.read(4))[0]
                vz = unpack("<f", f.read(4))[0]
                nz = unpack("<f", f.read(4))[0]
                vertices.append([vx,vy,vz])
                normals.append([0,0, nz])
            for i in range(VertexCount*2//9):
                fa_m += 1 * 4
                fb_m += 1 * 4
                fc_m += 1 * 4
                fa += 1 * 4
                fb += 1 * 4
                fc += 1 * 4
                faces.append([fb_m,fa_m,fc_m])
                faces.append([fa,fb,fc])
            
        elif Chunk == b"SST0":
            break
    
    BSDF = "Principled BSDF"
    vmesh = "dragonjanCol"
    meshID = len(bpy.data.objects)
    mesh = bpy.data.meshes.new("dragonjan")
    mesh.from_pydata(vertices, [], faces)
    object = bpy.data.objects.new("dragonjan", mesh)
    mesh.normals_split_custom_set_from_vertices(normals)
    bpy.context.collection.objects.link(object)
    mesh.vertex_colors.new(name=vmesh)

    for fac in mesh.polygons:
        fac.use_smooth = True

    vindex = 0
    for vertex in mesh.vertices:
        vertex.normal = normals[vindex]
        vindex += 1

    NU_MIX_MODE = 'ShaderNodeMixRGB'
    NU_RGBA_VERT = 'ShaderNodeVertexColor'
    MaterialName = "dragonjan Material"

    name=0

    obj = bpy.data.objects[name]
    mats = bpy.data.materials.new("dragonjan Material")
    obj.data.materials.append(mats)

    previous_mix = None
    previous_rgba = None

    for i, mat in enumerate(bpy.data.materials):
        mat.use_nodes = True
        bpy.data.materials[MaterialName].node_tree.nodes[BSDF].inputs[7].default_value = 0
        bpy.data.materials[MaterialName].node_tree.nodes[BSDF].inputs[9].default_value = 1
        #bpy.data.node.add_search(use_transform=True, node_item=items)
        mat.blend_method = "HASHED"
        mix = mat.node_tree.nodes.new(NU_MIX_MODE)
        rgbaV = mat.node_tree.nodes.new(NU_RGBA_VERT)
        mat.node_tree.nodes["Mix"].blend_type = 'MULTIPLY'
        mat.node_tree.nodes["Mix"].inputs[0].default_value = 1
        bpy.data.materials[MaterialName].node_tree.nodes["Vertex Color"].layer_name = vmesh
        nodes = mat.node_tree.nodes
        links = mat.node_tree.links
        principled = nodes.get('Principled BSDF')
        mixer = nodes.get("ShaderNodeVertexColor")
        for i in range(1):
            mix.location.x = -300
            if previous_mix:
                links.new(previous_mix.outputs[0], mix.inputs[0])
        previous_mix = mix
        links.new(mix.outputs[0], principled.inputs[0])
        for i in range(1):
            rgbaV.location.x = -300
            rgbaV.location.y = -300
            if previous_rgba:
                links.new(previous_rgba.outputs[0], rgbaV.inputs[0])
        previous_rgba = rgbaV
    links.new(rgbaV.outputs[1], principled.inputs[21])
    links.new(rgbaV.outputs[0], mix.inputs[1])
    
    #objs = bpy.data.objects["dragonjan"]
    #bpy.context.view_layer.objects.active = objs
    #bpy.ops.object.mode_set(mode='OBJECT', toggle=False)
    #bpy.ops.object.select_all(action='SELECT')"""
            
                

#don't use this just quite yet
def ExtractTextures(f, filepath):
    while 1:
        TexChunk = f.read(4)
        if TexChunk == b"TST0":
            TSTSize = unpack("<I", f.read(4))[0]
            TextureCount = unpack("<I", f.read(4))[0]
            unk = unpack("<I", f.read(4))[0]
            for i in range(TextureCount):
                pass
            bpy.data.images.new(name="dragonjan textures", width=width_, height=_, alpha=True)
        elif TexChunk == b"MS00":
            break
        
"""def dumpGSCTexture(f):
    f.seek(0)
    while 1:
        TexChunk = f.read(4)
        if TexChunk == 0x80800000:
            f.seek(2,1)
            pixlen = unpack("<I", f.read(4))[0] // 2
            f.seek(6,1)
            for i in range(pixlen//4):
                r = unpack("B", f.read(1))[0]
                g = unpack("B", f.read(1))[0]
                b = unpack("B", f.read(1))[0]
                a = unpack("B", f.read(1))[0] * 2
        break"""
        
"""f.seek(0)
dumpOneRead = f.read()
dumpReadOne = dumpOneRead.find(b"\x80\x80\x00\x00\x00\x00")
if dumpOneRead != 0:
    f.seek(dumpReadOne, 0)
    f.seek(-32,1)
    w = unpack("<I", f.read(4))[0] * 2
    h = unpack("<I", f.read(4))[0] * 2
    image_test = bpy.data.images.new(name="GSC Image", width=w, height=h, alpha=True)
    num_Pixels = len(image_test.pixels)
    f.seek(30, 1)
    pixellen = unpack("<I", f.read(4))[0] // 2
    f.seek(6,1)
    def grid(x,y):
        return x + w*y
    def drawPixel(x,y, R,G,B,A):

        pixelNumber = grid(x,y) * 4
    


        image_test.pixels[pixelNumber] = R
        image_test.pixels[pixelNumber+1] = G
        image_test.pixels[pixelNumber+2] = B
        image_test.pixels[pixelNumber+3] = A#
    for i in range(w//4):
        for k in range(h//4):
            drawPixel(i,k,unpack("B", f.read(1))[0]/255,unpack("B", f.read(1))[0]/255,unpack("B", f.read(1))[0]/255,unpack("B", f.read(1))[0]/127)"""
def wholeChunk2(f, vertices=[]):
    f.seek(0)
    QTRead = f.read()
    QTLoc = QTRead.find(b"\x03\x01\x00\x01\x01\x00\x00\x05")
    if QTRead != 0:
        f.seek(QTLoc, 0)
        f.seek(10,1)
        
        VertexCount = unpack("B", f.read(1))[0]
        Decimal = unpack("B", f.read(1))[0]
        for i in range(1):
            f.seek(4,1)
            vx = unpack("<f", f.read(2))[0] / 4096.0
            vy = unpack("<f", f.read(2))[0] / 4096.0
            vz = unpack("<f", f.read(2))[0] / 4096.0
            vertices.append([vx,vy,vz])
    mesh = bpy.data.meshes.new("dragonjan")
    mesh.from_pydata(vertices, [], [])
    object = bpy.data.objects.new("dragonjan", mesh)
    bpy.context.collection.objects.link(object)


def wholeChunk1(f, vertices=[], faces=[], normals=[], uvs=[], colors=[], fa=-1, fb=0, fc=1):
    f.seek(0)
    Material_ID = ""
    mat = bpy.data.materials.new(name=Material_ID)
    bpy.data.materials.get ("Material")
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
            vertexSize=0
            f.seek(2,1)
            vertexCount = unpack("B", f.read(1))[0]
            f.seek(1,1)
            for i in range(vertexCount):
                vx = unpack("<f", f.read(4))[0]
                vy = unpack("<f", f.read(4))[0]
                vz = unpack("<f", f.read(4))[0]
                nz = unpack("<f", f.read(4))[0] #normals
                if vy == 626239069825399828521156608.000000:
                    vy -=626239069825399828521156608.000000
                elif vy == 38335097425014816768.000000:
                    vy -= 38335097425014816768.000000
                elif vy == 623812068601110010234142720.000000:
                    vy -=623812068601110010234142720.000000
                if vz == 2504894888537322008696848384.000000:
                    vz -=2504894888537322008696848384.000000
                elif vz == 795473410667354881471283200.000000:
                    vz -= 795473410667354881471283200.000000
                elif vz == 626239069825399828521156608.000000:
                    vz -= 626239069825399828521156608.000000
                if vx == 2504894888537322008696848384.000000:
                    vx -=2504894888537322008696848384.000000
                elif vx == 38352131059152322560.000000:
                    vx -= 38352131059152322560.000000

                elif vx == 623812068601110010234142720.000000:
                    vx -= 623812068601110010234142720.000000
                vertices.append([vx,vy,vz])
                normals.append([nz,nz,nz])

            for i in range(vertexCount-2):
                fa+=1
                fb+=1
                fc+=1
                faces.append([fa,fb,fc])
        elif Chunk == b"SST0":
            break
        
    mesh = bpy.data.meshes.new("dragonjan")
    mesh.from_pydata(vertices, [], faces)
    object = bpy.data.objects.new("dragonjan", mesh)
    bpy.context.collection.objects.link(object)
    mesh.normals_split_custom_set_from_vertices(normals)
    bpy.data.materials["Material"].use_backface_culling = True
    objs = bpy.data.objects["dragonjan"]
    


"""def get_1stobjectspt3(f, vertices=[], faces=[], fa=-1, fb=0, fc=1):
    f.seek(0)
    wholemeshread = f.read()
    wholemeshfind = wholemeshread.find(b"\x03\x01\x00\x01\x03\x01")
    if wholemeshread != 0:
        f.seek(wholemeshfind, 0)
        f.seek(6, 1)
        vertexcount = unpack("b", f.read(1))[0]
        f.seek(1,1)
        for i in range(vertexcount):
            vx = unpack("<f", f.read(4))[0]
            vy = unpack("<f", f.read(4))[0]
            vz = unpack("<f", f.read(4))[0]
            nz = unpack("<f", f.read(4))[0]
            vertices.append([x,vy,vz])
        for i in range(vertexcount-2):
            fa +=1
            fb +=1
            fc +=1
            vertices.append([fa,fb,fc])
        f.seek(6, 1)
        uvcount = unpack("b", f.read(1))[0]
        f.seek(1,1)
        for i in range(uvcount):
            f.seek(4, 1)
        f.seek(6, 1)
        colorcount = unpack("b", f.read(1))[0]
        f.seek(1,1)
        for i in range(colorcount):
            f.seek(1,1)
            f.seek(1,1)
            f.seek(1,1)
            f.seek(1,1)
        mesh = bpy.data.meshes.new("dragonjan")
        mesh.from_pydata(vertices, [], faces)
        object = bpy.data.objects.new("dragonjan", mesh)
        bpy.context.collection.objects.link(object)
        mesh.vertex_colors.new(name="dragonjanCol")
        bpy.data.materials.new(name="default")
        uvtex = mesh.uv_layers.new()
        uvtex.name = 'dragonjanUV'
        for fac in mesh.polygons:
            fac.use_smooth = True
    else:
        raise Exception("that offset not found")"""

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
            uvs.append([ux,uy])
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
            uvs.append([ux, uy])
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
            uvs.append([ux, uy])
        obdata = bpy.context.object.data
        uv_tex = obdata.uv_layers.new()
        uv_layer = obdata.uv_layers[0].data
        vert_loops = {}
        for l in obdata.loops:
            vert_loops.setdefault(l.vertex_index, []).append(l.index)
        for i, coord in enumerate(uvs):
            for li in vert_loops[i]:
                uv_layer[li].uv = coord
            
            
def get_2ndobjects(f, vertices=[], chunks2=0, paddingWhere2=0, chunk2=0):
    f.seek(0)
    twoobjectsread = f.read()
    twoobjectfound = twoobjectsread.find(b"\x00\x00\x00\x00\x02\x80")
    if twoobjectsread != 0:
        f.seek(twoobjectfound,0)
        f.seek(chunk2, 1)
        f.seek(6, 1)
        vertexcount = unpack("b", f.read(1))[0]
        f.seek(1, 1)
        for i in range(vertexcount):
            f.seek(4,1)
            vx = unpack("<f", f.read(4))[0]
            vy = unpack("<f", f.read(4))[0]
            vz = unpack("<f", f.read(4))[0]
            nz = unpack("<f", f.read(4))[0]
            vertices.append([vx,vy,vz])
        mesh = bpy.data.meshes.new("dragonjan")
        mesh.from_pydata(vertices, [], [])
        object = bpy.data.objects.new("dragonjan", mesh)
        bpy.context.collection.objects.link(object)
        for fac in mesh.polygons:
            fac.use_smooth = True

def get_1stobjectspt2(f, fa=-1,fb=0,fc=1,vertices=[], faces=[]):
    f.seek(0)
    objectsread = f.read()
    objectfound = objectsread.find(b"\x03\x01\x00\x01\x03\x80")
    if objectsread != 0:
        f.seek(objectfound, 0)
        f.seek(6, 1)
        vertexcount = unpack("b", f.read(1))[0]
        f.seek(1, 1)
        for i in range(vertexcount):
            vx = unpack("<f", f.read(4))[0]
            vy = unpack("<f", f.read(4))[0]
            vz = unpack("<f", f.read(4))[0]
            nz = unpack("<f", f.read(4))[0]
            vertices.append([vx, vy, vz])
        for i in range(vertexcount-2):
            fa+=1
            fb+=1
            fc+=1
            faces.append([fa,fb,fc])
            
    BSDF = "Principled BSDF"
    vmesh = "dragonjanCol"
    meshID = len(bpy.data.objects)
    mesh = bpy.data.meshes.new("dragonjan")
    mesh.from_pydata(vertices, [], faces)
    object = bpy.data.objects.new("dragonjan", mesh)
    bpy.context.collection.objects.link(object)
    mesh.vertex_colors.new(name=vmesh)
    objs = bpy.data.objects["dragonjan"]
    bpy.context.view_layer.objects.active = objs
    bpy.ops.object.mode_set(mode='OBJECT', toggle=False)
    bpy.ops.object.select_all(action='SELECT')
    bpy.ops.transform.rotate(value=1.5708, orient_axis='X', orient_type='GLOBAL', orient_matrix=((1, 0, 0), (0, 1, 0), (0, 0, 1)), orient_matrix_type='GLOBAL', constraint_axis=(True, False, False), mirror=True, use_proportional_edit=False, proportional_edit_falloff='SMOOTH', proportional_size=1, use_proportional_connected=False, use_proportional_projected=False)
    bpy.ops.transform.rotate(value=3.14159, orient_axis='Z', orient_type='GLOBAL', orient_matrix=((1, 0, 0), (0, 1, 0), (0, 0, 1)), orient_matrix_type='GLOBAL', constraint_axis=(False, False, True), mirror=False, use_proportional_edit=False, proportional_edit_falloff='SMOOTH', proportional_size=1, use_proportional_connected=False, use_proportional_projected=False)
    bpy.ops.object.select_all(action='DESELECT')

    for fac in mesh.polygons:
        fac.use_smooth = True

    NU_MIX_MODE = 'ShaderNodeMixRGB'
    NU_RGBA_VERT = 'ShaderNodeVertexColor'
    MaterialName = "dragonjan Material"

    obj = bpy.data.objects["dragonjan"]
    mats = bpy.data.materials.new("dragonjan Material")
    obj.data.materials.append(mats)

    previous_mix = None
    previous_rgba = None

    for i, mat in enumerate(bpy.data.materials):
        mat.use_nodes = True
        bpy.data.materials[MaterialName].node_tree.nodes[BSDF].inputs[7].default_value = 0
        bpy.data.materials[MaterialName].node_tree.nodes[BSDF].inputs[9].default_value = 1
        #bpy.data.node.add_search(use_transform=True, node_item=items)
        mat.blend_method = "HASHED"
        mix = mat.node_tree.nodes.new(NU_MIX_MODE)
        rgbaV = mat.node_tree.nodes.new(NU_RGBA_VERT)
        mat.node_tree.nodes["Mix"].blend_type = 'MULTIPLY'
        mat.node_tree.nodes["Mix"].inputs[0].default_value = 1
        bpy.data.materials[MaterialName].node_tree.nodes["Vertex Color"].layer_name = vmesh
        nodes = mat.node_tree.nodes
        links = mat.node_tree.links
        principled = nodes.get('Principled BSDF')
        mixer = nodes.get("ShaderNodeVertexColor")
        for i in range(1):
            mix.location.x = -300
            if previous_mix:
                links.new(previous_mix.outputs[0], mix.inputs[0])
        previous_mix = mix
        links.new(mix.outputs[0], principled.inputs[0])
        for i in range(1):
            rgbaV.location.x = -300
            rgbaV.location.y = -300
            if previous_rgba:
                links.new(previous_rgba.outputs[0], rgbaV.inputs[0])
        previous_rgba = rgbaV
    links.new(rgbaV.outputs[1], principled.inputs[21])
    links.new(rgbaV.outputs[0], mix.inputs[1])
    

def get_1stobjects(f, fa=-1,fb=0,fc=1,vertices=[], faces=[], uvs=[], rgba=[], chunks=0, paddingWhere=0):
    f.seek(0)
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
            nz = unpack("<f", f.read(4))[0]
            vertices.append([vx,vy,vz])
        for i in range(vertexCount-2):
            fa += 1
            fb += 1
            fc += 1
            faces.append([fa,fb,fc])
        f.seek(6, 1)
        uvcount = unpack("b", f.read(1))[0]
        f.seek(1,1)
        for i in range(uvcount):
            f.seek(4,1)
            ux = unpack("h", f.read(2))[0] / 4096.0
            uy = unpack("h", f.read(2))[0] / 4096.0
            uvs.append([ux,uy])
        f.seek(6, 1)
        rgbacount = unpack("b", f.read(1))[0]
        f.seek(1,1)
        for c in range(rgbacount):
            r = unpack("B", f.read(1))[0] / 127.0
            g = unpack("B", f.read(1))[0] / 127.0
            b = unpack("B", f.read(1))[0] / 127.0
            a = unpack("B", f.read(1))[0] / 127.0
            rgba.append([r,g,b,a])
            
        MaterialName=0
        BSDF = "Principled BSDF"        
        mesh = bpy.data.meshes.new("dragonjan")
        mesh.from_pydata(vertices, [], faces)
        object = bpy.data.objects.new("dragonjan", mesh)
        bpy.context.collection.objects.link(object)
        #mesh.vertex_colors.new(name="dragonjanCol")
        bpy.data.materials.new(name="dragonjan_materials")
        """for face in mesh.vertex_colors[0].data:
            face.color = rgba[rgbacount]
            face.color = rgba[rgbacount]
            face.color = rgba[rgbacount]
            c+=1"""
        #bpy.data.materials[MaterialName].node_tree.nodes[BSDF].inputs[7].default_value = 0
        #bpy.data.materials[MaterialName].node_tree.nodes[BSDF].inputs[9].default_value = 1
        #MaterialName+=1 # the reason because there a dots stroke
            
        for fac in mesh.polygons:
            fac.use_smooth = True
        
        


def get_INST(f,emptytime=[]):
    f.seek(0)
    INSTread = f.read()
    INSTfound = INSTread.find(b"\x49\x4E\x53\x54")
    if INSTread != 0:
        f.seek(INSTfound, 0)
        f.seek(8,1)
        INSTS = unpack("<i", f.read(4))[0]
        INSTsize = unpack("<i", f.read(4))[0]
        INSTcount = unpack("<i", f.read(4))[0]
        unk01 = unpack("<i", f.read(4))[0]
        for i in range(INSTcount):
            INSTScaleX = unpack("<f", f.read(4))[0]
            f.seek(16,1)
            INSTScaleY = unpack("<f", f.read(4))[0]
            f.seek(16,1)
            INSTScaleZ = unpack("<f", f.read(4))[0]
            f.seek(4,1)
            INSTxTrans = unpack("<f", f.read(4))[0]
            INSTyTrans = unpack("<f", f.read(4))[0]
            INSTzTrans = unpack("<f", f.read(4))[0]
            INSTUNKFloat = unpack("<f", f.read(4))[0]
            f.seek(16, 1)
            bpy.ops.object.empty_add(type='CUBE', align='WORLD', location=([INSTxTrans, INSTyTrans,INSTzTrans]), scale=([INSTScaleX, INSTScaleY, INSTScaleZ]))
    else:
        raise Exception("no INST found")

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
            bpy.ops.object.empty_add(type='CUBE', align='WORLD', location=([SPECxTrans, SPECyTrans,SPECzTrans]), scale=([SPECScaleX, SPECScaleY, SPECScaleZ]))

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
            bpy.ops.object.empty_add(type='CUBE', align='WORLD', location=([IABLxTrans, IABLyTrans,IABLzTrans]), scale=([IABLScaleX, IABLScaleY, IABLScaleZ]))

def get_Animation_LIBRARY(f):
    f.seek(0)
    ALIBread = f.read()
    ALIBsearch = ALIBread.find(b"\x41\x4C\x49\x42")
    if ALIBread != 0:
        f.seek(ALIBsearch,0)
        ALIBS = unpack("<i", f.read(4))[0]
        ALIBSize = unpack("<i", f.read(4))[0]
        ALIBcount = unpack("<i", f.read(4))[0]
        unk01 = unpack("<i", f.read(4))[0]
        ALIBframecount = unpack("<i", f.read(4))[0]
        f.seek(4,1)
        f.seek(4,1)
        f.seek(20, 1)
        keyframecount = unpack("<i", f.read(4))[0]
        bpy.context.scene.frame_current=1
        bpy.context.scene.frame_start=1
        bpy.context.scene.frame_end=ALIBframecount
        #keyframes not available yet due lack of incompleted random bytes with chunks
        

def get_splineset(f, ea=-1, eb=0, vertices=[], edges=[]):
    f.seek(0)
    splinesetread = f.read()
    splinesearch = splinesetread.find(b"\x53\x53\x54\x30")
    if splinesetread != 0:
        f.seek(splinesearch, 0)
        SST0S = unpack("i", f.read(4))[0]
        SST0Size = unpack("i",f.read(4))[0]
        SST0E1 = unpack("i",f.read(4))[0]
        SplineTotalSize = unpack("i",f.read(4))[0]
        SST0E2 = unpack("i",f.read(4))[0]
        f.seek(4, 1)
        for i in range(SST0E2):
            vx = unpack("<f",f.read(4))[0]
            vy = unpack("<f",f.read(4))[0]
            vz = unpack("<f",f.read(4))[0]
            vertices.append([vx, vy, vz])
        for e in range(SST0E2-1):
            ea += 1
            eb += 1
            edges.append([ea,eb])
        mesh = bpy.data.meshes.new("SplineSet")
        mesh.from_pydata(vertices, edges, [])
        object = bpy.data.objects.new("SplineSet", mesh)
        bpy.context.collection.objects.link(object)
    else:
        raise Exception("no spline found")

def get_BoundsSet1(f, ea=-1, eb=0, vertices=[], bounds=[]):
    f.seek(0)
    boundssetread = f.read()
    boundssearch = boundssetread.find(b"\x42\x4E\x44\x53")
    if boundssetread != 0:
        f.seek(boundssearch, 0)
        BNDS = unpack("<I", f.read(4))[0]
        BNDS_Size = unpack("<I", f.read(4))[0]
        BNDS_Ver = unpack("<I", f.read(4))[0]
        BNDS_Count = unpack("<I", f.read(4))[0]
        unk01 = unpack("<I", f.read(4))[0]
        unk02 = unpack("<I", f.read(4))[0]
        for i in range(BNDS_Count):
            vx = unpack("<f", f.read(4))[0]
            vy = unpack("<f", f.read(4))[0]
            vz = unpack("<f", f.read(4))[0]
            f.seek(36,1)
            vertices.append([vx,vy,vz])
            
        for i in range(BNDS_Count-1):
            ea+=1
            eb+=1
            bounds.append([ea,eb])

        mesh = bpy.data.meshes.new("dragonjan Bounds")
        mesh.from_pydata(vertices, bounds, [])
        object = bpy.data.objects.new("dragonjan Bounds", mesh)
        bpy.context.collection.objects.link(object)

def indivitualMesh_1(f, filepath):
    vertices=[]
    faces=[]
    f.seek(0)
    fa=-4
    fb=-3
    fc=-2
    fa_m=-3
    fb_m=-2
    fc_m=-1
    while 1:
        Chunk = f.read(4)
        if Chunk == b"\x03\x01\x00\x01":
            f.seek(2,1)
            vertexcount = unpack("B", f.read(1))[0]
            f.seek(1,1)
            for i in range(vertexcount):
                vx = unpack("<f", f.read(4))[0]
                vy = unpack("<f", f.read(4))[0]
                vz = unpack("<f", f.read(4))[0]
                nz = unpack("<f", f.read(4))[0]
                vertices.append([vx,vy,vz])
        elif Chunk == b"SST0":
            break

    for i in range(1200):
        fa+=1*4
        fb+=1*4
        fc+=1*4
        fa_m+=1*4
        fb_m+=1*4
        fc_m+=1*4
        faces.append([fa,fb,fc])
        faces.append([fa_m,fb_m,fc_m])

    mesh = bpy.data.meshes.new(os.path.basename(filepath))
    mesh.from_pydata(vertices, [], faces)
    object = bpy.data.objects.new(os.path.basename(filepath), mesh)
    bpy.context.collection.objects.link(object)
            
        
        

def parse_gsc(filepath, Triangle_Strips_part3=False, Triangle_Strips_with_uvs_and_rgba=1, Triangle_StripsTwo=False, Triangle_Strips=False, WholeMassiveOne=False, ONE_CHUNK_OFFSET1=False, ONE_CHUNK_OFFSET1PT2=False, ONE_CHUNK_OFFSET2=False, SST=False, SPEC=False, INST=False, IABL=False, BoundingSet=False, SelectOnlyUVMesh=False, SelectOnly2ndUVMesh=False, SelectOnly3rdUVMesh=False, Triangles=False, Norm_Triangles=False, RGBAColors=False):
    with open(filepath, "rb") as f:
        
        if Triangle_Strips_part3:
            offset_0x03010001010000050380(f, vertices=[], faces=[], normals=[], fa=-1, fb=0, fc=1)
        if Triangle_Strips:
            wholeChunk1(f, vertices=[], faces=[], normals=[], uvs=[], colors=[], fa=-1, fb=0, fc=1)
        if WholeMassiveOne:
            wholeChunk2(f, vertices=[])
        if ONE_CHUNK_OFFSET1:
            get_1stobjects(f, fa=-1,fb=0,fc=1,vertices=[], faces=[], uvs=[], rgba=[], chunks=0, paddingWhere=0)
        if ONE_CHUNK_OFFSET1PT2:
            get_1stobjectspt2(f, fa=-1,fb=0,fc=1,vertices=[], faces=[])
        if ONE_CHUNK_OFFSET2:
            get_2ndobjects(f, vertices=[], chunks2=0, paddingWhere2=0, chunk2=0)
        if INST:
            get_INST(f,emptytime=[])
        if SPEC:
            get_SPEC(f, emptytime2=[])
        if IABL:
            get_SPEC_ANIMATION_BLOCK(f, emptytime3=[])
        if SST:
            get_splineset(f, ea=-1, eb=0, vertices=[], edges=[])
        if SelectOnlyUVMesh:
            selectUV(f, uvs=[])
        if SelectOnly2ndUVMesh:
            select2ndUV(f, uvs=[])
        if SelectOnly3rdUVMesh:
            selectUVThird(f, uvs=[])
        if BoundingSet:
            get_BoundsSet1(f, ea=-1, eb=0, vertices=[], bounds=[])
        if Triangles:
            FinalUnknownChunk(f, VCountThree=3, vertices=[], faces=[], normals=[], fa=-4, fb=-3,fc=-2,fa_m=-3,fb_m=-2,fc_m=-1)
        if Norm_Triangles:
            FinalUnknownNormalChunk(f, vertices=[], faces=[], normals=[], fa=-3, fb=-2,fc=-1)
        if Triangle_StripsTwo:
            DIFOffset_one(f, vertices=[], faces=[], fa=-1, fb=0, fc=1)
        if RGBAColors:
            ColorReach(f, colors=[])
        if Triangle_Strips_with_uvs_and_rgba == 1:
            get_1stobjects_with_uvs_and_rgba(f, fa=-1,fb=0,fc=1,vertices=[], faces=[], normals=[], uvs=[], rgba=[], chunks=0, paddingWhere=0)
        if Triangle_Strips_with_uvs_and_rgba == 2:
            get_2ndobjects_with_uvs_and_rgba(f, fa=-1,fb=0,fc=1,vertices=[], faces=[], normals=[], uvs=[], rgba=[], chunks=0, paddingWhere=0)
        if Triangle_Strips_with_uvs_and_rgba == 3:
            get_3rdobjects_with_uvs_and_rgba(f, vertices=[], faces=[], normals=[], fa=-1, fb=0, fc=1, uvs=[], rgba=[], chunks=0, paddingWhere=0)



