from project_class1 import main

def test_function1():
    r = main.my_first_func()
    assert r == "Hello world"

def test_function2():
    r = main.my_first_func()
    assert r != "Hello Pakistan"