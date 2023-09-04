import sys

import pygame

import game
import splash
from globals import *


class Main:
    def __init__(self):
        pygame.init()
        self.screen = pygame.display.set_mode((WIDTH, HEIGHT))
        pygame.display.set_caption(f"Untangle  {VERSION}")
        self.splash_screen = splash.SplashScreen(self.screen)
        self.game = game.Game(self.screen)

        font = pygame.font.SysFont("FreeSans", 100)
        self.title = font.render("Untangle", True, "black")
        self.title_pos = (CENTER_X - self.title.get_width() // 2, 50)
        self.font = pygame.font.SysFont("FreeSans", 30)
        self.level = self.font.render("Select Level", True, "black")
        self.level_pos = (300, 180)
        self.level_boxes = [pygame.rect.Rect((500 + x * 150, 165, 100, 60))
                            for x in range(len(LEVELS_NUMBERS))]

        self.level_num = [self.font.render(f"{x}", True, "black")
                          for x in LEVELS_NUMBERS]
        self.enter_level = self.font.render("Enter Level", True, "black")
        self.input_box = pygame.rect.Rect((350 + self.enter_level.get_width(),
                                           300, 150, 35))

        self.go_box = pygame.rect.Rect((self.input_box.topright[0] + 20,
                                        self.input_box.y - 10, 100, 55))

        self.go_text = self.font.render("GO", True, "black")
        x = self.go_box.centerx - self.go_text.get_width() // 2
        y = self.go_box.centery - self.go_text.get_height() // 2
        self.go_text_pos = x, y
        self.numbers = {pygame.K_0: 0, pygame.K_1: 1, pygame.K_2: 2,
                        pygame.K_3: 3, pygame.K_4: 4, pygame.K_5: 5,
                        pygame.K_6: 6, pygame.K_7: 7, pygame.K_8: 8,
                        pygame.K_9: 9, pygame.K_KP0: 0, pygame.K_KP1: 1,
                        pygame.K_KP2: 2, pygame.K_KP3: 3, pygame.K_KP4: 4,
                        pygame.K_KP5: 5, pygame.K_KP6: 6, pygame.K_KP7: 7,
                        pygame.K_KP8: 8, pygame.K_KP9: 9}
        self.user_input = ""
        self.input_selected = False
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
        self.draw_enter_level()
        pygame.display.flip()

    def draw_enter_level(self):
        self.screen.blit(self.enter_level, (300, 300))
        if self.input_selected:
            color = LIGHT_GREEN
        else:
            color = "white"
        pygame.draw.rect(self.screen, color, self.input_box)
        pygame.draw.rect(self.screen, "green", self.go_box)
        self.screen.blit(self.go_text, self.go_text_pos)
        if self.input_selected:
            text = self.font.render(self.user_input, True, "black")
            cx = self.input_box.x + text.get_width()
            cy = self.input_box.y + 5
            pygame.draw.line(self.screen, "black", (cx, cy), (cx, cy + 25))
            self.screen.blit(text, (self.input_box.x, self.input_box.y + 5))

    def check_for_mouse_click(self):
        mouse = pygame.mouse.get_pressed()
        if mouse[0] is True:
            mouse_x, mouse_y = pygame.mouse.get_pos()
            for i, box in enumerate(self.level_boxes):
                if box.collidepoint((mouse_x, mouse_y)):
                    self.selected_level = LEVELS_NUMBERS[i]
                    self.input_selected = False
                    self.user_input = ""
            if self.input_box.collidepoint(mouse_x, mouse_y):
                self.input_selected = True
            elif self.go_box.collidepoint(mouse_x, mouse_y):
                if self.user_input != "":
                    level = int(self.user_input)
                    if MIN_LEVEL <= level <= MAX_LEVEL:
                        self.selected_level = level
                    else:
                        self.user_input = ""
            else:
                self.input_selected = False
                self.user_input = ""

    def check_for_events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE:
                pygame.quit()
                sys.exit()
            if event.type == pygame.KEYDOWN and event.key in self.numbers:
                if len(self.user_input) < INPUT_LEN:
                    self.user_input += str(self.numbers[event.key])
            if event.type == pygame.KEYDOWN and event.key == pygame.K_BACKSPACE:
                if len(self.user_input) > 0:
                    self.user_input = self.user_input[:-1]

        self.check_for_mouse_click()


def main():
    untangle = Main()
    untangle.run()


if __name__ == "__main__":
    main()
