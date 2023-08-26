# Datenbank-Tool
- DB_NAME: messen.db
- EXPORT_DATEINAME: messen_datenbank_sicherung.csv
- IMPORT_DATEINAME: messen_datenbank_sicherung.csv
- TEXTDATEI_PFAD: messuebung_eingabe.txt
- MD_AUSGABE_DATEI: messen_daten_ausgabe.md

## Messübung und Kundenbeanstandung
### Licht vorne geht nicht, Abblendlicht VL n.i.O.
- **ID**: 1
- **Uebungsnummer**: Ü01
- **Fahrzeug**: BMW Compact E46 (Dieselmotor), 2001, Motor-Nr.: 204D4
- **Problem**: Licht vorne geht nicht, Abblendlicht VL n.i.O.
- **Fehlerspeicher**: 
- **Istwerte**: 
- **Ursache**: Unterbrechung auf Plusleitung von linken Abblendlicht E104 Pin 2 nach SG A192 Pin 7
- **Besonderheit**: 
    - Multimeter

--------------------------------------------------

### Rückfahrlicht ohne Funktion, Rückfahrlicht links n.i.O.
- **ID**: 2
- **Uebungsnummer**: Ü01
- **Fahrzeug**: Golf 6 1,4 l (Benzinmotor), 2012, Motor-Nr.: CAXA
- **Problem**: Rückfahrlicht ohne Funktion, Rückfahrlicht links n.i.O.
- **Fehlerspeicher**: 
- **Istwerte**: 
- **Ursache**: Unterbrechung auf Plusleitung von linken Rückfahrlicht M16 Pin 3 nach SG J519 Pin 28
- **Besonderheit**: 
    - Multimeter
    - Rechtslenker im Stromlaufplan beachten
    - Rückwärtsgang ein/aus

--------------------------------------------------

### Beleuchtung hinten defekt, Schlusslicht re. leuchtet schwach, n.i.O.
- **ID**: 3
- **Uebungsnummer**: Ü02
- **Fahrzeug**: Golf 6 1,4 l (Benzinmotor), 2012, Motor-Nr.: CAXA
- **Problem**: Beleuchtung hinten defekt, Schlusslicht re. leuchtet schwach, n.i.O.
- **Fehlerspeicher**: 
- **Istwerte**: 
- **Ursache**: Übergangswiderstand auf Plusleitung von rechten Schlusslicht M22 Pin 1 nach SG J519 Pin 26. Spannungsverlust von $1,15~V$.
- **Besonderheit**: 
    - Oszi
    - Multimeter
    - Brems- und Schlusslicht ist eine Einfaden-Glühlampe
    - PWM-Signal $\to$ Oszi messen

--------------------------------------------------

### Beleuchtung vorne geht nicht, Standlicht links n.i.O.
- **ID**: 4
- **Uebungsnummer**: Ü02
- **Fahrzeug**: BMW Compact E46 (Dieselmotor), 2001, Motor-Nr.: 204D4
- **Problem**: Beleuchtung vorne geht nicht, Standlicht links n.i.O.
- **Fehlerspeicher**: 
- **Istwerte**: 
- **Ursache**: Unterbrechung auf Zuleitung von linken Standlicht E5 Pin 2 nach SG A192 Pin 45
- **Besonderheit**: 
    - Multimeter
    - Ersatzwert von SG (Blinklicht VL an normal) wenn Standlicht def.
    - Bauteilprüfung oder Quertausch

--------------------------------------------------

### Kraftstoffverbrauch zu hoch
- **ID**: 5
- **Uebungsnummer**: Ü03
- **Fahrzeug**: VW Caddy 2,0 l (Dieselmotor), 2016, Motor-Nr.: DFSD
- **Problem**: Kraftstoffverbrauch zu hoch
- **Fehlerspeicher**: i.O.
- **Istwerte**: Kühlmitteltemperatur $5^\circ\text{C}$
- **Ursache**: Übergangswiderstand auf Signalleitung von Kühlmitteltemperaturgeber G62 Pin 1 nach SG J623 Pin 38. Spannungsverlust von $2,8~V$.
- **Besonderheit**: 
    - Multimeter
    - NTC Kühlmitteltemperaturgeber
    - ($U_K$ SG) Istwert = Sollwert ($U_K$ Sensor)
    - Referenzspannung am SG messen Strecker trennen

--------------------------------------------------

### Kraftstoffverbrauch zu hoch
- **ID**: 6
- **Uebungsnummer**: Ü04
- **Fahrzeug**: BMW Compact E46 (Dieselmotor), 2001, Motor-Nr.: 204D4
- **Problem**: Kraftstoffverbrauch zu hoch
- **Fehlerspeicher**: i.O.
- **Istwerte**: Ansauglufttemperatur $-40^\circ\text{C}$
- **Ursache**: Unterbrechung auf Signalleitung von Ansauglufttemperatursensor B6217 Pin 1 nach SG A2249 Pin 57. Referenzspannung ist mit Messung 1 als i.O. zu bewerten.
- **Besonderheit**: 
    - Multimeter
    - NTC - Ansauglufttemperatursensor
    - ($U_K$ SG) Istwert = Sollwert ($U_K$ Sensor)

--------------------------------------------------

### Kraftstoffverbrauch zu hoch
- **ID**: 7
- **Uebungsnummer**: Ü04
- **Fahrzeug**: BMW 344 E36, 1997, Motor-Nr.: 164E2
- **Problem**: Kraftstoffverbrauch zu hoch
- **Fehlerspeicher**: i.O.
- **Istwerte**: Ansauglufttemperatur $1^\circ\text{C}$
- **Ursache**: Übergangswiderstand auf Signalleitung von Ansauglufttemperatursensor B6233 Pin 4 nach SG A6000 Pin 77. Spannungsverlust von $1,9~V$.
- **Besonderheit**: 
    - Multimeter
    - NTC Ansauglufttemperatursensor
    - ($U_K$ SG) Istwert = Sollwert ($U_K$ Sensor)

--------------------------------------------------

### Nimmt schlecht Gas an
- **ID**: 8
- **Uebungsnummer**: Ü05
- **Fahrzeug**: VW Caddy 2,0 l (Dieselmotor), 2016, Motor-Nr.: DFSD
- **Problem**: Nimmt schlecht Gas an
- **Fehlerspeicher**: n.i.O.
- **Istwerte**: Fahrpedalsensor1 0,0 mV, Fahrpedalsensor2 i.O.
- **Ursache**: Unterbrechung auf Signalleitung von Fahrpedalsensor 1 G79 Pin 4 nach SG J623 Pin 77
- **Besonderheit**: 
    - Oszi
    - Multimeter
    - Poti Fahrpedalsensor
    - Durchgangsprüfung und Masseschlussprüfung Signalleitung

--------------------------------------------------

### Bockt beim Gas geben
- **ID**: 9
- **Uebungsnummer**: Ü06
- **Fahrzeug**: BMW 344 E36, 1997, Motor-Nr.: 164E2
- **Problem**: Bockt beim Gas geben
- **Fehlerspeicher**: i.O.
- **Istwerte**: Drosselklappenpositionssensor 2,08 bis 2,98 V
- **Ursache**: Übergangswiderstand auf Plusleitung von Drosselklappenpositionssensor R6252 Pin 1 nach SG A6000 Pin 59. Übergangswiderstand Masseleitung von Drosselklappenpositionssensor R6252 Pin 3 nach Masse-Verteiler X8005 Pin 5. Spannungsverlust gesamt $4~V$.
- **Besonderheit**: 
    - Oszi
    - Multimeter
    - Poti Drosselklappenpositionssensor

--------------------------------------------------

### Schlechte Gasannahme
- **ID**: 10
- **Uebungsnummer**: Ü06
- **Fahrzeug**: Golf 6 1,4 l (Benzinmotor), 2012, Motor-Nr.: CAXA
- **Problem**: Schlechte Gasannahme
- **Fehlerspeicher**: Fahrpedalsensor 1 und 2 - Signal zu niedrig
- **Istwerte**: Sensor D 0 \%
- **Ursache**: Übergangswiderstand auf Plusleitung von Gaspedalstellungsgeber G79 Pin 2 nach SG J623. Spannungsverlust von $2,4~V$.
- **Besonderheit**: 
    - Oszi
    - Cipos Fahrpedalsensor
    - Cipos (Hella berührungslos arbeitet nur wenn volle Versorgungsspannung anliegt)

--------------------------------------------------

### Motor springt verzögert an
- **ID**: 11
- **Uebungsnummer**: Ü07
- **Fahrzeug**: VW Caddy 2,0 l (Dieselmotor), 2016, Motor-Nr.: DFSD
- **Problem**: Motor springt verzögert an
- **Fehlerspeicher**: Nockenwellensensor
- **Istwerte**: Nockenwellendrehzahl $0~min^{-1}$
- **Ursache**: Unterbrechung auf Signalleitung von Nockenwellengeber G40 Pin 2 nach SG J623 Pin 59.
- **Besonderheit**: 
    - Oszi
    - Hallgeber Nockenwellensensor
    - Gutbild Hallgeber Sollwert: Rechtecksignal ($+5/12~V$)
    - PWM + Diodenprüflampe || bei Signalleitungsbruch
    - Referenz auf Oszi-Signalbild (Sollwert)

--------------------------------------------------

### Motor springt gar nicht an
- **ID**: 12
- **Uebungsnummer**: Ü07
- **Fahrzeug**: BMW Compact E46 (Dieselmotor), 2001, Motor-Nr.: 204D4
- **Problem**: Motor springt gar nicht an
- **Fehlerspeicher**: Nockenwellensensor
- **Istwerte**: Nockenwellendrehzahl $0~min^{-1}$
- **Ursache**: Unterbrechung auf Signalleitung von Nockenwellengeber B6219 Pin 2 nach SG A2249 Pin 62. Plusschlussprüfung steuergeräteseitig nicht durchführbar, da Stecker nicht trennbar.
- **Besonderheit**: 
    - Oszi
    - Hallgeber Nockenwellensensor
    - Gutbild Hallgeber Sollwert: Rechtecksignal ($+5/12~V$)

--------------------------------------------------

### Springt verzögert an und Lüfter läuft die ganze Zeit
- **ID**: 13
- **Uebungsnummer**: Ü08
- **Fahrzeug**: VW Caddy 2,0 l (Dieselmotor), 2016, Motor-Nr.: DFSD
- **Problem**: Springt verzögert an und Lüfter läuft die ganze Zeit
- **Fehlerspeicher**: Abgastemperaturgeber 3 - Kurzschluss nach Masse
- **Istwerte**: Abgastemperaturgeber 3 $900^\circ\text{C}$
- **Ursache**: Masseschluss auf Signalleitung von SG J623 Stecker T94 Pin 32 nach Abgastemperaturgeber G495.
- **Besonderheit**: 
    - Multimeter
    - PTC Abgastemperaturgeber
    - Am Ziel anfangen mit messen
    - Bosch-Info / Handbücher / Fahrzeug Widerstandswerte

--------------------------------------------------

### Springt extrem schlecht an
- **ID**: 14
- **Uebungsnummer**: Ü08
- **Fahrzeug**: Golf 6 1,4 l (Benzinmotor), 2012, Motor-Nr.: CAXA
- **Problem**: Springt extrem schlecht an
- **Fehlerspeicher**: Nockenwellensensor A - Signal zu hoch
- **Istwerte**: 
- **Ursache**: Übergangswiderstand auf Masseleitung von SG J623 Stecker T60 Pin 54 nach Nockenwellensensor G40 Stecker T3d Pin 3. Spannungsverlust von $2,9~V$
- **Besonderheit**: 
    - Oszi
    - Multimeter
    - Hallgeber Nockenwellensensor
    - Referenzspannung ($\text{U}_\text{Ref}$) am SG messen bei Übergangswiderstand ($\text{R}_\text{ü}$). (Stecker trennen)

--------------------------------------------------

### Nimmt kein Gas an
- **ID**: 15
- **Uebungsnummer**: Ü09
- **Fahrzeug**: Golf 6 1,4 l (Benzinmotor), 2012, Motor-Nr.: CAXA
- **Problem**: Nimmt kein Gas an
- **Fehlerspeicher**: Drosselklappenpoti - Signal zu hoch, Drosselklappenpoti 2 - Signal zu hoch
- **Istwerte**: Drosselklappenpoti 98 \%, Drosselklappenpoti 2 98 \%
- **Ursache**: Unterbrechung auf Masseleitung von SG J623 Stecker T60 Pin 44 nach Drosselklappensteuereinheit Stecker T6x Pin 6
- **Besonderheit**: 
    - Multimeter
    - Poti Drosselklappenpoti

--------------------------------------------------

### Motor springt nicht an
- **ID**: 16
- **Uebungsnummer**: Ü09
- **Fahrzeug**: BMW Compact E46 (Dieselmotor), 2001, Motor-Nr.: 204D4
- **Problem**: Motor springt nicht an
- **Fehlerspeicher**: Nockenwellensensor - Signal fehlerhaft
- **Istwerte**: 
- **Ursache**: Leitungsunterbrechung Plusversorgung von Sicherung F1 A8682 Stecker X8582 nach Nockenwellensensor B6219 Stecker X6219 Pin 1
- **Besonderheit**: 
    - Oszi
    - Multimeter
    - Hallgeber Nockenwellensensor
    - PWM

--------------------------------------------------

### MIL an, hoher Kraftstoffverbrauch
- **ID**: 17
- **Uebungsnummer**: Ü09
- **Fahrzeug**: VW Caddy 2,0 l (Dieselmotor), 2016, Motor-Nr.: DFSD
- **Problem**: MIL an, hoher Kraftstoffverbrauch
- **Fehlerspeicher**: Kühlmitteltemperatursensor - Signal zu hoch
- **Istwerte**: Kühlmitteltemperatursensor $108^\circ\text{C}$
- **Ursache**: Unterbrechung auf Signalleitung von Kühlmitteltemperatursensor G62 Pin 1 nach J623 Stecker T60 Pin 38
- **Besonderheit**: 
    - Oszi
    - Multimeter
    - NTC Kühlmitteltemperatursensor

--------------------------------------------------

### keine Leistung
- **ID**: 18
- **Uebungsnummer**: Ü10
- **Fahrzeug**: BMW Compact E46 (Dieselmotor), 2001, Motor-Nr.: 204D4
- **Problem**: keine Leistung
- **Fehlerspeicher**: LMM Bank 2 Funktion fehlerhaft
- **Istwerte**: Ansaugluft: i.O., Luftmasse: n.i.O.
- **Ursache**: Unterbrechung auf Signalleitung von HFM5 B6217 Pin 5 nach SG A2249 Pin 55.
- **Besonderheit**: 
    - Oszi
    - Multimeter
    - Heißfilm-Luftmassenmesser HFM5 analog + Ansauglufttemperatur
    - Bosch / Handbücher / Funktionsgruppen - Prüfung / Sollwerte + Pin-Belegung für Schaltplan
    - LMM Signal $1 - 5~V$ und Bauteilprüfung Nullluftmessung $1~V$

--------------------------------------------------

### Keine Leistung
- **ID**: 19
- **Uebungsnummer**: Ü10
- **Fahrzeug**: VW Caddy 2,0 l (Dieselmotor), 2016, Motor-Nr.: DFSD
- **Problem**: Keine Leistung
- **Fehlerspeicher**: LMM Signal unplausibel
- **Istwerte**: Ansauglufttemperatur: nicht verfügbar
- **Ursache**: Unterbrechung auf Signalleitung von SG J623 Pin 22 nach Ansauglufttemperatur G70 Pin 23
- **Besonderheit**: 
    - Oszi
    - Multimeter
    - Ansauglufttemperatur
    - Heißfilm-Luftmassenmesser HFM6 Signal digital (prüfbar wie Hallgeber)
    - Nullluftmessung HFM6 Signal digital (Soll: $1,76 - 1,93~\text{kHz}$)
    - Bosch / Handbücher / Funktionsgruppen - Prüfung / Sollwerte + Pin-Belegung für Schaltplan
    - PWM + Diodenprüflampe || bei Signal Leitungsbruch

--------------------------------------------------

### Ruckeln beim Beschleunigen
- **ID**: 20
- **Uebungsnummer**: Ü10
- **Fahrzeug**: Golf 6 1,4 l (Benzinmotor), 2012, Motor-Nr.: CAXA
- **Problem**: Ruckeln beim Beschleunigen
- **Fehlerspeicher**: Ladedrucksensor - Signal zu hoch
- **Istwerte**: Ladedruck: verändert sich nicht
- **Ursache**: Unterbrechung auf Signalleitung von Ladedrucksensor G31 Pin 4 nach SG J623 Pin 39.
- **Besonderheit**: 
    - Oszi
    - Multimeter
    - Ladedrucksensor
    - hat kein LMM verbaut
    - Sonderfall Ladedrucksensor: Leitungsunterbrechung $\to$ bei einer Spannungsfallmessung auf Signalleitung (Istwert: $U_\text{v} = 3,8~V$) ist kein Spannungsfall
    - Gegentest: Durchgangsprüfung Signalleitung (Sollwert: $< 1 \Omega$)

--------------------------------------------------

### Keine Gasannahme
- **ID**: 21
- **Uebungsnummer**: Ü11
- **Fahrzeug**: BMW 344 E36, 1997, Motor-Nr.: 164E2
- **Problem**: Keine Gasannahme
- **Fehlerspeicher**: Luftmengenmesser - Signal zu hoch
- **Istwerte**: Luftmengenmesser: $5~V$, Ansauglufttemperatur: $0^\circ\text{C}$
- **Ursache**: Unterbrechung auf Signalleitung von SG A6000 Pin 41 nach Luftmengenmesser B6233 Pin 2. Übergangswiderstand auf Signalleitung von SG A6000 Pin 77 und Ansauglufttemperatur B6233 Pin 4.
- **Besonderheit**: 
    - Oszi
    - Multimeter
    - Luftmengenmesser + Ansauglufttemperatur
    - Gutmann: Fahrzeuginformation / Bauteilprüfwerte
    - Luftmengenmesser $\to$ Oszi messen (Stauscheibe bewegen)

--------------------------------------------------

### Schlechte Leistung
- **ID**: 22
- **Uebungsnummer**: Ü12
- **Fahrzeug**: VW Caddy 2,0 l (Dieselmotor), 2016, Motor-Nr.: DFSD
- **Problem**: Schlechte Leistung
- **Fehlerspeicher**: Ladedruckregelventil Turbo 1 Unterbrechung
- **Istwerte**: 
- **Ursache**: Unterbrechung auf Steuerleitung von SG J623 Stecker T60 Pin 52 nach Ladedruckregelventil N75 Pin 2.
- **Besonderheit**: 
    - Stellgliedtest: N75 Abgasturbolader: n.i.O.
    - Multimeter
    - Ladedruckregelventil
    - Druckwandler - VTG-Lader $\to$ Leitschaufeln
    - Bosch / Suche Beanstandung: "schlechte Leistung" / Aktor-Auswahl / Prüfablauf
    - keine Sollwerte: "nach Angabe"
    - Gutmann-Tester: Aktor nicht ansteuerbar über Stellgliedtest (Dioden-Prüflampe parallel)
    - Standmotor - Bedienteil Zündung Ein + Fahrgeschwindigkeit 0 km/h stellen

--------------------------------------------------

### Schlechte Leistung
- **ID**: 23
- **Uebungsnummer**: Ü13
- **Fahrzeug**: Golf 6 1,4 l (Benzinmotor), 2012, Motor-Nr.: CAXA
- **Problem**: Schlechte Leistung
- **Fehlerspeicher**: Ladedruckregelventil A Funktion fehlerhaft
- **Istwerte**: 
- **Ursache**: Unterbrechung Steuerleitung von SG J623 Stecker T60 Pin 3 nach Ladedruckregelventil N75 Pin 2.
- **Besonderheit**: 
    - Stellgliedtest: N75 Abgasturbolader: n.i.O.
    - Multimeter
    - Ladedruckregelventil
    - Diodenprüflampe ||

--------------------------------------------------

### Springt nicht an
- **ID**: 24
- **Uebungsnummer**: Ü13
- **Fahrzeug**: BMW Compact E46 (Dieselmotor), 2001, Motor-Nr.: 204D4
- **Problem**: Springt nicht an
- **Fehlerspeicher**: Raildruckregelventil (DRV) Funktion fehlerhaft
- **Istwerte**: Raildrucksensor 0 bar
- **Ursache**: Unterbrechung auf Versorgungsleitung von Raildruckregelventil B2262 Stecker X2262 Pin 1 nach Sicherung F1 (A8682) Stecker 2051
- **Besonderheit**: 
    - Stellgliedtest: vom Tester nicht möglich $\to$ Signal am SG mit Oszi messen
    - Oszi
    - Multimeter
    - Raildruckregelventil

--------------------------------------------------

### MIL an
- **ID**: 25
- **Uebungsnummer**: Ü14
- **Fahrzeug**: VW Caddy 2,0 l (Dieselmotor), 2016, Motor-Nr.: DFSD
- **Problem**: MIL an
- **Fehlerspeicher**: Drosselklappensensor - Kurzschluss nach Plus
- **Istwerte**: Drosselklappenpositionssensor: 100\%
- **Ursache**: Unterbrechung auf Signalleitung von SG J623 Pin 11 nach Drosselklappenposition G69 Pin 2. Die Referenzspannung ist mit Messung 1 als i.O. zu bewerten.
- **Besonderheit**: 
    - Stellgliedtest: Drosselklappensteuereinheit ansteuern
    - Oszi
    - Multimeter
    - Drosselklappensteuereinheit
    - Trick: Diodenprüflampe als Spannungsteiler ca. $2,7~V \to$ Signal muss plausibel für SG sein
    - SG Signal Soll: $0,5 - 4,5~V$
    - Zündung aus + Diodenprüflampe am SG anklemmen nach Masse + Zündung an + Stellgliedtest aktivieren (raus und wieder rein)

--------------------------------------------------

### Läuft komisch, besteht die AU nicht, fängt an zu stottern beim Warmlaufen, Stecker ab von Lambdasonde
- **ID**: 26
- **Uebungsnummer**: Ü14
- **Fahrzeug**: BMW E36, 1997, Motor Nr.: 164E2
- **Problem**: Läuft komisch, besteht die AU nicht, fängt an zu stottern beim Warmlaufen, Stecker ab von Lambdasonde
- **Fehlerspeicher**: Lambda-Regelung außerhalb Bereich, Relaissondenheizung Unterbrechung
- **Istwerte**: Lambdasonde 0,7 V, Lambdaintegrator 80\%
- **Ursache**: Unterbrechung auf Signalleitung von SG A6000 Pin 70 nach Lambdassonde Pin 2. Plusschluss auf Signalleitung steuergeräteseitig
- **Besonderheit**: 
    - Oszi
    - Multimeter
    - Lambdasonde prüfen: kurze kräftige Gasstöße (Gashebel auf Null stellen vorher)

--------------------------------------------------

### Springt nicht an
- **ID**: 27
- **Uebungsnummer**: Ü15
- **Fahrzeug**: BMW Compact E46 (Dieselmotor), 2001, Motor-Nr.: 204D4
- **Problem**: Springt nicht an
- **Fehlerspeicher**: Raildrucküberwachung bei Start - Funktion fehlerhaft
- **Istwerte**: Raildrucksensor 70 bar n.i.O.
- **Ursache**: Übergangswiderstand auf Versorgungsleitung von Raildruckregelventil B2262 Stecker Pin 1 nach Sicherung F1 (A8682) Stecker 2051. Spannungsverlust von $12~V$
- **Besonderheit**: 
    - Stellgliedtest: vom Tester nicht möglich $\to$ Signal am SG mit Oszi messen
    - Oszi
    - Multimeter
    - Raildruckregelventil
    - Spannungsfall mit Oszi messen
    - weil PWM-Signal

--------------------------------------------------

### Besteht die AU nicht
- **ID**: 28
- **Uebungsnummer**: Ü16
- **Fahrzeug**: BMW 344 E36, 1997, Motor Nr.: 164E2
- **Problem**: Besteht die AU nicht
- **Fehlerspeicher**: Relais Sondenheizung Fehler
- **Istwerte**: 
- **Ursache**: Unterbrechung der Steuerleitung von A6000 Pin 37 nach Lambdasonden-Relais Pin 4
- **Besonderheit**: 
    - Stellgliedtest: n.i.O.
    - Oszi
    - Multimeter
    - Relais Sondenheizung
    - Lambdasonde prüfen - Kurze kräftige Gasstöße (Gashebel auf Null stellen vorher)

--------------------------------------------------

### Springt manchmal an
- **ID**: 29
- **Uebungsnummer**: Ü16
- **Fahrzeug**: Golf 6 1,4 l (Benzinmotor), 2012, Motor-Nr.: CAXA
- **Problem**: Springt manchmal an
- **Fehlerspeicher**: Nockenwellensensor A - Signal zu hoch
- **Istwerte**: 
- **Ursache**: Übergangswiderstand auf Masseleitung von SG J623 nach Nockenwellen-Sensor G40
- **Besonderheit**: 
    - Oszi
    - Nockenwellensensor
    - Fehlermeldung Signal zu hoch - Achtung: Ursache Schwellwert (ca. $< 2,5~V$) im SG nicht erreicht
    - PWM

--------------------------------------------------

### Springt an und geht wieder aus
- **ID**: 30
- **Uebungsnummer**: Ü16
- **Fahrzeug**: VW Caddy 2,0 l (Dieselmotor), 2016, Motor-Nr.: DFSD
- **Problem**: Springt an und geht wieder aus
- **Fehlerspeicher**: AGR - Kurzschluss nach Masse und Kurbelwellensensor - Signal fehlt
- **Istwerte**: 
- **Ursache**: Übergangswiderstand auf Versorgungsleitung von SG J623 Stecker T60 PIN 58 nach den Komponenten G28, GX5, GX6, GX3. Plusschluss messen nicht durchführbar, da Stecker am Geber G28 nicht trennbar.
- **Besonderheit**: 
    - Oszi
    - Multimeter
    - Kurbelwellensensor und Abgasrückführung (AGR)
    - PWM

--------------------------------------------------

### Leistungsprobleme, läuft schlecht
- **ID**: 31
- **Uebungsnummer**: Ü17
- **Fahrzeug**: BMW Compact E46 (Dieselmotor), 2001, Motor-Nr.: 204D4
- **Problem**: Leistungsprobleme, läuft schlecht
- **Fehlerspeicher**: LMM Bank2 - Funktion fehlerhaft und Ansauglufttemperatur Sensor - Signal fehlerhaft
- **Istwerte**: Luftmasse 1600 mg/Hub und Ansauglufttemperatur 19 °C
- **Ursache**: Übergangswiderstand in Masseleitung zwischen Steuergerät A2249 Pin 79 und Luftmassenmesser B6217 Pin 3
- **Besonderheit**: 
    - Oszi
    - Multimeter
    - Luftmassenmesser
    - Pin-Belegung von LMM = HFM5 analog (Vgl. Oppermann oder Bosch)
    - Achtung: Ein Übergangswiderstand in der Masseleitung hebt die Signalspannung an
    - (Signal Soll: $1 - 5~V$) und (Ist: $11,5~V$)
    - Trick: Signal messen "mit Stecker" und "ohne Stecker" $\to$ prüfen ob sich Signalspannung ändert
    - Sichere Masse am Steuergerät oder Batterie minus
    - Nullluftmessung $1~V$

--------------------------------------------------

### Motor läuft nicht richtig, nur auf 3 Zylinder
- **ID**: 32
- **Uebungsnummer**: Ü18
- **Fahrzeug**: BMW 344 E36, 1997, Motor Nr.: 164E2
- **Problem**: Motor läuft nicht richtig, nur auf 3 Zylinder
- **Fehlerspeicher**: Einspritzventil Zylinder 2 Unterbrechung
- **Istwerte**: 
- **Ursache**: Steuerleitungsunterbrechung zwischen Einspritzventil 2 und Steuergerät
- **Besonderheit**: 
    - Stellgliedtest: Einspritzventil 2 n.i.O.
    - Einspritzventil
    - Achtung: Fehler im Schaltplan Leitung im Steuergerät vertauscht zwischen Einspritzventil 2 (= Pin 3 am SG)  und 3 (= Pin 31 am SG)

--------------------------------------------------

### Batterie alle drei Tage entladen
- **ID**: 33
- **Uebungsnummer**: Ü19
- **Fahrzeug**: Golf 6 1,4 l (Benzinmotor), 2012, Motor-Nr.: CAXA
- **Problem**: Batterie alle drei Tage entladen
- **Fehlerspeicher**: 
- **Istwerte**: Batterietest: 10,8 V i.O. und Ruhestrommessung: 40 mA i.O.
- **Ursache**: Übergangswiderstand in der Plusladeleitung zwischen Generator B+  und Batterie Kl. 30
- **Besonderheit**: 
    - Oszi
    - Sun VAT60 (Batteriebelastungstest)
    - Generatortest Muster
    - Maßnahmen: Zündung an + Motor läuft + Generatordrehzahl 6000 U/min = Motordrehzahl 2000 U/min + Belastung: 120 A
    - Sichtprüfung: Batteriepole fest + Masseband + Ladekontrollleuchte usw.
    - Achtung: Oberwelligkeit i.O. aber Regulierspannung ($< 13~V$) n.i.O. $\to$ dann Erregerstromkreis def.

--------------------------------------------------

### Mal läuft der Motor unrund
- **ID**: 34
- **Uebungsnummer**: Ü19
- **Fahrzeug**: BMW 344 E36, 1997, Motor Nr.: 164E2
- **Problem**: Mal läuft der Motor unrund
- **Fehlerspeicher**: Lambdaregelung - Wert/Signal außerhalb des Bereichs
- **Istwerte**: 
- **Ursache**: Übergangswiderstand zwischen ein Einspritzventil 2 und Steuergerät
- **Besonderheit**: 
    - Bosch Universal-Oszilloskop
    - Einspritzventil

--------------------------------------------------

### Springt nicht an
- **ID**: 35
- **Uebungsnummer**: Ü20
- **Fahrzeug**: BMW Compact E46 (Dieselmotor), 2001, Motor-Nr.: 204D4
- **Problem**: Springt nicht an
- **Fehlerspeicher**: Nockenwellensensor Signal fehlerhaft
- **Istwerte**: 
- **Ursache**: Signalleitungsunterbrechung zwischen Steuergerät A2249 Pin 62 und Hallgeber Nockenwellensensor B6219 Pin 2. Plusschluss kann nicht nachgewiesen werden, da Stecker vom Steuergerät nicht trennbar.
- **Besonderheit**: 
    - Diodenprüflampe Parallel zur Signalleitung vom Steuergerät zum Sensor
    - PWM-Signal ($+5~V$)

--------------------------------------------------

### Keine Gasannahme
- **ID**: 36
- **Uebungsnummer**: Ü20
- **Fahrzeug**: Golf 6 1,4 l (Benzinmotor), 2012, Motor-Nr.: CAXA
- **Problem**: Keine Gasannahme
- **Fehlerspeicher**: Fahrpedalsensor 1 + 2 Signal zu niedrig
- **Istwerte**: Fahrpedalsensor 1 + 2 $0,0%$
- **Ursache**: Übergangswiderstand auf Plusleitung zwischen G79 (Poti1) Pin 2 und Steuergerät J623 Pin 82. Spannungsabfall $2,4~V$. Signalleitungsbruch zwischen G185 (Poti2) Pin 6 und Steuergerät J623 Pin 61.
- **Besonderheit**: 
    - Cipos Fahrpedalsensor
    - Messadapter für Fahrpedal
    - Fahrpedal betätigen

--------------------------------------------------

