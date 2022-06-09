import pygame


def music():
    pygame.init()
    pygame.mixer.music.load('./music/Overpass.mp3')
    pygame.mixer.music.play()
    input('parar musica')