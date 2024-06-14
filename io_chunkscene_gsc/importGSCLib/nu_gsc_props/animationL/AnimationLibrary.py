from struct import pack, unpack
import os
import bpy
import math

def get_Animation_LIBRARY(f):
    f.seek(0)
    ALIBread = f.read()
    ALIBsearch = ALIBread.find(b"\x41\x4C\x49\x42")
    if ALIBread != 0:
        f.seek(ALIBsearch,0)
        ALIBS = unpack("<I", f.read(4))[0]
        ALIBSize = unpack("<I", f.read(4))[0]
        ALIBcount = unpack("<I", f.read(4))[0]
        for i in range(ALIBcount):
            unknowns = unpack("<I", f.read(4))[0]
        unknown = unpack("<I", f.read(4))[0]
        count = unpack("<I", f.read(4))[0]
        floatcount = unpack("<f", f.read(4))[0]
        for i in range(unknown):
            pass
        
        bpy.context.scene.frame_current=1
        bpy.context.scene.frame_start=1
        bpy.context.scene.frame_end=int(floatcount)
