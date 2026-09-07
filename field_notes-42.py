# === Stage 42: Добавь цветной вывод через ANSI-коды с возможностью отключения ===
# Project: FieldNotes
ANSI = {
    'reset': '\033[0m',
    'bold': '\033[1m',
    'dim': '\033[2m',
    'red': '\033[31m',
    'green': '\033[32m',
    'yellow': '\033[33m',
    'blue': '\033[34m',
    'magenta': '\033[35m',
    'cyan': '\033[36m',
    'white': '\033[37m',
    'bg_red': '\033[41m',
    'bg_green': '\033[42m',
    'bg_yellow': '\033[43m',
    'bg_blue': '\033[44m',
}

def colorize(text, code, enable=True):
    if not enable:
        return text
    return ANSI[code] + text + ANSI['reset']
