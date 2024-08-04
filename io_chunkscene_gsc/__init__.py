bl_info = {
        'name'			: 'Finding Nemo GSC Level Chunk Importer',
	'author'		: 'DarkShadow Nemo',
	'version'		: (0, 5, 0),
	'blender'		: (4, 0, 0),
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
        ONE_CHUNK_OFFSET1: BoolProperty(
                name        = '0x030100010380',
                description = 'imports with vertices and triangle strips aligned up'
        )
        SST: BoolProperty(
                name        = 'SplineSet',
                description = 'imports splines with vertices and edges'
        )
        SPEC: BoolProperty(
                name        = 'SpecialSet',
                description = 'imports SpecialSet Objects'
	)
        INST_prim: BoolProperty(
                name        = 'INSTANCE PRIMARY',
                description = 'imports INSTANCE Objects first'
        )
        INST_seco: BoolProperty(
                name        = 'INSTANCE SECONDY',
                description = 'imports INSTANCE Objects second'
        )
        IABL: BoolProperty(
                name        = 'InstanceAnimationBlock',
                description = 'imports the stuff that you replaced in ram'
        )
        ALIB: BoolProperty(
                name        = 'animation library',
                description = 'TODO'
        )
        BoundingSet: BoolProperty(
                name        = 'BNDS',
                description = 'imports boundingsets'
        )
        SelectOnlyUVMesh: BoolProperty(
                name = "0x010000050480XX6D",
                description = "be careful to select the mesh before executing or you will get the wrong uv data, select mesh first before doing this or it won't work on 0x6D"
        )
        SelectOnly2ndUVMesh: BoolProperty(
                name = "0x010000050480XX65",
                description = "be careful to select the mesh before executing always on 0x65 next to it in a row"
        )
        SelectOnly3rdUVMesh: BoolProperty(
                name = "0x0480XX65",
                description = "be careful to select the mesh before executing, very short but done a workaround it this touches on this offset"
        )
        SelectOnly4thUVMesh: BoolProperty(
                name = "0x0480XX6D",
                description = "be careful to select the mesh before executing, very short but done a workaround it this touches on this offset"
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
        pointOne: BoolProperty(
                name = "one point",
                description = ""
        )
        directory: StringProperty()
        filter_glob: StringProperty(default = '*.gsc', options = {'HIDDEN'})
        def execute(self, context):
                paths = [os.path.join(self.directory, name.name) for name in self.files]
                if not paths: paths.append(self.filepath)
                importlib.reload(gsc_chunk_importer)
                for path in paths: gsc_chunk_importer.parse_gsc(path, pointOne = self.pointOne, Triangle_Strips_with_uvs_and_rgba = self.Triangle_Strips_with_uvs_and_rgba, Triangle_StripsTwo = self.Triangle_StripsTwo, Triangle_Strips = self.Triangle_Strips, ONE_CHUNK_OFFSET1 = self.ONE_CHUNK_OFFSET1,SST = self.SST,SPEC = self.SPEC,INST_prim = self.INST_prim,INST_seco = self.INST_seco,IABL = self.IABL,ALIB = self.ALIB, BoundingSet = self.BoundingSet, SelectOnlyUVMesh = self.SelectOnlyUVMesh, SelectOnly2ndUVMesh = self.SelectOnly2ndUVMesh, SelectOnly3rdUVMesh = self.SelectOnly3rdUVMesh, SelectOnly4thUVMesh = self.SelectOnly4thUVMesh, BatchHashVertexColors = self.BatchHashVertexColors, BatchUVSS = self.BatchUVSS, RGBAColors = self.RGBAColors)
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

        ofsetsOne : BoolProperty(
                name = "0x030100010380XX6C",
                description = "exports no uvs and vertex colors"
        )

        ofsetsOneC : BoolProperty(
                name = "0x030100010380XX6C Connection",
                description = "exports no uvs and vertex colors but connects"
        )

        ofsetsOneIMG : BoolProperty(
                name = "0x030100010380XX6C with textures",
                description = "exports uvs and vertex colors with textures"
        )
        
        directory: StringProperty()
        filter_glob: StringProperty(default = '*.gsc', options = {'HIDDEN'})
        def execute(self, context):
            importlib.reload(gsc_chunk_exporter)
            gsc_chunk_exporter.NUWrite(self.filepath, ofsetsOne = self.ofsetsOne, ofsetsOneC = self.ofsetsOneC, ofsetsOneIMG = self.ofsetsOneIMG)
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
