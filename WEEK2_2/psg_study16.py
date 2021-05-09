import PySimpleGUI as psg

layout = [
    # [psg.Slider(range=(1, 101), default_value=50, orientation="v")],
    [psg.Slider(range=(1, 101), default_value=50, orientation="h")],
    [psg.Ok(), psg.Cancel()]
]

window = psg.Window("Slider 테스트", layout)

event, values = window.read()
window.close()
print(event, values)