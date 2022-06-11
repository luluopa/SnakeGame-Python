import pytest
from Json import JsonHandle
from snakePython.Exceptions.ExceptionsHandle import JsonNotFoundException

def testJsonHandleFileOpenException():
    with pytest.raises(JsonNotFoundException):
        JsonHandle("settings.json").openJsonFile()