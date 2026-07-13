from app.voice.listen import listen
from app.voice.speech import speak
from app.brain.router import route

from app.wakeword.wake import is_wake_word
from app.memory import session

while True:

    command = listen()

    if command == "":
        continue

    # Waiting for Wake Word
    if not session.conversation_active:

        if is_wake_word(command):

            session.conversation_active = True
            speak("Yes Sir. I am listening.")

        continue

    # Conversation Mode

    if "go to sleep" in command or "sleep" in command:

        speak("Okay Sir. Going back to sleep.")
        session.conversation_active = False
        continue

    route(command)