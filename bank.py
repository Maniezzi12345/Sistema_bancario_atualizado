from datetime import datetime

conta = 500
NUMERO_SAQUES = 3
NUMERO_DEPOSITOS = 7
transacoes = []

while True:
    menu = int(input("""===============MENU================
    Digite a operação desejada:
                     
    [1] Depositar
    [2] Sacar
    [3] Extrato
    [4] Sair
                    
    => """))

    if menu == 1:
        while NUMERO_DEPOSITOS > 0:
            dinheiro_depositar = int(input("Digite um valor para depósito: "))
            if dinheiro_depositar < 0:
                print("Não é possível depositar esse valor. Digite outro valor válido:")

            else:
                conta += dinheiro_depositar
                NUMERO_DEPOSITOS -= 1
                data_hora = datetime.now().strftime("%d/%m/%Y %H:%M:%S")
                transacoes.append((f"Depósito: R${dinheiro_depositar:.2f}", data_hora))
                print(f"Saldo total da conta: R${conta:.2f}")
                print("Dinheiro depositado!")
                print("_______________________________________________________________________________")
                finalizar_deposito = int(input("Para finalizar a operação de depósito, digite [4] ou continue [1]: "))
               
                if finalizar_deposito == 4:
                    print("Operação de depósito finalizada!")
                    break

                elif finalizar_deposito == 1:
                    continue

                else:
                    break
        
        print("Você excedeu o limite de depósitos diários!")
        print(f"Saldo disponível: R${conta:.2f}")

    elif menu == 2:
        while NUMERO_SAQUES > 0:
            saque = int(input("Qual valor deseja sacar? "))
            if saque > 500 or saque < 5:
                print("Não é possível realizar saques acima de R$500,00 ou inferiores a R$5,00!")
                print(f"Saldo disponível na conta: R${conta:.2f}")
                print("_______________________________________________________________________________")

            else:
                if conta <= 0:
                    print("_______________________________________________________________________________")
                    print("Não há saldo suficiente para realizar o saque!")
                    print(f"Saldo disponível na conta: R${conta:.2f}")
                    print("Operação finalizada!")
                    print("_______________________________________________________________________________")
                    break

                else:
                    conta -= saque
                    NUMERO_SAQUES -= 1
                    data_hora = datetime.now().strftime("%d/%m/%Y %H:%M:%S")
                    transacoes.append((f"Saque: R${saque:.2f}", data_hora))
                    print("Saque liberado")
                    print("_______________________________________________________________________________")

                    finalizar_saque = int(input("Para finalizar a operação de saque, digite [4] ou continue [1]: "))
                    if finalizar_saque == 4:
                     print("Operação finalizada!")
                     break

                    elif finalizar_saque == 1:
                     continue

                    else:
                        break

        print("Você excedeu o limite de saques diários!")
        print(f"Saldo disponível: R${conta:.2f}")

    elif menu == 3:
        print("------- EXTRATO -----------------------------------------")
        for transacao, data_hora in transacoes:
            print(f"{transacao} / {data_hora}")
        print("----------------------------------------------------------")

    elif menu == 4:
        print("Operação finalizada!")
        break

    else:
        print("Número inválido, tente novamente!")
