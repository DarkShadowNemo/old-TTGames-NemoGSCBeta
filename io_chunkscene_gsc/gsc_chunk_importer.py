from struct import pack, unpack
import os
import bpy

    
    
    
    

chunk = 0 # what int property does not work with bool property might have to do this manually

def wholeChunk2(f, vertices=[]):
    f.seek(0)
    while 1:
        Chunk = f.read(4)
        if Chunk == b"\x02\x80\x01\x6C":
            for i in range(1):
                unknown = unpack("<I", f.read(4))[0]
                vx = unpack("<f", f.read(4))[0]
                vy = unpack("<f", f.read(4))[0]
                vz = unpack("<f", f.read(4))[0]
        elif Chunk == b"SST0":
            print(f.tell())
            break
    mesh = bpy.data.meshes.new("dragonjan")
    mesh.from_pydata(vertices, [], [])
    object = bpy.data.objects.new("dragonjan", mesh)
    bpy.context.collection.objects.link(object)

def wholeChunk1(f, vertices=[], faces=[], fa=-1, fb=0, fc=1):
    f.seek(0)
    while 1:
        Chunk = f.read(4)
        if Chunk == b"\x03\x01\x00\x01":
            f.seek(2,1)
            vertexCount = unpack("b", f.read(1))[0]
            clump = unpack("b", f.read(1))[0]
            for i in range(vertexCount):
                vx = unpack("<f", f.read(4))[0]
                vy = unpack("<f", f.read(4))[0]
                vz = unpack("<f", f.read(4))[0]
                nz = unpack("<f", f.read(4))[0] #normals
                vertices.append([vx,vy,vz])
            for i in range(vertexCount-2):
                fa += 1
                fb += 1
                fc += 1
                faces.append([fa,fb,fc])
        elif Chunk == b"SST0":
            print(f.tell())
            break
    MaterialName=0
    BSDF = "Principled BSDF"
    mesh = bpy.data.meshes.new("dragonjan")
    mesh.from_pydata(vertices, [], faces)
    object = bpy.data.objects.new("dragonjan", mesh)
    bpy.context.collection.objects.link(object)
    bpy.data.materials.new(name="dragonjan_materials")
    for fac in mesh.polygons:
        fac.use_smooth = True
    #bpy.data.materials[MaterialName].node_tree.nodes[BSDF].inputs[7].default_value = 0
    #bpy.data.materials[MaterialName].node_tree.nodes[BSDF].inputs[9].default_value = 1
    #MaterialName+=1 # the reason because there a dots stroke


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
            ux = unpack("<h", f.read(2))[0] / 10000.0
            uy = unpack("<h", f.read(2))[0] / 10000.0
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
            ux = unpack("<h", f.read(2))[0] / 10000.0
            uy = unpack("<h", f.read(2))[0] / 10000.0
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
            ux = unpack("<h", f.read(2))[0] / 10000.0
            uy = unpack("<h", f.read(2))[0] / 10000.0
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
        f.seek(chunk,1)
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
            
        MaterialName=0
        BSDF = "Principled BSDF"    
        mesh = bpy.data.meshes.new("dragonjan")
        mesh.from_pydata(vertices, [], faces)
        object = bpy.data.objects.new("dragonjan", mesh)
        bpy.context.collection.objects.link(object)
        mesh.vertex_colors.new(name="dragonjanCol")
        bpy.data.materials.new(name="dragonjan_materials")
        #bpy.data.materials[MaterialName].node_tree.nodes[BSDF].inputs[7].default_value = 0
        #bpy.data.materials[MaterialName].node_tree.nodes[BSDF].inputs[9].default_value = 1
        #MaterialName+=1 # the reason because there a dots stroke
        uvtex = mesh.uv_layers.new()
        uvtex.name = 'dragonjanUV'
        for fac in mesh.polygons:
            fac.use_smooth = True
    else:
        raise Exception("that offset not found")
    

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
            ux = unpack("h", f.read(2))[0] / 10000.0
            uy = unpack("h", f.read(2))[0] / 10000.0
            uvs.append([ux,uy])
        f.seek(6, 1)
        rgbacount = unpack("b", f.read(1))[0]
        f.seek(1,1)
        for i in range(rgbacount):
            r = unpack("b", f.read(1))[0] / 255.0
            g = unpack("b", f.read(1))[0] / 255.0
            b = unpack("b", f.read(1))[0] / 255.0
            a = unpack("b", f.read(1))[0] / 127.0
            rgba.append([r,g,b])
            
        MaterialName=0
        BSDF = "Principled BSDF"        
        mesh = bpy.data.meshes.new("dragonjan")
        mesh.from_pydata(vertices, [], faces)
        object = bpy.data.objects.new("dragonjan", mesh)
        bpy.context.collection.objects.link(object)
        mesh.vertex_colors.new(name="dragonjanCol")
        bpy.data.materials.new(name="dragonjan_materials")
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
            
        
        

def parse_gsc(filepath, WholeOne=False, WholeMassiveOne=False, ONE_CHUNK_OFFSET1=False, ONE_CHUNK_OFFSET1PT2=False, ONE_CHUNK_OFFSET2=False, SST=False, SPEC=False, INST=False, IABL=False, BoundingSet=False, SelectOnlyUVMesh=False, SelectOnly2ndUVMesh=False, SelectOnly3rdUVMesh=False):
    f = open(filepath, "rb")
    if WholeOne:
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
    f.close()



