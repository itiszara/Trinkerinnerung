# Importiere die benötigte Bibliothek für Desktop-Benachrichtigungen
# für Linus, macOS und Android - from plyer import notification
from win10toast import ToastNotifier    # für Windows
import time, random, sys

# Definiere eine Liste mit verschiedenen Erinnerungsnachrichten 
toasts = ["Trinken oder welken - du entscheidest!",
                 "Deine Pflanzen wollen, dass du auch mal trinkst!",
                 "Mehr Wasser, weniger Sorgen!",
                 "Hydriert bleiben, sonst wirst du zum Trockenobst!",
                 "Hey, dein Körper freut sich über einen Schluck Wasser!",
                 "Dein Gehirn liebt Wasser - tu ihm den Gefallen!",
                 "Ein Glas Wasser und die Welt sieht gleich besser aus!",
                 "Hydriert = motiviert! Los, trink einen Schluck!",
                 "Power up! Dein Körper braucht Flüssigkeit!",
                 "Ohne Wasser keine Energie - schnapp dir dein Glas!",
                 "Dein Körper ist eine Maschine - gib ihm den richtigen Treibstoff!",
                 "Dein Körper besteht zu 70% aus Wasser - Zeit, den Vorrat aufzufüllen!",
                 "Dein Gehirn ruft an: Es will mehr Wasser!",
                 "Bleib hydratisiert - du bist schließlich kein Kaktus!",
                 "Trink Wasser - sonst quietscht dein Gehirn beim Denken!",
                 "Mehr Wasser, weniger Falten. Ich sag´s ja nur…",
                 "Wasser ist quasi flüssige Produktivität. Gönn dir!",
                 "Hydration ist wie ein Schutzschild gegen miese Laune!",
                 "Deine Nieren haben mir geschrieben: Sie wollen mehr Wasser!"]

# Funktion, die eine Trink-Erinnerung als Desktop-Benachrichtigung anzeigt                
def drink_notification():
    # Erstelle ein ToastNotifier-Objekt für Windows-Benachrichtigungen
    toaster = ToastNotifier()
    # Zeige eine Benachrichtigung mit zufälliger Nachricht aus der Liste
    toaster.show_toast(
        "Drink Reminder",       # Titel der Benachrichtigung
        random.choice(toasts),  # Zufällige Erinnerung aus der Liste auswählen
        duration=30,            # Dauer der Benachrichtigung (in Sekunden)
        icon_path= r"C:\Users\Admin\Documents\Zara\Python Projects\Trink-Erinnerung\icon_tropfen_1F4_icon.ico", # Pfad zum Icon
        threaded=True           # Threaded=True sorgt dafür, dass die Benachrichtigung nicht das Hauptprogramm blockiert
        )
    
# Falls dieses Skript direkt ausgeführt wird, rufe die drink_notification-Funktion auf
if __name__ == "__main__":
    drink_notification()
