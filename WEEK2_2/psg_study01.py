import PySimpleGUI as psg

layout = [
    [psg.Button('버튼1', size=(20, 8))],
    [psg.Btn('버튼2', size=(10, 2), button_color=("blue", "green"))],
    [psg.B("버튼3")],
    [psg.Ok("예"), psg.Cancel()],
    [psg.Yes(), psg.No()]
]
window = psg.Window("버튼 처리 학습", layout)

event, values = window.read()
window.close()
print(event, values)