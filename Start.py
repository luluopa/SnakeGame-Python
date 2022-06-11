import pygame
from pygame.locals import *
from Window import Window
from entity.Snake import Snake
from surfaces.SnakeSurface import SnakeSurface

RUNNING = True

def main():
    pygame.init()
    window = Window()

    snake = Snake()
    snakeSurface = SnakeSurface()
    time = pygame.time.Clock()

    sufaceteste = pygame.Surface((10,10))
    sufaceteste.fill((255,0,0))

    while RUNNING:
        time.tick(60)
        window.checkingToClose()

        window.screen.fill((0,0,0))

        for position in snake.snakeBody:
            window.plotSurface(snakeSurface.snakeSurface, (position[0],position[1]))

        window.plotSurface(sufaceteste, (20,20))

        snake.updateSnake()

        pygame.display.update()

if __name__ == '__main__':
    main()