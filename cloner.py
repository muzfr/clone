import discord
import asyncio
from discord.ext import commands
import shutil
from colorama import init, Fore, Style

init(autoreset=True)

def center(text):
    terminal_width = shutil.get_terminal_size().columns
    return "\n".join(line.center(terminal_width) for line in text.splitlines())

def splash():
    art = Fore.MAGENTA + Style.BRIGHT + """
⡤⠲⡄⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⡎⢑
⠑⢲⠷⢤⣀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⣠⠶⠚⡟⠉
⠀⠸⡇⠀⠈⠙⠲⢤⣀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⣠⠴⠚⠉⠀⠀⠀⡇⠀
⠀⠀⡇⠀⠀⠀⠀⠀⠈⠙⣲⣀⠄⠠⠄⠒⠢⠤⠠⢴⠋⠁⠀⠀⠀⠀⠀⢸⠇⠀
⠀⠀⣧⠀⠀⠀⠀⠀⣀⠏⠀⠀⠀⠀⠀⠀⢀⠀⠀⠈⠉⢳⡀⠀⠀⠀⠀⢸⠀⠀
⠀⠀⢸⠀⠀⠀⣠⣾⠀⠀⠀⣂⡠⠤⢤⣤⠬⠤⢄⣰⠀⠀⠈⣷⡀⠀⠀⡾⠀⠀
⠀⠀⠸⢦⣀⣼⠋⢏⢀⡜⠊⠁⢠⣾⣿⣿⣿⣦⠀⠈⠑⠶⡀⣹⠹⡦⠖⠃⠀⠀
⠀⠀⠀⠀⢸⠃⠀⠀⠉⠀⠀⠀⠸⣁⣼⣿⣇⡸⠀⠀⠀⠀⠈⠁⠀⢻⡀⠀⠀⠀
⠀⠀⠀⠀⣾⠀⠀⠀⣠⡴⠒⠉⠓⠲⢼⣈⠯⠒⠋⠙⠲⣄⠀⠀⠀⢸⡇⠀⠀⠀
⠀⠀⠀⠀⢹⠀⠀⣰⠋⢲⣤⡀⠀⠀⠀⠀⠀⠀⠀⣠⣴⠋⢳⠀⠀⢸⠃⠀⠀⠀
⠀⠀⠀⠀⠈⣧⠀⣏⠀⢸⣿⠏⠀⠀⢀⣀⠀⠀⠀⢿⡿⠀⠈⡇⢠⠏⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠈⠳⣿⡀⠀⠀⠀⠀⠀⢌⣂⠅⠀⠀⠀⠀⢀⣼⡶⠋⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⢀⡀⣀⠽⠓⠲⠤⢤⣤⣤⣤⣤⣤⡤⠤⠶⢯⡁⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠣⠸⠛⠒⠒⢲⡀⠀⣀⡤⠦⣄⠀⢠⠖⠒⠒⠻⣀⠇⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢔⢑⠋⠁⠀⠀⠀⢹⠉⡂⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
"""
    print(center(art))
    print(center(Fore.LIGHTBLACK_EX + "⚠ @imneverenough ⚠\n"))

def show_status():
    terminal_width = shutil.get_terminal_size().columns
    cyan = Fore.CYAN + Style.BRIGHT
    green = Fore.GREEN + Style.BRIGHT
    white = Fore.WHITE + Style.BRIGHT
    gray = Fore.LIGHTBLACK_EX

    lines = [
        cyan + "+--------------------------------------+",  # 40 wide
        cyan + "|            CLONER STATUS             |",
        cyan + "+--------------------------------------+",
        green + "| Status:             ONLINE ✅        |",
        green + "| Cloning Channels:   ON ✅            |",
        green + "| Cloning Categories: ON ✅            |",
        cyan + "+--------------------------------------+",
        white + "|         Developed by muz             |",
        gray  + "|      Discord: @imneverenough         |",
        gray  + "|      YouTube: @reapproved            |",
        cyan + "+--------------------------------------+"
    ]

    for line in lines:
        print(line.center(terminal_width))
with open("token.txt", "r") as f:
    TOKEN = f.read().strip()

intents = discord.Intents.all()
client = commands.Bot(command_prefix="?", self_bot=True, intents=intents)
client.remove_command("help")

@client.event
async def on_ready():
    splash()
    show_status()

    print(f"Logged in as {client.user}")
    
    source_id = int(input("Enter the SOURCE server ID: "))
    target_id = int(input("Enter the TARGET server ID: "))

    source_guild = client.get_guild(source_id)
    target_guild = client.get_guild(target_id)

    if not source_guild:
        print("❌ Source server not found.")
    if not target_guild:
        print("❌ Target server not found.")
        await client.close()
        return

    await clone_server(source_guild, target_guild)
    print("✅ Clone complete.")
    await client.close()

async def clone_server(source_guild, target_guild):
    # Clone server name & icon (optional, commented out)
    # try:
    #     await target_guild.edit(name=source_guild.name)
    #     print(f"[+] Server name set to: {source_guild.name}")
    # except Exception as e:
    #     print(f"[-] Failed to set server name: {e}")

    print(Fore.YELLOW + "\n[~] Clearing channels from target server...")
    for ch in target_guild.channels:
        try:
            await ch.delete()
            print(Fore.LIGHTBLACK_EX + f"[~] Deleted: {ch.name}")
            await asyncio.sleep(0.6)
        except Exception as e:
            print(Fore.RED + f"[-] Couldn't delete {ch.name}: {e}")

    category_map = {}

    print(Fore.YELLOW + "\n[~] Cloning categories...")
    for category in source_guild.categories:
        try:
            new_cat = await target_guild.create_category(name=category.name)
            category_map[category.id] = new_cat
            print(Fore.GREEN + f"[+] Category Created: {category.name}")
            await asyncio.sleep(0.8)
        except Exception as e:
            print(Fore.RED + f"[-] Failed to create category {category.name}: {e}")

    print(Fore.YELLOW + "\n[~] Cloning text channels...")
    for channel in source_guild.text_channels:
        try:
            cat = category_map.get(channel.category_id)
            new_text = await target_guild.create_text_channel(
                name=channel.name,
                topic=channel.topic or None,
                category=cat
            )
            print(Fore.GREEN + f"[+] Text Channel Created: {channel.name}")
            await asyncio.sleep(0.8)
        except Exception as e:
            print(Fore.RED + f"[-] Failed to create text channel {channel.name}: {e}")

    print(Fore.YELLOW + "\n[~] Cloning voice channels...")
    for channel in source_guild.voice_channels:
        try:
            cat = category_map.get(channel.category_id)
            new_voice = await target_guild.create_voice_channel(
                name=channel.name,
                category=cat
            )
            print(Fore.GREEN + f"[+] Voice Channel Created: {channel.name}")
            await asyncio.sleep(0.8)
        except Exception as e:
            print(Fore.RED + f"[-] Failed to create voice channel {channel.name}: {e}")

client.run(TOKEN, bot=False)
