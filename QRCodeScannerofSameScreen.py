import pyzbar.pyzbar as pz
from tkinter.filedialog import askopenfilename
from PIL import Image,ImageGrab
def getData(img):
    data=pz.decode(img)
    for i in data:
        print(i.data.decode())
path=askopenfilename()
img1=ImageGrab.grab()
try:
    img2=Image.open(path)
    getData(img2)
except Exception as e:
    pass
getData(img1)
