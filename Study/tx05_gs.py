from gtts import gTTS
import sys
import time
import pygame
import RPi.GPIO as GPIO  
from time import sleep
from random import *


pygame.mixer.init()
pygame.mixer.music.load("Donny.wav")
pygame.mixer.music.play()
clock = pygame.time.Clock()

while pygame.mixer.music.get_busy():
    clock.tick(30)
pygame.mixer.quit()
