import qrcode
from random import randint
from tkinter.filedialog import askopenfilename
path=askopenfilename()
with open(path,"rb") as f:
    data=f.read()
qr=qrcode.make(data)
qr.save(f"qrcode_{randint(0,1000000)}.png")
