from domeniu.domeniu import getZiua, getSuma, getTipul, setZiua, setSuma, setTipul, getCodul


def adaugaTranzactie(tranzactie_noua, listaTranzactii):
    '''
    adauga o tranzactie in lista

    :param ziua: nr.intreg
    :param suma: float
    :param tipul: string
    :param listaTranzactii: lista de dictionare de tipul tranzactie
    :return:
    '''

    listaTranzactii.append(tranzactie_noua)

def actualizareTranzactie(cod, ziuaNoua, sumaNoua, tipulNou, listaTranzactii):
    '''
    actualizeaza o tranzactie
    :param codul: nr intreg
    :param ziuaNoua: nr.intreg
    :param sumaNoua: float
    :param tipulNou: string
    :param listaTranzactii: lista de dictionare de tip tranzactie
    :return:
    '''
    for i in range(0, len(listaTranzactii)-1):
        if getCodul(listaTranzactii[i]) == cod:
            setZiua(listaTranzactii[i], ziuaNoua)
            setSuma(listaTranzactii[i], sumaNoua)
            setTipul(listaTranzactii[i], tipulNou)

def get_tranzactie_by_cod(listaTranzactii, cod):
    '''
    Functie ce returneaza o tranzactie dupa cod
    :param lista_avioane:
    :param cod:
    :return: avion
    '''

    for tranzactie in listaTranzactii:
        if getCodul(tranzactie) == cod:
            return tranzactie
    return {}

def stergeTranzactiiDeLaOData(ziData, listaTranzactii):
    '''
    sterge tranzactiile dintr-o zi data
    :param ziData: nr.intreg
    :param listaTranzactii: lista de dictionare de tipul tranzactie
    :return:
    '''

    i = 0
    while i < len(listaTranzactii):
        if getZiua(listaTranzactii[i]) == ziData:
            listaTranzactii.pop(i)
            i = i - 1
        i += 1


def stergeTranzactieCuprinseInPerioadaData(ziInceput, ziSfarsit, listaTranzactii):
    '''
    sterge tranzactiile cuprinse intr-o perioada data
    :param ziInceput: nr.intreg
    :param ziSfarsit: nr.intreg
    :param listaTranzactii: lista de dictionare de tipul tranzactie
    :return:
    '''

    i = 0
    while i < len(listaTranzactii):
        if getZiua(listaTranzactii[i]) > ziInceput and getZiua(listaTranzactii[i]) < ziSfarsit:
            listaTranzactii.pop(i)
            i = i - 1
        i += 1


def stergeTranzactieDeUnAnumitCod(codulDat, listaTranzactii):
    '''
    sterge o tranzactie daca are tipul dat
    :param codul: nr.intreg
    :param listaTranzactii: lista de dictionare de tipul tranzactie
    :return:
    '''
    tranzactie_stearsa = {}
    i = 0
    while i < len(listaTranzactii):
        if getCodul(listaTranzactii[i]) == codulDat:
            tranzactie_stearsa = listaTranzactii.pop(i)
            i = i - 1
        i += 1
    return tranzactie_stearsa

def tranzactiiMaiMari(sumaData, listaTranzactii):
    '''
    gaseste tranzactiile mai mari decat o suma data
    :param sumaData: float
    :param listaTranzactii: lista de dictionare de tip tranzactie
    :return: lista de dictionare de tip tranzactie
    '''

    rezultat = []
    for tranzactie in listaTranzactii:
        if sumaData < getSuma(tranzactie) :
            rezultat.append(tranzactie)
    return rezultat

def tranzactiiEfectuateInainteDeOZi(ziData, sumaData, listaTranzactii):
    '''
    gaseste tranzactiile efectuate inainte de o zi data si mai mari decat o suma data
    :param ziData: nr.intreg
    :param sumaData: float
    :param listaTranzactii: lista de dictionare de tip tranzactie
    :return: lista de dictionare de tip tranzactie
    '''

    rezultat = []
    for tranzactie in listaTranzactii:
        if ziData - 1 == getZiua(tranzactie):
            if sumaData < getSuma(tranzactie):
                rezultat.append(tranzactie)
    return rezultat

def tranzactiiDeUnAnumitTip(tipDat, listaTranzactii):
    '''
    gaseste tranzactiile de un anumit tip
    :param tipDat: string
    :param listaTranzactii: lista de dictionare de tip tranzactie
    :return: lista de dictionare de tip tranzactie
    '''

    rezultat = []
    for tranzactie in listaTranzactii:
        if tipDat == getTipul(tranzactie):
            rezultat.append(tranzactie)
    return rezultat

def sumaTranzactiilorDeUnAnumitTip(tip, listaTranzactii):
    '''
    calculeaza suma tranzactiilor de un anumit tip
    :param tip: string
    :param listaTranzactii: lista de dictionare de tipul tranzactie
    :return: sumaTranzactiilor
    '''

    sumaTranzactiilor = 0
    for i in range(len(listaTranzactii)):
        if getTipul(listaTranzactii[i]) == tip:
            suma = getSuma(listaTranzactii[i])
            sumaTranzactiilor += suma
    return sumaTranzactiilor

def soldulContuluiLaODataAnume(ziua, listaTranzactii):
    '''
    calculeaza soldul la o data precizata
    :param ziua: nr.intreg
    :param listaTranzactii: lista de dictionare de tipul tranzactie
    :return: soldul
    '''

    soldul = 0
    for i in range(len(listaTranzactii)):
        if getZiua(listaTranzactii[i]) == ziua:
            suma = getSuma(listaTranzactii[i])
            soldul += suma
    return soldul

def tranzactiileDeUnAnumitTip(tip, listaTranzactii):
    '''
    afiseaza tranzactiile de un anumit tip ordonate dupa suma
    :param tip: string
    :param listaTranzactii: lista de dictionare de tipul tranzactie
    :return: lista de dictionare de tip tranzactie
    '''

    lista = []
    for i in range(len(listaTranzactii)):
        if getTipul(listaTranzactii[i]) == tip:
            lista.append(listaTranzactii[i])
    lista.sort(key = getSuma)
    return lista

def eliminaTranzactieDeUnAnumitTip(tipul, listaTranzactii):
     '''
     elimina o tranzactie daca are tipul dat
     :param tipul: string
     :param listaTranzactii: lista de dictionare de tipul tranzactie
     :return:
     '''

     i = 0
     while i < len(listaTranzactii):
        if getTipul(listaTranzactii[i]) == tipul:
            listaTranzactii.pop(i)
            i = i - 1
        i += 1


def eliminaTranzactiileDeUnAnumitTipMaiMiciDecatOSumaData(tipul, sumaData, listaTranzactii):
    '''
    elimina o tranzactie daca are tipul dat si are suma mai mica decat o suma data
    :param tipul: string
    :param sumaData: float
    :param listaTranzactii: lista de dictionare de tipul tranzactie
    :return:
    '''
    i = 0
    while i < len(listaTranzactii):
        if getTipul(listaTranzactii[i]) == tipul:
            if getSuma(listaTranzactii[i]) < sumaData:
                listaTranzactii.pop(i)
                i = i - 1
        i += 1


def adauga_in_undo(lista_undo, nume_comanda, lista_parametri):
    '''
    Functie care adauga o comanda si parametrii aferenti in lista de undo
    :param lista_undo:
    :param nume_comanda:
    :param lista_parametri:
    :return:
    '''
    lista_parametri.insert(0, nume_comanda)
    lista_undo.append(lista_parametri)

def undo(listaTranzactii, lista_undo):
    '''
    Functie care face undo la ultima operatie
    :param listaTranzactii:
    :param lista_undo:
    :return:
    '''
    if len(lista_undo) != 0:
        lista_comanda = lista_undo[len(lista_undo)-1]
        nume_operatie = lista_comanda[0]
        if nume_operatie == "sterge":
            codul = lista_comanda[1]
            stergeTranzactieDeUnAnumitCod(codul, listaTranzactii)
                
        elif nume_operatie == "adauga":
            for tranzactie in lista_comanda[1:]:
                adaugaTranzactie(tranzactie, listaTranzactii)

        elif nume_operatie == "modifica":
            codul = lista_comanda[1]
            ziua = lista_comanda[2]
            suma = lista_comanda[3]
            tipul = lista_comanda[4]
            actualizareTranzactie(codul, ziua, suma, tipul, listaTranzactii)
        lista_undo.pop()