import random
import copy
import tkinter as tk
import pygame
fps = pygame.time.Clock()
game = tk.Tk()
game.resizable(False, False)
game.title("maze runnah")

#Global Variables
dimy = 12
dimx = 6
mazey = dimy
yah = dimy - mazey
go = True
puddles = []
start = [dimy//2]
end = []
tend = []
score = [0]
pos = 0
gr = 0
n = 0
ifirst = True
complete = False
restart = False
done = [0]
G = [ [0] * dimy for _ in range(dimx)]
grid = [ [0] * dimy for _ in range(dimx)]
ppos = [dimx-1,dimy // 2]

canvas = tk.Canvas(game)
canvas.config(width=100*dimy, height=100*dimx, bg='#bbada0')
canvas.pack()

#Randomizes the values of a 2 dim array
def randomize(G):
    global dimy, dimx
    for i in range(dimx):
        for j in range(dimy):
            x = random.randint(1,2)
            if x == 1:
                G[i][j] = 0
            else:
                G[i][j] = 1
    return(G)

#Checks if theres a path
def river(x,y):
    if G[x][y] == 0:
        if x == yah:
            end.append(y) 
        if x > 0 and G[x-1][y] == 0 and not( (x-1,y) in puddles ):
            puddles.append((x-1,y))
            river(x-1,y)
        if y < dimy-1 and G[x][y+1] == 0 and not( (x,y+1) in puddles):
            puddles.append((x,y+1))
            river(x,y+1)
        if x < dimx-1 and G[x+1][y] == 0 and not( (x+1,y) in puddles):
            puddles.append((x+1,y))
            river(x+1,y)
        if y > 0 and G[x][y-1] == 0 and not( (x,y-1) in puddles):
            puddles.append((x,y-1))
            river(x,y-1)

#Finds an array with start values
def find():
    global go, restart, tend, puddles, end, start
    go = True
    restart = False
    while go == True:
        restart = False
        tend = []
        randomize(G)
        for i in start:
            puddles = []
            end = []
            river(dimx-1, i)
            if len(end) > 0:
                for k in end:
                    if k not in tend:
                        tend.append(k)
            else:
                restart = True
                tend = []
                break
        if restart == False:
            start = tend
            go = False
            return(G)

frame = [ [1] * dimy for _ in range(dimx)]
mazes = [0,0,0,0]
score[0] = canvas.create_text(50 * dimy, 10 * (dimx), text=str(n), fill="blue", font=('Helvetica 80 bold'))

#Updates the frame shown on screen when the position of the snake changes
def updateframe():
    global pos, complete
    if not(stop()) and complete == False:
        if pos == 3 * dimx:
            mazes.pop(0)
            find()
            mazes.append(copy.deepcopy(G))
            pos = 2 * dimx - 1
        else:
            for i in range(pos, pos + dimx):
                k = i // dimx
                j = dimx-1 - (i - (k * dimx))
                z = dimx - (i- pos) - 1
                frame[z] = mazes[k][j]
        frame[ppos[0]][ppos[1]] = 2
    elif complete == False:
        if pos == 3 * dimx:
            mazes.pop(0)
            find()
            mazes.append(copy.deepcopy(G))
            pos = 2 * dimx - 1
        else:
            for i in range(pos, pos + dimx):
                k = i // dimx
                j = dimx-1 - (i - (k * dimx))
                z = dimx - (i- pos) - 1
                frame[z] = mazes[k][j]
        frame[ppos[0]][ppos[1]] = 2
        convert()
        complete = True

#Code for when the snake goes up
def up(event):
    global pos, n
    if frame[ppos[0]-1][ppos[1]] == 0:
        if ppos[0] > dimx // 2:
            ppos[0] -= 1
        else:
            pos += 1
        n += 1
        updateframe()
        convert()

#Code for when the snake goes down
def down(event):
    global pos, n
    if not(ppos[0] == dimx - 1) and frame[ppos[0]+1][ppos[1]] == 0:
        ppos[0] += 1
        updateframe()
        convert()

#Code for when the snake goes right
def right(event):
    global pos, n
    if not(ppos[1] == dimy - 1) and frame[ppos[0]][ppos[1]+1] == 0 :
        ppos[1] += 1
        updateframe()
        convert()

#Code for when the snake goes left
def left(event):
    global pos, n
    if not(ppos[1] == 0) and frame[ppos[0]][ppos[1]-1] == 0:
        ppos[1] -= 1
        updateframe()
        convert()

#Determines if the snake cannot move anymore, to print "game over"
def stop():
    if ifirst == False:
        if not(frame[ppos[0]-1][ppos[1]] == 0 or (not(ppos[0] == dimx - 1) and frame[ppos[0]+1][ppos[1]] == 0) or (not(ppos[1] == dimy - 1) and frame[ppos[0]][ppos[1]+1] == 0 ) or (not(ppos[1] == 0) and frame[ppos[0]][ppos[1]-1] == 0)):
            return(True)
    return(False)

#Converts the grid of 1's and 0's into actual tkinter blocks
def convert():
    for i in range(dimx):
        for j in range(dimy):
            if frame[i][j] == 1:
                canvas.delete(grid[i][j])
                grid[i][j] = canvas.create_rectangle(100*j, 100*i, 100*j + 100, 100*i + 100, tag='bounce', outline="black", fill="#000000")
            elif frame[i][j] == 2:
                canvas.delete(grid[i][j])
                grid[i][j] = canvas.create_rectangle(100*j, 100*i, 100*j + 100, 100*i + 100, tag='bounce', outline="black", fill="#00FF00")
            else:
                canvas.delete(grid[i][j])
                grid[i][j] = 0
    canvas.delete(score[0])
    score[0] = canvas.create_text(50 * dimy, 10 * (dimx), text=str(n), fill="blue", font=('Helvetica 80 bold'))
    if complete == True:
        done[0] = canvas.create_text(50 * dimy, 50 * (dimx), text="GAME OVER", fill="red", font=('Helvetica 100 bold'))


  
#Generates the first frame
mazes[0] = copy.deepcopy(find())
mazes[1] = copy.deepcopy(find())
mazes[2] = copy.deepcopy(find())
mazes[3] = copy.deepcopy(find())
updateframe()
convert()
ifirst = False

#Keybinds
game.bind('<Key-Right>', right)
game.bind('<Key-Down>', down)
game.bind('<Key-Left>', left)
game.bind('<Key-Up>', up)
game.mainloop()
