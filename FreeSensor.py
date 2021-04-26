# -*- coding: utf-8 -*-
"""
Created on Sun Apr 25 19:52:38 2021

@author: Eliu
"""

#pip install keyboard

import keyboard
from time import sleep

def free_fire(cx, cy, w):
    res_x = 640
    res_y = 480
    time_release = 0.1
    sleep(0.001)
    
    no_move = w/3 #Divisor hace efecto en la sensibilidad
    if cx>(res_x/2)+no_move and cx !=0:
        print("IZQUIERDA")
        keyboard.press('a')
        #sleep(time_release)
        keyboard.press_and_release('d')
    

        
    elif cx<(res_x/2)-no_move:
        print("DERECHA")
        keyboard.press('d')
        #sleep(time_release)
        keyboard.press_and_release('a')
        
    else:
        print('CENTER')
        keyboard.press_and_release('d')
        keyboard.press_and_release('a')

    '''        
    keyboard.press('w')
    sleep(1)
    keyboard.press_and_release('w')
    '''



import cv2

face_cascade = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')
cap = cv2.VideoCapture(0) #My camer 640x480

while True:
    _, img = cap.read()
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    faces = face_cascade.detectMultiScale(gray, 1.1,4)
    for (x,y,w,h) in faces:
        cv2.rectangle(img, (x,y), (x+w, y+h), (255,0,0), 2)
        cx = x+(w/2)
        cy = y+(h/2)
        free_fire(cx, cy, w)
        print(str(cx)+'    '+str(cy))
    cv2.imshow('img', img)
    k = cv2.waitKey(30)
    if k == 27:
        break
cap.release()
        
