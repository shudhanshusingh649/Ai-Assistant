import subprocess

from app.voice.speech import speak
from app.automation.registry import APPS


def system_commands(command):

    command = command.lower()

    # -------------------------
    # OPEN APPS
    # -------------------------
    for app, actions in APPS.items():

        if app in command:

            if any(word in command for word in [
                "open",
                "start",
                "launch"
            ]):

                speak(f"Opening {app.title()}.")

                subprocess.Popen(
                    actions["open"],
                    shell=True
                )

                return True

            if any(word in command for word in [
                "close",
                "exit",
                "stop"
            ]):

                speak(f"Closing {app.title()}.")

                subprocess.run(
                    actions["close"] + " >nul 2>&1",
                    shell=True
                )

                return True

    return False