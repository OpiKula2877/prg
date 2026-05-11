import time
import os
import platform

# Pokus o import knihoven pro zobrazování obrázků
try:
    from PIL import Image
    PIL_AVAILABLE = True
except ImportError:
    PIL_AVAILABLE = False
    print("PIL (Pillow) není nainstalován – obrázky se nezobrazí.")

def show_image_temporarily(image_path, duration=3):
    """Zobrazí obrázek na určitou dobu a pak ho zavře."""
    if not PIL_AVAILABLE or not os.path.exists(image_path):
        return

    img = Image.open(image_path)
    img.show()
    time.sleep(duration)
    # Na některých systémech nelze okno automaticky zavřít, 
    # ale po 'duration' sekundách skript pokračuje.
    print("(Obrázek byl zobrazen a nyní se hra pokračuje...)\n")

def clear_screen():
    os.system('cls' if platform.system() == 'Windows' else 'clear')

def print_slow(text, delay=0.04):
    """Pomalu tiskne text pro lepší efekt."""
    for char in text:
        print(char, end='', flush=True)
        time.sleep(delay)
    print()

# --- Hlavní část hry ---
def main():
    clear_screen()
    print("🌟 Vítej ve Starém hvozdu – textové dobrodružství! 🌟\n")
    time.sleep(1)

    name = input("Jak se jmenuješ, cestovateli? ")
    print_slow(f"\nAhoj, {name}! Připrav se na nečekané zážitky...\n")

    time.sleep(1)
    print("Najednou před tebou vykoukne tajemný králík s hodinkami...")
    show_image_temporarily("králik.png", duration=2)  # Nahraď svojím obrázkem

    print_slow("Králík: 'Spěcháš? Já taky! Ale... chceš vědět tajemství lesa?'")
    choice = input("\n[1] Ano, řekni mi!\n[2] Ne, radši půjdu dál.\nVyber (1/2): ")

    if choice == "1":
        print_slow("\nKrálík ti utíká za strom a nechává ti starou mapu...")
        show_image_temporarily("mapa.png", duration=2)
        print_slow("Na mapě je označený poklad zakopaný pod Velkým dubem!\n")
        print("✅ Získal jsi: Starou mapu")
    else:
        print_slow("\nKrálík zmizí v mlze... Možná jsi ušetřil čas, ale co takhle dobrodružství?\n")

    print_slow("\nLes se před tebou rozprostírá... Co uděláš dál?")
    print("🔹 Možnosti: jdi na sever / prozkoumej jeskyni / vrať se domů")
    next_move = input("Tvá volba: ").strip().lower()

    if "sever" in next_move:
        print_slow("\nJdeš na sever a najdeš opuštěný chrám plný hádanek...")
    elif "jeskyn" in next_move:
        print_slow("\nV jeskyni slyšíš ozvěnu... Něco se hýbe ve tmě!")
    else:
        print_slow(f"\nVracíš se domů, {name}. Ale vzpomínky na les tě budou provázet navždy...")

    print("\n\nKONEC dobrodružství... Prozatím. 🏁")

if __name__ == "__main__":
    main()