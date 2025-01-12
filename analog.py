import cv2
import numpy as np

from constant import REDIUS,CENTER,CANVAS,COLORS

import helperfuntion as hf

image = np.full(CANVAS,255,dtype=np.uint8)

inti , dest = hf.get_tikits()

for i in range(len(inti)):
    if i%5 == 0:
        cv2.line(image,dest[i],inti[i],COLORS['black'],3) # to calculate hours point
    else:
        cv2.circle(image,dest[i],5,COLORS['black'],-1)# to calculate minitis

cv2.circle(image,CENTER,REDIUS+10,COLORS['yellow'],2)

cv2.circle(image,CENTER,4,COLORS['red'],-1)# a point to the center of the clock



# show the image until 'Esc' is pressed
while True:
    img = image.copy()
    
    clock_face = hf.get_line(img)
    
    cv2.imshow('test',clock_face)
    if(cv2.waitKey(1)==27):
        break
    
cv2.destroyAllWindows()# destroing all windows
    
    
