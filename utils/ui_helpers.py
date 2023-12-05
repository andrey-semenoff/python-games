def heading(text: str, decor: str = None) -> None:
    if decor:
        print(str(decor) * len(text))
    print(text)
    if decor:
        print(str(decor) * len(text))

def options(texts: [str]) -> None:
    stringFull = ''
    for idx, text in enumerate(texts):
        stringFull += '{}. {}\n'.format(idx + 1, text)
    print(stringFull + '\n')

def dialog(text: str, defaultInput: str = None) -> str:
    userInput = input('> {}: '.format(text))
    if userInput == '' and defaultInput:
        return defaultInput
    return userInput