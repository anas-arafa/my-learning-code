welcome_message="hello anas welcome to FPT project :"
print(welcome_message)
goals=''
assist=''
v1_wins=''
choice=''
while choice != "3":
    print('what do you want to do? !choice with nembers.\n 1) add \n 2) show \n 3) quit')
    choice=input("your choice => ")
    if choice == "1":
        c1 = input('goals=')
        c2 = input('assist=')
        c3 = input('1v1 wins=')
        goals=goals+c1
        assist=assist+c2
        v1_wins=v1_wins+c3
        continue
    elif choice == "2":
        print('goals='+goals+'  '+'assist='+assist+'  '+'1v1_wins='+v1_wins)
        continue
    else:
        quit()