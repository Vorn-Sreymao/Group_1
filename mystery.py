import tkinter as tk
from tkinter import font
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
            [1, 0, 1, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 1],
            [1, 0, 1, 0, 1, 3, 0, 0, 0, 0, 0, 0, 2, 0, 0, 0, 0, 1, 0, 1, 0, 0, 0, 0, 0, 0, 1, 0, 0, 1, 0, 0, 0, 0, 4, 0, 0, 0, 0, 0, 0, 0, 1, 0, 1],
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
            [1, 0, 1, 2, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 2, 0, 2, 0, 2, 6, 0, 0, 0, 0, 5, 1, 0, 1],
            [1, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 1],
            [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
            [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1]
    ]


# _____________________________________________varible______________________________________
count = 0
#_____________________________________Images______________________________________________
enemy_img = tk.PhotoImage(file="images/monster.png")
bgimg = tk.PhotoImage(file="images/bg.png")
mario_img = tk.PhotoImage(file="images/mario1.png")
wall_img = tk.PhotoImage(file="images/box.png")
coin_img = tk.PhotoImage(file="images/coin.png")
home_img = tk.PhotoImage(file="images/door.png")
fire_img = tk.PhotoImage(file="images/red.png")
winner_img = tk.PhotoImage(file="images/won.png")
lost_img = tk.PhotoImage(file="images/lost .png")
#____________________________________Sound________________________________________________________
winsound.PlaySound("sound/start.wav",winsound.SND_FILENAME | winsound.SND_ASYNC )

#____________________________________Theara_______________________________________________________

#_____________________________________Graphic of array2D__________________________________________
def drawGrid():
    global array2D,count,buttonPlay
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
    
def moveRight(event):
    global array2D,count
    winsound.PlaySound("sound\\run.wav", winsound.SND_ASYNC | winsound.SND_ASYNC)
    position = getIndex(array2D)
    row = position[0]
    col = position[1]
    if array2D[row][col+1] != 3 and array2D[row][col+1] != 4:
        if array2D[row][col+1] == 2:
            array2D[row][col] = 0
            array2D[row][col+1] = 6
            winsound.PlaySound("sound\\getCoin.wav", winsound.SND_ASYNC | winsound.SND_ASYNC)
            count += 10
        elif array2D[row][col+1] == 5:
            canvas.delete("all")
            youWin()
            array2D[row][col] = 0
            array2D[row][col+1] = 6
        elif array2D[row][col+1]!= 1:
            array2D[row][col]= 0
            array2D[row][col+1]=6
            canvas.delete("all")
    if array2D[row][col+1] == 3:
        canvas.delete("all")
        array2D[row][col] = 0
        array2D[row][col+1] = 6
        youLost()
    canvas.create_image(600, 370, image=bgimg)
    drawGrid()
    
# ______________________________Move Left______________________________________

def moveLeft(event):
    global count
    winsound.PlaySound("sound\\run.wav", winsound.SND_ASYNC | winsound.SND_ASYNC)
    position = getIndex(array2D)
    row = position[0]
    col = position[1]
    if array2D[row][col-1] != 3 and array2D[row][col-1] != 4:
        if array2D[row][col-1] == 2:
            array2D[row][col] = 0
            array2D[row][col-1] = 6
            winsound.PlaySound("sound\\getCoin.wav", winsound.SND_ASYNC | winsound.SND_ASYNC)
            count += 10
        elif array2D[row][col-1] == 5:
            canvas.delete("all")
            youWin()
            array2D[row][col] = 0
            array2D[row][col-1] = 6
        elif array2D[row][col-1]!= 1:
            array2D[row][col]= 0
            array2D[row][col-1]=6
            canvas.delete("all")
    if array2D[row][col-1] == 3:
        canvas.delete("all")
        array2D[row][col] = 0
        array2D[row][col-1] = 6
        youLost()
    canvas.create_image(600, 370, image=bgimg)
    drawGrid()

#________________________________Sreymao___________________________________________________
#_________________________________Move Up__________________________________________________

def moveUp(event):
    global count
    winsound.PlaySound("sound\\run.wav", winsound.SND_ASYNC | winsound.SND_ASYNC)
    position = getIndex(array2D)
    row = position[0]
    col = position[1]
    if array2D[row-1][col] != 3 and array2D[row-1][col] != 4:
        if array2D[row-1][col] == 2:
            array2D[row][col] = 0
            array2D[row-1][col] = 6
            winsound.PlaySound("sound\\getCoin.wav", winsound.SND_ASYNC | winsound.SND_ASYNC)
            count += 10
        elif array2D[row-1][col] == 5:
            canvas.delete("all")
            youWin()
            array2D[row][col] = 0
            array2D[row-1][col] = 6
        elif array2D[row-1][col]!= 1:
            array2D[row][col]= 0
            array2D[row-1][col]=6
            canvas.delete("all")
    if array2D[row-1][col] == 3:
        canvas.delete("all")
        array2D[row][col] = 0
        array2D[row-1][col] = 6
        youLost()
    canvas.create_image(600, 370, image=bgimg)
    drawGrid()
    
# _______________________________Move Down______________________________________   

def moveDown(event):
    global count
    winsound.PlaySound("sound\\run.wav", winsound.SND_ASYNC | winsound.SND_ASYNC)
    position = getIndex(array2D)
    row = position[0]
    col = position[1]
    if array2D[row+1][col] != 3 and array2D[row+1][col] != 4:
        if array2D[row+1][col] == 2:
            array2D[row][col] = 0
            array2D[row+1][col] = 6
            winsound.PlaySound("sound\\getCoin.wav", winsound.SND_ASYNC | winsound.SND_ASYNC)
            count += 10
        elif array2D[row+1][col] == 5:
            canvas.delete("all")
            youWin()
            array2D[row][col] = 0
            array2D[row+1][col] = 6
        elif array2D[row+1][col]!= 1:
            array2D[row][col]= 0
            array2D[row+1][col]=6
            canvas.delete("all")
    if array2D[row+1][col] == 3:
        canvas.delete("all")
        array2D[row][col] = 0
        array2D[row+1][col] = 6
        youLost()
    canvas.create_image(600, 370, image=bgimg)
    drawGrid()

#____________________________________Move Monster On Position____________________________________
def monster_Position():
    global array2D
    for row in range(len(array2D)):
        for col in range(len(array2D[row])):
            if array2D[row][col] == 3:
                position = [row, col]
    return position

def monster_Move_Position():
    global monster_Position, moveRight, moveLeft, youWin, youLost
    if not youWin and not youLost:
        canvas.delete("all")
        monsterOfPosition = monster_Position(array2D)
        row = monsterOfPosition[0]
        col = monsterOfPosition[1]
        if array2D[row][col+1] == 1:
            moveRight = False
        elif array2D[row][col-1] == 1:
            moveLeft = True
            
        if (col+1) < len(array2D[0]) and array2D[row][col+1] != 1 and moveRight and array2D[row][col+1] == 3:
            array2D[row][col] = 0
            array2D[row][col+1] == array2D
            
        if (col+1) < len(array2D[0]) and array2D[row][col-1] != 1 and moveRight and array2D[row][col-1] == 3:
            array2D[row][col] = 0
            array2D[row][col-1] == array2D
    
    drawGrid()
    canvas.after(50, monster_Move_Position)       
            
#_____________________________________Sreymao____________________________________________________

#_____________________________________You Win____________________________________________________

def youWin() :
    global canvas,count
    winsound.PlaySound("sound\\vanda.wav", winsound.SND_ASYNC | winsound.SND_ASYNC)
    canvas.create_image(700,400,image = winner_img)
    my_text=canvas.create_text(700, 300, text="🙌You Won!!!🙌", font=("pursor", 50), tags="id")
    canvas.itemconfig(my_text)
    canvas.create_text(700,400, text="🤗Totel Of Score:"+str(count),font=('Arial', 20))  
    canvas = root.geometry("1600x680")  
    print('You win')

#_____________________________________You Lost__________________________________________________
def youLost() :
    global canvas
    canvas.create_image(700,300,image = lost_img)
    my_text=canvas.create_text(700, 300, text="☹GameOver!!", font=("pursor", 50), tags="id",fill="#ffffff")
    canvas.itemconfig(my_text)
    winsound.PlaySound("sound\\gameover.wav", winsound.SND_ASYNC | winsound.SND_ASYNC)

#____________________________________Move Position Player_______________________________________

root.bind("<Right>", moveRight)
root.bind("<Left>", moveLeft)
root.bind("<Up>", moveUp)
root.bind("<Down>", moveDown)

#__________________________________Pack to show windows_________________________________________

canvas.pack(expand=True, fill='both')
frame.pack(expand=True, fill='both')
root.mainloop()

