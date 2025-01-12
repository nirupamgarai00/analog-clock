#sudo install openCV module usign pip
import cv2
import math
import datetime

# importing everything from constant.py
from constant import REDIUS
from constant import CENTER
from constant import COLORS
from constant import CANVAS


def get_tikits():# a function for calculating point of tiks 
    arr_inti= []
    arr_dest= []
    
    # this is the loop for storing the destination point for tiks
    for i in range(0,360,6):
        x_dest = CENTER[0] + REDIUS*math.sin(i*(math.pi/180))#calculating x coordinate
        y_dest = CENTER[1]+ REDIUS*math.cos(i*(math.pi/180))#calculating y coordinate
        
        arr_dest.append((int(x_dest),int(y_dest)))
    
    # this is the loop for storing the intial point for tiks
    for i in range(0,360,6):
        x_inti = CENTER[0] + (REDIUS-30)*math.sin(i*(math.pi/180))#calculating x coordinate
        y_inti = CENTER[1]+ (REDIUS-30)*math.cos(i*(math.pi/180))#calculating y coordinate
        
        arr_inti.append((int(x_inti),int(y_inti)))
    
    return arr_inti,arr_dest

# geting the time in realtime
def get_time():
    dt= datetime.datetime.now()
    
    h = dt.hour
    if h>12:
        h = h-12
        
    m = dt.minute
    s= dt.second
    return h,m,s


#use to calculate the clock line
def get_line(image):
    secend_line = REDIUS-35# len of secend clock
    min_line = REDIUS-60# len of minitis clock
    hour_line = REDIUS-80 # len of hour clock
    
    h,m,s= get_time()# feching the time from get_time
    
    #calculating the coordinates of secend clock for this particular time
    x_secend = int(CENTER[0]+secend_line*math.cos((s*6+270)*math.pi/180))
    y_secend = int(CENTER[1]+secend_line*math.sin((s*6+270)*math.pi/180))
    cv2.line(image,CENTER,(x_secend,y_secend),COLORS['blue'],3,cv2.LINE_AA)
    
    #calculating the coordinates of minites clock for this particular time
    x_min = int(CENTER[0]+min_line*math.cos((m*6+270)*math.pi/180))
    y_min = int(CENTER[1]+min_line*math.sin((m*6+270)*math.pi/180))
    cv2.line(image,CENTER,(x_min,y_min),COLORS['green'],3,cv2.LINE_AA)
    
    #calculating the coordinates of hour clock for this particular time
    x_hour = int(CENTER[0]+hour_line*math.cos((h*30+270)*math.pi/180))
    y_hour = int(CENTER[1]+hour_line*math.sin((h*30+270)*math.pi/180))
    cv2.line(image,CENTER,(x_hour,y_hour),COLORS['green'],3,cv2.LINE_AA)
    
    return image # returning the image
    
    

    
