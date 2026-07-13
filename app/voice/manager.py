import threading

is_speaking = False
stop_requested = False
current_answer = ""
current_index = 0

speech_thread = None