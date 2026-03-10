# Calculadora Python com Histórico
#Este é um projeto de calculadora funcional desenvolvida em Python, focada em lógica de programação, manipulação de listas e uso de funções.

## Funcionalidades
#- Operações matemáticas básicas: Soma, Subtração, Multiplicação e Divisão.
#- **Sistema de Histórico:** Armazena todas as operações realizadas durante a sessão.
#- **Tratamento de Erros:** Verificação para divisão por zero e operações inválidas.

## Tecnologias Utilizadas
# - **Python 3**
# - Conceitos aplicados:
#  - Laços de repetição (`while`, `for`)
 # - Estruturas condicionais (`if`, `elif`, `else`)
 # - Funções (`def`)
 # - Listas para armazenamento de dados

## Como usar
#1. Execute o arquivo `calculadora.py`.
#2. Escolha entre iniciar uma nova conta ou usar o resultado anterior.
#3. Digite os números e a operação desejada.
#4. Visualize o histórico a qualquer momento quando solicitado.

def fazer_multiplicacao(n1, n2):
    return n1 * n2
def fazer_divisao(n1, n2):
    return n1 / n2
def fazer_soma(n1, n2):
    return n1 + n2
def fazer_subtracao(n1, n2):
    return n1 - n2
def exibir_historico(lista_contas):
    print(f'\n=== HISTORICO DE CONTAS ===')
    for contas in lista_contas:
        print(contas)
    print('===========================\n')

resultado = 0
historico = []
while True:
    continua = input('Deseja começar uma nova conta ou continuar com o resultado anterior?? (nova/continuar)\n')
    if continua == 'continuar':
        numero1 = resultado
    elif continua == 'nova':
       numero1 = float(input('digite o primeiro numero:\n'))
    else:
        print('operaçao invalida\n')
        continue
    conta = str(input('digite a operaçao (multiplicaçao = *) (soma = +) (subtraçao = -) (divisão = /)\n'))
    if conta not in ['*', '+', '-', '/']:
        print('operacao invalida\n')
        continue
    numero2 = float(input('digite o segundo numero:\n'))
    if conta == '*':
        resultado = fazer_multiplicacao(numero1, numero2)
        historico.append(f"{numero1} * {numero2} = {resultado}")
        print(f'o resultado é {resultado}\n')
    elif conta == '+':
        resultado = fazer_soma(numero1, numero2)
        historico.append(f"{numero1} + {numero2} = {resultado}")
        print(f'o valor é {resultado}\n')
    elif conta == '-':
        resultado = fazer_subtracao(numero1, numero2)
        historico.append(f"{numero1} - {numero2} = {resultado}")
        print(f'o resultado é {resultado}\n')
    elif conta == '/' and numero2 != 0:
        resultado = fazer_divisao(numero1, numero2)
        historico.append(f"{numero1} / {numero2} = {resultado}")
        print(f'o resultado é {resultado}\n')
    elif conta == '/' and numero2 == 0:
        historico.append(f'uma divisão por 0 não existe')
        print(f'uma divisão por 0 não existe\n')
    else:
        historico.append('operaçao invalida')
        print('operacao invalida\n')
    hist = input('deseja ver o historico de contas (sim,nao)\n')
    if hist == 'sim':
        exibir_historico(historico)
    sair = input('deseja fazer outra conta? (sim/nao)\n')
    if sair == 'nao':
        print('encerrando a calculadora...\n')
        break