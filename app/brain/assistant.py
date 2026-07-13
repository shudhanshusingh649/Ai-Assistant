from app.voice.speech import speak
from app.brain.ollama_ai import ask_ai
from app.memory.memory import remember, recall


def process_command(command):

    command = command.lower().strip()

    # -----------------------------
    # Remember command
    # Example:
    # remember college is IIT Patna
    # -----------------------------
    if command.startswith("remember"):

        try:
            data = command.replace("remember", "").strip()

            key, value = data.split(" is ", 1)

            remember(key.strip(), value.strip())

            speak(f"Okay Sir. I will remember that your {key} is {value}.")

        except:
            speak("Please say it like remember college is IIT Patna.")

        return

    # -----------------------------
    # Recall command
    # Example:
    # what is my college
    # -----------------------------
    if command.startswith("what is my"):

        key = command.replace("what is my", "").strip()

        value = recall(key)

        if value:
            speak(f"Your {key} is {value}.")
        else:
            speak(f"I don't know your {key} yet.")

        return

    # -----------------------------
    # Basic Commands
    # -----------------------------
    if "hello" in command:
        speak("Hello Sir.")
        return

    if "your name" in command:
        speak("My name is Nexa.")
        return

    if "how are you" in command:
        speak("I am doing great.")
        return

    # -----------------------------
    # AI Response
    # -----------------------------
    print("🧠 NEXA Thinking...")

    answer = ask_ai(command)

    print(answer)

    speak(answer)