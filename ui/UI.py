from domeniu import toString, creeazaTranzactie, getCodul, getZiua, getSuma, getTipul
from repository.operatii import adaugaTranzactie, actualizareTranzactie, stergeTranzactiiDeLaOData, \
    stergeTranzactieCuprinseInPerioadaData, tranzactiiMaiMari, \
    tranzactiiEfectuateInainteDeOZi, tranzactiiDeUnAnumitTip, sumaTranzactiilorDeUnAnumitTip, \
    soldulContuluiLaODataAnume, tranzactiileDeUnAnumitTip, eliminaTranzactieDeUnAnumitTip, \
    eliminaTranzactiileDeUnAnumitTipMaiMiciDecatOSumaData, adauga_in_undo, undo, stergeTranzactieDeUnAnumitCod, \
    get_tranzactie_by_cod


def printMenu():
    print("1. Adauga tranzactie")
    print("2. Actualizeaza tranzactiile")
    print("3. Stergere tranzactii dintr-o data data")
    print("4. Stergere tranzactii dintr-o perioada")
    print("5. Stergere tranzactii dupa un anumit cod")
    print("6. Afiseaza tranzactiile mai mari decat o suma data")
    print("7. Afiseaza tranzactiile efectuate cu o zi inainte de ziua data si mai mari decat o suma data")
    print("8. Afiseaza tranzactiile de un anumit tip")
    print("9. Calculeaza suma tranzactiilor de un anumit tip")
    print("10. Afiseaza soldul dintr-o data data")
    print("11. Afiseaza tranzactiile de un anumit tip ordonate dupa suma")
    print("12. Eliminarea tuturor tranzactiilor de un anumit tip")
    print("13. Eliminarea tuturor tranzactiilor de un anumit tip mai mici decat o suma data")
    print("14. Undo")
    print("a. Afiseaza tranzactii")
    print("x. Iesire")

def printTranzactii(listaTranzactii):
    for tranzactie in listaTranzactii:
        print(toString(tranzactie))

def uiAdaugaTranzactie(listaTranzactii, lista_undo):
    codul = int(input("Dati codul: "))
    ziua = int(input("Dati ziua tranzactiei: "))
    suma = float(input("Dati suma tranzactiei: "))
    tipul = input("Dati tipul tranzactiei: ")
    tranzactie = creeazaTranzactie(codul, ziua, suma, tipul)
    adaugaTranzactie(tranzactie, listaTranzactii)
    lista_parametri = [codul]
    adauga_in_undo(lista_undo, "sterge", lista_parametri)

def uiActualizareTranzactie(listaTranzactii, lista_undo):
    cod = int(input("Dati codul: "))
    ziuaNoua = int(input("Dati ziua noua a tranzactiei: "))
    sumaNoua = float(input("Dati suma noua a tranzactiei: "))
    tipulNou = input("Dati tipul nou al tranzactiei: ")
    tranzactie = get_tranzactie_by_cod(listaTranzactii, cod)
    lista_parametri = [getCodul(tranzactie), getZiua(tranzactie), getSuma(tranzactie), getTipul(tranzactie)]
    adauga_in_undo(lista_undo, "modifica", lista_parametri)
    actualizareTranzactie(cod, ziuaNoua, sumaNoua, tipulNou, listaTranzactii)

def uiStergereTranzactiiDeLaOData(listaTranzactii):
    ziData = int(input("Dati ziua din care sa fie sterse tranzactiile: "))
    stergeTranzactiiDeLaOData(ziData, listaTranzactii)

def uiStergeTranzactiiDinPerioadaData(listaTranzactii):
    ziInceput = int(input("Dati ziua de inceput: "))
    ziSfarsit = int(input("Dati ziua de sfarsit: "))
    stergeTranzactieCuprinseInPerioadaData(ziInceput, ziSfarsit, listaTranzactii)

def uiStergeTranzactieDupaCod(listaTranzactii, lista_undo):
    codulDat = int(input("Dati codul tranzactiilor de sters: "))
    tranzactie_stearsa = stergeTranzactieDeUnAnumitCod(codulDat, listaTranzactii)
    lista_parametri = [tranzactie_stearsa]  # lista_parametri este o lista formata din avionul sters
    adauga_in_undo(lista_undo, "adauga", lista_parametri)

def uiTranzactiiSumeMaiMari(listaTranzactii):
    sumaData = float(input("Dati suma: "))
    return tranzactiiMaiMari(sumaData, listaTranzactii)

def uiTranzactiiEfectuateInainteDeOZi(listaTranzactii):
    ziData = int(input("Dati ziua: "))
    sumaData = float(input("Dati suma: "))
    return tranzactiiEfectuateInainteDeOZi(ziData, sumaData, listaTranzactii)

def uiTranzactiiDeUnAumitTip(listaTranzactii):
    tipDat = input("Dati tipul tranzactiei: ")
    return tranzactiiDeUnAnumitTip(tipDat, listaTranzactii)

def uiSumaTranzactiilorDeUnAnumitTip(listaTranzactii):
    tip = input("Dati tipul tranzactiei: ")
    return sumaTranzactiilorDeUnAnumitTip(tip, listaTranzactii)

def uiSoldulLaOAnumitaData(listaTranzactii):
    ziua = int(input("Dati ziua: "))
    return soldulContuluiLaODataAnume(ziua, listaTranzactii)

def uiTranzactiileDeUnAnumitTip(listaTranzactii):
    tip = input("Dati tipul: ")
    return tranzactiileDeUnAnumitTip(tip, listaTranzactii)

def uiEliminaTranzactieDupaTip(listaTranzactii):
    tipul = input("Dati tipul tranzactiilor de sters: ")
    eliminaTranzactieDeUnAnumitTip(tipul, listaTranzactii)

def uiEliminaTranzactiileDeUnAnumitTipMaiMiciDecatOSumaData(listaTranzactii):
    tipul = input("Dati tipul: ")
    sumaData = int(input("Dati suma: "))
    eliminaTranzactiileDeUnAnumitTipMaiMiciDecatOSumaData(tipul, sumaData, listaTranzactii)

def ui_undo(listaTranzactii, lista_undo):
    if len(lista_undo) == 0:
        print("Lista e in starea initiala.")
    else:
        undo(listaTranzactii, lista_undo)

def meniu():
    listaTranzactii = []
    lista_undo = []
    while True:
        printMenu()
        optiune = input("Dati optiunea: ")
        if optiune == "1":
            uiAdaugaTranzactie(listaTranzactii, lista_undo)
        elif optiune == "2":
            uiActualizareTranzactie(listaTranzactii, lista_undo)
        elif optiune == "3":
            uiStergereTranzactiiDeLaOData(listaTranzactii)
        elif optiune == "4":
            uiStergeTranzactiiDinPerioadaData(listaTranzactii)
        elif optiune == "5":
            uiStergeTranzactieDupaCod(listaTranzactii, lista_undo)
        elif optiune == "6":
            print(uiTranzactiiSumeMaiMari(listaTranzactii))
        elif optiune == "7":
            print(uiTranzactiiEfectuateInainteDeOZi(listaTranzactii))
        elif optiune == "8":
            print(uiTranzactiiDeUnAumitTip(listaTranzactii))
        elif optiune == "9":
            print(uiSumaTranzactiilorDeUnAnumitTip(listaTranzactii))
        elif optiune == "10":
            print(uiSoldulLaOAnumitaData(listaTranzactii))
        elif optiune == "11":
            print(uiTranzactiileDeUnAnumitTip(listaTranzactii))
        elif optiune == "12":
            uiEliminaTranzactieDupaTip(listaTranzactii)
        elif optiune == "13":
            uiEliminaTranzactiileDeUnAnumitTipMaiMiciDecatOSumaData(listaTranzactii)
        elif optiune == "14":
            ui_undo(listaTranzactii, lista_undo)
        elif optiune == "a":
            print(listaTranzactii)
        elif optiune == "x":
            break
        else:
            print("Optiune gresita! Reincercati")


