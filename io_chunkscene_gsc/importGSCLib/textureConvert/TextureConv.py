from struct import unpack, pack
import os
import bpy
import math
from io import BytesIO as bio

def truncate_cstr(s: bytes) -> bytes:
    index = s.find(0)
    if index == -1: return s
    return s[:index]
def fetch_cstr(f: 'filelike') -> bytearray:
    build = bytearray()
    while 1:
        strbyte = f.read(1)
        if strbyte == b'\0' or not strbyte: break
        build += strbyte
    return build

def get_size_from_sub_hdr(f, is_pallete):
    size_ = unpack('<H', f.read(2))[0]
    f.seek(14, 1)
    
    if is_pallete == True:
        if (size_ == 0x8080):
            return 256
        else:
            raise Exception("unsupported pallete size %d" % size_)
    
    return (abs(size_ - 0x8000) << 4)

def get_size_from_sub_hdrpt2(f, is_pallete):
    size_ = unpack('<H', f.read(2))[0]
    f.seek(14, 1)
    
    if is_pallete == True:
        if (size_ == 0x8080):
            return 256
        else:
            raise Exception("unsupported pallete size %d" % size_)
    
    return (abs(size_ - 0x8000) << 4)

def get_size_from_sub_hdr2(f, is_pallete):
    size_ = unpack('<H', f.read(2))[0]
    f.seek(14, 1)
    
    if is_pallete == True:
        if (size_ == 0x8008):
            return 16
        else:
            raise Exception("unsupported pallete size %d" % size_)
    
    return (abs(size_ - 0x8000) << 4)

def read_pallete2(f, amt):
    global g_pallete5
    global g_pallete6
    global g_pallete7
    global g_pallete8
    global g_pallete1b
    g_pallete5 = []
    g_pallete6 = []
    g_pallete7 = []
    g_pallete8 = []
    g_pallete1b = []
    water_idx=0
    for i in range(0, amt):
        r = unpack('B', f.read(1))[0]/255
        g = unpack('B', f.read(1))[0]/255
        b = unpack('B', f.read(1))[0]/255
        a = unpack('B', f.read(1))[0]/127
        r1 = round(r,3)
        g1 = round(g,3)
        b1 = round(b,3)
        a1 = round(a,3)
        
        r1*=0
        g1*=0
        b1*=0
        a1*=0
        
        r1+=255
        g1+=255
        b1+=255
        a1+=127

        r1-=255
        g1-=255
        b1-=255
        a1-=127
        
        r1+=255
        g1+=255
        b1+=255
        a1+=127

        r1/=255
        g1/=255
        b1/=255
        a1/=127

        water_idx+=1
        if water_idx == 1:
            if r == 0 and g == 0 and b == 0 and a == 1:
                r1*=0
                g1*=0
                b1*=0
        elif water_idx == 2:
            if r == 0 and g == 0 and b == 0 and a == 1:
                r1*=0
                g1*=0
                b1*=0
        elif water_idx == 3:
            if r == 0 and g == 0 and b == 0 and a == 1:
                r1*=0
                g1*=0
                b1*=0
        elif water_idx == 4:
            if r == 0 and g == 0 and b == 0 and a == 1:
                r1*=0
                g1*=0
                b1*=0
        elif water_idx == 5:
            if r == 0 and g == 0 and b == 0 and a == 1:
                r1*=0
                g1*=0
                b1*=0
        elif water_idx == 6:
            if r == 0 and g == 0 and b == 0 and a == 1:
                r1*=0
                g1*=0
                b1*=0
        elif water_idx == 7:
            if r == 0 and g == 0 and b == 0 and a == 1:
                r1*=0
                g1*=0
                b1*=0
        elif water_idx == 8:
            if r == 0 and g == 0 and b == 0 and a == 1:
                r1*=0
                g1*=0
                b1*=0
        elif water_idx == 9:
            if r == 0 and g == 0 and b == 0 and a == 1:
                r1*=0
                g1*=0
                b1*=0
        elif water_idx == 10:
            if r == 0 and g == 0 and b == 0 and a == 1:
                r1*=0
                g1*=0
                b1*=0
        elif water_idx == 11:
            if r == 0 and g == 0 and b == 0 and a == 1:
                r1*=0
                g1*=0
                b1*=0
        elif water_idx == 12:
            if r == 0 and g == 0 and b == 0 and a == 1:
                r1*=0
                g1*=0
                b1*=0
        elif water_idx == 13:
            if r == 0 and g == 0 and b == 0 and a == 1:
                r1*=0
                g1*=0
                b1*=0
        elif water_idx == 14:
            if r == 0 and g == 0 and b == 0 and a == 1:
                r1*=0
                g1*=0
                b1*=0
        elif water_idx == 15:
            if r == 0 and g == 0 and b == 0 and a == 1:
                r1*=0
                g1*=0
                b1*=0
        elif water_idx == 16:
            if r == 0 and g == 0 and b == 0 and a == 1:
                r1*=0
                g1*=0
                b1*=0

        g_pallete1b.append([int(r*255),int(g*255),int(b*255),int(a*127)])
        
        g_pallete5.append(r1)
        g_pallete6.append(g1)
        g_pallete7.append(b1)
        g_pallete8.append(a1)

    

def read_pallete(f, amt):
    global g_pallete1
    global g_pallete2
    global g_pallete3
    global g_pallete4
    global g_pallete1a
    g_pallete1 = []
    g_pallete2 = []
    g_pallete3 = []
    g_pallete4 = []
    g_pallete1a = []
    for i in range(0, amt):
        r = unpack('B', f.read(1))[0]/255
        g = unpack('B', f.read(1))[0]/255
        b = unpack('B', f.read(1))[0]/255
        a = unpack('B', f.read(1))[0]/127
        r1 = round(r,3)
        g1 = round(g,3)
        b1 = round(b,3)
        a1 = round(a,3)
        
        r1*=0
        g1*=0
        b1*=0
        a1*=0
        
        r1+=255
        g1+=255
        b1+=255
        a1+=127

        r1-=255
        g1-=255
        b1-=255
        a1-=127
        
        r1+=255
        g1+=255
        b1+=255
        a1+=127

        r1/=255
        g1/=255
        b1/=255
        a1/=127

        r1=r
        g1=g
        b1=b
        a1=a

        g_pallete1a.append([int(r*255),int(g*255),int(b*255),int(a*127)])
        
        g_pallete1.append(r1)
        g_pallete2.append(g1)
        g_pallete3.append(b1)
        g_pallete4.append(a1)

    f.seek(32,1)
    size1 = unpack("<I", f.read(4))[0]
    size2 = unpack("<I", f.read(4))[0]
    type1 = unpack("<I", f.read(4))[0]
    type2 = unpack("<I", f.read(4))[0]
    if type2 == 0:
        f.seek(48,1)
        height = unpack("<I", f.read(4))[0]
        width = unpack("<I", f.read(4))[0]
        f.seek(40,1)
        for x in range(0,width,1):
            for y in range(0,height,1):
                idx = unpack("B", f.read(1))[0]
        f.seek(80,1)
        
    elif type2 != 0:
        padsize1 = unpack("<I", f.read(4))[0]
        f.seek(padsize1,1)
        f.seek(48,1)
        height = unpack("<I", f.read(4))[0]
        width = unpack("<I", f.read(4))[0]
        f.seek(40,1)
        for x in range(0,width,1):
            for y in range(0,height,1):
                idx = unpack("B", f.read(1))[0]
        f.seek(80,1)

def parse_file2(f):
    global g_image_data2
    global width_
    global height_
    global some_width
    global some_height
    f.seek(0)
    Chunks = f.read()
    f.seek(0)

    while f.tell() < len(Chunks):
        Chunk = unpack("<I", f.read(4))[0]
        if Chunk == 208:
            f.seek(-20,1)
            height_ = unpack("<H", f.read(2))[0]
            type_1 = unpack("<H", f.read(2))[0]
            width_ = unpack("<H", f.read(2))[0]
            some_width = width_ * -1
            some_height = height_ // 2
            zero_1 = unpack("<H", f.read(2))[0]
            pitch = unpack("<I", f.read(4))[0]
            flag1 = unpack("B", f.read(1))[0]
            flag2 = unpack("B", f.read(1))[0]
            flag3 = unpack("B", f.read(1))[0]
            flags4 = unpack("B", f.read(1))[0]&0x80
            offset_pallete2 = unpack("<I", f.read(4))[0]
            
            size2 = unpack("<I", f.read(4))[0]
            type1 = unpack("<I", f.read(4))[0]
            type2 = unpack("<I", f.read(4))[0]
            if type2 == 0:
                textureRumble = unpack("B", f.read(1))[0]
                textureBrightness = unpack("B", f.read(1))[0]
                z1 = unpack("B", f.read(1))[0]
                flag5 = unpack("B", f.read(1))[0]
                z2 = unpack("<I", f.read(4))[0]
                z3 = unpack("<I", f.read(4))[0]
                textureRumble2 = unpack("B", f.read(1))[0]
                textureBrightness2 = unpack("B", f.read(1))[0]
                z1a = unpack("B", f.read(1))[0]
                flag6 = unpack("B", f.read(1))[0]
                unknown = unpack("<I", f.read(4))[0]
                depth = unpack(">I", f.read(4))[0]
                flag7 = unpack("<I", f.read(4))[0]
                null6 = unpack("<I", f.read(4))[0]
                null7 = unpack("<I", f.read(4))[0]
                null8 = unpack("<I", f.read(4))[0]
                flag8 = unpack("<I", f.read(4))[0]
                null9 = unpack("<I", f.read(4))[0]
                compressionHeight = unpack("<I", f.read(4))[0]
                compressionWidth = unpack("<I", f.read(4))[0]
                flag9 = unpack("<I", f.read(4))[0]
                null10 = unpack("<I", f.read(4))[0]
                null11 = unpack("<I", f.read(4))[0]
                null12 = unpack("<I", f.read(4))[0]
                flag10 = unpack("<I", f.read(4))[0]
                null13 = unpack("<I", f.read(4))[0]

                entries_amt2 = get_size_from_sub_hdr2(f, True)
                v1 = 1
                
                if entries_amt2 == 16:
                    v1 = 2
                if offset_pallete2 == 208:
                    read_pallete2(f, entries_amt2)

                    f.seek(32,1)
                    img_size2 = get_size_from_sub_hdr2(f, False)
                    g_image_data2 = bytes(f.read(img_size2))
                    return (width_, v1 * img_size2 // width_%width_+1, True)
    
def parse_file(f):
    global g_image_data
    global width_
    global height_
    global some_width
    global some_height
    f.seek(0)
    Chunks = f.read()
    f.seek(0)

    while f.tell() < len(Chunks):
        Chunk = f.read(4)
        if Chunk == b"\x90\x04\x00\x00":
            f.seek(-20,1)
            height_ = unpack("<H", f.read(2))[0]
            type_1 = unpack("<H", f.read(2))[0]
            width_ = unpack("<H", f.read(2))[0]
            some_width = width_ * -1
            some_height = height_ // 2
            zero_1 = unpack("<H", f.read(2))[0]
            pitch = unpack("<I", f.read(4))[0]
            flag1 = unpack("B", f.read(1))[0]
            flag2 = unpack("B", f.read(1))[0]
            flag3 = unpack("B", f.read(1))[0]
            flags4 = unpack("B", f.read(1))[0]&0x80
            offset_pallete = unpack("<I", f.read(4))[0]
            
            size2 = unpack("<I", f.read(4))[0]
            type1 = unpack("<I", f.read(4))[0]
            type2 = unpack("<I", f.read(4))[0]
            if type2 == 0:
                textureRumble = unpack("B", f.read(1))[0]
                textureBrightness = unpack("B", f.read(1))[0]
                z1 = unpack("B", f.read(1))[0]
                flag5 = unpack("B", f.read(1))[0]
                z2 = unpack("<I", f.read(4))[0]
                z3 = unpack("<I", f.read(4))[0]
                textureRumble2 = unpack("B", f.read(1))[0]
                textureBrightness2 = unpack("B", f.read(1))[0]
                z1a = unpack("B", f.read(1))[0]
                flag6 = unpack("B", f.read(1))[0]
                unknown = unpack("<I", f.read(4))[0]
                depth = unpack(">I", f.read(4))[0]
                flag7 = unpack("<I", f.read(4))[0]
                null6 = unpack("<I", f.read(4))[0]
                null7 = unpack("<I", f.read(4))[0]
                null8 = unpack("<I", f.read(4))[0]
                flag8 = unpack("<I", f.read(4))[0]
                null9 = unpack("<I", f.read(4))[0]
                compressionHeight = unpack("<I", f.read(4))[0]
                compressionWidth = unpack("<I", f.read(4))[0]
                flag9 = unpack("<I", f.read(4))[0]
                null10 = unpack("<I", f.read(4))[0]
                null11 = unpack("<I", f.read(4))[0]
                null12 = unpack("<I", f.read(4))[0]
                flag10 = unpack("<I", f.read(4))[0]
                null13 = unpack("<I", f.read(4))[0]

                entries_amt = get_size_from_sub_hdr(f, True)
                v1 = 1
                
                if entries_amt == 16:
                    v1 = 2
                if offset_pallete == 1168:
                    read_pallete(f, entries_amt)
                    img_size = get_size_from_sub_hdr(f, False)
                    g_image_data = bytes(f.read(img_size))
                    return (width_, v1 * img_size // width_%width_+width_, True)
            
def shift_array_bytes(arr, shift):
    arr_len = len(arr)
    if shift < 1:
        shift = arr_len - shift
    for i in range(arr_len - 1):
        tmp = arr[i]
        arr[i] = arr[(i+shift) % arr_len]
        arr[(i+shift) % arr_len] = tmp

def uninterlace_array_2bytes(arr, is_2nd, y):
    if(len(arr) != 16):
        raise Exception("len(arr) must be 16 bytes")
    
    arr_left = []
    arr_right = []
    
    if not is_2nd:
        shift_array_bytes(arr, 1)
        for i in range(4):
            arr_left.append(arr[i*4+2])
            arr_left.append(arr[i*4+3])
            arr_right.append(arr[i*4+0])
            arr_right.append(arr[i*4+1])
        
        #shift_array_bytes(arr_left, 0)
        px1 = arr_left[1]
        px2 = arr_left[3]
        px3 = arr_left[5]
        px0 = arr_left[7]
        arr_left[1] = px0
        arr_left[3] = px1
        arr_left[5] = px2
        arr_left[7] = px3
        
    else:
        shift_array_bytes(arr, -1)
        for i in range(4):
            arr_left.append(arr[i*4+0])
            arr_left.append(arr[i*4+1])
            arr_right.append(arr[i*4+2])
            arr_right.append(arr[i*4+3])
        #shift_array_bytes(arr_right, 0)
        px1 = arr_right[1]
        px2 = arr_right[3]
        px3 = arr_right[5]
        px0 = arr_right[7]
        arr_right[1] = px0
        arr_right[3] = px1
        arr_right[5] = px2
        arr_right[7] = px3
    
    return arr_left + arr_right

def copy_arr_to_arr_at_offset(offset, arr1, arr2):
    if len(arr1) < len(arr2):
        raise Exception("copy arr1 < arr2")
    
    if offset > len(arr1) - len(arr2):
        raise Exception("offset to big to copy")
    
    #print(offset, len(arr1), len(arr2))
    
    for i in range(len(arr2)):
        arr1[offset + i] = arr2[i]
    
def xy_to_yx(idx):
    x = idx % 16
    y = idx // 16
    return (y + x*16)

def idx_test(idx):
    #if idx*2 > 255:
    #   return idx*2 % 255
    #else:
    #   return idx*2 + 1
    
    #if (idx//16)*2 > 15:
    #   return ((idx//16)*2 % 15)*16 + 16 + idx % 16
    #else:
    #   return ((idx//16)*2 % 15)*16 + idx % 16
    
    #swap_arr = [+7, +5, +3, +1, -1, -3, -5, -7]
    #amt = 16
    #return idx + (amt - 1 - 2*(idx % amt))
    return idx
    

def make_test_image_256():
    global g_image_data
    arr = []
    for i in range(256*256):
        arr.append(i%64)
    g_image_data = arr

def blender_gsc_texture_convert(f):
    f.seek(0)
    parse_file2(f)
    if len(g_pallete5) == 16 and len(g_pallete6) == 16 and len(g_pallete7) == 16 and len(g_pallete8) == 16:
        im = bpy.data.images.new(name="GSC 0x8008", width=width_, height=height_, alpha=True)
        num_Pixels = len(im.pixels)
        def grid(x,y):
            return x + width_*y
        def drawPixel(x,y,R,G,B,A):
            pixelNumber = grid(x,y) * 4
             
            im.pixels[pixelNumber] = R
            im.pixels[pixelNumber+1] = G
            im.pixels[pixelNumber+2] = B
            im.pixels[pixelNumber+3] = A
        def replace_pixel(image, x, y, new_rgba):
            width = image.size[0]
            height = image.size[1]

            # Validate coordinates
            if not (0 <= x < width and 0 <= y < height):
                raise ValueError(f"Pixel coordinates ({x},{y}) out of range.")

            if len(new_rgba) != 4:
                raise ValueError("RGBA must have exactly 4 values.")

            # Blender stores pixels in a flat array: [R, G, B, A, R, G, B, A, ...]
            # Pixel index in array:
            index = (y * width + x) * 4

            # Replace pixel values
            for i in range(4):
                image.pixels[index + i] = float(new_rgba[i])
            
        def shift_and_stretch_black_pixels(image_name, black_threshold=0.05):
            """
            Shifts black pixels horizontally by replacing them with the nearest non-black neighbor.
            Then stretches pixels to cover black lines.
            
            :param image_name: Name of the image in bpy.data.images
            :param black_threshold: Threshold to detect black pixels (0.0 - 1.0)
            """
            # Get the image
            im = bpy.data.images.get(image_name)
            if not im:
                print(f"Image '{image_name}' not found.")
                return
            
            if im.pixels is None or len(im.pixels) == 0:
                print("Image has no pixel data.")
                return

            width, height = im.size
            pixels = list(im.pixels)  # Copy to a list for editing

            def is_black(r, g, b, threshold):
                return (r <= threshold and g <= threshold and b <= threshold)

            # Pass 1: Shift black pixels horizontally
            for y in range(height):
                for x in range(width):
                    idx = (y * width + x) * 4
                    r, g, b, a = pixels[idx:idx+4]

                    if is_black(r, g, b, black_threshold):
                        # Look left first
                        found = False
                        for lx in range(x - 1, -1, -1):
                            li = (y * width + lx) * 4
                            lr, lg, lb, la = pixels[li:li+4]
                            if not is_black(lr, lg, lb, black_threshold):
                                pixels[idx:idx+4] = [lr, lg, lb, la]
                                found = True
                                break

                        # If not found on left, look right
                        if not found:
                            for rx in range(x + 1, width):
                                ri = (y * width + rx) * 4
                                rr, rg, rb, ra = pixels[ri:ri+4]
                                if not is_black(rr, rg, rb, black_threshold):
                                    pixels[idx:idx+4] = [rr, rg, rb, ra]
                                    break

            # Pass 2: Stretch vertically to cover any remaining black lines
            for y in range(height):
                for x in range(width):
                    idx = (y * width + x) * 4
                    r, g, b, a = pixels[idx:idx+4]

                    if is_black(r, g, b, black_threshold):
                        # Look up
                        found = False
                        for uy in range(y - 1, -1, -1):
                            ui = (uy * width + x) * 4
                            ur, ug, ub, ua = pixels[ui:ui+4]
                            if not is_black(ur, ug, ub, black_threshold):
                                pixels[idx:idx+4] = [ur, ug, ub, ua]
                                found = True
                                break

                        # Look down if not found
                        if not found:
                            for dy in range(y + 1, height):
                                di = (dy * width + x) * 4
                                dr, dg, db, da = pixels[di:di+4]
                                if not is_black(dr, dg, db, black_threshold):
                                    pixels[idx:idx+4] = [dr, dg, db, da]
                                    break

            im.pixels[:] = pixels
            im.update()
            print(f"Black pixels in '{image_name}' shifted and stretched successfully.")

        img_0x8008_idx=0

        if img_0x8008_idx==0:
            
            
            for x in range(width_):
                for y in range(height_):
                    idx = g_image_data2[x // 2 + y*width_ // 2] & 0xF
                    if x % 2 == 1:
                        idx = (g_image_data2[x // 2 + y*width_ // 2]& 0xF0) >> 4
                        drawPixel(x,y,g_pallete5[idx],g_pallete6[idx],g_pallete7[idx],g_pallete8[idx])

            shift_and_stretch_black_pixels("GSC 0x8008", black_threshold=0.05)
            #im = bpy.data.images.get("GSC 0x8008")
            #if im is None:
            #raise RuntimeError("Image not found. Load gsc 0x8008 image first.")
            #replace_pixel(im, 62, 63, (0.098000,0.352000,0.578000,1.000000))
            #replace_pixel(im, 63, 63, (0.080000,0.332000,0.527000,1.000000))
            #im.update()
            #print("Pixel replaced successfully.")
            img_0x8008_idx+=1
            if img_0x8008_idx == 1:
                try:
                    image_name = "GSC 0x8008.001"
                    img = bpy.data.images[image_name]
                    bpy.data.images.remove(img)
                except:
                    KeyError
    f.seek(0) 
    parse_file(f)
            
        
    if len(g_pallete1) == 256 and len(g_pallete2) == 256 and len(g_pallete3) == 256 and len(g_pallete4) == 256 and height_ < 128 and width_ < 128:
        im = bpy.data.images.new(name="GSC 0x8080", width=width_, height=height_, alpha=True)
        num_Pixels = len(im.pixels)
        def grid(x,y):
            return x + width_*y
        def drawPixel(x,y,R,G,B,A):
            pixelNumber = grid(x,y) * 4
             
            im.pixels[pixelNumber] = R
            im.pixels[pixelNumber+1] = G
            im.pixels[pixelNumber+2] = B
            im.pixels[pixelNumber+3] = A

                 
        for x in range(width_):
            for y in range(height_):
                idx = g_image_data[x + y*width_]
                drawPixel(x,y,g_pallete1[idx],g_pallete2[idx],g_pallete3[idx],g_pallete4[idx])
    if len(g_pallete1) == 256 and len(g_pallete2) == 256 and len(g_pallete3) == 256 and len(g_pallete4) == 256 and (height_ == 256 and width_ == 256 or height_ == 128 and width_ == 128):
        for y in range(some_height):
            for x in range(some_width // 16):
                arr_int = g_image_data[y*some_width + x*16: y*some_width + x*16 + 16]
                arr_unint = uninterlace_array_2bytes(arr_int, True if y % 4 > 1 else False, y)
                copy_arr_to_arr_at_offset(y*some_width + x*16, g_image_data, arr_unint)
        im = bpy.data.images.new(name="GSC 0x8080", width=width_, height=height_, alpha=True)
        num_Pixels = len(im.pixels)
        def grid(x,y):
            return x + width_*y
        def drawPixel(x,y,R,G,B,A):
            pixelNumber = grid(x,y) * 4
             
            im.pixels[pixelNumber] = R
            im.pixels[pixelNumber+1] = G
            im.pixels[pixelNumber+2] = B
            im.pixels[pixelNumber+3] = A
        for y in range(height_ // 2):
            for x in range(width_):
                idx1 = g_image_data[2*y*width_ + 1*x + 0]
                idx2 = g_image_data[2*y*width_ + 1*x + 1]
                 
                drawPixel(x,y*2+0, g_pallete1[idx_test(idx1)],g_pallete2[idx_test(idx1)],g_pallete3[idx_test(idx1)],g_pallete4[idx_test(idx1)])
                drawPixel(x,y*2+1, g_pallete1[idx_test(idx2)],g_pallete2[idx_test(idx2)],g_pallete3[idx_test(idx2)],g_pallete4[idx_test(idx2)])
