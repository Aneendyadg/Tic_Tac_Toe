from tkinter import *
import tkinter.messagebox
def whole_prog():
    global master
    master = Tk()
    master.title("Tic Tac Toe")
    global pa,plb,p1,p2,pl1,pl2,bcl,f
    pa = StringVar()
    plb = StringVar()
    p1 = StringVar()
    p2 = StringVar()
    pl1 = Entry(master, textvariable=p1, bd=5,bg='black',fg='white')
    pl1.grid(row=1, column=1, columnspan=7)
    pl2 = Entry(master, textvariable=p2, bd=5,bg='black',fg='white')
    pl2.grid(row=2, column=1, columnspan=7)
    bcl = True
    f = 0
    def reset_board(rest):
	    master.destroy()
	    whole_prog()
    def disbtn():
        btn1.configure(state=DISABLED)
        btn2.configure(state=DISABLED)
        btn3.configure(state=DISABLED)
        btn4.configure(state=DISABLED)
        btn5.configure(state=DISABLED)
        btn6.configure(state=DISABLED)
        btn7.configure(state=DISABLED)
        btn8.configure(state=DISABLED)
        btn9.configure(state=DISABLED)
    def clickonbtn(btns):
        global bcl, f, pl2, pl1, plb, pa
        if btns["text"] == " " and bcl == True:
           btns["text"] = "X"
           bcl = False
           plb = p2.get() + " is the WINNER!!!"
           pa = p1.get() + " is the WINNER!!!"
           wincheck()
           f += 1
        elif btns["text"] == " " and bcl == False:
           btns["text"] = "O"
           bcl = True
           wincheck()
           f += 1
        else:
           tkinter.messagebox.showinfo("Tic-Tac-Toe", "Cannot choose this")
    def wincheck():
        if (btn1['text'] == 'X' and btn2['text'] == 'X' and btn3['text'] == 'X' or
           btn4['text'] == 'X' and btn5['text'] == 'X' and btn6['text'] == 'X' or
           btn7['text'] =='X' and btn8['text'] == 'X' and btn9['text'] == 'X' or
           btn1['text'] == 'X' and btn5['text'] == 'X' and btn9['text'] == 'X' or
           btn3['text'] == 'X' and btn5['text'] == 'X' and btn7['text'] == 'X' or
           btn1['text'] == 'X' and btn2['text'] == 'X' and btn3['text'] == 'X' or
           btn1['text'] == 'X' and btn4['text'] == 'X' and btn7['text'] == 'X' or
           btn2['text'] == 'X' and btn5['text'] == 'X' and btn8['text'] == 'X' or
           btn7['text'] == 'X' and btn6['text'] == 'X' and btn9['text'] == 'X'):
           disbtn()
           tkinter.messagebox.showinfo("Tic-Tac-Toe", pa)
        elif(f == 8):
            tkinter.messagebox.showinfo("Tic-Tac-Toe", "Game is Draw")
        elif (btn1['text'] == 'O' and btn2['text'] == 'O' and btn3['text'] == 'O' or
             btn4['text'] == 'O' and btn5['text'] == 'O' and btn6['text'] == 'O' or
             btn7['text'] == 'O' and btn8['text'] == 'O' and btn9['text'] == 'O' or
             btn1['text'] == 'O' and btn5['text'] == 'O' and btn9['text'] == 'O' or
             btn3['text'] == 'O' and btn5['text'] == 'O' and btn7['text'] == 'O' or
             btn1['text'] == 'O' and btn2['text'] == 'O' and btn3['text'] == 'O' or
             btn1['text'] == 'O' and btn4['text'] == 'O' and btn7['text'] == 'O' or
             btn2['text'] == 'O' and btn5['text'] == 'O' and btn8['text'] == 'O' or
             btn7['text'] == 'O' and btn6['text'] == 'O' and btn9['text'] == 'O'):
            disbtn()
            tkinter.messagebox.showinfo("Tic-Tac-Toe", plb)
    btns = StringVar()
    lab1 = Label( master, text="Player 1:", font='Arial 15 bold', bg='white', fg='navy', height=1, width=7)
    lab1.grid(row=1, column=0)
    lab2 = Label( master, text="Player 2:", font='Arial 15 bold', bg='white', fg='navy', height=1, width=7)
    lab2.grid(row=2, column=0)
    btn1 = Button(master, text=" ", font='Arial 15 bold', bg='pink', fg='navy', height=5, width=8, cursor="hand1",command=lambda: clickonbtn(btn1))
    btn1.grid(row=4, column=0)
    btn2 = Button(master, text=' ', font='Arial 15 bold', bg='pink', fg='navy', height=5, width=8, cursor="hand1",command=lambda: clickonbtn(btn2))
    btn2.grid(row=4, column=1)
    btn3 = Button(master, text=' ',font='Arial 15 bold', bg='pink', fg='navy', height=5, width=8, cursor="hand1",command=lambda: clickonbtn(btn3))
    btn3.grid(row=4, column=2)
    btn4 = Button(master, text=' ', font='Arial 15 bold', bg='pink', fg='navy', height=5, width=8, cursor="hand1",command=lambda: clickonbtn(btn4))
    btn4.grid(row=5, column=0)
    btn5 = Button(master, text=' ', font='Arial 15 bold', bg='pink', fg='navy', height=5, width=8, cursor="hand1",command=lambda: clickonbtn(btn5))
    btn5.grid(row=5, column=1)
    btn6 = Button(master, text=' ', font='Arial 15 bold', bg='pink', fg='navy', height=5, width=8, cursor="hand1",command=lambda: clickonbtn(btn6))
    btn6.grid(row=5, column=2)
    btn7 = Button(master, text=' ', font='Arial 15 bold', bg='pink', fg='navy', height=5, width=8, cursor="hand1",command=lambda: clickonbtn(btn7))
    btn7.grid(row=6, column=0)
    btn8 = Button(master, text=' ', font='Arial 15 bold', bg='pink', fg='navy', height=5, width=8, cursor="hand1",command=lambda: clickonbtn(btn8))
    btn8.grid(row=6, column=1)
    btn9 = Button(master, text=' ', font='Arial 15 bold', bg='pink', fg='navy', height=5, width=8, cursor="hand1",command=lambda: clickonbtn(btn9))
    btn9.grid(row=6, column=2)
    reset_b= Button(master, text="RESTART GAME", bg='gray', fg='black',font="Arial 8 bold", height=1, width=12, cursor="hand1",command=lambda: reset_board(reset_b))
    reset_b.grid(row=3, column=0)
    master.mainloop()
whole_prog()
    
