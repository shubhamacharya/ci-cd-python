from src.main import add

def test_add_function():
    assert add(5,5) == 10
    assert add(0,0) == 0
    