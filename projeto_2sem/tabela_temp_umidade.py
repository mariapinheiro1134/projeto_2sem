from os import system 
import csv

import tkinter as tk

from tkinter import messagebox
system('cls')

def carregar_dados():

  soma = 0       
  total = 0        
  texto_resultado = (
      ''       )

  nome_arquivo = r'Dados10.csv'

  try:

    with open(nome_arquivo, 'r', encoding='utf-8') as arquivo:      
      leitor = csv.reader(arquivo, delimiter=';')

      next(leitor)

      for linha in leitor:
        if len(linha) >= 6:
          data_hora, temp_str, umidade = linha[0], linha[1], linha[2]

          texto_resultado += (
              f'Data: {data_hora} | Temp: {temp_str} | Umid: {umidade}\n'
          )

               
          temp_num = float(temp_str.replace(' °C', '').replace(',', '.'))
          soma += temp_num        
          total += 1        
      
      if total > 0:
        media = soma / total        
        texto_resultado += f'\nTemperatura Média: {media:.2f} °C'

      
      caixa_texto.delete('1.0', tk.END)
           
      caixa_texto.insert(tk.END, texto_resultado)

  except FileNotFoundError:
         
    messagebox.showerror('Erro', "O arquivo 'Dados10.csv' não foi encontrado!")


ROXO = "#211B35"
AMEIXA = "#493B69"
VIOLETA = "#8068A8"
LAVANDA = "#C7B8EA"
LILAS_CLARO = "#F4F0FA"
BRANCO = "#FFFFFF"

# JANELA
janela = tk.Tk()
janela.title("Dashboard Meteorológico")
janela.geometry("650x450")
janela.configure(bg=LILAS_CLARO)

# TÍTULO
titulo = tk.Label(
    janela,
    text="Dashboard Meteorológico",
    font=("Arial", 20, "bold"),
    bg=ROXO,
    fg=BRANCO,
    pady=18
)
titulo.pack(fill="x")

subtitulo = tk.Label(
    janela,
    text="Dados de temperatura e umidade",
    font=("Arial", 11),
    bg=LILAS_CLARO,
    fg=AMEIXA
)
subtitulo.pack(pady=12)

# BOTÃO
botao = tk.Button(
    janela,
    text="Carregar dados e calcular média",
    command=carregar_dados,
    bg=VIOLETA,
    fg=BRANCO,
    activebackground=AMEIXA,
    activeforeground=BRANCO,
    font=("Arial", 10, "bold"),
    relief="flat",
    padx=15,
    pady=10,
    cursor="hand2"
)
botao.pack(pady=8)

# CAIXA DE RESULTADOS
caixa_texto = tk.Text(
    janela,
    wrap=tk.WORD,
    font=("Arial", 11),
    bg=BRANCO,
    fg=ROXO,
    insertbackground=ROXO,
    relief="flat",
    highlightthickness=1,
    highlightbackground=LAVANDA,
    padx=12,
    pady=12
)
caixa_texto.pack(
    fill="both",
    expand=True,
    padx=20,
    pady=15
)

janela.mainloop()
