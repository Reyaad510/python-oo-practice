"""Word Finder: finds random words from a dictionary."""
import random

class WordFinder:
    ...
    """A class to find random words from a dictionary file."""

    def __init__(self, file_path):
        """Initialize the WordFinder instance with a file path.
        
        Args:
            file_path (str): The path to the file containing words.
        """
        self.file_path = file_path
        self.words = self.read_words_from_file()
        self.num_words = len(self.words)
        print(f"{self.num_words} words read")
    
    def read_words_from_file(self):
        """Read words from the file and return them as a list."""
        with open(self.file_path, 'r') as file:
            return [line.strip() for line in file]

    def random(self):
        """Return a random word from the list of words."""
        return random.choice(self.words)






random_word = WordFinder("words.txt")
print(random_word.random())



class SpecialWordFinder(WordFinder):
    """A subclass of WordFinder that handles special cases such as comments and blank lines."""
    
    def read_words_from_file(self):
        """Read words from the file, ignoring comments and blank lines."""
        with open(self.file_path, 'r') as file:
            return [line.strip() for line in file if line.strip() and not line.startswith('#')]



special_word = SpecialWordFinder("words.txt")
print(special_word.random())