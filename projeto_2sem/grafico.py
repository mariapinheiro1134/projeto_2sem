from os import system

# ==============================================================================
# IMPORTAÇÃO DE BIBLIOTECAS
# ==============================================================================

import csv

# Importa a biblioteca padrão 'tkinter' para construir a interface gráfica (janela, botões) no Windows.
import tkinter as tk

# Importa o submódulo 'messagebox' do Tkinter para exibir caixas de diálogo pop-up de aviso ou erro.
from tkinter import messagebox

# Importa a biblioteca 'matplotlib.pyplot' para criar gráficos estatísticos e visuais.
import matplotlib.pyplot as plt

# Importa a classe 'FigureCanvasTkAgg' para integrar o gráfico do Matplotlib dentro da janela do Tkinter.
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg

system('cls')


nome_arquivo = r'Dados10.csv'

ROXO = "#211B35"
AMEIXA = "#493B69"
VIOLETA = "#8068A8"
LAVANDA = "#C7B8EA"
LILAS = "#F4F0FA"


def gerar_dashboard():
  datas = []
  temperaturas = []

  soma = 0
  total = 0

  try:

    with open(nome_arquivo, 'r', encoding='utf-8') as arquivo:

      leitor = csv.reader(arquivo, delimiter=';')

      next(leitor)

      for linha in leitor:

        if len(linha) >= 6:

          data_hora_completa = linha[0]

          data_hora = data_hora_completa.split(',')[-1].strip()

          temp_str = linha[1]

          temp_num = float(temp_str.replace(' °C', '').replace(',', '.'))

          datas.append(data_hora)
          temperaturas.append(temp_num)
          soma += temp_num
          total += 1

    if not temperaturas:
      messagebox.showwarning('Aviso', 'Nenhum dado encontrado para exibir.')
      return

    media = soma / total

    fig.clear()
    grafico = fig.add_subplot(111)
    grafico.set_facecolor("white")
    grafico.plot(datas, temperaturas, color=VIOLETA, marker="o")
    grafico.set_title(f"Temperatura Média: {media:.2f} °C", color=ROXO)
    grafico.set_xlabel("Horário", color=AMEIXA)
    grafico.set_ylabel("Temperatura (°C)", color=AMEIXA)
    grafico.tick_params(axis="x", rotation=45, colors=AMEIXA)
    grafico.tick_params(axis="y", colors=AMEIXA)
    grafico.grid(color=LAVANDA, linestyle="--", alpha=0.5)
    fig.tight_layout()
    
    canvas.draw()

  except FileNotFoundError:
    messagebox.showerror('Erro', "O arquivo 'Dados10.csv' não foi encontrado!")


janela = tk.Tk()
janela.title("Dashboard Meteorológico")
janela.geometry("750x600")
janela.configure(bg=LILAS)

tk.Label(
    janela, text="Dashboard Meteorológico",
    font=("Arial", 20, "bold"), bg=ROXO, fg="white", pady=15
).pack(fill="x")

tk.Button(
    janela, text="Gerar Gráfico", command=gerar_dashboard,
    bg=VIOLETA, fg="white", font=("Arial", 11, "bold"),
    relief="flat", padx=15, pady=8
).pack(pady=12)

fig = plt.Figure(figsize=(7, 4), dpi=100)
fig.patch.set_facecolor(LILAS)

canvas = FigureCanvasTkAgg(fig, master=janela)
canvas.get_tk_widget().pack(fill="both", expand=True, padx=15, pady=10)

janela.mainloop()
