#This is the main file for the chess bot

## It will take user input
## Display gamestate 


########################################################

# Dependancies for board

import pygame as pg
import engine

pg.init()


Width = Height = 512
Dimension = 8 # This is the number of spaces on each row of the chess board 
Sqsize = Height // Dimension
TopFPS = 30
Images = {}

'''
PyGame is very inefficent when loading images so I only want to load
The images once
'''

def ImageLoad():
    pieces = ["wP", "wR", "wN", "wB", "wK", "wQ", "bP", "bR", "bN", "bB", "bK", "bQ"]
    for piece in pieces:
        Images[piece] = pg.transform.scale(pg.image.load("images/" + piece + ".png"), (Sqsize,Sqsize))

'''
The main section of the code 
Shall handel all of the user input and update the graphics
'''

def main():
    
    screen = pg.display.set_mode((Width, Height))
    clock = pg.time.Clock()
    screen.fill(pg.Color("white"))
    gs = engine.gstate()
    validmoves = gs.vaidmove()
    movemade = False # Saves on time complexity 
    ImageLoad()
    running = True
    sqSel = () #No square that is currently selected by the user
    playclicks = [] #Keeps track of all the player click so that the play can go back

    while running:
        for i in pg.event.get():
            if i.type == pg.QUIT:
                running = False
            elif i.type == pg.MOUSEBUTTONDOWN: # If the user presses down the mouse
                loc = pg.mouse.get_pos() # finds the current x,y co-ordinates of the mouse
                col = loc[0]//Sqsize # Takes the cord in position 0 from loc and div by square size
                row = loc[1]//Sqsize # Takes the cord in position 1 from loc and div by square size
                print(col) 
                print(row)
                sqSel = (row, col) # Selects the row an colum from above
             
                
                sqSel = (row, col)
                playclicks.append(sqSel) # Adds in both the first and seconds clicks to a list
                print(sqSel)
            if len(playclicks) == 2: # after second click
                move = engine.Move(playclicks[0],playclicks[1], gs.board)
                
                if move in validmoves:
                    gs.makeMove(move)
                    movemade = True
                    sqSel = ()
                    playclicks = []
            elif i.type == pg.KEYDOWN:
                if i.key == pg.K_z:
                    gs.undo_move()
                    gs.vaidmove()

        if movemade:
            validmoves = gs.vaidmove()
            print(move.getChessNotation())
            movemade = False
        drawGameState(screen, gs)
        clock.tick(TopFPS)
        pg.display.flip()


'''
Graphics for the current game
'''

def drawGameState(screen, gs):
    drawBoard(screen) # Create the spaces on the board
    drawPieces(screen, gs.board) # Shows the places on the top of board

def drawBoard(screen):
    colours = [pg.Color("white"), pg.Color("grey")]
    for r in range(Dimension):
        for c in range (Dimension):
            colour = colours[((r+c) % 2)]
            pg.draw.rect(screen, colour, pg.Rect(c*Sqsize, r*Sqsize, Sqsize, Sqsize))



def drawPieces(screen, board):
    for r in range(Dimension):
        for c in range (Dimension):
            piece = board[r][c]
            if piece != "--": # The space is ocupied meaning a playable piece should be there
                screen.blit(Images[piece], pg.Rect(c*Sqsize, r*Sqsize, Sqsize, Sqsize))


if __name__ == "__main__":
    main()