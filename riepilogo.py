def crea_riepilogo(apparati):
    totale = len(apparati)
    conteggi = {
        "totale": totale,
        "OK": sum(1 for v in apparati.values() if v["stato"] == "OK"),
        "ATTENZIONE": sum(1 for v in apparati.values() if v["stato"] == "ATTENZIONE"),
        "OFFLINE": sum(1 for v in apparati.values() if v["stato"] == "OFFLINE"),
    }
    return conteggi



