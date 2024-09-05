import speech_recognition as sr
# import pyaudio
import streamlit as st
def record_query():
    r=sr.Recognizer()
    mic=sr.Microphone()
    with mic as source:
        st.write('Listening...start speaking')
        audio=r.listen(source)
    st.write('Processing')
    try:
        text = r.recognize_google(audio)
        return text
    except sr.UnknownValueError:
        st.write("Sorry, I couldn't understand you.")
        return 'no speech captured'
    except sr.RequestError as e:
        st.write(f"Could not request results from Google Speech Recognition service; {e}")
        return 'no speech captured'



if 'name'=='__main__':
    record_query()








