import random
import ctypes
import colorama
from colorama import Fore, Back, Style
from flask import Flask, request, jsonify, render_template

colorama.init(autoreset=True)
app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/inizia-gioco', methods=['POST'])
def inizia_gioco():
    risultato_gioco = gioca()  
    return jsonify({"risultato_gioco": risultato_gioco})

caratteristiche_calciatori = {
    "Romelu Lukaku": {
        "ruolo": "attaccante",
        "numero di maglia": 90,
        "nazionalità": "belga",
    },
    "Paulo Dybala": {
        "ruolo": "attaccante",
        "numero di maglia": 21,
        "nazionalità": "argentina",
    },
    "Tammy Abraham": {
        "ruolo": "attaccante",
        "numero di maglia": 9,
        "nazionalità": "inglese",
    },
    "Bryan Cristante": {
        "ruolo": "centrocampistan",
        "numero di maglia": 4,
        "nazionalità": "italiana",
    },
    "Leonardo Spinazzola": {
        "ruolo": "difensore",
        "numero di maglia": 37,
        "nazionalità": "italiana",
    },
    "Rui Patricìo": {
        "ruolo": "portiere",
        "numero di maglia": 1,
        "nazionalità": "portoghese",
    },
    "Rick Karsdorp": {
        "ruolo": "centrocampista",
        "numero di maglia": 2,
        "nazionalità": "olandese",
    },
    "Edoardo Bove": {
        "ruolo": "centrocampista",
        "numero di maglia": 52,
        "nazionalità": "italiana",
    },
    "Lorenzo Pellegrini": {
        "ruolo": "centrocampista",
        "numero di maglia": 7,
        "nazionalità": "italiana",
    },
    "Stephan El Shaarawy": {
        "ruolo": "attaccante",
        "numero di maglia": 92,
        "nazionalità": "italiana",
    },
    "Chris Smalling": {
        "ruolo": "difensore",
        "numero di maglia": 6,
        "nazionalità": "inglese",
    },
    "Gianluca Mancini": {
        "ruolo": "difensore",
        "numero di maglia": 23,
        "nazionalità": "italiana",
    },
}

def scegli_calciatore():
    return random.choice(list(caratteristiche_calciatori.keys()))

def gioca():
    print(Fore.YELLOW + Back.RED + "Benvenuto a akinASR" + Style.RESET_ALL)
    print(Fore.LIGHTRED_EX + Style.DIM + "Indovinerò il calciatore facendo domande con risposte sì/no." + Style.RESET_ALL)

    indovinato_numero = False
    indovinato = False
    domande_rimanenti = 10
    domande_fatte = []
    domande_possibili_attributo = list(list(list(caratteristiche_calciatori.keys())))  
    domande_possibili_numero = []

    for calciatore, caratteristiche in caratteristiche_calciatori.items():
        attributo = "numero di maglia"
        valore_attributo = caratteristiche.get(attributo, None)
        if valore_attributo is not None:
            domanda = f"Il tuo calciatore ha il {attributo} {valore_attributo}?"
            domande_possibili_attributo.append(domanda)

        attributo = "nazionalità"
        valore_attributo = caratteristiche.get(attributo, None)
        if valore_attributo is not None:
            domanda = f"Il tuo calciatore ha la {attributo} {valore_attributo}?"
            domande_possibili_attributo.append(domanda)

        attributo = "ruolo"
        valore_attributo = caratteristiche.get(attributo, None)
        if valore_attributo is not None:
            domanda = f"Il tuo calciatore ha il {attributo} {valore_attributo}?"
            domande_possibili_attributo.append(domanda)

    while not indovinato:
        def genera_domanda(domande_possibili_attributo, domande_possibili_numero):
            if domande_possibili_attributo and not indovinato_numero:
                return random.choice(domande_possibili_attributo)
            elif domande_possibili_numero:
                return random.choice(domande_possibili_numero)
            else:
                return ""
        domanda = genera_domanda(domande_possibili_attributo, domande_possibili_numero)
        if not domanda:
            break
        while True:
            risposta = input(f"{domanda} (si/no): ").strip().lower()
            if risposta in ("si", "no"):
                break
            else:
                print(Fore.BLUE + Style.BRIGHT + "Per favore, rispondi con 'si' o 'no'." + Style.RESET_ALL)

        domande_fatte.append(domanda)

        if risposta == "si":
            domande_rimanenti -= 1
            if domanda in domande_possibili_attributo:
                domande_possibili_attributo.remove(domanda)
            if domanda in domande_possibili_numero:
                domande_possibili_numero.remove(domanda)
                indovinato_numero = True

            calciatori_possibili = [calciatore for calciatore, caratteristiche_cal in caratteristiche_calciatori.items() if domanda in caratteristiche_cal]
            if len(calciatori_possibili) == 1:
                calciatore_indovinato = calciatori_possibili[0]
                print(Fore.GREEN + f'Ho indovinato! Il calciatore è {calciatore_indovinato}' + Style.RESET_ALL)
                rigioca = input('Vuoi rigiocare? (si/no): ')
                if rigioca == 'si':
                    gioca()
                elif rigioca == 'no':
                    break
                else:
                    print('Per favore, rispondi con si/no')
                    rigioca_due = input('Vuoi rigiocare? (si/no): ')
                    if rigioca_due == 'si':
                        gioca()
                    elif rigioca_due == 'no':
                        break
                    else:
                        ctypes.windll.user32.MessageBoxW(0, 'Bravo, ora devi riavviare il programma.', 'Recchione', 1)
                        break
        elif risposta == "no":
            domande_rimanenti -= 1
            if domanda in domande_possibili_attributo:
                domande_possibili_attributo.remove(domanda)
            if domanda in domande_possibili_numero:
                domande_possibili_numero.remove(domanda)

        if domande_rimanenti == 1:
            risposta_ultima_domanda = input(f'Il tuo calciatore è {scegli_calciatore()}? (si/no): ').strip().lower()
            if risposta_ultima_domanda == 'si':
                print(Fore.GREEN + "Ho indovinato!" + Style.RESET_ALL)
                user_scelta = input('Vuoi rigiocare? (si/no): ').strip().lower()
                if user_scelta == 'si':
                    gioca()
                elif user_scelta == 'no':
                    break
            else:
                print(Fore.RED + "Non sono riuscito ad indovinare il calciatore che hai pensato." + Style.RESET_ALL)
                user_scelta = input('Vuoi rigiocare? (si/no): ').strip().lower()
                if user_scelta == 'si':
                    gioca()
                elif user_scelta == 'no':
                    break
    else:
        print(f"Ok, continua. Ti rimangono {domande_rimanenti} domande.")


if __name__ == "__main__":
    gioca()
