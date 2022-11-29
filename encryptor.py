import PySimpleGUI as sg
import pyperclip

def encrypt(message, key):
    final_menssage = ""
    num = 0
    for letter in message:
        letter = int(ord(letter))
        lt = int(ord(key[num]))
        number = letter + lt
        if number > 1000:
            number -= 999
        final_letter = chr(number)
        final_menssage = final_menssage + final_letter
        if num == len(key) - 1:
            num = 0
        else: 
            num += 1
    return final_menssage

def decrypt(message, key):
    final_menssage = ""
    num = 0
    for letter in message:  
        letter = int(ord(letter))
        lt = int(ord(key[num]))
        number = letter - lt
        if number < 0:
            number += 999
        final_letter = chr(number)
        final_menssage = final_menssage + final_letter
        if num == len(key) - 1:
            num = 0
        else: 
            num += 1
    return final_menssage    

def create_Window(theme):
    sg.theme('Darkgray6')
    
    layout = [
        [sg.T('type the message:')],

        [sg.I(key = 'message', expand_x = True)],
        
        [sg.T('or')],

        [sg.T('change a file:')],

        [sg.I(key='file', expand_x = True), sg.FileBrowse('select file', file_types=(("TXT Files", "*.txt"), ("ALL Files", "*.*")))],

        [sg.T('Type the key:')],

        [sg.I(key='key', expand_x = True)],
        
        [sg.B('Encrypt', expand_x = True), sg.B('Decrypt', expand_x = True)],

        [sg.T('Result', size = (62,5), key = 'Result')],

        [sg.B('Copy')],

        [sg.T('Type a name for save in a file:')],
        
        [sg.I(key = 'name', expand_x = True), sg.B('Make a file', key = 'make')],

        [sg.T('The file has made with successfully', key = 'notfication', visible = False), ]
        
        ]
    return sg.Window('Encrypt', layout)

window = create_Window('dark')

while True:
    event, values = window.read(timeout = 10)
    if event == sg.WINDOW_CLOSED:
        break
    
    if event == 'Encrypt':
        message = str(window['message'].get())
        file = str(window['file'].get())
        key = str(window['key'].get())
        if key != '':
            if message != '':
                final_menssage = encrypt(message, key)
                window['Result'].update(final_menssage)
            elif file != '':
                file= str(window['file'].get())
                file = open(file, 'r', encoding="UTF-8")
                message = file.readlines()
                message = " ".join(message)
                file.close()
                final_menssage = encrypt(message, key)
                window['Result'].update(final_menssage)
            else:
                window['Result'].update('type the message')
        else:
            window['Result'].update('Type the key')
        

    if event == 'Decrypt':
        message = str(window['message'].get())
        file = str(window['file'].get())
        key = str(window['key'].get())
        if key != '':
            if message != '':
                final_menssage = decrypt(message, key)
                window['Result'].update(final_menssage)
            elif file != '':
                file= str(window['file'].get())
                file = open(file, 'r', encoding="UTF-8")
                message = file.readlines()
                message = " ".join(message)
                file.close()
                final_menssage = decrypt(message, key)
                window['Result'].update(final_menssage)
            elif message == '' and file == '':
                window['Result'].update('type the message')
        else:
            window['Result'].update('Type the key')

    if event == 'Copy':
        Result = str(window['Result'].get())
        pyperclip.copy(Result)
        window['Result'].update('successfully copied')

    if event == 'make':
        Result = str(window['Result'].get())
        name = str(window['name'].get())
        if name[-4:] != '.txt':
            name = name + '.txt'
        name = open(name, "w", encoding="UTF-8")
        name.write(Result)
        name.close()
        window['notfication'].update(visible = True)

window.close()