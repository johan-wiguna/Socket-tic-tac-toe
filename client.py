import PySimpleGUI as sg
import socket

LOCALHOST = socket.gethostbyname(socket.gethostname())
PORT = 5050
ADDR = (LOCALHOST, PORT)

sg.theme('Dark Gray 5')
layoutGame = [
    [sg.Text("", justification='center', size=(50,3), key='_QUESTION_')],
    [sg.Button("",'center',size=(25,5),key='_ANS1_')
    , sg.Button("",'center', size=(25,5),key='_ANS2_')]
]
layoutResult = [
    [sg.Text("RESULT", justification='center', size=(50,1))],
    [sg.Text("Tim 1", justification='center', size=(25,1)),sg.Text("Tim 2", justification='center', size=(25,1))],
    [sg.Text("", justification='center', size=(25,1), key='_RES_A_'), sg.Text("", justification='center', size=(25,1), key='_RES_B_')],
    [sg.Text("", justification='center', size=(25,1), key='_WINNER_')]
]

layout = [
    [sg.Column(layoutGame, key='-COL1-'), 
    sg.Column(layoutResult, visible=False, key='-COL2-')]
]
window = sg.Window('Kahoot!?', layout)

while True:
    event, values = window.read()
    if event == sg.WIN_CLOSED:
        break
    
    
    
window.close()