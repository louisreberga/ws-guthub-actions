"This module aim to run some unit test"

def inc(x):
    """"Add 1 to the input parameter
    
    Keyword arguments:
    x -- the element we want to add 1
    """
    return x + 1


def test_answer():
    """ Run a unit test of the inc function """
    assert inc(4) == 5
