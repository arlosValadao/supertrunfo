from random import randint
from os import system, name
from time import sleep


pontuacao_jogador1 = 0
pontuacao_jogador2 = 0
j1_carta1_nome = "nome carta 1"
j1_carta1_ataque = 0
j1_carta1_defesa = 0
j1_carta1_velocidade = 0
j1_carta2_nome = "nome carta 2"
j1_cata2_ataque = 0
j1_carta2_defesa = 0
j1_carta2_velocidade = 0
j1_carta3_nome = "nome carta 3"
j1_carta3_ataque = 0
j1_carta3_defesa = 0
j1_carta3_velocidade: int = 0
j2_carta4_nome = "nome carta 4"
j2_carta4_ataque = 0
j2_carta4_defesa = 0
j2_carta4_velocidade = 0
j2_carta5_nome = "nome carta 5"
j2_carta5_ataque = 0
j2_carta5_defesa = 0
j2_carta5_velocidade = 0
j2_carta6_nome = "nome carta 6"
j2_carta6_ataque = 0
j2_carta6_defesa = 0
j2_carta6_velocidade = 0
recorde = 0
escolha = ""
TEXTO_MENU = "\t  [ 1 ] -  NOVO JOGO \n \t" + \
    "  [ 2 ] - INFORMAÇÕES SOBRE O JOGO" + \
    " \n \t  [ 3 ] - SAIR DO JOGO"
# Valores fixos  correspondentes a cada atributo
ATAQUE = 120
DEFESA = 110
VELOCIDADE = 100


def informacoes_jogo():
    cls()
    cabecalho(" I N F O.  S O B R E  O  J O G O")
    print("1 - Deve-se definir o nome dos dois jogadores\n")
    print("2 - Os jogadores ficam encarregados de definir a quantiade de rodadas da partida\n")
    print("3 - Os dois jogadores receberão, de forma aleatória, 3 cartas com 3 atributos, ataque, defesa e velocidade.\n")
    print("4 - Todos atributos possuem valores aleatórios e são alterados a cada rodada\n")
    print("5 - O jogador que iniciar a primeira rodada fica encarregado de escolher um atributo e uma carta para jogar\n")
    print("6 - Conhecendo o atributo escolhido pelo primeiro jogador, o segundo jogador deve escolher uma carta e jogar\n")
    print("7 - Os valores dos atributos são expostos para ambos os jogadores e o vencedor da rodada e anunciado\n")
    print("8 - Uma nova rodada se inicia")
    input("\033[31m \tPressione <ENTER> para continuar\033[m")
    cls()


def cls():
    system("cls" if name == "nt" else "clear")


def cabecalho(texto=''):
    print('╔' + '═' * 78 + '╗')
    print('║ {:^76} ║'.format('S U P E R   T R U N F O  '))
    print('╚' + '═' * 78 + '╝')
    if texto != '':
        # print("\n{:^80}\n".format(texto))
        print("\n\033[1m{:^80}\033[m  ".format(texto))
        print("─" * 80)


while escolha != 3:
    cabecalho(TEXTO_MENU)
    while escolha != "1" and escolha != "2" and escolha != "3":
        escolha = input("\t\t\033[1m[1/2/3]?\033[m")
    escolha = int(escolha)
    if escolha == 1:
        nome_jogador1 = input(
            "\n\n\t[ - ] Digite o nome do primeiro jogador: ")
        print("\n")
        nome_jogador2 = input("\t[ - ] Digite o nome do segundo jogador: ")
        print("\n")
        numero_rodadas = ""
        while numero_rodadas != "1" and numero_rodadas != "2" and numero_rodadas != "3":
            numero_rodadas = input(
                "\t[ - ] Digite a quantidadede de rodadas uma vez que o minino e 3:  ")
        cls()
        vez_jogar = randint(1, 2)
        for rodada in range(int(numero_rodadas)):

            j1_carta1_nome = "  Leônidas"
            j1_carta1_ataque = randint(0, 70)
            j1_carta1_defesa = randint(0, 80)
            j1_carta1_velocidade = randint(0, 90)
            j1_carta2_nome = "  Dilios"
            j1_carta2_ataque = randint(0, 70)
            j1_carta2_defesa = randint(0, 80)
            j1_carta2_velocidade = randint(0, 90)
            j1_carta3_nome = "  Plistarco"
            j1_carta3_ataque = randint(0, 70)
            j1_carta3_defesa = randint(0, 80)
            j1_carta3_velocidade = randint(0, 90)
            j2_carta4_nome = "  Xerxes"
            j2_carta4_ataque = randint(0, 70)
            j2_carta4_defesa = randint(0, 80)
            j2_carta4_velocidade = randint(0, 90)
            j2_carta5_nome = "Rainha Gorgo"
            j2_carta5_ataque = randint(0, 70)
            j2_carta5_defesa = randint(0, 80)
            j2_carta5_velocidade = randint(0, 90)
            j2_carta6_nome = "  Pítia"
            j2_carta6_ataque = randint(0, 70)
            j2_carta6_defesa = randint(0, 80)
            j2_carta6_velocidade = randint(0, 90)

            if vez_jogar % 2 == 1:
                if vez_jogar == 1:
                    input(
                        "\n\n\n\n\t\t\t%s C O M E C A   J O G A N D O\n\t\t< ENTER > P A R A   C O N T I N U A R" % nome_jogador1)
                    cls()
                else:
                    input(
                        "\t\tA G O R A  E  A  V E Z  D E %s\n\t\t< ENTER > P A R A   C O N T I N U A R" % nome_jogador1)
                    cls()
                vez_jogar += 1

                print("#" * 30)
                print("#" + "\t\033[31mID - [  1  ]\033[m" + " " * 9 + "#")
                print("#" * 30)
                print("#" + "\t%s" % j1_carta1_nome + " " * 9 + "#")
                print("#" * 30)
                print("#" + "\tAtaque: %d" % j1_carta1_ataque + " " * 11 + "#")
                print("#" * 30)
                print("#" + "\tDefesa: %d" % j1_carta1_defesa + " " * 11 + "#")
                print("#" * 30)
                print("#" + "\tVelocidade: %d" %
                      j1_carta1_velocidade + " " * 7 + "#")
                print("#" * 30 + "\n\n")

                print("#" * 30)
                print("#" + "\t\033[31mID - [  2  ]\033[m" + " " * 9 + "#")
                print("#" * 30)
                print("#" + "\t%s" % j1_carta2_nome + " " * 9 + "#")
                print("#" * 30)
                print("#" + "\tAtaque: %d" % j1_carta2_ataque + " " * 11 + "#")
                print("#" * 30)
                print("#" + "\tDefesa: %d" % j1_carta2_defesa + " " * 11 + "#")
                print("#" * 30)
                print("#" + "\tVelocidade: %d" %
                      j1_carta2_velocidade + " " * 7 + "#")
                print("#" * 30 + "\n\n")

                print("#" * 30)
                print("#" + "\t\033[31mID - [  3  ]\033[m" + " " * 9 + "#")
                print("#" * 30)
                print("#" + "\t%s" % j1_carta3_nome + " " * 9 + "#")
                print("#" * 30)
                print("#" + "\tAtaque: %d" % j1_carta3_ataque + " " * 11 + "#")
                print("#" * 30)
                print("#" + "\tDefesa: %d" % j1_carta3_defesa + " " * 11 + "#")
                print("#" * 30)
                print("#" + "\tVelocidade: %d" %
                      j1_carta3_velocidade + " " * 7 + "#")
                print("#" * 30 + "\n\n")

                print("\tA T R I B U T O S   D I S P O N I V E I S\n")
                print("\t[ 1 ] - Ataque")
                print("\t[ 2 ] - Defesa")
                print("\t[ 3 ] - Velocidade")
                atributo = ""
                while atributo != "1" and atributo != "2" and atributo != "3":
                    atributo = input("%s, escolha um atributo:" %
                                     nome_jogador1)

                j1_carta_escolhida = ""
                while j1_carta_escolhida != "1" and j1_carta_escolhida != "2" and j1_carta_escolhida != "3":
                    j1_carta_escolhida = input(
                        "%s, carta ID 1, 2 ou 3?:" % nome_jogador1)
                cls()
                input("\t\t\n\n\n%s, voce esta ai? <ENTER> para confirmar " %
                      nome_jogador2)
                cls()


                if int(atributo) == 1:
                    print("\n\t\t%s o jogador %s escolheu o atributo ATAQUE" %
                          (nome_jogador2, nome_jogador1))
                    sleep(5)
                elif int(atributo) == 2:
                    print("\n\t\t%s o jogador %s escolheu o atributo DEFESA" %
                          (nome_jogador2, nome_jogador1))
                    sleep(5)
                elif int(atributo) == 3:
                    print("\n\t\t%s o jogador %s escolheu o atributo VELOCIDADE" % (
                        nome_jogador2, nome_jogador1))
                    sleep(5)

                print("#" * 30)
                print("#" + "\t\033[31mID - [  4  ]\033[m" + " " * 9 + "#")
                print("#" * 30)
                print("#" + "\t%s" % j2_carta4_nome + " " * 9 + "#")
                print("#" * 30)
                print("#" + "\tAtaque: %d" % j2_carta4_ataque + " " * 11 + "#")
                print("#" * 30)
                print("#" + "\tDefesa: %d" % j2_carta4_defesa + " " * 11 + "#")
                print("#" * 30)
                print("#" + "\tVelocidade: %d" %
                      j2_carta4_velocidade + " " * 7 + "#")
                print("#" * 30 + "\n\n")

                print("#" * 30)
                print("#" + "\t\033[31mID - [  5  ]\033[m" + " " * 9 + "#")
                print("#" * 30)
                print("#" + "\t%s" % j2_carta5_nome + " " * 9 + "#")
                print("#" * 30)
                print("#" + "\tAtaque: %d" % j2_carta5_ataque + " " * 11 + "#")
                print("#" * 30)
                print("#" + "\tDefesa: %d" % j2_carta5_defesa + " " * 11 + "#")
                print("#" * 30)
                print("#" + "\tVelocidade: %d" %
                      j2_carta5_velocidade + " " * 7 + "#")
                print("#" * 30 + "\n\n")

                print("#" * 30)
                print("#" + "\t\033[31mID - [  6  ]\033[m" + " " * 9 + "#")
                print("#" * 30)
                print("#" + "\t%s" % j2_carta6_nome + " " * 9 + "#")
                print("#" * 30)
                print("#" + "\tAtaque: %d" % j2_carta6_ataque + " " * 11 + "#")
                print("#" * 30)
                print("#" + "\tDefesa: %d" % j2_carta6_defesa + " " * 11 + "#")
                print("#" * 30)
                print("#" + "\tVelocidade: %d" %
                      j2_carta6_velocidade + " " * 7 + "#")
                print("#" * 30 + "\n\n")

                j2_carta_escolhida = ""
                while j2_carta_escolhida != "4" and j2_carta_escolhida != "5" and j2_carta_escolhida != "6":
                    j2_carta_escolhida = input(
                        "%s, carta ID 4, 5 ou 6?:" % nome_jogador2)
                cls()
                if int(atributo) == 1 and int(j1_carta_escolhida) == 1 and int(j2_carta_escolhida) == 4:
                    if j1_carta1_ataque > j2_carta4_ataque:
                        print("\n\tValor do atributo de %s: %d" %
                              (nome_jogador1, j1_carta1_ataque))
                        print("\n\tValor do atributo de %s : %d" %
                              (nome_jogador2, j2_carta4_ataque))
                        print("\n\t%s possui maior valor de atributo, com %d pontos" % (
                            nome_jogador1, j1_carta1_ataque))
                        pontuacao_jogador1 += ATAQUE
                        sleep(7)
                        cls()
                    elif j1_carta1_ataque < j2_carta4_ataque:
                        print("\n\tValor do atributo de %s: %d" %
                              (nome_jogador1, j1_carta1_ataque))
                        print("\n\tValor do atributo de %s : %d" %
                              (nome_jogador2, j2_carta4_ataque))
                        print("\n\t%s possui maior valor de atributo, com %d pontos" % (
                            nome_jogador2, j2_carta4_ataque))
                        pontuacao_jogador2 += ATAQUE
                        sleep(7)
                        cls()
                    else:
                        print("\n\n\t\tE M P A T E ")
                        print("\t\t\033[mAguarde...\033[m")
                        sleep(7)
                        cls()

                elif int(atributo) == 1 and int(j1_carta_escolhida) == 1 and int(j2_carta_escolhida) == 5:
                    if j1_carta1_ataque > j2_carta5_ataque:
                        print("\n\tValor do atributo de %s: %d" %
                              (nome_jogador1, j1_carta1_ataque))
                        print("\n\tValor do atributo de %s : %d" %
                              (nome_jogador2, j2_carta5_ataque))
                        print("\n\t%s possui maior valor de atributo, com %d pontos" % (
                            nome_jogador1, j1_carta1_ataque))
                        pontuacao_jogador1 += ATAQUE
                        sleep(7)
                        cls()
                    elif j1_carta1_ataque < j2_carta5_ataque:
                        print("\n\tValor do atributo de %s: %d" %
                              (nome_jogador1, j1_carta1_ataque))
                        print("\n\tValor do atributo de %s : %d" %
                              (nome_jogador2, j2_carta5_ataque))
                        print("\n\t%s possui maior valor de atributo, com %d pontos" % (
                            nome_jogador2, j2_carta5_ataque))
                        pontuacao_jogador2 += ATAQUE
                        sleep(7)
                        cls()
                    else:
                        print("\n\n\t\tE M P A T E ")
                        print("\t\t\033[mAguarde...\033[m")
                        sleep(7)
                        cls()

                elif int(atributo) == 1 and int(j1_carta_escolhida) == 1 and int(j2_carta_escolhida) == 6:
                    if j1_carta1_ataque > j2_carta6_ataque:
                        print("\n\tValor do atributo de %s: %d" %
                              (nome_jogador1, j1_carta1_ataque))
                        print("\n\tValor do atributo de %s : %d" %
                              (nome_jogador2, j2_carta6_ataque))
                        print("\n\t%s possui maior valor de atributo, com %d pontos" % (
                            nome_jogador1, j1_carta1_ataque))
                        pontuacao_jogador1 += ATAQUE
                        sleep(7)
                        cls()
                    elif j1_carta1_ataque < j2_carta6_ataque:
                        print("\n\tValor do atributo de %s: %d" %
                              (nome_jogador1, j1_carta1_ataque))
                        print("\n\tValor do atributo de %s : %d" %
                              (nome_jogador2, j2_carta6_ataque))
                        print("\n\t%s possui maior valor de atributo, com %d pontos" % (
                            nome_jogador2, j2_carta6_ataque))
                        pontuacao_jogador2 += ATAQUE
                        sleep(7)
                        cls()
                    else:
                        print("\n\n\t\tE M P A T E ")
                        print("\t\t\033[mAguarde...\033[m")
                        sleep(7)
                        cls()

                elif int(atributo) == 1 and int(j1_carta_escolhida) == 2 and int(j2_carta_escolhida) == 4:
                    if j1_carta2_ataque > j2_carta4_ataque:
                        print("\n\tValor do atributo de %s: %d" %
                              (nome_jogador1, j1_carta2_ataque))
                        print("\n\tValor do atributo de %s : %d" %
                              (nome_jogador2, j2_carta4_ataque))
                        print("\n\t%s possui maior valor de atributo, com %d pontos" % (
                            nome_jogador1, j1_carta2_ataque))
                        pontuacao_jogador1 += ATAQUE
                        sleep(7)
                        cls()
                    elif j1_carta2_ataque < j2_carta4_ataque:
                        print("\n\tValor do atributo de %s: %d" %
                              (nome_jogador1, j1_carta2_ataque))
                        print("\n\tValor do atributo de %s : %d" %
                              (nome_jogador2, j2_carta4_ataque))
                        print("\n\t%s possui maior valor de atributo, com %d pontos" % (
                            nome_jogador2, j2_carta4_ataque))
                        pontuacao_jogador2 += ATAQUE
                        sleep(7)
                        cls()
                    else:
                        print("\n\n\t\tE M P A T E ")
                        print("\t\t\033[mAguarde...\033[m")
                        sleep(7)
                        cls()

                elif int(atributo) == 1 and int(j1_carta_escolhida) == 2 and int(j2_carta_escolhida) == 5:
                    if j1_carta2_ataque > j2_carta5_ataque:
                        print("\n\tValor do atributo de %s: %d" %
                              (nome_jogador1, j1_carta2_ataque))
                        print("\n\tValor do atributo de %s : %d" %
                              (nome_jogador2, j2_carta5_ataque))
                        print("\n\t%s possui maior valor de atributo, com %d pontos" % (
                            nome_jogador1, j1_carta2_ataque))
                        pontuacao_jogador1 += ATAQUE
                        sleep(7)
                        cls()
                    elif j1_carta2_ataque < j2_carta5_ataque:
                        print("\n\tValor do atributo de %s: %d" %
                              (nome_jogador1, j1_carta2_ataque))
                        print("\n\tValor do atributo de %s : %d" %
                              (nome_jogador2, j2_carta5_ataque))
                        print("\n\t%s possui maior valor de atributo, com %d pontos" % (
                            nome_jogador2, j2_carta5_ataque))
                        pontuacao_jogador2 += ATAQUE
                        sleep(7)
                        cls()
                    else:
                        print("\n\n\t\tE M P A T E ")
                        print("\t\t\033[mAguarde...\033[m")
                        sleep(7)
                        cls()

                elif int(atributo) == 1 and int(j1_carta_escolhida) == 2 and int(j2_carta_escolhida) == 6:
                    if j1_carta2_ataque > j2_carta6_ataque:
                        print("\n\tValor do atributo de %s: %d" %
                              (nome_jogador1, j1_carta2_ataque))
                        print("\n\tValor do atributo de %s : %d" %
                              (nome_jogador2, j2_carta6_ataque))
                        print("\n\t%s possui maior valor de atributo, com %d pontos" % (
                            nome_jogador1, j1_carta2_ataque))
                        pontuacao_jogador1 += ATAQUE
                        sleep(7)
                        cls()
                    elif j1_carta2_ataque < j2_carta6_ataque:
                        print("\n\tValor do atributo de %s: %d" %
                              (nome_jogador1, j1_carta2_ataque))
                        print("\n\tValor do atributo de %s : %d" %
                              (nome_jogador2, j2_carta6_ataque))
                        print("\n\t%s possui maior valor de atributo, com %d pontos" % (
                            nome_jogador2, j2_carta6_ataque))
                        pontuacao_jogador2 += ATAQUE
                        sleep(7)
                        cls()
                    else:
                        print("\n\n\t\tE M P A T E ")
                        print("\t\t\033[mAguarde...\033[m")
                        sleep(7)
                        cls()

                elif int(atributo) == 1 and int(j1_carta_escolhida) == 3 and int(j2_carta_escolhida) == 4:
                    if j1_carta3_ataque > j2_carta4_ataque:
                        print("\n\tValor do atributo de %s: %d" %
                              (nome_jogador1, j1_carta3_ataque))
                        print("\n\tValor do atributo de %s : %d" %
                              (nome_jogador2, j2_carta4_ataque))
                        print("\n\t%s possui maior valor de atributo, com %d pontos" % (
                            nome_jogador1, j1_carta3_ataque))
                        pontuacao_jogador1 += ATAQUE
                        sleep(7)
                        cls()
                    elif j1_carta3_ataque < j2_carta4_ataque:
                        print("\n\tValor do atributo de %s: %d" %
                              (nome_jogador1, j1_carta3_ataque))
                        print("\n\tValor do atributo de %s : %d" %
                              (nome_jogador2, j2_carta4_ataque))
                        print("\n\t%s possui maior valor de atributo, com %d pontos" % (
                            nome_jogador2, j2_carta4_ataque))
                        pontuacao_jogador2 += ATAQUE
                        sleep(7)
                        cls()
                    else:
                        print("\n\n\t\tE M P A T E ")
                        print("\t\t\033[mAguarde...\033[m")
                        sleep(7)
                        cls()

                elif int(atributo) == 1 and int(j1_carta_escolhida) == 3 and int(j2_carta_escolhida) == 5:
                    if j1_carta3_ataque > j2_carta5_ataque:
                        print("\n\tValor do atributo de %s: %d" %
                              (nome_jogador1, j1_carta3_ataque))
                        print("\n\tValor do atributo de %s : %d" %
                              (nome_jogador2, j2_carta5_ataque))
                        print("\n\t%s possui maior valor de atributo, com %d pontos" % (
                            nome_jogador1, j1_carta3_ataque))
                        pontuacao_jogador1 += ATAQUE
                        sleep(7)
                        cls()
                    elif j1_carta3_ataque < j2_carta5_ataque:
                        print("\n\tValor do atributo de %s: %d" %
                              (nome_jogador1, j1_carta3_ataque))
                        print("\n\tValor do atributo de %s : %d" %
                              (nome_jogador2, j2_carta5_ataque))
                        print("\n\t%s possui maior valor de atributo, com %d pontos" % (
                            nome_jogador2, j2_carta5_ataque))
                        pontuacao_jogador2 += ATAQUE
                        sleep(7)
                        cls()
                    else:
                        print("\n\n\t\tE M P A T E ")
                        print("\t\t\033[mAguarde...\033[m")
                        sleep(7)
                        cls()

                elif int(atributo) == 1 and int(j1_carta_escolhida) == 3 and int(j2_carta_escolhida) == 6:
                    if j1_carta3_ataque > j2_carta6_ataque:
                        print("\n\tValor do atributo de %s: %d" %
                              (nome_jogador1, j1_carta3_ataque))
                        print("\n\tValor do atributo de %s : %d" %
                              (nome_jogador2, j2_carta6_ataque))
                        print("\n\t%s possui maior valor de atributo, com %d pontos" % (
                            nome_jogador1, j1_carta3_ataque))
                        pontuacao_jogador1 += ATAQUE
                        sleep(7)
                        cls()
                    elif j1_carta3_ataque < j2_carta6_ataque:
                        print("\n\tValor do atributo de %s: %d" %
                              (nome_jogador1, j1_carta3_ataque))
                        print("\n\tValor do atributo de %s : %d" %
                              (nome_jogador2, j2_carta6_ataque))
                        print("\n\t%s possui maior valor de atributo, com %d pontos" % (
                            nome_jogador2, j2_carta6_ataque))
                        pontuacao_jogador2 += ATAQUE
                        sleep(7)
                        cls()
                    else:
                        print("\n\n\t\tE M P A T E ")
                        print("\t\t\033[mAguarde...\033[m")
                        sleep(7)
                        cls()

                elif int(atributo) == 2 and int(j1_carta_escolhida) == 1 and int(j2_carta_escolhida) == 4:
                    if j1_carta1_defesa > j2_carta4_defesa:
                        print("\n\tValor do atributo de %s: %d" %
                              (nome_jogador1, j1_carta1_defesa))
                        print("\n\tValor do atributo de %s : %d" %
                              (nome_jogador2, j2_carta4_defesa))
                        print("\n\t%s possui maior valor de atributo, com %d pontos" % (
                            nome_jogador1, j1_carta1_defesa))
                        pontuacao_jogador1 += DEFESA
                        sleep(7)
                        cls()
                    elif j1_carta1_defesa < j2_carta4_defesa:
                        print("\n\tValor do atributo de %s: %d" %
                              (nome_jogador1, j1_carta1_defesa))
                        print("\n\tValor do atributo de %s : %d" %
                              (nome_jogador2, j2_carta4_defesa))
                        print("\n\t%s possui maior valor de atributo, com %d pontos" % (
                            nome_jogador2, j2_carta4_defesa))
                        pontuacao_jogador2 += DEFESA
                        sleep(7)
                        cls()
                    else:
                        print("\n\n\t\tE M P A T E ")
                        print("\t\t\033[mAguarde...\033[m")
                        sleep(7)
                        cls()

                elif int(atributo) == 2 and int(j1_carta_escolhida) == 1 and int(j2_carta_escolhida) == 5:
                    if j1_carta1_defesa > j2_carta5_defesa:
                        print("\n\tValor do atributo de %s: %d" %
                              (nome_jogador1, j1_carta1_defesa))
                        print("\n\tValor do atributo de %s : %d" %
                              (nome_jogador2, j2_carta5_defesa))
                        print("\n\t%s possui maior valor de atributo, com %d pontos" % (
                            nome_jogador1, j1_carta1_defesa))
                        pontuacao_jogador1 += DEFESA
                        sleep(7)
                        cls()
                    elif j1_carta1_defesa < j2_carta5_defesa:
                        print("\n\tValor do atributo de %s: %d" %
                              (nome_jogador1, j1_carta1_defesa))
                        print("\n\tValor do atributo de %s : %d" %
                              (nome_jogador2, j2_carta4_defesa))
                        print("\n\t%s possui maior valor de atributo, com %d pontos" % (
                            nome_jogador2, j2_carta5_defesa))
                        pontuacao_jogador2 += DEFESA
                        sleep(7)
                        cls()
                    else:
                        print("\n\n\t\tE M P A T E ")
                        print("\t\t\033[mAguarde...\033[m")
                        sleep(7)
                        cls()

                elif int(atributo) == 2 and int(j1_carta_escolhida) == 1 and int(j2_carta_escolhida) == 6:
                    if j1_carta1_defesa > j2_carta6_defesa:
                        print("\n\tValor do atributo de %s: %d" %
                              (nome_jogador1, j1_carta1_defesa))
                        print("\n\tValor do atributo de %s : %d" %
                              (nome_jogador2, j2_carta6_defesa))
                        print("\n\t%s possui maior valor de atributo, com %d pontos" % (
                            nome_jogador1, j1_carta1_defesa))
                        pontuacao_jogador1 += DEFESA
                        sleep(7)
                        cls()
                    elif j1_carta1_defesa < j2_carta6_defesa:
                        print("\n\tValor do atributo de %s: %d" %
                              (nome_jogador1, j1_carta1_defesa))
                        print("\n\tValor do atributo de %s : %d" %
                              (nome_jogador2, j2_carta6_defesa))
                        print("\n\t%s possui maior valor de atributo, com %d pontos" % (
                            nome_jogador2, j2_carta6_defesa))
                        pontuacao_jogador2 += DEFESA
                        sleep(7)
                        cls()
                    else:
                        print("\n\n\t\tE M P A T E ")
                        print("\t\t\033[mAguarde...\033[m")
                        sleep(7)
                        cls()

                elif int(atributo) == 2 and int(j1_carta_escolhida) == 2 and int(j2_carta_escolhida) == 4:
                    if j1_carta2_defesa > j2_carta4_defesa:
                        print("\n\tValor do atributo de %s: %d" %
                              (nome_jogador1, j1_carta2_defesa))
                        print("\n\tValor do atributo de %s : %d" %
                              (nome_jogador2, j2_carta4_defesa))
                        print("\n\t%s possui maior valor de atributo, com %d pontos" % (
                            nome_jogador1, j1_carta2_defesa))
                        pontuacao_jogador1 += DEFESA
                        sleep(7)
                        cls()
                    elif j1_carta2_defesa < j2_carta4_defesa:
                        print("\n\tValor do atributo de %s: %d" %
                              (nome_jogador1, j1_carta2_defesa))
                        print("\n\tValor do atributo de %s : %d" %
                              (nome_jogador2, j2_carta4_defesa))
                        print("\n\t%s possui maior valor de atributo, com %d pontos" % (
                            nome_jogador2, j2_carta4_defesa))
                        pontuacao_jogador2 += DEFESA
                        sleep(7)
                        cls()
                    else:
                        print("\n\n\t\tE M P A T E ")
                        print("\t\t\033[mAguarde...\033[m")
                        sleep(7)
                        cls()

                elif int(atributo) == 2 and int(j1_carta_escolhida) == 2 and int(j2_carta_escolhida) == 5:
                    if j1_carta2_defesa > j2_carta5_defesa:
                        print("\n\tValor do atributo de %s: %d" %
                              (nome_jogador1, j1_carta2_defesa))
                        print("\n\tValor do atributo de %s : %d" %
                              (nome_jogador2, j2_carta5_defesa))
                        print("\n\t%s possui maior valor de atributo, com %d pontos" % (
                            nome_jogador1, j1_carta2_defesa))
                        pontuacao_jogador1 += DEFESA
                        sleep(7)
                        cls()
                    elif j1_carta2_defesa < j2_carta5_defesa:
                        print("\n\tValor do atributo de %s: %d" %
                              (nome_jogador1, j1_carta2_defesa))
                        print("\n\tValor do atributo de %s : %d" %
                              (nome_jogador2, j2_carta5_defesa))
                        print("\n\t%s possui maior valor de atributo, com %d pontos" % (
                            nome_jogador2, j2_carta5_defesa))
                        pontuacao_jogador2 += DEFESA
                        sleep(7)
                        cls()
                    else:
                        print("\n\n\t\tE M P A T E ")
                        print("\t\t\033[mAguarde...\033[m")
                        sleep(7)
                        cls()

                elif int(atributo) == 2 and int(j1_carta_escolhida) == 2 and int(j2_carta_escolhida) == 6:
                    if j1_carta2_defesa > j2_carta6_defesa:
                        print("\n\tValor do atributo de %s: %d" %
                              (nome_jogador1, j1_carta2_defesa))
                        print("\n\tValor do atributo de %s : %d" %
                              (nome_jogador2, j2_carta6_defesa))
                        print("\n\t%s possui maior valor de atributo, com %d pontos" % (
                            nome_jogador1, j1_carta2_defesa))
                        pontuacao_jogador1 += DEFESA
                        sleep(7)
                        cls()
                    elif j1_carta2_defesa < j2_carta6_defesa:
                        print("\n\tValor do atributo de %s: %d" %
                              (nome_jogador1, j1_carta2_defesa))
                        print("\n\tValor do atributo de %s : %d" %
                              (nome_jogador2, j2_carta6_defesa))
                        print("\n\t%s possui maior valor de atributo, com %d pontos" % (
                            nome_jogador2, j2_carta6_defesa))
                        pontuacao_jogador2 += DEFESA
                        sleep(7)
                        cls()
                    else:
                        print("\n\n\t\tE M P A T E ")
                        print("\t\t\033[mAguarde...\033[m")
                        sleep(7)
                        cls()

                elif int(atributo) == 2 and int(j1_carta_escolhida) == 3 and int(j2_carta_escolhida) == 4:
                    if j1_carta3_defesa > j2_carta4_defesa:
                        print("\n\tValor do atributo de %s: %d" %
                              (nome_jogador1, j1_carta3_defesa))
                        print("\n\tValor do atributo de %s : %d" %
                              (nome_jogador2, j2_carta4_defesa))
                        print("\n\t%s possui maior valor de atributo, com %d pontos" % (
                            nome_jogador1, j1_carta3_defesa))
                        pontuacao_jogador1 += DEFESA
                        sleep(7)
                        cls()
                    elif j1_carta3_defesa < j2_carta4_defesa:
                        print("\n\tValor do atributo de %s: %d" %
                              (nome_jogador1, j1_carta3_defesa))
                        print("\n\tValor do atributo de %s : %d" %
                              (nome_jogador2, j2_carta4_defesa))
                        print("\n\t%s possui maior valor de atributo, com %d pontos" % (
                            nome_jogador2, j2_carta4_defesa))
                        pontuacao_jogador2 += DEFESA
                        sleep(7)
                        cls()
                    else:
                        print("\n\n\t\tE M P A T E ")
                        print("\t\t\033[mAguarde...\033[m")
                        sleep(7)
                        cls()

                elif int(atributo) == 2 and int(j1_carta_escolhida) == 3 and int(j2_carta_escolhida) == 5:
                    if j1_carta3_defesa > j2_carta5_defesa:
                        print("\n\tValor do atributo de %s: %d" %
                              (nome_jogador1, j1_carta3_defesa))
                        print("\n\tValor do atributo de %s : %d" %
                              (nome_jogador2, j2_carta5_defesa))
                        print("\n\t%s possui maior valor de atributo, com %d pontos" % (
                            nome_jogador1, j1_carta3_defesa))
                        pontuacao_jogador1 += DEFESA
                        sleep(7)
                        cls()
                    elif j1_carta3_defesa < j2_carta5_defesa:
                        print("\n\tValor do atributo de %s: %d" %
                              (nome_jogador1, j1_carta3_defesa))
                        print("\n\tValor do atributo de %s : %d" %
                              (nome_jogador2, j2_carta5_defesa))
                        print("\n\t%s possui maior valor de atributo, com %d pontos" % (
                            nome_jogador2, j2_carta5_defesa))
                        pontuacao_jogador2 += DEFESA
                        sleep(7)
                        cls()
                    else:
                        print("\n\n\t\tE M P A T E ")
                        print("\t\t\033[mAguarde...\033[m")
                        sleep(7)
                        cls()

                elif int(atributo) == 2 and int(j1_carta_escolhida) == 3 and int(j2_carta_escolhida) == 6:
                    if j1_carta3_defesa > j2_carta6_defesa:
                        print("\n\tValor do atributo de %s: %d" %
                              (nome_jogador1, j1_carta3_defesa))
                        print("\n\tValor do atributo de %s : %d" %
                              (nome_jogador2, j2_carta6_defesa))
                        print("\n\t%s possui maior valor de atributo, com %d pontos" % (
                            nome_jogador1, j1_carta3_defesa))
                        pontuacao_jogador1 += DEFESA
                        sleep(7)
                        cls()
                    elif j1_carta3_defesa < j2_carta6_defesa:
                        print("\n\tValor do atributo de %s: %d" %
                              (nome_jogador1, j1_carta3_defesa))
                        print("\n\tValor do atributo de %s : %d" %
                              (nome_jogador2, j2_carta6_defesa))
                        print("\n\t%s possui maior valor de atributo, com %d pontos" % (
                            nome_jogador2, j2_carta6_defesa))
                        pontuacao_jogador2 += DEFESA
                        sleep(7)
                        cls()
                    else:
                        print("\n\n\t\tE M P A T E ")
                        print("\t\t\033[mAguarde...\033[m")
                        sleep(7)
                        cls()


                elif int(atributo) == 3 and int(j1_carta_escolhida) == 1 and int(j2_carta_escolhida) == 4:
                    if j1_carta1_velocidade > j2_carta4_velocidade:
                        print("\n\tValor do atributo de %s: %d" %
                              (nome_jogador1, j1_carta1_velocidade))
                        print("\n\tValor do atributo de %s : %d" %
                              (nome_jogador2, j2_carta4_velocidade))
                        print("\n\t%s possui maior valor de atributo, com %d pontos" % (
                            nome_jogador1, j1_carta1_velocidade))
                        pontuacao_jogador1 += VELOCIDADE
                        sleep(7)
                        cls()
                    elif j1_carta1_velocidade < j2_carta4_velocidade:
                        print("\n\tValor do atributo de %s: %d" %
                              (nome_jogador1, j1_carta1_velocidade))
                        print("\n\tValor do atributo de %s : %d" %
                              (nome_jogador2, j2_carta4_velocidade))
                        print("\n\t%s possui maior valor de atributo, com %d pontos" % (
                            nome_jogador2, j2_carta4_velocidade))
                        pontuacao_jogador2 += VELOCIDADE
                        sleep(7)
                        cls()
                    else:
                        print("\n\n\t\tE M P A T E ")
                        print("\t\t\033[mAguarde...\033[m")
                        sleep(7)
                        cls()

                elif int(atributo) == 3 and int(j1_carta_escolhida) == 1 and int(j2_carta_escolhida) == 5:
                    if j1_carta1_velocidade > j2_carta5_velocidade:
                        print("\n\tValor do atributo de %s: %d" %
                              (nome_jogador1, j1_carta1_velocidade))
                        print("\n\tValor do atributo de %s : %d" %
                              (nome_jogador2, j2_carta5_velocidade))
                        print("\n\t%s possui maior valor de atributo, com %d pontos" % (
                            nome_jogador1, j1_carta1_velocidade))
                        pontuacao_jogador1 += VELOCIDADE
                        sleep(7)
                        cls()
                    elif j1_carta1_velocidade < j2_carta5_velocidade:
                        print("\n\tValor do atributo de %s: %d" %
                              (nome_jogador1, j1_carta1_velocidade))
                        print("\n\tValor do atributo de %s : %d" %
                              (nome_jogador2, j2_carta5_velocidade))
                        print("\n\t%s possui maior valor de atributo, com %d pontos" % (
                            nome_jogador2, j2_carta5_velocidade))
                        pontuacao_jogador2 += VELOCIDADE
                        sleep(7)
                        cls()
                    else:
                        print("\n\n\t\tE M P A T E ")
                        print("\t\t\033[mAguarde...\033[m")
                        sleep(7)
                        cls()

                elif int(atributo) == 3 and int(j1_carta_escolhida) == 1 and int(j2_carta_escolhida) == 6:
                    if j1_carta1_velocidade > j2_carta6_velocidade:
                        print("\n\tValor do atributo de %s: %d" %
                              (nome_jogador1, j1_carta1_velocidade))
                        print("\n\tValor do atributo de %s : %d" %
                              (nome_jogador2, j2_carta6_velocidade))
                        print("\n\t%s possui maior valor de atributo, com %d pontos" % (
                            nome_jogador1, j2_carta6_velocidade))
                        pontuacao_jogador1 += VELOCIDADE
                        sleep(7)
                        cls()
                    elif j1_carta1_velocidade < j2_carta6_velocidade:
                        print("\n\tValor do atributo de %s: %d" %
                              (nome_jogador1, j1_carta1_velocidade))
                        print("\n\tValor do atributo de %s : %d" %
                              (nome_jogador2, j2_carta6_velocidade))
                        print("\n\t%s possui maior valor de atributo, com %d pontos" % (
                            nome_jogador2, j2_carta6_velocidade))
                        pontuacao_jogador2 += VELOCIDADE
                        sleep(7)
                        cls()
                    else:
                        print("\n\n\t\tE M P A T E ")
                        print("\t\t\033[mAguarde...\033[m")
                        sleep(7)
                        cls()

                elif int(atributo) == 3 and int(j1_carta_escolhida) == 2 and int(j2_carta_escolhida) == 4:
                    if j1_carta2_velocidade > j2_carta4_velocidade:
                        print("\n\tValor do atributo de %s: %d" %
                              (nome_jogador1, j1_carta2_velocidade))
                        print("\n\tValor do atributo de %s : %d" %
                              (nome_jogador2, j2_carta4_velocidade))
                        print("\n\t%s possui maior valor de atributo, com %d pontos" % (
                            nome_jogador1, j1_carta2_velocidade))
                        pontuacao_jogador1 += VELOCIDADE
                        sleep(7)
                        cls()
                    elif j1_carta2_velocidade < j2_carta4_velocidade:
                        print("\n\tValor do atributo de %s: %d" %
                              (nome_jogador1, j1_carta2_velocidade))
                        print("\n\tValor do atributo de %s : %d" %
                              (nome_jogador2, j2_carta4_velocidade))
                        print("\n\t%s possui maior valor de atributo, com %d pontos" % (
                            nome_jogador2, j2_carta4_velocidade))
                        pontuacao_jogador2 += VELOCIDADE
                        sleep(7)
                        cls()
                    else:
                        print("\n\n\t\tE M P A T E ")
                        print("\t\t\033[mAguarde...\033[m")
                        sleep(7)
                        cls()

                elif int(atributo) == 3 and int(j1_carta_escolhida) == 2 and int(j2_carta_escolhida) == 5:
                    if j1_carta2_velocidade > j2_carta5_velocidade:
                        print("\n\tValor do atributo de %s: %d" %
                              (nome_jogador1, j1_carta2_velocidade))
                        print("\n\tValor do atributo de %s : %d" %
                              (nome_jogador2, j2_carta5_velocidade))
                        print("\n\t%s possui maior valor de atributo, com %d pontos" % (
                            nome_jogador1, j1_carta2_velocidade))
                        pontuacao_jogador1 += VELOCIDADE
                        sleep(7)
                        cls()
                    elif j1_carta2_velocidade < j2_carta5_velocidade:
                        print("\n\tValor do atributo de %s: %d" %
                              (nome_jogador1, j1_carta2_velocidade))
                        print("\n\tValor do atributo de %s : %d" %
                              (nome_jogador2, j2_carta5_velocidade))
                        print("\n\t%s possui maior valor de atributo, com %d pontos" % (
                            nome_jogador2, j2_carta5_velocidade))
                        pontuacao_jogador2 += VELOCIDADE
                        sleep(7)
                        cls()
                    else:
                        print("\n\n\t\tE M P A T E ")
                        print("\t\t\033[mAguarde...\033[m")
                        sleep(7)
                        cls()

                elif int(atributo) == 3 and int(j1_carta_escolhida) == 2 and int(j2_carta_escolhida) == 6:
                    if j1_carta2_velocidade > j2_carta6_velocidade:
                        print("\n\tValor do atributo de %s: %d" %
                              (nome_jogador1, j1_carta2_velocidade))
                        print("\n\tValor do atributo de %s : %d" %
                              (nome_jogador2, j2_carta6_velocidade))
                        print("\n\t%s possui maior valor de atributo, com %d pontos" % (
                            nome_jogador1, j1_carta2_velocidade))
                        pontuacao_jogador1 += VELOCIDADE
                        sleep(7)
                        cls()
                    elif j1_carta2_velocidade < j2_carta6_velocidade:
                        print("\n\tValor do atributo de %s: %d" %
                              (nome_jogador1, j1_carta2_velocidade))
                        print("\n\tValor do atributo de %s : %d" %
                              (nome_jogador2, j2_carta6_velocidade))
                        print("\n\t%s possui maior valor de atributo, com %d pontos" % (
                            nome_jogador2, j2_carta6_velocidade))
                        pontuacao_jogador2 += VELOCIDADE
                        sleep(7)
                        cls()
                    else:
                        print("\n\n\t\tE M P A T E ")
                        print("\t\t\033[mAguarde...\033[m")
                        sleep(7)
                        cls()

                elif int(atributo) == 3 and int(j1_carta_escolhida) == 3 and int(j2_carta_escolhida) == 4:
                    if j1_carta3_velocidade > j2_carta4_velocidade:
                        print("\n\tValor do atributo de %s: %d" %
                              (nome_jogador1, j1_carta3_velocidade))
                        print("\n\tValor do atributo de %s : %d" %
                              (nome_jogador2, j2_carta4_velocidade))
                        print("\n\t%s possui maior valor de atributo, com %d pontos" % (
                            nome_jogador1, j1_carta3_velocidade))
                        pontuacao_jogador1 += VELOCIDADE
                        sleep(7)
                        cls()
                    elif j1_carta3_velocidade < j2_carta4_velocidade:
                        print("\n\tValor do atributo de %s: %d" %
                              (nome_jogador1, j1_carta3_velocidade))
                        print("\n\tValor do atributo de %s : %d" %
                              (nome_jogador2, j2_carta4_velocidade))
                        print("\n\t%s possui maior valor de atributo, com %d pontos" % (
                            nome_jogador2, j2_carta4_velocidade))
                        pontuacao_jogador2 += VELOCIDADE
                        sleep(7)
                        cls()
                    else:
                        print("\n\n\t\tE M P A T E ")
                        print("\t\t\033[mAguarde...\033[m")
                        sleep(7)
                        cls()

                elif int(atributo) == 3 and int(j1_carta_escolhida) == 3 and int(j2_carta_escolhida) == 5:
                    if j1_carta3_velocidade > j2_carta5_velocidade:
                        print("\n\tValor do atributo de %s: %d" %
                              (nome_jogador1, j1_carta3_velocidade))
                        print("\n\tValor do atributo de %s : %d" %
                              (nome_jogador2, j2_carta5_velocidade))
                        print("\n\t%s possui maior valor de atributo, com %d pontos" % (
                            nome_jogador1, j1_carta3_velocidade))
                        pontuacao_jogador1 += VELOCIDADE
                        sleep(7)
                        cls()
                    elif j1_carta3_velocidade < j2_carta5_velocidade:
                        print("\n\tValor do atributo de %s: %d" %
                              (nome_jogador1, j1_carta3_velocidade))
                        print("\n\tValor do atributo de %s : %d" %
                              (nome_jogador2, j2_carta5_velocidade))
                        print("\n\t%s possui maior valor de atributo, com %d pontos" % (
                            nome_jogador2, j2_carta5_velocidade))
                        pontuacao_jogador2 += VELOCIDADE
                        sleep(7)
                        cls()
                    else:
                        print("\n\n\t\tE M P A T E ")
                        print("\t\t\033[mAguarde...\033[m")
                        sleep(7)
                        cls()

                elif int(atributo) == 3 and int(j1_carta_escolhida) == 3 and int(j2_carta_escolhida) == 6:
                    if j1_carta3_velocidade > j2_carta6_velocidade:
                        print("\n\tValor do atributo de %s: %d" %
                              (nome_jogador1, j1_carta3_velocidade))
                        print("\n\tValor do atributo de %s : %d" %
                              (nome_jogador2, j2_carta6_velocidade))
                        print("\n\t%s possui maior valor de atributo, com %d pontos" % (
                            nome_jogador1, j1_carta3_velocidade))
                        pontuacao_jogador1 += VELOCIDADE
                        sleep(7)
                        cls()
                    elif j1_carta3_velocidade < j2_carta6_velocidade:
                        print("\n\tValor do atributo de %s: %d" %
                              (nome_jogador1, j1_carta3_velocidade))
                        print("\n\tValor do atributo de %s : %d" %
                              (nome_jogador2, j2_carta6_velocidade))
                        print("\n\t%s possui maior valor de atributo, com %d pontos" % (
                            nome_jogador2, j2_carta6_velocidade))
                        pontuacao_jogador2 += VELOCIDADE
                        sleep(7)
                        cls()
                    else:
                        print("\n\n\t\tE M P A T E ")
                        print("\t\t\033[mAguarde...\033[m")
                        sleep(7)
                        cls()

            elif vez_jogar % 2 == 0:
                if vez_jogar == 2:
                    input(
                        "\n\n\n\n\t\t\t%s C O M E C A   J O G A N D O\n\t\t< ENTER > P A R A   C O N T I N U A R" % nome_jogador2)
                    cls()
                else:
                    input(
                        "\t\tA G O R A  E  A  V E Z  D E %s\n\t\t< ENTER > P A R A   C O N T I N U A R" % nome_jogador2)
                    cls()
                vez_jogar += 1

                print("#" * 30)
                print("#" + "\t\033[31mID - [  4  ]\033[m" + " " * 9 + "#")
                print("#" * 30)
                print("#" + "\t%s" % j2_carta4_nome + " " * 9 + "#")
                print("#" * 30)
                print("#" + "\tAtaque: %d" % j2_carta4_ataque + " " * 11 + "#")
                print("#" * 30)
                print("#" + "\tDefesa: %d" % j2_carta4_defesa + " " * 11 + "#")
                print("#" * 30)
                print("#" + "\tVelocidade: %d" %
                      j2_carta4_velocidade + " " * 7 + "#")
                print("#" * 30 + "\n\n")

                print("#" * 30)
                print("#" + "\t\033[31mID - [  5  ]\033[m" + " " * 9 + "#")
                print("#" * 30)
                print("#" + "\t%s" % j2_carta5_nome + " " * 9 + "#")
                print("#" * 30)
                print("#" + "\tAtaque: %d" % j2_carta5_ataque + " " * 11 + "#")
                print("#" * 30)
                print("#" + "\tDefesa: %d" % j2_carta5_defesa + " " * 11 + "#")
                print("#" * 30)
                print("#" + "\tVelocidade: %d" %
                      j2_carta5_velocidade + " " * 7 + "#")
                print("#" * 30 + "\n\n")

                print("#" * 30)
                print("#" + "\t\033[31mID - [  6  ]\033[m" + " " * 9 + "#")
                print("#" * 30)
                print("#" + "\t%s" % j2_carta6_nome + " " * 9 + "#")
                print("#" * 30)
                print("#" + "\tAtaque: %d" % j2_carta6_ataque + " " * 11 + "#")
                print("#" * 30)
                print("#" + "\tDefesa: %d" % j2_carta6_defesa + " " * 11 + "#")
                print("#" * 30)
                print("#" + "\tVelocidade: %d" %
                      j2_carta6_velocidade + " " * 7 + "#")
                print("#" * 30 + "\n\n")

                print("\tA T R I B U T O S   D I S P O N I V E I S\n")
                print("\t[ 1 ] - Ataque")
                print("\t[ 2 ] - Defesa")
                print("\t[ 3 ] - Velocidade")
                atributo = ""
                while atributo != "1" and atributo != "2" and atributo != "3":
                    atributo = input("%s, escolha um atributo:" %
                                     nome_jogador2)

                j2_carta_escolhida = ""
                while j2_carta_escolhida != "4" and j2_carta_escolhida != "5" and j2_carta_escolhida != "6":
                    j2_carta_escolhida = input(
                        "%s, carta ID 4, 5 ou 6?:" % nome_jogador2)
                cls()
                input("\t\t\n\n\n%s, voce esta ai? <ENTER> para confirmar " %
                      nome_jogador1)
                cls()

                if int(atributo) == 1:
                    print("\n\t\t%s o jogador %s escolheu o atributo ATAQUE" %
                          (nome_jogador1, nome_jogador2))
                    sleep(5)
                elif int(atributo) == 2:
                    print("\n\t\t%s o jogador %s escolheu o atributo DEFESA" %
                          (nome_jogador1, nome_jogador2))
                    sleep(5)
                elif int(atributo) == 3:
                    print("\n\t\t%s o jogador %s escolheu o atributo VELOCIDADE" % (
                        nome_jogador1, nome_jogador2))
                    sleep(5)

                print("#" * 30)
                print("#" + "\t\033[31mID - [  1  ]\033[m" + " " * 9 + "#")
                print("#" * 30)
                print("#" + "\t%s" % j1_carta1_nome + " " * 9 + "#")
                print("#" * 30)
                print("#" + "\tAtaque: %d" % j1_carta1_ataque + " " * 11 + "#")
                print("#" * 30)
                print("#" + "\tDefesa: %d" % j1_carta1_defesa + " " * 11 + "#")
                print("#" * 30)
                print("#" + "\tVelocidade: %d" %
                      j1_carta1_velocidade + " " * 7 + "#")
                print("#" * 30 + "\n\n")

                print("#" * 30)
                print("#" + "\t\033[31mID - [  2  ]\033[m" + " " * 9 + "#")
                print("#" * 30)
                print("#" + "\t%s" % j1_carta2_nome + " " * 9 + "#")
                print("#" * 30)
                print("#" + "\tAtaque: %d" % j1_carta2_ataque + " " * 11 + "#")
                print("#" * 30)
                print("#" + "\tDefesa: %d" % j1_carta2_defesa + " " * 11 + "#")
                print("#" * 30)
                print("#" + "\tVelocidade: %d" %
                      j1_carta2_velocidade + " " * 7 + "#")
                print("#" * 30 + "\n\n")

                print("#" * 30)
                print("#" + "\t\033[31mID - [  3  ]\033[m" + " " * 9 + "#")
                print("#" * 30)
                print("#" + "\t%s" % j1_carta3_nome + " " * 9 + "#")
                print("#" * 30)
                print("#" + "\tAtaque: %d" % j1_carta3_ataque + " " * 11 + "#")
                print("#" * 30)
                print("#" + "\tDefesa: %d" % j1_carta3_defesa + " " * 11 + "#")
                print("#" * 30)
                print("#" + "\tVelocidade: %d" %
                      j1_carta3_velocidade + " " * 7 + "#")
                print("#" * 30 + "\n\n")

                j1_carta_escolhida = ""
                while j1_carta_escolhida != "1" and j1_carta_escolhida != "2" and j1_carta_escolhida != "3":
                    j1_carta_escolhida = input(
                        "%s, carta ID 1, 2 ou 3?:" % nome_jogador1)
                cls()

                if int(atributo) == 1 and int(j2_carta_escolhida) == 4 and int(j1_carta_escolhida) == 1:
                    if j2_carta4_ataque > j1_carta1_ataque:
                        print("\n\tValor do atributo de %s: %d" %
                              (nome_jogador1, j1_carta1_ataque))
                        print("\n\tValor do atributo de %s : %d" %
                              (nome_jogador2, j2_carta4_ataque))
                        print("\n\t%s possui maior valor de atributo, com %d pontos" % (
                            nome_jogador2, j2_carta4_ataque))
                        pontuacao_jogador2 += ATAQUE
                        sleep(7)
                        cls()
                    elif j2_carta4_ataque < j1_carta1_ataque:
                        print("\n\tValor do atributo de %s: %d" %
                              (nome_jogador1, j1_carta1_ataque))
                        print("\n\tValor do atributo de %s : %d" %
                              (nome_jogador2, j2_carta4_ataque))
                        print("\n\t%s possui maior valor de atributo, com %d pontos" % (
                            nome_jogador1, j1_carta1_ataque))
                        pontuacao_jogador1 += ATAQUE
                        sleep(7)
                        cls()
                    else:
                        print("\n\n\t\tE M P A T E ")
                        print("\t\t\033[mAguarde...\033[m")
                        sleep(7)
                        cls()

                elif int(atributo) == 1 and int(j2_carta_escolhida) == 4 and int(j1_carta_escolhida) == 2:
                    if j2_carta4_ataque > j1_carta2_ataque:
                        print("\n\tValor do atributo de %s: %d" %
                              (nome_jogador1, j1_carta2_ataque))
                        print("\n\tValor do atributo de %s : %d" %
                              (nome_jogador2, j2_carta4_ataque))
                        print("\n\t%s possui maior valor de atributo, com %d pontos" % (
                            nome_jogador2, j2_carta4_ataque))
                        pontuacao_jogador2 += ATAQUE
                        sleep(7)
                        cls()
                    elif j2_carta4_ataque < j1_carta2_ataque:
                        print("\n\tValor do atributo de %s: %d" %
                              (nome_jogador1, j1_carta2_ataque))
                        print("\n\tValor do atributo de %s : %d" %
                              (nome_jogador2, j2_carta4_ataque))
                        print("\n\t%s possui maior valor de atributo, com %d pontos" % (
                            nome_jogador1, j1_carta2_ataque))
                        pontuacao_jogador1 += ATAQUE
                        sleep(7)
                        cls()
                    else:
                        print("\n\n\t\tE M P A T E ")
                        print("\t\t\033[mAguarde...\033[m")
                        sleep(7)
                        cls()

                elif int(atributo) == 1 and int(j2_carta_escolhida) == 4 and int(j1_carta_escolhida) == 3:
                    if j2_carta4_ataque > j1_carta3_ataque:
                        print("\n\tValor do atributo de %s: %d" %
                              (nome_jogador1, j1_carta3_ataque))
                        print("\n\tValor do atributo de %s : %d" %
                              (nome_jogador2, j2_carta4_ataque))
                        print("\n\t%s possui maior valor de atributo, com %d pontos" % (
                            nome_jogador2, j2_carta4_ataque))
                        pontuacao_jogador2 += ATAQUE
                        sleep(7)
                        cls()
                    elif j2_carta4_ataque < j1_carta3_ataque:
                        print("\n\tValor do atributo de %s: %d" %
                              (nome_jogador1, j1_carta3_ataque))
                        print("\n\tValor do atributo de %s : %d" %
                              (nome_jogador2, j2_carta4_ataque))
                        print("\n\t%s possui maior valor de atributo, com %d pontos" % (
                            nome_jogador1, j1_carta3_ataque))
                        pontuacao_jogador1 += ATAQUE
                        sleep(7)
                        cls()
                    else:
                        print("\n\n\t\tE M P A T E ")
                        print("\t\t\033[mAguarde...\033[m")
                        sleep(7)
                        cls()

                elif int(atributo) == 1 and int(j2_carta_escolhida) == 5 and int(j1_carta_escolhida) == 1:
                    if j2_carta5_ataque > j1_carta1_ataque:
                        print("\n\tValor do atributo de %s: %d" %
                              (nome_jogador1, j1_carta1_ataque))
                        print("\n\tValor do atributo de %s : %d" %
                              (nome_jogador2, j2_carta5_ataque))
                        print("\n\t%s possui maior valor de atributo, com %d pontos" % (
                            nome_jogador2, j2_carta5_ataque))
                        pontuacao_jogador2 += ATAQUE
                        sleep(7)
                        cls()
                    elif j2_carta5_ataque < j1_carta1_ataque:
                        print("\n\tValor do atributo de %s: %d" %
                              (nome_jogador1, j1_carta1_ataque))
                        print("\n\tValor do atributo de %s : %d" %
                              (nome_jogador2, j2_carta5_ataque))
                        print("\n\t%s possui maior valor de atributo, com %d pontos" % (
                            nome_jogador1, j1_carta1_ataque))
                        pontuacao_jogador1 += ATAQUE
                        sleep(7)
                        cls()
                    else:
                        print("\n\n\t\tE M P A T E ")
                        print("\t\t\033[mAguarde...\033[m")
                        sleep(7)
                        cls()

                elif int(atributo) == 1 and int(j2_carta_escolhida) == 5 and int(j1_carta_escolhida) == 2:
                    if j2_carta5_ataque > j1_carta2_ataque:
                        print("\n\tValor do atributo de %s: %d" %
                              (nome_jogador1, j1_carta2_ataque))
                        print("\n\tValor do atributo de %s : %d" %
                              (nome_jogador2, j2_carta5_ataque))
                        print("\n\t%s possui maior valor de atributo, com %d pontos" % (
                            nome_jogador2, j2_carta5_ataque))
                        pontuacao_jogador2 += ATAQUE
                        sleep(7)
                        cls()
                    elif j2_carta5_ataque < j1_carta2_ataque:
                        print("\n\tValor do atributo de %s: %d" %
                              (nome_jogador1, j1_carta2_ataque))
                        print("\n\tValor do atributo de %s : %d" %
                              (nome_jogador2, j2_carta5_ataque))
                        print("\n\t%s possui maior valor de atributo, com %d pontos" % (
                            nome_jogador1, j1_carta2_ataque))
                        pontuacao_jogador1 += ATAQUE
                        sleep(7)
                        cls()
                    else:
                        print("\n\n\t\tE M P A T E ")
                        print("\t\t\033[mAguarde...\033[m")
                        sleep(7)
                        cls()

                elif int(atributo) == 1 and int(j2_carta_escolhida) == 5 and int(j1_carta_escolhida) == 3:
                    if j2_carta5_ataque > j1_carta3_ataque:
                        print("\n\tValor do atributo de %s: %d" %
                              (nome_jogador1, j1_carta3_ataque))
                        print("\n\tValor do atributo de %s : %d" %
                              (nome_jogador2, j2_carta5_ataque))
                        print("\n\t%s possui maior valor de atributo, com %d pontos" % (
                            nome_jogador2, j2_carta5_ataque))
                        pontuacao_jogador2 += ATAQUE
                        sleep(7)
                        cls()
                    elif j2_carta5_ataque < j1_carta3_ataque:
                        print("\n\tValor do atributo de %s: %d" %
                              (nome_jogador1, j1_carta3_ataque))
                        print("\n\tValor do atributo de %s : %d" %
                              (nome_jogador2, j2_carta5_ataque))
                        print("\n\t%s possui maior valor de atributo, com %d pontos" % (
                            nome_jogador1, j1_carta3_ataque))
                        pontuacao_jogador1 += ATAQUE
                        sleep(7)
                        cls()
                    else:
                        print("\n\n\t\tE M P A T E ")
                        print("\t\t\033[mAguarde...\033[m")
                        sleep(7)
                        cls()

                elif int(atributo) == 1 and int(j2_carta_escolhida) == 6 and int(j1_carta_escolhida) == 1:
                    if j2_carta6_ataque > j1_carta1_ataque:
                        print("\n\tValor do atributo de %s: %d" %
                              (nome_jogador1, j1_carta1_ataque))
                        print("\n\tValor do atributo de %s : %d" %
                              (nome_jogador2, j2_carta6_ataque))
                        print("\n\t%s possui maior valor de atributo, com %d pontos" % (
                            nome_jogador2, j2_carta6_ataque))
                        pontuacao_jogador2 += ATAQUE
                        sleep(7)
                        cls()
                    elif j2_carta6_ataque < j1_carta1_ataque:
                        print("\n\tValor do atributo de %s: %d" %
                              (nome_jogador1, j1_carta1_ataque))
                        print("\n\tValor do atributo de %s : %d" %
                              (nome_jogador2, j2_carta6_ataque))
                        print("\n\t%s possui maior valor de atributo, com %d pontos" % (
                            nome_jogador1, j1_carta1_ataque))
                        pontuacao_jogador1 += ATAQUE
                        sleep(7)
                        cls()
                    else:
                        print("\n\n\t\tE M P A T E ")
                        print("\t\t\033[mAguarde...\033[m")
                        sleep(7)
                        cls()

                elif int(atributo) == 1 and int(j2_carta_escolhida) == 6 and int(j1_carta_escolhida) == 2:
                    if j2_carta6_ataque > j1_carta2_ataque:
                        print("\n\tValor do atributo de %s: %d" %
                              (nome_jogador1, j1_carta2_ataque))
                        print("\n\tValor do atributo de %s : %d" %
                              (nome_jogador2, j2_carta6_ataque))
                        print("\n\t%s possui maior valor de atributo, com %d pontos" % (
                            nome_jogador2, j2_carta6_ataque))
                        pontuacao_jogador2 += ATAQUE
                        sleep(7)
                        cls()
                    elif j2_carta6_ataque < j1_carta2_ataque:
                        print("\n\tValor do atributo de %s: %d" %
                              (nome_jogador1, j1_carta2_ataque))
                        print("\n\tValor do atributo de %s : %d" %
                              (nome_jogador2, j2_carta6_ataque))
                        print("\n\t%s possui maior valor de atributo, com %d pontos" % (
                            nome_jogador1, j1_carta2_ataque))
                        pontuacao_jogador1 += ATAQUE
                        sleep(7)
                        cls()
                    else:
                        print("\n\n\t\tE M P A T E ")
                        print("\t\t\033[mAguarde...\033[m")
                        sleep(7)
                        cls()

                elif int(atributo) == 1 and int(j2_carta_escolhida) == 6 and int(j1_carta_escolhida) == 3:
                    if j2_carta6_ataque > j1_carta3_ataque:
                        print("\n\tValor do atributo de %s: %d" %
                              (nome_jogador1, j1_carta3_ataque))
                        print("\n\tValor do atributo de %s : %d" %
                              (nome_jogador2, j2_carta6_ataque))
                        print("\n\t%s possui maior valor de atributo, com %d pontos" % (
                            nome_jogador2, j2_carta6_ataque))
                        pontuacao_jogador2 += ATAQUE
                        sleep(7)
                        cls()
                    elif j2_carta6_ataque < j1_carta3_ataque:
                        print("\n\tValor do atributo de %s: %d" %
                              (nome_jogador1, j1_carta3_ataque))
                        print("\n\tValor do atributo de %s : %d" %
                              (nome_jogador2, j2_carta6_ataque))
                        print("\n\t%s possui maior valor de atributo, com %d pontos" % (
                            nome_jogador1, j1_carta3_ataque))
                        pontuacao_jogador1 += ATAQUE
                        sleep(7)
                        cls()
                    else:
                        print("\n\n\t\tE M P A T E ")
                        print("\t\t\033[mAguarde...\033[m")
                        sleep(7)
                        cls()

                elif int(atributo) == 2 and int(j2_carta_escolhida) == 4 and int(j1_carta_escolhida) == 1:
                    if j2_carta4_defesa > j1_carta1_defesa:
                        print("\n\tValor do atributo de %s: %d" %
                              (nome_jogador1, j1_carta1_defesa))
                        print("\n\tValor do atributo de %s: %d" %
                              (nome_jogador2, j2_carta4_defesa))
                        print("\n\t%s possui maior valor de atributo, com %d pontos" % (
                            nome_jogador2, j2_carta4_defesa))
                        pontuacao_jogador2 += DEFESA
                        sleep(7)
                        cls()
                    elif j2_carta4_defesa < j1_carta1_defesa:
                        print("\n\tValor do atributo de %s: %d" %
                              (nome_jogador1, j1_carta1_defesa))
                        print("\n\tValor do atributo de %s: %d" %
                              (nome_jogador2, j2_carta4_defesa))
                        print("\n\t%s possui maior valor de atributo, com %d pontos" % (
                            nome_jogador1, j1_carta1_defesa))
                        pontuacao_jogador1 += DEFESA
                        sleep(7)
                        cls()
                    else:
                        print("\n\n\t\tE M P A T E ")
                        print("\t\t\033[mAguarde...\033[m")
                        sleep(7)
                        cls()

                elif int(atributo) == 2 and int(j2_carta_escolhida) == 4 and int(j1_carta_escolhida) == 2:
                    if j2_carta4_defesa > j1_carta2_defesa:
                        print("\n\tValor do atributo de %s: %d" %
                              (nome_jogador1, j1_carta2_defesa))
                        print("\n\tValor do atributo de %s: %d" %
                              (nome_jogador2, j2_carta4_defesa))
                        print("\n\t%s possui maior valor de atributo, com %d pontos" % (
                            nome_jogador2, j2_carta4_defesa))
                        pontuacao_jogador2 += DEFESA
                        sleep(7)
                        cls()
                    elif j2_carta4_defesa < j1_carta2_defesa:
                        print("\n\tValor do atributo de %s: %d" %
                              (nome_jogador1, j1_carta2_defesa))
                        print("\n\tValor do atributo de %s: %d" %
                              (nome_jogador2, j2_carta4_defesa))
                        print("\n\t%s possui maior valor de atributo, com %d pontos" % (
                            nome_jogador1, j1_carta2_defesa))
                        pontuacao_jogador1 += DEFESA
                        sleep(7)
                        cls()
                    else:
                        print("\n\n\t\tE M P A T E ")
                        print("\t\t\033[mAguarde...\033[m")
                        sleep(7)
                        cls()

                elif int(atributo) == 2 and int(j2_carta_escolhida) == 4 and int(j1_carta_escolhida) == 3:
                    if j2_carta4_defesa > j1_carta3_defesa:
                        print("\n\tValor do atributo de %s: %d" %
                              (nome_jogador1, j1_carta3_defesa))
                        print("\n\tValor do atributo de %s: %d" %
                              (nome_jogador2, j2_carta4_defesa))
                        print("\n\t%s possui maior valor de atributo, com %d pontos" % (
                            nome_jogador2, j2_carta4_defesa))
                        pontuacao_jogador2 += DEFESA
                        sleep(7)
                        cls()
                    elif j2_carta4_defesa < j1_carta3_defesa:
                        print("\n\tValor do atributo de %s: %d" %
                              (nome_jogador1, j1_carta3_defesa))
                        print("\n\tValor do atributo de %s: %d" %
                              (nome_jogador2, j2_carta4_defesa))
                        print("\n\t%s possui maior valor de atributo, com %d pontos" % (
                            nome_jogador1, j1_carta3_defesa))
                        pontuacao_jogador1 += DEFESA
                        sleep(7)
                        cls()
                    else:
                        print("\n\n\t\tE M P A T E ")
                        print("\t\t\033[mAguarde...\033[m")
                        sleep(7)
                        cls()

                elif int(atributo) == 2 and int(j2_carta_escolhida) == 5 and int(j1_carta_escolhida) == 1:
                    if j2_carta5_defesa > j1_carta1_defesa:
                        print("\n\tValor do atributo de %s: %d" %
                              (nome_jogador1, j1_carta1_defesa))
                        print("\n\tValor do atributo de %s: %d" %
                              (nome_jogador2, j2_carta5_defesa))
                        print("\n\t%s possui maior valor de atributo, com %d pontos" % (
                            nome_jogador2, j2_carta5_defesa))
                        pontuacao_jogador2 += DEFESA
                        sleep(7)
                        cls()
                    elif j2_carta5_defesa < j1_carta1_defesa:
                        print("\n\tValor do atributo de %s: %d" %
                              (nome_jogador1, j1_carta1_defesa))
                        print("\n\tValor do atributo de %s: %d" %
                              (nome_jogador2, j2_carta5_defesa))
                        print("\n\t%s possui maior valor de atributo, com %d pontos" % (
                            nome_jogador1, j1_carta1_defesa))
                        pontuacao_jogador1 += DEFESA
                        sleep(7)
                        cls()
                    else:
                        print("\n\n\t\tE M P A T E ")
                        print("\t\t\033[mAguarde...\033[m")
                        sleep(7)
                        cls()

                elif int(atributo) == 2 and int(j2_carta_escolhida) == 5 and int(j1_carta_escolhida) == 2:
                    if j2_carta5_defesa > j1_carta2_defesa:
                        print("\n\tValor do atributo de %s: %d" %
                              (nome_jogador1, j1_carta2_defesa))
                        print("\n\tValor do atributo de %s: %d" %
                              (nome_jogador2, j2_carta5_defesa))
                        print("\n\t%s possui maior valor de atributo, com %d pontos" % (
                            nome_jogador2, j2_carta5_defesa))
                        pontuacao_jogador2 += DEFESA
                        sleep(7)
                        cls()
                    elif j2_carta5_defesa < j1_carta2_defesa:
                        print("\n\tValor do atributo de %s: %d" %
                              (nome_jogador1, j1_carta2_defesa))
                        print("\n\tValor do atributo de %s: %d" %
                              (nome_jogador2, j2_carta5_defesa))
                        print("\n\t%s possui maior valor de atributo, com %d pontos" % (
                            nome_jogador1, j1_carta2_defesa))
                        pontuacao_jogador1 += DEFESA
                        sleep(7)
                        cls()
                    else:
                        print("\n\n\t\tE M P A T E ")
                        print("\t\t\033[mAguarde...\033[m")
                        sleep(7)
                        cls()

                elif int(atributo) == 2 and int(j2_carta_escolhida) == 5 and int(j1_carta_escolhida) == 3:
                    if j2_carta5_defesa > j1_carta3_defesa:
                        print("\n\tValor do atributo de %s: %d" %
                              (nome_jogador1, j1_carta3_defesa))
                        print("\n\tValor do atributo de %s: %d" %
                              (nome_jogador2, j2_carta5_defesa))
                        print("\n\t%s possui maior valor de atributo, com %d pontos" % (
                            nome_jogador2, j2_carta5_defesa))
                        pontuacao_jogador2 += DEFESA
                        sleep(7)
                        cls()
                    elif j2_carta5_defesa < j1_carta3_defesa:
                        print("\n\tValor do atributo de %s: %d" %
                              (nome_jogador1, j1_carta3_defesa))
                        print("\n\tValor do atributo de %s: %d" %
                              (nome_jogador2, j2_carta5_defesa))
                        print("\n\t%s possui maior valor de atributo, com %d pontos" % (
                            nome_jogador1, j1_carta3_defesa))
                        pontuacao_jogador1 += DEFESA
                        sleep(7)
                        cls()
                    else:
                        print("\n\n\t\tE M P A T E ")
                        print("\t\t\033[mAguarde...\033[m")
                        sleep(7)
                        cls()

                elif int(atributo) == 2 and int(j2_carta_escolhida) == 6 and int(j1_carta_escolhida) == 1:
                    if j2_carta6_defesa > j1_carta1_defesa:
                        print("\n\tValor do atributo de %s: %d" %
                              (nome_jogador1, j1_carta1_defesa))
                        print("\n\tValor do atributo de %s: %d" %
                              (nome_jogador2, j2_carta6_defesa))
                        print("\n\t%s possui maior valor de atributo, com %d pontos" % (
                            nome_jogador2, j2_carta6_defesa))
                        pontuacao_jogador2 += DEFESA
                        sleep(7)
                        cls()
                    elif j2_carta6_defesa < j1_carta1_defesa:
                        print("\n\tValor do atributo de %s: %d" %
                              (nome_jogador1, j1_carta1_defesa))
                        print("\n\tValor do atributo de %s: %d" %
                              (nome_jogador2, j2_carta6_defesa))
                        print("\n\t%s possui maior valor de atributo, com %d pontos" % (
                            nome_jogador1, j1_carta1_defesa))
                        pontuacao_jogador1 += DEFESA
                        sleep(7)
                        cls()
                    else:
                        print("\n\n\t\tE M P A T E ")
                        print("\t\t\033[mAguarde...\033[m")
                        sleep(7)
                        cls()

                elif int(atributo) == 2 and int(j2_carta_escolhida) == 6 and int(j1_carta_escolhida) == 2:
                    if j2_carta6_defesa > j1_carta2_defesa:
                        print("\n\tValor do atributo de %s: %d" %
                              (nome_jogador1, j1_carta2_defesa))
                        print("\n\tValor do atributo de %s: %d" %
                              (nome_jogador2, j2_carta6_defesa))
                        print("\n\t%s possui maior valor de atributo, com %d pontos" % (
                            nome_jogador2, j2_carta6_defesa))
                        pontuacao_jogador2 += DEFESA
                        sleep(7)
                        cls()

                    elif j2_carta6_defesa < j1_carta2_defesa:
                        print("\n\tValor do atributo de %s: %d" %
                              (nome_jogador1, j1_carta2_defesa))
                        print("\n\tValor do atributo de %s: %d" %
                              (nome_jogador2, j2_carta6_defesa))
                        print("\n\t%s possui maior valor de atributo, com %d pontos" % (
                            nome_jogador1, j1_carta2_defesa))
                        pontuacao_jogador1 += DEFESA
                        sleep(7)
                        cls()
                    else:
                        print("\n\n\t\tE M P A T E ")
                        print("\t\t\033[mAguarde...\033[m")
                        sleep(7)
                        cls()

                elif int(atributo) == 2 and int(j2_carta_escolhida) == 6 and int(j1_carta_escolhida) == 3:
                    if j2_carta6_defesa > j1_carta3_defesa:
                        print("\n\tValor do atributo de %s: %d" %
                              (nome_jogador1, j1_carta3_defesa))
                        print("\n\tValor do atributo de %s: %d" %
                              (nome_jogador2, j2_carta6_defesa))
                        print("\n\t%s possui maior valor de atributo, com %d pontos" % (
                            nome_jogador2, j2_carta6_defesa))
                        pontuacao_jogador2 += DEFESA
                        sleep(7)
                        cls()
                    elif j2_carta6_defesa < j1_carta3_defesa:
                        print("\n\tValor do atributo de %s: %d" %
                              (nome_jogador1, j1_carta3_defesa))
                        print("\n\tValor do atributo de %s: %d" %
                              (nome_jogador2, j2_carta6_defesa))
                        print("\n\t%s possui maior valor de atributo, com %d pontos" % (
                            nome_jogador1, j1_carta3_defesa))
                        pontuacao_jogador1 += DEFESA
                        sleep(7)
                        cls()
                    else:
                        print("\n\n\t\tE M P A T E ")
                        print("\t\t\033[mAguarde...\033[m")
                        sleep(7)
                        cls()

                elif int(atributo) == 3 and int(j2_carta_escolhida) == 4 and int(j1_carta_escolhida) == 1:
                    if j2_carta4_velocidade > j1_carta1_velocidade:
                        print("\n\tValor do atributo de %s: %d" %
                              (nome_jogador1, j1_carta1_velocidade))
                        print("\n\tValor do atributo de %s: %d" %
                              (nome_jogador2, j2_carta4_velocidade))
                        print("\n\t%s possui maior valor de atributo, com %d pontos" % (
                            nome_jogador2, j2_carta4_velocidade))
                        pontuacao_jogador2 += VELOCIDADE
                        sleep(7)
                        cls()
                    elif j2_carta4_velocidade < j1_carta1_velocidade:
                        print("\n\tValor do atributo de %s: %d" %
                              (nome_jogador1, j1_carta1_velocidade))
                        print("\n\tValor do atributo de %s: %d" %
                              (nome_jogador2, j2_carta4_velocidade))
                        print("\n\t%s possui maior valor de atributo, com %d pontos" % (
                            nome_jogador1, j1_carta1_velocidade))
                        pontuacao_jogador1 += VELOCIDADE
                        sleep(7)
                        cls()
                    else:
                        print("\n\n\t\tE M P A T E ")
                        print("\t\t\033[mAguarde...\033[m")
                        sleep(7)
                        cls()

                elif int(atributo) == 3 and int(j2_carta_escolhida) == 4 and int(j1_carta_escolhida) == 2:
                    if j2_carta4_velocidade > j1_carta2_velocidade:
                        print("\n\tValor do atributo de %s: %d" %
                              (nome_jogador1, j1_carta2_velocidade))
                        print("\n\tValor do atributo de %s: %d" %
                              (nome_jogador2, j2_carta4_velocidade))
                        print("\n\t%s possui maior valor de atributo, com %d pontos" % (
                            nome_jogador2, j2_carta4_velocidade))
                        pontuacao_jogador2 += VELOCIDADE
                        sleep(7)
                        cls()
                    elif j2_carta4_velocidade < j1_carta2_velocidade:
                        print("\n\tValor do atributo de %s: %d" %
                              (nome_jogador1, j1_carta2_velocidade))
                        print("\n\tValor do atributo de %s: %d" %
                              (nome_jogador2, j2_carta4_velocidade))
                        print("\n\t%s possui maior valor de atributo, com %d pontos" % (
                            nome_jogador1, j1_carta2_velocidade))
                        pontuacao_jogador1 += VELOCIDADE
                        sleep(7)
                        cls()
                    else:
                        print("\n\n\t\tE M P A T E ")
                        print("\t\t\033[mAguarde...\033[m")
                        sleep(7)
                        cls()

                elif int(atributo) == 3 and int(j2_carta_escolhida) == 4 and int(j1_carta_escolhida) == 3:
                    if j2_carta4_velocidade > j1_carta3_velocidade:
                        print("\n\tValor do atributo de %s: %d" %
                              (nome_jogador1, j1_carta3_velocidade))
                        print("\n\tValor do atributo de %s: %d" %
                              (nome_jogador2, j2_carta4_velocidade))
                        print("\n\t%s possui maior valor de atributo, com %d pontos" % (
                            nome_jogador2, j2_carta4_velocidade))
                        pontuacao_jogador2 += VELOCIDADE
                        sleep(7)
                        cls()
                    elif j2_carta4_velocidade < j1_carta3_velocidade:
                        print("\n\tValor do atributo de %s: %d" %
                              (nome_jogador1, j1_carta3_velocidade))
                        print("\n\tValor do atributo de %s: %d" %
                              (nome_jogador2, j2_carta4_velocidade))
                        print("\n\t%s possui maior valor de atributo, com %d pontos" % (
                            nome_jogador1, j1_carta3_velocidade))
                        pontuacao_jogador1 += VELOCIDADE
                        sleep(7)
                        cls()
                    else:
                        print("\n\n\t\tE M P A T E ")
                        print("\t\t\033[mAguarde...\033[m")
                        sleep(7)
                        cls()

                elif int(atributo) == 3 and int(j2_carta_escolhida) == 5 and int(j1_carta_escolhida) == 1:
                    if j2_carta5_velocidade > j1_carta1_velocidade:
                        print("\n\tValor do atributo de %s: %d" %
                              (nome_jogador1, j1_carta1_velocidade))
                        print("\n\tValor do atributo de %s: %d" %
                              (nome_jogador2, j2_carta5_velocidade))
                        print("\n\t%s possui maior valor de atributo, com %d pontos" % (
                            nome_jogador2, j2_carta5_velocidade))
                        pontuacao_jogador2 += VELOCIDADE
                        sleep(7)
                        cls()
                    elif j2_carta5_velocidade < j1_carta1_velocidade:
                        print("\n\tValor do atributo de %s: %d" %
                              (nome_jogador1, j1_carta1_velocidade))
                        print("\n\tValor do atributo de %s: %d" %
                              (nome_jogador2, j2_carta5_velocidade))
                        print("\n\t%s possui maior valor de atributo, com %d pontos" % (
                            nome_jogador1, j1_carta1_velocidade))
                        pontuacao_jogador1 += VELOCIDADE
                        sleep(7)
                        cls()
                    else:
                        print("\n\n\t\tE M P A T E ")
                        print("\t\t\033[mAguarde...\033[m")
                        sleep(7)
                        cls()

                elif int(atributo) == 3 and int(j2_carta_escolhida) == 5 and int(j1_carta_escolhida) == 2:
                    if j2_carta5_velocidade > j1_carta2_velocidade:
                        print("\n\tValor do atributo de %s: %d" %
                              (nome_jogador1, j1_carta2_velocidade))
                        print("\n\tValor do atributo de %s: %d" %
                              (nome_jogador2, j2_carta5_velocidade))
                        print("\n\t%s possui maior valor de atributo, com %d pontos" % (
                            nome_jogador2, j2_carta5_velocidade))
                        pontuacao_jogador2 += VELOCIDADE
                        sleep(7)
                        cls()
                    elif j2_carta5_velocidade < j1_carta2_velocidade:
                        print("\n\tValor do atributo de %s: %d" %
                              (nome_jogador1, j1_carta2_velocidade))
                        print("\n\tValor do atributo de %s: %d" %
                              (nome_jogador2, j2_carta5_velocidade))
                        print("\n\t%s possui maior valor de atributo, com %d pontos" % (
                            nome_jogador1, j1_carta2_velocidade))
                        pontuacao_jogador1 += VELOCIDADE
                        sleep(7)
                        cls()
                    else:
                        print("\n\n\t\tE M P A T E ")
                        print("\t\t\033[mAguarde...\033[m")
                        sleep(7)
                        cls()

                elif int(atributo) == 3 and int(j2_carta_escolhida) == 5 and int(j1_carta_escolhida) == 3:
                    if j2_carta5_velocidade > j1_carta3_velocidade:
                        print("\n\tValor do atributo de %s: %d" %
                              (nome_jogador1, j1_carta3_velocidade))
                        print("\n\tValor do atributo de %s: %d" %
                              (nome_jogador2, j2_carta5_velocidade))
                        print("\n\t%s possui maior valor de atributo, com %d pontos" % (
                            nome_jogador2, j2_carta5_velocidade))
                        pontuacao_jogador2 += VELOCIDADE
                        sleep(7)
                        cls()
                    elif j2_carta5_velocidade < j1_carta3_velocidade:
                        print("\n\tValor do atributo de %s: %d" %
                              (nome_jogador1, j1_carta3_velocidade))
                        print("\n\tValor do atributo de %s: %d" %
                              (nome_jogador2, j2_carta5_velocidade))
                        print("\n\t%s possui maior valor de atributo, com %d pontos" % (
                            nome_jogador1, j1_carta3_velocidade))
                        pontuacao_jogador1 += VELOCIDADE
                        sleep(7)
                        cls()
                    else:
                        print("\n\n\t\tE M P A T E ")
                        print("\t\t\033[mAguarde...\033[m")
                        sleep(7)
                        cls()

                elif int(atributo) == 3 and int(j2_carta_escolhida) == 6 and int(j1_carta_escolhida) == 1:
                    if j2_carta6_velocidade > j1_carta1_velocidade:
                        print("\n\tValor do atributo de %s: %d" %
                              (nome_jogador1, j1_carta1_velocidade))
                        print("\n\tValor do atributo de %s: %d" %
                              (nome_jogador2, j2_carta6_velocidade))
                        print("\n\t%s possui maior valor de atributo, com %d pontos" % (
                            nome_jogador2, j2_carta6_velocidade))
                        pontuacao_jogador2 += VELOCIDADE
                        sleep(7)
                        cls()
                    elif j2_carta6_velocidade < j1_carta1_velocidade:
                        print("\n\tValor do atributo de %s: %d" %
                              (nome_jogador1, j1_carta1_velocidade))
                        print("\n\tValor do atributo de %s: %d" %
                              (nome_jogador2, j2_carta6_velocidade))
                        print("\n\t%s possui maior valor de atributo, com %d pontos" % (
                            nome_jogador1, j1_carta1_velocidade))
                        pontuacao_jogador1 += VELOCIDADE
                        sleep(7)
                        cls()
                    else:
                        print("\n\n\t\tE M P A T E ")
                        print("\t\t\033[mAguarde...\033[m")
                        sleep(7)
                        cls()

                elif int(atributo) == 3 and int(j2_carta_escolhida) == 6 and int(j1_carta_escolhida) == 2:
                    if j2_carta6_velocidade > j1_carta2_velocidade:
                        print("\n\tValor do atributo de %s: %d" %
                              (nome_jogador1, j1_carta2_velocidade))
                        print("\n\tValor do atributo de %s: %d" %
                              (nome_jogador2, j2_carta6_velocidade))
                        print("\n\t%s possui maior valor de atributo, com %d pontos" % (
                            nome_jogador2, j2_carta6_velocidade))
                        pontuacao_jogador2 += VELOCIDADE
                        sleep(7)
                        cls()
                    elif j2_carta6_velocidade < j1_carta2_velocidade:
                        print("\n\tValor do atributo de %s: %d" %
                              (nome_jogador1, j1_carta2_velocidade))
                        print("\n\tValor do atributo de %s: %d" %
                              (nome_jogador2, j2_carta6_velocidade))
                        print("\n\t%s possui maior valor de atributo, com %d pontos" % (
                            nome_jogador1, j1_carta2_velocidade))
                        pontuacao_jogador1 += VELOCIDADE
                        sleep(7)
                        cls()
                    else:
                        print("\n\n\t\tE M P A T E ")
                        print("\t\t\033[mAguarde...\033[m")
                        sleep(7)
                        cls()

                elif int(atributo) == 3 and int(j2_carta_escolhida) == 6 and int(j1_carta_escolhida) == 3:
                    if j2_carta6_velocidade > j1_carta3_velocidade:
                        print("\n\tValor do atributo de %s: %d" %
                              (nome_jogador1, j1_carta3_velocidade))
                        print("\n\tValor do atributo de %s: %d" %
                              (nome_jogador2, j2_carta6_velocidade))
                        print("\n\t%s possui maior valor de atributo, com %d pontos" % (
                            nome_jogador2, j2_carta6_velocidade))
                        pontuacao_jogador2 += VELOCIDADE
                        sleep(7)
                        cls()
                    elif j2_carta6_velocidade < j1_carta3_velocidade:
                        print("\n\tValor do atributo de %s: %d" %
                              (nome_jogador1, j1_carta3_velocidade))
                        print("\n\tValor do atributo de %s: %d" %
                              (nome_jogador2, j2_carta6_velocidade))
                        print("\n\t%s possui maior valor de atributo, com %d pontos" % (
                            nome_jogador1, j1_carta3_velocidade))
                        pontuacao_jogador1 += VELOCIDADE
                        sleep(7)
                        cls()
                    else:
                        print("\n\n\t\tE M P A T E ")
                        print("\t\t\033[mAguarde...\033[m")
                        sleep(7)
                        cls()

        if pontuacao_jogador1 > pontuacao_jogador2:
            print("\n\n\n\n\t\t\t\t%s, PARABENS VOCE GANHOU A PARTIDA COM SCORE EQUIVALENTE A %d PONTOS" % (
                nome_jogador1, pontuacao_jogador1))
            sleep(7)
            cls()
        elif pontuacao_jogador1 < pontuacao_jogador2:
            print("\n\n\n\n\t\t\t\t%s, PARABENS VOCE GANHOU A PARTIDA COM SCORE EQUIVALENTE A %d PONTOS" % (
                nome_jogador2, pontuacao_jogador2))
            sleep(7)
            cls()
        elif pontuacao_jogador1 == pontuacao_jogador2:
            print("\n\n\n\n\t\t\t\tE  M  P  A  T  E")
            sleep(7)
            cls()
        if pontuacao_jogador1 > pontuacao_jogador2 and pontuacao_jogador1 > recorde:
            print("\n\n\t\t\t M U I T O   B E M, %s, V O C E  E  O  N O S S O  M A I S  N O V O  R E C O R D I S T A  C O M  %d  P O N T O S !! " % (
                nome_jogador1, pontuacao_jogador1))
            recorde = pontuacao_jogador1
            sleep(7)
            cls()
        elif pontuacao_jogador2 > pontuacao_jogador1 and pontuacao_jogador2 > recorde:
            print("\n\n\t\t\t M U I T O   B E M, %s, V O C E  E  O  N O S S O  M A I S  N O V O  R E C O R D I S T A  C O M  %d  P O N T O S !! " % (
                nome_jogador2, pontuacao_jogador2))
            recorde = pontuacao_jogador2
            sleep(7)
            cls()
    elif escolha == 2:
        informacoes_jogo()
