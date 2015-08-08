import pygame.mixer

pygame.mixer.init()

z = pygame.mixer.Sound("x.wav")

while True:
    z.play()
