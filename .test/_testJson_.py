import pytest
from Json import JsonHandle
from snakePython.exceptions.ExceptionsHandle import JsonNotFoundException

def testJsonHandleFileOpenException():
    with pytest.raises(JsonNotFoundException):
        JsonHandle("settings.json").openJsonFile()