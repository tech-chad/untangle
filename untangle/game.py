import sys

import pygame

import dot

from globals import *


class Game:
    def __init__(self, screen):
        self.screen = screen
        self.level = 0
        self.running = True
        self.dots = None
        font_60 = pygame.font.SysFont("FreeSans", 130)
        self.winner_string = font_60.render("COMPLETED", True, "Purple")

    def new_game(self, level_number):
        self.level = level_number
        self.dots = dot.Dots(self)
        self.running = True
        self.run()

    def run(self):
        self.draw()
        while self.running:
            self.update()
            self.draw()
            if self.dots.movement and self.dots.clicked is None:
                if self.dots.untangled():
                    self.running = False
                    self.display_winner()
                    continue
            self.check_for_events()

    def draw(self):
        self.screen.fill(LIGHT_GRAY)
        self.dots.draw()
        pygame.display.flip()

    def update(self):
        self.dots.update()

    def display_winner(self):
        x = CENTER_X - self.winner_string.get_width() // 2
        y = CENTER_Y - self.winner_string.get_height() // 2
        self.screen.blit(self.winner_string, (x, y))
        pygame.display.flip()
        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                if event.type == pygame.KEYDOWN or \
                        event.type == pygame.MOUSEBUTTONDOWN:
                    return

    def check_for_events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE:
                self.running = False
