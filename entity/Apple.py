import random
import sys, os
from pathlib import Path

from . import Snake

#importing path of exceptions module
BASE_DIR = Path(__file__).resolve().parent.parent
JSON_DIR = os.path.join(BASE_DIR, 'utils')
sys.path.append(JSON_DIR)

from Json import JsonHandle
DATA_JSON = JsonHandle(os.path.join(BASE_DIR, 'settings.json')).getData()

class Apple():
    positionApple_x = int(random.randint(0,DATA_JSON['windowSize'][0])/DATA_JSON['pixelSize']) * DATA_JSON['pixelSize']
    positionApple_y = int(random.randint(0,DATA_JSON['windowSize'][1])/DATA_JSON['pixelSize']) * DATA_JSON['pixelSize']

    def __init__(self) -> None:
        print(int(random.randint(0,DATA_JSON['windowSize'][0])/DATA_JSON['pixelSize']) * DATA_JSON['pixelSize'])
        pass

    def updatePositionApple(self, snake: Snake) -> None:
        self.positionApple_x = int(random.randint(0,DATA_JSON['windowSize'][0])/DATA_JSON['pixelSize']) * DATA_JSON['pixelSize']
        self.positionApple_y = int(random.randint(0,DATA_JSON['windowSize'][1])/DATA_JSON['pixelSize']) * DATA_JSON['pixelSize']

        for snakepart in snake.snakeBody:
                if [self.positionApple_x, self.positionApple_y] == snakepart:
                    self.updatePositionApple(snake)

    def getTupleAppleLocation(self):
        return tuple((self.positionApple_x, self.positionApple_y))

    def getPositions(self) -> list:
        return [self.positionApple_x, self.positionApple_y]
