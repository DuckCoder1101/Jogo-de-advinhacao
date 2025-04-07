import random

iniciarJogo = True

while iniciarJogo:
    print("-------------------------------------------------")
    print("BEM VINDO AO JOGO DE ADIVINHAÇÃO!")
    print("Eu pensei em um número aleatório de 4 dígitos, tente adivinhar!")
    print("Você tem 10 tentativas para acertar o número.")
    print("-------------------------------------------------")

    input("Digite alguma coisa para começar...")

    chave = random.randrange(1000, 9999)

    milhar = chave // 1000
    centena = (chave // 100) % 10
    dezena = (chave // 10) % 10
    unidade = chave % 10

    tentativas = 10
    while tentativas > 0:
        tentativas -= 1

        print("-------------------------------------------------")

        tentativa = int(input("Digite um número de 4 dígitos: "))

        milharTentativa = tentativa // 1000
        centenaTentativa = (tentativa // 100) % 10
        dezenaTentativa = (tentativa // 10) % 10
        unidadeTentativa = tentativa % 10

        milharCorrigido = milhar
        centenaCorrigido = centena
        dezenaCorrigido = dezena
        unidadeCorrigido = unidade

        if tentativa != chave:

            isUnidadeCorreta = unidade == unidadeTentativa
            isDezenaCorreta = dezena == dezenaTentativa
            isCentenaCorreta = centena == centenaTentativa
            isMilharCorreto = milhar == milharTentativa

            chaveParcial = ""

            print("DICA:")
            jaTemDica = False

            if not isMilharCorreto:
                milharCorrigido = "_"

                if tentativas <= 5 and not jaTemDica:
                    jaTemDica = True

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

            if not isCentenaCorreta:
                centenaCorrigido = "_"

                if tentativas <= 5 and not jaTemDica:
                    jaTemDica = True
                    
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

            if not isDezenaCorreta:
                dezenaCorrigido = "_"

                if tentativas <= 5 and not jaTemDica:
                    jaTemDica = True

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

            if not isUnidadeCorreta:
                unidadeCorrigido = "_"

                if tentativas <= 5 and not jaTemDica:
                    jaTemDica = True
                    
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

            if tentativas > 0:
                print(f"Você ainda tem {tentativas} tentativas!")
                print(f"A chave parcial é: {milharCorrigido}{centenaCorrigido}{dezenaCorrigido}{unidadeCorrigido}")

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