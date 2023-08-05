
dict: dict[str, list[str]] = {
    "yes": ["yes", "y", "yes!", "ja"],
    "no": ["no" "n", "no!", "nej"],
    "cancel":  ["cancel", "cancel!"],
    "stop": ["stop", "stop!"]
}


def s(word: str) -> str:
    word = word.lower()

    for short_word in dict:
        if word in dict[short_word]:
            word = short_word

    return word


def sf(word:str) -> str:

    if word == s(word):
        raise NameError
    else:
        return word

# _0884
