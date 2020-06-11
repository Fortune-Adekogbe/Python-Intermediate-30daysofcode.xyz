import pygame
from pygame.locals import *
import sys

pygame.init()
ttt = pygame.display.set_mode((300,325))
pygame.display.set_caption("Tic_tac_toe")


def initBoard(ttt):
    #initializing board
    background = pygame.Surface(ttt.get_size())
    background = background.convert()
    background.fill((250,250,250))

    #draw the grid lines
    #vertical lines
    pygame.draw.line(background,(0,0,0),(100,0),(100,300),2)
    pygame.draw.line(background,(0,0,0),(200,0),(200,300),2)

    #horizontal lines
    pygame.draw.line(background,(0,0,0),(0,100),(300,100),2)
    pygame.draw.line(background,(0,0,0),(0,200),(300,200),2)

    return background



def drawStatus(board):
    global XO, winner
    if winner is None:
        message = f"{XO}'s turn"
        if sum(grid[i].count('X') for i in range(3))==5:
            message = "Tis a draw... (Press any key to replay)"
    else:
        message = f"{'X' if XO=='O' else 'O'} won!!! (Press any key to replay)"
    font = pygame.font.Font(None, 24)
    text = font.render(message, 1, (0, 250, 0))

    board.fill((0, 0, 0), (0, 300, 300, 25))
    if len(message)>15:
        board.blit(text, (10, 305))
    else:
        board.blit(text, (120, 305))

def showBoard(ttt,board):
    drawStatus(board)
    ttt.blit(board,(0,0))
    pygame.display.flip()

def boardPos(mouseX,mouseY):
    row = mouseX//100
    column = mouseY//100
    return row,column

def drawMove(board,Brow,Bcolumn,Piece):
    # Draw X and O pieces
    cx = Brow*100 + 50
    cy = Bcolumn*100 + 50

    if Piece == "O":
        pygame.draw.circle(board,(0,0,0),(cx,cy),44,2)

    else:
        pygame.draw.line(board,(0,0,0),(cx-22,cy-22),(cx+22,cy+22),2)
        pygame.draw.line(board,(0,0,0),(cx+22,cy-22),(cx-22,cy+22),2)
    grid[Brow][Bcolumn] = Piece


def clickBoard(board):
    global grid, XO

    mouseX, mouseY = pygame.mouse.get_pos()
    row , column = boardPos(mouseX,mouseY)

    #verify that the space is unoccupied
    if row<3 and column<3:
        if not grid[row][column] in ['X','O'] and winner is None:
            drawMove(board,row,column,XO)

        temp = grid[:]
        aaa = ''.join([i for j in temp for i in j if i != None])

        #Change turn
        if winner is None:
            if aaa.count("X") - aaa.count("O")==1:
                XO = "O"
            elif aaa.count("0") - aaa.count("X")==1:
                XO = "X"
            elif aaa.count("X") == aaa.count("O"):
                    XO = "O" if XO=="X" else "X"
            elif  aaa.count("X") - aaa.count("O")>1:
                XO="O"
            elif  aaa.count("X") - aaa.count("O")<1:
                XO = "X"


def gameWon(board):
    global grid, winner
    won = ['X','O']
    for r in range(3):
        s = list(set(grid[r]))
        if len(s)==1 and s[0] in won:
            winner = s[0]
            pygame.draw.line(board,(250,0,0),((r*100)+50,0),((r*100)+50,300),2)


    for c in range(3):
        s = list(set(r[c] for r in grid))
        if len(s)==1 and s[0] in won:
            winner = s[0]
            pygame.draw.line(board, (250, 0, 0), (0, (c * 100) + 50), (300, (c * 100) + 50), 2)

    s1 = list(set(grid[i][i] for i in range(3)))
    if len(s1) == 1 and s1[0] in won:
        winner = s1[0]
        pygame.draw.line(board, (250, 0, 0), (50,50), (250,250), 2)
    s2 = list(set(grid[i][2-i] for i in range(3)))
    if len(s2) == 1 and s2[0] in won:
        winner = s2[0]
        pygame.draw.line(board, (250, 0, 0), (250,50), (50,250), 2)


def main():
    global running
    while running==1:
        for event in pygame.event.get():
            if event.type == KEYDOWN:
                running = 0
            elif event.type is MOUSEBUTTONDOWN:
                clickBoard(board)
            elif event.type == QUIT:
                sys.exit()


            #check for a winner
            gameWon(board)

            # Update the display
            showBoard(ttt,board)

count = 0
while True:
    board = initBoard(ttt)
    running = 1
    winner = None
    XO = "X"
    grid = [[None for i in range(3)] for j in range(3)]
    main()