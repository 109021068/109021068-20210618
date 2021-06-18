from tkinter import *
import hashlib

s256 = hashlib.sha256()

def login ():
    idData = entryID.get()
    pwData = entryPW.get()
    if len(idData) > 0 and len(pwData) > 0:
        s256.update(pwData.encode("utf-8"))
        pwHash = s256.hexdigest()
        #print(pwHash)
        if idData == "csie" and pwHash == "5515f0912ec4ca5c9537a9c29ed62372869e0f2332c58eb312bd7ca7de850456":
            #pwData == "h3041723"
            root.deiconify()
            top.destroy()
        else:
            entryID.delete (0, "end")
            entryPW.delete (0, "end")
    else:
        entryID.delete (0, "end")
        entryPW.delete (0, "end")


def exitProgram():
    top.destroy()
    root.destroy()

flag = True

def setBtnText(num):
    global flag
    if num == 0 and btn0.cget('text') == "":
        if flag:
            btn0.config(text="O")
        else:
            btn0.config(text="X")
        #btn0.config(state=DISABLED)
    elif num == 1 and btn1.cget('text') == "":
        if flag:
            btn1.config(text="O")
        else:
            btn1.config(text="X")
        #btn1.config(state=DISABLED)
    elif num == 2 and btn2.cget('text') == "":
        if flag:
            btn2.config(text="O")
        else:
            btn2.config(text="X")
        #btn2.config(state=DISABLED)
    elif num == 3 and btn3.cget('text') == "":
        if flag:
            btn3.config(text="O")
        else:
            btn3.config(text="X")
        #btn3.config(state=DISABLED)
    elif num == 4 and btn4.cget('text') == "":
        if flag:
            btn4.config(text="O")
        else:
            btn4.config(text="X")
        #btn4.config(state=DISABLED)
    elif num == 5 and btn5.cget('text') == "":
        if flag:
            btn5.config(text="O")
        else:
            btn5.config(text="X")
        #btn5.config(state=DISABLED)
    elif num == 6 and btn6.cget('text') == "":
        if flag:
            btn6.config(text="O")
        else:
            btn6.config(text="X")
        #btn6.config(state=DISABLED)
    elif num == 7 and btn7.cget('text') == "":
        if flag:
            btn7.config(text="O")
        else:
            btn7.config(text="X")
        #btn7.config(state=DISABLED)
    elif num == 8 and btn8.cget('text') == "":
        if flag:
            btn8.config(text="O")
        else:
            btn8.config(text="X")
        #btn8.config(state=DISABLED)
    flag = not flag

    if btn0.cget('text') == btn1.cget('text') and btn0.cget('text') == btn2.cget('text'):
        if btn0.cget('text') == "O":
            print("Player1 win")
        elif btn0.cget('text') == "X":
            print("Player2 win")
    if btn3.cget('text') == btn4.cget('text') and btn3.cget('text') == btn5.cget('text'):
        if btn3.cget('text') == "O":
            print("Player1 win")
        elif btn3.cget('text') == "X":
            print("Player2 win")
    if btn6.cget('text') == btn7.cget('text') and btn6.cget('text') == btn8.cget('text'):
        if btn6.cget('text') == "O":
            print("Player1 win")
        elif btn6.cget('text') == "X":
            print("Player2 win")
    if btn0.cget('text') == btn3.cget('text') and btn0.cget('text') == btn6.cget('text'):
        if btn0.cget('text') == "O":
            print("Player1 win")
        elif btn0.cget('text') == "X":
            print("Player2 win")
    if btn1.cget('text') == btn4.cget('text') and btn1.cget('text') == btn7.cget('text'):
        if btn1.cget('text') == "O":
            print("Player1 win")
        elif btn1.cget('text') == "X":
            print("Player2 win")
    if btn2.cget('text') == btn5.cget('text') and btn2.cget('text') == btn8.cget('text'):
        if btn2.cget('text') == "O":
            print("Player1 win")
        elif btn2.cget('text') == "X":
            print("Player2 win")
    if btn0.cget('text') == btn4.cget('text') and btn0.cget('text') == btn8.cget('text'):
        if btn0.cget('text') == "O":
            print("Player1 win")
        elif btn0.cget('text') == "X":
            print("Player2 win")
    if btn2.cget('text') == btn4.cget('text') and btn2.cget('text') == btn6.cget('text'):
        if btn2.cget('text') == "O":
            print("Player1 win")
        elif btn2.cget('text') == "X":
            print("Player2 win")

root = Tk()
root.geometry("500x400+200+200")
top = Toplevel (root)
labID = Label (top, text="ID", anchor=E, justify=RIGHT, font=("Times", 20))
labPW = Label (top, text="Password", anchor=E, justify=RIGHT, font=("Times", 20))
entryID = Entry (top)
entryPW = Entry(top, show="*")
btnLogin = Button (top, text="Login", command=login)
btnExit = Button (top, text="Exit", command=exitProgram)
labID.grid(row=0, column=0, sticky=NSEW)
entryID.grid(row=0, column=1, sticky=NSEW)
labPW.grid(row=1, column=0, sticky=NSEW)
entryPW.grid(row=1, column=1, sticky=NSEW)
btnLogin.grid(row=2, column=0, sticky=NSEW)
btnExit.grid(row=2, column=1, sticky=NSEW)
root.rowconfigure(0, weight=1)
root.rowconfigure(1, weight=1)
root.rowconfigure(2, weight=1)
root.columnconfigure(0, weight=1)
root.columnconfigure(1, weight=1)
root.columnconfigure(2, weight=1)

btn0 = Button(root, text="", command=lambda:setBtnText(0))
btn0.grid(row=0, column=0, sticky=NSEW)
btn1 = Button(root, text="", command=lambda:setBtnText(1))
btn1.grid(row=0, column=1, sticky=NSEW)
btn2 = Button(root, text="", command=lambda:setBtnText(2))
btn2.grid(row=0, column=2, sticky=NSEW)

btn3 = Button(root, text="", command=lambda:setBtnText(3))
btn3.grid(row=1, column=0, sticky=NSEW)
btn4 = Button(root, text="", command=lambda:setBtnText(4))
btn4.grid(row=1, column=1, sticky=NSEW)
btn5 = Button(root, text="", command=lambda:setBtnText(5))
btn5.grid(row=1, column=2, sticky=NSEW)

btn6 = Button(root, text="", command=lambda:setBtnText(6))
btn6.grid(row=2, column=0, sticky=NSEW)
btn7 = Button(root, text="", command=lambda:setBtnText(7))
btn7.grid(row=2, column=1, sticky=NSEW)
btn8 = Button(root, text="", command=lambda:setBtnText(8))
btn8.grid(row=2, column=2, sticky=NSEW)

root.withdraw()
root.mainloop()