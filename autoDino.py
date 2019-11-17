import keyboard
import time
import numpy as np
from PIL import ImageGrab

x = 150;
x1 = 110;
y = 53;
#i = 1;
while True:
    image = ImageGrab.grab(bbox=(384,338,871,412))
    # image.putpixel((x,y),(255,0,0));
	
    # image.save('D:\\python\\Scripts\\snapshots\\image' + str(i) +'.png');
    # i = i + 1;
	
    iswhite1 = np.all(image.getpixel((x,y)) == (247, 247, 247), axis=-1)
    iswhite2 = np.all(image.getpixel((x1,y)) == (247, 247, 247), axis=-1)
    if iswhite1 == False or iswhite2 == False:
        keyboard.press(' ');


