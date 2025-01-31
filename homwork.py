def sum(num1,num2):
    return num1+num2
def sub(num1,num2):
    return num1-num2
def times(num1,num2):
    return num1*num2
def divisin(num1,num2):
    return num1/num2

x=input("the first number")
z=input("the sign")
y=input("the second number")

if z=="+":
    print(sum(int(x),int(y)))
elif z=="-":
    print(sub(int(x),int(y)))
elif z=="*":
    print(times(int(x),int(y)))
elif z=="/":
    print(divisin(int(x),int(y)))










