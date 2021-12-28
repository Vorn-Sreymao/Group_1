import tkinter as tk
from tkinter import Canvas, font
from typing import Counter
import winsound
import random
# from tkinter.constants import NW, W
root = tk.Tk()
root.geometry("1600x700")
frame = tk.Frame()
frame.master.title("Python VC1")
canvas = tk.Canvas(frame)

#________________________________________Array2D Of Grid(Sreymao and Theara)_______________________________________
array2D = [
            [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
            [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
            [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
            [1, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 1],
            [1, 0, 1, 6, 1, 3, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 1],
            [1, 0, 1, 0, 1, 0, 0, 0, 0, 0, 0, 0, 2, 0, 0, 0, 0, 1, 0, 1, 0, 0, 0, 0, 0, 0, 1, 0, 0, 1, 0, 0, 0, 0, 4, 0, 0, 0, 0, 0, 0, 0, 1, 0, 1],
            [1, 0, 1, 0, 1, 1, 1, 1, 0, 0, 0, 2, 0, 2, 0, 0, 0, 1, 2, 1, 0, 0, 0, 2, 0, 0, 1, 0, 0, 1, 1, 1, 1, 0, 1, 1, 1, 1, 1, 1, 1, 0, 1, 0, 1],
            [1, 0, 1, 0, 0, 0, 0, 1, 0, 0, 0, 0, 2, 0, 0, 0, 0, 1, 0, 1, 0, 0, 2, 0, 2, 0, 1, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 3, 1, 0, 1, 0, 1],
            [1, 0, 1, 0, 4, 0, 0, 1, 0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 0, 1, 0, 0, 0, 2, 0, 0, 1, 0, 0, 0, 2, 0, 1, 0, 2, 0, 0, 1, 1, 1, 1, 0, 1, 0, 1],
            [1, 0, 1, 1, 1, 2, 0, 1, 0, 0, 2, 0, 0, 1, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 2, 0, 1, 2, 0, 2, 0, 1, 0, 2, 0, 0, 1, 0, 1],
            [1, 0, 1, 0, 1, 0, 0, 1, 0, 2, 0, 2, 0, 1, 0, 1, 1, 1, 1, 1, 0, 0, 0, 0, 0, 2, 1, 2, 0, 3, 2, 0, 1, 0, 2, 0, 0, 1, 0, 2, 0, 0, 1, 0, 1],
            [1, 0, 1, 0, 1, 0, 0, 0, 0, 0, 2, 0, 0, 1, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 1, 2, 0, 0, 0, 0, 0, 0, 1, 0, 2, 0, 0, 1, 0, 1],
            [1, 0, 1, 2, 1, 3, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 2, 2, 2, 0, 0, 0, 1, 0, 0, 1, 0, 2, 2, 0, 0, 0, 0, 1, 0, 2, 0, 0, 1, 0, 1],
            [1, 0, 1, 2, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 2, 0, 0, 1, 0, 1],
            [1, 0, 1, 2, 0, 0, 2, 2, 2, 2, 0, 0, 2, 0, 0, 0, 0, 3, 1, 0, 0, 0, 2, 0, 0, 0, 1, 0, 0, 1, 0, 0, 0, 0, 2, 0, 0, 0, 0, 0, 0, 0, 1, 0, 1],
            [1, 0, 1, 2, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 0, 2, 0, 2, 0, 0, 1, 0, 0, 1, 0, 0, 0, 2, 0, 2, 0, 0, 0, 0, 0, 0, 1, 0, 1],
            [1, 0, 1, 0, 0, 0, 2, 2, 2, 2, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 2, 0, 0, 3, 1, 0, 0, 1, 3, 0, 0, 4, 2, 0, 0, 0, 0, 0, 0, 0, 1, 0, 1],
            [1, 0, 1, 2, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 0, 1, 0, 0, 1, 1, 0, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 1],
            [1, 0, 1, 2, 1, 0, 0, 0, 0, 0, 0, 0, 2, 2, 2, 2, 2, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 2, 0, 2, 0, 2, 0, 2, 0, 0, 0, 0, 0, 1, 0, 1],
            [1, 0, 1, 2, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 2, 0, 2, 0, 2, 0, 0, 0, 0, 0, 5, 1, 0, 1],
            [1, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 1],
            [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
            [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1]
    ]


# _____________________________________________varible______________________________________
count = 0
gameNotOver = True
#_____________________________________Images______________________________________________
enemy_img = tk.PhotoImage(file="images/monster.png")
bgimg = tk.PhotoImage(file="images/bg.png")
mario_img = tk.PhotoImage(file="images/mario1.png")
wall_img = tk.PhotoImage(file="images/box.png")
coin_img = tk.PhotoImage(file="images/coin.png")
home_img = tk.PhotoImage(file="images/door.png")
fire_img = tk.PhotoImage(file="images/red.png")
winner_img = tk.PhotoImage(file="images/won.png")
lost_img = tk.PhotoImage(file="images/lost.png")
#____________________________________Sound________________________________________________________
winsound.PlaySound("sound/start.wav",winsound.SND_FILENAME | winsound.SND_ASYNC )

#____________________________________Theara_______________________________________________________

#_____________________________________Graphic of array2D__________________________________________
def drawGrid():
    global array2D,count
    canvas.create_image(600, 370, image=bgimg)
    canvas.create_text(100, 60, text="Your Score: " +str(count), font=("", 12))
    for row in range(len(array2D)):
        for col in range(len(array2D[row])):
            
            if array2D[row][col] == 1:
                canvas.create_image(15+(30*col),15+(30*row),image = wall_img)

            elif array2D[row][col] == 2:
                canvas.create_image(15+(30*col),15+(30*row),image = coin_img)

            elif array2D[row][col] == 3:
                canvas.create_image(15+(30*col),15+(30*row),image = enemy_img)

            elif array2D[row][col] == 4:
                canvas.create_image(15+(30*col),15+(30*row),image = fire_img)
                    
            elif array2D[row][col] == 5:
                canvas.create_image(15+(30*col),15+(30*row),image = home_img)

            elif array2D[row][col] == 6:
                canvas.create_image(15+(30*col),15+(30*row),image = mario_img)
drawGrid()



#_________________________________Theara_____________________________________________________________________


# _________________________________Move Right________________________________________________________________  
def getIndex(array2D):
     for row in range(len(array2D)):
          for col in range(len(array2D[row])):
               if array2D[row][col] == 6:
                    postion=[row, col]
     return postion


 
#__________________________________________PLAYER FOR MOVE RIGHT LEFT UP DOWN________________________

def move(direction):
    global gameNotOver, count
    player = getIndex(array2D)
    playerRow = player[0]
    playerColumn = player[1]

    #_____________________________________COMPUTE THE NEXT POSSITION__________________________________ 

    if gameNotOver :
        if direction == 'right':
            canvas.delete("all")
            nextRow = playerRow
            nextColumn = playerColumn + 1
        elif direction == 'left':
            canvas.delete("all")
            nextRow = playerRow
            nextColumn = playerColumn - 1
        elif direction == 'up':
            canvas.delete("all")
            nextRow = playerRow -1
            nextColumn = playerColumn 
        elif direction == 'down':
            canvas.delete("all")
            nextRow = playerRow +1
            nextColumn = playerColumn 
        if  array2D[nextRow][nextColumn] != 1 and array2D[nextRow][nextColumn] != 4:
            
            #____________________________MANAGE THE COIN_______________________________________________
            if array2D[nextRow][nextColumn] == 2:
                canvas.delete("all")
                count+= 10
                winsound.PlaySound("sound\\coin.wav", winsound.SND_ASYNC | winsound.SND_ASYNC)

            #_____________________________MANAGE THE ANAMY ____________________________________________
            if array2D[nextRow][nextColumn] == 3:
                canvas.delete("all")
                youLost()
                
            #_____________________________MANAGE THE DOOR______________________________________________
            elif array2D[nextRow][nextColumn] == 5:
                youWin()
            
                
            #_____________________________MANGE PLAYER_________________________________________________
            else:
                array2D[playerRow][playerColumn] = 0
                array2D[nextRow][nextColumn] = 6
            

    drawGrid()
#__________________________________FUNCTION FOR MOVERIGHT, MOVELEFT, MOVEUP , MOVEDOWN_________________
            
def moveRight(event):
    move('right')

def moveLeft(event):
    move('left')

def moveDown(event):
    move('down')

def moveUp(event):
    move('up')

#_____________________________________Sreymao____________________________________________________

#_____________________________________You Win____________________________________________________

def youWin() :
    global canvas,count
    canvas.delete("all")
    winsound.PlaySound("sound\\vanda.wav", winsound.SND_ASYNC | winsound.SND_ASYNC)
    canvas.create_image(700,400,image = winner_img)
    my_text=canvas.create_text(700, 300, text="🙌You Won!!!🙌", font=("pursor", 50), tags="id")
    canvas.itemconfig(my_text)
    canvas.create_text(700,400, text="🤗Totel Of Score:"+str(count),font=('Arial', 20))  
    print('You win')

#_____________________________________You Lost__________________________________________________
def youLost() :
    global canvas
    canvas.delete("all")
    canvas.create_image(700,300,image = lost_img)
    my_text=canvas.create_text(700, 300, text="☹GameOver!!", font=("pursor", 50), tags="id",fill="#ffffff")
    canvas.itemconfig(my_text)
    winsound.PlaySound("sound\\gameover.wav", winsound.SND_ASYNC | winsound.SND_ASYNC)
    print(youLost)

#____________________________________Move Position Player_______________________________________

root.bind("<Right>", moveRight)
root.bind("<Left>", moveLeft)
root.bind("<Up>", moveUp)
root.bind("<Down>", moveDown)

#__________________________________Pack to show windows_________________________________________

canvas.pack(expand=True, fill='both')
frame.pack(expand=True, fill='both')
root.mainloop()

