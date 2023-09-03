import sys

import pygame

import game
import splash
from globals import *


class Main:
    def __init__(self):
        pygame.init()
        self.screen = pygame.display.set_mode((WIDTH, HEIGHT))
        pygame.display.set_caption(f"Untangle  Version: {VERSION}")
        self.splash_screen = splash.SplashScreen(self.screen)
        self.game = game.Game(self.screen)

        font = pygame.font.SysFont("FreeSans", 100)
        self.title = font.render("Untangle", True, "black")
        self.title_pos = (CENTER_X - self.title.get_width() // 2, 50)
        font = pygame.font.SysFont("FreeSans", 30)
        self.level = font.render("Select Level", True, "black")
        self.level_pos = (300, 180)
        self.level_boxes = [pygame.rect.Rect((500 + x * 150, 165, 100, 60))
                            for x in range(len(LEVELS_NUMBERS))]

        self.level_num = [font.render(f"{x}", True, "black")
                          for x in LEVELS_NUMBERS]

        self.selected_level = None
        self.running = True

    def run(self):
        self.splash_screen.run()
        pygame.mouse.set_pos((CENTER_X, CENTER_Y))
        while self.running:
            self.draw()
            self.check_for_events()
            if self.selected_level is not None:
                pygame.mouse.set_pos((CENTER_X, CENTER_Y))
                self.game.new_game(self.selected_level)
                self.selected_level = None

    def draw(self):
        self.screen.fill(LIGHT_GRAY)
        self.screen.blit(self.title, self.title_pos)
        self.screen.blit(self.level, self.level_pos)
        for i, box in enumerate(self.level_boxes):
            pygame.draw.rect(self.screen, "gray", box)
            num = self.level_num[i]
            x = box.centerx - num.get_width() // 2
            y = box.centery - num.get_height() // 2
            self.screen.blit(num, (x, y))
        pygame.display.flip()

    def check_for_level_click(self):
        mouse = pygame.mouse.get_pressed()
        if mouse[0] is True:
            mouse_x, mouse_y = pygame.mouse.get_pos()
            for i, box in enumerate(self.level_boxes):
                if box.collidepoint((mouse_x, mouse_y)):
                    self.selected_level = LEVELS_NUMBERS[i]

    def check_for_events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE:
                pygame.quit()
                sys.exit()
        self.check_for_level_click()


def main():
    untangle = Main()
    untangle.run()


if __name__ == "__main__":
    main()
