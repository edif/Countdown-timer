import time
import pygame
pygame.mixer.init()
alarm = pygame.mixer.Sound("alarm_ding.ogg")
alarm_len = alarm.get_length()
#____________________________________________________________
print("It will play a sound at the end...\n")
print("Now, we can type the enter key for value 0\n")
#____________________________________________________________
try:
    minutes = int(input ("Minutes:"))*60
except ValueError:   
    minutes = 0*60
try:    
    seconds = int(input("Seconds:"))
except ValueError:
    seconds = 0
timer = minutes + seconds
for i in range(timer):
    print("", str(timer - i), end="\r")
    time.sleep(1)
alarm.play()
print("time's over\n")
#____________________________________________________________________
print("Check and Download this code at https://github.com/edif/Countdown-timer\n")
#____________________________________________________________________
time.sleep(alarm_len)