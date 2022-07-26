from tkinter import *

def click(event):
    global scvalue
    text = event.widget.cget('text')
    if text == '=':
        if scvalue.get().isdigit():
            value = int(scvalue.get())
        else:
            try:
                value = eval(scvalue.get())
            except Exception as e:
                print(e)
                value='Error'
                screen.update()
        scvalue.set(value)
        screen.update()
    elif text == 'C':
        scvalue.set("")
        screen.update()
    else:
        scvalue.set(scvalue.get() + text)
        screen.update()
    
root = Tk()
root.geometry("644x970")
root.title("Calculator made by Ankush Mallick")
root.wm_iconbitmap("1.ico")

scvalue = StringVar()
scvalue.set("")
screen = Entry(root, textvar=scvalue, font="lucida 30 bold")
screen.pack(fill=X, ipadx=8, pady=10, padx=10)

f = Frame(root, bg="grey")
b = Button(f, text="9", padx=28, pady=18, font="lucida 20 bold")
b.pack(side=LEFT, padx=18, pady=5)
b.bind("<Button-1>", click)

b = Button(f, text="8", padx=28, pady=18, font="lucida 20 bold")
b.pack(side=LEFT, padx=18, pady=5)
b.bind("<Button-1>", click)

b = Button(f, text="7", padx=28, pady=18, font="lucida 20 bold")
b.pack(side=LEFT, padx=18, pady=5)
b.bind("<Button-1>", click)

f.pack()

f1 = Frame(root, bg="grey")
b = Button(f1, text="6", padx=28, pady=18, font="lucida 20 bold")
b.pack(side=LEFT, padx=18, pady=5)
b.bind("<Button-1>", click)

b = Button(f1, text="5", padx=28, pady=18, font="lucida 20 bold")
b.pack(side=LEFT, padx=18, pady=5)
b.bind("<Button-1>", click)

b = Button(f1, text="4", padx=28, pady=18, font="lucida 20 bold")
b.pack(side=LEFT, padx=18, pady=5)
b.bind("<Button-1>", click)

f1.pack()

f2 = Frame(root, bg="grey")
b = Button(f2, text="3", padx=28, pady=18, font="lucida 20 bold")
b.pack(side=LEFT, padx=18, pady=5)
b.bind("<Button-1>", click)

b = Button(f2, text="2", padx=28, pady=18, font="lucida 20 bold")
b.pack(side=LEFT, padx=18, pady=5)
b.bind("<Button-1>", click)

b = Button(f2, text="1", padx=28, pady=18, font="lucida 20 bold")
b.pack(side=LEFT, padx=18, pady=5)
b.bind("<Button-1>", click)

f2.pack()

f3 = Frame(root, bg="grey")
b = Button(f3, text="0", padx=28, pady=18, font="lucida 19 bold")
b.pack(side=LEFT, padx=18, pady=5)
b.bind("<Button-1>", click)

b = Button(f3, text="C", padx=28, pady=18, font="lucida 19 bold")
b.pack(side=LEFT, padx=18, pady=5)
b.bind("<Button-1>", click)

b = Button(f3, text="=", padx=28, pady=18, font="lucida 19 bold")
b.pack(side=LEFT, padx=18, pady=5)
b.bind("<Button-1>", click)

f3.pack()

f4 = Frame(root, bg="grey")
b = Button(f4, text="+", padx=28, pady=18, font="lucida 20 bold")
b.pack(side=LEFT, padx=18, pady=5)
b.bind("<Button-1>", click)

b = Button(f4, text="-", padx=28, pady=18, font="lucida 20 bold")
b.pack(side=LEFT, padx=18, pady=5)
b.bind("<Button-1>", click)

b = Button(f4, text="*", padx=28, pady=18, font="lucida 20 bold")
b.pack(side=LEFT, padx=18, pady=5)
b.bind("<Button-1>", click)

f4.pack()

f5 = Frame(root, bg="grey")
b = Button(f5, text="/", padx=28, pady=18, font="lucida 20 bold")
b.pack(side=LEFT, padx=18, pady=5)
b.bind("<Button-1>", click)

b = Button(f5, text="%", padx=28, pady=18, font="lucida 20 bold")
b.pack(side=LEFT, padx=18, pady=5)
b.bind("<Button-1>", click)

b = Button(f5, text=".", padx=28, pady=18, font="lucida 20 bold")
b.pack(side=LEFT, padx=18, pady=5)
b.bind("<Button-1>", click)

f5.pack()
root.mainloop()
