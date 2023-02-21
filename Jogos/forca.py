import random

def jogar():
    print("*********************************")
    print("***Bem vindo ao jogo da Forca!***")
    print("*********************************")

    palavra_secreta = "paralelepipido".upper()

    arquivo = open("palavras.txt", "r")
    palavras = []

    for linha in arquivo:
        linha = linha.strip()
        palavras.append(linha)

    arquivo.close()

    numero = random.randrange(0, len(palavras))
    palavra_secreta = palavras[numero].upper()

    letras_acertadas = ["_" for letra in palavra_secreta]

    enforcou = False
    acertou = False
    erros = 0

    #Vai rodar o loop enquanto o jogador não ganhou nem perdeu
    while(not enforcou and not acertou):

        chute = input("Qual a letra? ")
        #retira os espaços dos dois lados
        chute = chute.strip().upper()

        if(chute in palavra_secreta):
            index = 0
            for letra in palavra_secreta:
                #Colocar a função upper permite as entradas recebidas pelo usuário seja maiuscula ou minuscula
                 if(chute == letra):
                     #Substitui o sublinhado pela letra encontrada
                    letras_acertadas[index] = letra
                 index += 1
        else:
            #Conta quantos erros o usuário cometeu
            erros +=1
            print(f"Ops, você errou! Faltam {6-erros} tentativas.")

        #Verifica se o usuário perdeu
        if(erros == 6):
            enforcou = True

        #Verifica se o usuário ganhou
        if("_" not in letras_acertadas):
            acertou = True

        #como está dentro de um while, esse valor vai ser atualizado a cada iteração do laço
        print(letras_acertadas)

    #Mostra se o usuário ganhou ou perdeu
    if(acertou == True):
        print("Você ganhou, parabéns!")
    else:
        print("Você perdeu, mais sorte na próxima")

    #Mensagem mostrada quando as iterações param
    print("Fim do jogo")

if(__name__ == "__main__"):
    jogar()
