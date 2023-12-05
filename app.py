from utils.ui_helpers import heading, options, dialog
from models.game import Game
from games.bundeslaender import Bundeslaender

def start_game() -> str:
    gamesList = [
        Bundeslaender,
    ]

    heading('Select a game from the list below', '=')
    options(map(lambda g: g.name, gamesList))

    game: Game = None
    while not game:
        selectedGame = dialog('I want to play game with the number')
        
        if selectedGame == 'exit':
            print('Ok, good bye... Come back soon!')
            quit()
        elif selectedGame.isnumeric() and int(selectedGame) > 0 and int(selectedGame) <= len(gamesList):
            game = gamesList[int(selectedGame) - 1]()

        if not game:
            print('Error: wrong index. Try again')
    print()
    game.start()
    print()
    return dialog('Do you want to play more? [Y, n]', 'Y')

while not start_game() == 'n':
    print()
    start_game()
    
print('Good luck! Hope you enjoy playing the games.')
print('(ʘ‿ʘ)╯')