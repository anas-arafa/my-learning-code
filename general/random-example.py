import random
x=input("enter a 4-digit PIN code:")
com=random.randint(1000,9999)
if len (x)==4 and x==com:
    print ("you win !")
    print(f"the computer generated this PIN :{com}")
elif len(x) != 4:
    print("please enter 4 digit PIN code")
else:
    print ("you loss")
    print(f"the computer generated this PIN :{com}")
