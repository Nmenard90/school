topLeft   = "X"
topMiddle = "X"
topRight  = " "
midLeft   = "O"
midMiddle = "X"
midRight  = "O"
botLeft   = " "
botMiddle = " "
botRight  = "X"

## X | O | O
##---+---+---
##   | X |
##---+---+---
##   |   | X

AllXs = "XXX"
AllOs = "OOO"

def display(tl, tm, tr, ml, mm, mr, bl, bm, br):
    print(" ", tl, " | ", tm, " | ", tr, sep="" )
    print("---+---+---")
    print(" ", ml, " | ", mm, " | ", mr, sep="" )
    print("---+---+---")
    print(" ", bl, " | ", bm, " | ", br, sep="" )

def haveTicTacToe(tl, tm, tr, ml, mm, mr, bl, bm, br):
    line = topLeft + topMiddle + topRight
    if line == AllXs:
        print("Tic tac toe in X in first row...")
        return True
    if line == AllOs:
        print("Tic tac toe in O in first row...")
        return True
    line = midLeft + midMiddle + midRight
    if line == AllXs:
        print("Tic tac toe in X in second row...")
        return True
    if line == AllOs:
        print("Tic tac toe in O in second row...")
        return True
    line = botLeft + botMiddle + botRight
    if line == AllXs:
        print("Tic tac toe in X in third row...")
        return True
    if line == AllOs:
        print("Tic tac toe in O in third row...")
        return True

    line = topLeft + midLeft + botLeft
    if line == AllXs:
        print("Tic tac toe in X in first column...")
        return True
    if line == AllOs:
        print("Tic tac toe in O in first column...")
        return True
    line = topMiddle + midMiddle + botMiddle
    if line == AllXs:
        print("Tic tac toe in X in second column...")
        return True
    if line == AllOs:
        print("Tic tac toe in O in second column...")
        return True
    line = topRight + midRight + botRight
    if line == AllXs:
        print("Tic tac toe in X in third column...")
        return True
    if line == AllOs:
        print("Tic tac toe in O in third column...")
        return True
    line = botLeft + midMiddle + topRight
    if line == AllXs:
        print("Tic tac toe in X in forward diagonal...")
        return True
    if  line == AllOs:
        print("Tic tac toe in O in forward diagonal...")
        return True
    line = botRight + midMiddle + topLeft
    if line == AllXs:
        print("Tic tac toe in X in backward diagonal...")
        return True
    if  line == AllOs:
        print("Tic tac toe in O in backward diagonal...")
        return True
    return False
        

    



        

display(topLeft, topMiddle, topRight, midLeft, midMiddle, midRight, botLeft,
        botMiddle, botRight)
haveTTT = haveTicTacToe(topLeft, topMiddle, topRight, midLeft, midMiddle, midRight, botLeft,
        botMiddle, botRight)
print(haveTTT)
