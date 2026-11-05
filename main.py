import tkinter as tk
from tkinter import messagebox
import time


MINUTOS_DE_ESTUDO = 60

# Quanto tempo de estudo até o aviso de treino (em minutos).
# Para testar rápido, troque 60 por 0.1 (são 6 segundos).

def criar_janela_escondida():
    root = tk.Tk()          # Cria a janela principal
    root.withdraw()         # esconde ela (só queremos os popups)
    root.attributes('-topmost', True)   #popups aparecem na frente de tudo
    return root

def avisar_treino(root):
   messagebox.showinfo(
    'Aviso de treino',
    'Hora de treinar!\nSó pode voltar depois de treinar!',
    parent=root,
)


def esperar_treino(root):
    # Repete até que o usuário confirme que treinou
    while True:
        treinou = messagebox.askyesno('Treino', 'Você já treinou?', parent=root)
        if treinou:
            return messagebox.showwarning('Ainda não', 'Então, vai treinar!', parent=root)
        time.sleep(60) # Espera 1 minuto antes de perguntar novamente
        


def main():
    root = criar_janela_escondida()
    print('Estudando... o aviso vem em breve.')
    time.sleep(MINUTOS_DE_ESTUDO * 60) # Converte minutos em segundos
    avisar_treino(root)
    esperar_treino(root)
    print('Treino concluído! Voltando aos estudos...')


main()