#!C:/Users/ejste/AppData/Local/Microsoft/WindowsApps/python3.9.exe

import os

os.environ["FAV_ANIMAL"] = input('What is your favorite animal?')
os.environ["HOME_STATE"] = input('What is your home state?')
os.environ["AREA_CODE"] = input('What is your area code?')

FAV_ANIMAL = os.getenv("FAV_ANIMAL")
HOME_STATE = os.getenv("HOME_STATE")
AREA_CODE = os.getenv("AREA_CODE")

print("FAV_ANIMAL: ",FAV_ANIMAL,"\nHOME_STATE: ",HOME_STATE,"\n AREA_CODE: ",AREA_CODE)
