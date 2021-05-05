import socket
from _thread import *
from tkinter import *
from tkinter import messagebox

HOST = socket.gethostbyname(socket.gethostname())
PORT = 5050
ADDR = (HOST, PORT)

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
server.bind(ADDR)
server.listen(1)
print("[Server is starting...]")
connectionSocket, clientAddress = server.accept()
score1 = 0 
score2 = 0
rows, cols = (3, 3)
arr = [[0 for i in range(cols)] for j in range(rows)]
clickCount = 0
roundCount = 1

def check_first_turn():
    global lStartFirst
    if(int(roundCount)%2!=0):
        return True
    else:
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

def btn_clicked(b):
    global isFirst, clickCount, bRematch, score1, score2, lResult, b0, b1, b2, b3, b4, b5, b6, b7, b8
    if(isFirst==True and clickCount%2==0) or (isFirst==False and clickCount%2!=0):
        if b["text"] == "":
            if isFirst == True:
                b["text"] = "X"
                b["fg"] = "blue"
                clickCount += 1
                row = b.grid_info()['row']-2
                column = b.grid_info()['column']
                arr[row][column] = 1
                print(arr)
            else:
                b["text"] = "O" 
                b["fg"] = "red"
                isFirst = True
                clickCount += 1
                row = b.grid_info()['row']-2
                column = b.grid_info()['column']
                arr[row][column] = 2
                print(arr)
                # messagebox.showerror("Not your turn","Please wait until your next turn.")

            if(check_win()==1):
                print("player 1 win")
                score1 += 1
                lResult.config(text="Player 1 win!")
                bRematch.config(state="normal", bg="red", fg="white")
            elif(check_win()==2):
                print("player 2 win")
                score2 += 1
                lResult.config(text="Player 2 win!")
                bRematch.config(state="normal", bg="red", fg="white")
            elif(clickCount==9):
                print("draw")
                lResult.config(text="Draw!")
                bRematch.config(state="normal", bg="red", fg="white")
            
            strIdx = str(row) + " " + str(column)
            strIdxEncoded = strIdx.encode("UTF-8")
            print("strIdx: ", strIdx)
            connectionSocket.send(strIdxEncoded)
        else: messagebox.showerror("Misclicked", "Please click an empty box.")
    else: messagebox.showerror("Opponent's turn", "Please for your next turn.")

def rematch(b):
    global clickCount, roundCount, score1, score2, b0, b1, b2, b3, b4, b5, b6, b7, b8, lResult, lRound, lScore1, lScore2
    clickCount = 0
    roundCount += 1

    lResult["text"] = ""
    lRound["text"] = "ROUND " + str(roundCount)
    lScore1["text"] = "P1 (You): " + str(score1)
    lScore2["text"] = "P2: " + str(score2)
    
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

root = Tk()
root.title('[SERVER] Tic Tac Toe')
root.resizable(0, 0)

lScore1 = Label(root, text="P1 (You): 0", font=("Helvetica", 10))
lScore2 = Label(root, text="P2: 0", font=("Helvetica", 10))
lRound = Label(root, text="ROUND 1", font=("Helvetica", 10, "bold"))
lStartFirst = Label(root, text="", font=("Helvetica", 10))
lResult = Label(root, text="", font=("Helvetica", 10, "bold"))

lScore1.grid(row=0, column=0)
lScore2.grid(row=0, column=2)
lRound.grid(row=0, column=1)
lStartFirst.grid(row=1, column=0, columnspan=3)
lResult.grid(row=5, column=0, columnspan=3)

if check_first_turn() == True: lStartFirst["text"] = "You start first (You: X)"
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

bRematch = Button(root, text="REMATCH", font=("Helvetica", 12), width=40, state=DISABLED, command=lambda: rematch(bRematch))
bBeginTurn = Button(root, text="BEGIN TURN", font=("Helvetica", 12), width=40, state=DISABLED, command=lambda: update_grid(bBeginTurn))
bRematch.grid(row=6, column=0, columnspan=3)

def receiveThread(server):
    global clickCount, connectionSocket
    while True:
        received = connectionSocket.recv(1024)
        receivedDecoded = received.decode()
        print("From client: ", received.decode())
        rowReceived = int(receivedDecoded[0])
        columnReceived = int(receivedDecoded[2])
        print("rowReceived: ", rowReceived)
        print("columnReceived: ", columnReceived)
        clickCount += 1

        arr[rowReceived][columnReceived] = 2
        if rowReceived == 0:
            if columnReceived == 0: b0.config(text="O", fg="red")
            elif columnReceived == 1: b1.config(text="O", fg="red")
            elif columnReceived == 2: b2.config(text="O", fg="red")
        elif rowReceived == 1:
            if columnReceived == 0: b3.config(text="O", fg="red")
            elif columnReceived == 1: b4.config(text="O", fg="red")
            elif columnReceived == 2: b5.config(text="O", fg="red")
        elif rowReceived == 2:
            if columnReceived == 0: b6.config(text="O", fg="red")
            elif columnReceived == 1: b7.config(text="O", fg="red")
            elif columnReceived == 2: b8.config(text="O", fg="red")
        check_win()

start_new_thread(receiveThread, (server,))
root.mainloop()