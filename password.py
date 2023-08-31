from ast import List
import random
import PySimpleGUI as sg
import os

class GerarSenha:
    #Interface
    def __init__(self):
        sg.theme('Black')
        layout = [
           [sg.Text('Nome', size= (10, 1)),
            sg.Input(key='nome', size =(20, 1))],
            [sg.Text('E-mail/Usuário', size = (10,1)), 
            sg.Input(key='usuario', size=(20, 1))],
            [sg.Text('Quantidade de caracteres'), sg.Combo(values=list(
            range(30)), key='total_chars', default_value=1, size=(3,1))],
            [sg.Output(size=(32,5))],
            [sg.Button('GERAR')]
        ] 

        self.janela= sg.Window('Gerador de Senhas', layout)
        
    def Inicio(self):
        while True:
            evento, valores = self.janela.read()
            if evento == sg.WIN_CLOSED:
                break
            if evento == 'GERAR':
                nova_senha = self.gerador(valores)
                print(nova_senha)
                self.salvar_senha(nova_senha, valores)    

    def gerador(self,valores):
        char_list = 'ABCDEFGHIJKLMNOPQRSTUVXZYWabcdefghijklmnopqrstuvxzyw1234567890!@#%&'
        chars = random.choices(char_list, k=int(valores['total_chars']))
        senha_nova = ''.join(chars)
        return senha_nova

    def salvar_senha(self, nova_senha, valores):
       with open('senhas.txt', 'a', newline='') as arquivo:
           arquivo.write(
               f"nome: {valores['nome']}, usuario:{valores['usuario']}, nova senha: {nova_senha}")
           
    print('Arquivo Salvo')
    


senha = GerarSenha()
senha.Inicio()




