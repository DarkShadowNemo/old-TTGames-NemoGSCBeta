bl_info = {
        'name'			: 'Finding Nemo GSC Level Chunk Importer',
        'author'		: 'DarkShadow Nemo',
        'version'		: (17, 0, 0),
        'blender'		: (4, 0, 0),
        'location'		: 'File > Import-Export',
        'description'           : 'Import GSC one mesh chunk makes it easier',
        'support'               : 'COMMUNITY',
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
        
        Triangle_Strips: BoolProperty(
                name        = 'Strips and Tri',
                description = ' 0x03010001 all offsets if they match it imports all the whole chunk in being aligned up gets all or most of it, you may get some vertex without faces'
        )
        directory: StringProperty()
        filter_glob: StringProperty(default = '*.gsc', options = {'HIDDEN'})
        def execute(self, context):
                paths = [os.path.join(self.directory, name.name) for name in self.files]
                if not paths: paths.append(self.filepath)
                importlib.reload(gsc_chunk_importer)
                for path in paths: gsc_chunk_importer.parse_gsc(path, Triangle_Strips = self.Triangle_Strips)
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
        ofsetsVC_One : BoolProperty(
                name = "0x030100010380XX6C VC",
                description = "exports vertex colors with no uvs"
        )
        smooth_ofsetsOne : BoolProperty(
                name = "Smooth 0x030100010380XX6C",
                description = "exports no uvs and vertex colors but smooth"
        )

        ofsetsTwo : BoolProperty(
                name = "0x03010001010000050380XX65",
                description = "Exports no uvs and vertex colors"
        )

        ofsetsOneIMG : BoolProperty(
                name = "0x030100010380XX6C with textures",
                description = "exports uvs and vertex colors with textures"
        )

        ofsetsOneIMGTwo : BoolProperty(
                name = "0x030100010380XX6C with float textures",
                description = "exports uvs and vertex colors with textures with floats"
        )
        
        directory: StringProperty()
        filter_glob: StringProperty(default = '*.gsc', options = {'HIDDEN'})
        def execute(self, context):
            importlib.reload(gsc_chunk_exporter)
            gsc_chunk_exporter.NUWrite(self.filepath, ofsetsOne = self.ofsetsOne, ofsetsVC_One = self.ofsetsVC_One, smooth_ofsetsOne = self.smooth_ofsetsOne, ofsetsTwo = self.ofsetsTwo, ofsetsOneIMG = self.ofsetsOneIMG,ofsetsOneIMGTwo = self.ofsetsOneIMGTwo)
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
