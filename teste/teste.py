from domeniu import creeazaTranzactie, getZiua, getSuma, getTipul, setZiua, setSuma, setTipul, getCodul, setCodul
from repository.operatii import adaugaTranzactie, actualizareTranzactie, stergeTranzactiiDeLaOData, \
    stergeTranzactieCuprinseInPerioadaData, tranzactiiMaiMari, \
    tranzactiiEfectuateInainteDeOZi, tranzactiiDeUnAnumitTip, soldulContuluiLaODataAnume, \
    sumaTranzactiilorDeUnAnumitTip, tranzactiileDeUnAnumitTip, eliminaTranzactieDeUnAnumitTip, \
    eliminaTranzactiileDeUnAnumitTipMaiMiciDecatOSumaData, stergeTranzactieDeUnAnumitCod


def testCreeazaTranzactie():
    tranzactie = creeazaTranzactie(143, 12, 23.7, "intrare")
    assert getCodul(tranzactie) == 143
    assert getZiua(tranzactie) == 12
    assert getSuma(tranzactie) == 23.7
    assert getTipul(tranzactie) == "intrare"
'''
def testAdaugaTranzactie():
    listaTranzactii = []
    adaugaTranzactie(143, 12, 23.7, "intrare", listaTranzactii)
    adaugaTranzactie(756, 23, 30, "iesire", listaTranzactii)

    assert len(listaTranzactii) == 2
    assert(getCodul(listaTranzactii[0]) == 143)
    assert(getZiua(listaTranzactii[0]) == 12)
    assert(getSuma(listaTranzactii[0]) == 23.7)
    assert(getTipul(listaTranzactii[0]) == "intrare")
    assert(getCodul(listaTranzactii[1]) == 756)
    assert (getZiua(listaTranzactii[1]) == 23)
    assert (getSuma(listaTranzactii[1]) == 30)
    assert (getTipul(listaTranzactii[1]) == "iesire")
'''
def testSetteri():
    tranzactie = creeazaTranzactie(143, 12, 30.7, "intrare")

    setCodul(tranzactie, 143)
    assert getCodul(tranzactie) == 143

    setZiua(tranzactie, 22)
    assert getZiua(tranzactie) == 22

    setSuma(tranzactie, 30.4)
    assert getSuma(tranzactie) == 30.4

    setTipul(tranzactie, "intrare")
    assert getTipul(tranzactie) == "intrare"

def testActualizareTranzactie():

    codul = 143
    ziuaNoua = 13
    sumaNoua = 24
    tipulNou = "iesire"
    listaTranzactii = []
    adaugaTranzactie(143, 12, 23.7, "intrare", listaTranzactii)
    adaugaTranzactie(789, 23, 30, "iesire", listaTranzactii)
    actualizareTranzactie(codul, ziuaNoua, sumaNoua, tipulNou, listaTranzactii)

    assert len(listaTranzactii) == 2
    assert (getZiua(listaTranzactii[0]) == 13)
    assert (getSuma(listaTranzactii[0]) == 24)
    assert (getTipul(listaTranzactii[0]) == "iesire")
    assert (getZiua(listaTranzactii[1]) == 23)
    assert (getSuma(listaTranzactii[1]) == 30)
    assert (getTipul(listaTranzactii[1]) == "iesire")


def testStergeTranzactiiDeLaOData():
    listaTranzactii = []
    adaugaTranzactie(143, 12, 27.8, "intrare", listaTranzactii)
    adaugaTranzactie(132, 27, 15, "iesire", listaTranzactii)

    stergeTranzactiiDeLaOData(12, listaTranzactii)

    assert(len(listaTranzactii) == 1)

def testStergeTranzactieCuprinseInPerioadaData():
    listaTranzactii = []
    adaugaTranzactie(143, 12, 27.8, "intrare", listaTranzactii)
    adaugaTranzactie(789, 27, 15, "iesire", listaTranzactii)

    stergeTranzactieCuprinseInPerioadaData(11, 28, listaTranzactii)

    assert(len(listaTranzactii) == 0)

def testStergeTranzactieDeUnAnumitCod():
    listaTranzactii = []
    adaugaTranzactie(132, 12, 27.8, "intrare", listaTranzactii)
    adaugaTranzactie(345, 27, 15, "iesire", listaTranzactii)

    stergeTranzactieDeUnAnumitCod(132, listaTranzactii)

    assert(len(listaTranzactii) == 1)

def testTranzactiiSumeMaiMari():
    listaTranzactii = []
    adaugaTranzactie(567, 12, 30.12, "intrare", listaTranzactii)
    adaugaTranzactie(345, 22, 25, "intrare", listaTranzactii)
    adaugaTranzactie(234, 3, 11, "iesire", listaTranzactii)

    rezultat = tranzactiiMaiMari(22.06, listaTranzactii)

    assert len(rezultat) == 2
    assert getSuma(rezultat[0]) == 30.12
    assert getSuma(rezultat[1]) == 25

def testTranzactiiEfectuateInainteDeOZi():
    listaTranzactii = []
    adaugaTranzactie(143, 12, 30.12, "intrare", listaTranzactii)
    adaugaTranzactie(123, 22, 25, "intrare", listaTranzactii)
    adaugaTranzactie(989, 3, 11, "iesire", listaTranzactii)

    rezultat = tranzactiiEfectuateInainteDeOZi(13, 10, listaTranzactii)

    assert len(rezultat) == 1
    assert getSuma(rezultat[0]) == 30.12

def testTranzactiiDeUnAnumitTip():
    listaTranzactii = []
    adaugaTranzactie(143, 12, 30.12, "intrare", listaTranzactii)
    adaugaTranzactie(132, 22, 25, "intrare", listaTranzactii)
    adaugaTranzactie(745, 3, 11, "iesire", listaTranzactii)

    rezultat = tranzactiiDeUnAnumitTip("iesire", listaTranzactii)

    assert len(rezultat) == 1
    assert getSuma(rezultat[0]) == 11

def testSoldLaData():
    listaTranzactii = []
    adaugaTranzactie(678, 12, 30, "intrare", listaTranzactii)
    adaugaTranzactie(634, 12, 25, "intrare", listaTranzactii)
    adaugaTranzactie(980, 3, 11, "iesire", listaTranzactii)

    rezultat = soldulContuluiLaODataAnume(12, listaTranzactii)

    assert (rezultat) == 55

def testSumaTranzactiilorDeUnAnumitTip():
    listaTranzactii = []
    adaugaTranzactie(123, 12, 30, "intrare", listaTranzactii)
    adaugaTranzactie(167, 12, 25, "intrare", listaTranzactii)
    adaugaTranzactie(678, 3, 11, "iesire", listaTranzactii)

    rezultat = sumaTranzactiilorDeUnAnumitTip("intrare", listaTranzactii)

    assert (rezultat) == 55

def testTranzactiileDeUnAnumitTip():
    listaTranzactii = []
    adaugaTranzactie(789, 12, 30.12, "intrare", listaTranzactii)
    adaugaTranzactie(234, 12, 25, "intrare", listaTranzactii)
    adaugaTranzactie(906, 3, 11, "iesire", listaTranzactii)

    rezultat = tranzactiileDeUnAnumitTip("intrare", listaTranzactii)

    assert len(rezultat) == 2
    assert getSuma(rezultat[0]) == 25
    assert getSuma(rezultat[1]) == 30.12

def testEliminaTranzactieDeUnAnumitTip():
    listaTranzactii = []
    adaugaTranzactie(456, 12, 27.8, "intrare", listaTranzactii)
    adaugaTranzactie(678, 27, 15, "iesire", listaTranzactii)

    eliminaTranzactieDeUnAnumitTip("intrare", listaTranzactii)

    assert(len(listaTranzactii) == 1)

def testEliminaTranzactiileDeUnAnumitTipMaiMiciDecatOSumaData():
    listaTranzactii = []
    adaugaTranzactie(678, 12, 27.8, "intrare", listaTranzactii)
    adaugaTranzactie(345, 27, 15, "iesire", listaTranzactii)

    eliminaTranzactiileDeUnAnumitTipMaiMiciDecatOSumaData("intrare", 30, listaTranzactii)

    assert(len(listaTranzactii) == 1)

def testAll():
    testCreeazaTranzactie()
    testSetteri()
    testAdaugaTranzactie()
    testActualizareTranzactie()
    testStergeTranzactiiDeLaOData()
    testStergeTranzactieCuprinseInPerioadaData()
    testStergeTranzactieDeUnAnumitCod()
    testTranzactiiEfectuateInainteDeOZi()
    testTranzactiiDeUnAnumitTip()
    testSoldLaData()
    testSumaTranzactiilorDeUnAnumitTip()
    testTranzactiileDeUnAnumitTip()
    testTranzactiiSumeMaiMari()
    testEliminaTranzactieDeUnAnumitTip()
    testEliminaTranzactiileDeUnAnumitTipMaiMiciDecatOSumaData()
