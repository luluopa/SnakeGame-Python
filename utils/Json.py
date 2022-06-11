import json
from snakePython.Exceptions.ExceptionsHandle import JsonNotFoundException

class JsonHandle():
    self.file = None
    self.data = dict()

    def __init__(self, jsonName: str) -> None:
        self.jsonName = jsonName

    def openJsonFile(self) -> None:
        try:
            self.file = open(self.jsonName)
        except JsonNotFoundException:
            raise JsonNotFoundException()

    def closeJsonFile(self) -> None:
        if not self.file == None:
            self.file.close()

    def readData(self) -> None:
        self.openJsonFile()
        self.data = json.load(self.file)

    def getData(self) -> dict:
        return self.data