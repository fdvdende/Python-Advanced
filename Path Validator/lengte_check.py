import os

def find_longest_path(path):
    # Vind het langste pad recursief
    langste_pad = ""
    max_lengte = 0

    for root, dirs, files in os.walk(path):
        for file in files:
            file_pad = os.path.join(root, file)
            if len(file_pad) > max_lengte:
                max_lengte = len(file_pad)
                langste_pad = file_pad

    return langste_pad, max_lengte

def main():
    # Vraag het bronpad aan de gebruiker
    bron_pad = input("Voer het bronpad in ")

    # Vraag het bestemmingspad aan de gebruiker
    bestemming_pad = input("Voer het bestemmingspad in ")

    # Vind het langste pad en de lengte ervan voor de bron
    langste_bron_pad, bron_lengte = find_longest_path(bron_pad)

    # Bereken de lengte van het bestemmingspad
    bestemming_lengte = bron_lengte + len(bestemming_pad)

    if langste_bron_pad:
        print(f"\nHet langste bronpad is: {langste_bron_pad}")
        print(f"Totale lengte van het langste bronpad: {bron_lengte}")

        print(f"\nHet opgegeven bestemmingspad is: {bestemming_pad}")
        print(f"Totale lengte van het bestemmingspad: {bestemming_lengte}")

        # Controleer of de totale lengte minder is dan 256 tekens
        if bestemming_lengte < 256:
            print("Totale lengte van bron- en bestemmingspaden is in orde.")
        else:
            print("Totale lengte van bron- en bestemmingspaden overschrijdt 256 tekens.")
    else:
        print("\nGeen bestanden of mappen gevonden.")

if __name__ == "__main__":
    main()
