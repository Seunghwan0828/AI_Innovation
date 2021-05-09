import PySimpleGUI as psg

layout = [
    [psg.Image("skyline.png")],
    [psg.Ok(), psg.Cancel()]
]

window = psg.Window("Image 테스트", layout)

event, values = window.read()
window.close()
print(event, values)