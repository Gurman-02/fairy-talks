import gtts
import os
import playsound

def textToSpeech(text):
    my_text=text
    sound = gtts.gTTS(text=my_text, lang='en', slow=False)
    sound.save('welcome.mp3') 
    playsound.playsound('welcome.mp3', True)   
    os.remove('welcome.mp3')

# textToSpeech('hellooooo')

# textToSpeech('again i am here')

# textToSpeech('once again hellooo!')