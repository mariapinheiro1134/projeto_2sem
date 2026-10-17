from os import system

# Importa o módulo 'csv' nativo do Python, responsável por lidar de forma segura e organizada com arquivos em formato tabular (CSV).

import csv
system('cls')

# Define o caminho completo para o arquivo no Windows.
# O uso da letra 'r' (raw string) antes das aspas é fundamental para que o Python ignore as barras invertidas ('\'), evitando conflitos de formatação.

nome_arquivo = r'C:\UNIP\Dados10.csv'

# Exibe uma mensagem inicial no terminal indicando qual arquivo está sendo processado.

print(f'--- Lendo os dados e calculando a temperatura média: {nome_arquivo} ---\n')

# Variáveis acumuladoras para o cálculo da média matemática posterior:

soma_temperaturas = 0.0  # Vai somar o valor de todas as temperaturas válidas
total_registros = 0  # Vai contar quantas linhas de dados válidas foram lidas

# O bloco 'try...except' serve para proteger o programa contra erros inesperados,
# como a ausência do arquivo no diretório especificado.
try:
  # Abre o arquivo no modo de leitura ('r') utilizando a codificação 'utf-8',
  # o que garante a leitura correta de acentos e caracteres especiais.
  with open(nome_arquivo, 'r', encoding='utf-8') as arquivo:
    # A função 'csv.reader' interpreta o arquivo separando as colunas
    # utilizando o ponto e vírgula (;) como delimitador.
    leitor = csv.reader(arquivo, delimiter=';')

    # A função 'next()' lê e descarta a primeira linha (cabeçalho da tabela),
    # pois ela contém apenas os títulos das colunas e não números para cálculo.
    cabecalho = next(leitor)

    # Exibe o cabeçalho formatado na tela com colunas alinhadas.
    print(
        f'{cabecalho[0]:<20} | {cabecalho[1]:<12} | {cabecalho[2]:<10} |'
        f' {cabecalho[3]:<12} | {cabecalho[4]:<13} | {cabecalho[5]:<6}'
    )
    print('-' * 85)  # Linha divisória visual no terminal

    # Estrutura de repetição 'for' para percorrer linha por linha do arquivo.
    for linha in leitor:
      # Garante que a linha possui pelo menos 6 colunas preenchidas,
      # evitando erros caso o arquivo possua linhas em branco ou incompletas.
      if len(linha) >= 6:
        # Extrai os dados de cada coluna para variáveis com nomes claros:
        data_hora = linha[0]  # Coluna 0: Data e Horário
        temperatura_str = linha[1]  # Coluna 1: Temperatura (ex: "14.72 °C")
        umidade = linha[2]  # Coluna 2: Umidade
        pressao = linha[3]  # Coluna 3: Pressão atmosférica
        luminosidade = linha[4]  # Coluna 4: Luminosidade
        chuva = linha[5]  # Coluna 5: Indicador de chuva

        # --- TRATAMENTO DOS DADOS PARA CÁLCULO ---
        # Como a temperatura vem como texto acompanhado de unidade ("14.72 °C"),
        # precisamos limpar a string para conseguir realizar operações matemáticas:
        # 1. Substitui " °C" por vazio ("")
        # 2. Substitui eventual vírgula por ponto (padrão numérico do Python)
        temp_limpa = temperatura_str.replace(' °C', '').replace(',', '.')

        # Converte o texto tratado de string para número decimal (float)
        temperatura_num = float(temp_limpa)

        # Acumula os valores para o cálculo da média
        soma_temperaturas += (
            temperatura_num  # Adiciona a temperatura atual à soma total
        )
        total_registros += (
            1  # Incrementa em 1 a contagem de registros processados
        )

        # Exibe a linha de dados formatada e alinhada no console
        print(
            f'{data_hora:<20} | {temperatura_str:<12} | {umidade:<10} |'
            f' {pressao:<12} | {luminosidade:<13} | {chuva:<6}'
        )

  # --- CÁLCULO E EXIBIÇÃO DA MÉDIA FINAL ---
  print('-' * 85)
  # Verifica se foram encontrados registros válidos para evitar erro de divisão por zero
  if total_registros > 0:
    # Calcula a média dividindo a soma de todas as temperaturas pela quantidade de linhas
    media_temperatura = soma_temperaturas / total_registros

    # Exibe o resultado formatado no console limitando a 2 casas decimais (':.2f')
    print(f'Temperatura Média da Turma/Período: {media_temperatura:.2f} °C')
  else:
    print('Nenhum dado encontrado para calcular a média.')

# --- TRATAMENTO DE EXCEÇÕES (Erros) ---
except FileNotFoundError:
  # Caso o arquivo não exista no caminho informado, exibe um aviso amigável
  print(
      f"Erro: O arquivo '{nome_arquivo}' não foi encontrado no diretório especificado."
  )
except Exception as e:
  # Captura qualquer outro tipo de erro inesperado durante a execução
  print(f'Ocorreu um erro inesperado: {e}')