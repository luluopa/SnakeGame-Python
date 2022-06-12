import sys, os, random
from pathlib import Path

#importing path of utils module
BASE_DIR = Path(__file__).resolve().parent.parent
UTILS_DIR = os.path.join(BASE_DIR, 'utils')
sys.path.append(UTILS_DIR)

from Json import JsonHandle
from . import Apple

JSON_DIR = os.path.join(BASE_DIR, 'settings.json')
pixelTam = JsonHandle(JSON_DIR).getData()['pixelSize']
DATA_JSON = JsonHandle(os.path.join(BASE_DIR, 'settings.json')).getData()

def upChoice(x,y) -> list:
    return list([x,y-pixelTam])

def downChoice(x,y) -> list:
    return list([x,y+pixelTam])

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
    positionSnake_x = int(random.randint(0,DATA_JSON['windowSize'][0])/DATA_JSON['pixelSize']) * DATA_JSON['pixelSize']
    positionSnake_y = int(random.randint(0,DATA_JSON['windowSize'][0])/DATA_JSON['pixelSize']) * DATA_JSON['pixelSize']

    direction = 'DOWN'

    snakeBody = list([[positionSnake_x, positionSnake_y],
                    [positionSnake_x, positionSnake_y - pixelTam],
                    [positionSnake_x, positionSnake_y - pixelTam*2]])

    def changeDirection(self, newDirection) -> None:
        if self.direction == 'UP' and not newDirection == 'DOWN':
            self.direction = newDirection
        elif self.direction == 'DOWN' and not newDirection == 'UP':
            self.direction = newDirection
        elif self.direction == 'LEFT' and not newDirection == 'RIGHT':
            self.direction = newDirection
        elif self.direction == 'RIGHT' and not newDirection == 'LEFT':
            self.direction = newDirection

    def updateHead(self) -> None:
        self.snakeBody[0] = dictChoicesDirection[self.direction](self.snakeBody[0][0], self.snakeBody[0][1])
 
    def updateBody(self) -> None:
        for snakepart in reversed(range(len(self.snakeBody))):
            #3 -> (3) -> (0,1,2) -> (2,1)
            if not snakepart == 0:
                self.snakeBody[snakepart] = [self.snakeBody[snakepart-1][0], self.snakeBody[snakepart-1][1]]

    def updateSnake(self) -> None:
        self.updateBody()
        self.updateHead()

    def snakeEaten(self) -> None:
        self.snakeBody.append([0,0])

    def checkHit(self, apple: Apple) -> None:
        if apple.getPositions() == self.snakeBody[0]:
            self.snakeEaten()
            apple.updatePositionApple(self)

    def checkIfLose(self) -> bool:
        for snakepart in range(len(self.snakeBody)):
            if not snakepart == 0:
                if self.snakeBody[0] == self.snakeBody[snakepart]:
                    return True
        return False

    def ifOutsideOfWindow(self) -> None:
        if self.snakeBody[0][0] > DATA_JSON['windowSize'][0]:
            self.snakeBody[0][0] = 0
        elif self.snakeBody[0][0] < 0:
            self.snakeBody[0][0] = DATA_JSON['windowSize'][0]
        elif self.snakeBody[0][1] > DATA_JSON['windowSize'][1]:
            self.snakeBody[0][1] = 0
        elif self.snakeBody[0][1] < 0:
            self.snakeBody[0][1] = DATA_JSON['windowSize'][1]