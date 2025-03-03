# für Linus, macOS und Android - from plyer import notification
from win10toast import ToastNotifier    # Windows
import time, random, sys

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
                
def drink_notification():
    toaster = ToastNotifier()
    toaster.show_toast(
        "Drink Reminder",
        random.choice(toasts),
        duration=30,
        icon_path= r"C:\Users\Admin\Documents\Zara\Python Projects\Trink-Erinnerung\icon_tropfen_1F4_icon.ico",
        threaded=True
        )

if __name__ == "__main__":
    drink_notification()