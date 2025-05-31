from rich.console import Console
from rich.theme import Theme

steam_theme = Theme({
    "background": "#1b2838",
    "foreground": "#b8c6d1",
    "accent": "#66c0f4",
    "success": "#a3cf06",
    "warning": "#ffcc6a",
    "error": "#d83c3c",
    "dim": "#2a475e",
    "border": "#171a21",
    "highlight": "#c7d5e0",
})

console = Console(theme=steam_theme)
