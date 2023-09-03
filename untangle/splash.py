import sys

import pygame

from globals import *


class SplashScreen:
    def __init__(self, screen):
        self.screen = screen
        self.running = True
        font = pygame.font.SysFont("FreeSans", 180)
        self.title = font.render("Untangle", True, "black")
        self.title_pos = (CENTER_X - self.title.get_width() // 2,
                          CENTER_Y - self.title.get_height() // 2)
        font = pygame.font.SysFont("FreeSans", 30)
        self.msg = font.render("Press any key to start", True, "black")
        self.msg_pos = (CENTER_X - self.msg.get_width() // 2, HEIGHT - 250)

    def run(self):
        while self.running:
            self.draw()
            self.check_for_events()

    def draw(self):
        self.screen.fill(LIGHT_GRAY)
        self.screen.blit(self.title, self.title_pos)
        self.screen.blit(self.msg, self.msg_pos)
        pygame.display.flip()

    def check_for_events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE:
                pygame.quit()
                sys.exit()
            if event.type == pygame.KEYDOWN or \
                    event.type == pygame.MOUSEBUTTONDOWN:
                self.running = False
