
gameBoard = {
    'topL':' ' , 'topM':' ' , 'topR':' ' , 
    'midL':' ' , 'midM':' ' , 'midR':' ' , 
    'lowL':' ' , 'lowM':' ' , 'lowR':' '
}

def printBoard(board):
    print(board['topL'] + '|' + board['topM'] + '|' + board['topR'])
    print('-+-+-')
    print(board['lowM'] + '|' + board['midM'] + '|' + board['midR'])
    print('-+-+-')
    print(board['lowL'] + '|' + board['lowM'] + '|' + board['lowR'])

turn = 'X'

for i in range(9):
    printBoard(gameBoard)
    print('\n' + str(turn) + "'s turn, select a position.")
    move = input()
    gameBoard[move] = turn
    if turn == 'X':
        turn = 'O'
    else:
        turn = 'X'

