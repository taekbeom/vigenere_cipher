import PySimpleGUI as sg


alp = 'абвгдежзийклмнопрстуфхцчшщъыьэюя '
alp_let = {l: i for i, l in enumerate(alp)}
alp_pos = {v: k for k, v in alp_let.items()}


def position(i, k):
    return k[i % len(k)]


def encode(v, k):
    encoded_mes = ''
    i_pos = -1
    for i, l in enumerate(v):
        if l in alp_let.keys():
            i_pos += 1
            encoded_mes += alp_pos[(alp_let[l]-alp_let[position(i_pos, k)]) % len(alp)]
        else:
            encoded_mes += l
    return encoded_mes


def decode(v, k):
    decoded_mes = ''
    i_pos = -1
    for i, l in enumerate(v):
        if l in alp_let.keys():
            i_pos += 1
            decoded_mes += alp_pos[(alp_let[l]+alp_let[position(i_pos, k)]) % len(alp)]
        else:
            decoded_mes += l
    return decoded_mes


bg = '#BD9C44'
bg_b = '#B27310'
t_warn = '#C70E0E'
t_res = '#06812D'

sg.set_options(background_color=bg)
sg.set_options(font=('Sitka Text', 12))

layout = [
    [sg.Text("Text", background_color=bg),
     sg.Text('', key='error_mes', text_color=t_warn, background_color=bg)],
    [sg.InputText(key='message')],
    [sg.Text("Key", background_color=bg),
     sg.Text('', key='error_key', text_color=t_warn, background_color=bg)],
    [sg.InputText(key='key')],
    [sg.Button("Encode", button_color=bg_b),
     sg.Button("Decode", button_color=bg_b)],
    [sg.Text("Result: ", background_color=bg),
     sg.InputText('', font='bold', size=(28, 28), expand_x=True, text_color=t_res, key='result', disabled=True)]
]

icon_path = 'file://icon.png'

window = sg.Window('(d)E(n)coder', layout, icon='icon.ico')

while True:
    event, values = window.read()

    if event == sg.WIN_CLOSED:
        break

    message = values['message']
    key = values['key']

    error_mes = ''
    error_key = ''

    if event == 'Encode' or event == 'Decode':
        if not message:
            error_mes = 'Type in message'
        else:
            error_mes = ''
        if not key:
            error_key = 'Type in key'
        elif not all(w.lower() in alp_let.keys() for w in key):
            error_key = 'Incorrect key'
        else:
            error_key = ''
        if not error_key and not error_mes:
            if event == 'Encode':
                result = encode(message.lower(), key.lower())
            else:
                result = decode(message.lower(), key.lower())
            window['result'].update(result)

    window['error_mes'].update(error_mes)
    window['error_key'].update(error_key)

window.close()
