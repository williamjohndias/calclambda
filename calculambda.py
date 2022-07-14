#calculadora com função lambda
def calculadora():
    addNum = lambda num1, num2: num1 + num2
    subNum = lambda num1, num2: num1 - num2
    divNum = lambda num1, num2: num1 / num2
    multNum = lambda num1, num2: num1 * num2
    while True:
        try:
            num1 = float(input('1 número: '))
            num2 = float(input('2 número: '))
            print('\noperações: \n')
            print('+\n-\nx\n/\n')
            print('para sair digite "q"\n')
            operacao = input('escolha a operação: ')
            if operacao == '+':
                print(addNum(num1, num2))
                calculadora()
            elif operacao == '-':
                print(subNum(num1, num2))
                calculadora()
            elif operacao == '/':
                print(divNum(num1, num2))
                calculadora()
            elif operacao == 'x':
                print(multNum(num1, num2))
                calculadora()
            elif operacao == 'q':
                print('fechando a calculadora...')
                break
            else:
                print('esta operação é inválida...')
                calculadora()
        except ValueError:
            print("Digite um número...")
        else:
            break
calculadora()









