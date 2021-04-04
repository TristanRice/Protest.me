from english_words import english_words_lower_alpha_set as english_words_set
from random import choice as random_choice

class WordRandomizer:
    """
    Class to create an iterator containing a number of random words
    Usage:
    >>> r = WordRandomizer()
    >>> for word in r:
    >>>     print(word)
    Will be used to create randomized IDs that look pretty (like Twitch has):
    https://clips.twitch.tv/JoyousDeterminedQuailBuddhaBar
    (I'm nEw AnD cOoL)
    I created a class for this because I don't want to have a function load all
    of the english words each time that I want to get random words. Instead, the
    words are loaded once in app/__init__.py, and then choose a number of random
    words each time that I want a random ID (which isn't very costly)
    """
    def __init__(self):
        self.words = self._create_wordlist()

    def _create_wordlist(self):
        return list(english_words_set)

    def __iter__(self, max_words=5):
        return (random_choice(self.words) for _ in range(max_words))
    
    def __call__(self, max_words):
        """
        The user can specify the number of words they want by using this function.
        If they jsut want the defualt number of words (5) then they can iterate
        through the object like they would normally. However, if they want more / less
        words then they can call the object, which will set the max number of words, and
        then return the iterator:
        >>> r = WordRandomizer()
        >>> for word in r(max_words=10):
        >>>     print(word)
        """
        return self.__iter__(max_words=max_words)