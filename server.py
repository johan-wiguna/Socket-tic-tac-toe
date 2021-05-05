import socket
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

score1 = 0 
score2 = 0
rows, cols = (3, 3)
arr = [[0 for i in range(cols)] for j in range(rows)]
clickCount = 0
roundCount = 1
def check_turn():
    if(int(roundCount)%2!=0):
        return True
    else:
        return False
clicked = check_turn() # True: Giliran X, False: Giliran O

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
    global clicked, clickCount, bRematch, score1, score2, lResult
    if b["text"] == "":
        if clicked == True:
            b["text"] = "X"
            b["fg"] = "blue"
            clicked = False
            clickCount += 1
            row = b.grid_info()['row']-2
            column = b.grid_info()['column']
            arr[row][column] = 1
            print(arr)
        else:
            #b["text"] = "O"
            #b["fg"] = "red"
            #clicked = True
            #clickCount += 1
            #row = b.grid_info()['row']-2
            #column = b.grid_info()['column']
            #arr[row][column] = 2
            #print(arr)
            messagebox.showerror("Not your turn","Please wait")

        if(check_win()==1):
            print("player 1 win")
            score1 += 1
            bRematch.config(state="normal", bg="red", fg="white")
        elif(check_win()==2):
            print("player 2 win")
            score2 += 1
            bRematch.config(state="normal", bg="red", fg="white")
        elif(clickCount==9):
            print("draw")
            bRematch.config(state="normal", bg="red", fg="white")
    else:
        messagebox.showerror("Misclicked", "Please click an empty box.")
    
    connectionSocket, clientAddress = server.accept()
    received = connectionSocket.recv(4096)
    receivedDecoded = received.decode()
    print("From client: ", received.decode())
    rowReceived = receivedDecoded[0]
    columnReceived = receivedDecoded[2]
    print("rowReceived: ", rowReceived)
    print("columnReceived: ", columnReceived)

root = Tk()
root.title('[SERVER] Tic Tac Toe')

lYou = Label(root, text="You: 0", font=("Helvetica", 10))
lEnemy = Label(root, text="Enemy: 0", font=("Helvetica", 10))
lRound = Label(root, text="ROUND 0", font=("Helvetica", 10, "bold"))
lStartFirst = Label(root, text="... start first (X)", font=("Helvetica", 10))
lResult = Label(root, text="", font=("Helvetica", 10, "bold"))

lYou.grid(row=0, column=0)
lEnemy.grid(row=0, column=2)
lRound.grid(row=0, column=1)
lStartFirst.grid(row=1, column=1)
lResult.grid(row=5, column=0, columnspan=3)

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