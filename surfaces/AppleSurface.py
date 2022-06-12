import sys, os
from pathlib import Path

#importing path of exceptions module
BASE_DIR = Path(__file__).resolve().parent.parent
JSON_DIR = os.path.join(BASE_DIR, 'exceptions')
sys.path.append(JSON_DIR)

from Json import JsonHandle
import pygame
from pygame.locals import *

DATA_JSON = JsonHandle(os.path.join(BASE_DIR, 'settings.json')).getData()

class AppleSurface():
    appleSurface = pygame.Surface(tuple((DATA_JSON['pixelSize'],DATA_JSON['pixelSize'])))

    def __init__(self) -> None:
        self.surfaceFill()

    def surfaceFill(self) -> None:
        self.appleSurface.fill(eval(DATA_JSON['colors']['white']))