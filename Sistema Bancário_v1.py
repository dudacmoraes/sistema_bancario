saldo = 10000
limite_valor_saque = 500
limite_saque_diario = 3
extrato = ''

while True:
    print('=-' * 10)
    print('INÍCIO'.center(20))
    print('''[1] Saque
[2] Depósito
[3] Extrato
[4] Sair''')
    print('=-' * 10 )

    opcao = int(input('Escolha uma opção: '))
    while opcao not in [1, 2, 3, 4]:
        print('Opção inválida! Tente novamente.')
        opcao = int(input('Escolha uma opção: '))

    if opcao == 1:
        if limite_saque_diario == 0:
            print('Você atingiu seu limite de saques diário. Tente novamente no próximo dia útil!')
        else:
            print(f'Saldo atual: R${saldo:.2f}')
            print(f'Saques restantes: {limite_saque_diario}')
            while True:
                sacar = int(input('Quanto você deseja sacar? R$'))
                if sacar > 0:
                    if sacar <= limite_valor_saque:
                        if sacar <= saldo:
                            saldo -= sacar
                            print(f'Saque realizado!\nSaldo atual: R${saldo:.2f}')
                            limite_saque_diario -= 1
                            extrato += f'Saque: -R${sacar:.2f}\n'
                            break
                        else:
                            print('Saldo insuficiente para saque.')
                    else:
                        print('Saque negado. Seu limite de saque é R$500,00!')
                else:
                    print('Valor inválido. Digite um valor válido!')

    elif opcao == 2:
        print(f'Saldo atual: R${saldo:.2f}')
        while True:
            depositar = int(input('Quanto você deseja depositar? R$'))
            if depositar > 0:
                saldo += depositar
                print(f'Depósito realizado!\nSaldo atual: R${saldo:.2f}.')
                extrato += f'Depósito: +R${depositar:.2f}\n'
                break
            else:
                print('Valor inválido. Digite um valor válido!')

    elif opcao == 3:
        print('=======EXTRATO=======')
        if extrato:
            print(extrato)
            print(f'Saldo: R${saldo:.2f}')
        else:
            print('Não foram realizadas movimentações na conta.')

    elif opcao == 4:
        print('Saindo...')
        break

print('Acesso encerrado.')
