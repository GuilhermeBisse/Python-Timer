import tkinter as tk
from tkinter import filedialog, messagebox

continuar = messagebox.askyesno('Continuar', 'Deseja continuar?')
with open('arquivos/origemdestino.txt', 'w') as arq:
    arq.write('Origem, Destino \n')
    while continuar:
        origem = filedialog.askdirectory()
        destino = filedialog.askdirectory()
        arq.write(f'{origem}, {destino} \n')
        continuar = messagebox.askyesno('Continuar', 'Deseja continuar?')



