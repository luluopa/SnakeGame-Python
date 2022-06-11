import sys, os
from pathlib import Path

#importing path of utils module
BASE_DIR = Path(__file__).resolve().parent.parent
UTILS_DIR = os.path.join(BASE_DIR, 'utils')
sys.path.append(UTILS_DIR)

from Json import JsonHandle

JSON_DIR = os.path.join(BASE_DIR, 'settings.json')
pixelTam = JsonHandle(JSON_DIR).getData()['pixelSize']

def upChoice(x,y) -> list:
    return list([x,y+pixelTam])

def downChoice(x,y) -> list:
    return list([x,y-pixelTam])

def rightChoice(x,y) -> list:
    return list([x+pixelTam,y])

def leftChoice(x,y) -> list:
    return list([x-pixelTam,y])

dictChoicesDirection = {
    "UP":upChoice,
    "DOWN":downChoice,
    "RIGHT":rightChoice,
    "LEFT":leftChoice
}

class Snake():
    #default values
    positionSnake_x = 50
    positionSnake_y = 50

    snakeInitialTam = 3
    direction = 'UP'

    snakeBody = list([[positionSnake_x, positionSnake_y],
                    [positionSnake_x, positionSnake_y - pixelTam],
                    [positionSnake_x, positionSnake_y - pixelTam*2]])

    def changeDirection(self, newDirection) -> None:
        self.direction = newDirection

    def updateHead(self) -> None:
        self.snakeBody[0] = dictChoicesDirection[self.direction](self.snakeBody[0][0], self.snakeBody[0][1])
 
    def updateBody(self) -> None:
        for snakepart in reversed(range(len(self.snakeBody)-1)):
            self.snakeBody[snakepart] = [self.snakeBody[snakepart+1][0], self.snakeBody[snakepart+1][1]]

    def updateSnake(self) -> None:
        self.updateHead()
        self.updateBody()

    def snakeEaten(self):
        self.snakeBody.append([0,0])