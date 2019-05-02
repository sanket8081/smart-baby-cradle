import pygame
import time
#import RPi.GPIO as GPIO

#GPIO SETUP
"""channelm = 21
pir=26
GPIO.setmode(GPIO.BCM)
GPIO.setup(channelm, GPIO.IN)
GPIO.setup(pir,GPIO.IN)
time.sleep(2)

#moisture detection
def moist():
    moisture=LOW
    if GPIO.input(channelm) :
                print ("no Water Detected!")
                moisture=LOW
    else:
                print ("Water detected!")
                moisture=HIGH"""

#musicplaying
def musicplay():
    pygame.mixer.init()
    pygame.mixer.music.load("music.wav")
    pygame.mixer.music.play()
    while pygame.mixer.music.get_busy() == True:
        continue

"""def presence():
    if GPIO.input(pir):
        baby="present"
    else:
        baby="absent""""



while True:
    count=0
    #check bed wet
    #moist()

    #temp var for moisture testing
    moisture="HIGH"
    current=input()
    if current=="cry":
        musicplay()
        time.sleep(5)
    """else:
        #check presence
        presence()

        if baby=="present":
            #baby is present
            continue
        elif baby=="absent":
            #baby is not present
            print("msg to mother that the baby is not present")
            exit()"""



    current=input()
    if current=="cry":
        #cradle swing
        #musicplay()
        while(count<3):
            print("swinggggggg swingggggggg")
            count+=1

    current=input()
    if current=="cry":
        #gsm module code
        if moisture=="HIGH":
            print("msg to mother----baby is crying due to bed wet please change the mattress")
        else:
            print("msg to mother----baby is crying need attenttion")



    continue

"""GPIO.add_event_detectm(channelm, GPIO.BOTH, bouncetime=300)  # let us know when the pin goes HIGH or LOW
GPIO.add_event_callbackm(channelm, callback)  # assign function to GPIO PIN, Run function on change"""
