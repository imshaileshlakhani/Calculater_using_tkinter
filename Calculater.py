from tkinter import *

root = Tk()


def click(event):
    global scvalue
    text = event.widget.cget("text")
    if text == "=":
        if scvalue.get().isdigit():
            value = int(scvalue.get())
        else:
            try:
                value = eval(screen.get())
            except:
                value = "Error"
        scvalue.set(value)
        screen.update()
    elif text == "C":
        scvalue.set("")
        screen.update()
    else:
        scvalue.set(scvalue.get() + text)
        screen.update()


root.geometry("644x900")

scvalue = StringVar()
scvalue.set("")

screen = Entry(root, textvar=scvalue, font="lucida 40 bold")
screen.pack(fill=X, padx=10, pady=10, ipadx=8)
f = Frame(root, bg="grey")
b = Button(f, text="9", font="lucida 40 bold", padx=28, pady=5)
b.pack(side=LEFT, padx=18, pady=5)
b.bind("<Button-1>",click)
b = Button(f, text="8", font="lucida 40 bold", padx=28, pady=5)
b.pack(side=LEFT, padx=18, pady=5)
b.bind("<Button-1>",click)
b = Button(f, text="7", font="lucida 40 bold", padx=28, pady=5)
b.pack(side=LEFT, padx=18, pady=5)
b.bind("<Button-1>",click)
f.pack()

f1 = Frame(root, bg="grey")
b = Button(f1, text="6", font="lucida 40 bold", padx=28, pady=5)
b.pack(side=LEFT, padx=18, pady=5)
b.bind("<Button-1>",click)
b = Button(f1, text="5", font="lucida 40 bold", padx=28, pady=5)
b.pack(side=LEFT, padx=18, pady=5)
b.bind("<Button-1>",click)
b = Button(f1, text="4", font="lucida 40 bold", padx=28, pady=5)
b.pack(side=LEFT, padx=18, pady=5)
b.bind("<Button-1>",click)
f1.pack()

f2 = Frame(root, bg="grey")
b = Button(f2, text="3", font="lucida 40 bold", padx=28, pady=5)
b.pack(side=LEFT, padx=18, pady=5)
b.bind("<Button-1>",click)
b = Button(f2, text="2", font="lucida 40 bold", padx=28, pady=5)
b.pack(side=LEFT, padx=18, pady=5)
b.bind("<Button-1>",click)
b = Button(f2, text="1", font="lucida 40 bold", padx=28, pady=5)
b.pack(side=LEFT, padx=18, pady=5)
b.bind("<Button-1>",click)
f2.pack()

f3 = Frame(root, bg="grey")
b = Button(f3, text="0", font="lucida 40 bold", padx=28, pady=5)
b.pack(side=LEFT, padx=18, pady=5)
b.bind("<Button-1>",click)
b = Button(f3, text="-", font="lucida 40 bold", padx=34, pady=5)
b.pack(side=LEFT, padx=18, pady=5)
b.bind("<Button-1>",click)
b = Button(f3, text="*", font="lucida 40 bold", padx=31, pady=5)
b.pack(side=LEFT, padx=18, pady=5)
b.bind("<Button-1>",click)
f3.pack()

f4 = Frame(root, bg="grey")
b = Button(f4, text="%", font="lucida 40 bold", padx=19, pady=5)
b.pack(side=LEFT, padx=18, pady=5)
b.bind("<Button-1>",click)
b = Button(f4, text="/", font="lucida 40 bold", padx=36, pady=5)
b.pack(side=LEFT, padx=18, pady=5)
b.bind("<Button-1>",click)
b = Button(f4, text="+", font="lucida 40 bold", padx=26, pady=5)
b.pack(side=LEFT, padx=18, pady=5)
b.bind("<Button-1>",click)
f4.pack()

f5 = Frame(root, bg="grey")
b = Button(f5, text="=", font="lucida 40 bold", padx=27, pady=5)
b.pack(side=LEFT, padx=18, pady=5)
b.bind("<Button-1>",click)
b = Button(f5, text="C", font="lucida 40 bold", padx=25, pady=5)
b.pack(side=LEFT, padx=18, pady=5)
b.bind("<Button-1>",click)
b = Button(f5, text=".", font="lucida 43 bold", padx=31, pady=0)
b.pack(side=LEFT, padx=18, pady=5)
b.bind("<Button-1>",click)
f5.pack()


root.mainloop()