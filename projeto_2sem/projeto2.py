# Importa o módulo 'csv' para realizar a leitura segura do arquivo tabular.
import csv

# Importa a biblioteca padrão 'tkinter' para criar janelas e componentes visuais no Windows.
import tkinter as tk

# Importa a função 'messagebox' do Tkinter para exibir caixas de diálogo de erro ou alerta  .
from tkinter import messagebox


# --- FUNÇÃO EXECUTADA AO CLICAR NO BOTÃO ---
def carregar_dados():
  """Esta função é acionada pelo botão da interface.

  Ela lê o arquivo CSV, processa os dados, calcula a média e exibe tudo na
  caixa de texto da janela do Windows      .
  """
  # Variáveis acumuladoras e de controle
  soma = 0  # Acumula a soma das temperaturas para o cálculo da média      
  total = 0  # Conta o número de linhas válidas lidas      
  texto_resultado = (
      ''  # String que vai acumular todo o texto que aparecerá na tela      
  )

  # Define o caminho completo do arquivo CSV no Windows (usando 'r' para evitar conflito com barras)      
  nome_arquivo = r'C:\UNIP\Dados10.csv'

  try:
    # Abre o arquivo no modo de leitura ('r') com codificação UTF-8 para suportar acentos      
    with open(nome_arquivo, 'r', encoding='utf-8') as arquivo:
      # Prepara o leitor CSV informando que o separador de colunas é o ponto e vírgula (;)      
      leitor = csv.reader(arquivo, delimiter=';')

      # A função next() pula a primeira linha (cabeçalho), pois ela contém apenas títulos      
      next(leitor)

      # Percorre o arquivo linha por linha      
      for linha in leitor:
        # Verifica se a linha possui pelo menos 6 colunas para evitar erros      
        if len(linha) >= 6:
          # Extrai os dados principais de interesse de cada coluna      
          data_hora, temp_str, umidade = linha[0], linha[1], linha[2]

          # Concatena a linha formatada na variável de texto que será exibida na tela      
          texto_resultado += (
              f'Data: {data_hora} | Temp: {temp_str} | Umid: {umidade}\n'
          )

          # --- TRATAMENTO E CÁLCULO DA TEMPERATURA ---
          # Remove o texto " °C" e substitui vírgula por ponto para converter em número decimal (float)      
          temp_num = float(temp_str.replace(' °C', '').replace(',', '.'))
          soma += temp_num  # Adiciona a temperatura à soma total      
          total += 1  # Incrementa o contador de registros      

      # Verifica se existem registros válidos para calcular a média      
      if total > 0:
        media = soma / total  # Calcula a temperatura média aritmética      
        # Adiciona o resultado da média formatado com duas casas decimais ao final do texto      
        texto_resultado += f'\nTemperatura Média: {media:.2f} °C'

      # --- ATUALIZAÇÃO DA TELA (Interface Gráfica) ---
      # Limpa todo o conteúdo anterior que estava escrito na caixa de texto ('1.0' significa do início ao fim)      
      caixa_texto.delete('1.0', tk.END)
      # Insere o texto completo com os dados e a média dentro da caixa de texto da janela      
      caixa_texto.insert(tk.END, texto_resultado)

  except FileNotFoundError:
    # Caso o arquivo não seja encontrado no diretório, exibe uma janela de erro amigável para o usuário      
    messagebox.showerror('Erro', "O arquivo 'Dados10.csv' não foi encontrado!")


# --- CONSTRUÇÃO DA JANELA PRINCIPAL DO WINDOWS ---

# Inicializa a janela principal utilizando o Tkinter      
janela = tk.Tk()
janela.title('Dashboard Meteorológico - Python')  # Título da barra da janela      
janela.geometry(
    '600x400'
)  # Define as dimensões iniciais da janela (largura x altura em pixels)      

# Cria um botão interativo na janela      
# O parâmetro 'command' diz ao botão qual função executar quando for clicado ('carregar_dados')      
botao = tk.Button(
    janela,
    text='Carregar Dados e Calcular Média',
    command=carregar_dados,
    bg='#4CAF50',  # Cor de fundo verde do botão      
    fg='white',  # Cor do texto branco      
    font=('Arial', 10, 'bold'),  # Estilo e tamanho da fonte      
)
botao.pack(pady=10)  # Posiciona o botão na janela com um espaçamento vertical de 10 pixels      

# Cria uma caixa de texto multilinha com barra de rolagem para exibir os dados estruturados      
# Utiliza a fonte 'Courier New' (fonte monoespaçada) para manter o alinhamento visual perfeito      
caixa_texto = tk.Text(
    janela, wrap=tk.WORD, width=70, height=18, font=('Courier New', 9)
)
caixa_texto.pack(
    padx=10, pady=10
)  # Posiciona a caixa de texto na janela com margens      

# Mantém a janela do Windows aberta em execução contínua, aguardando cliques ou interações      
janela.mainloop()