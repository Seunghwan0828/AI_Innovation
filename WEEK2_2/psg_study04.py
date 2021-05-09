import PySimpleGUI as psg

layout = [
    [psg.Checkbox("체크박스1", key="-CHECK1-")],
    [psg.CBox("체크박스2", key="-CHECK2-")],
    [psg.CB("체크박스3", key="-CHECK3-")],
    [psg.Ok(), psg.Cancel()]
]

window = psg.Window("Checkbox 테스트", layout)

event, values = window.read()
window.close()
print(event, values)