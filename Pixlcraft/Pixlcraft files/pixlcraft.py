from tkinter import *
from tkinter.ttk import *
from tkinter import filedialog
from PIL import ImageTk,Image
import os
from casegen import casegenerator
from tkinter import ttk
from tkinter import messagebox
from packmaker import addonfilemaker
import webbrowser


#from blocksinclude import blocksinclude


plugblocks = "ALLBLOCKS"

behaviorfilepath = os.getcwd() + "/main.py"

behaviorfilepath = behaviorfilepath.replace("\\", "/")
                                            
for i in range(len(behaviorfilepath)):
    if behaviorfilepath[-i] == "/":
        behaviorfilepath = behaviorfilepath[0:-i]
        break

for i in range(len(behaviorfilepath)):
    if behaviorfilepath[-i] == "/":
        behaviorfilepath = behaviorfilepath[0:-i]
        break

behaviorfilepath = behaviorfilepath + "/" +"Behavior Packs"
print(behaviorfilepath)              


#creates window
root = Tk()
root.title("Pixelcraft V1.0")
root.iconbitmap("pixlcraftlogo_tKt_icon.ico")
root.geometry("500x350")
print("Sucessfully loaded window!")


#declares a button style
style = Style()
style.configure('W.TButton', font =
               ('calibri', 10, 'bold'), 
                foreground = 'black')

#2nd button style
style2 = Style()
style2.configure('X.TButton', borderwidth = 0, background='white', foreground='black', border=0, font =('arial', 12, 'italic'))



#declares a canvas style
canvas_width = 390
canvas_height = 210

my_canvas = Canvas(root, width=canvas_width, height=canvas_height, highlightthickness=1, highlightbackground="gray")
my_canvas.configure(bg='white')

my_canvas.place(x=50, y=70)



startupimg = ImageTk.PhotoImage(Image.open("PixlCraftLogo.png"))

#loads image and puts it on canvas
canvasstartuplogo = my_canvas.create_image(195, 105,image=startupimg)





#widgets and functions:






#makes a prompt to name the function

def filenameinput():
    convertbtn.destroy()
    fileent.place(x=315, y=5)
    fileent.insert(0, "Enter_a_file_name")

    confbutton.place(x=355, y=30)
    rotateimgbtn.destroy()

    optionsbtn.destroy()






    
#color comparer
def warningmaker():
    messagebox.showinfo("Warning", "Depending on how large your image is, PixelCraft may become unresponsive.(This is normal) Please be patient and dont close the tab to prevent file corruption.")

    
    imgtofunc()
    


def imgtofunc():
    
    confbutton.destroy()
    fileent.place_forget()
    
    fullcommand1 = str("")
    fullcommand2 = str("")
    fullcommand3 = str("")
    fullcommand4 = str("")
    fullcommand5 = str("")
    fullcommand6 = str("")
    fullcommand7 = str("")
    fullcommand8 = str("")
    fullcommand9 = str("")
    fullcommand10 = str("")
    fullcommand11 = str("")
    fullcommand12 = str("")
    fullcommand13 = str("")
    fullcommand14 = str("")
    fullcommand15 = str("")
    fullcommand16 = str("")
    fullcommand17 = str("")
    fullcommand18 = str("")
    fullcommand19 = str("")
    fullcommand20 = str("")

    multij = 0

    
    steps = width/100

   
    #scans the pixels in x axis
    for i in range(width):

        
        #scans the pixels in y axis
        for j in range(height):

            
            #returns rgb values as tuple
           
            
            
            #mred, mgreen, mblue = imgfcalc.getpixel((i, j))
            mred, mgreen, mblue, mlight = image_rgba.getpixel((i, j))
            

            
            blockofpix = casegenerator(mred, mgreen, mblue, mlight, plugblocks)

            
            if r.get() == 1:
                singlecommand = "setblock" + " " + "~" + " " + "~" + str(j*-1) + " " + "~" + str(i) + " " + str(blockofpix) + "\n"
            elif r.get() == 2:
                singlecommand = "setblock" + " " + "~" + str(i) + " " + "~" + str(j*-1) + " " + "~" + " " + str(blockofpix) + "\n"
            elif r.get() == 3:
                singlecommand = "setblock" + " " + "~" + str(j*-1) + " " + "~" + " " + "~" + str(i) + " " + str(blockofpix) + "\n"


                
            if singlecommand.find("air") != -1:
                singlecommand = ""

            singlecommand = str(singlecommand)

        
            multij += 1
            
            if multij <= 10000: 
                fullcommand1 = fullcommand1 + singlecommand
                  
            if multij > 10000 and multij <= 20000:
                fullcommand2 = fullcommand2 + singlecommand

            if multij > 20000 and multij <= 30000:
                fullcommand3 = fullcommand3 + singlecommand

            if multij > 30000 and multij <= 40000:
                fullcommand4 = fullcommand4 + singlecommand

            if multij > 40000 and multij <= 50000:
                fullcommand5 = fullcommand5 + singlecommand

            if multij > 50000 and multij <= 60000:
                fullcommand6 = fullcommand6 + singlecommand

            if multij > 60000 and multij <= 70000:
                fullcommand7 = fullcommand7 + singlecommand

            if multij > 70000 and multij <= 80000:
                fullcommand8 = fullcommand8 + singlecommand

            if multij > 80000 and multij <= 90000:
                fullcommand9 = fullcommand9 + singlecommand

            if multij > 90000 and multij <= 100000:
                fullcommand10 = fullcommand10 + singlecommand

            if multij > 100000 and multij <= 110000:
                fullcommand11 = fullcommand11 + singlecommand

            if multij > 110000 and multij <= 120000:
                fullcommand12 = fullcommand12 + singlecommand

            if multij > 120000 and multij <= 130000:
                fullcommand13 = fullcommand13 + singlecommand

            if multij > 130000 and multij <= 140000:
                fullcommand14 = fullcommand14 + singlecommand

            if multij > 140000 and multij <= 150000:
                fullcommand15 = fullcommand15 + singlecommand

            if multij > 150000 and multij <= 160000:
                fullcommand16 = fullcommand16 + singlecommand

            if multij > 160000 and multij <= 170000:
                fullcommand17 = fullcommand17 + singlecommand
                
            if multij > 170000 and multij <= 180000:
                fullcommand18 = fullcommand18 + singlecommand
                
            if multij > 180000 and multij <= 190000:
                fullcommand19 = fullcommand19 + singlecommand
                
            if multij > 190000 and multij <= 200000:
                fullcommand20 = fullcommand20 + singlecommand

                
                
                

    if fullcommand1 != " ":            
            
            
        stringtosave1 = fullcommand1
    
        userentfilename = fileent.get() + ".mcfunction"

        functionfile = open(behaviorfilepath+"/"+userentfilename, 'w')
        functionfile.write(stringtosave1)
        functionfile.close()


    if fullcommand2 != " ":            
            
            
        stringtosave2 = fullcommand2
    
        userentfilename = fileent.get() + "_part2" + ".mcfunction"

        functionfile = open(behaviorfilepath+"/"+userentfilename, 'w')
        functionfile.write(stringtosave2)
        functionfile.close()


    if fullcommand3 != " ":            
            
            
        stringtosave3 = fullcommand3
    
        userentfilename = fileent.get() + "_part3" + ".mcfunction"

        functionfile = open(behaviorfilepath+"/"+userentfilename, 'w')
        functionfile.write(stringtosave3)
        functionfile.close()

    if fullcommand4 != " ":            
            
            
        stringtosave4 = fullcommand4
    
        userentfilename = fileent.get() + "_part4" + ".mcfunction"

        functionfile = open(behaviorfilepath+"/"+userentfilename, 'w')
        functionfile.write(stringtosave4)
        functionfile.close()

    if fullcommand5 != " ":            
            
            
        stringtosave5 = fullcommand5
    
        userentfilename = fileent.get() + "_part5" + ".mcfunction"

        functionfile = open(behaviorfilepath+"/"+userentfilename, 'w')
        functionfile.write(stringtosave5)
        functionfile.close()
        
    if fullcommand6 != " ":            
            
            
        stringtosave6 = fullcommand6
    
        userentfilename = fileent.get() + "_part6" + ".mcfunction"

        functionfile = open(behaviorfilepath+"/"+userentfilename, 'w')
        functionfile.write(stringtosave6)
        functionfile.close()

    if fullcommand7 != " ":            
            
            
        stringtosave7 = fullcommand7
    
        userentfilename = fileent.get() + "_part7" + ".mcfunction"

        functionfile = open(behaviorfilepath+"/"+userentfilename, 'w')
        functionfile.write(stringtosave7)
        functionfile.close()


    if fullcommand8 != " ":            
            
            
        stringtosave8 = fullcommand8
    
        userentfilename = fileent.get() + "_part8" + ".mcfunction"

        functionfile = open(behaviorfilepath+"/"+userentfilename, 'w')
        functionfile.write(stringtosave8)
        functionfile.close()

    if fullcommand9 != " ":            
            
            
        stringtosave9 = fullcommand9
    
        userentfilename = fileent.get() + "_part9" + ".mcfunction"

        functionfile = open(behaviorfilepath+"/"+userentfilename, 'w')
        functionfile.write(stringtosave9)
        functionfile.close()

    if fullcommand10 != " ":            
            
            
        stringtosave10 = fullcommand10
    
        userentfilename = fileent.get() + "_part10" + ".mcfunction"

        functionfile = open(behaviorfilepath+"/"+userentfilename, 'w')
        functionfile.write(stringtosave10)
        functionfile.close()

    if fullcommand11 != " ":            
            
            
        stringtosave11 = fullcommand11
    
        userentfilename = fileent.get() + "_part11" + ".mcfunction"

        functionfile = open(behaviorfilepath+"/"+userentfilename, 'w')
        functionfile.write(stringtosave11)
        functionfile.close()

    if fullcommand12 != " ":            
            
            
        stringtosave12 = fullcommand12
    
        userentfilename = fileent.get() + "_part12" + ".mcfunction"

        functionfile = open(behaviorfilepath+"/"+userentfilename, 'w')
        functionfile.write(stringtosave12)
        functionfile.close()

    if fullcommand13 != " ":            
            
            
        stringtosave13 = fullcommand13
    
        userentfilename = fileent.get() + "_part13" + ".mcfunction"

        functionfile = open(behaviorfilepath+"/"+userentfilename, 'w')
        functionfile.write(stringtosave13)
        functionfile.close()

    if fullcommand14 != " ":            
            
            
        stringtosave14 = fullcommand14
    
        userentfilename = fileent.get() + "_part14" + ".mcfunction"

        functionfile = open(behaviorfilepath+"/"+userentfilename, 'w')
        functionfile.write(stringtosave14)
        functionfile.close()

    if fullcommand15 != " ":            
            
            
        stringtosave15 = fullcommand15
    
        userentfilename = fileent.get() + "_part15" + ".mcfunction"

        functionfile = open(behaviorfilepath+"/"+userentfilename, 'w')
        functionfile.write(stringtosave15)
        functionfile.close()

    if fullcommand16 != " ":            
            
            
        stringtosave16 = fullcommand16
    
        userentfilename = fileent.get() + "_part16" + ".mcfunction"

        functionfile = open(behaviorfilepath+"/"+userentfilename, 'w')
        functionfile.write(stringtosave16)
        functionfile.close()

    if fullcommand17 != " ":            
            
            
        stringtosave17 = fullcommand17
    
        userentfilename = fileent.get() + "_part17" + ".mcfunction"

        functionfile = open(behaviorfilepath+"/"+userentfilename, 'w')
        functionfile.write(stringtosave17)
        functionfile.close()

    if fullcommand18 != " ":            
            
            
        stringtosave18 = fullcommand18
    
        userentfilename = fileent.get() + "_part18" + ".mcfunction"

        functionfile = open(behaviorfilepath+"/"+userentfilename, 'w')
        functionfile.write(stringtosave18)
        functionfile.close()

    if fullcommand19 != " ":            
            
            
        stringtosave19 = fullcommand19
    
        userentfilename = fileent.get() + "_part19" + ".mcfunction"

        functionfile = open(behaviorfilepath+"/"+userentfilename, 'w')
        functionfile.write(stringtosave19)
        functionfile.close()

    if fullcommand20 != " ":            
            
            
        stringtosave20 = fullcommand20
    
        userentfilename = fileent.get() + "_part20" + ".mcfunction"

        functionfile = open(behaviorfilepath+"/"+userentfilename, 'w')
        functionfile.write(stringtosave20)
        functionfile.close()
    





    #print(fullcommand)
    print('done')
    addonfilemaker(fileent.get(), userentfilename)

            
    #display restart button here         
            
    restartbtn.place(x=355, y=30)






#function executes after import button is pressed 
def importimages():
    #global variables must be defined in order for images to work
    global userchosenimg
    global userfile
    global newtext
    global width
    global height
    
    

    #file dialog prompt
    userfile = filedialog.askopenfilename(title="Select an image", filetypes = (("All Files", "*.*"), ("jpeg", ".jpeg"), ("jpg", ".jpg"), ("png", ".png")))



    #creates a variable of just the file name rather than the whole location
    for i in range(len(userfile)):
        userfilestrindex = userfile[i*-1]
        if userfilestrindex == "/":
            charsuntilslash = len(userfile) - i
            newtext = userfile[charsuntilslash+1:len(userfile)]
            break
        
    if len(newtext) >= 15:
        newtext = newtext[0:15]
        newtext = newtext + "..."
        print('changed')
            
            

    #displays name of selected image
    userimagefilename = Label(root, text=newtext, font=("Arial", 8))
    userimagefilename.place(x=40, y=30)


    #removes the import button
    importimages1.place_forget()
    
    #removes the default logo
    my_canvas.delete(canvasstartuplogo)

    #removes the name of the default image
    defaultimgfile.destroy()

    originallabel.destroy()

    fnorth.place(x=235, y=285)
    feast.place(x=235, y=305)
    fupwards.place(x=235, y=325)

    #copys the image and converts it so that it has a numeric value of rgb
    imgfcalcfunc(0)
def imgfcalcfunc(rotangle):
    global width
    global height
    global imgfcalc
    global image_rgba

    imgfcalc = Image.open(userfile)
    
    imgfcalc = imgfcalc.rotate(angle=rotangle)
                               
    width, height = imgfcalc.size
    image_rgba = imgfcalc.convert("RGBA")
    #dimensions label

    newimgdimstr = width, "x", height
    newimgdimlabel = Label(root, text=newimgdimstr, background='white', font=("Arial", 8, 'bold'))
    newimgdimlabel.place(x=375, y=260)

    
    
    loadontocanvas(0)
    #puts image on canvas
imgangle1 = 0
def loadontocanvas(rotationalangle):
    global resized
    global finalpic
    global userchosenimg1
    global userchosenimg
    
    print("loading...")
    try:
        my_canvas.delete(userchosenimg1)
    except:
        print("")
    numforrez = (width*175)/height
    
    userchosenimg = Image.open(userfile)
    resized = userchosenimg.resize((int(numforrez), 175), Image.ANTIALIAS)
    resized = resized.rotate(angle=imgangle1)
    finalpic = ImageTk.PhotoImage(resized)
    
    
    userchosenimg1 = my_canvas.create_image(195, 105,image=finalpic)
    
    
    print("successfully imported image")

    rotateimgbtn.place(x=355, y=300)

    convertbtn.place(x=160, y=27)
    
    
#end of function



def rotatetheimg():
    global imgangle1
    global rotq
    global rotp
    
    
    imgangle1 += 90
    if imgangle1 == 360:
        imgangle1 = 0

    
    loadontocanvas(imgangle1)
    imgfcalcfunc(imgangle1)
    
    
#the name of the default image file displayed when the window first starts up
defaultimgfile = Label(root, text='PixelCraftLogo.png')
defaultimgfile.place(x=40, y=30)
    
 
startupText = Label(root, text='Select an image file to create a behavior pack!', font=("calibri", 12))
startupText.place(x=0, y=0)



imageLabelText = Label(root, text='Image:', font=("Arial", 8, 'bold'))
imageLabelText.place(x=0, y=30)


#radio button

r = IntVar()
r.set("1")

fnorth = Radiobutton(root, text="Facing South", variable=r, value=1)
feast = Radiobutton(root, text="Facing West", variable=r, value=2)
fupwards = Radiobutton(root, text="Facing Upwards", variable=r, value=3)



radiob1 = r.get()





rotateimgbtn = Button(root, text='⭯', style = 'W.TButton', command=rotatetheimg)

importimages1 = Button(root, text='Browse', style = 'W.TButton', command=importimages)
importimages1.place(x=160, y=30)


convertbtn= Button(root, text='Create my files!', style = 'W.TButton', command=filenameinput)
fileent = Entry(root, width=20)
confbutton = Button(root, text='Confirm', style = 'W.TButton', command=warningmaker)

#width and height labels

originallabel = Label(root, text='224 x 183', background='white', font=("Arial", 8, 'bold'))
originallabel.place(x=375, y=260)



def restart_program():
    root.destroy()

 


restartbtn = Button(root, text="Close", style = 'W.TButton', command=restart_program) 


donatebtnimg = PhotoImage(file='paypal.png')

def openbrowser():
    webbrowser.open('https://www.paypal.com/paypalme/pixlcraft')


donatebutton = Button(root, text='Donate', image=donatebtnimg, compound = LEFT, style = 'X.TButton', command=openbrowser)
donatebutton.place(x=50, y=295)

#new code

def runoptions():
    global plugblocks

    
    root2 = Toplevel()
    root2.geometry("600x500")
    root2.title('Blocks')
    root2.iconbitmap('pixlcraftlogo_tKt_icon.ico')
    style = Style()
    style.configure('W.TButton', font =
                    ('calibri', 10, 'bold'), 
                    foreground = 'black')

    wool15img = ImageTk.PhotoImage(Image.open(os.getcwd()+"/textures/wool/wool_colored_black.png"))
    wool11img = ImageTk.PhotoImage(Image.open(os.getcwd()+"/textures/wool/wool_colored_blue.png"))
    wool12img = ImageTk.PhotoImage(Image.open(os.getcwd()+"/textures/wool/wool_colored_brown.png"))
    wool9img = ImageTk.PhotoImage(Image.open(os.getcwd()+"/textures/wool/wool_colored_cyan.png"))
    wool7img = ImageTk.PhotoImage(Image.open(os.getcwd()+"/textures/wool/wool_colored_gray.png"))
    wool13img = ImageTk.PhotoImage(Image.open(os.getcwd()+"/textures/wool/wool_colored_green.png"))
    wool3img = ImageTk.PhotoImage(Image.open(os.getcwd()+"/textures/wool/wool_colored_light_blue.png"))
    wool5img = ImageTk.PhotoImage(Image.open(os.getcwd()+"/textures/wool/wool_colored_lime.png"))
    wool2img = ImageTk.PhotoImage(Image.open(os.getcwd()+"/textures/wool/wool_colored_magenta.png"))
    wool1img = ImageTk.PhotoImage(Image.open(os.getcwd()+"/textures/wool/wool_colored_orange.png"))
    wool6img = ImageTk.PhotoImage(Image.open(os.getcwd()+"/textures/wool/wool_colored_pink.png"))
    wool10img = ImageTk.PhotoImage(Image.open(os.getcwd()+"/textures/wool/wool_colored_purple.png"))
    wool14img = ImageTk.PhotoImage(Image.open(os.getcwd()+"/textures/wool/wool_colored_red.png"))
    wool0img = ImageTk.PhotoImage(Image.open(os.getcwd()+"/textures/wool/wool_colored_white.png"))
    wool4img = ImageTk.PhotoImage(Image.open(os.getcwd()+"/textures/wool/wool_colored_yellow.png"))
    wool8img = ImageTk.PhotoImage(Image.open(os.getcwd()+"/textures/wool/wool_colored_light_gray.png"))



    terracotta15img = ImageTk.PhotoImage(Image.open(os.getcwd()+"/textures/terracotta/hardened_clay_stained_black.png"))
    terracotta11img = ImageTk.PhotoImage(Image.open(os.getcwd()+"/textures/terracotta/hardened_clay_stained_blue.png"))
    terracotta12img = ImageTk.PhotoImage(Image.open(os.getcwd()+"/textures/terracotta/hardened_clay_stained_brown.png"))
    terracotta13img = ImageTk.PhotoImage(Image.open(os.getcwd()+"/textures/terracotta/hardened_clay_stained_cyan.png"))
    terracotta9img = ImageTk.PhotoImage(Image.open(os.getcwd()+"/textures/terracotta/hardened_clay_stained_cyan.png"))
    terracotta7img = ImageTk.PhotoImage(Image.open(os.getcwd()+"/textures/terracotta/hardened_clay_stained_gray.png"))
    terracotta3img = ImageTk.PhotoImage(Image.open(os.getcwd()+"/textures/terracotta/hardened_clay_stained_light_blue.png"))
    terracotta5img = ImageTk.PhotoImage(Image.open(os.getcwd()+"/textures/terracotta/hardened_clay_stained_lime.png"))
    terracotta2img = ImageTk.PhotoImage(Image.open(os.getcwd()+"/textures/terracotta/hardened_clay_stained_magenta.png"))
    terracotta1img = ImageTk.PhotoImage(Image.open(os.getcwd()+"/textures/terracotta/hardened_clay_stained_orange.png"))
    terracotta6img = ImageTk.PhotoImage(Image.open(os.getcwd()+"/textures/terracotta/hardened_clay_stained_pink.png"))
    terracotta10img = ImageTk.PhotoImage(Image.open(os.getcwd()+"/textures/terracotta/hardened_clay_stained_purple.png"))
    terracotta14img = ImageTk.PhotoImage(Image.open(os.getcwd()+"/textures/terracotta/hardened_clay_stained_red.png"))
    terracotta0img = ImageTk.PhotoImage(Image.open(os.getcwd()+"/textures/terracotta/hardened_clay_stained_white.png"))
    terracotta4img = ImageTk.PhotoImage(Image.open(os.getcwd()+"/textures/terracotta/hardened_clay_stained_yellow.png"))
    terracotta8img = ImageTk.PhotoImage(Image.open(os.getcwd()+"/textures/terracotta/hardened_clay_stained_light_gray.png"))
    clay0img = ImageTk.PhotoImage(Image.open(os.getcwd()+"/textures/terracotta/hardened_clay.png"))

    wood4img = ImageTk.PhotoImage(Image.open(os.getcwd()+"/textures/wood/log_acacia.png"))
    wood5img = ImageTk.PhotoImage(Image.open(os.getcwd()+"/textures/wood/log_big_oak.png"))
    wood2img = ImageTk.PhotoImage(Image.open(os.getcwd()+"/textures/wood/log_birch.png"))
    wood3img = ImageTk.PhotoImage(Image.open(os.getcwd()+"/textures/wood/log_jungle.png"))
    woodimg = ImageTk.PhotoImage(Image.open(os.getcwd()+"/textures/wood/log_oak.png"))
    wood1img = ImageTk.PhotoImage(Image.open(os.getcwd()+"/textures/wood/log_spruce.png"))

    planks4img = ImageTk.PhotoImage(Image.open(os.getcwd()+"/textures/wood/planks_acacia.png"))
    planks5img = ImageTk.PhotoImage(Image.open(os.getcwd()+"/textures/wood/planks_big_oak.png"))
    planks2img = ImageTk.PhotoImage(Image.open(os.getcwd()+"/textures/wood/planks_birch.png"))
    planks3img = ImageTk.PhotoImage(Image.open(os.getcwd()+"/textures/wood/planks_jungle.png"))
    planksimg = ImageTk.PhotoImage(Image.open(os.getcwd()+"/textures/wood/planks_oak.png"))
    planks1img = ImageTk.PhotoImage(Image.open(os.getcwd()+"/textures/wood/planks_spruce.png"))

    strippedacaciaimg = ImageTk.PhotoImage(Image.open(os.getcwd()+"/textures/wood/stripped_acacia_log.png"))
    strippedbirchimg = ImageTk.PhotoImage(Image.open(os.getcwd()+"/textures/wood/stripped_birch_log.png"))
    strippeddarkoakimg = ImageTk.PhotoImage(Image.open(os.getcwd()+"/textures/wood/stripped_dark_oak_log.png"))
    strippedjungleimg = ImageTk.PhotoImage(Image.open(os.getcwd()+"/textures/wood/stripped_jungle_log.png"))
    strippedoakimg = ImageTk.PhotoImage(Image.open(os.getcwd()+"/textures/wood/stripped_oak_log.png"))
    strippedspruceimg = ImageTk.PhotoImage(Image.open(os.getcwd()+"/textures/wood/stripped_spruce_log.png"))









    wool15int = IntVar(value=1)
    wool11int = IntVar(value=1)
    wool12int = IntVar(value=1)
    wool9int = IntVar(value=1)
    wool7int = IntVar(value=1)
    wool13int = IntVar(value=1)
    wool3int = IntVar(value=1)
    wool5int = IntVar(value=1)
    wool2int = IntVar(value=1)
    wool1int = IntVar(value=1)
    wool6int = IntVar(value=1)
    wool10int = IntVar(value=1)
    wool14int = IntVar(value=1)
    wool0int = IntVar(value=1)
    wool4int = IntVar(value=1)
    wool8int = IntVar(value=1)

    def sdwoolall():
        if wool0int.get() == 1:
            wool0int.set(value=0)
            wool1int.set(value=0)
            wool2int.set(value=0)
            wool3int.set(value=0)
            wool4int.set(value=0)
            wool5int.set(value=0)
            wool6int.set(value=0)
            wool7int.set(value=0)
            wool8int.set(value=0)
            wool9int.set(value=0)
            wool10int.set(value=0)
            wool11int.set(value=0)
            wool12int.set(value=0)
            wool13int.set(value=0)
            wool14int.set(value=0)
            wool15int.set(value=0)
        elif wool0int.get() == 0:
            wool0int.set(value=1)
            wool1int.set(value=1)
            wool2int.set(value=1)
            wool3int.set(value=1)
            wool4int.set(value=1)
            wool5int.set(value=1)
            wool6int.set(value=1)
            wool7int.set(value=1)
            wool8int.set(value=1)
            wool9int.set(value=1)
            wool10int.set(value=1)
            wool11int.set(value=1)
            wool12int.set(value=1)
            wool13int.set(value=1)
            wool14int.set(value=1)
            wool15int.set(value=1)
            
    selectallwool = Button(root2, style='W.TButton', text='Select/Deselect All', command=sdwoolall)
    selectallwool.place(x=31, y=40)

        #wool 15
    wool15labimg = Label(root2, image=wool15img)
    wool15labcheck = Checkbutton(root2, text="Black Wool", variable=wool15int)
    wool15labcheck.place(x=46, y=70)
    wool15labimg.place(x=30, y=70)
        #wool 11
    wool11labimg = Label(root2, image=wool11img)
    wool11labcheck = Checkbutton(root2, text="Blue Wool", variable=wool11int)
    wool11labcheck.place(x=46, y=90)
    wool11labimg.place(x=30, y=90)
        #wool 12
    wool12labimg = Label(root2, image=wool12img)
    wool12labcheck = Checkbutton(root2, text="Brown Wool", variable=wool12int)
    wool12labcheck.place(x=46, y=110)
    wool12labimg.place(x=30, y=110)
        #wool 9
    wool9labimg = Label(root2, image=wool9img)
    wool9labcheck = Checkbutton(root2, text="Cyan Wool", variable=wool9int)
    wool9labcheck.place(x=46, y=130)
    wool9labimg.place(x=30, y=130)
        #wool 7
    wool7labimg = Label(root2, image=wool7img)
    wool7labcheck = Checkbutton(root2, text="Gray Wool", variable=wool7int)
    wool7labcheck.place(x=46, y=150)
    wool7labimg.place(x=30, y=150)
        #wool 13
    wool13labimg = Label(root2, image=wool13img)
    wool13labcheck = Checkbutton(root2, text="Green Wool", variable=wool13int)
    wool13labcheck.place(x=46, y=170)
    wool13labimg.place(x=30, y=170)
        #wool 3
    wool3labimg = Label(root2, image=wool3img)
    wool3labcheck = Checkbutton(root2, text="Light Blue Wool", variable=wool3int)
    wool3labcheck.place(x=46, y=190)
    wool3labimg.place(x=30, y=190)
        #wool 5
    wool5labimg = Label(root2, image=wool5img)
    wool5labcheck = Checkbutton(root2, text="Lime Wool", variable=wool5int)
    wool5labcheck.place(x=46, y=210)
    wool5labimg.place(x=30, y=210)
        #wool 2
    wool2labimg = Label(root2, image=wool2img)
    wool2labcheck = Checkbutton(root2, text="Magenta Wool", variable=wool2int)
    wool2labcheck.place(x=46, y=230)
    wool2labimg.place(x=30, y=230)
        #wool 1
    wool1labimg = Label(root2, image=wool1img)
    wool1labcheck = Checkbutton(root2, text="Orange Wool", variable=wool1int)
    wool1labcheck.place(x=46, y=250)
    wool1labimg.place(x=30, y=250)
        #wool 6
    wool6labimg = Label(root2, image=wool6img)
    wool6labcheck = Checkbutton(root2, text="Pink Wool", variable=wool6int)
    wool6labcheck.place(x=46, y=270)
    wool6labimg.place(x=30, y=270)
        #wool 10
    wool10labimg = Label(root2, image=wool10img)
    wool10labcheck = Checkbutton(root2, text="Purple Wool", variable=wool10int)
    wool10labcheck.place(x=46, y=290)
    wool10labimg.place(x=30, y=290)
        #wool 14
    wool14labimg = Label(root2, image=wool14img)
    wool14labcheck = Checkbutton(root2, text="Red Wool", variable=wool14int)
    wool14labcheck.place(x=46, y=310)
    wool14labimg.place(x=30, y=310)
        #wool 0
    wool0labimg = Label(root2, image=wool0img)
    wool0labcheck = Checkbutton(root2, text="White Wool", variable=wool0int)
    wool0labcheck.place(x=46, y=330)
    wool0labimg.place(x=30, y=330)
        #wool 4
    wool4labimg = Label(root2, image=wool4img)
    wool4labcheck = Checkbutton(root2, text="Yellow Wool", variable=wool4int)
    wool4labcheck.place(x=46, y=350)
    wool4labimg.place(x=30, y=350)
        #wool 8
    wool8labimg = Label(root2, image=wool8img)
    wool8labcheck = Checkbutton(root2, text="Light Gray Wool", variable=wool8int)
    wool8labcheck.place(x=46, y=370)
    wool8labimg.place(x=30, y=370)



    #terracotta


    terracotta15int = IntVar(value=1)
    terracotta11int = IntVar(value=1)
    terracotta12int = IntVar(value=1)
    terracotta9int = IntVar(value=1)
    terracotta7int = IntVar(value=1)
    terracotta13int = IntVar(value=1)
    terracotta3int = IntVar(value=1)
    terracotta5int = IntVar(value=1)
    terracotta2int = IntVar(value=1)
    terracotta1int = IntVar(value=1)
    terracotta6int = IntVar(value=1)
    terracotta10int = IntVar(value=1)
    terracotta14int = IntVar(value=1)
    terracotta0int = IntVar(value=1)
    terracotta4int = IntVar(value=1)
    terracotta8int = IntVar(value=1)
    clay0int = IntVar(value=1)
    def sdterracottaall():
        if terracotta0int.get() == 1:
            terracotta0int.set(value=0)
            terracotta1int.set(value=0)
            terracotta2int.set(value=0)
            terracotta3int.set(value=0)
            terracotta4int.set(value=0)
            terracotta5int.set(value=0)
            terracotta6int.set(value=0)
            terracotta7int.set(value=0)
            terracotta8int.set(value=0)
            terracotta9int.set(value=0)
            terracotta10int.set(value=0)
            terracotta11int.set(value=0)
            terracotta12int.set(value=0)
            terracotta13int.set(value=0)
            terracotta14int.set(value=0)
            terracotta15int.set(value=0)
            clay0int.set(value=0)
        elif terracotta0int.get() == 0:
            terracotta0int.set(value=1)
            terracotta1int.set(value=1)
            terracotta2int.set(value=1)
            terracotta3int.set(value=1)
            terracotta4int.set(value=1)
            terracotta5int.set(value=1)
            terracotta6int.set(value=1)
            terracotta7int.set(value=1)
            terracotta8int.set(value=1)
            terracotta9int.set(value=1)
            terracotta10int.set(value=1)
            terracotta11int.set(value=1)
            terracotta12int.set(value=1)
            terracotta13int.set(value=1)
            terracotta14int.set(value=1)
            terracotta15int.set(value=1)
            clay0int.set(value=1)
    selectallterracotta = Button(root2, style='W.TButton', text='Select/Deselect All', command=sdterracottaall)
    selectallterracotta.place(x=201, y=40)


        #clay
    clay0labimg = Label(root2, image=clay0img)
    clay0labcheck = Checkbutton(root2, text="Hardened Clay", variable=clay0int)
    clay0labcheck.place(x=216, y=390)
    clay0labimg.place(x=200, y=390)





        #terracotta 15
    terracotta15labimg = Label(root2, image=terracotta15img)
    terracotta15labcheck = Checkbutton(root2, text="Black terracotta", variable=terracotta15int)
    terracotta15labcheck.place(x=216, y=70)
    terracotta15labimg.place(x=200, y=70)
        #terracotta 11
    terracotta11labimg = Label(root2, image=terracotta11img)
    terracotta11labcheck = Checkbutton(root2, text="Blue terracotta", variable=terracotta11int)
    terracotta11labcheck.place(x=216, y=90)
    terracotta11labimg.place(x=200, y=90)
        #terracotta 12
    terracotta12labimg = Label(root2, image=terracotta12img)
    terracotta12labcheck = Checkbutton(root2, text="Brown terracotta", variable=terracotta12int)
    terracotta12labcheck.place(x=216, y=110)
    terracotta12labimg.place(x=200, y=110)
        #terracotta 9
    terracotta9labimg = Label(root2, image=terracotta9img)
    terracotta9labcheck = Checkbutton(root2, text="Cyan terracotta", variable=terracotta9int)
    terracotta9labcheck.place(x=216, y=130)
    terracotta9labimg.place(x=200, y=130)
        #terracotta 7
    terracotta7labimg = Label(root2, image=terracotta7img)
    terracotta7labcheck = Checkbutton(root2, text="Gray terracotta", variable=terracotta7int)
    terracotta7labcheck.place(x=216, y=150)
    terracotta7labimg.place(x=200, y=150)
        #terracotta 13
    terracotta13labimg = Label(root2, image=terracotta13img)
    terracotta13labcheck = Checkbutton(root2, text="Green terracotta", variable=terracotta13int)
    terracotta13labcheck.place(x=216, y=170)
    terracotta13labimg.place(x=200, y=170)
        #terracotta 3
    terracotta3labimg = Label(root2, image=terracotta3img)
    terracotta3labcheck = Checkbutton(root2, text="Light Blue terracotta", variable=terracotta3int)
    terracotta3labcheck.place(x=216, y=190)
    terracotta3labimg.place(x=200, y=190)
        #terracotta 5
    terracotta5labimg = Label(root2, image=terracotta5img)
    terracotta5labcheck = Checkbutton(root2, text="Lime terracotta", variable=terracotta5int)
    terracotta5labcheck.place(x=216, y=210)
    terracotta5labimg.place(x=200, y=210)
        #terracotta 2
    terracotta2labimg = Label(root2, image=terracotta2img)
    terracotta2labcheck = Checkbutton(root2, text="Magenta terracotta", variable=terracotta2int)
    terracotta2labcheck.place(x=216, y=230)
    terracotta2labimg.place(x=200, y=230)
        #terracotta 1
    terracotta1labimg = Label(root2, image=terracotta1img)
    terracotta1labcheck = Checkbutton(root2, text="Orange terracotta", variable=terracotta1int)
    terracotta1labcheck.place(x=216, y=250)
    terracotta1labimg.place(x=200, y=250)
        #terracotta 6
    terracotta6labimg = Label(root2, image=terracotta6img)
    terracotta6labcheck = Checkbutton(root2, text="Pink terracotta", variable=terracotta6int)
    terracotta6labcheck.place(x=216, y=270)
    terracotta6labimg.place(x=200, y=270)
        #terracotta 10
    terracotta10labimg = Label(root2, image=terracotta10img)
    terracotta10labcheck = Checkbutton(root2, text="Purple terracotta", variable=terracotta10int)
    terracotta10labcheck.place(x=216, y=290)
    terracotta10labimg.place(x=200, y=290)
        #terracotta 14
    terracotta14labimg = Label(root2, image=terracotta14img)
    terracotta14labcheck = Checkbutton(root2, text="Red terracotta", variable=terracotta14int)
    terracotta14labcheck.place(x=216, y=310)
    terracotta14labimg.place(x=200, y=310)
        #terracotta 0
    terracotta0labimg = Label(root2, image=terracotta0img)
    terracotta0labcheck = Checkbutton(root2, text="White terracotta", variable=terracotta0int)
    terracotta0labcheck.place(x=216, y=330)
    terracotta0labimg.place(x=200, y=330)
        #terracotta 4
    terracotta4labimg = Label(root2, image=terracotta4img)
    terracotta4labcheck = Checkbutton(root2, text="Yellow terracotta", variable=terracotta4int)
    terracotta4labcheck.place(x=216, y=350)
    terracotta4labimg.place(x=200, y=350)
        #terracotta 8
    terracotta8labimg = Label(root2, image=terracotta8img)
    terracotta8labcheck = Checkbutton(root2, text="Light Gray terracotta", variable=terracotta8int)
    terracotta8labcheck.place(x=216, y=370)
    terracotta8labimg.place(x=200, y=370)










    #woods
    wood4int = IntVar(value=1)
    wood5int = IntVar(value=1)
    wood2int = IntVar(value=1)
    wood3int = IntVar(value=1)
    woodint = IntVar(value=1)
    wood1int = IntVar(value=1)

    planks4int = IntVar(value=1)
    planks5int = IntVar(value=1)
    planks2int = IntVar(value=1)
    planks3int = IntVar(value=1)
    planksint = IntVar(value=1)
    planks1int = IntVar(value=1)

    strippedacaciaint = IntVar(value=1)
    strippedbirchint = IntVar(value=1)
    strippeddarkoakint = IntVar(value=1)
    strippedjungleint = IntVar(value=1)
    strippedoakint = IntVar(value=1)
    strippedspruceint = IntVar(value=1)


    def sdwoodall():
        if woodint.get() == 1:
            wood4int.set(value=0)
            wood5int.set(value=0)
            wood2int.set(value=0)
            wood3int.set(value=0)
            woodint.set(value=0)
            wood1int.set(value=0)

            planks4int.set(value=0)
            planks5int.set(value=0)
            planks2int.set(value=0)
            planks3int.set(value=0)
            planksint.set(value=0)
            planks1int.set(value=0)

            strippedacaciaint.set(value=0)
            strippedbirchint.set(value=0)
            strippeddarkoakint.set(value=0)
            strippedjungleint.set(value=0)
            strippedoakint.set(value=0)
            strippedspruceint.set(value=0)
            
        elif woodint.get() == 0:
            wood4int.set(value=1)
            wood5int.set(value=1)
            wood2int.set(value=1)
            wood3int.set(value=1)
            woodint.set(value=1)
            wood1int.set(value=1)

            planks4int.set(value=1)
            planks5int.set(value=1)
            planks2int.set(value=1)
            planks3int.set(value=1)
            planksint.set(value=1)
            planks1int.set(value=1)

            strippedacaciaint.set(value=1)
            strippedbirchint.set(value=1)
            strippeddarkoakint.set(value=1)
            strippedjungleint.set(value=1)
            strippedoakint.set(value=1)
            strippedspruceint.set(value=1)
            

    selectallwood = Button(root2, style='W.TButton', text='Select/Deselect All', command=sdwoodall)
    selectallwood.place(x=371, y=40)



        #terracotta 15
    wood4labimg = Label(root2, image=wood4img)
    wood4labcheck = Checkbutton(root2, text="Acacia log", variable=wood4int)
    wood4labcheck.place(x=386, y=70)
    wood4labimg.place(x=370, y=70)
        #terracotta 11
    wood5labimg = Label(root2, image=wood5img)
    wood5labcheck = Checkbutton(root2, text="Dark Oak log", variable=wood5int)
    wood5labcheck.place(x=386, y=90)
    wood5labimg.place(x=370, y=90)
        #terracotta 12
    wood2labimg = Label(root2, image=wood2img)
    wood2labcheck = Checkbutton(root2, text="Birch log", variable=wood2int)
    wood2labcheck.place(x=386, y=110)
    wood2labimg.place(x=370, y=110)
        #terracotta 9
    wood3labimg = Label(root2, image=wood3img)
    wood3labcheck = Checkbutton(root2, text="Jungle log", variable=wood3int)
    wood3labcheck.place(x=386, y=130)
    wood3labimg.place(x=370, y=130)
        #terracotta 7
    woodlabimg = Label(root2, image=woodimg)
    woodlabcheck = Checkbutton(root2, text="Oak log", variable=woodint)
    woodlabcheck.place(x=386, y=150)
    woodlabimg.place(x=370, y=150)
        #terracotta 13
    wood1labimg = Label(root2, image=wood1img)
    wood1labcheck = Checkbutton(root2, text="Spruce log", variable=wood1int)
    wood1labcheck.place(x=386, y=170)
    wood1labimg.place(x=370, y=170)
        #terracotta 3
    planks4labimg = Label(root2, image=planks4img)
    planks4labcheck = Checkbutton(root2, text="Acacia planks", variable=planks4int)
    planks4labcheck.place(x=386, y=190)
    planks4labimg.place(x=370, y=190)
        #terracotta 5
    planks5labimg = Label(root2, image=planks5img)
    planks5labcheck = Checkbutton(root2, text="Dark Oak planks", variable=planks5int)
    planks5labcheck.place(x=386, y=210)
    planks5labimg.place(x=370, y=210)
        #terracotta 2
    planks2labimg = Label(root2, image=planks2img)
    planks2labcheck = Checkbutton(root2, text="Birch planks", variable=planks2int)
    planks2labcheck.place(x=386, y=230)
    planks2labimg.place(x=370, y=230)
        #terracotta 1
    planks3labimg = Label(root2, image=planks3img)
    planks3labcheck = Checkbutton(root2, text="Jungle Planks", variable=planks3int)
    planks3labcheck.place(x=386, y=250)
    planks3labimg.place(x=370, y=250)
        #terracotta 6
    plankslabimg = Label(root2, image=planksimg)
    plankslabcheck = Checkbutton(root2, text="Oak planks", variable=planksint)
    plankslabcheck.place(x=386, y=270)
    plankslabimg.place(x=370, y=270)
        #terracotta 10
    planks1labimg = Label(root2, image=planks1img)
    planks1labcheck = Checkbutton(root2, text="Spruce planks", variable=planks1int)
    planks1labcheck.place(x=386, y=290)
    planks1labimg.place(x=370, y=290)
        #terracotta 14
    strippedacacialabimg = Label(root2, image=strippedacaciaimg)
    strippedacacialabcheck = Checkbutton(root2, text="Stripped Acacia log", variable=strippedacaciaint)
    strippedacacialabcheck.place(x=386, y=310)
    strippedacacialabimg.place(x=370, y=310)
        #terracotta 0
    strippedbirchlabimg = Label(root2, image=strippedbirchimg)
    strippedbirchlabcheck = Checkbutton(root2, text="Stripped Birch log", variable=strippedbirchint)
    strippedbirchlabcheck.place(x=386, y=330)
    strippedbirchlabimg.place(x=370, y=330)
        #terracotta 4
    strippeddarkoaklabimg = Label(root2, image=strippeddarkoakimg)
    strippeddarkoaklabcheck = Checkbutton(root2, text="Stripped Dark Oak log", variable=strippeddarkoakint)
    strippeddarkoaklabcheck.place(x=386, y=350)
    strippeddarkoaklabimg.place(x=370, y=350)
        #terracotta 8
    strippedjunglelabimg = Label(root2, image=strippedjungleimg)
    strippedjunglelabcheck = Checkbutton(root2, text="Stripped Jungle log", variable=strippedjungleint)
    strippedjunglelabcheck.place(x=386, y=370)
    strippedjunglelabimg.place(x=370, y=370)

    strippedoaklabimg = Label(root2, image=strippedoakimg)
    strippedoaklabcheck = Checkbutton(root2, text="Stripped Oak log", variable=strippedoakint)
    strippedoaklabcheck.place(x=386, y=390)
    strippedoaklabimg.place(x=370, y=390)

    strippedsprucelabimg = Label(root2, image=strippedspruceimg)
    strippedsprucelabcheck = Checkbutton(root2, text="Stripped Spruce log", variable=strippedspruceint)
    strippedsprucelabcheck.place(x=386, y=410)
    strippedsprucelabimg.place(x=370, y=410)








    #conclusion

    def concludechosenblocks():
        global concludinglist
        concludinglist = []
        if wool15int.get() == 1:
            concludinglist = concludinglist + ["case1"]
        if wool11int.get() == 1:
            concludinglist = concludinglist + ["case2"]
        if wool12int.get() == 1:
            concludinglist = concludinglist + ["case3"]
        if wool9int.get() == 1:
            concludinglist = concludinglist + ["case4"]
        if wool7int.get() == 1:
            concludinglist = concludinglist + ["case5"]
        if wool13int.get() == 1:
            concludinglist = concludinglist + ["case6"]
        if wool3int.get() == 1:
            concludinglist = concludinglist + ["case7"]
        if wool5int.get() == 1:
            concludinglist = concludinglist + ["case8"]
        if wool2int.get() == 1:
            concludinglist = concludinglist + ["case9"]
        if wool1int.get() == 1:
            concludinglist = concludinglist + ["case10"]
        if wool6int.get() == 1:
            concludinglist = concludinglist + ["case11"]
        if wool10int.get() == 1:
            concludinglist = concludinglist + ["case12"]
        if wool14int.get() == 1:
            concludinglist = concludinglist + ["case13"]
        if wool0int.get() == 1:
            concludinglist = concludinglist + ["case14"]
        if wool4int.get() == 1:
            concludinglist = concludinglist + ["case15"]
        if wool8int.get() == 1:
            concludinglist = concludinglist + ["case32"]






        #hardened clay
        if clay0int.get() == 1:
            concludinglist = concludinglist + ["case16"]

            
        if terracotta15int.get() == 1:
            concludinglist = concludinglist + ["case17"]
        if terracotta11int.get() == 1:
            concludinglist = concludinglist + ["case18"]
        if terracotta12int.get() == 1:
            concludinglist = concludinglist + ["case19"]
        if terracotta9int.get() == 1:
            concludinglist = concludinglist + ["case20"]
        if terracotta7int.get() == 1:
            concludinglist = concludinglist + ["case21"]
        if terracotta13int.get() == 1:
            concludinglist = concludinglist + ["case22"]
        if terracotta3int.get() == 1:
            concludinglist = concludinglist + ["case23"]
        if terracotta5int.get() == 1:
            concludinglist = concludinglist + ["case24"]
        if terracotta2int.get() == 1:
            concludinglist = concludinglist + ["case25"]
        if terracotta1int.get() == 1:
            concludinglist = concludinglist + ["case26"]
        if terracotta6int.get() == 1:
            concludinglist = concludinglist + ["case27"]
        if terracotta10int.get() == 1:
            concludinglist = concludinglist + ["case28"]
        if terracotta14int.get() == 1:
            concludinglist = concludinglist + ["case29"]
        if terracotta0int.get() == 1:
            concludinglist = concludinglist + ["case30"]
        if terracotta4int.get() == 1:
            concludinglist = concludinglist + ["case31"]
        if terracotta8int.get() == 1:
            concludinglist = concludinglist + ["case33"]


        if wood4int.get() == 1:
            concludinglist = concludinglist + ["case34"]
        if wood5int.get() == 1:
            concludinglist = concludinglist + ["case35"]
        if wood2int.get() == 1:
            concludinglist = concludinglist + ["case36"]
        if wood3int.get() == 1:
            concludinglist = concludinglist + ["case37"]
        if woodint.get() == 1:
            concludinglist = concludinglist + ["case38"]
        if wood1int.get() == 1:
            concludinglist = concludinglist + ["case39"]
        if planks4int.get() == 1:
            concludinglist = concludinglist + ["case40"]
        if planks5int.get() == 1:
            concludinglist = concludinglist + ["case41"]
        if planks2int.get() == 1:
            concludinglist = concludinglist + ["case42"]
        if planks3int.get() == 1:
            concludinglist = concludinglist + ["case43"]
        if planksint.get() == 1:
            concludinglist = concludinglist + ["case44"]
        if planks1int.get() == 1:
            concludinglist = concludinglist + ["case45"]
        if strippedacaciaint.get() == 1:
            concludinglist = concludinglist + ["case46"]
        if strippedbirchint.get() == 1:
            concludinglist = concludinglist + ["case47"]
        if strippeddarkoakint.get() == 1:
            concludinglist = concludinglist + ["case48"]
        if strippedjungleint.get() == 1:
            concludinglist = concludinglist + ["case49"]
        if strippedoakint.get() == 1:
            concludinglist = concludinglist + ["case50"]
        if strippedspruceint.get() == 1:
            concludinglist = concludinglist + ["case51"]

        
        


        try:
            return concludinglist
        except:
            return "ALLBLOCKS"



    def quittop():
        root2.quit()
        root2.destroy()
        
    quitbtn = Button(root2, text='Confirm', command=quittop)
    
    quitbtn.place(x=500, y=5)
    
    
    
    root2.mainloop()

    
    plugblocks = concludechosenblocks()
    print(plugblocks)


    

optionsbtn = Button(root, text="Options", style = 'W.TButton', command=runoptions)
optionsbtn.place(x=375, y=15)





root.mainloop()
