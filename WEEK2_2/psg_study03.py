import PySimpleGUI as psg

layout = [
    [psg.Canvas(size=(100, 100), background_color="blue", key="canvas")],
    [psg.Ok(), psg.Cancel()]
]

window = psg.Window("Canvas 테스트", layout)

event, values = window.read()
window.close()
print(event, values)