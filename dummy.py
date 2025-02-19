from tkinter import Tk, Canvas, PhotoImage, mainloop
from math import sin

WIDTH, HEIGHT = 600, 600

window = Tk()
canvas = Canvas(window, width=WIDTH, height=HEIGHT, bg="#000000")
canvas.pack()
img = PhotoImage(width=WIDTH, height=HEIGHT)
canvas.create_image((WIDTH/2, HEIGHT/2), image=img, state="normal")
x = 300
y = 300
img.put("#ffffff", (x,y))

mainloop()
