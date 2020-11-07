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
#color comparer
def warningmaker():
    messagebox.showinfo("Warning", "Depending on how large your image is, PixelCraft may become unresponsive.(This is normal) Please be patient and dont close the tab to prevent file corruption.")

    
    imgtofunc()
    


def imgtofunc():
    
    confbutton.destroy()
    fileent.place_forget()
    
    fullcommand1 = str(" ")
    fullcommand2 = str(" ")
    fullcommand3 = str(" ")
    fullcommand4 = str(" ")
    fullcommand5 = str(" ")
    fullcommand6 = str(" ")
    fullcommand7 = str(" ")
    fullcommand8 = str(" ")
    fullcommand9 = str(" ")
    fullcommand10 = str(" ")
    fullcommand11 = str(" ")
    fullcommand12 = str(" ")
    fullcommand13 = str(" ")
    fullcommand14 = str(" ")
    fullcommand15 = str(" ")
    fullcommand16 = str(" ")
    fullcommand17 = str(" ")
    fullcommand18 = str(" ")
    fullcommand19 = str(" ")
    fullcommand20 = str(" ")

    multij = 0

    
    steps = width/100

   
    #scans the pixels in x axis
    for i in range(width):

        
        #scans the pixels in y axis
        for j in range(height):

            
            #returns rgb values as tuple
           
            
            
            #mred, mgreen, mblue = imgfcalc.getpixel((i, j))
            mred, mgreen, mblue, mlight = image_rgba.getpixel((i, j))
            

            
            blockofpix = casegenerator(mred, mgreen, mblue, mlight)

            
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




root.mainloop()
