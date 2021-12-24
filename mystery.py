import tkinter as tk
# import winsound
# import random
# from tkinter.constants import NW, W
root = tk.Tk()
root.geometry("1600x700")
frame = tk.Frame()
frame.master.title("Python VC1")
canvas = tk.Canvas(frame)
#hello 
#________________________________________Array2D Of Grid(Sreymao and Theara)_______________________________________
array2D = [
            [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
            [1, 0, 0, 0, 0, 0, 2, 2, 2, 2, 2, 0, 0, 0, 0, 0, 0, 0, 0, 0, 2, 2, 2, 2, 2, 0, 0, 0, 0, 0, 0, 0, 0, 2, 2, 2, 2, 2, 0, 0, 0, 0, 0, 0, 1],
            [1, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 1],
            [1, 0, 1, 0, 0, 2, 0, 2, 0, 2, 0, 2, 0, 0, 3, 1, 0, 1, 3, 0, 0, 0, 2, 0, 2, 0, 0, 0, 0, 1, 3, 0, 0, 2, 0, 2, 0, 2, 0, 2, 0, 0, 1, 0, 1],
            [1, 0, 1, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 1, 0, 1, 1, 1, 1, 1, 1, 1, 1, 0, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 1, 0, 1],
            [1, 0, 1, 0, 1, 3, 0, 0, 0, 0, 0, 0, 2, 0, 0, 0, 0, 1, 0, 1, 0, 0, 0, 0, 0, 0, 1, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 1],
            [1, 0, 1, 0, 1, 1, 1, 1, 0, 0, 0, 2, 0, 2, 0, 0, 0, 1, 2, 1, 0, 0, 0, 2, 0, 0, 1, 4, 0, 1, 1, 1, 1, 0, 1, 1, 1, 1, 1, 1, 1, 0, 1, 0, 1],
            [1, 0, 1, 0, 0, 0, 0, 1, 0, 0, 0, 0, 2, 0, 0, 0, 0, 1, 0, 1, 0, 0, 2, 0, 2, 0, 1, 1, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 3, 1, 0, 1, 0, 1],
            [1, 0, 1, 0, 4, 0, 0, 1, 0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 0, 1, 0, 0, 0, 2, 0, 0, 0, 0, 0, 0, 2, 0, 1, 0, 2, 0, 0, 1, 1, 1, 1, 0, 1, 0, 1],
            [1, 0, 1, 0, 1, 2, 0, 1, 0, 0, 2, 0, 0, 1, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 2, 0, 0, 1, 2, 0, 1, 2, 0, 2, 0, 1, 0, 2, 0, 0, 1, 0, 1],
            [1, 2, 1, 0, 1, 0, 0, 1, 0, 2, 0, 2, 0, 1, 0, 1, 1, 1, 1, 1, 0, 0, 0, 0, 0, 2, 0, 2, 0, 1, 2, 0, 1, 0, 2, 0, 0, 1, 0, 2, 0, 0, 1, 2, 1],
            [1, 2, 1, 0, 1, 0, 0, 0, 0, 0, 2, 0, 0, 1, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 2, 0, 0, 0, 0, 0, 0, 1, 0, 2, 0, 0, 1, 2, 1],
            [1, 2, 1, 0, 1, 3, 0, 0, 0, 0, 0, 0, 0, 1, 0, 1, 0, 0, 0, 0, 2, 2, 2, 0, 0, 0, 4, 0, 0, 1, 0, 2, 2, 0, 0, 0, 0, 1, 0, 2, 0, 0, 1, 2, 1],
            [1, 2, 1, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 1, 0, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 2, 0, 0, 1, 2, 1],
            [1, 2, 1, 0, 0, 0, 2, 2, 2, 2, 0, 0, 2, 0, 0, 0, 0, 3, 1, 0, 0, 0, 2, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 2, 0, 0, 0, 0, 0, 0, 0, 1, 2, 1],
            [1, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 0, 2, 0, 2, 0, 0, 1, 0, 0, 1, 0, 0, 0, 2, 0, 2, 0, 0, 0, 0, 0, 0, 1, 0, 1],
            [1, 0, 1, 0, 0, 0, 2, 2, 2, 2, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 2, 0, 0, 0, 1, 0, 0, 1, 0, 0, 0, 0, 2, 0, 0, 0, 0, 0, 4, 0, 1, 0, 1],
            [1, 0, 1, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 1, 0, 1],
            [1, 0, 1, 0, 1, 0, 0, 0, 0, 0, 0, 0, 2, 2, 2, 2, 2, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 2, 2, 2, 2, 2, 0, 0, 0, 1, 0, 1, 0, 1],
            [1, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 5, 0, 0, 0, 0, 1, 0, 1],
            [1, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 1],
            [1, 6, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 3, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
            [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1]
    ]
#____________________________________User Image__________________________________________

mario_img = tk.PhotoImage(file="images/mario.png")

#_____________________________________Images______________________________________________
wall_img = tk.PhotoImage(file="images/box.png")
coin_img = tk.PhotoImage(file="images/coin.png")
home_img = tk.PhotoImage(file="images/home.png")
fire_img = tk.PhotoImage(file="images/red.png")
#_____________________________________Enemy image_________________________________________

enemy_img = tk.PhotoImage(file="images/ufo.png")

#_____________________________________Graphic of array2D__________________________________________
def drawGrid():
    global array2D
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

            elif array2D[row][col] == 6:
                canvas.create_image(15+(30*col),15+(30*row),image = mario_img)
drawGrid()

#__________________________________Move user____________________________________________________
def moveUp(event):
    global array2D
    canvas.delete("all")
    isTrue = True
    for row in range(len(array2D)):
        for col in range(len(array2D)):
            if array2D[row][col] == 6 and row > 0 and isTrue:
                array2D[row][col] = 0
                array2D[row-1][col] = 6
                isTrue = False            

    canvas.create_image(15+(30*col),15+(30*row),image = mario_img)
    drawGrid()

# ----------------------------------Move Down--------------------------------    

def moveDown(event):
    global array2D
    canvas.delete("all")
    isTrue = True
    for row in range(len(array2D)):
        for col in range(len(array2D)):
            if array2D[row][col] == 6 and row < len(array2D) - 1 and isTrue:
                array2D[row][col] = 0
                array2D[row+1][col] = 6
                isTrue = False
                
    canvas.create_image(15+(30*col),15+(30*row),image = mario_img)
    drawGrid()
#sreymao
# ---------------------------------Move RIGHT-----------------------------------

def moveLeft(event):
    global array2D
    canvas.delete("all")
    isTrue = True
    for row in range(len(array2D)):
        for col in range(len(array2D)):
            if array2D[row][col] == 6 and col > 0 and isTrue:
                array2D[row][col] = 0
                array2D[row][col-1] = 6
                isTrue = False        
    canvas.create_image(15+(30*col),15+(30*row),image = mario_img)
    drawGrid()

# ---------------------------------Move LEFT----------------------------------------

def moveRight(event):
    global array2D
    canvas.delete("all")
    isTrue = True
    for row in range(len(array2D)):
        for col in range(len(array2D)):
            if array2D[row][col] == 6 and col < len(array2D) - 1 and isTrue:
                array2D[row][col] = 0
                array2D[row][col+1] = 6
                isTrue = False
    drawGrid()
    

root.bind("<Right>", moveRight)
root.bind("<Left>", moveLeft)
root.bind("<Up>", moveUp)
root.bind("<Down>", moveDown)


canvas.pack(expand=True, fill='both')
frame.pack(expand=True, fill='both')
root.mainloop()