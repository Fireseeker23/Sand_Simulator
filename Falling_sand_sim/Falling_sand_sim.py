import tkinter as tk
import time
from threading import Thread


board = [[0 for _ in range(10)] for _ in range(10)]


def setup_board(root):
    label_grid = []
    for i in range(10):
        row = []
        for j in range(10):
            label = tk.Label(root, text='', width=8, height=3, borderwidth=0, relief="flat")
            label.grid(row=i, column=j)
            label.bind("<Button-1>", lambda event, x=i, y=j: start_animation(x, y))  #left_click
            row.append(label)
        label_grid.append(row)
    return label_grid


def update_display(label_grid):
    for i in range(10):
        for j in range(10):
            if board[i][j] == 1:
                label_grid[i][j].config(bg="yellow")  
            else:
                label_grid[i][j].config(bg="white") 
    root.update_idletasks()


def start_animation(index_r, index_c):
    if board[index_r][index_c] == 0:  
        board[index_r][index_c] = 1
        update_display(label_grid)
        Thread(target=animator, args=(index_r, index_c)).start()  


def animator(index_r, index_c):
    while True:
        if index_r == 9 or board[index_r + 1][index_c] == 1:
            break 
        else:
            board[index_r][index_c] = 0
            board[index_r + 1][index_c] = 1
            index_r += 1
            update_display(label_grid)
            time.sleep(0.05)  


root = tk.Tk()
root.title("Falling Sand Simulation")


label_grid = setup_board(root)

root.mainloop()
