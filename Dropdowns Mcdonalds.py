import tkinter as tk
from time import gmtime, strftime
import os

#Please read EULA

filename2 = ("./Orders/TotalOrders/Items.txt")
with open(filename2, "w+") as f2b:
    f2b.write("")
    #f2b.write("Total Items: \n\n")

totalOrder=[]
def resetAllMenus():
    sandwhich.set("None")
    sandwhichquantity.set("0")
    sandwhichsize.set("Normal")

    signature.set("None")
    signaturequantity.set("0")
    signaturesize.set("Normal")

    wrap.set("None")
    wrapquantity.set("0")
    wrapsize.set("Normal")

    fries.set("None")
    friesquantity.set("0")
    friessize.set("Normal")

    saver.set("None")
    saverquantity.set("0")
    saversize.set("Normal")

    happyMeal.set("None")
    happyMealquantity.set("0")
    happyMealsize.set("Normal")

    breakfast.set("None")
    breakfastquantity.set("0")
    breakfastsize.set("Individual")

    deserts.set("None")
    desertssize.set("")
    desertsquantity.set("0")

    nameEntryBox.delete(0, 'end')
    
    workOutTotal()

def addFinalOrder():
    global totalOrder
    if nameEntryBox.get() != "":
        workOutTotal()
        totalPrice = (float(sandwhichTotal()) + float(sigTotal()) + float(wrapsTotal()) + float(friesTotal()) + float(breakfastTotal()) + float(desertsTotal()) + float(happyMealTotal()) + float(saverMenuTotal()))
        currentTime = strftime("%Y-%m-%d %H:%M:%S", gmtime())
        totalOrder = [[nameEntryBox.get(),totalPrice,currentTime],[sandwhich.get(),sandwhichquantity.get(),sandwhichsize.get()],[signature.get(),signaturequantity.get(),signaturesize.get()],[wrap.get(),wrapquantity.get(),wrapsize.get()],[fries.get(),friesquantity.get(),friessize.get()],[saver.get(),saverquantity.get(),saversize.get()],[happyMeal.get(),happyMealquantity.get(),happyMealsize.get()],[breakfast.get(),breakfastquantity.get(),breakfastsize.get()],[deserts.get(),desertsquantity.get(),desertssize.get()]]
        resetAllMenus()
        addToFile()


def spaceCreator(string,when):
    if when == 0:
        comparison=45
    elif when == 1:
        comparison=20
        
    exactNumberOfSpaces=(":")
    spaceNumber=comparison-(int(len(string)))
    x = exactNumberOfSpaces.ljust(spaceNumber)
        
    return (x)
    
def addToFile():
    global totalOrder
    stop=False
    
    filename = ("./Orders/" + str(totalOrder[0][0]) + ".txt")
    os.makedirs(os.path.dirname(filename), exist_ok=True)
    with open(filename, "w") as f:
        f.write("TOTAL ORDER:\n\n")
        f.write(str(totalOrder[0][0]) + "     "  + str(totalOrder[0][2]) + "     " + str(totalOrder[0][1]) + "\n\n")
        for i in range(8):
            if (totalOrder[(i+1)][0] != "None") and (totalOrder[(i+1)][1] != "0"):
                f.write(str(totalOrder[(i+1)][0]) + str(spaceCreator(str(totalOrder[(i+1)][0]),0))  + str(totalOrder[(i+1)][2]) + str(spaceCreator(str(totalOrder[(i+1)][2]),1)) + str(totalOrder[(i+1)][1]) + ":\n")
                print(totalOrder[i+1])            
    f.close
    
    filename2 = ("./Orders/TotalOrders/Items.txt")
    os.makedirs(os.path.dirname(filename2), exist_ok=True)
    with open(filename2, "r+") as f2:
        data = []
        for i in range(8):
            if (totalOrder[(i+1)][0] != "None") and (totalOrder[(i+1)][1] != "0"):
                foodToAdd= (str(totalOrder[(i+1)][0]) + str(spaceCreator(str(totalOrder[(i+1)][0]),0))  + str(totalOrder[(i+1)][2]) + str(spaceCreator(str(totalOrder[(i+1)][2]),1)) + str(totalOrder[(i+1)][1]) + ":\n")
                #print(foodToAdd)
                foodToAdd = [x.strip(' ') for x in foodToAdd]
                #print (foodToAdd)
                foodToAdd=''.join(foodToAdd)
                #print (foodToAdd)
                data.append(foodToAdd)
        f2.close

    with open(filename2, "a") as f2b:
        f2b.writelines( data )
        f2b.close

    with open(filename2, "r+") as f2c:
        lines = [line.rstrip('\n') for line in f2c]
        lengthOfFile=len(lines)
        for i in range(0,lengthOfFile):
            for n in range(0,lengthOfFile):
                l1=((lines[i].split(':'))[0])
                l2=((lines[n].split(':'))[0])

                l1a=((lines[i].split(':'))[1])
                l2a=((lines[n].split(':'))[1])
                
                if (l1 == l2) and (l1a == l2a) and (i != n ) and (stop==False):
                    fixRepeats(i,n,lines)
                    stop=True
    f2c.close
    
def fixRepeats(i,n,lines):
    with open(filename2, "a") as f2b:
        newtotal=0
        oldA=((lines[i].split(':'))[2])
        oldB=((lines[n].split(':'))[2])
        newTotal=((int(oldB))+(int(oldA)))
        newString=str(str((lines[i].split(':'))[0]) + ":" + str((lines[i].split(':'))[1]) + ":" + str(newTotal) + "\n")
        f2b.writelines( newString )
    f2b.close

    f = open(filename2, "r")
    allFileData = f.readlines()
    f.close()

    f = open(filename2, "w")
    print(lines[i])
    print(allFileData)
    allFileData.remove(lines[i] + "\n")
    allFileData.remove(lines[n] + "\n")
    print(allFileData)

    for c in range(0,len(allFileData)):
        f.write(allFileData[c])
    f.close()


def finalExport():
    toWrite=[]
    with open(filename2, "r+") as f2c:
        lines = [line.rstrip('\n') for line in f2c]
        lengthOfFile=len(lines)
        for i in range(0,lengthOfFile):
            l1=((lines[i].split(':'))[0])

            l1a=((lines[i].split(':'))[1])

            l1b=((lines[i].split(':'))[2])
                
            print(lines)
            print("")
            print(l1)
            print(l1a)
            print(l1b)

            toWrite.append(str(l1) + str(spaceCreator(str(l1),0)) + str(l1a) + str(spaceCreator(str(l1a),0)) + str(l1b) + "\n")
            print(toWrite)
    f2c.close()
    
    f = open(filename2, "w")
    for c in range(0,len(toWrite)):
        f.write(toWrite[c])
    f.close()
    
def numberMultiplier(x,y):
    value = ((float(x))*(float(y)))
    return (value)

def sandwhichTotal():
    ss=sandwhich.get()
    ssize=sandwhichsize.get()
    sq=sandwhichquantity.get()
    rt=0.00
    if (ss == ("Chicken Legend with Cool Mayo")) or (ss == ("Chicken Legend with BBQ Sauce")) or (ss == ("Chicken Legend with Hot and Spicy Mayo")):
        if ssize == "Small":
            rt=rt+(numberMultiplier(3.59,sq))
        elif ssize == "Normal":
            rt=rt+(numberMultiplier(5.09,sq))
        elif ssize == "Large":
            rt=rt+(numberMultiplier(5.49,sq))

    elif ss == ("Chicken Selects 3 pieces"):
        if ssize == "Small":
            rt=rt+(numberMultiplier(3.19,sq))
        elif ssize == "Normal":
            rt=rt+(numberMultiplier(4.59,sq))
        elif ssize == "Large":
            rt=rt+(numberMultiplier(4.99,sq))

    elif ss == ("Chicken Selects 5 pieces"):
        if ssize == "Small":
            rt=rt+(numberMultiplier(4.19,sq))
        elif ssize == "Normal":
            rt=rt+(numberMultiplier(5.59,sq))
        elif ssize == "Large":
            rt=rt+(numberMultiplier(5.99,sq))
            
    elif ss == ("Big Mac"):
        if ssize == "Small":
            rt=rt+(numberMultiplier(2.99,sq))
        elif ssize == "Normal":
            rt=rt+(numberMultiplier(4.49,sq))
        elif ssize == "Large":
            rt=rt+(numberMultiplier(4.89,sq))

    elif ss == ("Quarter Pounder with Cheese"):
        if ssize == "Small":
            rt=rt+(numberMultiplier(2.99,sq))
        elif ssize == "Normal":
            rt=rt+(numberMultiplier(4.49,sq))
        elif ssize == "Large":
            rt=rt+(numberMultiplier(4.89,sq))

    elif ss == ("Filet-O-Fish"):
        if ssize == "Small":
            rt=rt+(numberMultiplier(2.79,sq))
        elif ssize == "Normal":
            rt=rt+(numberMultiplier(4.49,sq))
        elif ssize == "Large":
            rt=rt+(numberMultiplier(4.89,sq))

    elif ss == ("McChicken Sandwich"):
        if ssize == "Small":
            rt=rt+(numberMultiplier(2.99,sq))
        elif ssize == "Normal":
            rt=rt+(numberMultiplier(4.49,sq))
        elif ssize == "Large":
            rt=rt+(numberMultiplier(4.89,sq))

    elif ss == ("Chicken McNuggets 6 pieces"):
        if ssize == "Small":
            rt=rt+(numberMultiplier(2.99,sq))
        elif ssize == "Normal":
            rt=rt+(numberMultiplier(4.49,sq))
        elif ssize == "Large":
            rt=rt+(numberMultiplier(4.89,sq))
            
    elif ss == ("Chicken McNuggets 9 pieces"):
        if ssize == "Small":
            rt=rt+(numberMultiplier(3.19,sq))
        elif ssize == "Normal":
            rt=rt+(numberMultiplier(3.19,sq))
        elif ssize == "Large":
            rt=rt+(numberMultiplier(3.19,sq))
            
    elif ss == ("Chicken McNuggets 20 piece share box"):
        if ssize == "Small":
            rt=rt+(numberMultiplier(5.00,sq))
        elif ssize == "Normal":
            rt=rt+(numberMultiplier(5.00,sq))
        elif ssize == "Large":
            rt=rt+(numberMultiplier(5.00,sq))
            
    elif ss == ("Cheeseburger"):
        if ssize == "Small":
            rt=rt+(numberMultiplier(0.99,sq))
        elif ssize == "Normal":
            rt=rt+(numberMultiplier(0.99,sq))
        elif ssize == "Large":
            rt=rt+(numberMultiplier(0.99,sq))
            
    elif ss == ("Hamburger"):
        if ssize == "Small":
            rt=rt+(numberMultiplier(0.89,sq))
        elif ssize == "Normal":
            rt=rt+(numberMultiplier(0.89,sq))
        elif ssize == "Large":
            rt=rt+(numberMultiplier(0.89,sq))

    return (rt)

def sigTotal():
    rt=0.00
    ss=signature.get()
    sq=signaturequantity.get()
    ssize=signaturesize.get()
    if ss == ("The Classic"):
        if ssize == "Small":
            rt=rt+(numberMultiplier(4.79,sq))
        elif ssize == "Normal":
            rt=rt+(numberMultiplier(6.29,sq))
        elif ssize == "Large":
            rt=rt+(numberMultiplier(6.69,sq))

    elif ss == ("The BBQ"):
        if ssize == "Small":
            rt=rt+(numberMultiplier(4.79,sq))
        elif ssize == "Normal":
            rt=rt+(numberMultiplier(6.29,sq))
        elif ssize == "Large":
            rt=rt+(numberMultiplier(6.69,sq))
    return (rt)

def wrapsTotal():
    rt=0.00
    ss=wrap.get()
    sq=wrapquantity.get()
    ssize=wrapsize.get()
    if ((ss == ("The Sweet Chilli Chicken One")) or (ss == ("The Garlic Mayo Chicken One")) or (ss == ("The Hot Peri Peri Chicken One")) or (ss == ("The BBQ Chicken & Bacon One"))):
        if ssize == "Small":
            rt=rt+(numberMultiplier(2.99,sq))
        elif ssize == "Normal":
            rt=rt+(numberMultiplier(4.59,sq))
        elif ssize == "Large":
            rt=rt+(numberMultiplier(4.99,sq))
    return (rt)

def friesTotal():
    rt=0.00
    ss=fries.get()
    sq=friesquantity.get()
    ssize=friessize.get()
    if ss == ("Fries"):
        if ssize == "Small":
            rt=rt+(numberMultiplier(1.00,sq))
        elif ssize == "Normal":
            rt=rt+(numberMultiplier(1.10,sq))
        elif ssize == "Large":
            rt=rt+(numberMultiplier(1.40,sq))
    return (rt)

def saverMenuTotal():
    rt=0.00
    ss=saver.get()
    sq=saverquantity.get()
    ssize=saversize.get()
    if ss == ("BBQ Chicken Snack Wrap"):
        rt=rt+(numberMultiplier(1.49,sq))
    elif ss == ("Double Cheeseburger"):
        rt=rt+(numberMultiplier(1.49,sq))
    elif ss == ("BBQ Chicken BLC"):
        rt=rt+(numberMultiplier(1.49,sq))            
    elif ss == ("Mayo Chicken"):
        rt=rt+(numberMultiplier(0.99,sq))
    elif ss == ("Cheeseburger"):
        rt=rt+(numberMultiplier(0.99,sq))
    elif ss == ("Shaker Side Salad"):
        rt=rt+(numberMultiplier(1.09,sq))
    elif ss == ("Sundaes Strawberry"):
        rt=rt+(numberMultiplier(0.99,sq))
    elif ss == ("Sundaes Toffee"):
        rt=rt+(numberMultiplier(0.99,sq))
    elif ss == ("McFlurry Various"):
        rt=rt+(numberMultiplier(1.00,sq))
            
    return (rt)
    
def happyMealTotal():
    rt=0.00
    ss=happyMeal.get()
    sq=happyMealquantity.get()
    ssize=happyMealsize.get()
    if ss == ("HM Crispy Chicken Wrap"):
        rt=rt+(numberMultiplier(2.69,sq))
    elif ss == ("HM Cheeseburger"):
        rt=rt+(numberMultiplier(2.69,sq))
    elif ss == ("HM Hamburger"):
        rt=rt+(numberMultiplier(2.69,sq))            
    elif ss == ("HM Chicken McNuggets 4 pieces"):
        rt=rt+(numberMultiplier(2.69,sq))
    elif ss == ("HM Fish Fingers"):
        rt=rt+(numberMultiplier(2.69,sq))
            
    return (rt)

def breakfastTotal():
    rt=0.00
    ss=breakfast.get()
    sq=breakfastquantity.get()
    ssize=breakfastsize.get()
    
    if ss == ("Breakfast Wrap"):
        if ssize == "Individual":
            rt=rt+(numberMultiplier(2.79,sq))
        elif ssize == "Meal Price":
            rt=rt+(numberMultiplier(3.69,sq))
    elif ss == ("Sausage, Egg & Cheese Bagel"):
        if ssize == "Individual":
            rt=rt+(numberMultiplier(2.29,sq))
        elif ssize == "Meal Price":
            rt=rt+(numberMultiplier(3.59,sq))
    elif ss == ("Bacon, Egg & Cheese Bagel"):
        if ssize == "Individual":
            rt=rt+(numberMultiplier(2.29,sq))
        elif ssize == "Meal Price":
            rt=rt+(numberMultiplier(3.59,sq))
    elif ss == ("Double Sausage & Egg McMuffin"):
        if ssize == "Individual":
            rt=rt+(numberMultiplier(2.59,sq))
        elif ssize == "Meal Price":
            rt=rt+(numberMultiplier(3.89,sq))
    elif ss == ("Double Bacon & Egg McMuffin"):
        if ssize == "Individual":
            rt=rt+(numberMultiplier(2.59,sq))
        elif ssize == "Meal Price":
            rt=rt+(numberMultiplier(3.89,sq))
    elif ss == ("Pancakes & Syrup"):
        if ssize == "Individual":
            rt=rt+(numberMultiplier(2.19,sq))
        elif ssize == "Meal Price":
            rt=rt+(numberMultiplier(2.19,sq))
    elif ss == ("Pancakes & Sausage with Syrup"):
        if ssize == "Individual":
            rt=rt+(numberMultiplier(2.59,sq))
        elif ssize == "Meal Price":
            rt=rt+(numberMultiplier(3.49,sq))
    elif ss == ("Sausage & Egg McMuffin"):
        if ssize == "Individual":
            rt=rt+(numberMultiplier(2.19,sq))
        elif ssize == "Meal Price":
            rt=rt+(numberMultiplier(3.49,sq))
    elif ss == ("Bacon & Egg McMuffin"):
        if ssize == "Individual":
            rt=rt+(numberMultiplier(2.19,sq))
        elif ssize == "Meal Price":
            rt=rt+(numberMultiplier(3.49,sq))
    elif ss == ("Egg & Cheese McMuffin"):
        if ssize == "Individual":
            rt=rt+(numberMultiplier(1.69,sq))
        elif ssize == "Meal Price":
            rt=rt+(numberMultiplier(2.99,sq))
    elif ss == ("Bacon Roll"):
        if ssize == "Individual":
            rt=rt+(numberMultiplier(2.19,sq))
        elif ssize == "Meal Price":
            rt=rt+(numberMultiplier(3.49,sq))
    elif ss == ("Quaker Oatso Simple Porridge"):
        if ssize == "Individual":
            rt=rt+(numberMultiplier(0.99,sq))
        elif ssize == "Meal Price":
            rt=rt+(numberMultiplier(0.99,sq))
    elif ss == ("Hash Brown"):
        if ssize == "Individual":
            rt=rt+(numberMultiplier(0.79,sq))
        elif ssize == "Meal Price":
            rt=rt+(numberMultiplier(0.79,sq))
    elif ss == ("Egg & Cheese Snack Wrap"):
        if ssize == "Individual":
            rt=rt+(numberMultiplier(0.99,sq))
        elif ssize == "Meal Price":
            rt=rt+(numberMultiplier(0.99,sq))
    elif ss == ("Sausage & Egg Snack Wrap"):
        if ssize == "Individual":
            rt=rt+(numberMultiplier(1.29,sq))
        elif ssize == "Meal Price":
            rt=rt+(numberMultiplier(1.29,sq))
    elif ss == ("Bacon & Egg Snack Wrap"):
        if ssize == "Individual":
            rt=rt+(numberMultiplier(1.29,sq))
        elif ssize == "Meal Price":
            rt=rt+(numberMultiplier(1.29,sq))

    return (rt)

def desertsTotal():
    rt=0.00
    ss=deserts.get()
    sq=desertsquantity.get()
    ssize=desertssize.get()
    if ss == ("McFlurry"):
        rt=rt+(numberMultiplier(1.00,sq))
    elif ss == ("Hot Apple Pie"):
        rt=rt+(numberMultiplier(1.00,sq))
    elif ss == ("Fruit Bag"):
        rt=rt+(numberMultiplier(0.85,sq))            
    elif ss == ("Ice Cream Cone"):
        rt=rt+(numberMultiplier(1.00,sq))
    elif ss == ("Ice Cream Cone (with Cadbury 99 Flake)"):
        rt=rt+(numberMultiplier(1.00,sq))
    elif ss == ("Toffe Sundae)"):
        rt=rt+(numberMultiplier(0.99,sq))            
    elif ss == ("Strawberry Sundae"):
        rt=rt+(numberMultiplier(0.99,sq))
    elif ss == ("Chocolatey Donut"):
        rt=rt+(numberMultiplier(1.20,sq))
    elif ss == ("Blueberry Muffin"):
        rt=rt+(numberMultiplier(1.20,sq))
    elif ss == ("Chocolate Muffin"):
        rt=rt+(numberMultiplier(1.20,sq))
    elif ss == ("Triple Chocolate Cookie"):
        rt=rt+(numberMultiplier(1.20,sq))
    elif ss == ("Sugar Donut"):
        rt=rt+(numberMultiplier(1.10,sq)) 
    return (rt)    
  
def workOutTotal():
    total = (float(sandwhichTotal()) + float(sigTotal()) + float(wrapsTotal()) + float(friesTotal()) + float(breakfastTotal()) + float(desertsTotal()) + float(happyMealTotal()) + float(saverMenuTotal()))
    totalNumber.config(text=str("%.2f " % total))
    ###Next stage work out wrap total

root = tk.Tk()

defaultWidth=8

backgroundImagePath="./bg.gif"
backgroundImage=tk.PhotoImage(file=backgroundImagePath)
backgroundLabel= tk.Label(root, image=backgroundImage)
backgroundLabel.grid(column=0,row=0,columnspan=15)

lineImagePath="./line.gif"
lineImage=tk.PhotoImage(file=lineImagePath)
lineLabel= tk.Label(root, image=lineImage)
lineLabel.grid(column=0,row=3,columnspan=15)

lineLabel2= tk.Label(root, image=lineImage)
lineLabel2.grid(column=0,row=6,columnspan=15)

lineLabel3= tk.Label(root, image=lineImage)
lineLabel3.grid(column=0,row=8,columnspan=15)

verticalLinePath="./vline.gif"
verticalImage=tk.PhotoImage(file=verticalLinePath)
verticalImageItem= tk.Label(root, image=verticalImage)
verticalImageItem.grid(column=3,row=1,rowspan=6)

verticalImageItem2= tk.Label(root, image=verticalImage)
verticalImageItem2.grid(column=7,row=1,rowspan=6)

verticalImageItem3= tk.Label(root, image=verticalImage)
verticalImageItem3.grid(column=11,row=1,rowspan=6)
#
sandwhichesLabel=tk.Label(root, text="Sandwiches",font = "Calibri 15")
sandwhichesLabel.grid(row=1,column=0,columnspan=3)

sandwhich = tk.StringVar(root)
sandwhich.set("None")
sandwhiches=["None","Chicken Legend with Cool Mayo","Chicken Legend with BBQ Sauce","Chicken Legend with Hot and Spicy Mayo","Chicken Selects 3 pieces","Chicken Selects 5 pieces","Big Mac","Quarter Pounder with Cheese","Filet-O-Fish","McChicken Sandwich","Chicken McNuggets 6 pieces","Chicken McNuggets 9 pieces","Chicken McNuggets 20 piece share box","Cheeseburger","Hamburger"]
sandwhichOptions = tk.OptionMenu(root, sandwhich, *sandwhiches)
sandwhichOptions.grid(row=2,column=0)
sandwhichOptions.config(width=defaultWidth)

sandwhichquantity = tk.StringVar(root)
sandwhichquantity.set("0")
sandwhichquantities=["0","1","2","3","4","5","6","7","8","9","10","11","12","13","14","15","16","17","18","19","20"]
sandwhichquantityOptions = tk.OptionMenu(root, sandwhichquantity, *sandwhichquantities)
sandwhichquantityOptions.grid(row=2,column=1)
sandwhichquantityOptions.config(width=defaultWidth)

sandwhichsize = tk.StringVar(root)
sandwhichsize.set("Normal")
sandwhichsizes=["Normal","Large","Small"]
sandwhichsizeOptions = tk.OptionMenu(root, sandwhichsize, *sandwhichsizes)
sandwhichsizeOptions.grid(row=2,column=2)
sandwhichsizeOptions.config(width=defaultWidth)
#

signatureCollection=tk.Label(root, text="Signature Collection",font = "Calibri 15")
signatureCollection.grid(row=1,column=4,columnspan=3)

signature = tk.StringVar(root)
signature.set("None")
signatures=["None","The Classic","The BBQ","The Spicy"]
signatureOptions = tk.OptionMenu(root, signature, *signatures)
signatureOptions.grid(row=2,column=4)
signatureOptions.config(width=defaultWidth)

signaturequantity = tk.StringVar(root)
signaturequantity.set("0")
signaturequantities=["0","1","2","3","4","5","6","7","8","9","10","11","12","13","14","15","16","17","18","19","20"]
signaturequantityOptions = tk.OptionMenu(root, signaturequantity, *signaturequantities)
signaturequantityOptions.grid(row=2,column=5)
signaturequantityOptions.config(width=defaultWidth)

signaturesize = tk.StringVar(root)
signaturesize.set("Normal")
signaturesizes=["Normal","Large","Small"]
signaturesizeOptions = tk.OptionMenu(root, signaturesize, *signaturesizes)
signaturesizeOptions.grid(row=2,column=6)
signaturesizeOptions.config(width=defaultWidth)
#

wrapsLabel=tk.Label(root, text="Wraps",font = "Calibri 15")
wrapsLabel.grid(row=1,column=8,columnspan=3)

wrap = tk.StringVar(root)
wrap.set("None")
wraps=["None","The Sweet Chilli Chicken One","The Garlic Mayo Chicken One","The Hot Peri Peri Chicken One","The BBQ Chicken & Bacon One"]
wrapOptions = tk.OptionMenu(root, wrap, *wraps)
wrapOptions.grid(row=2,column=8)
wrapOptions.config(width=defaultWidth)

wrapquantity = tk.StringVar(root)
wrapquantity.set("0")
wrapquantities=["0","1","2","3","4","5","6","7","8","9","10","11","12","13","14","15","16","17","18","19","20"]
wrapquantityOptions = tk.OptionMenu(root, wrapquantity, *wrapquantities)
wrapquantityOptions.grid(row=2,column=9)
wrapquantityOptions.config(width=defaultWidth)

wrapsize = tk.StringVar(root)
wrapsize.set("Normal")
wrapsizes=["Normal","Large","Small"]
wrapsizeOptions = tk.OptionMenu(root, wrapsize, *wrapsizes)
wrapsizeOptions.grid(row=2,column=10)
wrapsizeOptions.config(width=defaultWidth)
##
friesLabel=tk.Label(root, text="Fries",font = "Calibri 15")
friesLabel.grid(row=1,column=12,columnspan=3)

fries = tk.StringVar(root)
fries.set("None")
friesYorN=["None","Fries"]
friesOptions = tk.OptionMenu(root, fries, *friesYorN)
friesOptions.grid(row=2,column=12)
friesOptions.config(width=defaultWidth)

friesquantity = tk.StringVar(root)
friesquantity.set("0")
friesquantities=["0","1","2","3","4","5","6","7","8","9","10","11","12","13","14","15","16","17","18","19","20"]
friesquantityOptions = tk.OptionMenu(root, friesquantity, *friesquantities)
friesquantityOptions.grid(row=2,column=13)
friesquantityOptions.config(width=defaultWidth)

friessize = tk.StringVar(root)
friessize.set("Normal")
friessizes=["Normal","Large","Small"]
friessizeOptions = tk.OptionMenu(root, friessize, *friessizes)
friessizeOptions.grid(row=2,column=14)
friessizeOptions.config(width=defaultWidth)#########################################Top Row of things
##

saverLabel=tk.Label(root, text="Saver Menu",font = "Calibri 15")
saverLabel.grid(row=4,column=12,columnspan=3)

saver = tk.StringVar(root)
saver.set("None")
savers=["None","BBQ Chicken Snack Wrap","Double Cheeseburger","BBQ Chicken BLC","Mayo Chicken","Cheeseburger","Shaker Side Salad","Sundaes Strawberry","Sundaes Toffee","McFlurry Various"]
saverOptions = tk.OptionMenu(root, saver, *savers)
saverOptions.grid(row=5,column=12)
saverOptions.config(width=defaultWidth)

saverquantity = tk.StringVar(root)
saverquantity.set("0")
saverquantities=["0","1","2","3","4","5","6","7","8","9","10","11","12","13","14","15","16","17","18","19","20"]
saverquantityOptions = tk.OptionMenu(root, saverquantity, *saverquantities)
saverquantityOptions.grid(row=5,column=13)
saverquantityOptions.config(width=defaultWidth)

saversize = tk.StringVar(root)
saversize.set("Normal")
saversizes=["Normal","Large","Small"]
saversizeOptions = tk.OptionMenu(root, saversize, *saversizes)
saversizeOptions.grid(row=5,column=14)
saversizeOptions.config(width=defaultWidth)
#

happyMealLabel=tk.Label(root, text="Happy Meal",font = "Calibri 15")
happyMealLabel.grid(row=4,column=8,columnspan=3)

happyMeal = tk.StringVar(root)
happyMeal.set("None")
happyMeals=["None","HM Crispy Chicken Wrap","HM Cheeseburger","HM Hamburger","HM Chicken McNuggets 4 pieces","HM Fish Fingers","HM Fruit Bag"]
happyMealOptions = tk.OptionMenu(root, happyMeal, *happyMeals)
happyMealOptions.grid(row=5,column=8)
happyMealOptions.config(width=defaultWidth)

happyMealquantity = tk.StringVar(root)
happyMealquantity.set("0")
happyMealquantities=["0","1","2","3","4","5","6","7","8","9","10","11","12","13","14","15","16","17","18","19","20"]
happyMealquantityOptions = tk.OptionMenu(root, happyMealquantity, *happyMealquantities)
happyMealquantityOptions.grid(row=5,column=9)
happyMealquantityOptions.config(width=defaultWidth)

happyMealsize = tk.StringVar(root)
happyMealsize.set("Normal")
happyMealsizes=["Normal","Large","Small"]
happyMealsizeOptions = tk.OptionMenu(root, happyMealsize, *happyMealsizes)
happyMealsizeOptions.grid(row=5,column=10)
happyMealsizeOptions.config(width=defaultWidth)

##

breakfastLabel=tk.Label(root, text="Breakfast",font = "Calibri 15")
breakfastLabel.grid(row=4,column=0,columnspan=3)

breakfast = tk.StringVar(root)
breakfast.set("None")
breakfasts=["None","Breakfast Wrap","Sausage, Egg & Cheese Bagel","Bacon, Egg & Cheese Bagel","Double Sausage & Egg McMuffin","Double Bacon & Egg McMuffin","Pancakes & Syrup","Pancakes & Sausage with Syrup","Sausage & Egg McMuffin","Bacon & Egg McMuffin","Egg & Cheese McMuffin","Bacon Roll","Quaker Oatso Simple Porridge","Hash Brown","Egg & Cheese Snack Wrap","Sausage & Egg Snack Wrap","Bacon & Egg Snack Wrap"]
breakfastOptions = tk.OptionMenu(root, breakfast, *breakfasts)
breakfastOptions.grid(row=5,column=0)
breakfastOptions.config(width=defaultWidth)

breakfastquantity = tk.StringVar(root)
breakfastquantity.set("0")
breakfastquantities=["0","1","2","3","4","5","6","7","8","9","10","11","12","13","14","15","16","17","18","19","20"]
breakfastquantityOptions = tk.OptionMenu(root, breakfastquantity, *breakfastquantities)
breakfastquantityOptions.grid(row=5,column=1)
breakfastquantityOptions.config(width=defaultWidth)

breakfastsize = tk.StringVar(root)
breakfastsize.set("Individual")
breakfastsizes=["Individual","Meal Price"]
breakfastsizeOptions = tk.OptionMenu(root, breakfastsize, *breakfastsizes)
breakfastsizeOptions.grid(row=5,column=2)
breakfastsizeOptions.config(width=defaultWidth)
#

desertsLabel=tk.Label(root, text="Deserts",font = "Calibri 15")
desertsLabel.grid(row=4,column=4,columnspan=3)

deserts = tk.StringVar(root)
deserts.set("None")
desertss=["None","McFlurry","Hot Apple Pie","Fruit Bag","Ice Cream Cone","Strawberry Sundae","Toffe Sundae","Sugar Donut","Triple Chocolate Cookie","Chocolate Muffin","Blueberry Muffin","Chocolatey Donut"]
desertsOptions = tk.OptionMenu(root, deserts, *desertss)
desertsOptions.grid(row=5,column=4)
desertsOptions.config(width=defaultWidth)

desertsquantity = tk.StringVar(root)
desertsquantity.set("0")
desertsquantities=["0","1","2","3","4","5","6","7","8","9","10","11","12","13","14","15","16","17","18","19","20"]
desertsquantityOptions = tk.OptionMenu(root, desertsquantity, *desertsquantities)
desertsquantityOptions.grid(row=5,column=5)
desertsquantityOptions.config(width=defaultWidth)

desertssize = tk.StringVar(root)
desertssize.set("")
desertssizes=[""]
desertssizeOptions = tk.OptionMenu(root, desertssize, *desertssizes)
desertssizeOptions.grid(row=5,column=6)
desertssizeOptions.config(width=defaultWidth)
##

nameLabel=tk.Label(root, text="Name: ",font = "Calibri 20")
nameLabel.grid(row=7,column=0,columnspan=2)

nameEntryBox = tk.Entry(root)
nameEntryBox.grid(row=7,column=2)

totalLabel=tk.Label(root, text="Total: ",font = "Calibri 20 bold")
totalLabel.grid(row=7,column=4)

totalNumber=tk.Label(root, text=(" 0.0 "),font = "Calibri 20")
totalNumber.grid(row=7,column=5,columnspan=2)

totalbutton = tk.Button(root, text="Click to Work Out Total",font = "Calibri 20", command=workOutTotal)
totalbutton.grid(row=7,column=8,columnspan=3)

addOrderButton = tk.Button(root, text="Click to add final order",font = "Calibri 20", command=addFinalOrder)
addOrderButton.grid(row=7,column=12,columnspan=3)

def generic():
    print("Generic")
    
def exitProgram():
    root.destroy()

rulesForGame2="""About:

All prices were correct at time of writing.
To change prices of individual items please either consult Felix
Please be aware that if you want to change your order, then the "Totals" file will not change.
You must restart the software and re-enter the orders.
To prevent this please make sure that you want to order food before pressing "Add Final Order".
"""

rulesForGame="""How To Use:

Select any item off of the McDonalds menu using the dropdown lists.
Click on "Work Out Total" to check the total of the order before ordering
Please be aware that if you want to change your order, then the "Totals" file will not change.
If you want to order multiple items off of the same drop down menu, then please add the first items to "Final Order", then start another order with the name ( YourName 2 )
Obviously replacing "YourName" with the name on YOUR birth certificate
"""
    
menubar = tk.Menu(root)
filemenu = tk.Menu(menubar, tearoff=0)
filemenu.add_command(label="New", command=resetAllMenus)
filemenu.add_separator()
filemenu.add_command(label="Exit", command=exitProgram)
menubar.add_cascade(label="File", menu=filemenu)

editmenu = tk.Menu(menubar, tearoff=0)
editmenu.add_command(label="Export Final List", command=finalExport)
menubar.add_cascade(label="Final Export", menu=editmenu)


# display the menu
root.config(menu=menubar)
root.title("McDonalds Ordering System")

root.mainloop()
#http://effbot.org/tkinterbook/entry.htm
