def addonfilemaker(entrename, userfuncfilename):
        
        import os
        import zipfile
        from PIL import Image
        import os.path
        from os import path
        from tkinter import messagebox
        import uuid

        savefilepath = os.getcwd()

        savefilepath = savefilepath.replace("\\", "/")


        for i in range(len(savefilepath)):
                if savefilepath[-i] == "/":
                        savefilepath = savefilepath[0:-i]
                        break

        os.chdir(savefilepath)


        os.chdir(savefilepath+"/Behavior Packs")




        #this is supposed to be the name of entree

        randuuid41 = '"' + str(uuid.uuid4()) + '"'
        randuuid42 = '"' + str(uuid.uuid4()) + '"'
        

        manifest = open("manifest.json", 'w')

        manifestjsonfile = ''' {\n    "format_version": 1,\n    "header": {\n        "description": "Create custom Images using function commands",\n        "name": "'''+ entrename +'''",\n        "uuid": ''' +randuuid41+ ''',\n        "version": [1, 11, 0],\n        "min_engine_version": [1, 11, 0]\n    },\n    "modules": [\n        {\n            "description": "PixelCraft",\n            "type": "data",\n            "uuid": '''+randuuid42+''',\n            "version": [1, 11, 0]\n        }\n    ]\n}'''


        manifest.write(manifestjsonfile)
        manifest.close()



        iconimgex = path.exists('pack_icon.png')

        if iconimgex == False:
                messagebox.showinfo("Error", "Missing required pack_icon.png in behavior packs folder!")
        






        
        #makes zip


        mcaddon = zipfile.ZipFile(entrename+'.mcaddon', 'w')#plug in ent.get

        mcaddon.write('manifest.json', 'pixelcraft/'+'manifest.json')
        mcaddon.write('pack_icon.png', 'pixelcraft/'+'pack_icon.png')
        mcaddon.write(entrename+'.mcfunction', 'pixelcraft/functions/'+entrename+'.mcfunction')

        if path.exists(savefilepath+'/Behavior Packs/'+entrename+'_part2'+'.mcfunction') == True:
                mcaddon.write(entrename+'_part2'+'.mcfunction', 'pixelcraft/functions/'+entrename+'_part2'+'.mcfunction')#plugin userentfilename
        if path.exists(savefilepath+'/Behavior Packs/'+entrename+'_part3'+'.mcfunction') == True:
                mcaddon.write(entrename+'_part3'+'.mcfunction', 'pixelcraft/functions/'+entrename+'_part3'+'.mcfunction')
        if path.exists(savefilepath+'/Behavior Packs/'+entrename+'_part4'+'.mcfunction') == True:        
                mcaddon.write(entrename+'_part4'+'.mcfunction', 'pixelcraft/functions/'+entrename+'_part4'+'.mcfunction')
        if path.exists(savefilepath+'/Behavior Packs/'+entrename+'_part5'+'.mcfunction') == True:
                mcaddon.write(entrename+'_part5'+'.mcfunction', 'pixelcraft/functions/'+entrename+'_part5'+'.mcfunction')
        if path.exists(savefilepath+'/Behavior Packs/'+entrename+'_part6'+'.mcfunction') == True:
                mcaddon.write(entrename+'_part6'+'.mcfunction', 'pixelcraft/functions/'+entrename+'_part6'+'.mcfunction')
        if path.exists(savefilepath+'/Behavior Packs/'+entrename+'_part7'+'.mcfunction') == True:
                mcaddon.write(entrename+'_part7'+'.mcfunction', 'pixelcraft/functions/'+entrename+'_part7'+'.mcfunction')
        if path.exists(savefilepath+'/Behavior Packs/'+entrename+'_part8'+'.mcfunction') == True:
                mcaddon.write(entrename+'_part8'+'.mcfunction', 'pixelcraft/functions/'+entrename+'_part8'+'.mcfunction')
        if path.exists(savefilepath+'/Behavior Packs/'+entrename+'_part9'+'.mcfunction') == True:
                mcaddon.write(entrename+'_part9'+'.mcfunction', 'pixelcraft/functions/'+entrename+'_part9'+'.mcfunction')
        if path.exists(savefilepath+'/Behavior Packs/'+entrename+'_part10'+'.mcfunction') == True:
                mcaddon.write(entrename+'_part10'+'.mcfunction', 'pixelcraft/functions/'+entrename+'_part10'+'.mcfunction')
        if path.exists(savefilepath+'/Behavior Packs/'+entrename+'_part11'+'.mcfunction') == True:
                mcaddon.write(entrename+'_part11'+'.mcfunction', 'pixelcraft/functions/'+entrename+'_part11'+'.mcfunction')
        if path.exists(savefilepath+'/Behavior Packs/'+entrename+'_part12'+'.mcfunction') == True:
                mcaddon.write(entrename+'_part12'+'.mcfunction', 'pixelcraft/functions/'+entrename+'_part12'+'.mcfunction')
        if path.exists(savefilepath+'/Behavior Packs/'+entrename+'_part13'+'.mcfunction') == True:
                mcaddon.write(entrename+'_part13'+'.mcfunction', 'pixelcraft/functions/'+entrename+'_part13'+'.mcfunction')
        if path.exists(savefilepath+'/Behavior Packs/'+entrename+'_part14'+'.mcfunction') == True:
                mcaddon.write(entrename+'_part14'+'.mcfunction', 'pixelcraft/functions/'+entrename+'_part14'+'.mcfunction')
        if path.exists(savefilepath+'/Behavior Packs/'+entrename+'_part15'+'.mcfunction') == True:
                mcaddon.write(entrename+'_part15'+'.mcfunction', 'pixelcraft/functions/'+entrename+'_part15'+'.mcfunction')
        if path.exists(savefilepath+'/Behavior Packs/'+entrename+'_part16'+'.mcfunction') == True:
                mcaddon.write(entrename+'_part16'+'.mcfunction', 'pixelcraft/functions/'+entrename+'_part16'+'.mcfunction')
        if path.exists(savefilepath+'/Behavior Packs/'+entrename+'_part17'+'.mcfunction') == True:
                mcaddon.write(entrename+'_part17'+'.mcfunction', 'pixelcraft/functions/'+entrename+'_part17'+'.mcfunction')
        if path.exists(savefilepath+'/Behavior Packs/'+entrename+'_part18'+'.mcfunction') == True:
                mcaddon.write(entrename+'_part18'+'.mcfunction', 'pixelcraft/functions/'+entrename+'_part18'+'.mcfunction')
        if path.exists(savefilepath+'/Behavior Packs/'+entrename+'_part19'+'.mcfunction') == True:
                mcaddon.write(entrename+'_part19'+'.mcfunction', 'pixelcraft/functions/'+entrename+'_part19'+'.mcfunction')
        if path.exists(savefilepath+'/Behavior Packs/'+entrename+'_part20'+'.mcfunction') == True:
                mcaddon.write(entrename+'_part20'+'.mcfunction', 'pixelcraft/functions/'+entrename+'_part20'+'.mcfunction')
        
        mcaddon.close
        try:
                os.remove(entrename+'.mcfunction')
        except:
                pass
        try:
                os.remove(entrename+'_part2'+'.mcfunction')
        except:
                pass
        try:
                os.remove(entrename+'_part3'+'.mcfunction')
        except:
                pass
        try:
                os.remove(entrename+'_part4'+'.mcfunction')
        except:
                pass
        try:
                os.remove(entrename+'_part5'+'.mcfunction')
        except:
                pass
        try:
                os.remove(entrename+'_part6'+'.mcfunction')
        except:
                pass
        try:
                os.remove(entrename+'_part7'+'.mcfunction')
        except:
                pass
        try:
                os.remove(entrename+'_part8'+'.mcfunction')
        except:
                pass
        try:
                os.remove(entrename+'_part9'+'.mcfunction')
        except:
                pass
        try:
                os.remove(entrename+'_part10'+'.mcfunction')
        except:
                pass
        try:
                os.remove(entrename+'_part11'+'.mcfunction')
        except:
                pass
        try:
                os.remove(entrename+'_part12'+'.mcfunction')
        except:
                pass
        try:
                os.remove(entrename+'_part13'+'.mcfunction')
        except:
                pass
        try:
                os.remove(entrename+'_part14'+'.mcfunction')
        except:
                pass
        try:
                os.remove(entrename+'_part15'+'.mcfunction')
        except:
                pass
        try:
                os.remove(entrename+'_part16'+'.mcfunction')
        except:
                pass
        try:
                os.remove(entrename+'_part17'+'.mcfunction')
        except:
                pass
        try:
                os.remove(entrename+'_part18'+'.mcfunction')
        except:
                pass
        try:
                os.remove(entrename+'_part19'+'.mcfunction')
        except:
                pass
        try:
                os.remove(entrename+'_part20'+'.mcfunction')
        except:
                pass
        try:
                os.remove('manifest.json')
        except:
                pass


