from app.brain.intent import detect_intent

from app.automation.system import system_commands
from app.automation.browser import browser_commands
from app.automation.search import google_search
from app.automation.screenshot import take_screenshot

from app.brain.assistant import process_command


def route(command):

    intent = detect_intent(command)

    # -------------------------
    # Open Applications
    # -------------------------
    if intent == "open":

        system_commands(command)

    # -------------------------
    # Close Applications
    # -------------------------
    elif intent == "close":

        system_commands(command)

    # -------------------------
    # Browser Commands
    # -------------------------
    elif intent == "browser":

        browser_commands(command)

    # -------------------------
    # Google Search
    # -------------------------
    elif intent == "search":

        query = (
            command.replace("search", "")
            .replace("google", "")
            .strip()
        )

        google_search(query)

    # -------------------------
    # Screenshot
    # -------------------------
    elif intent == "screenshot":

        take_screenshot()

    # -------------------------
    # Memory + AI
    # -------------------------
    else:

        process_command(command)