import pygame

pygame.mixer.init()


def play_audio(file_path):
    pygame.mixer.music.load(file_path)
    pygame.mixer.music.play()


def stop_audio():
    pygame.mixer.music.stop()


def is_playing():
    return pygame.mixer.music.get_busy()