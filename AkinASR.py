import random
import ctypes
import colorama
from colorama import Fore, Back, Style
colorama.init(autoreset=True)

caratteristiche_calciatori = {
    "Romelu Lukaku": {"nero": True, "attaccante": True, "centrocampista": False, "Difensore": False, "portiere": True, "po fa de tutto": False, "nazionalità italiana": False, "numero più alto del 50": True, "numero: 90": True, "numero: 7": False, "numero: 92": False, "numero: 9": False},
    "Lorenzo Pellegrini": {"nero": False, "attaccante": False, "centrocampista": True, "Difensore": False, "portiere": False, "po fa de tutto": False, "nazionalità italiana": True, "numero più alto del 50": False, "numero: 7": True, "numero: 90": False, "numero: 92": False, "numero: 9": False},
    "Stephan El Shaarawy": {"nero": False, "attaccante": True, "centrocampista": False, "Difensore": False, "portiere": False, "po fa de tutto": False, "nazionalità italiana": True, "numero più alto del 50": True, "numero: 92": True, "numero: 90": False, "numero: 7": False, "numero: 92": False, "numero: 9": False},
    "Tammy Abraham": {"nero": True, "attaccante": True, "centrocampista": False, "Difensore": False, "portiere": False, "po fa de tutto": False, "nazionalità italiana": False, "numero più alto del 50": False, "numero: 9": True, "numero: 90": False, "numero: 7": False, "numero: 92": False},
    "Bryan Cristante": {"nero": False, "attaccante": False, "centrocampista": True, "Difensore": False, "portiere": False, "po fa de tutto": True, "nazionalità italiana": True, "numero più alto del 50": False, "numero: 4": True, "numero: 90": False, "numero: 7": False, "numero: 92": False, "numero: 9": False},
    "Paulo Dybala": {"nero": False, "attaccante": True, "centrocampista": False, "Difensore": False, "portiere": False, "po fa de tutto": False, "nazionalità italiana": False, "numero più alto del 50": False, "numero: 21": True, "numero: 90": False, "numero: 7": False, "numero: 92": False, "numero: 9": False},
    "Leonardo Spinazzola": {"nero": False, "attaccante": False, "centrocampista": False, "Difensore": True, "portiere": False, "po fa de tutto": False, "nazionalità italiana": True, "numero più alto del 50": False, "numero: 37": True, "numero: 90": False, "numero: 7": False, "numero: 92": False, "numero: 9": False},
    "Rui Patricìo": {"nero": False, "attaccante": False, "centrocampista": False, "Difensore": False, "portiere": True, "po fa de tutto": False, "nazionalità italiana": False, "numero più alto del 50": False, "numero: 1": True, "numero: 90": False, "numero: 7": False, "numero: 92": False, "numero: 9": False},
    "Rick Karsdorp": {"nero": False, "attaccante": False, "centrocampista": True, "Difensore": True, "portiere": False, "po fa de tutto": False, "nazionalità italiana": False, "numero più alto del 50": False, "numero: 2": True, "numero: 90": False, "numero: 7": False, "numero: 92": False, "numero: 9": False},
    "Edoardo Bove": {"nero": False, "attaccante": False, "centrocampista": True, "Difensore": False, "portiere": False, "po fa de tutto": False, "nazionalità italiana": True, "numero più alto del 50": True, "numero: 52": True, "numero: 90": False, "numero: 7": False, "numero: 92": False, "numero: 9": False}
}

def genera_domanda(domande_fatte):
    domande_possibili = list(random.choice(list(caratteristiche_calciatori.values())).keys())
    domanda = random.choice(domande_possibili)
    
    while domanda in domande_fatte:
        domanda = random.choice(domande_possibili)
    
    return domanda
    pass

def scegli_calciatore():
    return random.choice(list(caratteristiche_calciatori.keys()))
    pass

def gioca():
    print(Fore.YELLOW + Back.RED + "Benvenuto a akinASR" + Style.RESET_ALL)
    print(Fore.LIGHTRED_EX + Style.DIM + "Indovinerò il calciatore daa maggica facendo domande con risposte sì/no." + Style.RESET_ALL)

    indovinato = False
    domande_rimanenti = 10
    domande_fatte = []

    while not indovinato:
        domanda = genera_domanda(domande_fatte)
        while True:
            risposta = input(f"Il calciatore ha la caratteristica '{domanda}'? (si/no): ").strip().lower()
            if risposta in ("si", "no"):
                break
            else:
                print(Fore.BLUE + Style.BRIGHT + "Per favore, rispondi con 'si' o 'no'." + Style.RESET_ALL)
        
        domande_fatte.append(domanda)
        
        if risposta == "si":
            domande_rimanenti -= 1
            caratteristica = domanda
            calciatori_possibili = [calciatore for calciatore, caratteristiche_cal in caratteristiche_calciatori.items() if caratteristiche_cal[caratteristica]]
    
            if len(calciatori_possibili) == 1:
                domanda_ultima = input(f"Il calciatore che hai pensato è {calciatori_possibili[0]}?")
                if domanda_ultima == 'si':
                    print(Fore.GREEN + 'Hai vinto!' + Style.RESET_ALL)
                    rigioca = input('Vuoi rigiocare?')
                    if rigioca == 'si':
                        gioca()
                    elif rigioca == 'no':
                        break
                    else:
                        print('per favore rispondi con si/no')
                        rigioca_due = input('Vuoi rigiocare?')
                        if rigioca_due == 'si':
                                gioca()
                        elif rigioca_due == 'no':
                            break
                        else:
                            ctypes.windll.user32.MessageBoxW(0, 'bravo adesso devi restartare il programma, ti stavo facilitando le cose', 'stolto', 1) 
                            break
        elif risposta == "no":
            domande_rimanenti -= 1

        if domande_rimanenti == 1:
                    risposta_ultima_domanda = input(f'Il tuo calciatore è {scegli_calciatore()}? (si/no): ').strip().lower()
                    if risposta_ultima_domanda == 'si':
                        print(Fore.GREEN + "Ho indovinato!" + Style.RESET_ALL)
                        user_sc3lta = ctypes.windll.user32.MessageBoxW(0, 'Vuoi rigiocare?', 'Game Over', 4)
                        if user_sc3lta == 6:
                            gioca()
                        else:
                            break
                    else:
                        print(Fore.RED + "Non sono riuscito ad indovinare il calciatore che hai pensato." + Style.RESET_ALL)
                        user_scelta = ctypes.windll.user32.MessageBoxW(0, 'Vuoi rigiocare?', 'Game Over', 4)
                        if user_scelta == 6:
                            gioca()
                        else:
                            break
        else:
            print(f"Ok, continua. Ti rimangono {domande_rimanenti} domande.")

if __name__ == "__main__":
    gioca()
