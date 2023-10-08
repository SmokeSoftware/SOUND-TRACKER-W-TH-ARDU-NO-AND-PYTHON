import serial
import pydirectinput
from ctypes import cast, POINTER
from comtypes import CLSCTX_ALL
from pycaw.pycaw import AudioUtilities, IAudioEndpointVolume
import tkinter as tk
from tkinter import*
import time

arduino = serial.Serial('COM4',9600,timeout = 5) # edit this part your port adress

APP = tk.Tk()
APP.title("ARDUİNO SOUND ADJUNMENT")
APP.minsize(400,200)
APP.maxsize(400,200)

def get_volume():
    devices = AudioUtilities.GetSpeakers()
    interface = devices.Activate(
        IAudioEndpointVolume._iid_, CLSCTX_ALL, None)
    volume = cast(interface, POINTER(IAudioEndpointVolume))
    return volume.GetMasterVolumeLevelScalar()

def set_volume(volume_level):
    devices = AudioUtilities.GetSpeakers()
    interface = devices.Activate(
        IAudioEndpointVolume._iid_, CLSCTX_ALL, None)
    volume = cast(interface, POINTER(IAudioEndpointVolume))
    volume.SetMasterVolumeLevelScalar(volume_level, None)


BOOL = False

def ACTİVATE_PROGRAM():
    global BOOL
    BOOL = True
    START_APP_BUTTON["text"] = "ACTİVATED"
    START_APP_BUTTON["state"] = DISABLED
    APP_İNFO["font"] = "Arial 30"
    while BOOL:
        analog_value = arduino.readline().decode('utf-8').strip()

        DDATA = int(analog_value)
        DDATA /= 100

        set_volume(DDATA)
        #print("Instant Sound Level: (%)",int(DDATA*100))

        data = arduino.readline().decode('utf-8').strip()
        APP_İNFO.config(text="Sound Level: " + data)
        APP.update()


def boolfalse(event):
    global BOOL
    BOOL = False
    START_APP_BUTTON["text"] = "ACTİVATE PROGRAM"
    START_APP_BUTTON["state"] = NORMAL
    APP_İNFO["font"] = "Arial 20"
    APP_İNFO["text"] = "PLEASE ACTİVE\n THE PROGRAM"

APP_İNFO = tk.Label(APP,text = "PLEASE ACTİVE\n THE PROGRAM",fg = "blue",bg = "white",font = "Arial 20")
APP_İNFO.place(width = 400,height = 100,x = 0,y = 0)

APP.bind("<Key>", boolfalse)


START_APP_BUTTON = tk.Button(APP,text = "ACTİVATE PROGRAM",fg = "lime",bg = "black",font = "Arial 27",activebackground = "lime",activeforeground = "black",command = ACTİVATE_PROGRAM)
START_APP_BUTTON.place(width = 400,height = 100,x = 0,y = 100)

APP.mainloop()
    






