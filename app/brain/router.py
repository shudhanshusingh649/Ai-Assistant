from app.automation.system import system_commands
from app.automation.browser import browser_commands
from app.automation.search import google_search
from app.brain.assistant import process_command
from app.automation.screenshot import take_screenshot


def route(command):

    command = command.lower()

    if "youtube" in command or "google" in command or "github" in command or "gmail" in command:

        browser_commands(command)

    elif "search" in command:

        query = command.replace("search", "").strip()

        google_search(query)

    elif "screenshot" in command:

        take_screenshot()

    elif "open" in command:

        system_commands(command)

    else:

        process_command(command)