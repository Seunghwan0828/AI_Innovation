import PySimpleGUI as psg

column1 = [
    [psg.Checkbox("체크박스1", key="-CHECK1-")],
    [psg.CBox("체크박스2", key="-CHECK2-")],
    [psg.CB("체크박스3", key="-CHECK3-")],
]

column2 = [
    [psg.Checkbox("체크박스A", key="-CHECKA-")],
    [psg.CBox("체크박스B", key="-CHECKB-")],
    [psg.CB("체크박스C", key="-CHECKC-")],
]

layout = [
    [psg.Column(column1), psg.VerticalSeparator(), psg.Col(column2)],
    [psg.Ok(), psg.Cancel()]
]

window = psg.Window("Checkbox 테스트", layout)

event, values = window.read()
window.close()
print(event, values)