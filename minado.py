from time import time
from colorama import Fore, Back, Style, init
from random import randrange
from os import system

def interVal(v, maximo):
    return -1 < v < maximo

def venceu():
    return pos == 0

def perdeu():
    if modo != 0:
        return mapa[linOr][colOr][1] == "B"

def met1(valores):
    global linOr, colOr, pos
    for lin, col in valores:
        if mapa[lin][col][0] == "P":
            jogada(1, lin, col)

def met2(lin, col):
    global pos
    vet = set()
    auxTop(qualAux(lin, col), lin, col, vet)
    while vet:
        lin, col = vet.pop()
        if mapa[lin][col][0] == "P":
            if mapa[lin][col][1] == 0:
                auxTop(qualAux(lin, col), lin, col, vet)
            pos -= 1
            mapa[lin][col][0] = mapa[lin][col][1]

def met3(valores):
    for lin, col in valores:
        mapa[lin][col][2] += 1

def met4(valores):
    for lin, col in valores:
        mapa[lin][col][2] -= 1

def met5(valores):
    for lin, col in valores:
        mapa[lin][col][2] += 1
        if mapa[lin][col][1] != "B":
            mapa[lin][col][1] += 1


def qualAux(lin, col):
    v = {0 <lin < altura - 1, 0 < col < largura - 1}
    if {True, True} == v:
        return [[-1, 0, 1], [-1, 0, 1]]
    elif v == {True, False}:
        if col == 0:
            return [[-1, 0, 1], [0, 1]]
        elif col == largura - 1:
            return [[-1, 0, 1], [0, -1]]
        elif lin == 0:
            return [[0, 1], [-1, 0, 1]]
        else:
            return [[-1, 0], [-1, 0, 1]]
    else:
        if lin == 0:
            if col == 0:
                return [[0, 1], [0, 1]]
            else:
                return [[0, 1], [-1, 0]]
        elif col == 0:
            return [[-1, 0], [1, 0]]
        else:
            return [[-1, 0], [-1, 0]]

def auxTop(valores, lin, col, ant):
    interAl, interCol = valores
    for i in interAl:
        for y in interCol:
            if not(y == 0 and i == 0):
                ant.add((lin + i, col + y))


def auxPro(valores, lin, col):
    v = []
    interAl, interCol = valores
    for i in interAl:
        for y in interCol:
            if not(y == 0 and i == 0):
                v.append([lin + i, col + y])
    return v

def jogada(tipo, lin, col):
    global pos, colOr, linOr
    if tipo == 1:
        if mapa[lin][col][1] != "B":
            if mapa[lin][col][0] != "P":
                if mapa[lin][col][2] == 0:
                    met1(auxPro(qualAux(lin, col), lin, col))
            else:
               if mapa[lin][col][1] == 0:
                   mapa[lin][col][0] = 0
                   pos -= 1
                   met2(lin, col)
               else:
                   mapa[lin][col][0] = mapa[lin][col][1]
                   pos -= 1
        else:
            mapa[lin][col][0] = f"{Fore.RED}B{Style.RESET_ALL}"
            linOr = lin
            colOr = col
    else:
        if mapa[lin][col][0] in {"M", "P"}:
            if mapa[lin][col][0] != "M":
                mapa[lin][col][0] = "M"
                met4(auxPro(qualAux(lin, col), lin, col))
            else:
                mapa[lin][col][0] = "P"
                met3(auxPro(qualAux(lin, col), lin, col))

def printMapaFinal():
    system('cls')
    print("    ", end="")
    print(*[1,2,3,4,5,6,7,8,9,10], sep=" | ")
    print()
    k = 1
    for i in range(altura):
        resp = []
        for t in mapa[i]:
            f = t
            t = t[0]
            if t == 0:
                resp.append(f" {Style.RESET_ALL}")
            elif type(t) != type(1):
                if t == "M" and f[1] == "B":
                    resp.append(f"{Fore.GREEN}✔{Style.RESET_ALL}")
                elif t == "P" and f[1] == "B":
                    resp.append(f"{Fore.RED}✔{Style.RESET_ALL}")
                elif t == "P":
                    resp.append(f"{Back.GREEN} {Style.RESET_ALL}")
                else:
                    resp.append(f"{Fore.RED}✖{Style.RESET_ALL}")
            elif t < 3:
                resp.append(f"{Fore.LIGHTCYAN_EX}{t}{Style.RESET_ALL}")
            elif t < 5:
                resp.append(f"{Fore.LIGHTYELLOW_EX}{t}{Style.RESET_ALL}")
            else:
                resp.append(f"{Fore.LIGHTRED_EX}{t}{Style.RESET_ALL}")
        print(f"{k}" + " " * (2 + len(str(altura)) - len(str(k)) - 1)+ f" {Style.RESET_ALL}", end="")
        k += 1
        print(*resp, sep=f" | {Style.RESET_ALL}", end="")
        print(f" {Style.RESET_ALL}")
        if i != altura - 1:
            print(3* " " + f"⊢--+---+---+---+---+---+---+---+---+--⊣{Style.RESET_ALL}") #--+-+-+-+-+-+-+-+-+-+-+-+-+-
    print()

def printMapa():
    system('cls')
    print("    ", end="")
    print(*[1,2,3,4,5,6,7,8,9,10], sep=" | ")
    print()
    k = 1
    for i in range(altura):
        resp = []
        for t in mapa[i]:
            t = t[0]
            if t == 0:
                resp.append(f" {Style.RESET_ALL}")
            elif type(t) != type(1):
                if t == "M":
                    resp.append(f"{Back.BLUE} {Style.RESET_ALL}")
                elif t == "P":
                    resp.append(f"{Back.GREEN} {Style.RESET_ALL}")
                else:
                    resp.append(f"{Fore.RED}✖{Style.RESET_ALL}")
            elif t < 3:
                resp.append(f"{Fore.LIGHTCYAN_EX}{t}{Style.RESET_ALL}")
            elif t < 5:
                resp.append(f"{Fore.LIGHTYELLOW_EX}{t}{Style.RESET_ALL}")
            else:
                resp.append(f"{Fore.LIGHTRED_EX}{t}{Style.RESET_ALL}")
        print(f"{k}" + " " * (2 + len(str(altura)) - len(str(k)) - 1)+ f" {Style.RESET_ALL}", end="")
        k += 1
        print(*resp, sep=f" | {Style.RESET_ALL}", end="")
        print(f" {Style.RESET_ALL}")
        if i != altura - 1:
            print(3* " " + f"⊢--+---+---+---+---+---+---+---+---+--⊣{Style.RESET_ALL}") #--+-+-+-+-+-+-+-+-+-+-+-+-+-
    print()

def minando():
    global pos
    _ = 0
    while _ < numBombas:
        lin, col = randrange(0, altura), randrange(0, largura)
        if mapa[lin][col][1] != "B":
            mapa[lin][col][1] = "B"
            pos -= 1
            met5(auxPro(qualAux(lin, col), lin, col))
            _ += 1

altura, largura = int(input("Digite a altura do campo que deseja jogar: ")), 10
if (altura == 0) + (largura == 0) == 0:
    numBombas = int(input("Digite o numero de bombas que deseja: "))
    if numBombas + 1 <  altura * largura:
        v = time()
        numJogas = 0
        mapa = [[['P', 0, 0] for _ in range(largura)] for _ in range(altura)]
        pos  = altura * largura
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
                    numJogas += 1
            continuar = not(venceu()) and not(perdeu())
        printMapaFinal()
        if venceu():
            print("Você Venceu")
        else:
            print("Você Perdeu")
        print(f"Numero de jogadas: {numJogas}\nTempo de jogo: {time() - v}")
