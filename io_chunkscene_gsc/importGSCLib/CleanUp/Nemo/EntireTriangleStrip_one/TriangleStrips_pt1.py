from struct import unpack, pack
import os
import bpy
import math
import glob


def wholeChunk1(f, filepath):
    #TODO Directory
    if os.path.basename(filepath) == r"luxo_04.gsc":
        
        vertices=[]
        faces=[]
        normals=[]
        uvs=[]
        colors=[]
        fa=-1
        fb=0
        fc=1
        f.seek(0)
        while 1:
            Chunk = f.read(4)
            if Chunk == b"\x03\x01\x00\x01":
                flag1 = unpack("B", f.read(1))[0]
                f.seek(1,1)
                vertexCount = unpack("B", f.read(1))[0]
                flag2 = unpack("B", f.read(1))[0]
                for i in range(vertexCount):
                    vx = unpack("<f", f.read(4))[0]
                    vy = unpack("<f", f.read(4))[0]
                    vz = unpack("<f", f.read(4))[0]
                    vw = unpack("<f", f.read(4))[0]
                    vertices.append([vx,vz,vy])
                    normals.append([0,0,1])

                for i in range(vertexCount-2):
                    fa+=1
                    fb+=1
                    fc+=1
                    faces.append([fa,fb,fc])
                if len(vertices) == 7114:
                    if faces.remove([485,486,487]):
                        pass
                    elif faces.remove([487,488,489]):
                        pass
                    elif faces.remove([488,489,490]):
                        pass
                    elif faces.remove([119,120,121]):
                        pass
                    elif faces.remove([484,485,486]):
                        pass
                    elif faces.remove([5052,5053,5054]):
                        pass
                    elif faces.remove([5853,5854,5855]):
                        pass
                    elif faces.remove([5758,5759,5760]):
                        pass
                    elif faces.remove([3766,3767,3768]):
                        pass
                    elif faces.remove([4422,4423,4424]):
                        pass
                    elif faces.remove([4421,4422,4423]):
                        pass
                    elif faces.remove([2839,2840,2841]):
                        pass
                    elif faces.remove([1432,1433,1434]):
                        pass
                    elif faces.remove([1497,1498,1499]):
                        pass
                    elif faces.remove([1453,1454,1455]):
                        pass
                    elif faces.remove([1454,1455,1456]):
                        pass
                    elif faces.remove([1632,1633,1634]):
                        pass
                    elif faces.remove([5049,5050,5051]):
                        pass
                    elif faces.remove([3887,3888,3889]):
                        pass
                    elif faces.remove([3888,3889,3890]):
                        pass
                    elif faces.remove([4005,4006,4007]):
                        pass
                    elif faces.remove([4006,4007,4008]):
                        pass
                    elif faces.remove([6036,6037,6038]):
                        pass
                    elif faces.remove([6102,6103,6104]):
                        pass
                    elif faces.remove([3172,3173,3174]):
                        pass
                    elif faces.remove([2936,2937,2938]):
                        pass
                    elif faces.remove([2840,2841,2842]):
                        pass
                    elif faces.remove([3173,3174,3175]):
                        pass
                    elif faces.remove([2937,2938,2939]):
                        pass
                    elif faces.remove([3289,3290,3291]):
                        pass
                    elif faces.remove([6095,6096,6097]):
                        pass
                    elif faces.remove([1088,1089,1090]):
                        pass
                    elif faces.remove([6103,6104,6105]):
                        pass
                    elif faces.remove([1096,1097,1098]):
                        pass
                    elif faces.remove([1095,1096,1097]):
                        pass
                    elif faces.remove([6164,6165,6166]):
                        pass
                    elif faces.remove([1156,1157,1158]):
                        pass
                    elif faces.remove([1155,1156,1157]):
                        pass
                    elif faces.remove([6163,6164,6165]):
                        pass
                    elif faces.remove([1565,1566,1567]):
                        pass
                    elif faces.remove([1566,1567,1568]):
                        pass
                    elif faces.remove([1410,1411,1412]):
                        pass
                    elif faces.remove([1431,1432,1433]):
                        pass
                    elif faces.remove([1475,1476,1477]):
                        pass
                    elif faces.remove([1519,1520,1521]):
                        pass
                    elif faces.remove([6246,6247,6248]):
                        pass
                    elif faces.remove([2004,2005,2006]):
                        pass
                    elif faces.remove([2741,2742,2743]):
                        pass
                    elif faces.remove([2740,2741,2742]):
                        pass
                    elif faces.remove([1973,1974,1975]):
                        pass
                    elif faces.remove([1974,1975,1976]):
                        pass
                    elif faces.remove([1752,1753,1754]):
                        pass
                    elif faces.remove([1753,1754,1755]):
                        pass
                    elif faces.remove([5048,5049,5050]):
                        pass
                    elif faces.remove([5047,5048,5049]):
                        pass
                    elif faces.remove([5046,5047,5048]):
                        pass
                    elif faces.remove([1543,1544,1545]):
                        pass
                    elif faces.remove([1542,1543,1544]):
                        pass
                    elif faces.remove([1618,1619,1620]):
                        pass
                    elif faces.remove([1476,1477,1478]):
                        pass
                    elif faces.remove([1590,1591,1592]):
                        pass
                    elif faces.remove([1970,1971,1972]):
                        pass
                    elif faces.remove([1928,1929,1930]):
                        pass
                    elif faces.remove([1929,1930,1931]):
                        pass
                    elif faces.remove([5045,5046,5047]):
                        pass
                    elif faces.remove([5044,5045,5046]):
                        pass
                    elif faces.remove([1971,1972,1973]):
                        pass
                    elif faces.remove([1825,1826,1827]):
                        pass
                    elif faces.remove([1824,1825,1826]):
                        pass
                    elif faces.remove([1961,1962,1963]):
                        pass
                    elif faces.remove([1962,1963,1964]):
                        pass
                    elif faces.remove([1968,1969,1970]):
                        pass
                    elif faces.remove([1967,1968,1969]):
                        pass
                    elif faces.remove([1913,1914,1915]):
                        pass
                    elif faces.remove([1912,1913,1914]):
                        pass
                    elif faces.remove([1934,1935,1936]):
                        pass
                    elif faces.remove([1933,1934,1935]):
                        pass
                    elif faces.remove([1777,1778,1779]):
                        pass
                    elif faces.remove([1776,1777,1778]):
                        pass
                    elif faces.remove([1893,1894,1895]):
                        pass
                    elif faces.remove([1892,1893,1894]):
                        pass
                    elif faces.remove([1938,1939,1940]):
                        pass
                    elif faces.remove([1939,1940,1941]):
                        pass
                    elif faces.remove([1804,1805,1806]):
                        pass
                    elif faces.remove([1869,1870,1871]):
                        pass
                    elif faces.remove([1846,1847,1848]):
                        pass
                    elif faces.remove([1868,1869,1870]):
                        pass
                    elif faces.remove([1805,1806,1807]):
                        pass
                    elif faces.remove([1847,1848,1849]):
                        pass
                    elif faces.remove([6096,6097,6098]):
                        pass
                    elif faces.remove([1089,1090,1091]):
                        pass
                    elif faces.remove([1227,1228,1229]):
                        pass
                    elif faces.remove([1228,1229,1230]):
                        pass
                    elif faces.remove([6222,6223,6224]):
                        pass
                    elif faces.remove([6223,6224,6225]):
                        pass
                    elif faces.remove([6239,6240,6241]):
                        pass
                    elif faces.remove([6238,6239,6240]):
                        pass
                    elif faces.remove([1098,1099,1100]):
                        pass
                    elif faces.remove([6105,6106,6107]):
                        pass
                    elif faces.remove([3676,3677,3678]):
                        pass
                    elif faces.remove([3311,3312,3313]):
                        pass
                    elif faces.remove([3312,3313,3314]):
                        pass
                    elif faces.remove([3401,3402,3403]):
                        pass
                    elif faces.remove([3402,3403,3404]):
                        pass
                    elif faces.remove([3301,3302,3303]):
                        pass
                    elif faces.remove([3300,3301,3302]):
                        pass
                    elif faces.remove([3064,3065,3066]):
                        pass
                    elif faces.remove([3075,3076,3077]):
                        pass
                    elif faces.remove([3076,3077,3078]):
                        pass
                    elif faces.remove([3065,3066,3067]):
                        pass
                    elif faces.remove([6228,6229,6230]):
                        pass
                    elif faces.remove([6106,6107,6108]):
                        pass
                    elif faces.remove([1099,1100,1101]):
                        pass
                    elif faces.remove([6229,6230,6231]):
                        pass
                    elif faces.remove([6173,6174,6175]):
                        pass
                    elif faces.remove([1165,1166,1167]):
                        pass
                    elif faces.remove([6181,6182,6183]):
                        pass
                    elif faces.remove([6174,6175,6176]):
                        pass
                    elif faces.remove([1173,1174,1175]):
                        pass
                    elif faces.remove([6182,6183,6184]):
                        pass
                    elif faces.remove([1174,1175,1176]):
                        pass
                    elif faces.remove([1498,1499,1500]):
                        pass
                    elif faces.remove([1617,1618,1619]):
                        pass
                    elif faces.remove([1520,1521,1522]):
                        pass
                    elif faces.remove([1409,1410,1411]):
                        pass
                    elif faces.remove([6232,6233,6234]):
                        pass
                    elif faces.remove([6231,6232,6233]):
                        pass
                    elif faces.remove([1166,1167,1168]):
                        pass
                    elif faces.remove([3277,3278,3279]):
                        pass
                    elif faces.remove([3041,3042,3043]):
                        pass
                    elif faces.remove([6035,6036,6037]):
                        pass
                    elif faces.remove([42,43,44]):
                        pass
                    elif faces.remove([43,44,45]):
                        pass
                    elif faces.remove([120,121,122]):
                        pass
                    elif faces.remove([323,324,325]):
                        pass
                    elif faces.remove([324,325,326]):
                        pass
                    elif faces.remove([357,358,359]):
                        pass
                    elif faces.remove([358,359,360]):
                        pass
                    elif faces.remove([289,290,291]):
                        pass
                    elif faces.remove([290,291,292]):
                        pass
                    elif faces.remove([256,257,258]):
                        pass
                    elif faces.remove([255,256,257]):
                        pass
                    elif faces.remove([391,392,393]):
                        pass
                    elif faces.remove([392,393,394]):
                        pass
                    elif faces.remove([975,976,977]):
                        pass
                    elif faces.remove([634,635,636]):
                        pass
                    elif faces.remove([582,583,584]):
                        pass
                    elif faces.remove([980,981,982]):
                        pass
                    elif faces.remove([981,982,983]):
                        pass
                    elif faces.remove([583,584,585]):
                        pass
                    elif faces.remove([635,636,637]):
                        pass
                    elif faces.remove([463,464,465]):
                        pass
                    elif faces.remove([97,98,99]):
                        pass
                    elif faces.remove([98,99,100]):
                        pass
                    elif faces.remove([459,460,461]):
                        pass
                    elif faces.remove([460,461,462]):
                        pass
                    elif faces.remove([462,463,464]):
                        pass
                    elif faces.remove([425,426,427]):
                        pass
                    elif faces.remove([426,427,428]):
                        pass
                    elif faces.remove([221,222,223]):
                        pass
                    elif faces.remove([222,223,224]):
                        pass
                    elif faces.remove([187,188,189]):
                        pass
                    elif faces.remove([153,154,155]):
                        pass
                    elif faces.remove([154,155,156]):
                        pass
                    elif faces.remove([73,74,75]):
                        pass
                    elif faces.remove([72,73,74]):
                        pass
                    elif faces.remove([50,51,52]):
                        pass
                    elif faces.remove([539,540,541]):
                        pass
                    elif faces.remove([538,539,540]):
                        pass
                    elif faces.remove([872,873,874]):
                        pass
                    elif faces.remove([873,874,875]):
                        pass
                    elif faces.remove([906,907,908]):
                        pass
                    elif faces.remove([838,839,840]):
                        pass
                    elif faces.remove([907,908,909]):
                        pass
                    elif faces.remove([839,840,841]):
                        pass
                    elif faces.remove([974,975,976]):
                        pass
                    elif faces.remove([804,805,806]):
                        pass
                    elif faces.remove([805,806,807]):
                        pass
                    elif faces.remove([770,771,772]):
                        pass
                    elif faces.remove([771,772,773]):
                        pass
                    elif faces.remove([940,941,942]):
                        pass
                    elif faces.remove([941,942,943]):
                        pass
                    elif faces.remove([737,738,739]):
                        pass
                    elif faces.remove([536,537,538]):
                        pass
                    elif faces.remove([561,562,563]):
                        pass
                    elif faces.remove([560,561,562]):
                        pass
                    elif faces.remove([535,536,537]):
                        pass
                    elif faces.remove([597,598,599]):
                        pass
                    elif faces.remove([1029,1030,1031]):
                        pass
                    elif faces.remove([1028,1029,1030]):
                        pass
                    elif faces.remove([596,597,598]):
                        pass
                    elif faces.remove([585,586,587]):
                        pass
                    elif faces.remove([613,614,615]):
                        pass
                    elif faces.remove([612,613,614]):
                        pass
                    elif faces.remove([49,50,51]):
                        pass
                    elif faces.remove([4669,4670,4671]):
                        pass
                    elif faces.remove([5757,5758,5759]):
                        pass
                    elif faces.remove([5054,5055,5056]):
                        pass
                    elif faces.remove([5053,5054,5055]):
                        pass
                    elif faces.remove([5055,5056,5057]):
                        pass
                    elif faces.remove([3846,3847,3848]):
                        pass
                    elif faces.remove([3845,3846,3847]):
                        pass
                    elif faces.remove([3807,3808,3809]):
                        pass
                    elif faces.remove([3808,3809,3810]):
                        pass
                    elif faces.remove([6247,6248,6249]):
                        pass
                    elif faces.remove([1633,1634,1635]):
                        pass
                    elif faces.remove([2003,2004,2005]):
                        pass
                    elif faces.remove([5854,5855,5856]):
                        pass
                    elif faces.remove([4081,4082,4083]):
                        pass
                    elif faces.remove([4080,4081,4082]):
                        pass
                    elif faces.remove([4172,4173,4174]):
                        pass
                    elif faces.remove([4171,4172,4173]):
                        pass
                    elif faces.remove([4069,4070,4071]):
                        pass
                    elif faces.remove([4070,4071,4072]):
                        pass
                    elif faces.remove([4294,4295,4296]):
                        pass
                    elif faces.remove([4074,4075,4076]):
                        pass
                    elif faces.remove([4073,4074,4075]):
                        pass
                    elif faces.remove([4029,4030,4031]):
                        pass
                    elif faces.remove([4028,4029,4030]):
                        pass
                    elif faces.remove([4047,4048,4049]):
                        pass
                    elif faces.remove([4046,4047,4048]):
                        pass
                    elif faces.remove([4380,4381,4382]):
                        pass
                    elif faces.remove([4379,4380,4381]):
                        pass
                    elif faces.remove([4160,4161,4162]):
                        pass
                    elif faces.remove([4126,4127,4128]):
                        pass
                    elif faces.remove([4187,4188,4189]):
                        pass
                    elif faces.remove([4188,4189,4190]):
                        pass
                    elif faces.remove([4281,4282,4283]):
                        pass
                    elif faces.remove([4227,4228,4229]):
                        pass
                    elif faces.remove([4247,4248,4249]):
                        pass
                    elif faces.remove([4338,4339,4340]):
                        pass
                    elif faces.remove([4034,4035,4036]):
                        pass
                    elif faces.remove([4033,4034,4035]):
                        pass
                    elif faces.remove([4226,4227,4228]):
                        pass
                    elif faces.remove([4293,4294,4295]):
                        pass
                    elif faces.remove([4200,4201,4202]):
                        pass
                    elif faces.remove([4330,4331,4332]):
                        pass
                    elif faces.remove([4207,4208,4209]):
                        pass
                    elif faces.remove([4208,4209,4210]):
                        pass
                    elif faces.remove([4266,4267,4268]):
                        pass
                    elif faces.remove([4159,4160,4161]):
                        pass
                    elif faces.remove([4199,4200,4201]):
                        pass
                    elif faces.remove([4273,4274,4275]):
                        pass
                    elif faces.remove([4121,4122,4123]):
                        pass
                    elif faces.remove([4095,4096,4097]):
                        pass
                    elif faces.remove([4094,4095,4096]):
                        pass
                    elif faces.remove([4240,4241,4242]):
                        pass
                    elif faces.remove([4241,4242,4243]):
                        pass
                    elif faces.remove([4305,4306,4307]):
                        pass
                    elif faces.remove([4125,4126,4127]):
                        pass
                    elif faces.remove([4246,4247,4248]):
                        pass
                    elif faces.remove([4106,4107,4108]):
                        pass
                    elif faces.remove([4107,4108,4109]):
                        pass
                    elif faces.remove([4282,4283,4284]):
                        pass
                    elif faces.remove([4320,4321,4322]):
                        pass
                    elif faces.remove([4321,4322,4323]):
                        pass
                    elif faces.remove([4331,4332,4333]):
                        pass
                    elif faces.remove([4337,4338,4339]):
                        pass
                    elif faces.remove([4267,4268,4269]):
                        pass
                    elif faces.remove([4112,4113,4114]):
                        pass
                    elif faces.remove([4113,4114,4115]):
                        pass
                    elif faces.remove([4299,4300,4301]):
                        pass
                    elif faces.remove([4298,4299,4300]):
                        pass
                    elif faces.remove([4303,4304,4305]):
                        pass
                    elif faces.remove([4302,4303,4304]):
                        pass
                    elif faces.remove([4306,4307,4308]):
                        pass
                    elif faces.remove([4130,4131,4132]):
                        pass
                    elif faces.remove([4129,4130,4131]):
                        pass
                    elif faces.remove([4119,4120,4121]):
                        pass
                    elif faces.remove([4120,4121,4122]):
                        pass
                    elif faces.remove([4274,4275,4276]):
                        pass
                    elif faces.remove([5852,5853,5854]):
                        pass
                    elif faces.remove([4642,4643,4644]):
                        pass
                    elif faces.remove([4641,4642,4643]):
                        pass
                    elif faces.remove([5042,5043,5044]):
                        pass
                    elif faces.remove([5043,5044,5045]):
                        pass
                    elif faces.remove([1373,1374,1375]):
                        pass
                    elif faces.remove([2828,2829,2830]):
                        pass
                    elif faces.remove([5056,5057,5058]):
                        pass
                    elif faces.remove([5057,5058,5059]):
                        pass
                    elif faces.remove([5058,5059,5060]):
                        pass
                    elif faces.remove([5059,5060,5061]):
                        pass
                    elif faces.remove([6611,6612,6613]):
                        pass
                    elif faces.remove([6429,6430,6431]):
                        pass
                    elif faces.remove([6248,6249,6250]):
                        pass
                    elif faces.remove([5591,5592,5593]):
                        pass
                    elif faces.remove([5071,5072,5073]):
                        pass
                    elif faces.remove([6249,6250,6251]):
                        pass
                    elif faces.remove([5409,5410,5411]):
                        pass
                    elif faces.remove([5227,5228,5229]):
                        pass
                    elif faces.remove([5070,5071,5072]):
                        pass
                    elif faces.remove([6626,6627,6628]):
                        pass
                    elif faces.remove([6444,6445,6446]):
                        pass
                    elif faces.remove([6262,6263,6264]):
                        pass
                    elif faces.remove([5869,5870,5871]):
                        pass
                    elif faces.remove([5592,5593,5594]):
                        pass
                    elif faces.remove([5410,5411,5412]):
                        pass
                    elif faces.remove([5228,5229,5230]):
                        pass
                    elif faces.remove([6627,6628,6629]):
                        pass
                    elif faces.remove([6445,6446,6447]):
                        pass
                    elif faces.remove([6263,6264,6265]):
                        pass
                    elif faces.remove([5870,5871,5872]):
                        pass
                    elif faces.remove([5576,5577,5578]):
                        pass
                    elif faces.remove([5394,5395,5396]):
                        pass
                    elif faces.remove([5212,5213,5214]):
                        pass
                    elif faces.remove([6583,6584,6585]):
                        pass
                    elif faces.remove([6401,6402,6403]):
                        pass
                    elif faces.remove([6008,6009,6010]):
                        pass
                    elif faces.remove([5730,5731,5732]):
                        pass
                    elif faces.remove([5548,5549,5550]):
                        pass
                    elif faces.remove([5366,5367,5368]):
                        pass
                    elif faces.remove([5184,5185,5186]):
                        pass
                    elif faces.remove([6582,6583,6584]):
                        pass
                    elif faces.remove([6400,6401,6402]):
                        pass
                    elif faces.remove([6007,6008,6009]):
                        pass
                    elif faces.remove([5729,5730,5731]):
                        pass
                    elif faces.remove([5547,5548,5549]):
                        pass
                    elif faces.remove([5365,5366,5367]):
                        pass
                    elif faces.remove([5183,5184,5185]):
                        pass
                    elif faces.remove([6610,6611,6612]):
                        pass
                    elif faces.remove([6428,6429,6430]):
                        pass
                    elif faces.remove([5575,5576,5577]):
                        pass
                    elif faces.remove([5393,5394,5395]):
                        pass
                    elif faces.remove([5211,5212,5213]):
                        pass
                    elif faces.remove([5683,5684,5685]):
                        pass
                    elif faces.remove([5501,5502,5503]):
                        pass
                    elif faces.remove([5319,5320,5321]):
                        pass
                    elif faces.remove([5137,5138,5139]):
                        pass
                    elif faces.remove([6536,6537,6538]):
                        pass
                    elif faces.remove([6354,6355,6356]):
                        pass
                    elif faces.remove([5961,5962,5963]):
                        pass
                    elif faces.remove([5684,5685,5686]):
                        pass
                    elif faces.remove([5502,5503,5504]):
                        pass
                    elif faces.remove([6537,6538,6539]):
                        pass
                    elif faces.remove([668,669,670]):
                        pass
                    elif faces.remove([1140,1141,1142]):
                        pass
                    elif faces.remove([188,189,190]):
                        pass
                    elif faces.remove([1126,1127,1128]):
                        pass
                    elif faces.remove([1620,1621,1622]):
                        pass
                    elif faces.remove([1621,1622,1623]):
                        pass
                    elif faces.remove([1127,1128,1129]):
                        pass
                    elif faces.remove([1595,1596,1597]):
                        pass
                    elif faces.remove([1596,1597,1598]):
                        pass
                    elif faces.remove([1589,1590,1591]):
                        pass
                    elif faces.remove([1627,1628,1629]):
                        pass
                    elif faces.remove([1628,1629,1630]):
                        pass
                    elif faces.remove([1118,1119,1120]):
                        pass
                    elif faces.remove([1119,1120,1121]):
                        pass
                    elif faces.remove([6126,6127,6128]):
                        pass
                    elif faces.remove([6125,6126,6127]):
                        pass
                    elif faces.remove([6201,6202,6203]):
                        pass
                    elif faces.remove([1194,1195,1196]):
                        pass
                    elif faces.remove([6200,6201,6202]):
                        pass
                    elif faces.remove([1193,1194,1195]):
                        pass
                    elif faces.remove([1038,1039,1040]):
                        pass
                    elif faces.remove([1234,1235,1236]):
                        pass
                    elif faces.remove([1233,1234,1235]):
                        pass
            elif Chunk == b"SST0":
                break
            
        mesh = bpy.data.meshes.new("luxo_04")
        mesh.from_pydata(vertices, [], faces)
        object = bpy.data.objects.new("luxo_04", mesh)
        bpy.context.collection.objects.link(object)
        
