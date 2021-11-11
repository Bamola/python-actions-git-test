import os.path, sys
sys.path.append(os.path.join(os.path.dirname(os.path.realpath(__file__)), os.pardir))
from src.app import index

def test_index():
    assert index()=="Hello, World!"