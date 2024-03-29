bl_info = {
        'name'			: 'Finding Nemo GSC Level Chunk Importer',
	'author'		: 'DarkShadow Nemo',
	'version'		: (0, 3, 7),
	'blender'		: (3, 0, 0),
	'location'		: 'File > Import-Export',
	'description'           : 'Import GSC one mesh chunk makes it easier',
	'category'		: 'Chunk-Importer and Chunk-Exporter'
}
import os
import bpy
import importlib
from bpy.props import CollectionProperty, StringProperty, BoolProperty, EnumProperty, FloatProperty, IntProperty
from bpy_extras.io_utils import ImportHelper, ExportHelper


from.import gsc_chunk_importer, gsc_chunk_exporter

class ImportChunkGSC(bpy.types.Operator, ImportHelper):
        bl_idname  = 'import_chunk.gsc'
        bl_label   = 'Import Chunk GSC'
        bl_options = {'UNDO'}
        filename_ext = '.gsc'
        files: CollectionProperty(
                name	    = 'File path',
                description = 'File path used for finding the GSC Chunk file.',
                type	    = bpy.types.OperatorFileListElement
        )

        Triangle_Strips_part3: BoolProperty(
                name        = "Triangle Strips pt 3",
                description = "May take time to load because impossible to use while 1"
        )

        Triangle_Strips_with_uvs_and_rgba: IntProperty(
                name        = "Triangle_Strips uvs and rgba",
                description = "gets uvs and rgba as well"
        )

        Triangle_StripsTwo: BoolProperty(
                name        = "Triangle_Strips pt 2",
                description = "0x010000050380 all offsets"
        )
        
        Triangle_Strips: BoolProperty(
                name        = 'Triangle_Strips',
                description = ' 0x03010001 all offsets if they match it imports all the whole chunk in being aligned up gets all or most of it, you may get some vertex without faces'
        )
        WholeMassiveOne: BoolProperty(
                name        = '0x00000280 all offsets',
                description = 'unfortanately this imports vertices only no idea to import faces for this offset'
        )
        ONE_CHUNK_OFFSET1: BoolProperty(
                name        = '0x030100010380',
                description = 'imports with vertices and triangle strips aligned up'
        )
        ONE_CHUNK_OFFSET2: BoolProperty(
                name        = '0x000000000280',
                description = 'imports with vertices but no triangle strips you have to do this manually'
        )
        SST: BoolProperty(
                name        = 'SplineSet',
                description = 'imports splines with vertices and edges'
        )
        SPEC: BoolProperty(
                name        = 'SpecialSet',
                description = 'imports SpecialSet Objects'
	)
        INST: BoolProperty(
                name        = 'INSTANCE',
                description = 'imports INSTANCE Objects with namedtable strings'
        )
        IABL: BoolProperty(
                name        = 'InstanceAnimationBlock',
                description = 'imports the stuff that you replaced in ram'
        )
        BoundingSet: BoolProperty(
                name        = 'BNDS',
                description = 'imports boundingsets'
        )
        ONE_CHUNK_OFFSET1PT2: BoolProperty(
                name = "0x030100010380 Part 2",
                description = 'supports now dodgy lego star wars and nemo there nemo offset starts at 0x0480XX6D and uv and rgba data for lego star wars'
        )
        SelectOnlyUVMesh: BoolProperty(
                name = "0x010000050480",
                description = "be careful to select the mesh before executing or you will get the wrong uv data, select mesh first before doing this or it won't work"
        )
        SelectOnly2ndUVMesh: BoolProperty(
                name = "0x010000050480",
                description = "be careful to select the mesh before executing always on 0x65 next to it in a row"
        )
        SelectOnly3rdUVMesh: BoolProperty(
                name = "0x0480XX65",
                description = "be careful to select the mesh before executing, very short but done a workaround it this touches on this offset"
        )
        Triangles: BoolProperty(
                name = "Triangles",
                description = "some may use triangles, this reduces some duplicated edges use at your own risk"
        )
        Norm_Triangles: BoolProperty(
                name = "Normal Triangles",
                description = "imports normal triangles if you want to get the whole entire mesh it requires patches and modifiying the gsc file format"
        )
        BatchHashVertexColors: BoolProperty(
                name = "BatchHashVertexColors",
                description = "imports vertex colors everything"
        )
        BatchUVSS: BoolProperty(
                name = "Batch UVS",
                description = "imports uvs and everything"
        )
        RGBAColors: BoolProperty(
                name = "RGBA Hash Colors",
                description = "chooses one RGBA only since it's impossible with the whole mesh unless you remove other offsets"
        )
        directory: StringProperty()
        filter_glob: StringProperty(default = '*.gsc', options = {'HIDDEN'})
        def execute(self, context):
                paths = [os.path.join(self.directory, name.name) for name in self.files]
                if not paths: paths.append(self.filepath)
                importlib.reload(gsc_chunk_importer)
                for path in paths: gsc_chunk_importer.parse_gsc(path, Triangle_Strips_part3 = self.Triangle_Strips_part3, Triangle_Strips_with_uvs_and_rgba = self.Triangle_Strips_with_uvs_and_rgba, Triangle_StripsTwo = self.Triangle_StripsTwo, Triangle_Strips = self.Triangle_Strips, WholeMassiveOne = self.WholeMassiveOne, ONE_CHUNK_OFFSET1 = self.ONE_CHUNK_OFFSET1,ONE_CHUNK_OFFSET1PT2 = self.ONE_CHUNK_OFFSET1PT2,ONE_CHUNK_OFFSET2 = self.ONE_CHUNK_OFFSET2,SST = self.SST,SPEC = self.SPEC,INST = self.INST,IABL = self.IABL,BoundingSet = self.BoundingSet, SelectOnlyUVMesh = self.SelectOnlyUVMesh, SelectOnly2ndUVMesh = self.SelectOnly2ndUVMesh, SelectOnly3rdUVMesh = self.SelectOnly3rdUVMesh, Triangles = self.Triangles, Norm_Triangles = self.Norm_Triangles, BatchHashVertexColors = self.BatchHashVertexColors, BatchUVSS = self.BatchUVSS, RGBAColors = self.RGBAColors)
                return {'FINISHED'}

class ExportChunkGSC(bpy.types.Operator, ExportHelper):
        bl_idname  = 'export_chunk.gsc'
        bl_label   = 'Export Chunk GSC'
        bl_options = {'UNDO'}
        filename_ext = '.gsc'
        files: CollectionProperty(
                name	    = 'File path',
                description = 'File path used for finding the GSC Chunk file.',
                type	    = bpy.types.OperatorFileListElement
        )
        OFFSET1: IntProperty(
                name = "0x030100010380XX6C",
                description = "exports original offset, choose a number"
        )
        OFFSET2: IntProperty(
                name = "0x03010001010000050380",
                description = "exports short signed integer 4096, experimental not sure this will go above it"
        )
        custom_faces: BoolProperty(
                name = "Custom Faces",
                description = "exports custom faces that TTGames never uses, MIGHT NOT WORK IN GAME"
        )
        
        directory: StringProperty()
        filter_glob: StringProperty(default = '*.gsc', options = {'HIDDEN'})
        def execute(self, context):
            importlib.reload(gsc_chunk_exporter)
            gsc_chunk_exporter.NUWrite(self.filepath, OFFSET1 = self.OFFSET1, OFFSET2 = self.OFFSET2)
            return {"FINISHED"}
        


	
def menu_func_import(self, context):
        self.layout.operator(ImportChunkGSC.bl_idname, text='GSC Chunk Importer (.gsc)')

def menu_func_export(self, context):
        self.layout.operator(ExportChunkGSC.bl_idname, text='GSC Chunk Exporter (.gsc)')

def register():
        bpy.utils.register_class(ImportChunkGSC)
        bpy.utils.register_class(ExportChunkGSC)
        bpy.types.TOPBAR_MT_file_import.append(menu_func_import)
        bpy.types.TOPBAR_MT_file_export.append(menu_func_export)
def unregister():
        bpy.utils.unregister_class(ImportChunkGSC)
        bpy.utils.unregister_class(ExportChunkGSC)
        bpy.types.TOPBAR_MT_file_import.remove(menu_func_import)
        bpy.types.TOPBAR_MT_file_export.remove(menu_func_export)
if __name__ == '__main__':
        register()
        unregister()
