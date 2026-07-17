def detect_intent(command):

    command = command.lower()

    if any(word in command for word in [
        "open",
        "start",
        "launch"
    ]):
        return "open"

    if any(word in command for word in [
        "close",
        "exit",
        "stop"
    ]):
        return "close"

    if any(word in command for word in [
        "search",
        "google"
    ]):
        return "search"

    if any(word in command for word in [
        "youtube",
        "github",
        "gmail"
    ]):
        return "browser"

    if "screenshot" in command:
        return "screenshot"

    if command.startswith("remember"):
        return "memory"

    if command.startswith("what is my"):
        return "recall"

    return "ai"