from dog import Dog
import pytest

def test_age_is_valid_range():
    '''validates age property is an integer between 0 and 20'''
    dog = Dog("Buddy", "Beagle", 5)
    assert dog.age == 5

    with pytest.raises(ValueError):
        dog.age = -1  # too low

    with pytest.raises(ValueError):
        dog.age = 21  # too high

    with pytest.raises(ValueError):
        dog.age = "five"  # not an integer
