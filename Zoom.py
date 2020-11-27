import pyautogui as pag
import subprocess
import time
import csv
import tkinter as tk
from tkinter import *

def join():
    print("Opening Zoom...")
    subprocess.Popen(str(zum), shell=True)
    time.sleep(3)

    print("Joining Zoom...")
    join1 = pag.locateCenterOnScreen('join.jpg', confidence=.8)
    pag.click(join1)
    time.sleep(.5)

    pag.typewrite(Mid)
    join2 = pag.locateCenterOnScreen('join2.jpg', confidence=.8)
    pag.click(join2)
    time.sleep(3)
    pag.typewrite(Pas)

    join3 = pag.locateCenterOnScreen('join3.jpg', confidence=.8)
    pag.click(join3)
    time.sleep(5)
    novid = pag.locateCenterOnScreen('join4.jpg', confidence=.8)
    pag.click(novid)

    print("Joined")

def read():
    data = csv.reader(open('link_kelas.csv', 'r'))
    global clength, mid, pas, clas, rlength, zum

    mid = []
    pas = []
    clas = []
    rlength = 0

    for row in data:
        clength = len(row)
        mid.append(row[0])
        pas.append(row[1])
        clas.append(row[2])
        rlength += 1

    dir = open("zoomdir.txt", "r")
    zum = dir.readline()
    print(zum)

def select(x):
    global Mid, Pas
    Mid = mid[x]
    print("Meeting ID:", Mid)
    Pas = pas[x]
    print("Password:", Pas)

def display():
    window = Tk()
    #window.geometry("400x600")
    window.title("ZOOM BOT")
    greet = tk.Label(
        text="SELECT CLASS",
        width = 20, height = 5)
    greet.pack(side=tk.LEFT)

    for i in range(1, rlength):
        button = tk.Button(
            text=(clas[i]),
            width=20, height=5, bg="red", fg="white",
            command=lambda i=i:[select(i), window.destroy()])
        button.pack(padx=5, pady=5)

    window.mainloop()

read()
display()

print("\nClass Selected\n")
join()


print("done")