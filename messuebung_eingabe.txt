---
title: "03-Messübung-Kundenbeanstandung-Ursache"
author: "ju"
date: \today
bibliography: literatur-kfz.bib
csl: zitierstil-number.csl
---
<!-------------------------------------------------------------------------------
ju 23-8-23 03-Messübung-Kundenbeanstandung

**Schulungsmotor:** VW Caddy 2,0 l (Dieselmotor), 2016, Motor-Nr.: DFSD
**Schulungsmotor:** BMW 344 E36, 1997, Motor-Nr.: 164E2
**Fahrzeug:** BMW Compact E46 (Dieselmotor), 2001, Motor-Nr.: 204D4
**Fahrzeug:** Golf 6 1,4 l (Benzinmotor), 2012, Motor-Nr.: CAXA
**Fahrzeug:** Opel, 2023, Motor-Nr.: XXX

Bemerkung: Komma-Trennzeichen , ist Aufzählungszeichen - für Markdown
Kopiere 03-Messübung-Kundenbeanstandung-Ursache.md nach messuebung_eingabe.txt
# Datenbank-Tool: messen_datenbank_tool.py
DB_NAME: messen.db
EXPORT_DATEINAME: messen_datenbank_sicherung.csv
IMPORT_DATEINAME: messen_datenbank_sicherung.csv
TEXTDATEI_PFAD: messuebung_eingabe.txt <= 03-Messübung-Kundenbeanstandung-Ursache.md
MD_AUSGABE_DATEI: messen_daten_ausgabe.md => Pra-Keywords-02-Messen-Kundenbeanstandung-Ursache.pdf
+-------------------------------------------------------------------------------->
# Messübung - Kundenbeanstandung - Ursache

## Ü01 Beleuchtung - Abblendlicht und Rückfahrlicht

Messen

1. **Uebungsnummer** Ü01
2. **Fahrzeug** BMW Compact E46 (Dieselmotor), 2001, Motor-Nr.: 204D4
3. **Problem** Licht vorne geht nicht, Abblendlicht VL n.i.O.
4. **Fehlerspeicher**
5. **Istwerte**
6. **Ursache** Unterbrechung auf Plusleitung von linken Abblendlicht E104 Pin 2 nach SG A192 Pin 7 
7. **Besonderheit** Multimeter

Messen

1. **Uebungsnummer** Ü01
2. **Fahrzeug** Golf 6 1,4 l (Benzinmotor), 2012, Motor-Nr.: CAXA
3. **Problem** Rückfahrlicht ohne Funktion, Rückfahrlicht links n.i.O.
4. **Fehlerspeicher**
5. **Istwerte**
6. **Ursache** Unterbrechung auf Plusleitung von linken Rückfahrlicht M16 Pin 3 nach SG J519 Pin 28 
7. **Besonderheit** Multimeter, Rechtslenker im Stromlaufplan beachten, Rückwärtsgang ein/aus

## Ü02 Beleuchtung - Schlusslicht und Standlicht

Messen

1. **Uebungsnummer** Ü02
2. **Fahrzeug** Golf 6 1,4 l (Benzinmotor), 2012, Motor-Nr.: CAXA
3. **Problem** Beleuchtung hinten defekt, Schlusslicht re. leuchtet schwach, n.i.O.
4. **Fehlerspeicher**
5. **Istwerte**
6. **Ursache** Übergangswiderstand auf Plusleitung von rechten Schlusslicht M22 Pin 1 nach SG J519 Pin 26. Spannungsverlust von $1,15~V$.
7. **Besonderheit** Oszi, Multimeter, Brems- und Schlusslicht ist eine Einfaden-Glühlampe, PWM-Signal $\to$ Oszi messen

Messen

1. **Uebungsnummer** Ü02
2. **Fahrzeug** BMW Compact E46 (Dieselmotor), 2001, Motor-Nr.: 204D4
3. **Problem** Beleuchtung vorne geht nicht, Standlicht links n.i.O.
4. **Fehlerspeicher**
5. **Istwerte**
6. **Ursache** Unterbrechung auf Zuleitung von linken Standlicht E5 Pin 2 nach SG A192 Pin 45
7. **Besonderheit** Multimeter, Ersatzwert von SG (Blinklicht VL an normal) wenn Standlicht def., Bauteilprüfung oder Quertausch

## Ü03 NTC - Kühlmitteltemperaturgeber

Messen

1. **Uebungsnummer** Ü03
2. **Fahrzeug** VW Caddy 2,0 l (Dieselmotor), 2016, Motor-Nr.: DFSD
3. **Problem** Kraftstoffverbrauch zu hoch
4. **Fehlerspeicher** i.O.
5. **Istwerte** Kühlmitteltemperatur $5^\circ\text{C}$
6. **Ursache** Übergangswiderstand auf Signalleitung von Kühlmitteltemperaturgeber G62 Pin 1 nach SG J623 Pin 38. Spannungsverlust von $2,8~V$.
7. **Besonderheit** Multimeter, NTC Kühlmitteltemperaturgeber, ($U_K$ SG) Istwert = Sollwert ($U_K$ Sensor), Referenzspannung am SG messen Strecker trennen

## Ü04 NTC - Ansauglufttemperatursensor

Messen

1. **Uebungsnummer** Ü04
2. **Fahrzeug** BMW Compact E46 (Dieselmotor), 2001, Motor-Nr.: 204D4
3. **Problem** Kraftstoffverbrauch zu hoch
4. **Fehlerspeicher** i.O.
5. **Istwerte** Ansauglufttemperatur $-40^\circ\text{C}$
6. **Ursache** Unterbrechung auf Signalleitung von Ansauglufttemperatursensor B6217 Pin 1 nach SG A2249 Pin 57. Referenzspannung ist mit Messung 1 als i.O. zu bewerten.
7. **Besonderheit** Multimeter, NTC - Ansauglufttemperatursensor, ($U_K$ SG) Istwert = Sollwert ($U_K$ Sensor)

Messen

1. **Uebungsnummer** Ü04
2. **Fahrzeug** BMW 344 E36, 1997, Motor-Nr.: 164E2
3. **Problem** Kraftstoffverbrauch zu hoch
4. **Fehlerspeicher** i.O.
5. **Istwerte** Ansauglufttemperatur $1^\circ\text{C}$
6. **Ursache** Übergangswiderstand auf Signalleitung von Ansauglufttemperatursensor B6233 Pin 4 nach SG A6000 Pin 77. Spannungsverlust von $1,9~V$.
7. **Besonderheit** Multimeter, NTC Ansauglufttemperatursensor, ($U_K$ SG) Istwert = Sollwert ($U_K$ Sensor)

## Ü05 Poti - Fahrpedalsensor

Messen

1. **Uebungsnummer** Ü05
2. **Fahrzeug** VW Caddy 2,0 l (Dieselmotor), 2016, Motor-Nr.: DFSD
3. **Problem** Nimmt schlecht Gas an
4. **Fehlerspeicher** n.i.O.
5. **Istwerte** Fahrpedalsensor1 0,0 mV, Fahrpedalsensor2 i.O.
6. **Ursache** Unterbrechung auf Signalleitung von Fahrpedalsensor 1 G79 Pin 4 nach SG J623 Pin 77
7. **Besonderheit** Oszi, Multimeter, Poti Fahrpedalsensor, Durchgangsprüfung und Masseschlussprüfung Signalleitung

## Ü06 Poti - Drosselklappenpositionssensor und Cipos - Fahrpedalsensor

Messen

1. **Uebungsnummer** Ü06
2. **Fahrzeug** BMW 344 E36, 1997, Motor-Nr.: 164E2
3. **Problem** Bockt beim Gas geben
4. **Fehlerspeicher** i.O.
5. **Istwerte** Drosselklappenpositionssensor 2,08 bis 2,98 V
6. **Ursache** Übergangswiderstand auf Plusleitung von Drosselklappenpositionssensor R6252 Pin 1 nach SG A6000 Pin 59. Übergangswiderstand Masseleitung von Drosselklappenpositionssensor R6252 Pin 3 nach Masse-Verteiler X8005 Pin 5. Spannungsverlust gesamt $4~V$.
7. **Besonderheit** Oszi, Multimeter, Poti Drosselklappenpositionssensor

Messen

1. **Uebungsnummer** Ü06
2. **Fahrzeug** Golf 6 1,4 l (Benzinmotor), 2012, Motor-Nr.: CAXA
3. **Problem** Schlechte Gasannahme
4. **Fehlerspeicher** Fahrpedalsensor 1 und 2 - Signal zu niedrig
5. **Istwerte** Sensor D 0 \% 
6. **Ursache** Übergangswiderstand auf Plusleitung von Gaspedalstellungsgeber G79 Pin 2 nach SG J623. Spannungsverlust von $2,4~V$.
7. **Besonderheit** Oszi, Cipos Fahrpedalsensor, Cipos (Hella berührungslos arbeitet nur wenn volle Versorgungsspannung anliegt)


## Ü07 Hallgeber - Nockenwellensensor

Messen

1. **Uebungsnummer** Ü07
2. **Fahrzeug** VW Caddy 2,0 l (Dieselmotor), 2016, Motor-Nr.: DFSD
3. **Problem** Motor springt verzögert an
4. **Fehlerspeicher** Nockenwellensensor
5. **Istwerte** Nockenwellendrehzahl $0~min^{-1}$
6. **Ursache** Unterbrechung auf Signalleitung von Nockenwellengeber G40 Pin 2 nach SG J623 Pin 59.
7. **Besonderheit** Oszi, Hallgeber Nockenwellensensor, Gutbild Hallgeber Sollwert: Rechtecksignal ($+5/12~V$), PWM + Diodenprüflampe || bei Signalleitungsbruch, Referenz auf Oszi-Signalbild (Sollwert)

Messen

1. **Uebungsnummer** Ü07
2. **Fahrzeug** BMW Compact E46 (Dieselmotor), 2001, Motor-Nr.: 204D4
3. **Problem** Motor springt gar nicht an
4. **Fehlerspeicher** Nockenwellensensor
5. **Istwerte** Nockenwellendrehzahl $0~min^{-1}$
6. **Ursache** Unterbrechung auf Signalleitung von Nockenwellengeber B6219 Pin 2 nach SG A2249 Pin 62. Plusschlussprüfung steuergeräteseitig nicht durchführbar, da Stecker nicht trennbar.
7. **Besonderheit** Oszi, Hallgeber Nockenwellensensor, Gutbild Hallgeber Sollwert: Rechtecksignal ($+5/12~V$)

## Ü08 Hallgeber - Nockenwellensensor und PTC - Abgastemperaturgeber

Messen

1. **Uebungsnummer** Ü08
2. **Fahrzeug** VW Caddy 2,0 l (Dieselmotor), 2016, Motor-Nr.: DFSD
3. **Problem** Springt verzögert an und Lüfter läuft die ganze Zeit
4. **Fehlerspeicher** Abgastemperaturgeber 3 - Kurzschluss nach Masse
5. **Istwerte** Abgastemperaturgeber 3 $900^\circ\text{C}$
6. **Ursache** Masseschluss auf Signalleitung von SG J623 Stecker T94 Pin 32 nach Abgastemperaturgeber G495.
7. **Besonderheit** Multimeter, PTC Abgastemperaturgeber, Am Ziel anfangen mit messen, Bosch-Info / Handbücher / Fahrzeug Widerstandswerte

Messen

1. **Uebungsnummer** Ü08
2. **Fahrzeug** Golf 6 1,4 l (Benzinmotor), 2012, Motor-Nr.: CAXA
3. **Problem** Springt extrem schlecht an
4. **Fehlerspeicher** Nockenwellensensor A - Signal zu hoch
5. **Istwerte**
6. **Ursache** Übergangswiderstand auf Masseleitung von SG J623 Stecker T60 Pin 54 nach Nockenwellensensor G40 Stecker T3d Pin 3. Spannungsverlust von $2,9~V$
7. **Besonderheit** Oszi, Multimeter, Hallgeber Nockenwellensensor, Referenzspannung ($\text{U}_\text{Ref}$) am SG messen bei Übergangswiderstand ($\text{R}_\text{ü}$). (Stecker trennen)

## Ü09 Potentiometer - Drosselklappenpoti und Hallgeber - Nockenwellensensor und NTC - Kühlmitteltemperatursensor

Messen

1. **Uebungsnummer** Ü09
2. **Fahrzeug** Golf 6 1,4 l (Benzinmotor), 2012, Motor-Nr.: CAXA
3. **Problem** Nimmt kein Gas an
4. **Fehlerspeicher** Drosselklappenpoti - Signal zu hoch, Drosselklappenpoti 2 - Signal zu hoch
5. **Istwerte** Drosselklappenpoti 98 \%, Drosselklappenpoti 2 98 \%
6. **Ursache** Unterbrechung auf Masseleitung von SG J623 Stecker T60 Pin 44 nach Drosselklappensteuereinheit Stecker T6x Pin 6
7. **Besonderheit** Multimeter, Poti Drosselklappenpoti

Messen

1. **Uebungsnummer** Ü09
2. **Fahrzeug** BMW Compact E46 (Dieselmotor), 2001, Motor-Nr.: 204D4
3. **Problem** Motor springt nicht an
4. **Fehlerspeicher** Nockenwellensensor - Signal fehlerhaft
5. **Istwerte**
6. **Ursache** Leitungsunterbrechung Plusversorgung von Sicherung F1 A8682 Stecker X8582 nach Nockenwellensensor B6219 Stecker X6219 Pin 1
7. **Besonderheit**  Oszi, Multimeter, Hallgeber Nockenwellensensor, PWM

Messen

1. **Uebungsnummer** Ü09
2. **Fahrzeug** VW Caddy 2,0 l (Dieselmotor), 2016, Motor-Nr.: DFSD
3. **Problem** MIL an, hoher Kraftstoffverbrauch
4. **Fehlerspeicher** Kühlmitteltemperatursensor - Signal zu hoch
5. **Istwerte** Kühlmitteltemperatursensor $108^\circ\text{C}$
6. **Ursache** Unterbrechung auf Signalleitung von Kühlmitteltemperatursensor G62 Pin 1 nach J623 Stecker T60 Pin 38
7. **Besonderheit** Oszi, Multimeter, NTC Kühlmitteltemperatursensor

## Ü10 Luftmassenmesser - Ansauglufttemperatur - Ladedrucksensor

Messen

1. **Uebungsnummer** Ü10
2. **Fahrzeug** BMW Compact E46 (Dieselmotor), 2001, Motor-Nr.: 204D4
3. **Problem** keine Leistung 
4. **Fehlerspeicher** LMM Bank 2 Funktion fehlerhaft
5. **Istwerte** Ansaugluft: i.O., Luftmasse: n.i.O.
6. **Ursache** Unterbrechung auf Signalleitung von HFM5 B6217 Pin 5 nach SG A2249 Pin 55.
7. **Besonderheit** Oszi, Multimeter, Heißfilm-Luftmassenmesser HFM5 analog + Ansauglufttemperatur, Bosch / Handbücher / Funktionsgruppen - Prüfung / Sollwerte + Pin-Belegung für Schaltplan, LMM Signal $1 - 5~V$ und Bauteilprüfung Nullluftmessung $1~V$

Messen

1. **Uebungsnummer** Ü10
2. **Fahrzeug** VW Caddy 2,0 l (Dieselmotor), 2016, Motor-Nr.: DFSD
3. **Problem** Keine Leistung 
4. **Fehlerspeicher** LMM Signal unplausibel
5. **Istwerte** Ansauglufttemperatur: nicht verfügbar
6. **Ursache** Unterbrechung auf Signalleitung von SG J623 Pin 22 nach Ansauglufttemperatur G70 Pin 23
7. **Besonderheit** Oszi, Multimeter, Ansauglufttemperatur, Heißfilm-Luftmassenmesser HFM6 Signal digital (prüfbar wie Hallgeber), Nullluftmessung HFM6 Signal digital (Soll: $1,76 - 1,93~\text{kHz}$), Bosch / Handbücher / Funktionsgruppen - Prüfung / Sollwerte + Pin-Belegung für Schaltplan, PWM + Diodenprüflampe || bei Signal Leitungsbruch

Messen

1. **Uebungsnummer** Ü10
2. **Fahrzeug** Golf 6 1,4 l (Benzinmotor), 2012, Motor-Nr.: CAXA
3. **Problem** Ruckeln beim Beschleunigen
4. **Fehlerspeicher** Ladedrucksensor - Signal zu hoch
5. **Istwerte** Ladedruck: verändert sich nicht
6. **Ursache** Unterbrechung auf Signalleitung von Ladedrucksensor G31 Pin 4 nach SG J623 Pin 39.
7. **Besonderheit** Oszi, Multimeter, Ladedrucksensor, hat kein LMM verbaut, Sonderfall Ladedrucksensor: Leitungsunterbrechung $\to$ bei einer Spannungsfallmessung auf Signalleitung (Istwert: $U_\text{v} = 3,8~V$) ist kein Spannungsfall, Gegentest: Durchgangsprüfung Signalleitung (Sollwert: $< 1 \Omega$)

## Ü11 Luftmengenmesser

Messen

1. **Uebungsnummer** Ü11
2. **Fahrzeug** BMW 344 E36, 1997, Motor-Nr.: 164E2
3. **Problem** Keine Gasannahme
4. **Fehlerspeicher** Luftmengenmesser - Signal zu hoch
5. **Istwerte** Luftmengenmesser: $5~V$, Ansauglufttemperatur: $0^\circ\text{C}$
6. **Ursache** Unterbrechung auf Signalleitung von SG A6000 Pin 41 nach Luftmengenmesser B6233 Pin 2. Übergangswiderstand auf Signalleitung von SG A6000 Pin 77 und Ansauglufttemperatur B6233 Pin 4.
7. **Besonderheit** Oszi, Multimeter, Luftmengenmesser + Ansauglufttemperatur, Gutmann: Fahrzeuginformation / Bauteilprüfwerte, Luftmengenmesser $\to$ Oszi messen (Stauscheibe bewegen)

## Ü12 Ladedruckregelventil Turbo (Aktor)

Messen

1. **Uebungsnummer** Ü12
2. **Fahrzeug** VW Caddy 2,0 l (Dieselmotor), 2016, Motor-Nr.: DFSD
3. **Problem** Schlechte Leistung 
4. **Fehlerspeicher** Ladedruckregelventil Turbo 1 Unterbrechung
5. **Istwerte**
6. **Ursache** Unterbrechung auf Steuerleitung von SG J623 Stecker T60 Pin 52 nach Ladedruckregelventil N75 Pin 2.
7. **Besonderheit** Stellgliedtest: N75 Abgasturbolader: n.i.O., Multimeter, Ladedruckregelventil, Druckwandler - VTG-Lader $\to$ Leitschaufeln, Bosch / Suche Beanstandung: "schlechte Leistung" / Aktor-Auswahl / Prüfablauf, keine Sollwerte: "nach Angabe", Gutmann-Tester: Aktor nicht ansteuerbar über Stellgliedtest (Dioden-Prüflampe parallel), Standmotor - Bedienteil Zündung Ein + Fahrgeschwindigkeit 0 km/h stellen

## Ü13 Ladedruckregelventil und Raildruckregelventil (Aktor)

Messen

1. **Uebungsnummer** Ü13
2. **Fahrzeug** Golf 6 1,4 l (Benzinmotor), 2012, Motor-Nr.: CAXA
3. **Problem** Schlechte Leistung 
4. **Fehlerspeicher** Ladedruckregelventil A Funktion fehlerhaft
5. **Istwerte**
6. **Ursache** Unterbrechung Steuerleitung von SG J623 Stecker T60 Pin 3 nach Ladedruckregelventil N75 Pin 2.
7. **Besonderheit** Stellgliedtest: N75 Abgasturbolader: n.i.O., Multimeter, Ladedruckregelventil, Diodenprüflampe ||

Messen

1. **Uebungsnummer** Ü13
2. **Fahrzeug** BMW Compact E46 (Dieselmotor), 2001, Motor-Nr.: 204D4
3. **Problem** Springt nicht an
4. **Fehlerspeicher** Raildruckregelventil (DRV) Funktion fehlerhaft
5. **Istwerte** Raildrucksensor 0 bar
6. **Ursache** Unterbrechung auf Versorgungsleitung von Raildruckregelventil B2262 Stecker X2262 Pin 1 nach Sicherung F1 (A8682) Stecker 2051
7. **Besonderheit** Stellgliedtest: vom Tester nicht möglich $\to$ Signal am SG mit Oszi messen, Oszi, Multimeter, Raildruckregelventil

## Ü14 Lambdasonde und Drosselklappensteuereinheit (Sensor + Aktor)

Messen

1. **Uebungsnummer** Ü14
2. **Fahrzeug** VW Caddy 2,0 l (Dieselmotor), 2016, Motor-Nr.: DFSD
3. **Problem** MIL an
4. **Fehlerspeicher** Drosselklappensensor - Kurzschluss nach Plus
5. **Istwerte** Drosselklappenpositionssensor: 100\%
6. **Ursache** Unterbrechung auf Signalleitung von SG J623 Pin 11 nach Drosselklappenposition G69 Pin 2. Die Referenzspannung ist mit Messung 1 als i.O. zu bewerten.
7. **Besonderheit** Stellgliedtest: Drosselklappensteuereinheit ansteuern,  Oszi, Multimeter, Drosselklappensteuereinheit, Trick: Diodenprüflampe als Spannungsteiler ca. $2,7~V \to$ Signal muss plausibel für SG sein, SG Signal Soll: $0,5 - 4,5~V$, Zündung aus + Diodenprüflampe am SG anklemmen nach Masse + Zündung an + Stellgliedtest aktivieren (raus und wieder rein)

Messen

1. **Uebungsnummer** Ü14
2. **Fahrzeug** BMW E36, 1997, Motor Nr.: 164E2
3. **Problem** Läuft komisch, besteht die AU nicht, fängt an zu stottern beim Warmlaufen, Stecker ab von Lambdasonde
4. **Fehlerspeicher** Lambda-Regelung außerhalb Bereich, Relaissondenheizung Unterbrechung
5. **Istwerte** Lambdasonde 0,7 V, Lambdaintegrator 80\%
6. **Ursache** Unterbrechung auf Signalleitung von SG A6000 Pin 70 nach Lambdassonde Pin 2. Plusschluss auf Signalleitung steuergeräteseitig 
7. **Besonderheit** Oszi, Multimeter, Lambdasonde prüfen: kurze kräftige Gasstöße (Gashebel auf Null stellen vorher)

## Ü15 Raildruckregelventil (Aktor)

Messen

1. **Uebungsnummer** Ü15
2. **Fahrzeug** BMW Compact E46 (Dieselmotor), 2001, Motor-Nr.: 204D4
3. **Problem** Springt nicht an
4. **Fehlerspeicher** Raildrucküberwachung bei Start - Funktion fehlerhaft
5. **Istwerte** Raildrucksensor 70 bar n.i.O.
6. **Ursache** Übergangswiderstand auf Versorgungsleitung von Raildruckregelventil B2262 Stecker Pin 1 nach Sicherung F1 (A8682) Stecker 2051. Spannungsverlust von $12~V$
7. **Besonderheit** Stellgliedtest: vom Tester nicht möglich $\to$ Signal am SG mit Oszi messen, Oszi, Multimeter, Raildruckregelventil, Spannungsfall mit Oszi messen, weil PWM-Signal

## Ü16 Relais Lambdasondenheizung - Nockenwellensensor - Kurbelwellensensor und AGR

Messen

1. **Uebungsnummer** Ü16
2. **Fahrzeug** BMW 344 E36, 1997, Motor Nr.: 164E2
3. **Problem** Besteht die AU nicht
4. **Fehlerspeicher** Relais Sondenheizung Fehler
5. **Istwerte**
6. **Ursache** Unterbrechung der Steuerleitung von A6000 Pin 37 nach Lambdasonden-Relais Pin 4
7. **Besonderheit** Stellgliedtest: n.i.O., Oszi, Multimeter, Relais Sondenheizung, Lambdasonde prüfen - Kurze kräftige Gasstöße (Gashebel auf Null stellen vorher)

Messen

1. **Uebungsnummer** Ü16
2. **Fahrzeug** Golf 6 1,4 l (Benzinmotor), 2012, Motor-Nr.: CAXA
3. **Problem** Springt manchmal an
4. **Fehlerspeicher** Nockenwellensensor A - Signal zu hoch
5. **Istwerte**
6. **Ursache** Übergangswiderstand auf Masseleitung von SG J623 nach Nockenwellen-Sensor G40
7. **Besonderheit**  Oszi, Nockenwellensensor, Fehlermeldung Signal zu hoch - Achtung: Ursache Schwellwert (ca. $< 2,5~V$) im SG nicht erreicht, PWM

Messen

1. **Uebungsnummer** Ü16
2. **Fahrzeug** VW Caddy 2,0 l (Dieselmotor), 2016, Motor-Nr.: DFSD
3. **Problem** Springt an und geht wieder aus
4. **Fehlerspeicher** AGR - Kurzschluss nach Masse und Kurbelwellensensor - Signal fehlt
5. **Istwerte**
6. **Ursache** Übergangswiderstand auf Versorgungsleitung von SG J623 Stecker T60 PIN 58 nach den Komponenten G28, GX5, GX6, GX3. Plusschluss messen nicht durchführbar, da Stecker am Geber G28 nicht trennbar.
7. **Besonderheit** Oszi, Multimeter, Kurbelwellensensor und Abgasrückführung (AGR), PWM


## Ü17 Luftmassenmesser

Messen

1. **Uebungsnummer** Ü17
2. **Fahrzeug** BMW Compact E46 (Dieselmotor), 2001, Motor-Nr.: 204D4
3. **Problem** Leistungsprobleme, läuft schlecht
4. **Fehlerspeicher** LMM Bank2 - Funktion fehlerhaft und Ansauglufttemperatur Sensor - Signal fehlerhaft
5. **Istwerte** Luftmasse 1600 mg/Hub und Ansauglufttemperatur 19 °C 
6. **Ursache** Übergangswiderstand in Masseleitung zwischen Steuergerät A2249 Pin 79 und Luftmassenmesser B6217 Pin 3
7. **Besonderheit** Oszi, Multimeter, Luftmassenmesser, Pin-Belegung von LMM = HFM5 analog (Vgl. Oppermann oder Bosch), Achtung: Ein Übergangswiderstand in der Masseleitung hebt die Signalspannung an, (Signal Soll: $1 - 5~V$) und (Ist: $11,5~V$), Trick: Signal messen "mit Stecker" und "ohne Stecker" $\to$ prüfen ob sich Signalspannung ändert, Sichere Masse am Steuergerät oder Batterie minus, Nullluftmessung $1~V$


## Ü18 Einspritzventil

Messen

1. **Uebungsnummer** Ü18
2. **Fahrzeug** BMW 344 E36, 1997, Motor Nr.: 164E2
3. **Problem** Motor läuft nicht richtig, nur auf 3 Zylinder
4. **Fehlerspeicher** Einspritzventil Zylinder 2 Unterbrechung
5. **Istwerte**
6. **Ursache** Steuerleitungsunterbrechung zwischen Einspritzventil 2 und Steuergerät
7. **Besonderheit** Stellgliedtest: Einspritzventil 2 n.i.O., Einspritzventil, Achtung: Fehler im Schaltplan Leitung im Steuergerät vertauscht zwischen Einspritzventil 2 (= Pin 3 am SG)  und 3 (= Pin 31 am SG)


## Ü19 - Generatortest und Einspritzventil

Messen

1. **Uebungsnummer** Ü19
2. **Fahrzeug** Golf 6 1,4 l (Benzinmotor), 2012, Motor-Nr.: CAXA
3. **Problem** Batterie alle drei Tage entladen
4. **Fehlerspeicher** 
5. **Istwerte** Batterietest: 10,8 V i.O. und Ruhestrommessung: 40 mA i.O.
6. **Ursache** Übergangswiderstand in der Plusladeleitung zwischen Generator B+  und Batterie Kl. 30
7. **Besonderheit** Oszi, Sun VAT60 (Batteriebelastungstest), Generatortest Muster, Maßnahmen: Zündung an + Motor läuft + Generatordrehzahl 6000 U/min = Motordrehzahl 2000 U/min + Belastung: 120 A, Sichtprüfung: Batteriepole fest + Masseband + Ladekontrollleuchte usw., Achtung: Oberwelligkeit i.O. aber Regulierspannung ($< 13~V$) n.i.O. $\to$ dann Erregerstromkreis def.

Messen

1. **Uebungsnummer** Ü19
2. **Fahrzeug** BMW 344 E36, 1997, Motor Nr.: 164E2
3. **Problem** Mal läuft der Motor unrund
4. **Fehlerspeicher** Lambdaregelung - Wert/Signal außerhalb des Bereichs
5. **Istwerte**
6. **Ursache** Übergangswiderstand zwischen ein Einspritzventil 2 und Steuergerät
7. **Besonderheit** Bosch Universal-Oszilloskop, Einspritzventil

## Ü20 Hallgeber Nockenwellensensor und Cipos Fahrpedalsensor

Messen

1. **Uebungsnummer** Ü20
2. **Fahrzeug** BMW Compact E46 (Dieselmotor), 2001, Motor-Nr.: 204D4
3. **Problem** Springt nicht an
4. **Fehlerspeicher** Nockenwellensensor Signal fehlerhaft
5. **Istwerte** 
6. **Ursache** Signalleitungsunterbrechung zwischen Steuergerät A2249 Pin 62 und Hallgeber Nockenwellensensor B6219 Pin 2. Plusschluss kann nicht nachgewiesen werden, da Stecker vom Steuergerät nicht trennbar.
7. **Besonderheit** Diodenprüflampe Parallel zur Signalleitung vom Steuergerät zum Sensor, PWM-Signal ($+5~V$)

Messen

1. **Uebungsnummer** Ü20
2. **Fahrzeug** Golf 6 1,4 l (Benzinmotor), 2012, Motor-Nr.: CAXA
3. **Problem** Keine Gasannahme
4. **Fehlerspeicher** Fahrpedalsensor 1 + 2 Signal zu niedrig
5. **Istwerte** Fahrpedalsensor 1 + 2 $0,0%$
6. **Ursache** Übergangswiderstand auf Plusleitung zwischen G79 (Poti1) Pin 2 und Steuergerät J623 Pin 82. Spannungsabfall $2,4~V$. Signalleitungsbruch zwischen G185 (Poti2) Pin 6 und Steuergerät J623 Pin 61.
7. **Besonderheit** Cipos Fahrpedalsensor, Messadapter für Fahrpedal, Fahrpedal betätigen