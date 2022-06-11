import random
from . import windowSize

class Apple():
    positionApple_x = random.randint(0,windowSize.x)
    positionApple_y = random.randint(0,windowSize.y)

    def __init__(self) -> None:
        pass

    def updatePositionApple(self) -> None:
        self.positionApple_x = random.randint(0,windowSize.x)
        self.positionApple_y = random.randint(0,windowSize.y)

    def __str__(self) -> str:
        return "apple"