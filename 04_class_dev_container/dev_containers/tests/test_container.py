from dev_containers import main

def test_function1():
    r = main.index()
    assert r != "Hello World"

def test_function2():
    r = main.piaic()
    assert r != "organiztion Piaic"