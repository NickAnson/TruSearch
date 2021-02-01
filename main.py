from tkinter import *
import tkinter as tk
import random


def linSearchGraph(nums, screen, canvas, size):
    start = 0
    for i in range(len(nums)):
        canvas.create_rectangle(start * (800 / size), 800 - nums[i], start * (800 / size) + (800 / size), 800,
                                fill='black')
        start = start + 1
    canvas.pack()
    screen.update()
    return


def linSearch(x, nums, screen, canvas, size):
    linSearchGraph(nums, screen, canvas, size)
    for i in range(len(nums)):
        graphUpdate(i, nums[i], x, screen, canvas, size)
        if nums[i] == x:  # item found, return the index value
            return i
    return -1  # loop finished, item was not in list


def windowSetup():
    screen = Tk()
    screen.title("Linear Search")
    screen.geometry("800x800")
    return screen


def graphUpdate(index, currentNum, finding, screen, canvas, size):
    if currentNum == finding:
        canvas.create_rectangle(index * (800 / size), 800 - currentNum, index * (800 / size) + 800 / size, 800,
                                fill='green')
    else:
        canvas.create_rectangle(index * (800 / size), 800 - currentNum, index * (800 / size) + 800 / size, 800,
                                fill='red')
    canvas.pack()
    screen.update()
    return


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    window = windowSetup()
    numToFind = 50

    numArray = random.sample(range(1, 500), 499)
    canvas = tk.Canvas(window, height=window.winfo_screenheight(), width=window.winfo_screenwidth())
    canvas.config(bg='white')
    canvas.create_text(90, 20, fill="darkblue", font="Times 20 italic bold",
                       text="Linear Search")

    # graphUpdate(a, window)
    linSearch(numToFind, numArray, window, canvas, len(numArray))

    window.mainloop()
