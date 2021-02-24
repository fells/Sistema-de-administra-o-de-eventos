from lib.interface import *

from lib.interface import *

class SalaCafe:
    def arquivoExiste (nome):
        try:
            a = open(nome, "rt")
            a.close()
        except FileNotFoundError:
            return False
        else:
            return True

    def criarArquivo(nome):
        try:
            a = open(nome, "wt+")
            a.close()
        except:
            print("Ouve um erro na criação do arquivoSalaCafe de sala de café!")
        else:
            print(f"Sala {nome} criada com sucesso!")

    def lerArquivo (nome):
        try:
            a = open(nome, "rt")
        except:
            print("Erro ao ler o arquivoEstudante!")
        else:
            Menu.window("SALA(S) CAFÉ CADASTRADA(S)")
            for linha in a:
                dado = linha.split (";")
                dado [0] = dado [0].replace ("\n", "")
                print (f"{dado [0]}")
        finally:
            a.close()

    def cadastrarSalaCafe (arq, nome):
        try:
            a = open(arq, "at")
        except:
            print("Houve um erro na abertura do arquivoEstudante!")
        else:
            try:
                a.write(f"{nome}\n")
            except:
                print("Houve um erro na hora de escrever os dados")
            else:
                print(f"Novo Registro de {nome} adicionado")
                a.close()


