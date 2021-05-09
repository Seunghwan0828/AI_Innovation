import PySimpleGUI as psg

column1 = [
    [psg.Radio("Radio1", group_id=1)],
    [psg.Radio("Radio2", group_id=1)],
    [psg.Radio("Radio3", group_id=1)],
]

column2 = [
    [psg.Radio("RadioA", group_id=2)],
    [psg.Radio("RadioB", group_id=2)],
    [psg.Radio("RadioC", group_id=3)],
]

layout = [
    [psg.Column(column1), psg.VerticalSeparator(), psg.Col(column2)],
    [psg.Ok(), psg.Cancel()]
]

window = psg.Window("Radio 테스트", layout)

event, values = window.read()
window.close()
print(event, values)