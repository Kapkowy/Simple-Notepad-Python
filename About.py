import PySimpleGUI as Sg
import io

layout = [[Sg.Text("               Ver: 1.0")],
         [Sg.Text("Title: Python-Simple-Text-Editor")],
         [Sg.Text("Status: Not finished yet")],
         [Sg.Text("Next update: Soon")],
         [Sg.Button('Quit', key='Quit')]]
window = Sg.Window('test', layout, no_titlebar=True)
while True:
    event, values = window.read()
    if event == Sg.WINDOW_CLOSED or event == 'Quit':
        break
window.close()
