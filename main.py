from datetime import datetime, timedelta

def berechne_feierabend(startzeit_str, dauer_str):
    # Eingabe parsen
    startzeit = datetime.strptime(startzeit_str, "%H:%M")
    stunden, minuten = map(int, dauer_str.split(":"))
    arbeitsdauer = timedelta(hours=stunden, minutes=minuten)

    # Feierabend berechnen
    feierabend = startzeit + arbeitsdauer
    return feierabend.strftime("%H:%M")

def main():
    print("🕒 Arbeitszeit-Rechner")
    start = input("Wann hast du angefangen zu arbeiten? (HH:MM): ")
    dauer = input("Wie lange willst du heute arbeiten? (HH:MM): ")

    try:
        feierabend = berechne_feierabend(start, dauer)
        print(f"✅ Du kannst um {feierabend} Uhr Feierabend machen!")
    except Exception as e:
        print("❌ Fehler bei der Eingabe. Bitte im Format HH:MM eingeben.")
        print(e)

if __name__ == "__main__":
    main()
