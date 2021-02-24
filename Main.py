from lib.interface import *
from lib.arquivoEstudante import *
from lib.arquivoSala import *
from lib.arquivoSalaCafe import *
from time import sleep

arq = "Estudantes.txt"
arq2 = "Salas.txt"
arq3 = "Salascafé.txt"

if not Estudante.arquivoExiste(arq):
    Estudante.criarArquivo(arq)

if not Sala.arquivoExiste(arq2):
    Sala.criarArquivo(arq2)

if not SalaCafe.arquivoExiste(arq3):
    Sala.criarArquivo(arq3)


while True:
    resposta = Menu.menu(["Cadastrar sala(s)", "Cadastrar Aluno(a)", "Cadastrar Sala de café", "Consultar Alunos", "Sair do sistema"])
    if resposta == 1:
        Menu.window("NOVO CADASTRO DE SALA(S)")
        quantidade = int(input("Insira a quantidade máxima por sala: "))
        nome = str(input("Insira o nome da sala que deseja criar: "))
        Sala.cadastrarSala(arq2, nome, quantidade)

    elif resposta == 2:
        Menu.window("NOVO CADASTRO DE ALUNO(A)")
        nome = str(input("Insira o nome do aluno: "))
        sobreNome= str(input("Inisira o sobrenome do aluno: "))
        Estudante.cadastrarAluno(arq, nome, sobreNome)

    elif resposta == 3:
        Menu.window("NOVO CADASTRO DE SALA DE CAFÉ")
        nome = str(input("Insira o nome da sua sala de coffebreak: "))
        SalaCafe.cadastrarSalaCafe(arq3,nome)
    elif resposta == 4:
        Menu.window("ALUNO(A)/SALA(S)")
        Estudante.lerArquivo (arq)
        Sala.lerArquivo(arq2)
        SalaCafe.lerArquivo(arq3)
    elif resposta == 5:
        Menu.window("Saindo do sistema")
        break

    else:
        Menu.window("Erro! Digite uma opçao válida")

    sleep(2)




