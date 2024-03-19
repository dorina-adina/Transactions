def creeazaTranzactie(codul, ziua, suma, tipul):
    '''
    creeaza un dictionar de tipul tranzactie
    :param codul: nr.intreg
    :param ziua: nr.intreg
    :param suma: float
    :param tipul: string
    :return: un dicitonar de tipul tranzactie
    '''
    #return {
    #    "codul": codul,
    #   "ziua": ziua,
    #    "suma": suma,
    #    "tipul": tipul }
    dictionar_tranzactie = { "codul": codul, "ziua": ziua, "suma": suma, "tipul": tipul}
    return dictionar_tranzactie

def getCodul(tranzactie):
    return tranzactie["codul"]

def getZiua(tranzactie):
    return tranzactie["ziua"]

def getSuma(tranzactie):
    return tranzactie["suma"]

def getTipul(tranzactie):
    return tranzactie["tipul"]

def setCodul(tranzactie, codul):
   tranzactie["codul"] = codul

def setZiua(tranzactie, ziua):
    tranzactie["ziua"] = ziua

def setSuma(tranzactie, suma):
    tranzactie["suma"] = suma

def setTipul(tranzactie, tipul):
    tranzactie["tipul"] = tipul

def toString(tranzactie):
    return  "Codul: " + str(getCodul(tranzactie)) + "ziua: " + str(getZiua(tranzactie)) + ", suma: " + str(getSuma(tranzactie)) + \
           ", tipul: " + str(getTipul(tranzactie))