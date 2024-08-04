from struct import pack, unpack
import bpy
import math
import os
from .exportGSCLib.strips.strips_0x030100010380XX6C import *
from .exportGSCLib.strips.strips_0x03010001010000050380XX65 import *
from .exportGSCLib.strips.strips_0x030100010380XX6C_with_textures2 import *
from .exportGSCLib.strips.strips_0x030100010380XX6C_Connecters import *

#primtype

"""
NUPT_POINT = 0, # invalid
NUPT_LINE = 1, # invalid
NUPT_TRI = 2, # invalid
NUPT_TRISTRIP = 3, # invalid
NUPT_NDXLINE = 4, # invalid
NUPT_NDXTRI = 5, # invalid
NUPT_NDXTRISTRIP = 6, # valid
NUPT_BEZPATCH = 7, # invalid
NUPT_BEZTRI = 8, # invalid
NUPT_FACEON = 9 # invalid
"""

def NUWrite(filepath, ofsetsOne=False,ofsetsOneC=False,ofsetsOneIMG=False):
    with open(filepath, "wb") as f:
        if ofsetsOne:
            vertices_0x03010010380XX6C_(f)
        if ofsetsOneIMG:
            vertices_0x030100010380XX6C_with_texture2_(f)
        if ofsetsOneC:
            vertices_0x03010010380XX6C_Connection(f)
    
