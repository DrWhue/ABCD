from tkinter import *

root = Tk()

# testing out buttons for funs
"""
topFrame = Frame(root)
topFrame.pack()
bottomFrame = Frame(root)
bottomFrame.pack(side = BOTTOM)

button1 = Button(topFrame, text = "buttom1", fg = "red")
button2 = Button(topFrame, text = "buttom2", fg = "blue")
button3 = Button(topFrame, text = "buttom3", fg = "green")
button4 = Button(bottomFrame, text = "buttom4", fg = "purple")

button1.pack(side = LEFT)
button2.pack(side = LEFT)
button3.pack(side = LEFT)
button4.pack(side = BOTTOM)
"""

# implenting widgets and COLOR WORKS
"""
one = Label(root, text = "1", bg = "red", fg = "white")
one.pack()
two = Label(root, text = "2", bg = "blue", fg = "black")
two.pack(fill = X)
three = Label(root, text = "3", bg = "purple", fg = "yellow")
three.pack(side = LEFT, fill = Y)
"""

# username and password
"""""
label_1 = Label(root, text = "Name")
label_2 = Label(root, text = "Password")
entry_1 = Entry(root)
entry_2 = Entry(root)

label_1.grid(row = 0)
label_2.grid(row = 1)

entry_1.grid(row = 0, column = 1)
entry_2.grid(row = 1, column = 1)
"""

# more on username and password
"""""
label_1 = Label(root, text = "Name")
label_2 = Label(root, text = "Password")
entry_1 = Entry(root)
entry_2 = Entry(root)

label_1.grid(row = 0, sticky = E)
label_2.grid(row = 1, sticky = E)

entry_1.grid(row = 0, column = 1)
entry_2.grid(row = 1, column = 1)

c = Checkbutton(root, text = "Keep me logged in")
c.grid(columnspan =2)
"""

# using classes (quit button testing)
"""""
class buttons:
    def __init__(self, master):
        frame = Frame(master)
        frame.pack()

        self.quitButton = Button(frame, text = "Quit", command = frame.quit)
        self.quitButton.pack(side = LEFT)

b = buttons(root)
"""

# shapes and graphics
"""""
canvas = Canvas(root, width = 200, height = 100)
canvas.pack()

blackLine = canvas.create_line(0, 0, 200, 50)
redLine = canvas.create_line(0, 100, 200, 50, fill = "red")C
greenBox = canvas.create_rectangle(25, 25, 130, 60, fill = "green")
"""

# images and icons (IMPORTANT)

from PIL import Image, ImageTk

image = Image.open("Cells.jpg")
photo = ImageTk.PhotoImage(image)

label = Label(image = photo)
label.pack()


root.mainloop()
