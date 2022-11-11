
import random

from sys import argv
script, optionvalue , accountname = argv



def genpass ():    
    strminus     = "abcdefghijklmnopqrstuvwxyz"
    strmayus     = strminus.upper()
    strnumbers   = "1234567890"   
    combined     = strminus +strmayus + strnumbers   
    eleminus     = strminus[random.randint(0,24)]
    elemayus     = strmayus[random.randint(0,24)]
    elemnumber   = strnumbers[random.randint(0,9)]    
    passwordgnt  = "" +eleminus+ elemayus+elemnumber
    longpwd      = random.randint(8,16)
    passwordgnt2 = random.sample(combined,longpwd-3) 

    for i in passwordgnt2:
        passwordgnt = passwordgnt + i  
    
    return(passwordgnt)

docname = "pwddoc.txt"

with open(docname) as pwddoc:
        items =pwddoc.readlines()
        pwddoc.close()

def adddata():
    with open("pwddoc.txt", 'w') as temp_file:
        for item in items:
            temp_file.write("%s\n" % item.rstrip())
        
          
    

def addpwd():
    snname = accountname
    lenname = len(snname)
    while lenname<8:
        snname = snname +" "
        lenname = len(snname)
    sw=0
    for x in range(len(items)):
        if (items[x][4:12])== snname:
            pwsgnt = genpass()
            items[x] = items[x][:20].rstrip() +pwsgnt +"\n"
            print("Password generated!")          
            sw=1
            adddata()
            break       
    if sw==0:
        pwsgnt = genpass()
        naccount = "SN: " + snname + ", PWD :"+pwsgnt
        items.insert(0,naccount)
        print("Password generated!")
        adddata()
    
    

def showpwd():
    snname = accountname
    lenname = len(snname)
    while lenname<8:
        snname = snname +" "
        lenname = len(snname)
    sw=0
    for x in range(len(items)):
        if (items[x][4:12])== snname:
            print(items[x].rstrip())          
            sw=1
            break        
    if sw==0:
        print("The account doesnt exist") 
        
    
   
def runp():
    selected_option = int(optionvalue)
    print("--------------------------------------")
    if selected_option==1:
        addpwd()
                    
    elif selected_option==2:
        showpwd()           
    print("--------------------------------------")
   
runp()

