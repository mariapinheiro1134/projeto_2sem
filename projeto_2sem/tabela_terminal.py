from os import system
import csv
system('cls')


nome_arquivo = r'Dados10.csv'

print(f'--- Lendo os dados e calculando a temperatura média: {nome_arquivo} ---\n')

soma_temperaturas = 0.0  
total_registros = 0  


try:
  
  with open(nome_arquivo, 'r', encoding='utf-8') as arquivo:
  
    leitor = csv.reader(arquivo, delimiter=';')

    cabecalho = next(leitor)

    print(
        f'{cabecalho[0]:<20} | {cabecalho[1]:<12} | {cabecalho[2]:<10} |'
        f' {cabecalho[3]:<12} | {cabecalho[4]:<13} | {cabecalho[5]:<6}'
    )
    print('-' * 85)  

    for linha in leitor:
      
      if len(linha) >= 6:
        
        data_hora = linha[0]  
        temperatura_str = linha[1]  
        umidade = linha[2]  
        pressao = linha[3]  
        luminosidade = linha[4]  
        chuva = linha[5]  

        
        temp_limpa = temperatura_str.replace(' °C', '').replace(',', '.')

        temperatura_num = float(temp_limpa)

        soma_temperaturas += (
            temperatura_num  
        )
        total_registros += (
            1  
        )
  
        print(
            f'{data_hora:<20} | {temperatura_str:<12} | {umidade:<10} |'
            f' {pressao:<12} | {luminosidade:<13} | {chuva:<6}'
        )


  print('-' * 85)

  if total_registros > 0:
  
    media_temperatura = soma_temperaturas / total_registros

    print(f'Temperatura Média da Turma/Período: {media_temperatura:.2f} °C')
  else:
    print('Nenhum dado encontrado para calcular a média.')


except FileNotFoundError:

  print(
      f"Erro: O arquivo '{nome_arquivo}' não foi encontrado no diretório especificado."
  )
except Exception as e:

  print(f'Ocorreu um erro inesperado: {e}')