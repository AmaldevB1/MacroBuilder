# -*- coding: utf-8 -*-
"""
Created on Sat Mar 16 01:02:07 2024

@author: ASUS
"""
from pynput.keyboard import Key, Listener,Controller
import yaml


buffer = ""
dic ={"po":"police","k8":"kubernetes"}

with open('macros.yaml', 'r') as stream:
    try:
        dic = yaml.safe_load(stream)
        #print(dic)
    except yaml.YAMLError as e:
        print(e)

res = max(dic.keys(), key = len)
maxLen = len(res)
keyboard = Controller()
alive=True

def compareMacro():
    global buffer,dic
    # if len(buffer)>3 and buffer[-3:]=="qqq":
    #     print('detected')ppp
    #print(buffer)
    if len(buffer)==maxLen and dic.get(buffer[-maxLen:])!=None:
        print('detected ')
        keyboard.press(Key.backspace)
        keyboard.release(Key.backspace)
        keyboard.press(Key.backspace)
        keyboard.release(Key.backspace)

        keyboard.type(dic.get(buffer[-maxLen:]))
        
        
def on_press(key):
    global buffer
    try:
        #print('alphanumeric key {0} pressed'.format(key.char))
        if(len(buffer)==maxLen and key.char!=None):
            buffer= buffer[1:]+key.char
        elif key.char!=None:
            buffer=buffer+key.char
    except AttributeError:
        buffer=buffer

def on_release(key):
    #print('{0} released'.format(key))
    global alive
    if key == Key.esc:
        alive=False
        return False
    elif key == Key.ctrl_l:
        compareMacro()
    
    
listener = Listener(on_press=on_press, on_release=on_release)
listener.start()
while alive:
    i=0
    