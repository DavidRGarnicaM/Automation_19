import random
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
print( f"Password: {passwordgnt} ")