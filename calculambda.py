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

            print('escolha sua operação: ')
            print('  + - x /  ')
            print('para sair digite "q"')
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
            elif operacao == ' ':
                print('error')
                calculadora()
            elif operacao == 'q':
                print('fechando a calculadora...')
                break
            else:
                calculadora()
        except ValueError as e:
            print("Digite um número...", e)
        else:
            break
calculadora()









