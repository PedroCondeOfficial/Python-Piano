"""
        Made by Pedro E. Conde
                v1.0.0
              10/07/2019
"""
# Imports pygame and playsound libraries to set up window and playback functions
from playsound import playsound
import pygame, sys
import pygame.locals

# Creates class called Piano
class Piano():
    # Initializing function to prepare program window
    def __init__(self):
        pygame.init()
        bg = pygame.image.load('piano.jpg')
        BLACK = (0,0,0)
        HEIGHT = 167
        WIDTH = 200
        w = pygame.display.set_mode((WIDTH, HEIGHT), 0, 0)
        pygame.mixer.init()
        i = 0

        while True:
            w.blit(bg, (0, 0))
            # Gets key press events and plays the appropriate key and displays a blip of the pressed key
            for event in pygame.event.get():
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_a:
                        pygame.mixer.music.load('C.wav')
                        pygame.mixer.music.play()
                        font = pygame.font.Font(None, 36)
                        text = font.render('C', 1, (255, 0, 0))
                        w.blit(text, (5, 145) )
                    elif event.key == pygame.K_w:
                        pygame.mixer.music.load('C#.wav')
                        pygame.mixer.music.play()
                        font = pygame.font.Font(None, 36)
                        text = font.render('C#', 1, (255, 0, 0))
                        w.blit(text, (10, 90))
                    elif event.key == pygame.K_s:
                        pygame.mixer.music.load('D.wav')
                        pygame.mixer.music.play()
                        font = pygame.font.Font(None, 36)
                        text = font.render('D', 1, (255, 0, 0))
                        w.blit(text, (30, 145))
                    elif event.key == pygame.K_e:
                        pygame.mixer.music.load('Eb.wav')
                        pygame.mixer.music.play()
                        font = pygame.font.Font(None, 36)
                        text = font.render('Eb', 1, (255, 0, 0))
                        w.blit(text, (50, 90))
                    elif event.key == pygame.K_d:
                        pygame.mixer.music.load('E.wav')
                        pygame.mixer.music.play()
                        font = pygame.font.Font(None, 36)
                        text = font.render('E', 1, (255, 0, 0))
                        w.blit(text, (60, 145))
                    elif event.key == pygame.K_f:
                        pygame.mixer.music.load('F.wav')
                        pygame.mixer.music.play()
                        font = pygame.font.Font(None, 36)
                        text = font.render('F', 1, (255, 0, 0))
                        w.blit(text, (95, 145))
                    elif event.key == pygame.K_t:
                        pygame.mixer.music.load('F#.wav')
                        pygame.mixer.music.play()
                        font = pygame.font.Font(None, 36)
                        text = font.render('F#', 1, (255, 0, 0))
                        w.blit(text, (100, 90))
                    elif event.key == pygame.K_g:
                        pygame.mixer.music.load('G.wav')
                        pygame.mixer.music.play()
                        font = pygame.font.Font(None, 36)
                        text = font.render('G', 1, (255, 0, 0))
                        w.blit(text, (120, 145))
                    elif event.key == pygame.K_y:
                        pygame.mixer.music.load('G#.wav')
                        pygame.mixer.music.play()
                        font = pygame.font.Font(None, 36)
                        text = font.render('G#', 1, (255, 0, 0))
                        w.blit(text, (135, 90))
                    elif event.key == pygame.K_h:
                        pygame.mixer.music.load('A.wav')
                        pygame.mixer.music.play()
                        font = pygame.font.Font(None, 36)
                        text = font.render('A', 1, (255, 0, 0))
                        w.blit(text, (145, 145))
                    elif event.key == pygame.K_u:
                        pygame.mixer.music.load('Bb.wav')
                        pygame.mixer.music.play()
                        font = pygame.font.Font(None, 36)
                        text = font.render('Bb', 1, (255, 0, 0))
                        w.blit(text, (160, 90))
                    elif event.key == pygame.K_j:
                        pygame.mixer.music.load('B.wav')
                        pygame.mixer.music.play()
                        font = pygame.font.Font(None, 36)
                        text = font.render('B', 1, (255, 0, 0))
                        w.blit(text, (180, 145))
                    # Creates quit function
                    elif event.key == pygame.K_ESCAPE:
                        self.i += 1
                    # Prevents other key events from triggering playback
                    else:
                        print("Not a valid key")
            pygame.display.update()
# Calls the Piano class
piano = Piano()
