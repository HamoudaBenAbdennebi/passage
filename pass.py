

def saisieN():
    N = int(input('donner N : '))
    while N > 101 or N < 4:
        N = int(input('donner N : '))
    return N


def replire(Tmatricules, Tscores, N):
    for i in range(N):
        print("donner la matricule de l'employée N", i+1, end=' ')
        mat = int(input())
        while len(str(mat)) != 8:
            print("donner la matricule de l'employée N", i+1, end=' ')
            mat = int(input())
        print("donner le score de l'employée N", i+1, end=' ')
        score = int(input())
        while score > 120 or score < 20:
            print("donner le score de l'employée N", i+1, end=' ')
            score = int(input())
        Tmatricules.append(mat)
        Tscores.append(score)


def ranger(Tmatricules, Tscores, N):
    verif = True
    passage = 0
    while verif:
        verif = False
        passage += 1
        for i in range(0, len(Tscores) - passage):
            if Tscores[i] > Tscores[i + 1]:
                verif = True
                Tscores[i], Tscores[i + 1] = \
                    Tscores[i + 1], Tscores[i]
                Tmatricules[i], Tmatricules[i + 1] = \
                    Tmatricules[i + 1], Tmatricules[i]


def reverse(T, N):
    TR = []
    for i in range(N-1, -1, -1):
        TR.append(T[i])
    return TR


def winners(TmatriculesR, TscoresR, N):
    per = (N/100)*25
    per = int(round(per))
    for i in range(per):
        print(TmatriculesR[i])


Tmatricules = []
Tscores = []
N = saisieN()

replire(Tmatricules, Tscores, N)
ranger(Tmatricules, Tscores, N)


TmatriculesR = reverse(Tmatricules, N)
TscoresR = reverse(Tscores, N)

winners(TmatriculesR, TscoresR, N)
