import pygame
import random
from colors import *


class Cell:

    def __init__(self, i, j):
        """
        :param i: col
        :param j: row
        """
        self.i = i
        self.j = j
        self.walls = [True, True, True, True]
        self.visited = False

    def show(self, screen, w):
        """
        Shows the walls around the cell
        :param screen: screen
        :param w: int
        :return: None
        """
        x = self.i * w
        y = self.j * w
        if self.walls[0]:
            pygame.draw.line(screen, black, (x, y), (x + w, y), 2)
        if self.walls[1]:
            pygame.draw.line(screen, black, (x + w, y), (x + w, y + w), 2)
        if self.walls[2]:
            pygame.draw.line(screen, black, (x + w, y + w), (x, y + w), 2)
        if self.walls[3]:
            pygame.draw.line(screen, black, (x, y + w), (x, y), 2)
        if self.visited:
            rect = pygame.Rect(x + 2, y + 2, w - 1, w - 1)
            pygame.draw.rect(screen, white, rect)

    def checkNeighbors(self, grid):
        """
        check every neighbor around the selected cell
        and return a random one
        :param grid: grid
        :return: random index
        """
        neighbors = []
        # TODO get search index function from 1024.py
        top = grid[cercaIndice(self.i, self.j - 1)]
        right = grid[cercaIndice(self.i + 1, self.j)]
        bottom = grid[cercaIndice(self.i, self.j + 1)]
        left = grid[cercaIndice(self.i - 1, self.j)]

        if top and not top.visited:
            neighbors.append(top)
        if right and not right.visited:
            neighbors.append(right)
        if bottom and not bottom.visited:
            neighbors.append(bottom)
        if left and not left.visited:
            neighbors.append(left)
        if len(neighbors) > 0:
            r = int(random.randrange(0, len(neighbors)))
            return neighbors[r]
        else:
            return None

    def highlight(self, screen, w):
        """
        highlight the position
        :param screen: screen
        :param w: int
        :return: None
        """
        x = self.i * w
        y = self.j * w
        rect = pygame.Rect(x, y, w, w)
        pygame.draw.rect(screen, green, rect)
