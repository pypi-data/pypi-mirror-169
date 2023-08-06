"""Style declarations for log messages & other things."""

import fontawesome as fai
from chalky import Chalk, bg, fg, hex
from chalky.color import Color
from chalky.style import Style

# Too much custom
ghost = hex("#f8f8ff", background=False)
gray65 = hex("#a6a6a6", background=False)
gray09 = hex("#171717")

# Composition
fg = {
    "w": gray65,  # Chalk(foreground=Color.WHITE),
    "g": Chalk(foreground=Color.BRIGHT_GREEN),
    "r": Chalk(foreground=Color.RED),
    "b": Chalk(foreground=Color.BLUE),
}

bg = {"g9": gray09}

weight = {
    "it": Chalk(style={Style.ITALIC}),
    "b": Chalk(style={Style.BOLD}),
    "s": Chalk(style={Style.STRIKETHROUGH}),
    "t": Chalk(style={Style.SLOW_BLINK}),
}

# print(custom_rgb | "Potential link text")
# print(custom_hex | "Black on green text")

# Exports
get_andlog_fmt = lambda: fg["b"] & weight["b"]
get_orlog_fmt = lambda: fg["w"] + weight["it"] + bg["g9"]
