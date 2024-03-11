import os
import shutil
import tkinter as tk
from tkinter import filedialog

# Função para separar os ficheiros por extensão
def separar_arquivos_por_extensao(pasta_origem):
    # Obter a lista de arquivos na pasta de origem
    arquivos = os.listdir(pasta_origem)

    for arquivo in arquivos:
        caminho_completo = os.path.join(pasta_origem, arquivo)
        if os.path.isfile(caminho_completo):
            # Separar o nome do ficheiro e a extensão
            nome_arquivo, extensao = os.path.splitext(arquivo)
            extensao = extensao.lower()  # Converter para minúsculas para evitar problemas de case sensitive

            # Criar a pasta correspondente à extensão, caso não exista
            pasta_extensao = os.path.join(pasta_origem, extensao[1:].upper() + 's')  # Ignorar o ponto inicial da extensão
            os.makedirs(pasta_extensao, exist_ok=True)

            # Mover o ficheiro para a pasta de acordo com a extensão
            shutil.move(caminho_completo, os.path.join(pasta_extensao, arquivo))

#Função para selecionar a pasta de forma gráfica
def selecionar_pasta():
    pasta_origem = filedialog.askdirectory()
    if pasta_origem:
        separar_arquivos_por_extensao(pasta_origem)
        print("Arquivos separados com sucesso!")


