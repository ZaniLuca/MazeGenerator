#!/usr/local/bin/python3.8

import random

import pygame

# ----- Colors
WHITE = pygame.Color(255, 255, 255)
BLACK = pygame.Color(0, 0, 0)
GREY = pygame.Color(128, 128, 128)
GREEN = pygame.Color(0, 255, 0)
# ----- Constants
WIN_HEIGHT = 400
WIN_WIDTH = 400
W = 40
# ----- PygameInit
pygame.init()
pygame.display.set_caption("Maze Generator")
WIN = pygame.display.set_mode((WIN_WIDTH, WIN_HEIGHT))
# ----- Variables
cols = WIN_WIDTH // W
rows = WIN_HEIGHT // W
grid = []
stack = []


# ----- Cell class
class Cell:
    def __init__(self, i, j):
        self.i = i
        self.j = j
        self.walls = [True, True, True, True]
        self.visited = False

    def show(self):
        x = self.i * W
        y = self.j * W
        if self.walls[0]:
            pygame.draw.line(WIN, BLACK, (x, y), (x + W, y), 2)
        if self.walls[1]:
            pygame.draw.line(WIN, BLACK, (x + W, y), (x + W, y + W), 2)
        if self.walls[2]:
            pygame.draw.line(WIN, BLACK, (x + W, y + W), (x, y + W), 2)
        if self.walls[3]:
            pygame.draw.line(WIN, BLACK, (x, y + W), (x, y), 2)
        if self.visited:
            rect = pygame.Rect(x + 2, y + 2, W - 1, W - 1)
            pygame.draw.rect(WIN, WHITE, rect)

    def checkNeighbors(self):
        neighbors = []

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

    def highlight(self):
        x = self.i * W
        y = self.j * W
        rect = pygame.Rect(x, y, W, W)
        pygame.draw.rect(WIN, GREEN, rect)


# ----- Functions
def makeGrid():
    for j in range(rows):
        for i in range(cols):
            cell = Cell(i, j)
            grid.append(cell)


def index(i, j):
    if i < 0 or j < 0 or i > cols - 1 or j > rows - 1:
        return -1
    return i + j * cols


def removeWalls(a, b):
    x = a.i - b.i
    if x == 1:
        a.walls[3] = False
        b.walls[1] = False
    elif x == -1:
        a.walls[1] = False
        b.walls[3] = False
    y = a.j - b.j
    if y == 1:
        a.walls[0] = False
        b.walls[2] = False
    elif y == -1:
        a.walls[2] = False
        b.walls[0] = False


def cercaIndice(i, j):
    for square in range(len(grid)):
        if grid[square].i == i and grid[square].j == j:
            return square
    return -1


# ----- Main
makeGrid()

current = grid[0]
# ----- GameLoop
clock = pygame.time.Clock()
run = True
while run:

    clock.tick(30)
    # pygame.time.delay(300)
    WIN.fill(WHITE)
    for i in range(len(grid)):
        grid[i].show()

    current.visited = True
    current.highlight()
    next = current.checkNeighbors()
    if next:
        next.visited = True
        removeWalls(current, next)
        stack.append(current)

        current = next
    elif len(stack) > 0:
        current = stack.pop()

    event = pygame.event.wait()
    if event.type == pygame.QUIT:
        run = False
    pygame.display.update()
pygame.quit()
