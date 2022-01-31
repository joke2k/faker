from .codes import codes


def unidecode(txt: str) -> str:
    chars = ""
    for ch in txt:
        codepoint = ord(ch)

        if not codepoint:
            chars += "\x00"
            continue

        try:
            chars += codes[codepoint - 1]
        except IndexError:
            pass
    return chars
