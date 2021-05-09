import PySimpleGUI as psg

data = list("abcdefg")

layout = [
    [psg.Listbox(values=data, size=(20, 4))],
    [psg.Ok(), psg.Cancel()]
]

window = psg.Window("ListBox 테스트", layout)

event, values = window.read()
window.close()
print(event, values)