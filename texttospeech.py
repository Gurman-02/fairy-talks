
import pyttsx3

engine = None
engine_running = False

def engine_start():
    global engine, en
    if engine is None:
        engine = pyttsx3.init()
        engine.setProperty('voice', 'HKEY_LOCAL_MACHINE\SOFTWARE\Microsoft\Speech\Voices\Tokens\TTS_MS_EN-US_ZIRA_11.0')
        engine.setProperty('rate', 140)
        engine_running = True










def speak(text):
    global engine, engine_running
    if engine is not None:
        if engine_running:
            engine.stop()
        engine.say(text)
        try:
            engine.runAndWait()
        except RuntimeError:
            pass
        engine_running = False
        
    else:
        engine_start()
        engine.say(text)
        engine.runAndWait()
        engine_running = False
