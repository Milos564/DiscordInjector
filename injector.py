import time, sys, os, getpass
from colorama import Fore

def clear():
    if sys.platform == 'darwin':
        os.system('clear')
    elif os.name == 'nt':
        os.system('cls')
    else:
        os.system('clear')


username = getpass.getuser()
success = f'{Fore.GREEN}[✓]{Fore.WHITE}'
error = f'{Fore.RED}[✗]{Fore.WHITE}'
log = f'{Fore.YELLOW}[*]{Fore.WHITE}'


detect_versions = lambda discordpath,idxsubpath: [
    (discordpath+vsn+idxsubpath, vsn) for vsn in (os.listdir(discordpath) if os.path.exists(discordpath) else []) if os.path.isdir(discordpath+vsn) and len(vsn.split('.')) == 3 ]

if sys.platform == 'darwin':
    clear()
    print(f'{success} Detected A OS X Machine')
    baseclients = {
    'STABLE' : detect_versions('/Users/%s/Library/Application Support/discord/'%username, '/modules/discord_desktop_core/index.js'),
    'CANARY' : detect_versions('/Users/%s/Library/Application Support/discordcanary/'%username, '/modules/discord_desktop_core/index.js'),
    'PTB'    : detect_versions('/Users/%s/Library/Application Support/discordptb/'%username, '/modules/discord_desktop_core/index.js')
}
elif os.name == 'nt':
    clear()
    print(f'{success} Detected A Windows Machine')
    baseclients = {
        'STABLE' : detect_versions('C:/Users/%s/AppData/Roaming/Discord/'%username, '/modules/discord_desktop_core/index.js'),
        'CANARY' : detect_versions('C:/Users/%s/AppData/Roaming/discordcanary/'%username, '/modules/discord_desktop_core/index.js'),
        'PTB'    : detect_versions('C:/Users/%s/AppData/Roaming/Discord PTB/'%username, '/modules/discord_desktop_core/index.js')
}
else:
    clear()
    print(f'{success} Detected A Linux Machine')
    baseclients = {
        'STABLE' : detect_versions('/home/%s/.config/discord/'%username, '/modules/discord_desktop_core/index.js'),
        'CANARY' : detect_versions('/home/%s/.config/discordcanary/'%username, '/modules/discord_desktop_core/index.js'),
        'PTB'    : detect_versions('/home/%s/.config/discordptb/'%username, '/modules/discord_desktop_core/index.js'),
        'SNAP'   : detect_versions('/home/%s/snap/discord/current/.config/discord/'%username, '/modules/discord_desktop_core/index.js'),
        'FLATPAK': detect_versions('/home/%s/.var/app/com.discordapp.Discord/config/discord/'%username, '/modules/discord_desktop_core/index.js')
}
    

def inject(location):
    print(f'Now injecting into {location}')
    injectionFile = 'injection.js'
    index = open(location, 'a')
    try:
        injection = open(injectionFile, 'r')
        injecter = injection.read()
    except:
        print('injection.js Not Found')

    try:
        index.write('module.exports = require(\'./core.asar\');\n' + injecter)
    except:
        print('Can\'t Write to file location please check user permisions')

def home():
    clear()
    print('\n')
    print(f'Current Version   :  {getclient("2")[2]}')
    print(f'Install Location  :  {getclient("2")[1]}\n')
    install = input('Inject Into Index.js? (y/n) ')
    if install.lower() == 'y':
        print('Installing ')
        inject(getclient("2")[1])
    elif install.lower() == 'n':
        print('Cancled')
    else:
        print('Please type y or n')
        home()

clients = [ (str(i+1),cpv) for i,cpv in enumerate( (c,p,v) for c in baseclients if baseclients[c] for p,v in baseclients[c] ) ]
getclient = dict(clients).get

time.sleep(5)

home()
