import random
import time
import sys
from colorama import Fore, Back, Style, init

# Initialize colorama
init(autoreset=True)

# ==================== GAME CONFIG ====================
LEGEND_CHANCE = 1_000_000  # 1 in a million
PLAYER_ENERGY = 100
SEARCH_COST = 10
FAME_REQUIRED = 1000
SPECIAL_EVENTS = {
    "Coffee Break": {"energy": +30, "text": "You found an abandoned coffee shop! +30 energy"},
    "Bug Fix": {"fame": +50, "text": "You fixed a critical bug! +50 fame"},
    "Stack Overflow": {"energy": -15, "text": "You got lost on Stack Overflow! -15 energy"}
}

# ==================== ART ASSETS ====================
def print_title():
    print(Fore.CYAN + r"""
   ███╗   ██╗ █████╗ ███╗   ███╗███████╗     ██╗     ███████╗ ██████╗ ███████╗███╗   ██╗██████╗ ███████╗
   ████╗  ██║██╔══██╗████╗ ████║██╔════╝     ██║     ██╔════╝██╔════╝ ██╔════╝████╗  ██║██╔══██╗██╔════╝
   ██╔██╗ ██║███████║██╔████╔██║█████╗       ██║     █████╗  ██║  ███╗█████╗  ██╔██╗ ██║██║  ██║███████╗
   ██║╚██╗██║██╔══██║██║╚██╔╝██║██╔══╝       ██║     ██╔══╝  ██║   ██║██╔══╝  ██║╚██╗██║██║  ██║╚════██║
   ██║ ╚████║██║  ██║██║ ╚═╝ ██║███████╗     ███████╗███████╗╚██████╔╝███████╗██║ ╚████║██████╔╝███████║
   ╚═╝  ╚═══╝╚═╝  ╚═╝╚═╝     ╚═╝╚══════╝     ╚══════╝╚══════╝ ╚═════╝ ╚══════╝╚═╝  ╚═══╝╚═════╝ ╚══════╝
    """)
    print(Fore.YELLOW + f"\nA game where you search for the legendary coder: {Fore.RED}KURUCZ GERGELY {Fore.YELLOW}(1 in {LEGEND_CHANCE:,} chance!)")
    print(Fore.GREEN + "\nTIP: Type 'help' for commands")

def print_legend_found():
    print(Fore.MAGENTA + r"""
    ╔════════════════════════════════════════════╗
    ║   ██████╗  ██████╗ ██████╗ ███████╗██████╗ ║
    ║  ██╔════╝ ██╔═══██╗██╔══██╗██╔════╝██╔══██╗║
    ║  ██║  ███╗██║   ██║██║  ██║█████╗  ██████╔╝║
    ║  ██║   ██║██║   ██║██║  ██║██╔══╝  ██╔══██╗║
    ║  ╚██████╔╝╚██████╔╝██████╔╝███████╗██║  ██║║
    ║   ╚═════╝  ╚═════╝ ╚═════╝ ╚══════╝╚═╝  ╚═╝║
    ╚════════════════════════════════════════════╝
    """)

# ==================== GAME STATE ====================
player = {
    "fame": 0,
    "energy": PLAYER_ENERGY,
    "found_legends": [],
    "searches": 0,
    "special_events": 0
}

# ==================== CHARACTER GENERATION ====================
def generate_character():
    origins = ["Hungarian", "Japanese", "Russian", "Brazilian", "Indian"]
    origin = random.choice(origins)
    
    gender = random.choice(["male", "female"])
    first_names = {
        "Hungarian": {"male": ["Gergely", "Ádám", "Péter"], "female": ["Anna", "Katalin", "Éva"]},
        "Japanese": {"male": ["Haruto", "Riku", "Yuto"], "female": ["Himari", "Mei", "Sakura"]}
    }.get(origin, {"male": ["John", "David"], "female": ["Sarah", "Emily"]})
    
    last_names = {
        "Hungarian": ["Kovács", "Szabó", "Kurucz"],
        "Japanese": ["Sato", "Suzuki", "Tanaka"]
    }.get(origin, ["Smith", "Johnson"])
    
    first = random.choice(first_names[gender])
    last = random.choice(last_names)
    
    # Check for Kurucz Gergely
    if first == "Gergely" and last == "Kurucz":
        if random.randint(1, LEGEND_CHANCE) == 1:
            return {
                "name": "Kurucz Gergely",
                "nickname": "The Unkillable Debugger",
                "origin": "Hungarian",
                "age": 24,
                "title": "The Code Messiah",
                "stats": {"Coding": 1000, "Coffee Resistance": 1000},
                "fact": "Can debug segfaults by staring at the screen",
                "is_legend": True
            }
    
    # Normal character
    titles = {
        "Hungarian": ["Code Wizard", "Binary Bard"],
        "Japanese": ["Pixel Samurai", "Algorithm Ronin"]
    }.get(origin, ["The Programmer", "The Developer"])
    
    return {
        "name": f"{first} {last}",
        "origin": origin,
        "age": random.randint(18, 80),
        "title": random.choice(titles),
        "stats": {"Skill": random.randint(1, 100)},
        "is_legend": False
    }

# ==================== GAME MECHANICS ====================
def handle_special_event():
    if random.random() < 0.15:  # 15% chance for special event
        event = random.choice(list(SPECIAL_EVENTS.keys()))
        effect = SPECIAL_EVENTS[event]
        
        print(Fore.BLUE + f"\n⚡ {event.upper()} ⚡")
        print(Fore.CYAN + effect["text"])
        
        if "energy" in effect:
            player["energy"] = max(0, player["energy"] + effect["energy"])
        if "fame" in effect:
            player["fame"] += effect["fame"]
        
        player["special_events"] += 1
        return True
    return False

def search_for_legend():
    if player["energy"] < SEARCH_COST:
        print(Fore.RED + "\n⚠️ You're too exhausted to keep searching!")
        return False
    
    player["energy"] -= SEARCH_COST
    player["searches"] += 1
    
    print(Fore.YELLOW + f"\n🔍 Searching... (Energy: {player['energy']}/100)")
    time.sleep(0.5)
    
    # Check for special event first
    if not handle_special_event():
        char = generate_character()
        
        if char["is_legend"]:
            player["fame"] = FAME_REQUIRED
            player["found_legends"].append(char)
            print_legend_found()
            print(Fore.GREEN + "\n🎉✨ YOU FOUND THE LEGENDARY KURUCZ GERGELY! ✨🎉")
            print(Fore.MAGENTA + f"Fact: {char['fact']}")
        else:
            fame_gain = char["stats"]["Skill"] // 10
            player["fame"] += fame_gain
            print(Fore.WHITE + f"\nFound: {Fore.CYAN}{char['name']} {Fore.WHITE}({char['origin']})")
            print(f"{Fore.YELLOW}Title: {char['title']} | {Fore.GREEN}Skill: {char['stats']['Skill']}")
            print(f"{Fore.BLUE}+{fame_gain} fame")
    
    return True

def rest():
    recovery = random.randint(20, 40)
    player["energy"] = min(100, player["energy"] + recovery)
    print(Fore.GREEN + f"\n💤 You rest and recover {recovery} energy. (Now: {player['energy']}/100)")

def show_status():
    print(Fore.CYAN + "\n" + "═" * 40)
    print(f"{Fore.YELLOW}⭐ Fame: {Fore.WHITE}{player['fame']}/{FAME_REQUIRED}")
    print(f"{Fore.YELLOW}⚡ Energy: {Fore.WHITE}{player['energy']}/100")
    print(f"{Fore.YELLOW}🔎 Searches: {Fore.WHITE}{player['searches']}")
    print(f"{Fore.YELLOW}✨ Special Events: {Fore.WHITE}{player['special_events']}")
    if player["found_legends"]:
        print(f"{Fore.MAGENTA}🏆 Legend Found: {Fore.WHITE}KURUCZ GERGELY")
    print(Fore.CYAN + "═" * 40)

def show_help():
    print(Fore.CYAN + "\n" + "═" * 40)
    print(f"{Fore.YELLOW}COMMANDS:")
    print(f"{Fore.GREEN}search/s{Fore.WHITE} - Search for the legend (costs 10 energy)")
    print(f"{Fore.GREEN}rest/r{Fore.WHITE} - Recover energy (random 20-40)")
    print(f"{Fore.GREEN}status{Fore.WHITE} - Show your current stats")
    print(f"{Fore.GREEN}help{Fore.WHITE} - Show this help menu")
    print(f"{Fore.GREEN}quit/q{Fore.WHITE} - Exit the game")
    print(Fore.CYAN + "═" * 40)

# ==================== MAIN GAME LOOP ====================
def main():
    print_title()
    
    while player["fame"] < FAME_REQUIRED and player["energy"] > 0:
        show_status()
        choice = input(f"\n{Fore.WHITE}What will you do? ").lower()
        
        if choice in ["s", "search"]:
            search_for_legend()
        elif choice in ["r", "rest"]:
            rest()
        elif choice == "status":
            continue  # Status will show again at loop start
        elif choice == "help":
            show_help()
        elif choice in ["q", "quit"]:
            print(Fore.YELLOW + "\nThanks for playing!")
            return
        else:
            print(Fore.RED + "Invalid command! Type 'help' for options.")
        
        # Small delay for better pacing
        time.sleep(0.3)
    
    # Game end
    if player["fame"] >= FAME_REQUIRED:
        print(Fore.GREEN + "\n" + "⭐" * 50)
        print(Fore.YELLOW + "YOU WIN! The legend of Kurucz Gergely is real!")
        print(Fore.CYAN + "His power: Can write bug-free code on first try")
        print(Fore.GREEN + "⭐" * 50)
    else:
        print(Fore.RED + "\n" + "💀" * 50)
        print(Fore.YELLOW + "GAME OVER! You failed to find the legend...")
        print(Fore.CYAN + "Maybe next time!")
        print(Fore.RED + "💀" * 50)

if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        print(Fore.YELLOW + "\n\nGame interrupted. Thanks for playing!")
        sys.exit(0)