import math
from tkinter import messagebox

def casegenerator (red, green, blue, trans, includedblocks):
    if includedblocks == 'ALLBLOCKS':
        includedblocks = ['case1', 'case2', 'case3', 'case4', 'case5', 'case6', 'case7', 'case8', 'case9', 'case10', 'case11', 'case12', 'case13', 'case14', 'case15', 'case16', 'case17', 'case18'
                          , 'case19', 'case20', 'case21', 'case22', 'case23', 'case24', 'case25', 'case26', 'case27', 'case28', 'case29', 'case30', 'case31', 'case32', 'case33', 'case34', 'case35', 'case36'
                          , 'case37', 'case38', 'case39', 'case40', 'case41', 'case42', 'case43', 'case44', 'case45', 'case46', 'case47', 'case48', 'case49', 'case50', 'case51']
    
    caselist = []
    #wools
    if 'case1' in includedblocks or includedblocks == "ALLBLOCKS":
        
        case1 = math.sqrt((20-red)**2 + (21-green)**2 + (25-blue)**2)
        caselist = caselist + [case1]
        
    if 'case2' in includedblocks or includedblocks == "ALLBLOCKS":    
        case2 = math.sqrt((53-red)**2 + (57-green)**2 + (157-blue)**2)
        caselist = caselist + [case2]
    if 'case3' in includedblocks or includedblocks == "ALLBLOCKS":
        case3 = math.sqrt((114-red)**2 + (71-green)**2 + (40-blue)**2)
        caselist = caselist + [case3]
    if 'case4' in includedblocks or includedblocks == "ALLBLOCKS":
        case4 = math.sqrt((21-red)**2 + (137-green)**2 + (145-blue)**2)
        caselist = caselist + [case4]
    if 'case5' in includedblocks or includedblocks == "ALLBLOCKS":
        case5 = math.sqrt((62-red)**2 + (68-green)**2 + (71-blue)**2)
        caselist = caselist + [case5]
    if 'case6' in includedblocks or includedblocks == "ALLBLOCKS":
        case6 = math.sqrt((84-red)**2 + (109-green)**2 + (27-blue)**2)
        caselist = caselist + [case6]
    if 'case7' in includedblocks or includedblocks == "ALLBLOCKS":
        case7 = math.sqrt((58-red)**2 + (175-green)**2 + (217-blue)**2)
        caselist = caselist + [case7]
    if 'case8' in includedblocks or includedblocks == "ALLBLOCKS":
        case8 = math.sqrt((112-red)**2 + (185-green)**2 + (25-blue)**2)
        caselist = caselist + [case8]
    if 'case9' in includedblocks or includedblocks == "ALLBLOCKS":
        case9 = math.sqrt((189-red)**2 + (68-green)**2 + (179-blue)**2)
        caselist = caselist + [case9]
    if 'case10' in includedblocks or includedblocks == "ALLBLOCKS":
        case10 = math.sqrt((240-red)**2 + (118-green)**2 + (19-blue)**2)
        caselist = caselist + [case10]
    if 'case11' in includedblocks or includedblocks == "ALLBLOCKS":
        case11 = math.sqrt((237-red)**2 + (141-green)**2 + (172-blue)**2)
        caselist = caselist + [case11]
    if 'case12' in includedblocks or includedblocks == "ALLBLOCKS":
        case12 = math.sqrt((121-red)**2 + (42-green)**2 + (172-blue)**2)
        caselist = caselist + [case12]
    if 'case13' in includedblocks or includedblocks == "ALLBLOCKS":
        case13 = math.sqrt((160-red)**2 + (39-green)**2 + (34-blue)**2)
        caselist = caselist + [case13]
    if 'case14' in includedblocks or includedblocks == "ALLBLOCKS":
        case14 = math.sqrt((233-red)**2 + (236-green)**2 + (236-blue)**2)
        caselist = caselist + [case14]
    if 'case15' in includedblocks or includedblocks == "ALLBLOCKS":
        case15 = math.sqrt((248-red)**2 + (197-green)**2 + (39-blue)**2)
        caselist = caselist + [case15]
    #gray
    if 'case32' in includedblocks or includedblocks == "ALLBLOCKS":
        case32 = math.sqrt((142-red)**2 + (142-green)**2 + (134-blue)**2)
        caselist = caselist + [case32]

    #terracottas
    if 'case16' in includedblocks or includedblocks == "ALLBLOCKS":
        case16 = math.sqrt((152-red)**2 + (94-green)**2 + (67-blue)**2)
        caselist = caselist + [case16]
    if 'case17' in includedblocks or includedblocks == "ALLBLOCKS":
        case17 = math.sqrt((37-red)**2 + (22-green)**2 + (16-blue)**2)
        caselist = caselist + [case17]
    if 'case18' in includedblocks or includedblocks == "ALLBLOCKS":
        case18 = math.sqrt((74-red)**2 + (59-green)**2 + (91-blue)**2)
        caselist = caselist + [case18]
    if 'case19' in includedblocks or includedblocks == "ALLBLOCKS":
        case19 = math.sqrt((77-red)**2 + (51-green)**2 + (35-blue)**2)
        caselist = caselist + [case19]
    if 'case20' in includedblocks or includedblocks == "ALLBLOCKS":
        case20 = math.sqrt((86-red)**2 + (91-green)**2 + (91-blue)**2)
        caselist = caselist + [case20]
    if 'case21' in includedblocks or includedblocks == "ALLBLOCKS":
        case21 = math.sqrt((57-red)**2 + (42-green)**2 + (35-blue)**2)
        caselist = caselist + [case21]
    if 'case22' in includedblocks or includedblocks == "ALLBLOCKS":
        case22 = math.sqrt((76-red)**2 + (83-green)**2 + (42-blue)**2)
        caselist = caselist + [case22]
    if 'case23' in includedblocks or includedblocks == "ALLBLOCKS":
        case23 = math.sqrt((113-red)**2 + (108-green)**2 + (137-blue)**2)
        caselist = caselist + [case23]
    if 'case24' in includedblocks or includedblocks == "ALLBLOCKS":
        case24 = math.sqrt((103-red)**2 + (117-green)**2 + (52-blue)**2)
        caselist = caselist + [case24]
    if 'case25' in includedblocks or includedblocks == "ALLBLOCKS":
        case25 = math.sqrt((149-red)**2 + (88-green)**2 + (108-blue)**2)
        caselist = caselist + [case25]
    if 'case26' in includedblocks or includedblocks == "ALLBLOCKS":
        case26 = math.sqrt((161-red)**2 + (83-green)**2 + (37-blue)**2)
        caselist = caselist + [case26]
    if 'case27' in includedblocks or includedblocks == "ALLBLOCKS":
        case27 = math.sqrt((161-red)**2 + (78-green)**2 + (78-blue)**2)
        caselist = caselist + [case27]
    if 'case28' in includedblocks or includedblocks == "ALLBLOCKS":
        case28 = math.sqrt((118-red)**2 + (70-green)**2 + (86-blue)**2)
        caselist = caselist + [case28]
    if 'case29' in includedblocks or includedblocks == "ALLBLOCKS":
        case29 = math.sqrt((143-red)**2 + (61-green)**2 + (46-blue)**2)
        caselist = caselist + [case29]
    if 'case30' in includedblocks or includedblocks == "ALLBLOCKS":
        case30 = math.sqrt((209-red)**2 + (178-green)**2 + (161-blue)**2)
        caselist = caselist + [case30]
    if 'case31' in includedblocks or includedblocks == "ALLBLOCKS":
        case31 = math.sqrt((186-red)**2 + (133-green)**2 + (35-blue)**2)
        caselist = caselist + [case31]
    #gray
    if 'case33' in includedblocks or includedblocks == "ALLBLOCKS":
        case33 = math.sqrt((135-red)**2 + (106-green)**2 + (97-blue)**2)
        caselist = caselist + [case33]
    
    #wood logs planks and stripped
    if 'case34' in includedblocks or includedblocks == "ALLBLOCKS":
        case34 = math.sqrt((103-red)**2 + (96-green)**2 + (86-blue)**2)
        caselist = caselist + [case34]
    if 'case35' in includedblocks or includedblocks == "ALLBLOCKS":
        case35 = math.sqrt((60-red)**2 + (46-green)**2 + (26-blue)**2)
        caselist = caselist + [case35]
    if 'case36' in includedblocks or includedblocks == "ALLBLOCKS":
        case36 = math.sqrt((216-red)**2 + (215-green)**2 + (210-blue)**2)
        caselist = caselist + [case36]
    if 'case37' in includedblocks or includedblocks == "ALLBLOCKS":
        case37 = math.sqrt((85-red)**2 + (67-green)**2 + (25-blue)**2)
        caselist = caselist + [case37]
    if 'case38' in includedblocks or includedblocks == "ALLBLOCKS":
        case38 = math.sqrt((109-red)**2 + (85-green)**2 + (50-blue)**2)
        caselist = caselist + [case38]
    if 'case39' in includedblocks or includedblocks == "ALLBLOCKS":
        case39 = math.sqrt((58-red)**2 + (37-green)**2 + (16-blue)**2)
        caselist = caselist + [case39]
    if 'case40' in includedblocks or includedblocks == "ALLBLOCKS":
        case40 = math.sqrt((168-red)**2 + (90-green)**2 + (50-blue)**2)
        caselist = caselist + [case40]
    if 'case41' in includedblocks or includedblocks == "ALLBLOCKS":
        case41 = math.sqrt((66-red)**2 + (43-green)**2 + (20-blue)**2)
        caselist = caselist + [case41]
    if 'case42' in includedblocks or includedblocks == "ALLBLOCKS":
        case42 = math.sqrt((192-red)**2 + (175-green)**2 + (121-blue)**2)
        caselist = caselist + [case42]
    if 'case43' in includedblocks or includedblocks == "ALLBLOCKS":
        case43 = math.sqrt((160-red)**2 + (115-green)**2 + (80-blue)**2)
        caselist = caselist + [case43]
    if 'case44' in includedblocks or includedblocks == "ALLBLOCKS":
        case44 = math.sqrt((162-red)**2 + (130-green)**2 + (78-blue)**2)
        caselist = caselist + [case44]
    if 'case45' in includedblocks or includedblocks == "ALLBLOCKS":
        case45 = math.sqrt((114-red)**2 + (84-green)**2 + (48-blue)**2)
        caselist = caselist + [case45]
    if 'case46' in includedblocks or includedblocks == "ALLBLOCKS":
        case46 = math.sqrt((174-red)**2 + (92-green)**2 + (59-blue)**2)
        caselist = caselist + [case46]
    if 'case47' in includedblocks or includedblocks == "ALLBLOCKS":
        case47 = math.sqrt((196-red)**2 + (176-green)**2 + (118-blue)**2)
        caselist = caselist + [case47]
    if 'case48' in includedblocks or includedblocks == "ALLBLOCKS":
        case48 = math.sqrt((65-red)**2 + (51-green)**2 + (31-blue)**2)
        caselist = caselist + [case48]
    if 'case49' in includedblocks or includedblocks == "ALLBLOCKS":
        case49 = math.sqrt((171-red)**2 + (132-green)**2 + (84-blue)**2)
        caselist = caselist + [case49]
    if 'case50' in includedblocks or includedblocks == "ALLBLOCKS":
        case50 = math.sqrt((177-red)**2 + (144-green)**2 + (86-blue)**2)
        caselist = caselist + [case50]
    if 'case51' in includedblocks or includedblocks == "ALLBLOCKS":
        case51 = math.sqrt((79-red)**2 + (60-green)**2 + (34-blue)**2)
        caselist = caselist + [case51]

    caselist.sort()

    finalnum = caselist[:1]
    finalnum = str(finalnum)
    
    finalnum = finalnum.replace("[", "")
    finalnum = finalnum.replace("]", "")

    
    try:
        finalnum = float(finalnum)
    except:
            messagebox.showinfo("Error", "You must select at least one block.")
            quit()
    try:
        if trans == 0:
            return "air"
            print('returning air due to transparency')
        
        if 'case1' in includedblocks and finalnum == case1:
            return "wool 15"

        if 'case2' in includedblocks and finalnum == case2:    
            return "wool 11"
        if 'case3' in includedblocks and finalnum == case3:
            return "wool 12"
        if 'case4' in includedblocks and finalnum == case4:
            return "wool 9"
        if 'case5' in includedblocks and finalnum == case5:
            return "wool 7"
        if 'case6' in includedblocks and finalnum == case6:
            return "wool 13"
        if 'case7' in includedblocks and finalnum == case7:
            return "wool 3"
        if 'case8' in includedblocks and finalnum == case8:
            return "wool 5"
        if 'case9' in includedblocks and finalnum == case9:
            return "wool 2"
        if 'case10' in includedblocks and finalnum == case10:
            return "wool 1"
        if 'case11' in includedblocks and finalnum == case11:
            return "wool 6"
        if 'case12' in includedblocks and finalnum == case12:
            return "wool 10"
        if 'case13' in includedblocks and finalnum == case13:
            return "wool 14"
        if 'case14' in includedblocks and finalnum == case14:
            return "wool"
        if 'case15' in includedblocks and finalnum == case15:
            return "wool 4"
        if 'case16' in includedblocks and finalnum == case16:
            return "hardened_clay"

        if 'case17' in includedblocks and finalnum == case17:
            return "stained_hardened_clay 15"
        if 'case18' in includedblocks and finalnum == case18:
            return "stained_hardened_clay 9"
        if 'case19' in includedblocks and finalnum == case19:
            return "stained_hardened_clay 11"
        if 'case20' in includedblocks and finalnum == case20:
            return "stained_hardened_clay 12"
        if 'case21' in includedblocks and finalnum == case21:
            return "stained_hardened_clay 7"
        if 'case22' in includedblocks and finalnum == case22:
            return "stained_hardened_clay 3"
        if 'case23' in includedblocks and finalnum == case23:
            return "stained_hardened_clay 13"
        if 'case24' in includedblocks and finalnum == case24:
            return "stained_hardened_clay 5"
        if 'case25' in includedblocks and finalnum == case25:
            return "stained_hardened_clay 2"
        if 'case26' in includedblocks and finalnum == case26:
            return "stained_hardened_clay 1"
        if 'case27' in includedblocks and finalnum == case27:
            return "stained_hardened_clay 6"
        if 'case28' in includedblocks and finalnum == case28:
            return "stained_hardened_clay 10"
        if 'case29' in includedblocks and finalnum == case29:
            return "stained_hardened_clay 14"
        if 'case30' in includedblocks and finalnum == case30:
            return "stained_hardened_clay"
        if 'case31' in includedblocks and finalnum == case31:
            return "stained_hardened_clay 4"
        if 'case32' in includedblocks and finalnum == case32:
        #light gray wool
            return "wool 8"
        #light gray terracotta
        if 'case33' in includedblocks and finalnum == case33:
            return "stained_hardened_clay 8"

        #woods
        if 'case34' in includedblocks and finalnum == case34:
            return "wood 4"
        if 'case35' in includedblocks and finalnum == case35:
            return "wood 5"
        if 'case36' in includedblocks and finalnum == case36:
            return "wood 2"
        if 'case37' in includedblocks and finalnum == case37:
            return "wood 3"
        if 'case38' in includedblocks and finalnum == case38:
            return "wood"
        if 'case39' in includedblocks and finalnum == case39:
            return "wood 1"
        if 'case40' in includedblocks and finalnum == case40:
            return "planks 4"
        if 'case41' in includedblocks and finalnum == case41:
            return "planks 5"
        if 'case42' in includedblocks and finalnum == case42:
            return "planks 2"
        if 'case43' in includedblocks and finalnum == case43:
            return "planks 3"
        if 'case44' in includedblocks and finalnum == case44:
            return "planks"
        if 'case45' in includedblocks and finalnum == case45:
            return "planks 1"
        if 'case46' in includedblocks and finalnum == case46:
            return "stripped_acacia_log"
        if 'case47' in includedblocks and finalnum == case47:
            return "stripped_birch_log"
        if 'case48' in includedblocks and finalnum == case48:
            return "stripped_dark_oak_log"
        if 'case49' in includedblocks and finalnum == case49:
            return "stripped_jungle_log"
        if 'case50' in includedblocks and finalnum == case50:
            return "stripped_oak_log"
        if 'case51' in includedblocks and finalnum == case51:
            return "stripped_spruce_log"


    except:
        return "air"
        print('returning air')

    
    
