from typing import List
import requests
import json
from time import sleep
from functools import reduce
from models.game import Game
from models.question import Question
from utils.ui_helpers import dialog

class Bundeslaender(Game):
    name = 'Bundesländer'
    questions: List[Question] = []

    def __init__(self) -> None:
        pass
        res = requests.get('https://raw.githubusercontent.com/andrey-semenoff/db-for-python-games/main/db.json')
        data = res.json()
        self.questions.clear()
        for q in data['questions']:
            self.questions.append(Question(q['text'], q['answer'], q['score']))

    def start(self) -> None:
        self.intro()
        score: int = 0
        for q in self.questions:
            score += q.run()
        self.showResults(score)
        
    def intro(self) -> None:
        lineLength = 75
        for i in range(lineLength):
            print('>', end='', flush=True)
            sleep(0.05)
        print('''
▒█▀▀█ ▒█░▒█ ▒█▄░▒█ ▒█▀▀▄ ▒█▀▀▀ ▒█▀▀▀█ ▒█░░░ ░█▀▀█ ▒█▄░▒█ ▒█▀▀▄ ▒█▀▀▀ ▒█▀▀█
▒█▀▀▄ ▒█░▒█ ▒█▒█▒█ ▒█░▒█ ▒█▀▀▀ ░▀▀▀▄▄ ▒█░░░ ▒█▄▄█ ▒█▒█▒█ ▒█░▒█ ▒█▀▀▀ ▒█▄▄▀
▒█▄▄█ ░▀▄▄▀ ▒█░░▀█ ▒█▄▄▀ ▒█▄▄▄ ▒█▄▄▄█ ▒█▄▄█ ▒█░▒█ ▒█░░▀█ ▒█▄▄▀ ▒█▄▄▄ ▒█░▒█''')
        print('>' * lineLength)
        print()
    
    def getMaxScore(self) -> int:
        return reduce(lambda sum, q: sum + q.score, self.questions, 0)
    
    def showResults(self, score: int) -> None:
        lineLength = 75
        maxScore = self.getMaxScore()
        percentage = score / maxScore

        print('-' * lineLength)
        print('Your result is: {} of {} ({}%).'.format(score, maxScore, round(percentage * 100)))

        if percentage == 0:
            print('It\'s too bad...')
        elif percentage < 0.5:
            print('Not bad, but could be better')
        elif percentage < 0.85:
            print('Good, you made not too much mistakes')
        elif percentage < 1:
            print('Cool, you know almost everything')
        else:
            print('Amazing! You\'ve made no mistakes!')

        print('-' * lineLength)
    

