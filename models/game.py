from time import sleep

class Game:
    name: str
    path = __file__

    def start(self) -> None:
        pass

    def intro(self) -> None:
        for i in range(100):
            print('>', end='', flush=True)
            sleep(0.05)
        print('\n')

    def getMaxScore(self) -> int:
        pass
