import os

def getch():
    try:
        import msvcrt
        char = msvcrt.getch()
    except ImportError:
        pass
    return char


def interpret(scream):
    print("---------------------------------------\nOutput:\n")
    pointerMap = {0:0}
    pointerLocation = 0
    step = 0
    code = scream.split(" ")
    while step < (len(code)):
        if code[step] == 'AAAH':
            pointerLocation += 1
        elif code[step] == 'AAAAGH':
            pointerLocation -= 1
        elif code[step] == 'FUCK':
            if not pointerMap.get(pointerLocation):
                pointerMap[pointerLocation] = 0
            pointerMap[pointerLocation] += 1
        elif code[step] == 'SHIT':
            if not pointerMap.get(pointerLocation):
                pointerMap[pointerLocation] = 0
            pointerMap[pointerLocation] -= 1
        elif code[step] == '!!!!!!':
            print(chr(pointerMap[pointerLocation]),end='',flush=True)
        elif code[step] == 'WHAT?!':
            charInput = getch()
            
            pointerMap[pointerLocation] = ord(charInput)
        elif code[step] == 'OW':
            if pointerMap[pointerLocation] == 0:
                openBraces = 1
                while openBraces > 0:
                    step += 1
                    if code[step] == 'OW':
                        openBraces += 1
                    elif code[step] == 'OWIE':
                        openBraces -= 1
        elif code[step] == 'OWIE':
            openBraces = 1
            while openBraces >0:
                step -= 1
                if code[step] == 'OW':
                    openBraces -= 1
                elif code[step] == 'OWIE':
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
    interpret(' '.join(lines))

def loadFile():
    fileDir = os.getcwd() + '/screams/'
    fileDirContents = os.listdir(fileDir)
    print("\nFiles in screams directory:\n---------------------------")
    print(*fileDirContents, sep='\n')
    loadTarget = input("\nFile to load: ")
    loadTarget = fileDir + loadTarget

    try:
        with open(loadTarget, encoding="utf-8") as file:
            lines = [l.rstrip('\n') for l in file]
        interpret(' '.join(lines))
    except FileNotFoundError:
        print("No such file in screams directory.")


print('\n\nWritten by Baguette (https://hbaguette.neocities.org)')
print('#####################################################\n## [L] Load File  [D] Interpret Directly  [Q] Quit ##\n#####################################################')
menuSelected = False
while menuSelected == False:
    menuChoice = getch()
    if menuChoice.lower() == b'l':
        menuSelected = True
        loadFile()
    elif menuChoice.lower() == b'd':
        menuSelected = True
        writeDirect()
    elif menuChoice.lower() == b'q':
        quit()
