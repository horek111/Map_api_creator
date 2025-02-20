import tkinter

height = 600
wight = 600
master = tkinter.Tk()
canvas = tkinter.Canvas(master, bg="white", height=height, wight=wight)
canvas.pack()
delta = 600 / 8
color = "red"
for i in range(1, 9):
    canvas.create_line((delta * i, 0), (delta * i, height), fill="black")
    canvas.create_line((0, delta * i), (wight, delta * i), fill="black")
    ost = 0
    if i == 4 or i ==5:
        color = "blue"
    else:
        for j in range(0, 8):
            if i % 2 == 0:
                ost = 1 if ost == 0 else 1
            if j % 2 == ost:
                canvas.create_oval((delta * i - delta, delta * i - delta), (delta * i - delta, delta * i - delta))






master.mainloop()