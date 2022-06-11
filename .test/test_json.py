import sys,os
from pathlib import Path

#importing path of exceptions module
BASE_DIR = Path(__file__).resolve().parent.parent
EXCEPTIONS_DIR = os.path.join(BASE_DIR, 'exceptions')
JSON_DIR = os.path.join(BASE_DIR, 'utils')

sys.path.append(EXCEPTIONS_DIR)
sys.path.append(JSON_DIR)

import pytest
from Json import JsonHandle
from ExceptionsHandle import JsonNotFoundException

def testJsonHandleOpenFile():
    file = JsonHandle(os.path.join(BASE_DIR, 'settings.json')).getData()
    assert not file == None

def testJsonHandleFileOpenException():
    with pytest.raises(JsonNotFoundException):
        JsonHandle("notfound.json").getData()