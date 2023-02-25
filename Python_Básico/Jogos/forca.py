import random




def jogar():

    mensage_de_abertura()
    palavra_secreta = carrega_palavra_secreta()
    letras_acertadas = inicializa_mascara_da_palavra(palavra_secreta)


    #Váriveis usadas no while
    enforcou = False
    acertou = False
    erros = 0
    #Vai rodar o loop enquanto o jogador não ganhou nem perdeu
    while(not enforcou and not acertou):

        chute = chute_usuario()

        if(chute in palavra_secreta):
            marca_chute_correto(palavra_secreta, chute, letras_acertadas)
        else:
            #Conta quantos erros o usuário cometeu
            erros +=1
            desenha_forca(erros)

        #Verifica se o usuário perdeu
        if(erros == 7):
            enforcou = True

        #Verifica se o usuário ganhou
        if("_" not in letras_acertadas):
            acertou = True

        #como está dentro de um while, esse valor vai ser atualizado a cada iteração do laço
        print(letras_acertadas)

    #Mostra se o usuário ganhou ou perdeu
    if(acertou == True):
       imprime_mensagem_de_vitoria()
    else:
        imprime_mensagem_de_derrota(palavra_secreta)

def mensage_de_abertura():
    print("*********************************")
    print("***Bem vindo ao jogo da Forca!***")
    print("*********************************")

def carrega_palavra_secreta():
    arquivo = open("palavras.txt", "r")
    palavras = []

    for linha in arquivo:
        linha = linha.strip()
        palavras.append(linha)

    arquivo.close()

    numero = random.randrange(0, len(palavras))
    palavra_secreta = palavras[numero].upper()

    return palavra_secreta

def inicializa_mascara_da_palavra(palavra):
    return ["_" for letra in palavra]

def chute_usuario():
    chute = input("Qual a letra? ")
    # retira os espaços dos dois lados
    chute = chute.strip().upper()
    return chute


def marca_chute_correto(palavra_secreta, chute, letras_acertadas):
    index = 0
    for letra in palavra_secreta:
        # Colocar a função upper permite as entradas recebidas pelo usuário seja maiuscula ou minuscula
        if (chute == letra):
            # Substitui o sublinhado pela letra encontrada
            letras_acertadas[index] = letra
        index += 1


def imprime_mensagem_de_vitoria():
    print("Parabéns, você ganhou!")
    print("       ___________      ")
    print("      '._==_==_=_.'     ")
    print("      .-\\:      /-.    ")
    print("     | (|:.     |) |    ")
    print("      '-|:.     |-'     ")
    print("        \\::.    /      ")
    print("         '::. .'        ")
    print("           ) (          ")
    print("         _.' '._        ")
    print("        '-------'       ")


def imprime_mensagem_de_derrota(palavra_secreta):
    print("Puxa, você foi enforcado!")
    print("A palavra era {}".format(palavra_secreta))
    print("    _______________         ")
    print("   /               \       ")
    print("  /                 \      ")
    print("//                   \/\  ")
    print("\|   XXXX     XXXX   | /   ")
    print(" |   XXXX     XXXX   |/     ")
    print(" |   XXX       XXX   |      ")
    print(" |                   |      ")
    print(" \__      XXX      __/     ")
    print("   |\     XXX     /|       ")
    print("   | |           | |        ")
    print("   | I I I I I I I |        ")
    print("   |  I I I I I I  |        ")
    print("   \_             _/       ")
    print("     \_         _/         ")
    print("       \_______/           ")

def desenha_forca(erros):
    print("  _______     ")
    print(" |/      |    ")

    if(erros == 1):
        print(" |      (_)   ")
        print(" |            ")
        print(" |            ")
        print(" |            ")

    if(erros == 2):
        print(" |      (_)   ")
        print(" |      \     ")
        print(" |            ")
        print(" |            ")

    if(erros == 3):
        print(" |      (_)   ")
        print(" |      \|    ")
        print(" |            ")
        print(" |            ")

    if(erros == 4):
        print(" |      (_)   ")
        print(" |      \|/   ")
        print(" |            ")
        print(" |            ")

    if(erros == 5):
        print(" |      (_)   ")
        print(" |      \|/   ")
        print(" |       |    ")
        print(" |            ")

    if(erros == 6):
        print(" |      (_)   ")
        print(" |      \|/   ")
        print(" |       |    ")
        print(" |      /     ")

    if (erros == 7):
        print(" |      (_)   ")
        print(" |      \|/   ")
        print(" |       |    ")
        print(" |      / \   ")

    print(" |            ")
    print("_|___         ")
    print()

if(__name__ == "__main__"):
    jogar()
