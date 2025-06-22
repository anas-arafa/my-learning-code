import qrcode
data=input(" enter a link or a text")
img= qrcode.make(data)
file_name=input("enter a file name")
img.save(file_name)
open(file_name)