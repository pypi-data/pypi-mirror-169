from colorama import Fore, Style, init
init()

__version__ = "1.6.6"

def cprint(text, color, end='\n'):
    if len(str(text).strip()) == 0: return
    fore = getattr(Fore, color.upper())
    print('{0}{1}{2}'.format(fore, text, Style.RESET_ALL), end=end)

def color(text, color, style='Normal'):
    fore = getattr(Fore, color.upper())
    style = getattr(Style, style.upper())
    return '{0}{1}{2}{3}'.format(fore, style, text, Style.RESET_ALL)
