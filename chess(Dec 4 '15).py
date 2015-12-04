def createBoard():
    chessboard = [[]*8 for _ in range(8)]
    #for i in chessboard:
    #    print i
    for i in range(8):          #y axis
        for j in range(8):      #x axis
            if (i%2 ==0):       #if even numbered row
                if (j%2 ==0):   #if even numbered column
                    chessboard[i].append('[ | ]')
                elif (j%2 ==1):
                    chessboard[i].append('[X| ]')           
            else:
                if (j%2 ==0):
                    chessboard[i].append('[X| ]')
                else:
                    chessboard[i].append('[ | ]')
    #want this for display, but not at this stage vvv            
    #    chessboard[i] = ''.join(chessboard[i]) + "\n"
    print "\n \n"
    #for k in range :
     #   k = ''.join(k) + "\n"
        #print k
    return chessboard

def setBoard(board):
    #sets the pieces on the board
    # p = pawn
    # k = knight
    # b = bishop
    # r = rook
    # q = queen
    # + = king
    newBoard = []
    pieces1 = ["R","K","B","+","Q","B","K","R"]
    pieces2 = ["R","K","B","Q","+","B","K","R"]
    for i in range(8):      #i = row of the board
        if (i == 0):
            for j in range(8):
                board[i][j] = setPiece(board[i][j],pieces1[j])
        if ((i == 1) or (i == 6)):
            for j in range(8):
                board[i][j] = setPiece(board[i][j],"P")        
        if (i == 7):
            for j in range(8):
                board[i][j] = setPiece(board[i][j],pieces2[j])
        #print ''.join(board[i]) + "\n"
    return board

def displayBoard(ready):
    row = 0
    while (row < 8):
        if (row == 7):
            print str(8 - row)+'|' + ''.join(ready[row])
            print " |________________________________________"
        else:
            print str(8 - row)+'|' + ''.join(ready[row]) + "\n |"
        row += 1
    print "    A    B    C    D    E    F    G    H    "

def setPiece(string,new): 
    #allows for placing/ removing piece from tile
    return string[:3] + new + string[4:]
    
def movePiece(start, end, board):
    # start, end comprise the order
    # move [start] to [end]
    # ex: move A2 to A4
    # NOTE: need to remember that prog reads board from 8 -> 1
    #       and I read it from 1 -> 8
    #       might need an invertMove method for my moves
    invList = [7,6,5,4,3,2,1,0] #row 1 to 0 to 7, row 8 to 7 to 0
    sRow = invList[int(start[1]) - 1] 
    eRow = invList[int(end[1]) - 1]
    sCol = ord(start[0]) - 65
    eCol = ord(end[0]) - 65
    board[eRow][eCol] = setPiece(board[eRow][eCol],board[sRow][sCol][3])
    board[sRow][sCol] = setPiece(board[sRow][sCol]," ")
    return board
    
# MAIN #
empty = createBoard()
board = setBoard(empty)
displayBoard(board)
directions = "Please type moves in format '[start tile] to [end tile]', or 'End' to end the match" 
move = raw_input("Your Move? ").upper()
while move:
    if (move == "END"):
        print "\nFinal Board: "
        displayBoard(board)
        break
    elif (("A" <= move[0] <= "H") and (1 <= int(move[1]) <= 8)):
            board = movePiece(move[:2], move[6:], board)
            displayBoard(board)    
    else:
        print "Invalid move." , directions
    move = raw_input("Your Move? ")