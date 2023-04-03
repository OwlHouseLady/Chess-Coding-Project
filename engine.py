# This is the engine file, It is a class

## It stores all the information of the state of the current chess game
## Responsible for valid moves in the game
## Make a move log 

########

# Embeded lists in order to store start points for pieces
class gstate():
    def __init__(self):
        # Chosen a typical 8x8 2d list with each item in the list having two characters
        # One character is to identify what colour which the piece is 
        # Lowercase b for black
        # lowercase w for white
        # The second character is to identify what type of piece it is 
        # for example R for rook or Q for queen
        # The second item is written in capitals
        # The double hypen was chosen so that I could pass it as a empty space
        # On the board
        self.board = [
            ["bR", "bN", "bB", "bQ", "bK", "bB", "bN", "bR"], 
            ["bP", "bP", "bP", "bP", "bP", "bP", "bP", "bP"],
            ["--", "--", "--", "--", "--", "--", "--", "--"],
            ["--", "--", "--", "--", "--", "--", "--", "--"],
            ["--", "--", "--", "--", "--", "--", "--", "--"],
            ["--", "--", "--", "--", "--", "--", "--", "--"],
            ["wP", "wP", "wP", "wP", "wP", "wP", "wP", "wP"],
            ["wR", "wN", "wB", "wQ", "wK", "wB", "wN", "wR"]]
            
        self.wtf = True # White to move if false it is black to move
        self.log = [] #Keeps a move log
    
    def makeMove(self,move): # Takes the move as a paramater as executes it. Does nto working currently for castling, en passent and promotion 
        self.board[move.startRow][move.startCol] = "--"
        self.board[move.endRow][move.endCol] = move.pieceMoved
        self.log.append(move) # Keeps the move inside of a log
        self.wtf = not self.wtf 
    
    def undo_move(self):
        if len(self.log) != 0:
            move = self.log.pop()
            self.board[move.startRow][move.startCol] = move.pieceMoved
            self.board[move.endRow][move.endCol] = move.pieceCaptured # changed this line to fix 
            self.wtf = not self.wtf # Reverses whos move it is


    '''
    Check if king  is placed in check
    '''

    def vaidmove(self):
        return self.possible_moves()

    def possible_moves(self):
        moves = [] # Initialize an empty list to store all the possible moves
        for r in range(len(self.board)): # Loop through each row of the board
            for c in range(len(self.board[r])): # Loop through each column in the current row
                playerturn = self.board[r][c][0] # Get the color of the player whose turn it is
                # Check if the current player can move based on the "wtf" (white-to-move-first) option
                if (playerturn == "w" and self.wtf) or (playerturn == "b" and not self.wtf):
                    piece = self.board[r][c][1] # Get the type of the piece at the current position
                    # Determine the valid moves for the current piece and add them to the "moves" list
                    if piece == "P":
                        print("test")
                        self.getPawnMoves(r,c,moves)
                        print (*moves)
                    elif piece == "R":
                        self.getRookMoves(r,c,moves)
                    elif piece == "B":
                        self.getBishopMoves(r,c,moves)
                    elif piece == "Q":
                        self.getQueenMoves(r,c,moves)
                    elif piece == "K":
                        self.getKingMoves(r,c,moves)
        return moves 
    
 # This method is used to get all the possible moves for a pawn
# given its current position (r,c) on the board.

    def getPawnMoves(self, r, c, moves):
        # 'wtf' is a flag that indicates if it's a white or black pawn.
        if self.wtf:
            # If it's a white pawn, we check if the cell in front of it is empty.
            # If it is, we can move one step forward.
            if self.board[r-1][c] == "--":
                moves.append(Move((r, c), (r-1, c), self.board))
                # If the white pawn is at its starting position (row 6) and the
                # cell two steps in front of it is also empty, it can move two
                # steps forward.
                if r == 6 and self.board[r-2][c] == "--":
                    moves.append(Move((r,c), (r-2, c), self.board))
    
    def getRookMoves(self,r,c,moves):
        pass      
    def getBishopMoves(self,r,c,moves):
        pass      
    def getQueenMoves(self,r,c,moves):
        pass      
    def getKingMoves(self,r,c,moves):
        pass                   

class Move():
    # map the key to a value

    #key : value

    ranksToRows = {"1":7, "2":6, "3":5,"4":4,
                   "5":3,"6":2, "7":1, "8":0}
    
    rowsToRanks = {v: k for k, v in ranksToRows.items()}
    filesToCols = {"a":0, "b":1, "c":2, "d":3,
                   "e":4,"f":5, "g":6, "h":7}
    colsToFiles = {v: k for k, v in filesToCols.items()}

    def __init__(self, startSq, endSq, board):
        self.startRow = startSq[0]
        self.startCol = startSq[1]
        self.endRow = endSq[0] 
        self.endCol = endSq[1]
        self.pieceMoved = board[self.startRow][self.startCol]
        self.pieceCaptured = board[self.endRow][self.endCol]

    def getChessNotation(self):
        return self.getRankFile(self.startRow, self.startCol) + self.getRankFile(self.endRow, self.endCol)
    def getRankFile(self,r,c):
        return self.colsToFiles[c] + self.rowsToRanks[r]
    

