import math

def casegenerator (red, green, blue, trans):
    
    #wools
    case1 = math.sqrt((20-red)**2 + (21-green)**2 + (25-blue)**2)
    case2 = math.sqrt((53-red)**2 + (57-green)**2 + (157-blue)**2)
    case3 = math.sqrt((114-red)**2 + (71-green)**2 + (40-blue)**2)
    case4 = math.sqrt((21-red)**2 + (137-green)**2 + (145-blue)**2)
    case5 = math.sqrt((62-red)**2 + (68-green)**2 + (71-blue)**2)
    case6 = math.sqrt((84-red)**2 + (109-green)**2 + (27-blue)**2)
    case7 = math.sqrt((58-red)**2 + (175-green)**2 + (217-blue)**2)
    case8 = math.sqrt((112-red)**2 + (185-green)**2 + (25-blue)**2)
    case9 = math.sqrt((189-red)**2 + (68-green)**2 + (179-blue)**2)
    case10 = math.sqrt((240-red)**2 + (118-green)**2 + (19-blue)**2)
    case11 = math.sqrt((237-red)**2 + (141-green)**2 + (172-blue)**2)
    case12 = math.sqrt((121-red)**2 + (42-green)**2 + (172-blue)**2)
    case13 = math.sqrt((160-red)**2 + (39-green)**2 + (34-blue)**2)
    case14 = math.sqrt((233-red)**2 + (236-green)**2 + (236-blue)**2)
    case15 = math.sqrt((248-red)**2 + (197-green)**2 + (39-blue)**2)

    #terracottas
    case16 = math.sqrt((152-red)**2 + (94-green)**2 + (67-blue)**2)
    case17 = math.sqrt((37-red)**2 + (22-green)**2 + (16-blue)**2)
    case18 = math.sqrt((74-red)**2 + (59-green)**2 + (91-blue)**2)
    case19 = math.sqrt((77-red)**2 + (51-green)**2 + (35-blue)**2)
    case20 = math.sqrt((86-red)**2 + (91-green)**2 + (91-blue)**2)
    case21 = math.sqrt((57-red)**2 + (42-green)**2 + (35-blue)**2)
    case22 = math.sqrt((76-red)**2 + (83-green)**2 + (42-blue)**2)
    case23 = math.sqrt((113-red)**2 + (108-green)**2 + (137-blue)**2)
    case24 = math.sqrt((103-red)**2 + (117-green)**2 + (52-blue)**2)
    case25 = math.sqrt((149-red)**2 + (88-green)**2 + (108-blue)**2)
    case26 = math.sqrt((161-red)**2 + (83-green)**2 + (37-blue)**2)
    case27 = math.sqrt((161-red)**2 + (78-green)**2 + (78-blue)**2)
    case28 = math.sqrt((118-red)**2 + (70-green)**2 + (86-blue)**2)
    case29 = math.sqrt((143-red)**2 + (61-green)**2 + (46-blue)**2)
    case30 = math.sqrt((209-red)**2 + (178-green)**2 + (161-blue)**2)
    case31 = math.sqrt((186-red)**2 + (133-green)**2 + (35-blue)**2)
    

    caselist = [case1, case2, case3, case4, case5, case6, case7, case8, case9, case10, case11, case12, case13, case14, case15, case16, case17, case18, case19, case20, case21, case22, case23, case24, case25, case26, case27, case28, case29, case30, case31]

    caselist.sort()

    finalnum = caselist[:1]
    finalnum = str(finalnum)
    
    finalnum = finalnum.replace("[", "")
    finalnum = finalnum.replace("]", "")

    finalnum = float(finalnum)
    
    if trans == 0:
        return "air"
    elif finalnum == case1:
        return "wool 15"
    elif finalnum == case2:
        return "wool 11"
    elif finalnum == case3:
        return "wool 12"
    elif finalnum == case4:
        return "wool 9"
    elif finalnum == case5:
        return "wool 7"
    elif finalnum == case6:
        return "wool 13"
    elif finalnum == case7:
        return "wool 3"
    elif finalnum == case8:
        return "wool 5"
    elif finalnum == case9:
        return "wool 2"
    elif finalnum == case10:
        return "wool 1"
    elif finalnum == case11:
        return "wool 6"
    elif finalnum == case12:
        return "wool 10"
    elif finalnum == case13:
        return "wool 14"
    elif finalnum == case14:
        return "wool"
    elif finalnum == case15:
        return "wool 4"
    elif finalnum == case16:
        return "hardened_clay"
    elif finalnum == case17:
        return "stained_hardened_clay 15"
    elif finalnum == case18:
        return "stained_hardened_clay 9"
    elif finalnum == case19:
        return "stained_hardened_clay 11"
    elif finalnum == case20:
        return "stained_hardened_clay 12"
    elif finalnum == case21:
        return "stained_hardened_clay 7"
    elif finalnum == case22:
        return "stained_hardened_clay 3"
    elif finalnum == case23:
        return "stained_hardened_clay 13"
    elif finalnum == case24:
        return "stained_hardened_clay 5"
    elif finalnum == case25:
        return "stained_hardened_clay 2"
    elif finalnum == case26:
        return "stained_hardened_clay 1"
    elif finalnum == case27:
        return "stained_hardened_clay 6"
    elif finalnum == case28:
        return "stained_hardened_clay 10"
    elif finalnum == case29:
        return "stained_hardened_clay 14"
    elif finalnum == case30:
        return "stained_hardened_clay"
    elif finalnum == case31:
        return "stained_hardened_clay 4"
   
    else:
        return "air"

    
    
