import random

iniciarJogo = True

while iniciarJogo:
    print("-------------------------------------------------")
    print("BEM VINDO AO JOGO DE ADIVINHAÇÃO!")
    print("Eu pensei em um número aleatório de 4 dígitos, tente adivinhar!")
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
            if tentativas <= 5:
                if (
                    (unidade == dezena or unidade == centena or unidade == milhar) or
                    (dezena == centena or dezena == milhar) or
                    (centena == milhar)
                ):
                    print("\t=>HÁ números repetidos na chave!")
                else:
                    print("\t=>NÃO HÁ números repetidos na chave!")

            # Verifica cada dígito individualmente para exibir as dicas
            if not isMilharCorreto:
                chaveParcial += "_"

                # Verifica se o milhar é maior que 5
                if tentativas <= 5:
                    if milhar > 5:
                        print(f"\t=>O primeiro número é MAIOR que 5!")
                    else:
                        print(f"\t=>O primeiro número é MENOR que 5!")

                if (
                    milharTentativa == unidade or
                    milharTentativa == dezena  or
                    milharTentativa == centena
                ):
                    print(f"\t=>O número {milharTentativa} está na chave, mas na posição errada.")
            else:
                chaveParcial += f"{milharTentativa}"

            if not isCentenaCorreta:
                chaveParcial += "_"

                # Verifica se a centena é par
                if tentativas <= 5:
                    if centena % 2 == 0:
                        print("\t=>O segundo número é PAR!")
                    else:
                        print("\t=>O segundo número é ÍMPAR!")

                if (
                    centenaTentativa == unidade or
                    centenaTentativa == dezena  or
                    centenaTentativa == milhar
                ):
                    print(f"\t=>O número {centenaTentativa} está na chave, mas na posição errada.")
            else:
                chaveParcial += f"{centenaTentativa}"

            if not isDezenaCorreta:
                chaveParcial += "_"

                # Verifica se a dezena é maior que 5
                if tentativas <= 5:
                    if dezena > 5:
                        print(f"\t=>O terceiro número é MAIOR que 5!")
                    else:
                        print(f"\t=>O terceiro número é MENOR que 5!")

                if (
                    dezenaTentativa == unidade or
                    dezenaTentativa == centena or
                    dezenaTentativa == milhar
                ):
                    print(f"\t=>O número {dezenaTentativa} está na chave, mas na posição errada.")
            else:
                chaveParcial += f"{dezenaTentativa}"

            if not isUnidadeCorreta:
                chaveParcial += "_"

                # Verifica se a unidade é par ou ímpar
                if tentativas <= 5:
                    if unidade % 2 == 0:
                        print("\t=>O ultimo número é PAR!")
                    else:
                        print("\t=>O ultimo número é ÍMPAR!")
                
                if (
                    unidadeTentativa == milhar or 
                    unidadeTentativa == centena or 
                    unidadeTentativa == dezena
                ):
                    print(f"\t=>O número {unidadeTentativa} está na chave, mas na posição errada.")
            else:
                chaveParcial += f"{unidadeTentativa}"

            # --- FIM DAS VERIFICAÇÕES DE DÍGITO ---

            if tentativas > 0:
                print(f"Você ainda tem {tentativas} tentativas!")
                print(f"A chave parcial é: {chaveParcial}")

        else:
            print("-------------------------------------------------")
            print(f"Parabéns! Você acertou o número com {10 - tentativas} tentativas!")

            tentativas = 0
        
    print("-------------------------------------------------")
    print("Fim de jogo! Você não acertou o número.")
    print(f"O número era {chave}.")
    print("-------------------------------------------------")

    continuar = int(input("Deseja jogar novamente? (1 = SIM - 0 = NAO): "))
    iniciarJogo = continuar == 1