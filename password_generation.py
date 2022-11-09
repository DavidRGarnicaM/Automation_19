import random

def genpass ():
    # MAIN CHAIN 
    minus = "abcdefghijklmnopqrstuvwxyz"
    mayus = minus.upper()
    numbers = "1234567890"
    # COMBINED CHAIN
    combined = minus +mayus + numbers 
    # POPUP A RANDOM ELEMENT 
    elemnumber =  random.randint(0,9)
    elemnumber = numbers[elemnumber]
    eleminus  =  random.randint(0,24)
    eleminus = minus[eleminus]
    elemayus  =  random.randint(0,24)
    elemayus = mayus[elemayus]
    # ASIGNING LONG TO THE PSW
    long = random.randint(8,16)
    # ADD THE THREE RULES 
    passwordgnt = "" +eleminus+ elemayus+elemnumber 
    # GENERATION A COMPLEMENTARY CHAIN
    passwordgnt2 = random.sample(combined,long-3)
    # ASINGING ALL THE REST OF CHARACTERS
    for i in passwordgnt2:
        passwordgnt = passwordgnt + i 
    # SHOWING THE PSW GENERATED 
    return(passwordgnt)


## VERRSION2  
sML = {"Facebook":"","Twiter":"","Github":""}

def smread():
    smkey =   input("Social Media?")
    pwsgnt = genpass()
    sML[smkey] = pwsgnt
    print("Password Generated!!")
    print("************************************************")
def smshow():
    smkey =   input("Social Media?")
    print("************************************************")
    if smkey == "ALL":
        print(sML)

    elif smkey in sML:
        print(f"Social Media: {smkey}",f"\nPassword:     {sML[smkey]}")
    else: 
        print("The Social Media doesnt exist.  Please try again")
        smread()
    
        

def runf():
    selected_option =0
    print("************************************************")
    while  selected_option != 3:
        print("1 GENERATE PWS")
        print("2 SHOW  PWS")
        print("3 EXIT ")
        print("************************************************")
        selected_option = int(input("Write an option:"))
        print("************************************************")
        if(selected_option ==1):
            smread()
        if(selected_option ==2 ):
            smshow()
            print("************************************************")            
        if(selected_option ==3 ):
            break
      

runf()

