import threading

voice_thread = None


def start(target, *args):

    global voice_thread

    if voice_thread and voice_thread.is_alive():
        return

    voice_thread = threading.Thread(
        target=target,
        args=args,
        daemon=True
    )

    voice_thread.start()


def is_running():

    global voice_thread

    return voice_thread is not None and voice_thread.is_alive()