from registro_apparati import APPARATI, aggiungi_apparato, aggiorna_stato
from riepilogo import crea_riepilogo
from report import filtra_per_stato, filtra_per_bus

def main():
    print("=== REGISTRO INIZIALE ===")
    print(APPARATI)

    print("\n=== PROVA AGGIORNAMENTO ED INSERIMENTO ===")
    aggiungi_apparato("ALT-04", "Altimetro Radar", "BUS-B", "OK")
    aggiorna_stato("COM-02", "OK")

    print("\n=== REPORT PER STATO ===")
    print("Apparati OK:", filtra_per_stato(APPARATI, "OK"))
    print("Apparati ATTENZIONE:", filtra_per_stato(APPARATI, "ATTENZIONE"))
    print("Apparati OFFLINE:", filtra_per_stato(APPARATI, "OFFLINE"))

    print("\n=== REPORT PER BUS ===")
    print("BUS-A:", filtra_per_bus(APPARATI, "BUS-A"))
    print("BUS-B:", filtra_per_bus(APPARATI, "BUS-B"))

    print("\n=== RIEPILOGO GENERALE ===")
    riepilogo = crea_riepilogo(APPARATI)

    for chiave, valore in riepilogo.items():
        print(f"{chiave}: {valore}")


if __name__ == "__main__":
    main()