from typing import List
from utils.ui_helpers import dialog
import random

class Question:
    phrasesCorrect: List[str] = ['Correct!', 'Right!', 'Amazing!', 'Good!']
    phrasesFalsch: List[str] = ['Mistake...', 'Falsy...', 'Wrong answer...', 'No...']
    def __init__(self, text: str, answer: str, score: int):
        self.text = text
        self.answer = answer
        self.score = score
    
    def run(self) -> int:        
        answer = dialog('{} [{}]'.format(self.text, self.score))
        if answer == 'quit':
            print('Ok, good bye... Come back soon!')
            quit()
        elif self.answer == answer:
            print(random.choice(self.phrasesCorrect))
            return self.score
        print(random.choice(self.phrasesFalsch))
        return 0
