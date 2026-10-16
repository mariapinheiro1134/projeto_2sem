### Código Documentado
# Este código une a leitura dos dados do arquivo CSV, o cálculo da temperatura média 
# e a geração dinâmica de um gráfico interativo com a biblioteca matplotlib embutido 
# numa janela do tkinter.

# ==============================================================================
# IMPORTAÇÃO DE BIBLIOTECAS
# ==============================================================================

# Importa o módulo 'csv' para realizar a leitura segura de arquivos tabulares separados por delimitador.
import csv

# Importa a biblioteca padrão 'tkinter' para construir a interface gráfica (janela, botões) no Windows.
import tkinter as tk

# Importa o submódulo 'messagebox' do Tkinter para exibir caixas de diálogo pop-up de aviso ou erro.
from tkinter import messagebox

# Importa a biblioteca 'matplotlib.pyplot' para criar gráficos estatísticos e visuais.
import matplotlib.pyplot as plt

# Importa a classe 'FigureCanvasTkAgg' para integrar o gráfico do Matplotlib dentro da janela do Tkinter.
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg

# ==============================================================================
# CONFIGURAÇÃO DE CAMINHO
# ==============================================================================

# Define a variável com o caminho completo do arquivo CSV no Windows.
# O caractere 'r' antes da string indica "raw string", evitando que barras invertidas (\) sejam lidas como caracteres de escape.
nome_arquivo = r'C:\UNIP\Dados10.csv'


# ==============================================================================
# FUNÇÃO PRINCIPAL: GERAR DASHBOARD E GRÁFICO
# ==============================================================================
def gerar_dashboard():
  """Esta função é acionada pelo botão da interface.

  Ela abre o arquivo CSV, processa as linhas para extrair os horários e
  temperaturas,
  calcula estatísticas e desenha o gráfico atualizado dentro da janela.
  """
  # Listas vazias que irão armazenar os dados extraídos do arquivo para popular o gráfico
  datas = []
  temperaturas = []

  # Variáveis acumuladoras para o cálculo da média
  soma = 0
  total = 0

  try:
    # Abre o arquivo CSV no modo leitura ('r') utilizando a codificação UTF-8 para aceitar acentuação
    with open(nome_arquivo, 'r', encoding='utf-8') as arquivo:
      # Configura o leitor de CSV informando que os campos são separados por ponto e vírgula (;)
      leitor = csv.reader(arquivo, delimiter=';')

      # Pula a primeira linha do arquivo, pois ela contém apenas o cabeçalho (títulos das colunas)
      next(leitor)

      # Loop que percorre o arquivo linha por linha
      for linha in leitor:
        # Verifica se a linha possui pelo menos 6 colunas para evitar erros de índice fora do limite
        if len(linha) >= 6:
          # Extrai a primeira coluna (data e hora completa)
          data_hora_completa = linha[0]

          # Utiliza .split(',') para pegar apenas a parte da hora (separada por vírgula) e .strip() para remover espaços em branco
          data_hora = data_hora_completa.split(',')[-1].strip()

          # Extrai a segunda coluna contendo a string da temperatura (ex: "25,5 °C")
          temp_str = linha[1]

          # --- TRATAMENTO E CONVERSÃO DOS DADOS ---
          # Remove a unidade " °C" e substitui a vírgula por ponto para que o Python consiga converter em número decimal (float)
          temp_num = float(temp_str.replace(' °C', '').replace(',', '.'))

          # Adiciona os valores tratados às respectivas listas e variáveis de cálculo
          datas.append(data_hora)
          temperaturas.append(temp_num)
          soma += temp_num
          total += 1

    # Valida se foram encontrados registros válidos para exibição
    if not temperaturas:
      messagebox.showwarning('Aviso', 'Nenhum dado encontrado para exibir.')
      return

    # Calcula a temperatura média aritmética geral
    media = soma / total

    # --- CRIAÇÃO E ATUALIZAÇÃO DO GRÁFICO COM MATPLOTLIB ---
    # Limpa a figura anterior do gráfico para evitar sobreposições caso o botão seja clicado várias vezes
    fig.clear()

    # Adiciona um subplot (gráfico 2D) na posição 111 (1 linha, 1 coluna, 1º gráfico)
    fig_plot = fig.add_subplot(111)

    # Plota os dados de horário (eixo X) versus temperatura (eixo Y) com marcadores circulares e linha vermelha
    fig_plot.plot(
        datas,
        temperaturas,
        marker='o',
        color='tab:red',
        linestyle='-',
        linewidth=2,
    )

    # Configura os títulos e rótulos dos eixos do gráfico, incluindo a média calculada no título principal
    fig_plot.set_title(
        f'Evolução da Temperatura ao Longo do Tempo (Média: {media:.2f} °C)'
    )
    fig_plot.set_xlabel('Horário')
    fig_plot.set_ylabel('Temperatura (°C)')

    # Rotaciona os rótulos do eixo X em 45 graus para melhorar a legibilidade dos horários
    fig_plot.tick_params(axis='x', rotation=45)

    # Ajusta o layout automaticamente para que nenhum elemento seja cortado na janela
    fig.tight_layout()

    # Atualiza o componente visual (Canvas) na tela para renderizar o novo gráfico gerado
    canvas.draw()

  except FileNotFoundError:
    # Exibe uma mensagem de erro em janela pop-up caso o arquivo não seja localizado no caminho especificado
    messagebox.showerror('Erro', "O arquivo 'Dados10.csv' não foi encontrado!")


# ==============================================================================
# CONSTRUÇÃO DA INTERFACE GRÁFICA (GUI) COM TKINTER
# ==============================================================================

# Inicializa a janela principal do aplicativo Windows
janela = tk.Tk()
janela.title('Dashboard Meteorológico Avançado - Tkinter & Matplotlib')
janela.geometry('750x600')  # Define o tamanho inicial da janela (Largura x Altura)

# Cria o botão interativo na janela
botao = tk.Button(
    janela,
    text='Carregar Dados e Gerar Gráfico',
    command=gerar_dashboard,  # Associa o clique do botão à função principal criada acima
    bg='#2196F3',  # Cor de fundo azul do botão
    fg='white',  # Cor do texto do botão (branco)
    font=('Arial', 10, 'bold'),  # Família, tamanho e estilo da fonte
)
botao.pack(
    pady=10
)  # Posiciona o botão na janela com espaçamento vertical (padding) de 10 pixels

# Cria a figura base do Matplotlib com dimensões de 7x4 polegadas e resolução de 100 DPI
fig = plt.Figure(figsize=(7, 4), dpi=100)

# Integra a figura do Matplotlib dentro de um componente de tela (Canvas) compatível com o Tkinter
canvas = FigureCanvasTkAgg(fig, master=janela)
canvas.get_tk_widget().pack(
    padx=10, pady=10, fill=tk.BOTH, expand=True
)  # Expande e centraliza o gráfico na janela

# Mantém a janela aberta em loop contínuo, aguardando interações do usuário (como cliques)
janela.mainloop()
