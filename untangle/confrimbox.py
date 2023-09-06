import sys

import pygame

from globals import *


class ConfirmBox:
    def __init__(self, screen, msg, true_msg="Yes", false_msg="No"):
        self.screen = screen
        font_50 = pygame.font.SysFont("FreeSans", 50)
        box_width = 500
        box_height = 300
        x = CENTER_X - box_width // 2
        y = CENTER_Y - box_height // 2
        self.msg_box = pygame.rect.Rect(x, y, box_width, box_height)
        x = self.msg_box.left + 50
        y = self.msg_box.bottom - 150
        self.true_box = pygame.rect.Rect(x, y, 150, 100)
        x = self.msg_box.right - 200
        y = self.msg_box.bottom - 150
        self.false_box = pygame.rect.Rect(x, y, 150, 100)
        self.message = font_50.render(msg, True, (0, 0, 0))
        self.true_msg = font_50.render(true_msg, True, (0, 0, 0))
        self.false_msg = font_50.render(false_msg, True, (0, 0, 0))
        self.running = True
        self.result = False

    def check_for_events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE:
                self.running = False
                self.result = False
            elif event.type == pygame.MOUSEBUTTONDOWN:
                mouse_x, mouse_y = pygame.mouse.get_pos()
                if self.true_box.collidepoint(mouse_x, mouse_y):
                    self.running = False
                    self.result = True
                elif self.false_box.collidepoint(mouse_x, mouse_y):
                    self.running = False
                    self.result = False

    def draw(self):
        pygame.draw.rect(self.screen, (130, 130, 130), self.msg_box)
        pygame.draw.rect(self.screen, (210, 210, 210), self.true_box)
        pygame.draw.rect(self.screen, (210, 210, 210), self.false_box)
        x = CENTER_X - self.message.get_width() // 2
        self.screen.blit(self.message, (x, CENTER_Y - 100))
        x = self.true_box.centerx - self.true_msg.get_width() // 2
        y = self.true_box.centery - self.true_msg.get_height() // 2
        self.screen.blit(self.true_msg, (x, y))
        x = self.false_box.centerx - self.false_msg.get_width() // 2
        y = self.false_box.centery - self.false_msg.get_height() // 2
        self.screen.blit(self.false_msg, (x, y))
        pygame.display.flip()

    def run(self):
        self.running = True
        pygame.mouse.set_visible(True)
        self.draw()
        while self.running:
            self.check_for_events()
        pygame.mouse.set_visible(False)
        return self.result
