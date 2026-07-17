import time

from app.voice.listen import listen
from app.voice.speech import speak
from app.brain.router import route

from app.wakeword.wake import is_wake_word
from app.core.conversation import conversation


while True:

    # Auto sleep after inactivity
    if conversation.timeout(30):
        speak("Going to sleep.")
        conversation.sleep()

    command = listen()

    if command == "":
        continue

    # -------------------------
    # Waiting for Wake Word
    # -------------------------
    if not conversation.is_awake():

        if is_wake_word(command):

            conversation.wake()

            speak("Yes Sir. I am listening.")

        continue

    # -------------------------
    # Ignore wake word again
    # -------------------------
    if command in ["nexa", "hey nexa"]:
        continue

    # -------------------------
    # Sleep Command
    # -------------------------
    if "go to sleep" in command or "sleep" in command:

        speak("Okay Sir.")

        conversation.sleep()

        continue

    # Update timer
    conversation.update()

    # Execute command
    route(command)

    time.sleep(0.3)