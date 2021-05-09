import PySimpleGUI as psg

data = list("abcdefg")
# ["a", "b", "c", "d", "e", "f", "g"]

layout = [
    [psg.Combo(values=data, size=(10, 4), default_value=data[2])],
    [psg.Ok(), psg.Cancel()]
]

window = psg.Window("Checkbox 테스트", layout)

event, values = window.read()
window.close()
print(event, values)