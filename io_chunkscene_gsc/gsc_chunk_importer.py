from struct import pack, unpack
import os
import bpy
import bmesh
import math
from io import BytesIO as bio
from .importGSCLib.strips.cleanup.chunk_strips import *    
            
        
        

def parse_gsc(filepath, Triangle_Strips=False):
    with open(filepath, "rb") as f:
        if Triangle_Strips:
            wholeChunk1_none(f, filepath)
                



