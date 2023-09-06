import sys

import pygame

import confrimbox
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
        self.quit_level = confrimbox.ConfirmBox(screen, "Quit the level?")
        self.quit_game = confrimbox.ConfirmBox(screen, "Quit the game?")
        self.reset_level = confrimbox.ConfirmBox(screen, "Reset level?")

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
                if self.quit_game.run():
                    pygame.quit()
                    sys.exit()
            if event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE:
                if self.quit_level.run():
                    self.running = False
            elif event.type == pygame.KEYDOWN and event.key == pygame.K_r:
                if self.reset_level.run():
                    self.dots.reset_dots()
                    pygame.mouse.set_visible(True)
