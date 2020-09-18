def interpret(scream):
    pointerMap = {0:0}
    pointerLocation = 0
    step = 0
    code = scream.split(" ")
    while step < (len(code)-1):
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
            print(chr(pointerMap[pointerLocation]),end='')
        elif code[step] == 'WHAT?!':
            try:
                pointerMap[pointerLocation] = int(input("Input:"))
            except ValueError:
                pointerMap[pointerLocation] = ord(x)
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

print("Written by Baguette (https://hbaguette.neocities.org)")
screamcode = input("Enter the SCREAMCODE to interpret below:\n---------------------------------------\n")
print("---------------------------------------\nOutput:\n")
interpret(screamcode)
