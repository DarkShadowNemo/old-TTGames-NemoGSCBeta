from struct import unpack, pack
import bpy
import os
import math

def terC_(f):
    FileSize=0
    f.write(pack("<I", FileSize))

    for i, (obdata, ob) in enumerate(zip(bpy.data.meshes, bpy.data.objects)):
        if obdata.name == "Normal":
            f.write(pack("<H", 0))
            f.write(pack("<H", 1))
            coords=[
                ob.matrix_world @ v.co
                for v in obdata.vertices
            ]
            if coords:
                minx = min(v.x for v in coords)
                maxx = max(v.x for v in coords)

                minz = min(v.z for v in coords)
                maxz = max(v.z for v in coords)

                f.write(pack("<f", minx))
                f.write(pack("<f", minz))
                f.write(pack("<f", maxx))
                f.write(pack("<f", maxz))
                for v in coords:
                    f.write(pack("<f", v.co.x))
                    f.write(pack("<f", v.co.z))
                    f.write(pack("<f", v.co.y))
    size1 = f.seek(FileSize,2)
    f.seek(0)
    f.write(pack("<I", size1*2))
                
    
    
    
    

