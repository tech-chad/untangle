import math
import random

import pygame

import dot_presets
from globals import *


class Dots:
    def __init__(self, game):
        self.game = game
        self.number_of_dots = game.level
        self.dot_list = self.setup_dots()
        self.backup_dot_list = self.make_backup()
        self.clicked = None
        self.movement = False

    def draw(self):
        for dot in self.dot_list:
            dot.draw_lines()
        for dot in self.dot_list:
            dot.draw()
        if self.clicked is not None:
            for dot in self.clicked.connections:
                dot.draw_connected()
            for dot in self.clicked.sec_connections:
                dot.draw_connected()
            self.clicked.draw_clicked()

    def update(self):
        mouse = pygame.mouse.get_pressed()
        if mouse[0] is True:
            self.movement = True
            mouse_x, mouse_y = pygame.mouse.get_pos()
            if self.clicked is None:
                for dot in self.dot_list:
                    if dot.check_if_clicked(mouse_x, mouse_y):
                        self.clicked = dot
                        dot.update(mouse_x, mouse_y)
                        break
            if self.clicked is not None:
                self.clicked.update(mouse_x, mouse_y)

        elif mouse[0] is False and self.clicked is not None:
            self.clicked.clicked = False
            self.clicked = None

    def make_backup(self):
        backup_list = []
        for dot in self.dot_list:
            backup_list.append((dot.x, dot.y))
        return backup_list

    def reset_dots(self):
        for i, dot in enumerate(self.dot_list):
            x, y = self.backup_dot_list[i]
            dot.x = x
            dot.y = y

    def setup_dots(self):
        dot_list = []
        if self.number_of_dots <= 9:
            wide = 3
        elif self.number_of_dots <= 25:
            wide = 4
        else:
            wide = 10
        if self.number_of_dots <= 25:
            preset = dot_presets.patterns[self.number_of_dots]
        else:
            preset = self.auto_set_dots()
        for i, cell in enumerate(preset):
            y = i // wide * 80 + 20
            x = i % wide * 80 + 20
            dot = Dot(self.game.screen, x, y)
            dot_list.append(dot)
        for i, dot in enumerate(dot_list):
            cell = preset[i]
            connections = cell[0]
            sec_connections = cell[1]
            for conn in connections:
                cx, cy = conn
                num = cy * wide + cx
                dot.add_connection(dot_list[num])
            for conn in sec_connections:
                cx, cy = conn
                num = cy * wide + cx
                dot.add_sec_connection(dot_list[num])
        start_points = self.get_points()
        print(len(start_points))
        for dot in dot_list:
            coord = random.choice(start_points)
            start_points.pop(start_points.index(coord))
            dot.update(coord[0], coord[1])
        return dot_list

    def auto_set_dots(self):
        dot_list = dot_presets.base_dots
        for new_dot in range(10, self.number_of_dots):
            dot_list.append([[], []])
            new_x = new_dot % 10
            new_y = new_dot // 10
            # which connections set to use
            if new_dot % 10 == 0:  # first dot in the row
                x = new_x + 1
                y = new_y - 1
                dot_list[new_dot][0].append([x, y])
                dot_list[new_dot - 9][1].append([new_x, new_y])
                x = new_x
                y = new_y - 1
                dot_list[new_dot][0].append([x, y])
                dot_list[new_dot - 10][1].append([new_x, new_y])
            elif new_dot % 10 == 9:  # last dot in the row
                x = new_x - 1
                y = new_y - 1
                dot_list[new_dot][0].append([x, y])
                dot_list[new_dot - 11][1].append([new_x, new_y])
                x = new_x
                y = new_y - 1
                dot_list[new_dot][0].append([x, y])
                dot_list[new_dot - 10][1].append([new_x, new_y])
                x = new_x - 1
                y = new_y
                dot_list[new_dot][0].append([x, y])
                dot_list[new_dot - 1][1].append([new_x, new_y])
            elif new_dot % 2 == 0:  # even dot
                # x = new_x + 1
                # y = new_y - 1
                # dot_list[new_dot][0].append([x, y])
                # dot_list[new_dot - 9][1].append([new_x, new_y])
                x = new_x
                y = new_y - 1
                dot_list[new_dot][0].append([x, y])
                dot_list[new_dot - 10][1].append([new_x, new_y])
                x = new_x - 1
                y = new_y
                dot_list[new_dot][0].append([x, y])
                dot_list[new_dot - 1][1].append([new_x, new_y])
            elif new_dot % 2 == 1:  # odd dot
                x = new_x + 1
                y = new_y - 1
                dot_list[new_dot][0].append([x, y])
                dot_list[new_dot - 9][1].append([new_x, new_y])
                x = new_x
                y = new_y - 1
                dot_list[new_dot][0].append([x, y])
                dot_list[new_dot - 10][1].append([new_x, new_y])
                x = new_x - 1
                y = new_y
                dot_list[new_dot][0].append([x, y])
                dot_list[new_dot - 1][1].append([new_x, new_y])
        return dot_list

    def get_points(self):
        start_list = []
        degree = 360 // self.number_of_dots
        for i in range(self.number_of_dots):
            x = CENTER_X + PLACEMENT_RADIUS * math.sin(math.radians(i * degree))
            y = CENTER_Y + PLACEMENT_RADIUS * math.cos(math.radians(i * degree))
            start_list.append((x, y))
        return start_list

    def untangled(self):
        for dot in self.dot_list:
            connections = dot.connections
            for conn in connections:
                for find_dot in self.dot_list:
                    if dot == find_dot:
                        continue
                    if conn == find_dot:
                        continue
                    find_connections = find_dot.connections
                    for find_conn in find_connections:
                        if dot == find_conn:
                            continue
                        if conn == find_conn:
                            continue
                        if self.do_intersect(dot, conn, find_dot, find_conn):
                            return False
        return True

    @classmethod
    def orientation(cls, p, q, r):
        val = (float(q.y - p.y) * (r.x - q.x)) - \
              (float(q.x - p.x) * (r.y - q.y))
        if val > 0:
            # Clockwise orientation
            return 1
        elif val < 0:
            # Counterclockwise orientation
            return 2
        else:
            # Collinear orientation
            return 0

    @classmethod
    def on_segment(cls, p, q, r):
        if ((q.x <= max(p.x, r.x)) and (q.x >= min(p.x, r.x)) and
                (q.y <= max(p.y, r.y)) and (q.y >= min(p.y, r.y))):
            return True
        return False

    @classmethod
    def do_intersect(cls, p1, q1, p2, q2):
        o1 = cls.orientation(p1, q1, p2)
        o2 = cls.orientation(p1, q1, q2)
        o3 = cls.orientation(p2, q2, p1)
        o4 = cls.orientation(p2, q2, q1)

        # General case
        if (o1 != o2) and (o3 != o4):
            return True

        # p1 , q1 and p2 are collinear and p2 lies on segment p1q1
        if (o1 == 0) and cls.on_segment(p1, p2, q1):
            return True

        # p1 , q1 and q2 are collinear and q2 lies on segment p1q1
        if (o2 == 0) and cls.on_segment(p1, q2, q1):
            return True

        # p2 , q2 and p1 are collinear and p1 lies on segment p2q2
        if (o3 == 0) and cls.on_segment(p2, p1, q2):
            return True

        # p2 , q2 and q1 are collinear and q1 lies on segment p2q2
        if (o4 == 0) and cls.on_segment(p2, q1, q2):
            return True
        return False


class Dot:
    def __init__(self, screen, x, y):
        self.screen = screen
        self.x = x
        self.y = y
        self.radius = DOT_RADIUS
        self.connections = []
        self.sec_connections = []
        self.clicked = False
        self.circle = None

    def update(self, x, y):
        self.x = x
        self.y = y

    def check_if_clicked(self, x, y):
        if self.circle.collidepoint(x, y):
            self.clicked = True
            return True
        else:
            self.clicked = False
            return False

    def draw(self):
        if self.clicked is False:
            loc = (self.x, self.y)
            color = "blue"
            self.circle = pygame.draw.circle(
                self.screen,
                color,
                (self.x, self.y),
                self.radius)
            pygame.draw.circle(self.screen, "black", loc, self.radius, 1)

    def draw_clicked(self):
        loc = (self.x, self.y)
        self.circle = pygame.draw.circle(self.screen, "green", loc, self.radius)
        pygame.draw.circle(self.screen, "black", loc, self.radius, 1)

    def draw_connected(self):
        loc = (self.x, self.y)
        self.circle = pygame.draw.circle(self.screen, "red", loc, self.radius)
        pygame.draw.circle(self.screen, "black", loc, self.radius, 1)

    def draw_lines(self):
        for dot in self.connections:
            x = dot.x
            y = dot.y
            pygame.draw.line(self.screen, "black", (self.x, self.y), (x, y))

    def add_connection(self, dot):
        self.connections.append(dot)

    def add_sec_connection(self, dot):
        self.sec_connections.append(dot)
