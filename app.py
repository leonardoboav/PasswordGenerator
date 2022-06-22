#Importação de bibliotecas
import random
import venv
import pandas as pd

#Arranjando caracteres em variáveis
lowercase = "abcdefghijklmnopqrstuvwxyz" 
uppercase = 'ABCDEFGHIJKLMNOPKRSTUVWXYZ'
numbers = '0123456789'
symbols = '!@#$%&*()+='

#Definições para gerar senha
string = lowercase + uppercase + numbers + symbols
lenght = 8
senha = "".join(random.sample(string, lenght));

#Gerando a senha
print('Sua nova senha é:' + senha)

