"""
Maze generator by Luca Zani
https://github.com/ZaniLuca/MazeGenerator
made following TheCodingTrain tutorials
https://www.youtube.com/user/shiffman
"""

import pygame
import random

pygame.init()


class Game:

    def __init__(self):
        self.width = 400
        self.height = 400
        self.w = 50
        self.screen = pygame.display.set_mode((self.width, self.height))
        self.fps = 30
        self.done = False

        pygame.display.set_caption("Maze Generator")

    def run(self):
        clock = pygame.time.Clock()

        run = True
        while run:
            clock.tick(self.fps)

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    run = False
        pygame.quit()

    def update(self):
        pass


g = Game()
g.run()