import random
min_num=1
max_num=6
while True:
    num=random.randint(min_num,max_num)
    print("dice rolling")
    print("the value is")
    print(num)
    roll_again=input("roll the dice again??")
    if roll_again=="no":
        break

