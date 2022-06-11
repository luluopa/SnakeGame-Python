import sys, os
from pathlib import Path

#importing path of exceptions module
BASE_DIR = Path(__file__).resolve().parent.parent
EXCEPTIONS_DIR = os.path.join(BASE_DIR, 'exceptions')
sys.path.append(EXCEPTIONS_DIR)

import json
from ExceptionsHandle import JsonNotFoundException

class JsonHandle():
    file = None
    data = dict()

    def __init__(self, jsonName: str) -> None:
        self.jsonName = jsonName

        self.readData()

    def openJsonFile(self) -> None:
        try:
            self.file = open(self.jsonName)
        except:
            raise JsonNotFoundException()

    def closeJsonFile(self) -> None:
        if not self.file == None:
            self.file.close()

    def readData(self) -> None:
        self.openJsonFile()
        self.data = json.load(self.file)
        self.closeJsonFile()

    def getData(self) -> dict:
        return self.data