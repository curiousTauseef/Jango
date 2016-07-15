import pygame
import time

f = open('.Jango_temp.txt','r')
check = f.readline()
f.close()

pygame.init()
pygame.mixer.music.load(check)
pygame.mixer.music.play()

while True:
   time.sleep(1)
