import pytest
from app.randomwords import WordRandomizer
import re


random_words = WordRandomizer()


def test_randomizer1_method1():
    words = [word for word in random_words]
    assert len(words) == 5, f"Test failed because number of words is {len(words)} and not 5"

def test_randomizer1_method2():
    NUMBER_OF_WORDS = 20
    words = [word for word in random_words(max_words=NUMBER_OF_WORDS)]
    assert len(words) == NUMBER_OF_WORDS, f"Test failed because number of words is {len(words)} and not {NUMBER_OF_WORDS}"

def test_randomizer1_method3():
    regex_match_alphabetical = "^[a-zA-Z]+$"
    words = "".join([word for word in random_words])
    assert re.match(regex_match_alphabetical, words), f"Test failed because string is not alphanumeric"