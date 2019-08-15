import time
import pygame
pygame.mixer.init()
alarm = pygame.mixer.Sound("alarm_ding.ogg")
alarm_len = alarm.get_length()
minutes = int(input ("Minutes:"))*60
seconds = int(input("Seconds:"))
timer = minutes + seconds
for i in range(timer):
    print("", str(timer - i), end="\r")
    time.sleep(1)
alarm.play()
print("time's over")
time.sleep(alarm_len)