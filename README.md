# Trink-Erinnerung mit Python

Dieses Skript zeigt regelmäßig eine Benachrichtigung an, um dich ans Trinken zu erinnern. Es funktioniert auf Windows aber mit ein paar kleinen Änderungen auch auf Linux und macOS.

## Funktionen

- Zufällige motivierende Trink-Erinnerungen

- Unterstützung für Windows (win10toast) und Linux/macOS (plyer)

- Automatische Ausführung mit dem Windows Task Scheduler möglich

## Installation

### 1️. Python installieren

Falls du Python noch nicht installiert hast, lade es hier herunter: [Python Download](https://www.python.org/downloads/)

### 2️. Notwendige Abhängigkeiten installieren

Öffne eine Eingabeaufforderung (Windows) oder ein Terminal (Linux/macOS) und gib folgenden Befehl ein:

pip install plyer win10toast

## Nutzung

Speichere das Skript als drink_reminder.py und führe es mit folgendem Befehl aus:

python drink_reminder.py

## Automatische Ausführung

Falls du das Skript alle 30 Minuten automatisch ausführen möchtest, kannst du den Windows Task Scheduler verwenden:

### Windows Task Scheduler einrichten

1. Task Scheduler öffnen (Windows-Taste drücken, nach "Task Scheduler" suchen und öffnen)

2. Neue Aufgabe erstellen: Rechts auf "Create Basic Task" klicken

3. Einen Namen vergeben: z. B. "Trink-Erinnerung"

4. Trigger setzen: "Daily" auswählen, dann alle 30 Minuten wiederholen

5. Aktion auswählen: "Start a Program"

6. Pfad zur Python.exe eingeben (z. B. C:\Users\Admin\AppData\Local\Programs\Python\Python313\python.exe)

   Skript als Argument übergeben: C:\Pfad\zu\drink_reminder.py

7. Fertigstellen und testen

### Linux/macOS: Automatische Ausführung mit cron

1. Terminal öffnen und crontab -e eingeben

2. Diese Zeile hinzufügen, um das Skript alle 30 Minuten auszuführen:

   */30 * * * * /usr/bin/python3 /Pfad/zu/drink_reminder.py

## Anpassungen

Die Nachrichten kannst du im toasts-Array im Skript ändern oder erweitern.

Falls du ein eigenes Symbol möchtest, ersetze icon_path in win10toast durch den Pfad zu deiner .ico-Datei.

# Viel Spaß und bleib hydriert! 💧
