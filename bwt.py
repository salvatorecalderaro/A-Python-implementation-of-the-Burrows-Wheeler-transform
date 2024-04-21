# BWT

def bwt(s):
    aus=s
    rotazioni_cicliche=[]
    #Creazione ed ordinamento lessicografico delle rotazioni cicliche della stringa in input
    for i in range(len(s)):
        w=aus[-1]+aus[:-1]
        n="".join(w)
        aus=n
        rotazioni_cicliche.append(n)
    rotazioni_cicliche=sorted(rotazioni_cicliche)

    print("Rotazioni cicliche in ordine lessicografico:")
    for i in rotazioni_cicliche:
        print(i)

    """
    Output della BWT:
    inidice I a cui corrisponde la stringa originale nella matrice delle rotazioni cicliche
    F: prima colonna della matrice delle rotazioni cicliche
    L: ultima colonna della matrice delle rotazioni cicliche
    """
    F=[]
    L=[]
    for i in range(len(rotazioni_cicliche)):
        if(rotazioni_cicliche[i]==s):
            I=i
        L.append(rotazioni_cicliche[i][len(s)-1])
        F.append(rotazioni_cicliche[i][0])
    ris=""
    ris=ris.join(L)
    return (I, ris, L,F)


def invBwt(F,L,I):
    X=L
    thau=[[],[]]
    # Costruzione della permutazione thau
    for i in range(0, len(F)):
        thau[0].append(i)
        j=L.index(F[i])
        L[j]=0
        thau[1].append(j)
    print("Permutazione thau:")
    print(thau)

    #Ricostruzione della stringa di partenza
    ris=[]
    ris.append(F[I])
    while(len(ris)< (len(F))):
        i=thau[1][I]
        ris.append(F[i])
        I=i
    s=""
    s=s.join(ris)
    return s


s=input("Inserire la stringa ")
I,ris,L,F=bwt(s)
print("Output: %d %s " %(I,ris))
ris=invBwt(F,L,I)
print("\n")
print(ris)
