import tkinter as tk
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
            [1, 0, 1, 6, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 1],
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
            [1, 0, 1, 2, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 2, 0, 2, 0, 2, 0, 0, 0, 0, 0, 5, 1, 0, 1],
            [1, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 1],
            [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
            [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1]
    ]

#___________________________________Background Image_____________________________________
bg_img = tk.PhotoImage(file="images/bg.png")
canvas.create_image(600, 370, image=bg_img)

#____________________________________User Image__________________________________________

mario_img = tk.PhotoImage(file="images/mario1.png")
#_____________________________________Images______________________________________________
wall_img = tk.PhotoImage(file="images/box.png")
coin_img = tk.PhotoImage(file="images/coin.png")
home_img = tk.PhotoImage(file="images/door.png")
fire_img = tk.PhotoImage(file="images/red.png")
winner_img = tk.PhotoImage(file="images/won.png")
lost_img = tk.PhotoImage(file="images/lost .png")

#_____________________________________Enemy image________________________________________________

enemy_img = tk.PhotoImage(file="images/monster.png")

#____________________________________Sound________________________________________________________
winsound.PlaySound("sound/start.wav",winsound.SND_FILENAME | winsound.SND_ASYNC )

# ___________________________________getIndex___________________________________________________
#____________________________________Theara_______________________________________________________
count =0
def getIndexOfscore():
    index = 0
    for row in range(len(array2D)):
        for col in range(len(array2D[row])):
            if array2D[row][col] == 6:
                index = (row,col)
    return index
# ______________________________________SUM OF SCORE______________________________________________
def sumOfscore():
    global count
    index = getIndexOfscore()
    if array2D[index[0]][index[1]+1]==2 or array2D[index[0]][index[1]-1]==2 or array2D[index[0]+1][index[1]]==2 or array2D[index[0]-1][index[1]]==2: 
        winsound.PlaySound("sound\\coin.wav", winsound.SND_ASYNC | winsound.SND_ASYNC)
        count += 10
    return count 
#_____________________________________Graphic of array2D__________________________________________
def drawGrid():
    global array2D,count,coin,sumOfscore
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
    canvas.create_text(150,50, text="Your score: "+str(sumOfscore()),font=('Arial', 20))  
drawGrid()

#__________________________________Move position of  user____________________________________________________ 

#_________________________________Theara_____________________________________________________________________

# _________________________________Move Right________________________________________________________________  
def getIndex(array2D):
     for row in range(len(array2D)):
          for col in range(len(array2D[row])):
               if array2D[row][col] == 6:
                    postion=[row, col]
     return postion
    
def moveRight(event):
    position = getIndex(array2D)
    row = position[0]
    col = position[1]
    if array2D[row][col+1] != 3 and array2D[row][col+1] != 4:
        if array2D[row][col+1] == 2:
            array2D[row][col] = 0
            array2D[row][col+1] = 6
            sumOfscore()
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
    canvas.create_image(600, 370, image=bg_img)
    drawGrid()
    
# ______________________________Move Left______________________________________

def moveLeft(event):
    position = getIndex(array2D)
    row = position[0]
    col = position[1]
    if array2D[row][col-1] != 3 and array2D[row][col-1] != 4:
        if array2D[row][col-1] == 2:
            array2D[row][col] = 0
            array2D[row][col-1] = 6
            sumOfscore()
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
    canvas.create_image(600, 370, image=bg_img)
    drawGrid()

#________________________________Sreymao___________________________________________________
#_________________________________Move Up__________________________________________________

def moveUp(event):
    position = getIndex(array2D)
    row = position[0]
    col = position[1]
    if array2D[row-1][col] != 3 and array2D[row-1][col] != 4:
        if array2D[row-1][col] == 2:
            array2D[row][col] = 0
            array2D[row-1][col] = 6
            sumOfscore()
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
    canvas.create_image(600, 370, image=bg_img)
    drawGrid()
    
# _______________________________Move Down______________________________________   

def moveDown(event):
    position = getIndex(array2D)
    row = position[0]
    col = position[1]
    if array2D[row+1][col] != 3 and array2D[row+1][col] != 4:
        if array2D[row+1][col] == 2:
            array2D[row][col] = 0
            array2D[row+1][col] = 6
            sumOfscore()
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
    canvas.create_image(600, 370, image=bg_img)
    drawGrid()

#____________________________________Move Monster________________________________________________
moveMonster = []
def moveMonster(array2D):
    monster = []
    for row in range(len(array2D)):
        for col in range(len(array2D[row])):
            if array2D[row][col] == 3:
                monster.append([row,col])
    print(monster)
    return monster
    
def moveMonsterInGrid(array2D, right, col):
    move = []
    if (array2D[right][col-1] == 0):
        move.append("Left")
    elif (array2D[right][col+1] == 0):
        move.append("Right")
    elif (array2D[right-1][col] == 0):
        move.append("Up")
    elif (array2D[right+1][col] == 0):
        move.append("Down")
    return move

def canMoveMonster():
    global array2D
    getindexMonster = moveMonster(array2D)
    print(getindexMonster)
    for enemy in getindexMonster:
        row = enemy[0]
        col = enemy[1]
        # print(row, col)
        monsters = moveMonsterInGrid(array2D, row, col)
        # print(monsters)
        
        if len(monsters) > 3:
            move = random.choice(monsters)
            print(move)
         
        if move == "Left":
            if array2D[row][col-1] == 0 and array2D[row][col] != 6:
                array2D[row][col] == 0
                array2D[row][col-1] == 3
                
        if move == "Right":      
            if array2D[row][col+1] == 0 and array2D[row][col+1] != 6:
                array2D[row][col] == 0
                array2D[row][col+1] == 3
        
        if move == "Up":        
            if array2D[row-1][col] == 0 and array2D[row-1][col] != 6:
                array2D[row][col] == 0
                array2D[row-1][col] == 3
        
        if move == "Down":       
            if array2D[row+1][col] == 0 and array2D[row+1][col] != 6:
                array2D[row][col] == 0
                array2D[row+1][col] == 3
    drawGrid()
    canvas.after(50, canMoveMonster)
canvas.after(50, canMoveMonster)
# canvas.delete("all")
drawGrid()
    
  

#_____________________________________You won or You Lost________________________________________

#_____________________________________Sreymao____________________________________________________

#_____________________________________You Win____________________________________________________
def youWin() :
    global canvas
    canvas.create_image(700,400,image = winner_img)
    my_text=canvas.create_text(700, 300, text="🙌You Won!!!🙌", font=("pursor", 50), tags="id")
    canvas.itemconfig(my_text)
    canvas.create_text(700,400, text="🤗Totel Of Score:"+str(sumOfscore()),font=('Arial', 20))  
    winsound.PlaySound("sound\\vanda.wav", winsound.SND_ASYNC | winsound.SND_ASYNC)
    canvas = root.geometry("1600x680")  
    print('You win')

#_____________________________________You Lost__________________________________________________
def youLost() :
    global canvas
    canvas.create_image(700,300,image = lost_img)
    my_text=canvas.create_text(700, 300, text="You LOST!!", font=("pursor", 50), tags="id")
    canvas.itemconfig(my_text)
    winsound.PlaySound("sound\\gameover.wav", winsound.SND_ASYNC | winsound.SND_ASYNC)
    canvas= root.geometry("1600x680")

#____________________________________Move Position Player_______________________________________

root.bind("<Right>", moveRight)
root.bind("<Left>", moveLeft)
root.bind("<Up>", moveUp)
root.bind("<Down>", moveDown)

#__________________________________Pack to show windows_________________________________________

canvas.pack(expand=True, fill='both')
frame.pack(expand=True, fill='both')
root.mainloop()

