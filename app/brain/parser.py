def parse_command(command):

    command = command.lower().strip()

    fillers = [
        "please",
        "could you",
        "can you",
        "kindly",
        "nexa",
        "hey",
        "jarvis"
    ]

    for word in fillers:
        command = command.replace(word, "")

    command = " ".join(command.split())

    return command