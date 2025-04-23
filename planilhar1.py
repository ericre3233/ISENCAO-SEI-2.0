import ttkbootstrap as ttk
from ttkbootstrap.constants import *
from typing import Self
from botcity.core import DesktopBot
from isencaogerados1 import isencaogerados1
from enviarger import enviarger
import webbrowser
import sys
import os
import threading
import keyboard

link_file = "link.txt"  # Nome do arquivo para armazenar o link

contagem = [
    "1", "2", "3", "4", "5", "6", "7", "8", "9", "10", "11", "12", "13", "14", "15", "16", "17", "18", "19", "20",
    "21", "22", "23", "24", "25", "26", "27", "28", "29", "30", "35", "40", "45", "50", "100", "150", "200", "250",
    "300", "350"
]

def save_link(link):
    with open(link_file, "w") as file:
        file.write(link)

def load_link():
    if os.path.exists(link_file):
        with open(link_file, "r") as file:
            return file.read().strip()
    return ""

link_salvo = load_link()  # Carregar o link ao iniciar o bot

def release_keys():
    if keyboard.is_pressed('ctrl'):
        keyboard.release('ctrl')
    if keyboard.is_pressed('shift'):
        keyboard.release('shift')

def interromper():
    while True:
        if keyboard.is_pressed('e'):
            release_keys()
            os._exit(0)

def parar():
    while True:
        if keyboard.is_pressed('r'):
            release_keys()
            python = sys.executable
            os.execl(python, python, *sys.argv)

class Bot(DesktopBot):
    def action(self, execution=None):
        global link_salvo  # Usar a variável global

        def iniciar_isencao():
            cont = int(combo_contagem.get())
            threading.Thread(target=interromper).start()
            threading.Thread(target=parar).start()
            webbrowser.open(entry_link.get())
            isencaogerados1(0, cont, bot=self, self=self)

        def enviar_processos():
            cont = int(combo_contagem.get())
            threading.Thread(target=interromper).start()
            threading.Thread(target=parar).start()
            webbrowser.open(entry_link.get())
            enviarger(0, cont, bot=self, self=self)

        # Criar a janela principal
        app = ttk.Window(themename="darkly")  # Escolha um tema moderno
        app.title("PLANILHAR")
        app.geometry("500x400")

        # Alterar o fundo para branco
        app.configure(bg="white")

        # Criar estilos personalizados para os campos de entrada e combobox
        style = ttk.Style()
        style.configure("Custom.TEntry", fieldbackground="lightgray", foreground="black")
        style.configure("Custom.TCombobox", fieldbackground="lightgray", foreground="black")

        # Layout
        ttk.Label(app, text="Link:", anchor="center", background="white", foreground="black").pack(pady=5)
        entry_link = ttk.Entry(app, width=50, style="Custom.TEntry")
        entry_link.insert(0, link_salvo)
        entry_link.pack(pady=5)

        ttk.Label(app, text="Quantidade de processos para planilhar:", anchor="center", background="white", foreground="black").pack(pady=5)
        combo_contagem = ttk.Combobox(app, values=contagem, width=10, style="Custom.TCombobox")
        combo_contagem.set(contagem[0])
        combo_contagem.pack(pady=5)

        ttk.Label(app, text="Comandos:", anchor="center", background="white", foreground="black").pack(pady=5)
        ttk.Label(app, text="Pressione 'p' para voltar ao menu principal.", anchor="center", background="white", foreground="black").pack()
        ttk.Label(app, text="Pressione 'e' para interromper e fechar.", anchor="center", background="white", foreground="black").pack()

        ttk.Button(app, text="ISENÇÃO DE IPVA / ICMS - TAXI / PCD - GERADOS", command=iniciar_isencao).pack(pady=10)
        ttk.Button(app, text="ENVIAR PROCESSOS - COORD - GERADOS", command=enviar_processos).pack(pady=10)

        # Salvar o link ao fechar
        def on_close():
            save_link(entry_link.get())
            app.destroy()

        app.protocol("WM_DELETE_WINDOW", on_close)
        app.mainloop()

    def not_found(self, label):
        print(f"Element not found: {label}")

if __name__ == '__main__':
    Bot.main()