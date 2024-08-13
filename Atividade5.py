SaldoPoupança = 500
SaldoCorrente = 2000


for i in range(2):
    email = input("Digite seu Email: ")
    senha = input("Digite sua Senha: ")

    if (email == "Filipi" and senha == "1234"):

        print("Acesso permitido")
        
        print("\n=== Caixa Eletronico ===")
        print("1 - Saque")
        print("2 - Depósito")
        print("3 - Transferencia")
        print("4 - Saldo")
        print("5 - Sair")
        
        opcao = input("Escolha uma opção: ")
        match opcao:
            case "1":
                print("Você escolheu o Saque")
                saque = float(input("Informe o valor do Saque: R$ "))
                SaldoCorrente-=saque
                
                print(f"Seu Saque de R$ {saque} foi realizado com sucesso")
                
                print(f"Seu Saldo atual é de {SaldoCorrente}")
                break
            case "2":
                print("\n=== Depositar em qual conta? ===")
                print("1 - Conta Corrente")
                print("2 - conta Poupança")
                
                deposito = input("Escolha uma opção: ")
                match deposito:
                    case "1":
                        dep1 = float(input("Informe o valor do Depósito: R$ "))
                        SaldoCorrente+=dep1
                        
                        print(f"Seu Depósito de R$ {dep1} foi realizado com sucesso")
                        
                        print(f"Seu Saldo da CC atual é de {SaldoCorrente}")
                        break
                    case "2":
                        dep2 = float(input("Informe o valor do Depósito: R$ "))
                        SaldoPoupança+=dep2
                        
                        print(f"Seu Depósito de R$ {dep2} foi realizado com sucesso")
                    
                        print(f"Seu Saldo da Poupança atual é de {SaldoPoupança}")
                        break
            case "3":
                print("Você escolheu a transferencia")
                transferencia = float(input("Informe o valor da transferencia: R$ "))
                SaldoCorrente-=transferencia
                
                print(f"Sua Transferencia de R$ {transferencia} foi realizado com sucesso")
                
                print(f"Seu Saldo da CC atual é de {SaldoCorrente}")
                break             
            case "4":
                print("\n=== Saldo da Conta ===")
                print("1 - Conta Corrente")
                print("2 - conta Poupança")
                
                op = input("Escolha uma opção: ")
                match op:
                    case "1":
                        print(f"Seu Saldo CC é de R$ {SaldoCorrente}")
                    case "2":
                        print(f"Seu Saldo da Poupança é de R$ {SaldoPoupança}")           
            case "5":
                sair = print("Saindo do Caixa")
                break
    else:
        print("Acesso negado")
        if (i == 1):
            break
        resposta = bool(input("Tentar Novamente?"))
        if (resposta == True):
            print("Você tem apenas 1 chance")
                  
                  
                  
                  
                  
                  
            
        