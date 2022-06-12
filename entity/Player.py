from typing import Any
import pygame
from pygame.locals import *

from entity.Snake import Snake

dictChoicesDirection = {
    pygame.K_UP:"UP",
    pygame.K_DOWN:"DOWN",
    pygame.K_LEFT:"LEFT",
    pygame.K_RIGHT:"RIGHT"
}

class Player():
    keyPressed = None
    previousKey = None

    def getKeyPressed(self) -> None:
        self.keyPressed = pygame.key.get_pressed()

    def getNewDirection(self):
        if self.keyPressed[pygame.K_UP]:
            return "UP"
        elif self.keyPressed[pygame.K_DOWN]:
            return "DOWN"
        elif self.keyPressed[pygame.K_LEFT]:
            return "LEFT"
        elif self.keyPressed[pygame.K_RIGHT]:
            return "RIGHT"

    def callSnakeDirection(self, snake: Snake, newDirection: str) -> None:
        snake.changeDirection(newDirection)
                    
    def updateEventKey(self, snake: Snake):
        self.getKeyPressed()
        newDirection = self.getNewDirection()
        if newDirection:
            self.callSnakeDirection(snake, newDirection)