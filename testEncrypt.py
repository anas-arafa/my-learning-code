import string
key = 19
x1 = input("E")
start = ord('a')
charIndex = string.ascii_lowercase.index(x1)
y1 = chr(((charIndex +key)%26 )+start)
print(y1)

charIndex = string.ascii_lowercase.index(y1)
y2 = chr(((charIndex -key)%26 )+start)
# x2 = y1
# y2 =chr(int((ord(x2) / 2) - 5) % 256)
print(y2)