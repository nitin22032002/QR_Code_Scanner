from cv2 import VideoCapture,destroyAllWindows,waitKey,imshow
import pyzbar.pyzbar as pz
from keyboard import is_pressed
video=VideoCapture(0)
while True:
    status,image=video.read()
    data = pz.decode(image)
    for i in data:
        print(i.data.decode())
    if(data):break
    imshow("Scanner",image)
    waitKey(1)
    if(is_pressed("s")):
        break
video.release()
destroyAllWindows()