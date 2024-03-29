# Dibuat oleh Vicky Ricardo (6181801011) & Johan Adi Wiguna (6181801018)

import socket
from _thread import *
from tkinter import *
from tkinter import messagebox

HOST = socket.gethostbyname(socket.gethostname())
PORT = 5050
ADDR = (HOST, PORT)

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect(ADDR)

winner = 0
score1 = 0 
score2 = 0
rows, cols = (3, 3)
arr = [[0 for i in range(cols)] for j in range(rows)]
clickCount = 0
roundCount = 1

mySymbol = ""
myColor = ""
opSymbol = ""
opColor = ""

def check_first_turn():
    global lStartFirst, mySymbol, myColor, opSymbol, opColor
    if(int(roundCount)%2==0):
        mySymbol = "X"
        myColor = "blue"
        opSymbol = "O"
        opColor = "Red"
        return True
    else:
        mySymbol = "O"
        myColor = "Red"
        opSymbol = "X"
        opColor = "Blue"
        return False

isFirst = check_first_turn() # True: X, False: O


def check_win():
    #vertical
    for i in range(len(arr)):
        a = arr[i][0]
        b = arr[i][1]
        c = arr[i][2]
        if((a==b) and (b==c) and a != 0):
            return a
    
    #horizontal
    for i in range(len(arr)):
        a = arr[0][i]
        b = arr[1][i]
        c = arr[2][i]
        if((a==b) and (b==c) and a != 0):
            return a

    #diagonal \
    a = arr[0][0]
    b = arr[1][1]
    c = arr[2][2]
    if((a==b) and (b==c) and a != 0):
        return a

    #diagonal /
    a = arr[0][2]
    b = arr[1][1]
    c = arr[2][0]
    if((a==b) and (b==c) and a != 0):
        return a

def define_winner():
    global score1, score2, lResult, bRematch, lScore1, lScore2, winner
    if(check_win()==1):
        score1 += 1
        lResult.config(text="Player 1 win!")
        lScore1.config(text="P1: " + str(score1))
        bRematch.config(state="normal", bg="green", fg="white")
        winner = 1
    elif(check_win()==2):
        score2 += 1
        lResult.config(text="Player 2 win!")
        lScore2.config(text="P2 (You): " + str(score2))
        bRematch.config(state="normal", bg="green", fg="white")
        winner = 2
    elif(clickCount==9):
        score1 += 1
        score2 += 1
        lResult.config(text="Draw!")
        lScore1.config(text="P1: " + str(score1))
        lScore2.config(text="P2 (You): " + str(score2))
        bRematch.config(state="normal", bg="green", fg="white")

def btn_clicked(b):
    global client, isFirst, clickCount, bRematch, lResult, winner
    if(winner!=0):
        messagebox.showinfo("Game over", "If you wish to play again, please click the Rematch button.")
    elif(isFirst==True and clickCount%2==0) or (isFirst==False and clickCount%2!=0):
        if b["text"] == "":
            b["text"] = mySymbol
            b["fg"] = myColor
            clickCount += 1
            row = b.grid_info()['row']-2
            column = b.grid_info()['column']
            arr[row][column] = 2
            print(arr)
            
            define_winner()

            strIdx = str(row) + " " + str(column)
            strIdxEncoded = strIdx.encode("UTF-8")
            print("strIdx: ", strIdx)
            client.send(strIdxEncoded)
        else: messagebox.showerror("Misclicked", "Please click an empty box.")
    else: messagebox.showerror("Opponent's turn", "Please wait for your next turn.")

def rematch(b, stat):
    global clickCount, roundCount, score1, score2, winner, isFirst, b0, b1, b2, b3, b4, b5, b6, b7, b8, lResult, lRound, lScore1, lScore2, mySymbol
    clickCount = 0
    roundCount += 1
    winner = 0
    isFirst = check_first_turn()
    print("mySymbol: " + mySymbol)
    lResult["text"] = ""
    lRound["text"] = "ROUND " + str(roundCount)
    lScore1["text"] = "P1: " + str(score1)
    lScore2["text"] = "P2 (You): " + str(score2)

    b.config(state="disabled", bg="SystemButtonFace")

    b0.config(text="")
    b1.config(text="")
    b2.config(text="")

    b3.config(text="")
    b4.config(text="")
    b5.config(text="")

    b6.config(text="")
    b7.config(text="")
    b8.config(text="")

    for i in range(len(arr)):
        for j in range(len(arr)):
            arr[i][j] = 0

    if (check_first_turn()): lStartFirst["text"] = "You start first (You: X)"
    else: lStartFirst["text"] = "Opponent start first (You: O)"
    if stat!="req": client.send("rematch".encode("UTF-8"))

root = Tk()
root.title('[CLIENT] Tic Tac Toe')
root.resizable(0, 0)

lScore1 = Label(root, text="P1: 0", font=("Helvetica", 10))
lScore2 = Label(root, text="P2 (You): 0", font=("Helvetica", 10))
lRound = Label(root, text="ROUND 1", font=("Helvetica", 10, "bold"))
lStartFirst = Label(root, text="", font=("Helvetica", 10), bg="PeachPuff2", width=45)
lResult = Label(root, text="", font=("Helvetica", 10, "bold"))

lScore1.grid(row=0, column=0)
lScore2.grid(row=0, column=2)
lRound.grid(row=0, column=1)
lStartFirst.grid(row=1, column=0, columnspan=3)
lResult.grid(row=5, column=0, columnspan=3)

if (check_first_turn()): lStartFirst["text"] = "You start first (You: X)"
else: lStartFirst["text"] = "Opponent start first (You: O)"

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

bRematch = Button(root, text="REMATCH", font=("Helvetica", 12), width=40, state=DISABLED, command=lambda: rematch(bRematch, ""))

bRematch.grid(row=6, column=0, columnspan=3)

def receiveThread(client):
    global clickCount, connectionSocket, bRematch, winner
    while True:
        received = client.recv(1024)
        receivedDecoded = received.decode()
        print("From server: ", received.decode())
        if receivedDecoded == "rematch": rematch(bRematch, "req")
        elif receivedDecoded == "quit": close_game()
        else:
            rowReceived = int(receivedDecoded[0])
            columnReceived = int(receivedDecoded[2])
            print("rowReceived: ", rowReceived)
            print("columnReceived: ", columnReceived)
            clickCount += 1

            arr[rowReceived][columnReceived] = 1
            if rowReceived == 0:
                if columnReceived == 0: b0.config(text=opSymbol, fg=opColor)
                elif columnReceived == 1: b1.config(text=opSymbol, fg=opColor)
                elif columnReceived == 2: b2.config(text=opSymbol, fg=opColor)
            elif rowReceived == 1:
                if columnReceived == 0: b3.config(text=opSymbol, fg=opColor)
                elif columnReceived == 1: b4.config(text=opSymbol, fg=opColor)
                elif columnReceived == 2: b5.config(text=opSymbol, fg=opColor)
            elif rowReceived == 2:
                if columnReceived == 0: b6.config(text=opSymbol, fg=opColor)
                elif columnReceived == 1: b7.config(text=opSymbol, fg=opColor)
                elif columnReceived == 2: b8.config(text=opSymbol, fg=opColor)
            
            define_winner()

start_new_thread(receiveThread, (client,))

def on_closing():
    if messagebox.askokcancel("Quit game", "Are you sure you want to quit?"):
        client.send("quit".encode("UTF-8"))
        root.destroy()

def close_game():
    root.destroy()

root.protocol("WM_DELETE_WINDOW", on_closing)
root.mainloop()