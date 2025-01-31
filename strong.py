import string
import random
t1=list(string.ascii_uppercase)
t2=list(string.ascii_lowercase)
t3=list(string.punctuation)
t4=list(string.digits)
characters_numbers=int(input("how many characters for the password??"))
while True:
    if characters_numbers <6:
        print("you need at list 6 characters")
        characters_number = input("how many characters for the password ?")
    else:
        break
random.shuffle(t1)
random.shuffle(t2)
random.shuffle(t3)
random.shuffle(t4)
part1=round(30*characters_numbers/100)
part2=round(20*characters_numbers/100)
password=[]
for i in range(part1):
    password.append(t1[i])
    password.append(t2[i])
for x in range(part2):
    password.append(t3[x])
    password.append(t4[x])
random.shuffle(password)
new_pass="".join(password)
print(new_pass)