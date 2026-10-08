def filtra_per_stato(apparati, stato):
    return [
        (codice, dati)
        for codice, dati in apparati.items()
        if dati["stato"] == stato
    ]


def filtra_per_bus(apparati, bus):
    return [
        (codice, dati)
        for codice, dati in apparati.items()
        if dati["bus"] == bus
    ]


def filtra_per_tipo(apparati, tipo):
    return [
        (codice, dati)
        for codice, dati in apparati.items()
        if dati["tipo"] == tipo
    ]

