from os import listdir
import pygame
import random

sounds_dir = "./sounds"


def play_random_sound():
    global sounds_dir
    try:
        files = [f for f in listdir(sounds_dir) if f.endswith(".wav")]
        random.randint(1, 10)
        f = "%s/%s" % (sounds_dir, files[random.randint(0, len(files) - 1)])
        pygame.mixer.init()
        pygame.mixer.music.load(f)
        pygame.mixer.music.play()
        while pygame.mixer.music.get_busy():
            continue
    except:
        pass


play_random_sound()
