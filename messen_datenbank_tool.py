import sqlite3
import csv
import re

"""
Bemerkung: Komma-Trennzeichen , ist Aufzählungszeichen - für Markdown
Kopiere 03-Messübung-Kundenbeanstandung-Ursache.md nach messuebung_eingabe.txt
# Datenbank-Tool: messen_datenbank_tool.py
DB_NAME: messen.db
EXPORT_DATEINAME: messen_datenbank_sicherung.csv
IMPORT_DATEINAME: messen_datenbank_sicherung.csv
TEXTDATEI_PFAD: messuebung_eingabe.txt <= 03-Messübung-Kundenbeanstandung-Ursache.md
MD_AUSGABE_DATEI: messen_daten_ausgabe.md => Pra-Keywords-02-Messen-Kundenbeanstandung-Ursache.pdf
"""


# anpassen
DB_NAME = 'messen.db'
EXPORT_DATEINAME = 'messen_datenbank_sicherung.csv'
IMPORT_DATEINAME = 'messen_datenbank_sicherung.csv'
TEXTDATEI_PFAD = 'messuebung_eingabe.txt'
MD_AUSGABE_DATEI = 'messen_daten_ausgabe.md'
DANGEROUS_KEYWORDS = ["DROP", "DELETE", "INSERT", "UPDATE", "SELECT", "--", ";"]

####################################################################
def verbindung_herstellen(db_name=DB_NAME):
    try:
        verbindung = sqlite3.connect(db_name)
        zeiger = verbindung.cursor()
        return verbindung, zeiger
    except sqlite3.Error as e:
        print(f"Fehler beim Verbinden zur Datenbank: {e}")
        return None, None


def tabelle_erstellen(zeiger):
    zeiger.execute('''
        CREATE TABLE IF NOT EXISTS messungen (
            ID INTEGER PRIMARY KEY,
            Uebungsnummer TEXT,
            Fahrzeug TEXT,
            Problem TEXT,
            Fehlerspeicher TEXT,
            Istwerte TEXT,
            Ursache TEXT,
            Besonderheit TEXT
        )
    ''')


def daten_anzeigen(zeiger):
    zeiger.execute("SELECT * FROM messungen")
    ergebnisse = zeiger.fetchall()
    # Debug-Ausgabe für Daten aus der Datenbank
    print(f"Gefundene Datensätze in der Datenbank: {len(ergebnisse)}")
    formatierte_ausgabe(ergebnisse, in_datei_speichern=True)




def formatierte_ausgabe(ergebnisse, in_datei_speichern=False, suchbegriff=None, spaltenname=None):
    header = [
        "ID",
        "Uebungsnummer",
        "Fahrzeug",
        "Problem",
        "Fehlerspeicher",
        "Istwerte",
        "Ursache",
        "Besonderheit"
    ]

    def formatiere_wert(wert, terminal=False):
        if '$' in wert:
            teile = []
            temp = ''
            in_math = False
            for char in wert:
                if char == '$':
                    in_math = not in_math
                if char == ',' and not in_math:
                    teile.append(temp.strip())
                    temp = ''
                else:
                    temp += char
            if temp:
                teile.append(temp.strip())
        else:
            teile = wert.split(',')
        
        einrueckung = "\t" if terminal else "    "
        formatierter_wert = ("\n" + einrueckung if "\n" not in wert else "") + "- " + ("\n" + einrueckung + "- ").join([item.strip() for item in teile])
        
        return formatierter_wert

    if in_datei_speichern:
        with open(MD_AUSGABE_DATEI, 'w', encoding='utf-8') as datei:
            datei.write("# Datenbank-Tool\n")
            konfiguration = [
                ("DB_NAME", DB_NAME),
                ("EXPORT_DATEINAME", EXPORT_DATEINAME),
                ("IMPORT_DATEINAME", IMPORT_DATEINAME),
                ("TEXTDATEI_PFAD", TEXTDATEI_PFAD),
                ("MD_AUSGABE_DATEI", MD_AUSGABE_DATEI)
            ]
            for key, value in konfiguration:
                datei.write(f"- {key}: {value}\n")
            datei.write("\n")
            
            if suchbegriff and spaltenname:
                datei.write(f"## Suchergebnisse für '{suchbegriff}' in Spalte '{spaltenname}'\n")
                datei.write("\n")
            
            datei.write("## Messübung und Kundenbeanstandung\n")
            for reihe in ergebnisse:
                problem = reihe[header.index("Problem")]
                datei.write(f"### {problem}\n")
                for titel, wert in zip(header, reihe):
                    if titel == "Besonderheit":
                        wert = formatiere_wert(wert)
                    datei.write(f"- **{titel}**: {wert}\n")
                datei.write("\n" + "-" * 50 + "\n\n")

    for reihe in ergebnisse:
        problem = reihe[header.index("Problem")]
        print(f"Kundenbeanstandung: {problem}")
        for titel, wert in zip(header, reihe):
            if titel == "Besonderheit":
                wert = formatiere_wert(wert, terminal=True)
            print(f"{titel}: {wert}")
        print("-" * 50)  # Trennlinie zwischen den Einträgen







def daten_exportieren(zeiger, dateiname):
    zeiger.execute("SELECT * FROM messungen")
    ergebnisse = zeiger.fetchall()
    with open(dateiname, 'w', newline='') as datei:
        csv_writer = csv.writer(datei, delimiter=';')
        csv_writer.writerows(ergebnisse)

def daten_importieren(verbindung, zeiger, dateiname):
    try:
        with open(dateiname, 'r') as datei:
            csv_reader = csv.reader(datei, delimiter=';')
            for index, reihe in enumerate(csv_reader, start=1):
                # Überprüfen, ob die Daten schädlichen Code enthalten
                if any(is_malicious(item) for item in reihe):
                    print(f"Potenziell schädlicher Eintrag in Zeile {index} gefunden. Überspringe diesen Eintrag.")
                    continue
                if len(reihe) != 8:
                    print(f"Fehler in Zeile {index}: {reihe} hat nicht die erwartete Anzahl an Werten.")
                    continue
                
                # Duplikat-Check, der auf Uebungsnummer, Fahrzeug und Problem basiert
                zeiger.execute("SELECT ID FROM messungen WHERE Uebungsnummer=? AND Fahrzeug=? AND Problem=?", (reihe[1], reihe[2], reihe[3]))
                existing_entry = zeiger.fetchone()
                
                if existing_entry:
                    # Aktualisieren des bestehenden Eintrags
                    zeiger.execute("""
                        UPDATE messungen SET
                            Uebungsnummer=?, Fahrzeug=?, Problem=?, Fehlerspeicher=?, Istwerte=?, Ursache=?, Besonderheit=?
                        WHERE ID=?
                    """, (reihe[1], reihe[2], reihe[3], reihe[4], reihe[5], reihe[6], reihe[7], existing_entry[0]))
                else:
                    # Einfügen eines neuen Eintrags
                    zeiger.execute("INSERT INTO messungen (Uebungsnummer, Fahrzeug, Problem, Fehlerspeicher, Istwerte, Ursache, Besonderheit) VALUES (?, ?, ?, ?, ?, ?, ?)", reihe[1:])
        
        verbindung.commit()
    except FileNotFoundError:
        print(f"Datei {dateiname} nicht gefunden!")
    except sqlite3.Error as e:
        print(f"Fehler beim Importieren der Daten: {e}")


def daten_suchen(zeiger, spaltenname, suchbegriff):
    erlaubte_spalten = [
        "ID", "Uebungsnummer", "Fahrzeug", "Istwerte", "Problem",
        "Fehlerspeicher", "Besonderheit", "Ursache"
    ]
    if spaltenname not in erlaubte_spalten:
        print("Ungültiger Spaltenname!")
        return

    sql_befehl = f"SELECT * FROM messungen WHERE {spaltenname} LIKE ?"
    zeiger.execute(sql_befehl, ('%' + suchbegriff + '%',))
    ergebnisse = zeiger.fetchall()
    
    if ergebnisse:
        print(f"\nSuchergebnisse für '{suchbegriff}' in Spalte '{spaltenname}':\n")
        formatierte_ausgabe(ergebnisse, in_datei_speichern=True, suchbegriff=suchbegriff, spaltenname=spaltenname)
    else:
        print(f"Keine Ergebnisse gefunden für '{suchbegriff}' in Spalte '{spaltenname}'.")


def duplikate_entfernen(verbindung, tabelle_name='messungen'):
    try:
        zeiger = verbindung.cursor()
        zeiger.execute(f"""
        DELETE FROM {tabelle_name}
        WHERE rowid NOT IN (
            SELECT MIN(rowid)
            FROM {tabelle_name}
            GROUP BY Uebungsnummer, Fahrzeug, Istwerte, Problem, Fehlerspeicher, Besonderheit, Ursache
        )
        """)
        verbindung.commit()
        print("Duplikate erfolgreich entfernt!")
    except sqlite3.Error as e:
        print(f"Fehler beim Entfernen von Duplikaten: {e}")


def daten_loeschen(verbindung, zeiger):
    try:
        id_nummer = input("Bitte geben Sie die ID des Eintrags ein, den Sie löschen möchten: ")
        zeiger.execute("DELETE FROM messungen WHERE ID=?", (id_nummer,))
        verbindung.commit()
        if zeiger.rowcount == 0:
            print(f"Eintrag mit ID {id_nummer} nicht gefunden!")
        else:
            print(f"Eintrag mit ID {id_nummer} wurde erfolgreich gelöscht!")
    except ValueError:
        print("Ungültige ID-Nummer!")
    except sqlite3.Error as e:
        print(f"Fehler beim Löschen des Eintrags: {e}")

def daten_hinzufuegen(verbindung, zeiger):
    try:
        uebungsnummer = input("Bitte Uebungsnummer eingeben: ")
        fahrzeug = input("Bitte Fahrzeug eingeben: ")
        istwerte = input("Bitte Istwerte eingeben: ")
        problem = input("Bitte Problem eingeben: ")
        fehlerspeicher = input("Bitte Fehlerspeicher eingeben: ")
        besonderheit = input("Bitte Besonderheit eingeben: ")
        ursache = input("Bitte Ursache eingeben: ")

        zeiger.execute("""
            INSERT INTO messungen (
                Uebungsnummer, Fahrzeug, Problem, Fehlerspeicher,
                Istwerte, Ursache, Besonderheit
            )
            VALUES (?, ?, ?, ?, ?, ?, ?)
        """, (uebungsnummer, fahrzeug, problem, fehlerspeicher, istwerte, ursache, besonderheit))

        verbindung.commit()
        print("Daten erfolgreich hinzugefügt!")
    except sqlite3.Error as e:
        print(f"Fehler beim Hinzufügen der Daten: {e}")


def extract_data(text, pattern):
    match = re.search(pattern, text)
    return match.group(1).strip() if match else ''

def daten_aus_textdatei_importieren(verbindung, zeiger, dateipfad):
    """Final method to import data from the structured text file into the database."""
    # Define the keywords we're looking for
    keywords = [
        "Uebungsnummer", "Fahrzeug", "Problem", "Fehlerspeicher",
        "Istwerte", "Ursache", "Besonderheit"
    ]
    
    data = []
    current_data = {}
    
    # Read the file line by line
    with open(dateipfad, 'r', encoding='utf-8') as file:
        for line in file:
            line = line.strip()
            
            # Check each keyword
            for keyword in keywords:
                if f"**{keyword}**" in line:
                    # Extract the value
                    value = line.split(f"**{keyword}**")[1].strip()
                    current_data[keyword] = value
                    break
            
            # Check if we have a complete set of data
            if len(current_data) == len(keywords):
                data.append(current_data)
                current_data = {}
    
        # Insert or update data in the database
        for eintrag in data:
            # Überprüfen, ob ein Eintrag mit derselben Uebungsnummer und Fahrzeug bereits existiert
            zeiger.execute("SELECT ID FROM messungen WHERE Uebungsnummer=? AND Fahrzeug=?", (eintrag["Uebungsnummer"], eintrag["Fahrzeug"]))
            existing_entry = zeiger.fetchone()
            
            if existing_entry:
                # Aktualisieren des bestehenden Eintrags
                zeiger.execute("""
                    UPDATE messungen SET
                        Problem=?, Fehlerspeicher=?, Istwerte=?, Ursache=?, Besonderheit=?
                    WHERE ID=?
                """, (eintrag["Problem"], eintrag["Fehlerspeicher"], eintrag["Istwerte"], eintrag["Ursache"], eintrag["Besonderheit"], existing_entry[0]))
            else:
                # Einfügen eines neuen Eintrags
                zeiger.execute(
                    "INSERT INTO messungen (Uebungsnummer, Fahrzeug, Problem, Fehlerspeicher, Istwerte, Ursache, Besonderheit) VALUES (?, ?, ?, ?, ?, ?, ?)",
                    (eintrag["Uebungsnummer"], eintrag["Fahrzeug"], eintrag["Problem"], eintrag["Fehlerspeicher"], eintrag["Istwerte"], eintrag["Ursache"], eintrag["Besonderheit"])
                )
                
        verbindung.commit()
        print("Daten erfolgreich in die Datenbank eingefügt!")


def daten_in_csv_exportieren():
    """Daten aus der Datenbank in eine CSV-Datei exportieren."""
    
    # Verbindung zur Datenbank herstellen
    verbindung = sqlite3.connect(db_path)
    zeiger = verbindung.cursor()

    # Alle Einträge aus der Tabelle "messungen" abrufen
    zeiger.execute("SELECT * FROM messungen")
    eintraege = zeiger.fetchall()

    # Überschriften für die CSV-Datei definieren
    ueberschriften = [
        "ID", "Uebungsnummer", "Fahrzeug", "Problem",
        "Fehlerspeicher", "Istwerte", "Ursache", "Besonderheit"
    ]

    # Daten in die CSV-Datei schreiben
    csv_pfad = "/mnt/data/sicherung.csv"
    with open(csv_pfad, 'w', encoding='utf-8', newline='') as datei:
        schreiber = csv.writer(datei)
        schreiber.writerow(ueberschriften)
        schreiber.writerows(eintraege)

    # Verbindung zur Datenbank schließen
    verbindung.close()
    
def is_malicious(data):
    """Einfache Überprüfung auf schädlichen Code in den Daten."""
    for keyword in DANGEROUS_KEYWORDS:
        if keyword in data.upper():
            return True
    return False

def main():
    verbindung, zeiger = verbindung_herstellen('messen.db')
    tabelle_erstellen(zeiger)  # Stellen Sie sicher, dass die Tabelle existiert
    if not zeiger:
        return

    while True:  # Eine Schleife um das Hauptmenü
        print("Willkommen zum Datenbank-Tool!")
        print("Mögliche Aktionen:")
        print("1. Daten anzeigen")
        print("2. Daten exportieren")
        print("3. Daten importieren")
        print("4. Daten suchen")
        print("5. Duplikate entfernen")
        print("6. Daten löschen")
        print("7. Daten hinzufügen")
        print("8. Daten aus Textdatei importieren")
        print("9. Beenden")
        print("#" * 50)  # Trennlinie
        aktion = input("Bitte Aktion durch Nummer auswählen: ")

        if aktion == "1":
            daten_anzeigen(zeiger)
        elif aktion == "2":
            daten_exportieren(zeiger, EXPORT_DATEINAME)
        elif aktion == "3":
            daten_importieren(verbindung, zeiger, IMPORT_DATEINAME)
        elif aktion == "4":
            spaltenname = input("Bitte Spaltennamen eingeben, in dem gesucht werden soll: ")
            suchbegriff = input("Bitte Suchbegriff eingeben: ")
            daten_suchen(zeiger, spaltenname, suchbegriff)
        elif aktion == "5":
            duplikate_entfernen(verbindung)
        elif aktion == "6":
            daten_loeschen(verbindung, zeiger)
        elif aktion == "7":
            daten_hinzufuegen(verbindung, zeiger)
        elif aktion == "8":
            daten_aus_textdatei_importieren(verbindung, zeiger, TEXTDATEI_PFAD)
        elif aktion == "9":
            print("Auf Wiedersehen!")
            break  # Beendet die Schleife und somit das Programm
        else:
            print("Ungültige Auswahl!")
        
        print("#" * 50)  # Trennlinie

    verbindung.close()

if __name__ == '__main__':
    main()


