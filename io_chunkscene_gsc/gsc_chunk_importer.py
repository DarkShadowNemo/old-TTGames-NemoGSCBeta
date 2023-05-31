from struct import pack, unpack
import os
import bpy
import bmesh
import math
            

def get_3rdobjects_with_uvs_and_rgba(f, vertices=[], faces=[], fa=-1, fb=0, fc=1, uvs=[], rgba=[], chunks=0, paddingWhere=0):
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

def get_2ndobjects_with_uvs_and_rgba(f, fa=-1,fb=0,fc=1,vertices=[], faces=[], uvs=[], rgba=[], chunks=0, paddingWhere=0):
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

        BSDF = "Principled BSDF"
        meshID = len(bpy.data.objects) 
        mesh = bpy.data.meshes.new("dragonjan")
        mesh.from_pydata(vertices, [], faces)
        object = bpy.data.objects.new("dragonjan", mesh)
        bpy.context.collection.objects.link(object)
        bpy.data.materials.new(name="dragonjan_materials")
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

def get_1stobjects_with_uvs_and_rgba(f, fa=-1,fb=0,fc=1,vertices=[], faces=[], uvs=[], rgba=[], chunks=0, paddingWhere=0):
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

        BSDF = "Principled BSDF"
        meshID = len(bpy.data.objects) 
        mesh = bpy.data.meshes.new("dragonjan")
        mesh.from_pydata(vertices, [], faces)
        object = bpy.data.objects.new("dragonjan", mesh)
        bpy.context.collection.objects.link(object)
        bpy.data.materials.new(name="dragonjan_materials")
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



def FinalUnknownChunk(f, VCountThree=3, vertices=[], faces=[], fa=-4, fb=-3,fc=-2,fa_m=-3,fb_m=-2,fc_m=-1):
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
            for i in range(VertexCount*2//9-2):
                fa_m += 1 * 4
                fb_m += 1 * 4
                fc_m += 1 * 4
                faces.append([fb_m,fa_m,fc_m])
            for i in range(VertexCount*2//9-2):
                fa += 1 * 4
                fb += 1 * 4
                fc += 1 * 4
                faces.append([fa,fb,fc])
            
        elif Chunk == b"SST0":
            break
    for a in bpy.context.screen.areas:
        if a.type == 'VIEW_3D':
            for s in a.spaces:
                if s.type == 'VIEW_3D':
                    s.clip_end = 400000
                    s.clip_start = 1
    
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


def wholeChunk1(f, vertices=[], faces=[], normals=[], fa=-1, fb=0, fc=1):
    f.seek(0)
    while 1:
        Chunk = f.read(4)
        if Chunk == b"\x03\x01\x00\x01":
            vertexSize=0
            f.seek(2,1)
            vertexCount = unpack("b", f.read(1))[0]
            clump = unpack("b", f.read(1))[0]
            FaceIndex = 0
            #todo fix messed up triangle strips WIP
            for i in range(vertexCount):
                vx = unpack("<f", f.read(4))[0]
                vy = unpack("<f", f.read(4))[0]
                vz = unpack("<f", f.read(4))[0]
                nz = unpack("<f", f.read(4))[0] #normals
                vertices.append([vx,vy,vz])
                normals.append([0,0,nz])

            for i in range(vertexCount-2):
                FaceIndex+=1
                fa+=1
                fb+=1
                fc+=1
                faces.append([fa,fb,fc])
            #https://stackoverflow.com/questions/51481077/python-removing-an-item-from-a-list-in-the-if-statement-condition
            """if len(faces) == 48570:
                #boing_01
                if faces.remove([47668,47669,47670]):
                    pass
                elif faces.remove([24337,24338,24339]):
                    pass
                elif faces.remove([24336,24337,24338]):
                    pass
                elif faces.remove([8505,8506,8507]):
                    pass
                elif faces.remove([207,208,209]):
                    pass
                elif faces.remove([3259,3260,3261]):
                    pass
                elif faces.remove([3258,3259,3260]):
                    pass
                elif faces.remove([1658,1659,1660]):
                    pass
                elif faces.remove([1659,1660,1661]):
                    pass
                elif faces.remove([43594, 43595, 43596]):
                    pass
                elif faces.remove([43595, 43596, 43597]):
                    pass
                elif faces.remove([43597, 43598, 43599]):
                    pass
                elif faces.remove([43596, 43597, 43598]):
                    pass
                elif faces.remove([43598, 43599, 43600]):
                    pass
                elif faces.remove([43600, 43601, 43602]):
                    pass
                elif faces.remove([43601, 43602, 43603]):
                    pass
                elif faces.remove([43602, 43603, 43604]):
                    pass
                elif faces.remove([43603, 43604, 43605]):
                    pass
                elif faces.remove([3251, 3252, 3253]):
                    pass
                elif faces.remove([3250, 3251, 3252]):
                    pass
                elif faces.remove([1648, 1649, 1650]):
                    pass
                elif faces.remove([1647, 1648, 1649]):
                    pass
                elif faces.remove([1650, 1651, 1652]):
                    pass
                elif faces.remove([1651, 1652, 1653]):
                    pass
                elif faces.remove([3257, 3258, 3259]):
                    pass
                elif faces.remove([3099, 3100, 3101]):
                    pass
                elif faces.remove([3098, 3099, 3100]):
                    pass
                elif faces.remove([3097, 3098, 3099]):
                    pass
                elif faces.remove([3256, 3257, 3258]):
                    pass
                elif faces.remove([3248, 3249, 3250]):
                    pass
                elif faces.remove([1499, 1500, 1501]):
                    pass
                elif faces.remove([1498, 1499, 1500]):
                    pass
                elif faces.remove([3096, 3097, 3098]):
                    pass
                elif faces.remove([13060, 13061, 13062]):
                    pass
                elif faces.remove([13063, 13064, 13065]):
                    pass
                elif faces.remove([13064, 13065, 13066]):
                    pass
                elif faces.remove([13059, 13060, 13061]):
                    pass
                elif faces.remove([14314, 14315, 14316]):
                    pass
                elif faces.remove([14315, 14316, 14317]):
                    pass
                elif faces.remove([14041, 14042, 14043]):
                    pass
                elif faces.remove([14042, 14043, 14044]):
                    pass
                elif faces.remove([14320, 14321, 14322]):
                    pass
                elif faces.remove([12491, 12492, 12493]):
                    pass
                elif faces.remove([12490, 12491, 12492]):
                    pass
                elif faces.remove([12486, 12487, 12488]):
                    pass
                elif faces.remove([13778, 13779, 13780]):
                    pass
                elif faces.remove([13777, 13778, 13779]):
                    pass
                elif faces.remove([32072, 32073, 32074]):
                    pass
                elif faces.remove([32073, 32074, 32075]):
                    pass
                elif faces.remove([15356, 15357, 15358]):
                    pass
                elif faces.remove([15355, 15356, 15357]):
                    pass
                elif faces.remove([15323, 15324, 15325]):
                    pass
                elif faces.remove([15322, 15323, 15324]):
                    pass"""
            if len(faces) == 6686:
                #luxo_04
                if faces.remove([3887,3888,3889]):
                    pass
                elif faces.remove([3888,3889,3890]):
                    pass
                elif faces.remove([4005,4006,4007]):
                    pass
                elif faces.remove([4006,4007,4008]):
                    pass
                elif faces.remove([3921,3922,3923]):
                    pass
                elif faces.remove([3964,3965,3966]):
                    pass
                elif faces.remove([3963,3964,3965]):
                    pass
                elif faces.remove([3922,3923,3924]):
                    pass
                elif faces.remove([3846,3847,3848]):
                    pass
                elif faces.remove([3845,3846,3847]):
                    pass
                elif faces.remove([3808,3809,3810]):
                    pass
                elif faces.remove([3807,3808,3809]):
                    pass
                elif faces.remove([3766,3767,3768]):
                    pass
                elif faces.remove([3765,3766,3767]):
                    pass
                elif faces.remove([4018,4019,4020]):
                    pass
                elif faces.remove([4017,4018,4019]):
                    pass
                elif faces.remove([4028,4029,4030]):
                    pass
                elif faces.remove([4029,4030,4031]):
                    pass
                elif faces.remove([1746,1747,1748]):
                    pass
                elif faces.remove([1747,1748,1749]):
                    pass
                elif faces.remove([1693,1694,1695]):
                    pass
                elif faces.remove([1692,1693,1694]):
                    pass
                elif faces.remove([1703,1704,1705]):
                    pass
                elif faces.remove([1704,1705,1706]):
                    pass
                elif faces.remove([1716,1717,1718]):
                    pass
                elif faces.remove([1717,1718,1719]):
                    pass
                elif faces.remove([1752,1753,1754]):
                    pass
                elif faces.remove([1753,1754,1755]):
                    pass
                elif faces.remove([1727,1728,1729]):
                    pass
                elif faces.remove([2839,2840,2841]):
                    pass
                elif faces.remove([1974,1975,1976]):
                    pass
                elif faces.remove([1633,1634,1635]):
                    pass
                elif faces.remove([2003,2004,2005]):
                    pass
                elif faces.remove([2741,2742,2743]):
                    pass
                elif faces.remove([1632,1633,1634]):
                    pass
                elif faces.remove([1673,1674,1675]):
                    pass
                elif faces.remove([1726,1727,1728]):
                    pass
                elif faces.remove([1672,1673,1674]):
                    pass
                elif faces.remove([1653,1654,1655]):
                    pass
                elif faces.remove([1652,1653,1654]):
                    pass
                elif faces.remove([2780,2781,2782]):
                    pass
                elif faces.remove([2800,2801,2802]):
                    pass
                elif faces.remove([2827,2828,2829]):
                    pass
                elif faces.remove([2828,2829,2830]):
                    pass
                elif faces.remove([2825,2826,2827]):
                    pass
                elif faces.remove([2824,2825,2826]):
                    pass
                elif faces.remove([2822,2823,2824]):
                    pass
                elif faces.remove([6247,6248,6249]):
                    pass
                elif faces.remove([2810,2811,2812]):
                    pass
                elif faces.remove([2821,2822,2823]):
                    pass
                elif faces.remove([2811,2812,2813]):
                    pass
                elif faces.remove([2781,2782,2783]):
                    pass
                elif faces.remove([6036,6037,6038]):
                    pass
                elif faces.remove([2760,2761,2762]):
                    pass
                elif faces.remove([2761,2762,2763]):
                    pass
                elif faces.remove([1993,1994,1995]):
                    pass
                elif faces.remove([2801,2802,2803]):
                    pass
                elif faces.remove([1973,1974,1975]):
                    pass
                elif faces.remove([2004,2005,2006]):
                    pass
                elif faces.remove([2740,2741,2742]):
                    pass
                elif faces.remove([2840,2841,2842]):
                    pass
                elif faces.remove([4171,4172,4173]):
                    pass
                elif faces.remove([4172,4173,4174]):
                    pass
                elif faces.remove([4421,4422,4423]):
                    pass
                elif faces.remove([4422,4423,4424]):
                    pass
                elif faces.remove([4080,4081,4082]):
                    pass
                elif faces.remove([4069,4070,4071]):
                    pass
                elif faces.remove([4070,4071,4072]):
                    pass
                elif faces.remove([4081,4082,4083]):
                    pass
                elif faces.remove([5850,5851,5852]):
                    pass
                elif faces.remove([5851,5852,5853]):
                    pass
                elif faces.remove([5853,5854,5855]):
                    pass
                elif faces.remove([5855,5856,5857]):
                    pass
                elif faces.remove([5053,5054,5055]):
                    pass
                elif faces.remove([5052,5053,5054]):
                    pass
                elif faces.remove([5050,5051,5052]):
                    pass
                elif faces.remove([5049,5050,5051]):
                    pass
                elif faces.remove([5048,5049,5050]):
                    pass
                elif faces.remove([5047,5048,5049]):
                    pass
                elif faces.remove([5046,5047,5048]):
                    pass
                elif faces.remove([5045,5046,5047]):
                    pass
                elif faces.remove([5044,5045,5046]):
                    pass
                elif faces.remove([5852,5853,5854]):
                    pass
                elif faces.remove([5758,5759,5760]):
                    pass
                elif faces.remove([6246,6247,6248]):
                    pass
                elif faces.remove([1970,1971,1972]):
                    pass
                elif faces.remove([1929,1930,1931]):
                    pass
                elif faces.remove([1928,1929,1930]):
                    pass
                elif faces.remove([1754,1755,1756]):
                    pass
                elif faces.remove([1968,1969,1970]):
                    pass
                elif faces.remove([1453,1454,1455]):
                    pass
                elif faces.remove([1454,1455,1456]):
                    pass
                elif faces.remove([1967,1968,1969]):
                    pass
                elif faces.remove([1913,1914,1915]):
                    pass
                elif faces.remove([1912,1913,1914]):
                    pass
                elif faces.remove([1824,1825,1826]):
                    pass
                elif faces.remove([1825,1826,1827]):
                    pass
                elif faces.remove([1934,1935,1936]):
                    pass
                elif faces.remove([1962,1963,1964]):
                    pass
                elif faces.remove([1961,1962,1963]):
                    pass
                elif faces.remove([1971,1972,1973]):
                    pass
                elif faces.remove([1777,1778,1779]):
                    pass
                elif faces.remove([6035,6036,6037]):
                    pass
                #elif faces.remove([6036,6037,6038]):
                    #pass
                elif faces.remove([6037,6038,6039]):
                    pass
                elif faces.remove([6038,6039,6040]):
                    pass
                elif faces.remove([6039,6040,6041]):
                    pass
                elif faces.remove([6040,6041,6042]):
                    pass
                elif faces.remove([6042,6043,6044]):
                    pass
                elif faces.remove([6041,6042,6043]):
                    pass
                elif faces.remove([6044,6045,6046]):
                    pass
                elif faces.remove([1893,1894,1895]):
                    pass
                elif faces.remove([1892,1893,1894]):
                    pass
                elif faces.remove([1782,1783,1784]):
                    pass
                elif faces.remove([1783,1784,1785]):
                    pass
                elif faces.remove([5055,5056,5057]):
                    pass
                elif faces.remove([5054,5055,5056]):
                    pass
                elif faces.remove([5757,5758,5759]):
                    pass
                elif faces.remove([1933,1934,1935]):
                    pass
                elif faces.remove([1776,1777,1778]):
                    pass
                elif faces.remove([1869,1870,1871]):
                    pass
                elif faces.remove([1868,1869,1870]):
                    pass
                elif faces.remove([1846,1847,1848]):
                    pass
                elif faces.remove([1804,1805,1806]):
                    pass
                elif faces.remove([1847,1848,1849]):
                    pass
                elif faces.remove([1805,1806,1807]):
                    pass
                elif faces.remove([1938,1939,1940]):
                    pass
                elif faces.remove([1939,1940,1941]):
                    pass
                elif faces.remove([1522,1523,1524]):
                    pass
                elif faces.remove([1523,1524,1525]):
                    pass
                elif faces.remove([1432,1433,1434]):
                    pass
                elif faces.remove([1431,1432,1433]):
                    pass
                elif faces.remove([1542,1543,1544]):
                    pass
                elif faces.remove([1543,1544,1545]):
                    pass
                elif faces.remove([1410,1411,1412]):
                    pass
                elif faces.remove([1409,1410,1411]):
                    pass
                elif faces.remove([1565,1566,1567]):
                    pass
                elif faces.remove([1566,1567,1568]):
                    pass
                elif faces.remove([1476,1477,1478]):
                    pass
                elif faces.remove([1497,1498,1499]):
                    pass
                elif faces.remove([1498,1499,1500]):
                    pass
                elif faces.remove([1475,1476,1477]):
                    pass
                elif faces.remove([1519,1520,1521]):
                    pass
                elif faces.remove([1520,1521,1522]):
                    pass
                elif faces.remove([1617,1618,1619]):
                    pass
                elif faces.remove([1618,1619,1620]):
                    pass
                elif faces.remove([1590,1591,1592]):
                    pass
                elif faces.remove([1589,1590,1591]):
                    pass
                elif faces.remove([1627,1628,1629]):
                    pass
                elif faces.remove([1624,1625,1626]):
                    pass
                elif faces.remove([1625,1626,1627]):
                    pass
                elif faces.remove([6164,6165,6166]):
                    pass
                elif faces.remove([1156,1157,1158]):
                    pass
                elif faces.remove([1155,1156,1157]):
                    pass
                elif faces.remove([6163,6164,6165]):
                    pass
                elif faces.remove([1151,1152,1153]):
                    pass
                elif faces.remove([6243,6244,6245]):
                    pass
                elif faces.remove([6244,6245,6246]):
                    pass
                elif faces.remove([1215,1216,1217]):
                    pass
                elif faces.remove([6238,6239,6240]):
                    pass
                elif faces.remove([1216,1217,1218]):
                    pass
                elif faces.remove([6239,6240,6241]):
                    pass
                elif faces.remove([6232,6233,6234]):
                    pass
                elif faces.remove([6231,6232,6233]):
                    pass
                elif faces.remove([6223,6224,6225]):
                    pass
                elif faces.remove([6222,6223,6224]):
                    pass
                elif faces.remove([1228,1229,1230]):
                    pass
                elif faces.remove([1227,1228,1229]):
                    pass
                elif faces.remove([1596,1597,1598]):
                    pass
                elif faces.remove([1595,1596,1597]):
                    pass
                elif faces.remove([1620,1621,1622]):
                    pass
                elif faces.remove([1126,1127,1128]):
                    pass
                elif faces.remove([1127,1128,1129]):
                    pass
                elif faces.remove([1621,1622,1623]):
                    pass
                elif faces.remove([1628,1629,1630]):
                    pass
                elif faces.remove([6126,6127,6128]):
                    pass
                elif faces.remove([6125,6126,6127]):
                    pass
                elif faces.remove([1118,1119,1120]):
                    pass
                elif faces.remove([1119,1120,1121]):
                    pass
                elif faces.remove([6128,6129,6130]):
                    pass
                elif faces.remove([6129,6130,6131]):
                    pass
                elif faces.remove([6112,6113,6114]):
                    pass
                elif faces.remove([1105,1106,1107]):
                    pass
                elif faces.remove([1106,1107,1108]):
                    pass
                elif faces.remove([6113,6114,6115]):
                    pass
                elif faces.remove([6174,6175,6176]):
                    pass
                elif faces.remove([1166,1167,1168]):
                    pass
                elif faces.remove([6173,6174,6175]):
                    pass
                elif faces.remove([1165,1166,1167]):
                    pass
                elif faces.remove([6142,6143,6144]):
                    pass
                elif faces.remove([1140,1141,1142]):
                    pass
                elif faces.remove([6141,6142,6143]):
                    pass
                elif faces.remove([1139,1140,1141]):
                    pass
                elif faces.remove([6103,6104,6105]):
                    pass
                elif faces.remove([1096,1097,1098]):
                    pass
                elif faces.remove([6102,6103,6104]):
                    pass
                elif faces.remove([1095,1096,1097]):
                    pass
                elif faces.remove([6181,6182,6183]):
                    pass
                elif faces.remove([1173,1174,1175]):
                    pass
                elif faces.remove([6182,6183,6184]):
                    pass
                elif faces.remove([1174,1175,1176]):
                    pass
                elif faces.remove([6105,6106,6107]):
                    pass
                elif faces.remove([1098,1099,1100]):
                    pass
                elif faces.remove([6106,6107,6108]):
                    pass
                elif faces.remove([1099,1100,1101]):
                    pass
                elif faces.remove([6229,6230,6231]):
                    pass
                elif faces.remove([6228,6229,6230]):
                    pass
                elif faces.remove([6095,6096,6097]):
                    pass
                elif faces.remove([1088,1089,1090]):
                    pass
                elif faces.remove([6096,6097,6098]):
                    pass
                elif faces.remove([6089,6090,6091]):
                    pass
                elif faces.remove([6200,6201,6202]):
                    pass
                elif faces.remove([1193,1194,1195]):
                    pass
                elif faces.remove([6201,6202,6203]):
                    pass
                elif faces.remove([1194,1195,1196]):
                    pass
                elif faces.remove([6226,6227,6228]):
                    pass
                elif faces.remove([6225,6226,6227]):
                    pass
                elif faces.remove([3764,3765,3766]):
                    pass
                elif faces.remove([3311,3312,3313]):
                    pass
                elif faces.remove([3312,3313,3314]):
                    pass
                elif faces.remove([3401,3402,3403]):
                    pass
                elif faces.remove([3402,3403,3404]):
                    pass
                elif faces.remove([3172,3173,3174]):
                    pass
                elif faces.remove([2936,2937,2938]):
                    pass
                elif faces.remove([3173,3174,3175]):
                    pass
                elif faces.remove([2937,2938,2939]):
                    pass
                elif faces.remove([3277,3278,3279]):
                    pass
                elif faces.remove([3041,3042,3043]):
                    pass
                elif faces.remove([3276,3277,3278]):
                    pass
                elif faces.remove([3040,3041,3042]):
                    pass
                elif faces.remove([3289,3290,3291]):
                    pass
                elif faces.remove([3676,3677,3678]):
                    pass
                elif faces.remove([3675,3676,3677]):
                    pass
                elif faces.remove([3730,3731,3732]):
                    pass
                elif faces.remove([3742,3743,3744]):
                    pass
                elif faces.remove([1234,1235,1236]):
                    pass
                elif faces.remove([1233,1234,1235]):
                    pass
                elif faces.remove([460,461,462]):
                    pass
                elif faces.remove([459,460,461]):
                    pass
                elif faces.remove([484,485,486]):
                    pass
                elif faces.remove([485,486,487]):
                    pass
                elif faces.remove([98,99,100]):
                    pass
                elif faces.remove([119,120,121]):
                    pass
                elif faces.remove([120,121,122]):
                    pass
                elif faces.remove([487,488,489]):
                    pass
                elif faces.remove([488,489,490]):
                    pass
                elif faces.remove([43,44,45]):
                    pass
                elif faces.remove([42,43,44]):
                    pass
                elif faces.remove([72,73,74]):
                    pass
                elif faces.remove([73,74,75]):
                    pass
                elif faces.remove([50,51,52]):
                    pass
                elif faces.remove([536,537,538]):
                    pass
                elif faces.remove([560,561,562]):
                    pass
                elif faces.remove([561,562,563]):
                    pass
                elif faces.remove([535,536,537]):
                    pass
                elif faces.remove([49,50,51]):
                    pass
                elif faces.remove([612,613,614]):
                    pass
                elif faces.remove([613,614,615]):
                    pass
                elif faces.remove([582,583,584]):
                    pass
                elif faces.remove([583,584,585]):
                    pass
                elif faces.remove([1028,1029,1030]):
                    pass
                elif faces.remove([1029,1030,1031]):
                    pass
                elif faces.remove([634,635,636]):
                    pass
                elif faces.remove([635,636,637]):
                    pass
                elif faces.remove([980,981,982]):
                    pass
                elif faces.remove([981,982,983]):
                    pass
                elif faces.remove([97,98,99]):
                    pass
                elif faces.remove([596,597,598]):
                    pass
                elif faces.remove([463,464,465]):
                    pass
                elif faces.remove([597,598,599]):
                    pass
                elif faces.remove([585,586,587]):
                    pass
                elif faces.remove([539,540,541]):
                    pass
                elif faces.remove([975,976,977]):
                    pass
                elif faces.remove([974,975,976]):
                    pass
                elif faces.remove([838,839,840]):
                    pass
                elif faces.remove([839,840,841]):
                    pass
                elif faces.remove([872,873,874]):
                    pass
                elif faces.remove([538,539,540]):
                    pass
                elif faces.remove([873,874,875]):
                    pass
                elif faces.remove([906,907,908]):
                    pass
                elif faces.remove([907,908,909]):
                    pass
                elif faces.remove([804,805,806]):
                    pass
                elif faces.remove([805,806,807]):
                    pass
                elif faces.remove([940,941,942]):
                    pass
                elif faces.remove([941,942,943]):
                    pass
                elif faces.remove([771,772,773]):
                    pass
                elif faces.remove([770,771,772]):
                    pass
                elif faces.remove([462,463,464]):
                    pass
                elif faces.remove([357,358,359]):
                    pass
                elif faces.remove([358,359,360]):
                    pass
                elif faces.remove([391,392,393]):
                    pass
                elif faces.remove([323,324,325]):
                    pass
                elif faces.remove([324,325,326]):
                    pass
                elif faces.remove([392,393,394]):
                    pass
                elif faces.remove([289,290,291]):
                    pass
                elif faces.remove([425,426,427]):
                    pass
                elif faces.remove([290,291,292]):
                    pass
                elif faces.remove([255,256,257]):
                    pass
                elif faces.remove([426,427,428]):
                    pass
                elif faces.remove([256,257,258]):
                    pass
                elif faces.remove([6052,6053,6054]):
                    pass
                elif faces.remove([1045,1046,1047]):
                    pass
                elif faces.remove([6053,6054,6055]):
                    pass
                elif faces.remove([1046,1047,1048]):
                    pass
                elif faces.remove([1373,1374,1375]):
                    pass
                elif faces.remove([1372,1373,1374]):
                    pass
                elif faces.remove([6046,6047,6048]):
                    pass
                elif faces.remove([1039,1040,1041]):
                    pass
                elif faces.remove([6045,6046,6047]):
                    pass
                elif faces.remove([1038,1039,1040]):
                    pass
                elif faces.remove([6066,6067,6068]):
                    pass
                elif faces.remove([1059,1060,1061]):
                    pass
                elif faces.remove([6065,6066,6067]):
                    pass
                elif faces.remove([1058,1059,1060]):
                    pass
                elif faces.remove([6074,6075,6076]):
                    pass
                elif faces.remove([1067,1068,1069]):
                    pass
                elif faces.remove([6073,6074,6075]):
                    pass
                elif faces.remove([1066,1067,1068]):
                    pass
                elif faces.remove([6048,6049,6050]):
                    pass
                elif faces.remove([1041,1042,1043]):
                    pass
                elif faces.remove([1089,1090,1091]):
                    pass
                elif faces.remove([4047,4048,4049]):
                    pass
                elif faces.remove([4073,4074,4075]):
                    pass
                elif faces.remove([4074,4075,4076]):
                    pass
                elif faces.remove([4380,4381,4382]):
                    pass
                elif faces.remove([4379,4380,4381]):
                    pass
                elif faces.remove([4188,4189,4190]):
                    pass
                elif faces.remove([4187,4188,4189]):
                    pass
                elif faces.remove([4046,4047,4048]):
                    pass
                elif faces.remove([4227,4228,4229]):
                    pass
                elif faces.remove([4226,4227,4228]):
                    pass
                elif faces.remove([4095,4096,4097]):
                    pass
                elif faces.remove([4094,4095,4096]):
                    pass
                elif faces.remove([4126,4127,4128]):
                    pass
                elif faces.remove([4125,4126,4127]):
                    pass
                elif faces.remove([4033,4034,4035]):
                    pass
                elif faces.remove([4034,4035,4036]):
                    pass
                elif faces.remove([4208,4209,4210]):
                    pass
                elif faces.remove([4207,4208,4209]):
                    pass
                elif faces.remove([4120,4121,4122]):
                    pass
                elif faces.remove([4121,4122,4123]):
                    pass
                elif faces.remove([4273,4274,4275]):
                    pass
                elif faces.remove([4274,4275,4276]):
                    pass
                elif faces.remove([4200,4201,4202]):
                    pass
                elif faces.remove([4199,4200,4201]):
                    pass
                elif faces.remove([1393,1394,1395]):
                    pass
                elif faces.remove([1394,1395,1396]):
                    pass
                elif faces.remove([1338,1339,1340]):
                    pass
                elif faces.remove([1337,1338,1339]):
                    pass
                elif faces.remove([1285,1286,1287]):
                    pass
                elif faces.remove([1311,1312,1313]):
                    pass
                elif faces.remove([1312,1313,1314]):
                    pass
                elif faces.remove([1402,1403,1404]):
                    pass
                elif faces.remove([1401,1402,1403]):
                    pass
                elif faces.remove([1286,1287,1288]):
                    pass
                elif faces.remove([6080,6081,6082]):
                    pass
                elif faces.remove([1073,1074,1075]):
                    pass
                elif faces.remove([1074,1075,1076]):
                    pass
                elif faces.remove([6081,6082,6083]):
                    pass
                elif faces.remove([3591,3592,3593]):
                    pass
                elif faces.remove([3590,3591,3592]):
                    pass
                elif faces.remove([3300,3301,3302]):
                    pass
                elif faces.remove([3064,3065,3066]):
                    pass
                elif faces.remove([3209,3210,3211]):
                    pass
                elif faces.remove([3076,3077,3078]):
                    pass
                elif faces.remove([3075,3076,3077]):
                    pass
                elif faces.remove([3301,3302,3303]):
                    pass
                elif faces.remove([3065,3066,3067]):
                    pass
                elif faces.remove([3053,3054,3055]):
                    pass
                elif faces.remove([3290,3291,3292]):
                    pass
                elif faces.remove([3054,3055,3056]):
                    pass
                elif faces.remove([3222,3223,3224]):
                    pass
                elif faces.remove([2986,2987,2988]):
                    pass
                elif faces.remove([3221,3222,3223]):
                    pass
                elif faces.remove([2985,2986,2987]):
                    pass
                elif faces.remove([3084,3085,3086]):
                    pass
                elif faces.remove([2848,2849,2850]):
                    pass
                elif faces.remove([3083,3084,3085]):
                    pass
                elif faces.remove([2847,2848,2849]):
                    pass
                elif faces.remove([3210,3211,3212]):
                    pass
                elif faces.remove([2974,2975,2976]):
                    pass
                elif faces.remove([3235,3236,3237]):
                    pass
                elif faces.remove([2999,3000,3001]):
                    pass
                elif faces.remove([2973,2974,2975]):
                    pass
                elif faces.remove([3268,3269,3270]):
                    pass
                elif faces.remove([3032,3033,3034]):
                    pass
                elif faces.remove([3269,3270,3271]):
                    pass
                elif faces.remove([3033,3034,3035]):
                    pass
                elif faces.remove([3234,3235,3236]):
                    pass
                elif faces.remove([2998,2999,3000]):
                    pass
                elif faces.remove([3260,3261,3262]):
                    pass
                elif faces.remove([3024,3025,3026]):
                    pass
                elif faces.remove([3187,3188,3189]):
                    pass
                elif faces.remove([2951,2952,2953]):
                    pass
                elif faces.remove([3169,3170,3171]):
                    pass
                elif faces.remove([2933,2934,2935]):
                    pass
                elif faces.remove([3170,3171,3172]):
                    pass
                elif faces.remove([2934,2935,2936]):
                    pass
                elif faces.remove([3137,3138,3139]):
                    pass
                elif faces.remove([2901,2902,2903]):
                    pass
                elif faces.remove([3151,3152,3153]):
                    pass
                elif faces.remove([2915,2916,2917]):
                    pass
                elif faces.remove([3540,3541,3542]):
                    pass
                elif faces.remove([3758,3759,3760]):
                    pass
                elif faces.remove([3528,3529,3530]):
                    pass
                elif faces.remove([3759,3760,3761]):
                    pass
                elif faces.remove([3529,3530,3531]):
                    pass
                elif faces.remove([3539,3540,3541]):
                    pass
                elif faces.remove([3452,3453,3454]):
                    pass
                elif faces.remove([3561,3562,3563]):
                    pass
                elif faces.remove([3562,3563,3564]):
                    pass
                elif faces.remove([3336,3337,3338]):
                    pass
                elif faces.remove([3571,3572,3573]):
                    pass
                elif faces.remove([3570,3571,3572]):
                    pass
                elif faces.remove([3611,3612,3613]):
                    pass
                elif faces.remove([3610,3611,3612]):
                    pass
                elif faces.remove([3367,3368,3369]):
                    pass
                elif faces.remove([3368,3369,3370]):
                    pass
                elif faces.remove([3601,3602,3603]):
                    pass
                elif faces.remove([3335,3336,3337]):
                    pass
                elif faces.remove([3320,3321,3322]):
                    pass
                elif faces.remove([3319,3320,3321]):
                    pass
                elif faces.remove([3441,3442,3443]):
                    pass
                elif faces.remove([3451,3452,3453]):
                    pass
                elif faces.remove([3729,3730,3731]):
                    pass
                elif faces.remove([3440,3441,3442]):
                    pass
                elif faces.remove([3741,3742,3743]):
                    pass
                elif faces.remove([3717,3718,3719]):
                    pass
                elif faces.remove([3751,3752,3753]):
                    pass
                elif faces.remove([3692,3693,3694]):
                    pass
                elif faces.remove([3465,3466,3467]):
                    pass
                elif faces.remove([3691,3692,3693]):
                    pass
                elif faces.remove([3464,3465,3466]):
                    pass
                elif faces.remove([3706,3707,3708]):
                    pass
                elif faces.remove([3705,3706,3707]):
                    pass
                elif faces.remove([3518,3519,3520]):
                    pass
                elif faces.remove([3752,3753,3754]):
                    pass
                elif faces.remove([3579,3580,3581]):
                    pass
                elif faces.remove([3683,3684,3685]):
                    pass
                elif faces.remove([3684,3685,3686]):
                    pass
                elif faces.remove([3695,3696,3697]):
                    pass
                elif faces.remove([3551,3552,3553]):
                    pass
                elif faces.remove([3552,3553,3554]):
                    pass
                elif faces.remove([3257,3258,3259]):
                    pass
                elif faces.remove([3021,3022,3023]):
                    pass
                elif faces.remove([3256,3257,3258]):
                    pass
                elif faces.remove([3020,3021,3022]):
                    pass
                elif faces.remove([3517,3518,3519]):
                    pass
                elif faces.remove([1344,1345,1346]):
                    pass
                elif faces.remove([1345,1346,1347]):
                    pass
                elif faces.remove([1231,1232,1233]):
                    pass
                elif faces.remove([1230,1231,1232]):
                    pass
                elif faces.remove([1159,1160,1161]):
                    pass
                elif faces.remove([4669,4670,4671]):
                    pass
                elif faces.remove([4670,4671,4672]):
                    pass
                elif faces.remove([669,670,671]):
                    pass
                elif faces.remove([668,669,670]):
                    pass
                elif faces.remove([702,703,704]):
                    pass
                elif faces.remove([736,737,738]):
                    pass
                elif faces.remove([737,738,739]):
                    pass
                elif faces.remove([703,704,705]):
                    pass
                elif faces.remove([4642,4643,4644]):
                    pass
                elif faces.remove([4641,4642,4643]):
                    pass
                elif faces.remove([5806,5807,5808]):
                    pass
                elif faces.remove([4294,4295,4296]):
                    pass
                elif faces.remove([4293,4294,4295]):
                    pass
                #elif faces.remove([4338,4339,4400]):
                    #pass
                elif faces.remove([222,223,224]):
                    pass
                elif faces.remove([221,222,223]):
                    pass
                elif faces.remove([187,188,189]):
                    pass
                elif faces.remove([153,154,155]):
                    pass
                elif faces.remove([154,155,156]):
                    pass
                elif faces.remove([188,189,190]):
                    pass
                elif faces.remove([4247,4248,4249]):
                    pass
                elif faces.remove([4241,4242,4243]):
                    pass
                elif faces.remove([4246,4247,4248]):
                    pass
                elif faces.remove([4337,4338,4339]):
                    pass
                elif faces.remove([4267,4268,4269]):
                    pass
                elif faces.remove([4266,4267,4268]):
                    pass
                elif faces.remove([4240,4241,4242]):
                    pass
                elif faces.remove([4220,4221,4222]):
                    pass
                elif faces.remove([4219,4220,4221]):
                    pass
                elif faces.remove([4130,4131,4132]):
                    pass
                elif faces.remove([4129,4130,4131]):
                    pass
                elif faces.remove([5042,5043,5044]):
                    pass
                elif faces.remove([5043,5044,5045]):
                    pass
                elif faces.remove([4682,4683,4684]):
                    pass
                elif faces.remove([4681,4682,4683]):
                    pass
                elif faces.remove([4614,4615,4616]):
                    pass
                elif faces.remove([4613,4614,4615]):
                    pass
            elif len(faces) == 20135:
                #Blocks_01
                if faces.remove([10831,10832,10833]):
                    pass
                elif faces.remove([10832,10833,10834]):
                    pass
                elif faces.remove([9772,9773,9774]):
                    pass
                elif faces.remove([9771,9772,9773]):
                    pass
                elif faces.remove([2197,2198,2199]):
                    pass
                elif faces.remove([2199,2200,2201]):
                    pass
                elif faces.remove([9619,9620,9621]):
                    pass
                elif faces.remove([9620,9621,9622]):
                    pass
                elif faces.remove([9841,9842,9843]):
                    pass
                elif faces.remove([9842,9843,9844]):
                    pass
                elif faces.remove([9678,9679,9680]):
                    pass
                elif faces.remove([9661,9662,9663]):
                    pass
                elif faces.remove([9660,9661,9662]):
                    pass
                elif faces.remove([9552,9553,9554]):
                    pass
                elif faces.remove([9699,9700,9701]):
                    pass
                elif faces.remove([19969,19970,19971]):
                    pass
                elif faces.remove([19825,19826,19827]):
                    pass
                elif faces.remove([19681,19682,19683]):
                    pass
                elif faces.remove([19537,19538,19539]):
                    pass
                elif faces.remove([19393,19394,19395]):
                    pass
                elif faces.remove([19249,19250,19251]):
                    pass
                elif faces.remove([18989,18990,18991]):
                    pass
                elif faces.remove([18845,18846,18847]):
                    pass
                elif faces.remove([18701,18702,18703]):
                    pass
                elif faces.remove([18557,18558,18559]):
                    pass
                elif faces.remove([18413,18414,18415]):
                    pass
                elif faces.remove([18269,18270,18271]):
                    pass
                #elif faces.remove([11571,11572,17573]):
                    #pass
                elif faces.remove([9469,9470,9471]):
                    pass
                elif faces.remove([9468,9469,9470]):
                    pass
                elif faces.remove([9465,9466,9467]):
                    pass
                elif faces.remove([7225,7226,7227]):
                    pass
                elif faces.remove([9464,9465,9466]):
                    pass
                elif faces.remove([9585,9586,9587]):
                    pass
                elif faces.remove([9586,9587,9588]):
                    pass
                elif faces.remove([9582,9583,9584]):
                    pass
                elif faces.remove([9581,9582,9583]):
                    pass
                elif faces.remove([2408,2409,2410]):
                    pass
                elif faces.remove([3074,3075,3076]):
                    pass
                elif faces.remove([3075,3076,3077]):
                    pass
                elif faces.remove([9604,9605,9606]):
                    pass
                elif faces.remove([9679,9680,9681]):
                    pass
                elif faces.remove([9470,9471,9472]):
                    pass
                elif faces.remove([9598,9599,9600]):
                    pass
                elif faces.remove([9605,9606,9607]):
                    pass
                elif faces.remove([9551,9552,9553]):
                    pass
                elif faces.remove([9391,9392,9393]):
                    pass
                elif faces.remove([2390,2391,2392]):
                    pass
                elif faces.remove([9554,9555,9556]):
                    pass
                elif faces.remove([9555,9556,9557]):
                    pass
                elif faces.remove([2381,2382,2383]):
                    pass
                elif faces.remove([2382,2383,2384]):
                    pass
                elif faces.remove([2384,2385,2386]):
                    pass
                elif faces.remove([2385,2386,2387]):
                    pass
                elif faces.remove([2416,2417,2418]):
                    pass
                elif faces.remove([9730,9731,9732]):
                    pass
                elif faces.remove([9729,9730,9731]):
                    pass
                elif faces.remove([2967,2968,2969]):
                    pass
                elif faces.remove([2966,2967,2968]):
                    pass
                elif faces.remove([2935,2936,2937]):
                    pass
            elif len(faces) == 316:
                #loading
                if faces.remove([145,146,147]):
                    pass
                elif faces.remove([313,314,315]):
                    pass
                elif faces.remove([142,143,144]):
                    pass
        elif Chunk == b"SST0":
            break
    for a in bpy.context.screen.areas:
        if a.type == 'VIEW_3D':
            for s in a.spaces:
                if s.type == 'VIEW_3D':
                    s.clip_end = 400000
                    s.clip_start = 1

    C = bpy.context
    BSDF = "Principled BSDF"
    vmesh = "dragonjanCol"
    materialnamess = "dragonjan Material"
    dragonjannames = "dragonjan"
    meshID = len(bpy.data.objects)
    mesh = bpy.data.meshes.new("dragonjan")
    mesh.from_pydata(vertices, [], faces)
    object = bpy.data.objects.new("dragonjan", mesh)
    bpy.context.collection.objects.link(object)
    mesh.vertex_colors.new(name=vmesh)
    vindex = 0
    for vertex in mesh.vertices:
        vertex.normal = normals[vindex]
        vindex += 1
    objs = bpy.data.objects[dragonjannames]
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
    NU_TEXTURE = 'ShaderNodeTexImage'
    MaterialName = "dragonjan Material"

    obj = bpy.data.objects[dragonjannames]
    mats = bpy.data.materials.new(materialnamess)
    obj.data.materials.append(mats)

    previous_mix = None
    previous_rgba = None
    previous_img = None

    for i, mat in enumerate(bpy.data.materials):
        mat.use_nodes = True
        bpy.data.materials[MaterialName].node_tree.nodes[BSDF].inputs[7].default_value = 0
        bpy.data.materials[MaterialName].node_tree.nodes[BSDF].inputs[9].default_value = 1
        #bpy.data.node.add_search(use_transform=True, node_item=items)
        mat.blend_method = "HASHED"
        mix = mat.node_tree.nodes.new(NU_MIX_MODE)
        rgbaV = mat.node_tree.nodes.new(NU_RGBA_VERT)
        texA = mat.node_tree.nodes.new(NU_TEXTURE)
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
        for i in range(1):
            texA.location.x = -300
            texA.location.y = -100
            if previous_img:
                links.new(previous_img.outputs[0], previous_img.inputs[0])
            previous_rgba = NU_TEXTURE
    links.new(rgbaV.outputs[1], principled.inputs[21])
    links.new(rgbaV.outputs[0], mix.inputs[1])
    links.new(texA.outputs[0], mix.inputs[2])


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
            uvs.append([uy,ux])
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
            uvs.append([uy, ux])
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
            
        
        

def parse_gsc(filepath, Triangle_Strips_with_uvs_and_rgba=1, Triangle_StripsTwo=False, Triangle_Strips=False, WholeMassiveOne=False, ONE_CHUNK_OFFSET1=False, ONE_CHUNK_OFFSET1PT2=False, ONE_CHUNK_OFFSET2=False, SST=False, SPEC=False, INST=False, IABL=False, BoundingSet=False, SelectOnlyUVMesh=False, SelectOnly2ndUVMesh=False, SelectOnly3rdUVMesh=False, Triangles=False, RGBAColors=False):
    f = open(filepath, "rb")
    if Triangle_Strips:
        wholeChunk1(f, vertices=[], faces=[], normals=[], fa=-1, fb=0, fc=1)
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
        FinalUnknownChunk(f, VCountThree=3, vertices=[], faces=[], fa=-4, fb=-3,fc=-2,fa_m=-3,fb_m=-2,fc_m=-1)

    if Triangle_StripsTwo:
        DIFOffset_one(f, vertices=[], faces=[], fa=-1, fb=0, fc=1)
    if RGBAColors:
        ColorReach(f, colors=[])
    if Triangle_Strips_with_uvs_and_rgba == 1:
        get_1stobjects_with_uvs_and_rgba(f, fa=-1,fb=0,fc=1,vertices=[], faces=[], uvs=[], rgba=[], chunks=0, paddingWhere=0)
    if Triangle_Strips_with_uvs_and_rgba == 2:
        get_2ndobjects_with_uvs_and_rgba(f, fa=-1,fb=0,fc=1,vertices=[], faces=[], uvs=[], rgba=[], chunks=0, paddingWhere=0)
    if Triangle_Strips_with_uvs_and_rgba == 3:
        get_3rdobjects_with_uvs_and_rgba(f, vertices=[], faces=[], fa=-1, fb=0, fc=1, uvs=[], rgba=[], chunks=0, paddingWhere=0)
    
    f.close()



