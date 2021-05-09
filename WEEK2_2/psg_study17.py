import PySimpleGUI as psg

layout = [
    [psg.Spin(initial_value=3, values=list(range(1, 10)), size=(10, 10))],
    [psg.Ok(), psg.Cancel()]
]

window = psg.Window("Spin 테스트", layout)

event, values = window.read()
window.close()
print(event, values)