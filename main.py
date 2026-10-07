from registro_apparati import APPARATI, aggiungi_apparato, aggiorna_stato
from riepilogo import crea_riepilogo

def main():
    print("=== REGISTRO INIZIALE ===")
    print(APPARATI)

    print("\n=== PROVA AGGIORNAMENTO ED INSERIMENTO ===")
    aggiungi_apparato("ALT-04", "Altimetro Radar", "BUS-B", "OK")
    aggiorna_stato("COM-02", "OK")

    print("\n=== RIEPILOGO GENERALE ===")
    riepilogo = crea_riepilogo(APPARATI)
    for chiave, valore in riepilogo.items():
        print(f"{chiave}: {valore}")

if __name__ == "__main__":
    main()