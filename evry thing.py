import re

# names_ages=[["anas",'omar','sara'],['9','13','15']]
# print(names_ages[0][2]+ ':'+ ' ' + 'the age is' + ' ' +names_ages[1][2])


# import copy
# li1 = [1, 2, [3, 5], 4]
# li2 = copy.copy(li1)
# print("li2 ID: ", id(li2), "Value: ", li2)
# li3 = copy.deepcopy(li1)
# print("li3 ID: ", id(li3), "Value: ", li3)


# languages=[]
# while True:
#     language=input("enter the language\n")
#     language=language.lower()
#     if language == "python":
#         print("good job")
#     if language not in ["python","c++","java","php","html"]:
#         break
#     languages.append(language)
# print(len(languages))


# x=[]
# name=input('enter your name')
# for x in name :
#     print(x)


# family=['anas','omar','sara','tamer']
# familyy=family
# familyy[1]="mom"
# print(family)


# quision=input('enter your name\n')
# quision=quision.lower()
# family={'anas':'2011','omar':'2015','sara':'2009'}
# if quision in family:
#     print(family[quision])
# else:
#     print('you are not from the users')


# family={'anas':'2011',
#         'omar':'2015',
#         'sara':'2009'}
# while True:
#     quision=input('enter your name or press enter to exit\n')
#     if quision == "":
#         break
#     quision=quision.lower()
#     if quision in family:
#         print(family[quision]+' '+'is for'+ ' '+quision+'.')
#     else:
#         print(quision+'is not available you can add it')
#         age=input('please enter your age\n')
#         family[quision]=age
# print(family)


# family={'anas':'2011',
#         'omar':'2015',
#         'sara':'2009'}
# for i in family:
#     print(list(family.keys()))


# print('Hello there!\n How are you?\n I\'m doing fine.')


# name='anas'
# print(name.islower())


# while True:
#     password=input('enter the password\n')
#     if password.isalnum():
#         age=input("enter your age\n")
#         if age.isdecimal():
#             break


# print('PICNIC ITEMS'.center(20,"_"))


# import re
# number=re.compile(r'(\(\d\d\d\))_(\d\d\d_\d\d\d\d)')
# searching=number.search("my phone num is (232)_334_5674.")
# fullnum=searching.groups()
# number_code,main_num=fullnum
# print(number_code+'\n'+main_num)


import re
# from os import PRIO_PGRP
#
# from strong import password

# x=re.compile(r'batman|tina fey')
# y=x.findall('batman and tina fey')
# print(y)


# vuol=re.compile(r'[aeuioAEUIO]')
# X=vuol.findall("add eye FOOD ink UPPER")
# print(X)

password=input("enter your password\n ")
def is_password_strong(password):
    if len(password)>= 8 :
        pattern=re.compile(r'[A-Z]')
        pattern2 = re.compile(r'[a-z]')
        pattern3=re.compile(r'\d')
        capital=pattern.search(password)
        if capital != None:
            small=pattern2.search(password)
            if small != None:
                num=pattern3.search(password)
                if num != None:
                    print("True")
                else:
                    print("false")
            else:
                print("false")
        else:
            print("false")

    else:
        print("false")
