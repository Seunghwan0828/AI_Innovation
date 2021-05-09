import PySimpleGUI as psg

layout = [
    [psg.Multiline(size=(100, 20))],
    [psg.Ok(), psg.Cancel()]
]

window = psg.Window("멀티라인 테스트", layout)

event, values = window.read()
window.close()
print(event, values)