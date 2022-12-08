bl_info = {
        'name'			: 'Finding Nemo GSC Level Chunk Importer',
	'author'		: 'DarkShadow Nemo',
	'version'		: (0, 1, 8),
	'blender'		: (3, 0, 0),
	'location'		: 'File > Import',
	'description'           : 'Import GSC one mesh chunk makes it easier',
	'category'		: 'Chunk-Importer',
        'warning'               : 'Exporter is Non-Functioned and missing ingame it might work for customs'
}
import os
import bpy
import importlib
from bpy.props import CollectionProperty, StringProperty, BoolProperty, EnumProperty, FloatProperty, IntProperty
from bpy_extras.io_utils import ImportHelper, ExportHelper

from.import gsc_chunk_importer

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
        WholeOne: BoolProperty(
                name        = '0x03010001 all offsets',
                description = 'if they match it imports all the whole chunk in'
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
        directory: StringProperty()
        filter_glob: StringProperty(default = '*.gsc', options = {'HIDDEN'})
        def execute(self, context):
                paths = [os.path.join(self.directory, name.name) for name in self.files]
                if not paths: paths.append(self.filepath)
                importlib.reload(gsc_chunk_importer)
                for path in paths: gsc_chunk_importer.parse_gsc(path, WholeOne = self.WholeOne, WholeMassiveOne = self.WholeMassiveOne, ONE_CHUNK_OFFSET1 = self.ONE_CHUNK_OFFSET1,ONE_CHUNK_OFFSET1PT2 = self.ONE_CHUNK_OFFSET1PT2,ONE_CHUNK_OFFSET2 = self.ONE_CHUNK_OFFSET2,SST = self.SST,SPEC = self.SPEC,INST = self.INST,IABL = self.IABL,BoundingSet = self.BoundingSet, SelectOnlyUVMesh = self.SelectOnlyUVMesh, SelectOnly2ndUVMesh = self.SelectOnly2ndUVMesh, SelectOnly3rdUVMesh = self.SelectOnly3rdUVMesh)
                return {'FINISHED'}
	
def menu_func_import(self, context):
        self.layout.operator(ImportChunkGSC.bl_idname, text='GSC Chunk Importer (.gsc)')
def register():
        bpy.utils.register_class(ImportChunkGSC)
        bpy.types.TOPBAR_MT_file_import.append(menu_func_import)
def unregister():
        bpy.utils.unregister_class(ImportChunkGSC)
        bpy.types.TOPBAR_MT_file_import.remove(menu_func_import)
if __name__ == '__main__': register()
