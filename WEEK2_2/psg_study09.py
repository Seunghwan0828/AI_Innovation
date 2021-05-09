import PySimpleGUI as psg

layout = [
    [psg.Text("입력 1")],
    [psg.Input(key="-IN1-")],
    [psg.Text("입력 2"), psg.Input(key="-IN2-")],
    [psg.Text("입력 3"), psg.Input(key="-IN3-")],
    [psg.Ok(), psg.Cancel()]
]

window = psg.Window("Input 테스트", layout)

event, values = window.read()
window.close()
print(event, values)