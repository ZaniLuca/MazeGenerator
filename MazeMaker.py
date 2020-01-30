"""
Maze generator by Luca Zani
https://github.com/ZaniLuca/MazeGenerator
made following TheCodingTrain tutorials
https://www.youtube.com/user/shiffman
"""

import pygame
from Cell import *
import random

pygame.init()


class Game:

    def __init__(self):
        self.width = 400
        self.height = 400
        self.w = 50
        self.screen = pygame.display.set_mode((self.width, self.height))
        self.fps = 30
        self.grid = [[None for i in range(self.width // self.w)] for j in
                     range(self.height // self.w)]
        self.stack = []
        self.done = False

        pygame.display.set_caption("Maze Generator")

    def run(self):
        """
        Game loop
        :return: None
        """
        clock = pygame.time.Clock()
        self.createGrid()
        current = self.grid[0][0]

        run = True
        while run:
            clock.tick(self.fps)

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    run = False
            self.update()
        pygame.quit()

    def update(self):
        """
        updates the screen
        draw everything
        :return: None
        """
        self.screen.fill(white)
        for i in range(self.width // self.w):
            for j in range(self.height // self.w):
                self.grid[i][j].show(self.screen, self.w)
        pygame.display.flip()

    def createGrid(self):
        """
        create the grid
        :return: None
        """

        for i in range(self.width // self.w):  # Cols
            for j in range(self.height // self.w):  # Rows
                self.grid[i][j] = Cell(i, j)


g = Game()
g.run()
