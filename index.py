import random

iniciarJogo = True

while iniciarJogo:
    print("-------------------------------------------------")
    print("BEM VINDO AO JOGO DE ADIVINHAÇÃO!")
    print("Eu pensei em um número aleatório de 4 dígitos. Tente adivinhar!")
    print("Você tem 10 tentativas para acertar o número.")
    print("-------------------------------------------------")

    input("Digite alguma coisa para começar...")

    # Gera um número aleatório de 4 dígitos
    chave = random.randrange(1000, 9999)

    # Separa as casas decimais do número gerado
    milhar = chave // 1000
    centena = (chave // 100) % 10
    dezena = (chave // 10) % 10
    unidade = chave % 10

    # Loop de tentativas
    tentativas = 10
    while tentativas > 0:
        tentativas -= 1

        print("-------------------------------------------------")

        # Recebe a tentativa do usuário
        tentativa = int(input("Digite um número de 4 dígitos: "))

        # Separa as casas decimais da tentativa
        milharTentativa = tentativa // 1000
        centenaTentativa = (tentativa // 100) % 10
        dezenaTentativa = (tentativa // 10) % 10
        unidadeTentativa = tentativa % 10

        # Verifica se a tentativa é igual à chave
        if tentativa != chave:

            # Cria uma variável booleana para cada dígito
            isUnidadeCorreta = unidade == unidadeTentativa
            isDezenaCorreta = dezena == dezenaTentativa
            isCentenaCorreta = centena == centenaTentativa
            isMilharCorreto = milhar == milharTentativa

            chaveParcial = ""

            print("DICAS:")

            # Verifica a existencia de digitos iguais
            if (
                (unidade == dezena or unidade == centena or unidade == milhar) or
                (dezena == centena or dezena == milhar) or
                (centena == milhar)
            ):
                print("\t==> Há números repetidos na chave!")
            
            # Verifica cada dígito individualmente para exibir as dicas

            if not isMilharCorreto:
                chaveParcial += "_"

                if (
                    milharTentativa == unidade or
                    milharTentativa == dezena  or
                    milharTentativa == centena
                ):
                    print(f"\t==> O número {milharTentativa} está na chave, mas na posição errada.")
                else:
                    print(f"\t==> O número {milharTentativa} não está na chave.")
            else:
                chaveParcial += f"{milharTentativa}"

            if not isCentenaCorreta:
                chaveParcial += "_"

                if (
                    centenaTentativa == unidade or
                    centenaTentativa == dezena  or
                    centenaTentativa == milhar
                ):
                    print(f"\t==> O número {centenaTentativa} está na chave, mas na posição errada.")
                else:
                    print(f"\t==> O número {centenaTentativa} não está na chave.")
            else:
                chaveParcial += f"{centenaTentativa}"

            if not isDezenaCorreta:
                chaveParcial += "_"

                if (
                    dezenaTentativa == unidade or
                    dezenaTentativa == centena or
                    dezenaTentativa == milhar
                ):
                    print(f"\t==> O número {dezenaTentativa} está na chave, mas na posição errada.")
                else:
                    print(f"\t==> O número {dezenaTentativa} não está na chave.")
            else:
                chaveParcial += f"{dezenaTentativa}"

            if not isUnidadeCorreta:
                chaveParcial += "_"

                if (
                    unidadeTentativa == milhar or 
                    unidadeTentativa == centena or 
                    unidadeTentativa == dezena
                ):
                    print(f"\t==> O número {unidadeTentativa} está na chave, mas na posição errada.")

                else:
                    print(f"\t==> O número {unidadeTentativa} não está na chave.")
            else:
                chaveParcial += f"{unidadeTentativa}"

            # --- FIM DAS VERIFICAÇÕES DE DÍGITO ---

            print(f"Você ainda tem {tentativas} tentativas!")
            print(f"A chave parcial é: {chaveParcial}")

        else:
            print("-------------------------------------------------")
            print(f"Parabéns! Você acertou o número com {10 - tentativas} tentativas!")

            tentativas = 0
        
    print("Fim de jogo!")
    print(f"O número era {chave}.")
    print("-------------------------------------------------")

    continuar = int(input("Deseja jogar novamente? (1 = SIM - 0 = NAO): "))
    iniciarJogo = continuar == 1