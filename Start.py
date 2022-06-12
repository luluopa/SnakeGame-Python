import pygame
from pygame.locals import *
from Window import Window
from entity.Apple import Apple
from entity.Player import Player
from entity.Snake import Snake
from surfaces.AppleSurface import AppleSurface
from surfaces.SnakeSurface import SnakeSurface

RUNNING = True

def main():
    pygame.init()
    window = Window()

    snake = Snake()
    snakeSurface = SnakeSurface()

    apple = Apple()
    appleSurface = AppleSurface()

    player = Player()
    time = pygame.time.Clock()

    while RUNNING:
        time.tick(15)
        window.checkingToClose()

        window.screen.fill((0,0,0))

        player.updateEventKey(snake)

        window.plotSnake(snakeSurface.snakeSurface, snake)
        window.plotSurface(appleSurface.appleSurface, apple.getTupleAppleLocation())

        snake.checkHit(apple)
        snake.updateSnake()
        snake.ifOutsideOfWindow()

        if snake.checkIfLose():
            break

        pygame.display.update()

if __name__ == '__main__':
    main()