import random
import PySimpleGUI as sg
import os

class Gerarsenha:
    def __init__(self):
        sg.theme('Black')
        layout = [
           [sg.Text('Nome', size= (10, 1)),
            sg.Input(key='nome', size =(20, 1)),
            sg.Text('E-mail/Usuário', size = (10,1)), sg.Input(key='usuario', size=(20, 1))],
            sg.Text('Quantidade de caracteres'), sg.Combo(values=list(
            range(30)), ke='total_chars', default_value=1, size=(3,1)),
            [sg.Output(size=(32,5))],
            [sg.Button('GERAR')]
        ]
       self.janela = sg.Window('Gerador de Senhas', layout)
    def Inicio(self):
        pass
    def salvar_senha(self):
        pass

senha = Gerarsenha()
senha.Inicio()




