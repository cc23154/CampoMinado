from colorama import Fore, Back, Style, init
from random import randrange
from os import system

init()

def interVal(v, maximo):
    return -1 < v < maximo

def venceu():
    return len(pos) == 0

def perdeu():
    if modo != 0:
        return mapa[linOr][colOr][1] == "B"

def met1(lin, col):
    if mapa[lin][col][0] == "P":
        jogada(1, lin, col)

def met2(vet):
    global pos
    while vet:
        lin, col = vet.pop()
        for i in [-1 , 0, 1]:
            if interVal(lin + i, altura):
                for y in [-1, 0, 1]:
                    if interVal(col + y, largura) and not (y == 0 and i == 0):
                        pos = pos - {(lin + i,col + y)}
                        if mapa[lin + i][col + y][1] == 0 and mapa[lin + i][col + y][0] == "P":
                            vet.add((lin + i, col + y))
                        mapa[lin + i][col + y][0] = mapa[lin + i][col + y][2]

def met3(lin, col):
    mapa[lin][col][2] += 1

def met4(lin, col):
    mapa[lin][col][2] -= 1

def met5(lin, col):
    mapa[lin][col][2] += 1
    if mapa[lin][col][1] != "B":
        mapa[lin][col][1] += 1

def aux(met, lin, col):
    for i in [-1 , 0, 1]:
        if interVal(lin + i, altura):
            for y in [-1, 0, 1]:
                if interVal(col + y, largura) and not (y == 0 and i == 0):
                    met(lin + i, col + y)

def jogada(tipo, lin, col):
    global pos, colOr, linOr
    if tipo == 1:
        if mapa[lin][col][1] != "B":
            if mapa[lin][col][0] != "P":
                if mapa[lin][col][2] == 0:
                    aux(met1, lin, col)
            else:
               if mapa[lin][col][1] == 0:
                   mapa[lin][col][0] = 0
                   pos = pos - {(lin, col)}
                   met2({(lin, col)})
               else:
                   mapa[lin][col][0] = mapa[lin][col][1]
                   pos = pos - {(lin, col)}
        else:
            mapa[lin][col][0] = f"{Fore.RED}B{Style.RESET_ALL}"
            linOr = lin
            colOr = col
    else:
        if mapa[lin][col][0] in {"M", "P"}:
            if mapa[lin][col][0] != "M":
                mapa[lin][col][0] = "M"
                aux(met4, lin, col)
            else:
                mapa[lin][col][0] = "P"
                aux(met3, lin, col)

def printMapa():
    system('cls')
    print("   ", end="")
    print(*[1,2,3,4,5,6,7,8,9,10], sep=" | ")
    print()
    k = 1
    for i in range(altura):
        resp = []
        for t in mapa[i]:
            t = t[0]
            if t == 0:
                resp.append(" ")
            elif type(t) != type(1):
                if t == "M":
                    resp.append(f"{Fore.BLUE}M{Style.RESET_ALL}")
                elif t == "P":
                    resp.append(f"{Fore.GREEN}P{Style.RESET_ALL}")
                else:
                    resp.append(f"{Fore.RED}B{Style.RESET_ALL}")
            
            elif t < 3:
                resp.append(f"{Fore.LIGHTCYAN_EX}{t}{Style.RESET_ALL}")
            elif t < 5:
                resp.append(f"{Fore.LIGHTYELLOW_EX}{t}{Style.RESET_ALL}")
            else:
                resp.append(f"{Fore.LIGHTRED_EX}{t}{Style.RESET_ALL}")
        print(f"{k}" + " " * (1 + len(str(altura)) - len(str(k))), end="")
        k += 1
        print(*resp, sep=" | ")
        if i != altura - 1:
            print("    " + "---" * (largura - 1) + '-' * largura)

    print()

def minando():
    global pos
    _ = 0
    while _ < min(altura * largura, numBombas):
        lin, col = randrange(0, 10), randrange(0, 10)
        if mapa[lin][col][1] != "B":
            mapa[lin][col][1] = "B"
            pos = pos - {(lin, col)}
            aux(met5, lin, col)
            _ += 1

altura, largura = map(int, input("Digite a altura e largura do campo que deseja jogar: \n").split())
if (altura == 0) + (largura == 0) == 0:
    numBombas = int(input("Digite o numero de bombas que deseja: "))
    mapa = [[['P', 0, 0] for _ in range(largura)] for _ in range(altura)]
    pos  = {(i, y) for i in range(largura) for y in range(altura)}
    minando()
    continuar = not(venceu())
    while continuar:
        printMapa()
        _ = input("Digite a linha e a coluna que deseja ativar(se quiser marcar adcione ao final um numero 0), separa por espaço os valores necessarios: ").split()
        modo = 1
        if len(_) == 3:
            modo = int(_[2])
        linOr = int(_[0]) - 1
        colOr = int(_[1]) - 1
        if modo in {1, 0}:
            if interVal(linOr, altura) and interVal(colOr, largura):
                jogada(modo, linOr, colOr)
        continuar = not(venceu()) and not(perdeu())
    printMapa()
    if perdeu():
        print("Vagabunda fudida")
    else:
        print("Inteligente dms slk")