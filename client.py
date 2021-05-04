import socket
from tkinter import *
from tkinter import messagebox

LOCALHOST = socket.gethostbyname(socket.gethostname())
PORT = 5050
ADDR = (LOCALHOST, PORT)

clicked = True # True: Giliran X, False: Giliran O
clickCount = 0
roundCount = 0

def btn_clicked(b):
    global clicked, clickCount
    if b["text"] == "":
        if clicked == True:
            b["text"] = "X"
            b["fg"] = "blue"
            clicked = False
            clickCount += 1
        else:
            b["text"] = "O"
            b["fg"] = "red"
            clicked = True
            clickCount += 1
    else:
        messagebox.showerror("Misclicked", "Please click an empty box.")

root = Tk()
root.title('[CLIENT] Tic Tac Toe')

lYou = Label(root, text="You: ...", font=("Helvetica", 10))
lEnemy = Label(root, text="Enemy: ...", font=("Helvetica", 10))
lRound = Label(root, text="ROUND ...", font=("Helvetica", 10, "bold"))
lStartFirst = Label(root, text="... start first (X)", font=("Helvetica", 10))

lYou.grid(row=0, column=0)
lEnemy.grid(row=0, column=2)
lRound.grid(row=0, column=1)
lStartFirst.grid(row=1, column=1)

# Button untuk setiap box
b0 = Button(root, text="", font=("Helvetica", 20), height=3, width=7, bg="SystemButtonFace", command=lambda: btn_clicked(b0))
b1 = Button(root, text="", font=("Helvetica", 20), height=3, width=7, bg="SystemButtonFace", command=lambda: btn_clicked(b1))
b2 = Button(root, text="", font=("Helvetica", 20), height=3, width=7, bg="SystemButtonFace", command=lambda: btn_clicked(b2))

b3 = Button(root, text="", font=("Helvetica", 20), height=3, width=7, bg="SystemButtonFace", command=lambda: btn_clicked(b3))
b4 = Button(root, text="", font=("Helvetica", 20), height=3, width=7, bg="SystemButtonFace", command=lambda: btn_clicked(b4))
b5 = Button(root, text="", font=("Helvetica", 20), height=3, width=7, bg="SystemButtonFace", command=lambda: btn_clicked(b5))

b6 = Button(root, text="", font=("Helvetica", 20), height=3, width=7, bg="SystemButtonFace", command=lambda: btn_clicked(b6))
b7 = Button(root, text="", font=("Helvetica", 20), height=3, width=7, bg="SystemButtonFace", command=lambda: btn_clicked(b7))
b8 = Button(root, text="", font=("Helvetica", 20), height=3, width=7, bg="SystemButtonFace", command=lambda: btn_clicked(b8))

# Memasukkan setiap button ke dalam grid
b0.grid(row=2, column=0)
b1.grid(row=2, column=1)
b2.grid(row=2, column=2)

b3.grid(row=3, column=0)
b4.grid(row=3, column=1)
b5.grid(row=3, column=2)

b6.grid(row=4, column=0)
b7.grid(row=4, column=1)
b8.grid(row=4, column=2)

bRematch = Button(root, text="REMATCH", font=("Helvetica", 12), width=40, state=DISABLED)

bRematch.grid(row=5, column=0, columnspan=3)

root.mainloop()

while True:
    event, values = window.read()
    if event == sg.WIN_CLOSED:
        break
    
window.close()