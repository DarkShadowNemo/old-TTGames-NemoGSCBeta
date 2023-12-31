from struct import unpack, pack
import os
import bpy
import math
import glob


def wholeChunk1_alspier(f, filepath):
    #TODO Directory
    if os.path.basename(filepath) == r"alspier.gsc":
        
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
                if len(vertices) == 246502:
                    if faces.remove([80444,80445,80446]):
                        pass
                    elif faces.remove([52114,52115,52116]):
                        pass
                    elif faces.remove([60255,60256,60257]):
                        pass
                    elif faces.remove([60254,60255,60256]):
                        pass
                    elif faces.remove([172818,172819,172820]):
                        pass
                    elif faces.remove([171719,171720,171721]):
                        pass
                    elif faces.remove([171720,171721,171722]):
                        pass
                    elif faces.remove([85266,85267,85268]):
                        pass
                    elif faces.remove([88614,88615,88616]):
                        pass
                    elif faces.remove([88615,88616,88617]):
                        pass
                    elif faces.remove([86748,86749,86750]):
                        pass
                    elif faces.remove([171691,171692,171693]):
                        pass
                    elif faces.remove([61197,61198,61199]):
                        pass
                    elif faces.remove([52452,52453,52454]):
                        pass
                    elif faces.remove([161245,161246,161247]):
                        pass
                    elif faces.remove([145509,145510,145511]):
                        pass
                    elif faces.remove([212055,212056,212057]):
                        pass
                    elif faces.remove([210075,210076,210077]):
                        pass
                    elif faces.remove([208773,208774,208775]):
                        pass
                    elif faces.remove([206151,206152,206153]):
                        pass
                    elif faces.remove([204849,204850,204851]):
                        pass
                    elif faces.remove([203547,203548,203549]):
                        pass
                    elif faces.remove([174724,174725,174726]):
                        pass
                    elif faces.remove([172827,172828,172829]):
                        pass
                    elif faces.remove([169756,169757,169758]):
                        pass
                    elif faces.remove([167996,167997,167998]):
                        pass
                    elif faces.remove([144338,144339,144340]):
                        pass
                    elif faces.remove([80445,80446,80447]):
                        pass
                    elif faces.remove([52636,52637,52638]):
                        pass
                    elif faces.remove([172817,172818,172819]):
                        pass
                    elif faces.remove([173281,173282,173283]):
                        pass
                    elif faces.remove([172816,172817,172818]):
                        pass
                    elif faces.remove([171690,171691,171692]):
                        pass
                    elif faces.remove([108940,108941,108942]):
                        pass
                    elif faces.remove([108941,108942,108943]):
                        pass
                    elif faces.remove([152308,152309,152310]):
                        pass
                    elif faces.remove([151362,151363,151364]):
                        pass
                    elif faces.remove([152307,152308,152309]):
                        pass
                    elif faces.remove([151361,151362,151363]):
                        pass
                    elif faces.remove([144288,144289,144290]):
                        pass
                    elif faces.remove([149887,149888,149889]):
                        pass
                    elif faces.remove([151435,151436,151437]):
                        pass
                    elif faces.remove([151500,151501,151502]):
                        pass
                    elif faces.remove([150554,150555,150556]):
                        pass
                    elif faces.remove([151499,151500,151501]):
                        pass
                    elif faces.remove([150553,150554,150555]):
                        pass
                    elif faces.remove([61299,61300,61301]):
                        pass
                    elif faces.remove([115894,115895,115896]):
                        pass
                    elif faces.remove([125461,125462,125463]):
                        pass
                    elif faces.remove([87815,87816,87817]):
                        pass
                    elif faces.remove([79977,79978,79979]):
                        pass
                    elif faces.remove([141920,141921,141922]):
                        pass
                    elif faces.remove([179357,179358,179359]):
                        pass
                    elif faces.remove([130867,130868,130869]):
                        pass
                    elif faces.remove([125315,125316,125317]):
                        pass
                    elif faces.remove([173296,173297,173298]):
                        pass
                    elif faces.remove([123073,123074,123075]):
                        pass
                    elif faces.remove([173297,173298,173299]):
                        pass
                    elif faces.remove([178884,178885,178886]):
                        pass
                    elif faces.remove([141803,141804,141805]):
                        pass
                    elif faces.remove([128778,128779,128780]):
                        pass
                    elif faces.remove([161196,161197,161198]):
                        pass
                    elif faces.remove([32163,32164,32165]):
                        pass
                    elif faces.remove([125460,125461,125462]):
                        pass
                    elif faces.remove([125333,125334,125335]):
                        pass
                    elif faces.remove([117057,117058,117059]):
                        pass
                    elif faces.remove([52253,52254,52255]):
                        pass
                    elif faces.remove([52451,52452,52453]):
                        pass
                    elif faces.remove([34672,34673,34674]):
                        pass
                    elif faces.remove([178675,178676,178677]):
                        pass
                    elif faces.remove([173234,173235,173236]):
                        pass
                    elif faces.remove([173160,173161,173162]):
                        pass
                    elif faces.remove([173159,173160,173161]):
                        pass
                    elif faces.remove([173186,173187,173188]):
                        pass
                    elif faces.remove([173185,173186,173187]):
                        pass
                    elif faces.remove([173216,173217,173218]):
                        pass
                    elif faces.remove([173215,173216,173217]):
                        pass
                    elif faces.remove([173233,173234,173235]):
                        pass
                    elif faces.remove([173245,173246,173247]):
                        pass
                    elif faces.remove([173251,173252,173253]):
                        pass
                    elif faces.remove([173252,173253,173254]):
                        pass
                    elif faces.remove([173246,173247,173248]):
                        pass
                    elif faces.remove([173257,173258,173259]):
                        pass
                    elif faces.remove([173258,173259,173260]):
                        pass
                    elif faces.remove([173263,173264,173265]):
                        pass
                    elif faces.remove([173264,173265,173266]):
                        pass
                    elif faces.remove([173269,173270,173271]):
                        pass
                    elif faces.remove([173270,173271,173272]):
                        pass
                    elif faces.remove([173275,173276,173277]):
                        pass
                    elif faces.remove([173276,173277,173278]):
                        pass
                    elif faces.remove([173228,173229,173230]):
                        pass
                    elif faces.remove([173227,173228,173229]):
                        pass
                    elif faces.remove([173222,173223,173224]):
                        pass
                    elif faces.remove([173165,173166,173167]):
                        pass
                    elif faces.remove([173166,173167,173168]):
                        pass
                    elif faces.remove([173203,173204,173205]):
                        pass
                    elif faces.remove([173204,173205,173206]):
                        pass
                    elif faces.remove([173198,173199,173200]):
                        pass
                    elif faces.remove([173209,173210,173211]):
                        pass
                    elif faces.remove([173197,173198,173199]):
                        pass
                    elif faces.remove([173173,173174,173175]):
                        pass
                    elif faces.remove([173174,173175,173176]):
                        pass
                    elif faces.remove([173210,173211,173212]):
                        pass
                    elif faces.remove([173221,173222,173223]):
                        pass
                    elif faces.remove([173282,173283,173284]):
                        pass
                    elif faces.remove([173182,173183,173184]):
                        pass
                    elif faces.remove([173181,173182,173183]):
                        pass
                    elif faces.remove([173240,173241,173242]):
                        pass
                    elif faces.remove([173239,173240,173241]):
                        pass
                    elif faces.remove([173111,173112,173113]):
                        pass
                    elif faces.remove([173153,173154,173155]):
                        pass
                    elif faces.remove([173154,173155,173156]):
                        pass
                    elif faces.remove([173141,173142,173143]):
                        pass
                    elif faces.remove([173147,173148,173149]):
                        pass
                    elif faces.remove([173148,173149,173150]):
                        pass
                    elif faces.remove([173142,173143,173144]):
                        pass
                    elif faces.remove([173123,173124,173125]):
                        pass
                    elif faces.remove([173122,173123,173124]):
                        pass
                    elif faces.remove([173112,173113,173114]):
                        pass
                    elif faces.remove([173098,173099,173100]):
                        pass
                    elif faces.remove([173097,173098,173099]):
                        pass
                    elif faces.remove([173136,173137,173138]):
                        pass
                    elif faces.remove([173104,173105,173106]):
                        pass
                    elif faces.remove([173135,173136,173137]):
                        pass
                    elif faces.remove([173103,173104,173105]):
                        pass
                    elif faces.remove([173192,173193,173194]):
                        pass
                    elif faces.remove([173191,173192,173193]):
                        pass
                    elif faces.remove([173168,173169,173170]):
                        pass
                    elif faces.remove([173169,173170,173171]):
                        pass
                    elif faces.remove([173118,173119,173120]):
                        pass
                    elif faces.remove([173119,173120,173121]):
                        pass
                    elif faces.remove([173107,173108,173109]):
                        pass
                    elif faces.remove([173090,173091,173092]):
                        pass
                    elif faces.remove([173089,173090,173091]):
                        pass
                    elif faces.remove([172787,172788,172789]):
                        pass
                    elif faces.remove([172951,172952,172953]):
                        pass
                    elif faces.remove([172952,172953,172954]):
                        pass
                    elif faces.remove([172926,172927,172928]):
                        pass
                    elif faces.remove([171713,171714,171715]):
                        pass
                    elif faces.remove([171629,171630,171631]):
                        pass
                    elif faces.remove([171630,171631,171632]):
                        pass
                    elif faces.remove([171697,171698,171699]):
                        pass
                    elif faces.remove([172945,172946,172947]):
                        pass
                    elif faces.remove([174001,174002,174003]):
                        pass
                    elif faces.remove([171654,171655,171656]):
                        pass
                    elif faces.remove([171606,171607,171608]):
                        pass
                    elif faces.remove([171590,171591,171592]):
                        pass
                    elif faces.remove([171589,171590,171591]):
                        pass
                    elif faces.remove([171605,171606,171607]):
                        pass
                    elif faces.remove([173033,173034,173035]):
                        pass
                    elif faces.remove([172946,172947,172948]):
                        pass
                    elif faces.remove([172932,172933,172934]):
                        pass
                    elif faces.remove([172933,172934,172935]):
                        pass
                    elif faces.remove([172943,172944,172945]):
                        pass
                    elif faces.remove([172942,172943,172944]):
                        pass
                    elif faces.remove([172788,172789,172790]):
                        pass
                    elif faces.remove([172936,172937,172938]):
                        pass
                    elif faces.remove([172935,172936,172937]):
                        pass
                    elif faces.remove([172876,172877,172878]):
                        pass
                    elif faces.remove([172875,172876,172877]):
                        pass
                    elif faces.remove([172870,172871,172872]):
                        pass
                    elif faces.remove([171712,171713,171714]):
                        pass
                    elif faces.remove([171638,171639,171640]):
                        pass
                    elif faces.remove([171622,171623,171624]):
                        pass
                    elif faces.remove([171625,171626,171627]):
                        pass
                    elif faces.remove([171626,171627,171628]):
                        pass
                    elif faces.remove([171621,171622,171623]):
                        pass
                    elif faces.remove([171639,171640,171641]):
                        pass
                    elif faces.remove([171614,171615,171616]):
                        pass
                    elif faces.remove([171705,171706,171707]):
                        pass
                    elif faces.remove([171704,171705,171706]):
                        pass
                    elif faces.remove([171613,171614,171615]):
                        pass
                    elif faces.remove([171646,171647,171648]):
                        pass
                    elif faces.remove([171645,171646,171647]):
                        pass
                    elif faces.remove([171686,171687,171688]):
                        pass
                    elif faces.remove([171649,171650,171651]):
                        pass
                    elif faces.remove([171650,171651,171652]):
                        pass
                    elif faces.remove([171673,171674,171675]):
                        pass
                    elif faces.remove([171655,171656,171657]):
                        pass
                    elif faces.remove([171658,171659,171660]):
                        pass
                    elif faces.remove([171657,171658,171659]):
                        pass
                    elif faces.remove([171696,171697,171698]):
                        pass
                    elif faces.remove([171572,171573,171574]):
                        pass
                    elif faces.remove([171552,171553,171554]):
                        pass
                    elif faces.remove([171514,171515,171516]):
                        pass
                    elif faces.remove([34659,34660,34661]):
                        pass
                    elif faces.remove([47967,47968,47969]):
                        pass
                    elif faces.remove([141398,141399,141400]):
                        pass
                    elif faces.remove([141397,141398,141399]):
                        pass
                    elif faces.remove([141389,141390,141391]):
                        pass
                    elif faces.remove([141390,141391,141392]):
                        pass
                    elif faces.remove([32566,32567,32568]):
                        pass
                    elif faces.remove([141318,141319,141320]):
                        pass
                    elif faces.remove([141319,141320,141321]):
                        pass
                    elif faces.remove([47940,47941,47942]):
                        pass
                    elif faces.remove([47868,47869,47870]):
                        pass
                    elif faces.remove([47867,47868,47869]):
                        pass
                    elif faces.remove([115893,115894,115895]):
                        pass
                    elif faces.remove([61237,61238,61239]):
                        pass
                    elif faces.remove([172623,172624,172625]):
                        pass
                    elif faces.remove([172161,172162,172163]):
                        pass
                    elif faces.remove([172557,172558,172559]):
                        pass
                    elif faces.remove([172556,172557,172558]):
                        pass
                    elif faces.remove([171416,171417,171418]):
                        pass
                    elif faces.remove([171415,171416,171417]):
                        pass
                    elif faces.remove([171393,171394,171395]):
                        pass
                    elif faces.remove([171394,171395,171396]):
                        pass
                    elif faces.remove([171478,171479,171480]):
                        pass
                    elif faces.remove([171479,171480,171481]):
                        pass
                    elif faces.remove([173059,173060,173061]):
                        pass
                    elif faces.remove([171526,171527,171528]):
                        pass
                    elif faces.remove([171527,171528,171529]):
                        pass
                    elif faces.remove([171520,171521,171522]):
                        pass
                    elif faces.remove([171521,171522,171523]):
                        pass
                    elif faces.remove([171279,171280,171281]):
                        pass
                    elif faces.remove([171280,171281,171282]):
                        pass
                    elif faces.remove([171267,171268,171269]):
                        pass
                    elif faces.remove([171299,171300,171301]):
                        pass
                    elif faces.remove([171298,171299,171300]):
                        pass
                    elif faces.remove([171286,171287,171288]):
                        pass
                    elif faces.remove([171287,171288,171289]):
                        pass
                    elif faces.remove([88627,88628,88629]):
                        pass
                    elif faces.remove([88628,88629,88630]):
                        pass
                    elif faces.remove([212082,212083,212084]):
                        pass
                    elif faces.remove([125480,125481,125482]):
                        pass
                    elif faces.remove([118033,118034,118035]):
                        pass
                    elif faces.remove([161244,161245,161246]):
                        pass
                    elif faces.remove([123183,123184,123185]):
                        pass
                    elif faces.remove([173818,173819,173820]):
                        pass
                    elif faces.remove([178692,178693,178694]):
                        pass
                    elif faces.remove([178691,178692,178693]):
                        pass
                    elif faces.remove([178714,178715,178716]):
                        pass
                    elif faces.remove([172151,172152,172153]):
                        pass
                    elif faces.remove([172142,172143,172144]):
                        pass
                    elif faces.remove([172141,172142,172143]):
                        pass
                    elif faces.remove([172152,172153,172154]):
                        pass
                    elif faces.remove([172369,172370,172371]):
                        pass
                    elif faces.remove([172763,172764,172765]):
                        pass
                    elif faces.remove([172762,172763,172764]):
                        pass
                    elif faces.remove([172773,172774,172775]):
                        pass
                    elif faces.remove([172772,172773,172774]):
                        pass
                    elif faces.remove([172776,172777,172778]):
                        pass
                    elif faces.remove([172775,172776,172777]):
                        pass
                    elif faces.remove([172596,172597,172598]):
                        pass
                    elif faces.remove([171716,171717,171718]):
                        pass
                    elif faces.remove([173125,173126,173127]):
                        pass
                    elif faces.remove([173026,173027,173028]):
                        pass
                    elif faces.remove([173027,173028,173029]):
                        pass
                    elif faces.remove([171687,171688,171689]):
                        pass
                    elif faces.remove([173126,173127,173128]):
                        pass
                    elif faces.remove([171689,171690,171691]):
                        pass
                    elif faces.remove([171677,171678,171679]):
                        pass
                    elif faces.remove([171676,171677,171678]):
                        pass
                    elif faces.remove([172624,172625,172626]):
                        pass
                    elif faces.remove([173082,173083,173084]):
                        pass
                    elif faces.remove([173030,173031,173032]):
                        pass
                    elif faces.remove([173031,173032,173033]):
                        pass
                    elif faces.remove([173081,173082,173083]):
                        pass
                    elif faces.remove([171663,171664,171665]):
                        pass
                    elif faces.remove([171685,171686,171687]):
                        pass
                    elif faces.remove([171661,171662,171663]):
                        pass
                    elif faces.remove([171666,171667,171668]):
                        pass
                    elif faces.remove([171665,171666,171667]):
                        pass
                    elif faces.remove([173070,173071,173072]):
                        pass
                    elif faces.remove([173071,173072,173073]):
                        pass
                    elif faces.remove([171586,171587,171588]):
                        pass
                    elif faces.remove([171683,171684,171685]):
                        pass
                    elif faces.remove([171684,171685,171686]):
                        pass
                    elif faces.remove([172523,172524,172525]):
                        pass
                    elif faces.remove([172522,172523,172524]):
                        pass
                    elif faces.remove([172516,172517,172518]):
                        pass
                    elif faces.remove([172478,172479,172480]):
                        pass
                    elif faces.remove([172479,172480,172481]):
                        pass
                    elif faces.remove([172766,172767,172768]):
                        pass
                    elif faces.remove([172491,172492,172493]):
                        pass
                    elif faces.remove([171553,171554,171555]):
                        pass
                    elif faces.remove([171575,171576,171577]):
                        pass
                    elif faces.remove([171576,171577,171578]):
                        pass
                    elif faces.remove([171515,171516,171517]):
                        pass
                    elif faces.remove([173014,173015,173016]):
                        pass
                    elif faces.remove([173047,173048,173049]):
                        pass
                    elif faces.remove([171482,171483,171484]):
                        pass
                    elif faces.remove([171542,171543,171544]):
                        pass
                    elif faces.remove([172957,172958,172959]):
                        pass
                    elif faces.remove([172964,172965,172966]):
                        pass
                    elif faces.remove([173058,173059,173060]):
                        pass
                    elif faces.remove([173004,173005,173006]):
                        pass
                    elif faces.remove([173005,173006,173007]):
                        pass
                    elif faces.remove([171582,171583,171584]):
                        pass
                    elif faces.remove([172974,172975,172976]):
                        pass
                    elif faces.remove([171530,171531,171532]):
                        pass
                    elif faces.remove([171529,171530,171531]):
                        pass
                    elif faces.remove([171598,171599,171600]):
                        pass
                    elif faces.remove([171597,171598,171599]):
                        pass
                    elif faces.remove([171483,171484,171485]):
                        pass
                    elif faces.remove([171583,171584,171585]):
                        pass
                    elif faces.remove([172958,172959,172960]):
                        pass
                    elif faces.remove([173046,173047,173048]):
                        pass
                    elif faces.remove([172963,172964,172965]):
                        pass
                    elif faces.remove([172969,172970,172971]):
                        pass
                    elif faces.remove([172970,172971,172972]):
                        pass
                    elif faces.remove([171543,171544,171545]):
                        pass
                    elif faces.remove([173054,173055,173056]):
                        pass
                    elif faces.remove([173053,173054,173055]):
                        pass
                    elif faces.remove([171571,171572,171573]):
                        pass
                    elif faces.remove([173015,173016,173017]):
                        pass
                    elif faces.remove([172973,172974,172975]):
                        pass
                    elif faces.remove([171389,171390,171391]):
                        pass
                    elif faces.remove([171556,171557,171558]):
                        pass
                    elif faces.remove([171555,171556,171557]):
                        pass
                    elif faces.remove([171384,171385,171386]):
                        pass
                    elif faces.remove([171390,171391,171392]):
                        pass
                    elif faces.remove([171402,171403,171404]):
                        pass
                    elif faces.remove([171401,171402,171403]):
                        pass
                    elif faces.remove([171383,171384,171385]):
                        pass
                    elif faces.remove([172986,172987,172988]):
                        pass
                    elif faces.remove([171378,171379,171380]):
                        pass
                    elif faces.remove([171455,171456,171457]):
                        pass
                    elif faces.remove([171404,171405,171406]):
                        pass
                    elif faces.remove([171405,171406,171407]):
                        pass
                    elif faces.remove([171457,171458,171459]):
                        pass
                    elif faces.remove([171350,171351,171352]):
                        pass
                    elif faces.remove([118032,118033,118034]):
                        pass
                    elif faces.remove([178713,178714,178715]):
                        pass
                    elif faces.remove([170772,170773,170774]):
                        pass
                    elif faces.remove([172830,172831,172832]):
                        pass
                    elif faces.remove([130793,130794,130795]):
                        pass
                    elif faces.remove([86747,86748,86749]):
                        pass
                    elif faces.remove([60268,60269,60270]):
                        pass
                    elif faces.remove([201397,201398,201399]):
                        pass
                    elif faces.remove([196309,196310,196311]):
                        pass
                    elif faces.remove([185822,185823,185824]):
                        pass
                    elif faces.remove([194076,194077,194078]):
                        pass
                    elif faces.remove([189669,189670,189671]):
                        pass
                    elif faces.remove([194077,194078,194079]):
                        pass
                    elif faces.remove([189670,189671,189672]):
                        pass
                    elif faces.remove([188597,188598,188599]):
                        pass
                    elif faces.remove([198945,198946,198947]):
                        pass
                    elif faces.remove([183693,183694,183695]):
                        pass
                    elif faces.remove([12,13,14]):
                        pass
                    elif faces.remove([13,14,15]):
                        pass
                    elif faces.remove([32162,32163,32164]):
                        pass
                    elif faces.remove([112116,112117,112118]):
                        pass
                    elif faces.remove([145510,145511,145512]):
                        pass
                    elif faces.remove([34671,34672,34673]):
                        pass
                    elif faces.remove([178672,178673,178674]):
                        pass
                    elif faces.remove([178304,178305,178306]):
                        pass
                    elif faces.remove([164786,164787,164788]):
                        pass
                    elif faces.remove([79976,79977,79978]):
                        pass
                    elif faces.remove([42965,42966,42967]):
                        pass
                    elif faces.remove([164418,164419,164420]):
                        pass
                    elif faces.remove([164050,164051,164052]):
                        pass
                    elif faces.remove([163682,163683,163684]):
                        pass
                    elif faces.remove([163314,163315,163316]):
                        pass
                    elif faces.remove([162946,162947,162948]):
                        pass
                    elif faces.remove([162578,162579,162580]):
                        pass
                    elif faces.remove([162210,162211,162212]):
                        pass
                    elif faces.remove([161842,161843,161844]):
                        pass
                    elif faces.remove([112911,112912,112913]):
                        pass
                    elif faces.remove([112113,112114,112115]):
                        pass
                    elif faces.remove([49661,49662,49663]):
                        pass
                    elif faces.remove([42962,42963,42964]):
                        pass
                    elif faces.remove([34656,34657,34658]):
                        pass
                    elif faces.remove([34565,34566,34567]):
                        pass
                    elif faces.remove([85265,85266,85267]):
                        pass
                    elif faces.remove([112788,112789,112790]):
                        pass
                    elif faces.remove([34568,34569,34570]):
                        pass
                    elif faces.remove([125481,125482,125483]):
                        pass
                    elif faces.remove([87816,87817,87818]):
                        pass
                    elif faces.remove([201378,201379,201380]):
                        pass
                    elif faces.remove([179637,179638,179639]):
                        pass
                    elif faces.remove([145117,145118,145119]):
                        pass
                    elif faces.remove([14625,14626,14627]):
                        pass
                    elif faces.remove([48695,48696,48697]):
                        pass
                    elif faces.remove([85269,85270,85271]):
                        pass
                    elif faces.remove([173987,173988,173989]):
                        pass
                    elif faces.remove([173804,173805,173806]):
                        pass
                    elif faces.remove([173802,173803,173804]):
                        pass
                    elif faces.remove([14632,14633,14634]):
                        pass
                    elif faces.remove([14417,14418,14419]):
                        pass
                    elif faces.remove([14416,14417,14418]):
                        pass
                    elif faces.remove([14633,14634,14635]):
                        pass
                    elif faces.remove([18484,18485,18486]):
                        pass
                    elif faces.remove([18485,18486,18487]):
                        pass
                    elif faces.remove([18477,18478,18479]):
                        pass
                    elif faces.remove([18476,18477,18478]):
                        pass
                    elif faces.remove([18456,18457,18458]):
                        pass
                    elif faces.remove([18457,18458,18459]):
                        pass
                    elif faces.remove([18449,18450,18451]):
                        pass
                    elif faces.remove([18448,18449,18450]):
                        pass
                    elif faces.remove([18428,18429,18430]):
                        pass
                    elif faces.remove([18429,18430,18431]):
                        pass
                    elif faces.remove([18420,18421,18422]):
                        pass
                    elif faces.remove([18421,18422,18423]):
                        pass
                    elif faces.remove([48693,48694,48695]):
                        pass
                    elif faces.remove([34655,34656,34657]):
                        pass
                    elif faces.remove([14624,14625,14626]):
                        pass
                    elif faces.remove([112708,112709,112710]):
                        pass
                    elif faces.remove([86864,86865,86866]):
                        pass
                    elif faces.remove([86863,86864,86865]):
                        pass
                    elif faces.remove([108950,108951,108952]):
                        pass
                    elif faces.remove([99960,99961,99962]):
                        pass
                    elif faces.remove([99798,99799,99800]):
                        pass
                    elif faces.remove([86851,86852,86853]):
                        pass
                    elif faces.remove([86852,86853,86854]):
                        pass
                    elif faces.remove([86872,86873,86874]):
                        pass
                    elif faces.remove([86871,86872,86873]):
                        pass
                    elif faces.remove([86883,86884,86885]):
                        pass
                    elif faces.remove([173805,173806,173807]):
                        pass
                    elif faces.remove([99480,99481,99482]):
                        pass
                    elif faces.remove([85263,85264,85265]):
                        pass
                    elif faces.remove([174002,174003,174004]):
                        pass
                    elif faces.remove([173819,173820,173821]):
                        pass
                    elif faces.remove([99318,99319,99320]):
                        pass
                    elif faces.remove([117920,117921,117922]):
                        pass
                    elif faces.remove([117803,117804,117805]):
                        pass
                    elif faces.remove([117802,117803,117804]):
                        pass
                    elif faces.remove([117824,117825,117826]):
                        pass
                    elif faces.remove([117825,117826,117827]):
                        pass
                    elif faces.remove([117821,117822,117823]):
                        pass
                    elif faces.remove([117820,117821,117822]):
                        pass
                    elif faces.remove([117857,117858,117859]):
                        pass
                    elif faces.remove([117856,117857,117858]):
                        pass
                    elif faces.remove([117921,117922,117923]):
                        pass
                    elif faces.remove([123142,123143,123144]):
                        pass
                    elif faces.remove([193980,193981,193982]):
                        pass
                    elif faces.remove([87788,87789,87790]):
                        pass
                    elif faces.remove([99000,99001,99002]):
                        pass
                    elif faces.remove([172529,172530,172531]):
                        pass
                    elif faces.remove([98838,98839,98840]):
                        pass
                    elif faces.remove([61236,61237,61238]):
                        pass
                    elif faces.remove([172370,172371,172372]):
                        pass
                    elif faces.remove([172379,172380,172381]):
                        pass
                    elif faces.remove([172380,172381,172382]):
                        pass
                    elif faces.remove([171942,171943,171944]):
                        pass
                    elif faces.remove([172162,172163,172164]):
                        pass
                    elif faces.remove([212087,212088,212089]):
                        pass
                    elif faces.remove([8871,8872,8873]):
                        pass
                    elif faces.remove([5030,5031,5032]):
                        pass
                    elif faces.remove([5031,5032,5033]):
                        pass
                    elif faces.remove([14741,14742,14743]):
                        pass
                    elif faces.remove([9880,9881,9882]):
                        pass
                    elif faces.remove([15480,15481,15482]):
                        pass
                    elif faces.remove([98517,98518,98519]):
                        pass
                    elif faces.remove([171349,171350,171351]):
                        pass
                    elif faces.remove([171251,171252,171253]):
                        pass
                    elif faces.remove([171252,171253,171254]):
                        pass
                    elif faces.remove([171283,171284,171285]):
                        pass
                    elif faces.remove([171445,171446,171447]):
                        pass
                    elif faces.remove([171341,171342,171343]):
                        pass
                    elif faces.remove([171463,171464,171465]):
                        pass
                    elif faces.remove([171462,171463,171464]):
                        pass
                    elif faces.remove([172912,172913,172914]):
                        pass
                    elif faces.remove([171263,171264,171265]):
                        pass
                    elif faces.remove([171262,171263,171264]):
                        pass
                    elif faces.remove([171249,171250,171251]):
                        pass
                    elif faces.remove([171248,171249,171250]):
                        pass
                    elif faces.remove([171266,171267,171268]):
                        pass
                    elif faces.remove([171334,171335,171336]):
                        pass
                    elif faces.remove([171139,171140,171141]):
                        pass
                    elif faces.remove([171089,171090,171091]):
                        pass
                    elif faces.remove([171129,171130,171131]):
                        pass
                    elif faces.remove([98467,98468,98469]):
                        pass
                    elif faces.remove([85249,85250,85251]):
                        pass
                    elif faces.remove([85199,85200,85201]):
                        pass
                    elif faces.remove([84286,84287,84288]):
                        pass
                    elif faces.remove([84124,84125,84126]):
                        pass
                    elif faces.remove([72025,72026,72027]):
                        pass
                    elif faces.remove([71975,71976,71977]):
                        pass
                    elif faces.remove([69107,69108,69109]):
                        pass
                    elif faces.remove([69057,69058,69059]):
                        pass
                    elif faces.remove([64242,64243,64244]):
                        pass
                    elif faces.remove([64138,64139,64140]):
                        pass
                    elif faces.remove([60265,60266,60267]):
                        pass
                    elif faces.remove([49006,49007,49008]):
                        pass
                    elif faces.remove([42654,42655,42656]):
                        pass
                    elif faces.remove([33472,33473,33474]):
                        pass
                    elif faces.remove([144723,144724,144725]):
                        pass
                    elif faces.remove([49664,49665,49666]):
                        pass
                    elif faces.remove([84299,842300,842301]):
                        pass
                    elif faces.remove([72038,72039,72040]):
                        pass
                    elif faces.remove([69120,69121,69122]):
                        pass
                    elif faces.remove([174004,174005,174006]):
                        pass
                    elif faces.remove([64255,64256,64257]):
                        pass
                    elif faces.remove([61211,61212,61213]):
                        pass
                    elif faces.remove([85259,85260,85261]):
                        pass
                    elif faces.remove([154536,154537,154538]):
                        pass
                    elif faces.remove([48696,48697,48698]):
                        pass
                    elif faces.remove([80684,80685,80686]):
                        pass
                    elif faces.remove([86843,86844,86845]):
                        pass
                    elif faces.remove([86844,86845,86846]):
                        pass
                    elif faces.remove([86835,86836,86837]):
                        pass
                    elif faces.remove([86836,86837,86838]):
                        pass
                    elif faces.remove([86827,86828,86829]):
                        pass
                    elif faces.remove([86828,86829,86830]):
                        pass
                    elif faces.remove([86819,86820,86821]):
                        pass
                    elif faces.remove([86820,86821,86822]):
                        pass
                    elif faces.remove([86811,86812,86813]):
                        pass
                    elif faces.remove([86812,86813,86814]):
                        pass
                    elif faces.remove([86803,86804,86805]):
                        pass
                    elif faces.remove([86804,86805,86806]):
                        pass
                    elif faces.remove([86795,86796,86797]):
                        pass
                    elif faces.remove([86796,86797,86798]):
                        pass
                    elif faces.remove([86787,86788,86789]):
                        pass
                    elif faces.remove([86788,86789,86790]):
                        pass
                    elif faces.remove([86764,86765,86766]):
                        pass
                    elif faces.remove([86763,86764,86765]):
                        pass
                    elif faces.remove([86771,86772,86773]):
                        pass
                    elif faces.remove([86772,86773,86774]):
                        pass
                    elif faces.remove([86780,86781,86782]):
                        pass
                    elif faces.remove([86779,86780,86781]):
                        pass
                    elif faces.remove([86859,86860,86861]):
                        pass
                    elif faces.remove([86860,86861,86862]):
                        pass
                    elif faces.remove([86855,86856,86857]):
                        pass
                    elif faces.remove([86856,86857,86858]):
                        pass
                    elif faces.remove([86876,86877,86878]):
                        pass
                    elif faces.remove([86875,86876,86877]):
                        pass
                    elif faces.remove([86880,86881,86882]):
                        pass
                    elif faces.remove([86879,86880,86881]):
                        pass
                    elif faces.remove([125314,125315,125316]):
                        pass
                    elif faces.remove([32938,32939,32940]):
                        pass
                    elif faces.remove([141623,141624,141625]):
                        pass
                    elif faces.remove([141636,141637,141638]):
                        pass
                    elif faces.remove([141635,141636,141637]):
                        pass
                    elif faces.remove([141624,141625,141626]):
                        pass
                    elif faces.remove([51234,51235,51236]):
                        pass
                    elif faces.remove([51235,51236,51237]):
                        pass
                    elif faces.remove([51330,51331,51332]):
                        pass
                    elif faces.remove([51331,51332,51333]):
                        pass
                    elif faces.remove([51316,51317,51318]):
                        pass
                    elif faces.remove([51317,51318,51319]):
                        pass
                    elif faces.remove([51326,51327,51328]):
                        pass
                    elif faces.remove([51327,51328,51329]):
                        pass
                    elif faces.remove([52635,52636,52637]):
                        pass
                    elif faces.remove([155245,155246,155247]):
                        pass
                    elif faces.remove([136762,136763,136764]):
                        pass
                    elif faces.remove([155246,155247,155248]):
                        pass
                    elif faces.remove([136763,136764,136765]):
                        pass
                    elif faces.remove([34654,34655,34656]):
                        pass
                    elif faces.remove([34653,34654,34655]):
                        pass
                    elif faces.remove([34652,34653,34654]):
                        pass
                    elif faces.remove([178676,178677,178678]):
                        pass
                    elif faces.remove([115582,115583,115584]):
                        pass
                    elif faces.remove([28407,28408,28409]):
                        pass
                    elif faces.remove([28406,28407,28408]):
                        pass
                    elif faces.remove([52113,52114,52115]):
                        pass
                    elif faces.remove([86613,86614,86615]):
                        pass
                    elif faces.remove([86612,86613,86614]):
                        pass
                    elif faces.remove([130792,130793,130794]):
                        pass
                    elif faces.remove([61298,61299,61300]):
                        pass
                    elif faces.remove([193926,193927,193928]):
                        pass
                    elif faces.remove([193925,193926,193927]):
                        pass
                    elif faces.remove([172528,172529,172530]):
                        pass
                    elif faces.remove([172517,172518,172519]):
                        pass
                    elif faces.remove([172562,172563,172564]):
                        pass
                    elif faces.remove([172563,172564,172565]):
                        pass
                    elif faces.remove([172541,172542,172543]):
                        pass
                    elif faces.remove([172540,172541,172542]):
                        pass
                    elif faces.remove([172618,172619,172620]):
                        pass
                    elif faces.remove([172617,172618,172619]):
                        pass
                    elif faces.remove([172612,172613,172614]):
                        pass
                    elif faces.remove([172611,172612,172613]):
                        pass
                    elif faces.remove([172765,172766,172767]):
                        pass
                    elif faces.remove([172602,172603,172604]):
                        pass
                    elif faces.remove([172601,172602,172603]):
                        pass
                    elif faces.remove([173996,173997,173998]):
                        pass
                    elif faces.remove([173813,173814,173815]):
                        pass
                    elif faces.remove([173997,173998,173999]):
                        pass
                    elif faces.remove([84311,84312,84313]):
                        pass
                    elif faces.remove([112914,112915,112916]):
                        pass
                    elif faces.remove([112551,112552,112553]):
                        pass
                    elif faces.remove([112550,112551,112552]):
                        pass
                    elif faces.remove([112607,112608,112609]):
                        pass
                    elif faces.remove([123119,123120,123121]):
                        pass
                    elif faces.remove([123104,123105,123106]):
                        pass
                    elif faces.remove([123120,123121,123122]):
                        pass
                    elif faces.remove([123105,123106,123107]):
                        pass
                    elif faces.remove([125332,125333,125334]):
                        pass
                    elif faces.remove([123182,123183,123184]):
                        pass
                    elif faces.remove([172504,172505,172506]):
                        pass
                    elif faces.remove([172503,172504,172505]):
                        pass
                    elif faces.remove([172497,172498,172499]):
                        pass
                    elif faces.remove([172507,172508,172509]):
                        pass
                    elif faces.remove([172490,172491,172492]):
                        pass
                    elif faces.remove([172475,172476,172477]):
                        pass
                    elif faces.remove([172476,172477,172478]):
                        pass
                    elif faces.remove([172514,172515,172516]):
                        pass
                    elif faces.remove([172513,172514,172515]):
                        pass
                    elif faces.remove([172506,172507,172508]):
                        pass
                    elif faces.remove([172546,172547,172548]):
                        pass
                    
            elif Chunk == b"SST0":
                break
            
        mesh = bpy.data.meshes.new("alspier")
        mesh.from_pydata(vertices, [], faces)
        object = bpy.data.objects.new("alspier", mesh)
        bpy.context.collection.objects.link(object)
        
