p_board = {1: ' ', 2: ' ', 3: ' ',
           4: ' ', 5: ' ', 6: ' ',
           7: ' ', 8: ' ', 9: ' '}

player = 'X'
Viji = 'O'

def print_p_board(p_board):
    print(p_board[1] + " | " + p_board[2] + " | " + p_board[3])
    print("--+---+--")
    print(p_board[4] + " | " + p_board[5] + " | " + p_board[6])
    print("--+---+--")
    print(p_board[7] + " | " + p_board[8] + " | " + p_board[9])

def Spaceavailability(position):
    if p_board[position] == ' ':
        return True
    return False

def insertLetter(letter, position):
    if Spaceavailability(position):
        p_board[position] = letter 
        print_p_board(p_board)
        if Tie():
            print("Tie!")
            exit() 
        if Winner():
            if letter == 'X':
                print("Congratulations!! You won")
                exit()
            else:
                print("Viji Winners!!!")
                exit()
        return 
    else:
        print("Invalid position")
        position = int(input("Please enter a new position: "))
        insertLetter(letter, position)
        return  

def Winner():
    if (p_board[1] == p_board[2] and p_board[1] == p_board[3] and p_board[1] != ' '):
        return True
    elif (p_board[4] == p_board[5] and p_board[4] == p_board[6] and p_board[4] != ' '):
        return True
    elif (p_board[7] == p_board[8] and p_board[7] == p_board[9] and p_board[7] != ' '):
        return True
    elif (p_board[1] == p_board[4] and p_board[1] == p_board[7] and p_board[1] != ' '):
        return True
    elif (p_board[2] == p_board[5] and p_board[2] == p_board[8] and p_board[2] != ' '):
        return True
    elif (p_board[3] == p_board[6] and p_board[3] == p_board[9] and p_board[3] != ' '):
        return True
    elif (p_board[1] == p_board[5] and p_board[1] == p_board[9] and p_board[1] != ' '):
        return True
    elif (p_board[7] == p_board[5] and p_board[7] == p_board[3] and p_board[7] != ' '):
        return True
    else:
        return False 
    
def checkWinnerner(mark):
    if (p_board[1] == p_board[2] and p_board[1] == p_board[3] and p_board[1] == mark):
        return True
    elif (p_board[4] == p_board[5] and p_board[4] == p_board[6] and p_board[4] == mark):
        return True
    elif (p_board[7] == p_board[8] and p_board[7] == p_board[9] and p_board[7] == mark):
        return True
    elif (p_board[1] == p_board[4] and p_board[1] == p_board[7] and p_board[1] == mark):
        return True
    elif (p_board[2] == p_board[5] and p_board[2] == p_board[8] and p_board[2] == mark):
        return True
    elif (p_board[3] == p_board[6] and p_board[3] == p_board[9] and p_board[3] == mark):
        return True
    elif (p_board[1] == p_board[5] and p_board[1] == p_board[9] and p_board[1] == mark):
        return True
    elif (p_board[7] == p_board[5] and p_board[7] == p_board[3] and p_board[7] == mark):
        return True
    else:
        return False

def Tie():
    for key in p_board.keys():
        if p_board[key] == ' ':
            return False
    return True

def playerMove():
    position = int(input("Enter the position: "))
    insertLetter(player, position)
    return 

def viji():
    bestscore = -1000
    bestmove = 0
    for key in p_board.keys():
        if p_board[key] == ' ':
            p_board[key] = Viji
            score = minimax(p_board, False)
            p_board[key] = ' '
            if score > bestscore:
                bestscore = score
                bestmove = key
    insertLetter(Viji, bestmove)
    return

def minimax(p_board, maximizing):
    if checkWinnerner(Viji):
        return 1
    elif checkWinnerner(player):
        return -1
    elif Tie():
        return 0
    if maximizing:
        bestscore = -1000
        for key in p_board.keys():
            if p_board[key] == ' ':
                p_board[key] = Viji
                score = minimax(p_board, False)
                p_board[key] = ' '
                if score > bestscore:
                    bestscore = score
        return bestscore
    else:
        bestscore = 1000
        for key in p_board.keys():
            if p_board[key] == ' ':
                p_board[key] = player
                score = minimax(p_board, True)
                p_board[key] = ' '
                if score < bestscore:
                    bestscore = score
        return bestscore

while not Winner():
    playerMove()
    viji()
