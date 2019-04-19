#-*-code:utf-8

import requests
from os import system
from sys import platform
from time import sleep


class Main(object):
    def __init__(self):
        if platform == 'linux':
            system('clear')
        elif platform == 'win32':
            system('cls')
        self.pergunta = int(input('[1]Consultar Cep\n[2]Sair\n: '))
        if self.pergunta == 1:
            self.getCep()
        else:
            system('exit')



    def getCep(self):
        if platform == 'linux':
            system('clear')
        elif platform == 'win32':
            system('cls')
        self.quest = input("Insira o Cep para consulta: ")
        if len(self.quest) != 8:
            print('Cep inválido\n O Cep deve conter 8 digitos')
            sleep(3)
            self.getCep()
        else:
            self.consulta()




    def consulta(self):
        self.req  = requests.get('https://viacep.com.br/ws/{}/json/'.format(self.quest))
        self.endereco = self.req.json()
        print('Cidade: ', self.endereco['localidade'])
        print('Bairro: ', self.endereco['bairro'])
        print('Estado: ', self.endereco['uf'])
        print('Rua:    ', self.endereco['logradouro'])
        self.quest2 = int(input('[1]Nova consulta\n[2]Sair\n: '))
        if self.quest2 == 1:
            self.consulta()
        else:
            system('exit')
       
        



if __name__ == '__main__':
    Consul = Main()    