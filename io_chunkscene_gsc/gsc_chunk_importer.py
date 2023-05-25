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
            for i in range(VertexCount*2//8):
                fa += 1 * 4
                fb += 1 * 4
                fc += 1 * 4
                faces.append([fa,fb,fc])
            for i in range(VertexCount*2//8):
                fa_m += 1 * 4
                fb_m += 1 * 4
                fc_m += 1 * 4
                faces.append([fb_m,fa_m,fc_m])
            
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


def wholeChunk1(f, vertices=[], faces=[], fa=-1, fb=0, fc=1):
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

            for i in range(vertexCount-2):
                FaceIndex+=1
                fa+=1
                fb+=1
                fc+=1
                faces.append([fa,fb,fc])
            #https://stackoverflow.com/questions/51481077/python-removing-an-item-from-a-list-in-the-if-statement-condition
            if len(faces) == 48570:
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
                    pass
            elif len(faces) == 6686:
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
                #elif faces.remove([2821,2822,2823]):
                    #pass
                elif faces.remove([2810,2811,2812]):
                    pass
                elif faces.remove([2821,2822,2823]):
                    pass
                elif faces.remove([2811,2812,2813]):
                    pass
                elif faces.remove([2781,2782,2783]):
                    pass
                #elif faces.remove([2811,2812,2813]):
                    #pass
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
    materialnamess = "dragonjan Material"
    dragonjannames = "dragonjan"
    meshID = len(bpy.data.objects)
    mesh = bpy.data.meshes.new("dragonjan")
    mesh.from_pydata(vertices, [], faces)
    object = bpy.data.objects.new("dragonjan", mesh)
    bpy.context.collection.objects.link(object)
    mesh.vertex_colors.new(name=vmesh)
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
        wholeChunk1(f, vertices=[], faces=[], fa=-1, fb=0, fc=1)
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



