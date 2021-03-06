from lib.interface import *

from lib.interface import *

class Sala:
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
            print("Ouve um erro na criação do arquivoSala de salas!")
        else:
            print(f"Sala {nome} criada com sucesso!")

    def lerArquivo (nome):
        try:
            a = open(nome, "rt")
        except:
            print("Erro ao ler o arquivoEstudante!")
        else:
            Menu.window("SALA(S) CADASTRADA(S)")
            for linha in a:
                dados = linha.split (";")
                dados [1] = dados [1].replace ("\n", "")
                print (f"{dados [0]:<20} cabem{dados [1]:>5} pessoa(s) nessa sala")
        finally:
            a.close()

    def cadastrarSala (arq, nome, quantidade):
        try:
            a = open(arq, "at")
        except:
            print("Houve um erro na abertura do arquivoEstudante!")
        else:
            try:
                a.write(f"{nome};{quantidade}\n")
            except:
                print("Houve um erro na hora de escrever os dados")
            else:
                print(f"Novo Registro de {nome} adicionado")
                a.close()


