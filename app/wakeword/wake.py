WAKE_WORDS = [
    "hey nexa",
    "nexa",
    "hello nexa"
]


def is_wake_word(text):

    text = text.lower()

    for word in WAKE_WORDS:

        if word in text:
            return True

    return False