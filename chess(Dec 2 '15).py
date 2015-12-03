
#from 12/2/2015

chessboard = [[]*8 for _ in range(8)]
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
print "\n \n"
for k in chessboard:
	print ''.join(k) + "\n"