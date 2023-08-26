# Datenbank-Tool

Dieses Skript ermöglicht die Verwaltung und Manipulation einer SQLite-Datenbank, die speziell für Fahrzeugmessungen entwickelt wurde. Sie können Daten anzeigen, exportieren, importieren, suchen, Duplikate entfernen, Daten löschen, hinzufügen und sogar Daten aus einer strukturierten Textdatei importieren. Datei: messen_datenbank_tool.py

## Importierte Module:

- `sqlite3`: Ein Modul, um SQLite-Datenbankoperationen in Python durchzuführen.
- `csv`: Ein Modul, um CSV-Dateien zu lesen und zu schreiben.
- `re`: Ein Modul, um reguläre Ausdrücke in Python zu verwenden.

## Konfiguration

Einige Konfigurationsvariablen sind im Skript festgelegt:

- `DB_NAME`: Name der Datenbankdatei.
- `EXPORT_DATEINAME`: Name der Datei, in die Daten exportiert werden.
- `IMPORT_DATEINAME`: Name der Datei, aus der Daten importiert werden.
- `TEXTDATEI_PFAD`: Pfad zur strukturierten Textdatei.
- `MD_AUSGABE_DATEI`: Pfad zur Markdown-Ausgabedatei.
- `DANGEROUS_KEYWORDS`: Eine Liste von gefährlichen Schlüsselwörtern, die vermieden werden sollten, um SQL-Injection zu verhindern.

## Hauptfunktionen

- `verbindung_herstellen()`: Verbindung zur Datenbank herstellen.
- `tabelle_erstellen()`: Erstellen der Hauptdatenbanktabelle, falls sie nicht existiert.
- `daten_anzeigen()`: Zeigt alle Daten in der Datenbank an.
- `daten_exportieren()`: Exportiert Daten aus der Datenbank in eine CSV-Datei.
- `daten_importieren()`: Importiert Daten aus einer CSV-Datei in die Datenbank.
- `daten_suchen()`: Sucht nach einem bestimmten Begriff in einer angegebenen Spalte.
- `duplikate_entfernen()`: Entfernt Duplikate aus der Datenbank basierend auf mehreren Kriterien.
- `daten_loeschen()`: Löscht einen bestimmten Eintrag aus der Datenbank basierend auf seiner ID.
- `daten_hinzufuegen()`: Fügt manuell Daten zur Datenbank hinzu.
- `daten_aus_textdatei_importieren()`: Importiert Daten aus einer strukturierten Textdatei in die Datenbank.

## Benutzung

Um das Skript auszuführen, navigieren Sie zum Verzeichnis, in dem es sich befindet, und führen Sie es mit Python aus:

```
python3 messen_datenbank_tool.py
```

Folgen Sie dann den Anweisungen auf dem Bildschirm, um die gewünschte Aktion auszuwählen und durchzuführen.


## Zusammenfassung der hochgeladenen Dateien

1. **messen_datenbank_sicherung.csv**:
    - Dies ist eine CSV-Datei, die Daten zu Fahrzeugproblemen und deren Lösungen enthält.
    - Die Daten sind durch Semikolon (;) getrennt.
    - Enthält Details wie Fahrzeuginfo, Problem, Lösung und verwendete Werkzeuge.

2. **messen_daten_ausgabe.md**:
    - Dies ist eine Markdown-Datei, die eine formatierte Darstellung der Daten aus der CSV-Datei enthält.
    - Enthält Überschriften, Metadaten und formatierte Abschnitte für jeden Datensatz.

3. **messen_datenbank_tool.py**:
    - Ein Python-Skript, das Funktionen zur Interaktion mit einer SQLite-Datenbank bietet.
    - Bietet Funktionen zum Verbinden, Erstellen von Tabellen und anderen Datenbankoperationen.

4. **messuebung_eingabe.txt**:
    - Eine Textdatei im Markdown-Format, die eine Liste von Messübungen oder Diagnosen für verschiedene Fahrzeuge enthält.

5. **messen.db**:
    - Eine SQLite-Datenbank, die eine Tabelle namens `messungen` enthält.
    - Die Tabelle `messungen` enthält Daten, die den Einträgen in der CSV-Datei ähneln.





