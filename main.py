import functools
import keyboard
import PySimpleGUI as Sg
import time
import io

menu_def = [['&File', ['Save As', 'Open', 'Save', 'E&xit']],
            ['&Crazy', ['Delete all']],
            ['&Help', '&About...'], ]

layout = [[Sg.Menu(menu_def, tearoff=True)],
          [Sg.Multiline("", size=(85, 35), enable_events=True, visible=True, key='testek')],
          ]

rt = 'notepad'
tr = Sg.popup_get_folder("Please select folder!", "Notepad STARTUP", icon='icon.ico')
if tr == '':
    print("THIS PROGRAM CANT WORKING IF YOU DONT SELECT WHERE YOU WANT TO SAVE (ERROR)")
elif tr and not '':
    print("you select " + tr)
else:
    print("THIS PROGRAM CANT WORKING IF YOU DONT SELECT WHERE YOU WANT TO SAVE (ERROR)")

window = Sg.Window('Notepad python', layout, icon='icon.ico')

while True:
    event, values = window.read()
    if event == Sg.WINDOW_CLOSED or event == 'Exit':
        break
    if event == 'New':
        window['testek'].update("Start Writing")
    elif event == 'Open':
        ter = open(Sg.popup_get_file("", file_types=(("Text Files", "*.txt"),)))
        window['testek'].update(ter.read())
    elif event == 'Save As':
        rt = Sg.popup_get_text('Name of file without .txt', "Notepad", icon='icon.ico')
        if tr != '' in tr:
            print(tr)
        elif tr == '' in tr:
            tr = Sg.popup_get_folder('Where you want to save?', "Notepad", icon='icon.ico')
        with io.open(tr + '/' + rt + ".txt", "a", encoding="utf8") as f:
            f.write(values['testek'])
            f.write('\n')
        f.close()
    elif event == 'Delete all':
        window['testek'].update("")
        print(values['testek'])
        window.refresh()
    elif keyboard.is_pressed("ctrl+s"):
        with io.open(tr + '/' + rt + ".txt", "a", encoding="utf8") as f:
            f.write(values['testek'])
            f.write('\n')
        f.close()
    elif event == 'About':
        import About
window.close()
