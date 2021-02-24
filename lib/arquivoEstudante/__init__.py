from lib.interface import *

class Estudante:
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
            print("Ouve um erro na criação do arquivoEstudante de estudantes!")
        else:
            print(f"Estudante {nome} criado com sucesso!")

    def lerArquivo (nome):
        try:
            a = open(nome, "rt")
        except:
            print("Erro ao ler o arquivoEstudante!")
        else:
            Menu.window("PESSOA(S) CADASTRADA(S)")
            for linha in a:
                dados = linha.split(";")
                dados[1] = dados[1].replace("\n", "")
                print(f"{dados[0]:<8}{dados[1]:>3}")
        finally:
            a.close()

    def cadastrarAluno (arq, nome, sobrenome):
        try:
            a = open(arq, "at")
        except:
            print("Houve um erro na abertura do arquivoEstudante!")
        else:
            try:
                a.write(f"{nome};{sobrenome}\n")
            except:
                print("Houve um erro na hora de escrever os dados")
            else:
                print(f"Novo Registro de {nome} adicionado")
                a.close()

