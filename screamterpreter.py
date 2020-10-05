import os, sys

def getch():
    try:
        import msvcrt
        return msvcrt.getch() # takes keystroke as byte literal
    except (ImportError,ModuleNotFoundError):
        import tty, termios
        fd = sys.stdin.fileno()
        old_settings = termios.tcgetattr(fd)
        try:
            tty.setraw(fd)
            ch = sys.stdin.read(1) # takes keystroke as ASCII
        finally:
            termios.tcsetattr(fd, termios.TCSADRAIN, old_settings)
        return ch


# Parse a string into a list of token strings
def tokenize(string):
    # Tokens that start with other tokens go before the tokens they contain ('OWIE' comes before 'OW')
    tokens = ['AAAH', 'AAAAGH', 'FUCK', 'SHIT', '!!!!!!', 'WHAT?!', 'OWIE', 'OW']

    program = []
    remaining = string
    while len(remaining) > 0:
        # Iterate over all possible tokens
        for token in tokens:
            # If the token matches the beginning of the remaining string, remove it from the remaining string and add it to the program
            if remaining.startswith(token):
                remaining = remaining.split(token, 1)[1]
                program.append(token)
                continue

        # This will only be called if no tokens match
        remaining = remaining[1:]

    return program


def interpret(tokens):
    pointerMap = {0:0}
    pointerLocation = 0
    step = 0
    while step < len(tokens):
        token = tokens[step]
        if token == 'AAAH':
            pointerLocation += 1
        elif token == 'AAAAGH':
            pointerLocation -= 1
        elif token == 'FUCK':
            if not pointerMap.get(pointerLocation):
                pointerMap[pointerLocation] = 0
            pointerMap[pointerLocation] += 1
        elif token == 'SHIT':
            if not pointerMap.get(pointerLocation):
                pointerMap[pointerLocation] = 0
            pointerMap[pointerLocation] -= 1
        elif token == '!!!!!!':
            print(chr(pointerMap[pointerLocation]),end='',flush=True)
        elif token == 'WHAT?!':
            charInput = getch()
            pointerMap[pointerLocation] = ord(charInput)
        elif token == 'OW':
            if pointerMap[pointerLocation] == 0:
                openBraces = 1
                while openBraces > 0:
                    step += 1
                    if tokens[step] == 'OW':
                        openBraces += 1
                    elif tokens[step] == 'OWIE':
                        openBraces -= 1
        elif token == 'OWIE':
            openBraces = 1
            while openBraces >0:
                step -= 1
                if tokens[step] == 'OW':
                    openBraces -= 1
                elif tokens[step] == 'OWIE':
                    openBraces += 1
            step -= 1
        step += 1


def writeDirect():
    lines = []
    inputFinished = False
    inputStep = 1
    print("\n\n\nTo finish your input, put a single . ALONE on a new line.")
    print("Enter the SCREAMCODE to interpret below:\n---------------------------------------")
    while inputFinished == False:
        screamcode = input()
        inputStep += 1
        if screamcode == '.':
            inputFinished = True
        else:
            lines.append(screamcode)

    screamcode = ' '.join(lines)
    print("---------------------------------------\nOutput:\n")
    interpret(tokenize(' '.join(lines)))

def loadFile():
    fileDir = os.path.dirname(__file__) + '/screams/'
    fileDirContents = os.listdir(fileDir)
    print("\nFiles in screams directory:\n---------------------------")
    print(*fileDirContents, sep='\n')
    loadTarget = input("\nFile to load: ")
    loadTarget = fileDir + loadTarget

    try:
        with open(loadTarget, encoding="utf-8") as file:
            lines = [l.rstrip('\n') for l in file]
        print("---------------------------------------\nOutput:\n")
        interpret(tokenize(' '.join(lines)))
    except FileNotFoundError:
        print("No such file in screams directory.")

try:
    fileDir = os.getcwd()
    loadTarget = fileDir + '/' + sys.argv[1]
    with open(loadTarget, encoding="utf-8") as file:
        lines = [l.rstrip('\n') for l in file]
    interpret(tokenize(' '.join(lines)))
    quit()
except IndexError:
    pass

print('\n\nWritten by Baguette (https://hbaguette.neocities.org)')
print('#####################################################\n## [L] Load File  [D] Interpret Directly  [Q] Quit ##\n#####################################################')
menuSelected = False
while menuSelected == False:
    menuChoice = getch() # IF functions below accept byte literal OR ascii
    if (menuChoice.lower() == b'l') or (menuChoice.lower() == 'l'):
        menuSelected = True
        loadFile()
    elif (menuChoice.lower() == b'd') or (menuChoice.lower() == 'd'):
        menuSelected = True
        writeDirect()
    elif (menuChoice.lower() == b'q') or (menuChoice.lower() == 'q'):
        quit()
