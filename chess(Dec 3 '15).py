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
def setPiece(string,new): 
    #allows for placing/ removing piece from tile
    return string[:3] + new + string[4:]
    
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
        print ''.join(board[i]) + "\n"
    return board
# MAIN #
x = createBoard()
y = setBoard(x)
#for i in y:
#    print ''.join(i) + "\n"