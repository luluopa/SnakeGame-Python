import pygame
from pygame.locals import *
from entity.Snake import Snake

from utils.Json import JsonHandle

DATA_JSON = JsonHandle('settings.json').getData()

class Window():

    def __init__(self) -> None:
        self.screen = self.initScreen()
        self.screen.fill(eval(DATA_JSON['colors']['red']))
        self.setName(DATA_JSON['windowName'])
        pass

    def initScreen(self) -> None:
        return pygame.display.set_mode((DATA_JSON['windowSize'][0],DATA_JSON['windowSize'][1]))

    def setName(self, name: str) -> None:
        pygame.display.set_caption(name)

    def checkingToClose(self) -> None:
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
    
    def plotSurface(self, surface: pygame.Surface, location: tuple) -> None:
        self.screen.blit(surface, location)

    def plotSnake(self, surface: pygame.Surface, snake: Snake) -> None:
        for location in snake.snakeBody:
            self.plotSurface(surface, (location[0],location[1]))