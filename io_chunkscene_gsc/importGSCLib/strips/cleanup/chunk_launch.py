from struct import unpack, pack
import os
import math
from .chunk_strips import *

def chunkLaunch(f, filepath):
    f.seek(0)
    wholeChunk1_none(f, filepath)
    f.seek(0)
