"""
A dictionary that maps Todoist color codes to
ANSI escape sequence colors.

Visit https://developer.todoist.com/sync/v8/#colors
to see the colors and code supported by Todoist.
"""
COLOR = {
    30: '\u001b[38;5;53m ',
    31: '\u001b[38;5;196m ',
    32: '\u001b[38;5;208m ',
    33: '\u001b[38;5;220m ',
    34: '\u001b[38;5;106m ',
    35: '\u001b[38;5;40m ',
    36: '\u001b[38;5;28m ',
    37: '\u001b[38;5;79m ',
    38: '\u001b[38;5;30m ',
    39: '\u001b[38;5;33m ',
    40: '\u001b[38;5;117m ',
    41: '\u001b[38;5;26m ',
    42: '\u001b[38;5;92m ',
    43: '\u001b[38;5;129m ',
    44: '\u001b[38;5;176m ',
    45: '\u001b[38;5;198m ',
    46: '\u001b[38;5;210m ',
    47: '\u001b[38;5;245m ',
    48: '\u001b[38;5;253m ',
    49: '\u001b[38;5;137m ',
    'RESET': '\u001b[0m',
    'BOLD': '\u001b[1m',
    'UNDERLINE': '\u001b[4m',
    'REVERSED': '\u001b[7m'
}
