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


def filtra_per_nome(apparati, nome, contiene=True, case_insensitive=True):
    if nome is None:
        return []

    results = []
    for codice, dati in apparati.items():
        valore = dati.get("nome")
        if valore is None:
            continue

        if case_insensitive:
            nome_cmp = nome.lower()
            valore_cmp = valore.lower()
        else:
            nome_cmp = nome
            valore_cmp = valore

        if contiene:
            if nome_cmp in valore_cmp:
                results.append((codice, dati))
        else:
            if nome_cmp == valore_cmp:
                results.append((codice, dati))

    return results
