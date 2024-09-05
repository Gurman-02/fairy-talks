
# import streamlit as st
# import base64
# import pyttsx3
# import speechtotext as stt
# import json
# import threading
# import pickle




# engine = pyttsx3.init()
# engine.setProperty('voice', 'HKEY_LOCAL_MACHINE\SOFTWARE\Microsoft\Speech\Voices\Tokens\TTS_MS_EN-US_ZIRA_11.0')
# engine.setProperty('rate', 140)

# # path = 'bg3.gif'
# path='images/new-bg.gif'

# file_ = open(path, "rb")
# contents = file_.read()
# data_url = base64.b64encode(contents).decode("utf-8")
# file_.close()

# path_character_talking = 'images/2-talking-unscreen.gif'  
# path_character_listening = 'images/listening1-unscreen.gif'


# is_speaking = False

# page_bg = f"""
# <style>
# [data-testid="stApp"] {{
#     opacity: 0.8;
#     background-color: #d5d9c7;
#     background-image: url('data:image/gif;base64,{data_url}');
#     background-repeat: no-repeat;
#     background-size: cover;
#     background-attachment: fixed;
# }}
# [data-testid='stHeader']{{ 
#     background: rgba(0,0,0,0); 
# }}
# [data-testid="stButton"] {{
#     position: fixed;
#     top:80%;
#     left: 70%  !important;
#     transform: translateX(-50%);
#     z-index: 1;
# }}
# </style>
# """

# image_char = f"""
# <style>
# [data-testid="stImage"] {{
#     position:absolute;
#     z-index: 1;
#     width:100px;
#     right:90% !important;
#     padding-top:100px;
#     padding-right:200px;
# }}
# </style>
# """


# st.markdown(page_bg,unsafe_allow_html=True)

# st.markdown(image_char,unsafe_allow_html=True)

# #----------------------footer-------------
# from htbuilder import HtmlElement, div, ul, li, br, hr, a, p, img, styles, classes, fonts
# from htbuilder.units import percent, px
# from htbuilder.funcs import rgba, rgb


# def image(src_as_string, **style):
#     return img(src=src_as_string, style=styles(**style))


# def link(link, text, **style):
#     return a(_href=link, _target="_blank", style=styles(**style))(text)


# def layout(*args):

#     style = """
#     <style>
#       # MainMenu {visibility: hidden;}
#       footer {visibility: hidden;}
     
#     </style>
#     """

#     style_div = styles(
#         position="fixed",
#         left=0,
#         bottom=0,
#         margin=px(0, 0, 0, 0),
#         width=percent(100),
#         color="white",
#         text_align="center",
#         justify_content='center',
#         height="auto",
#         opacity=1,
#     )

#     style_hr = styles(
#         display="block",
#         margin=px(0, 0, 0, 0),
#         border_style="inset",
#         border_width=px(2)
#     )

#     body = p()
#     foot = div(
#         style=style_div
#     )(
#         hr(
#             style=style_hr
#         ),
#         body
#     )

#     st.markdown(style, unsafe_allow_html=True)

#     for arg in args:
#         if isinstance(arg, str):
#             body(arg)

#         elif isinstance(arg, HtmlElement):
#             body(arg)

#     st.markdown(str(foot), unsafe_allow_html=True)


# def footer():
#     myargs = [
#         link('https://gurman-02.github.io/about-me-fairy-talk/','About Me'),
#         "&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;",
#         "Made in ",
#         image('https://avatars3.githubusercontent.com/u/45109972?s=400&v=4',
#               width=px(25), height=px(25)),
#         " with ❤️ by Gurman ",
#         "&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;",
#         # 'Gurman',
#         # br(),
#         # link("https://buymeacoffee.com/chrischross", image('https://i.imgur.com/thJhzOO.png')),
#         # link('dashboard','Statistics')
#     ]
#     layout(*myargs)
# footer()





# #---------------------first character--------------------

# character_image = st.image(path_character_listening, use_column_width=True)

# def switch_character_gif(is_speaking):
#     if is_speaking:
#         character_image.image(path_character_talking, use_column_width=True)
#     else:
#         character_image.image(path_character_listening, use_column_width=True)

# # def on_finish(name, completed):
# #     global is_speaking
# #     is_speaking = False
# #     switch_character_gif(is_speaking)


# # engine.connect('finished-utterance', on_finish)


# #---for first charcter---
# # def speaks(text,fairy):
# #     if fairy=='one':
# #         global is_speaking
# #         is_speaking = True
# #         switch_character_gif(is_speaking)
# #         engine.say(text)
# #         engine.runAndWait()
# #         is_speaking = False
# #         switch_character_gif(is_speaking)
# #     else:
# #         engine.say(text)
# #         engine.runAndWait()



# # speaks("Welcome i am first fairy")

# # if 'first_run' not in st.session_state:
# #     st.session_state['first_run'] = True
# #     speaks("Welcome i am first fairy")  # This will only run on the initial script execution



# #--for second and third character
# # def speak(text):
# #     engine.say(text)
# #     engine.runAndWait()







# def run_speech(text):
#     engine.say(text)
#     engine.runAndWait()

# def speaks(text):
#     global is_speaking
#     is_speaking = True
#     switch_character_gif(is_speaking)
#     thread = threading.Thread(target=run_speech, args=(text,))
#     thread.start()

# def speak(text):
#     thread = threading.Thread(target=run_speech, args=(text,))
#     thread.start()



# # #----------------second character--------------------


# second_character_container = st.markdown("", unsafe_allow_html=True)

# def display_and_speak_second_character(text):
#     image2 = 'images/Untitled-design-2--unscreen.gif'
#     with open(image2, 'rb') as f:
#         image_data_2 = base64.b64encode(f.read()).decode('utf-8')

#     character_2_style = f"""
#     <div id="second-character-container" style="
#         position: fixed;
#         top: 14.5%;
#         left: 57%;
#         transform: rotate(30deg);
#         z-index: 1;
#         height: 100px;
#         width: 200px;
#         background-image: url('data:image/gif;base64,{image_data_2}');
#         background-size: cover;
#     "></div>
#     """

   
#     second_character_container.markdown(character_2_style, unsafe_allow_html=True)
#     # speaks(text,'two')
#     speak(text)
#     second_character_container.markdown("", unsafe_allow_html=True)


# # display_and_speak_second_character("Hello, I am the second character.")







# # #3rd charcater-----------------


# third_character_container = st.empty()

# def display_and_speak_third_character(text):
#     image3 = 'fairy3.gif'
#     with open(image3, 'rb') as f:
#         image_data_3 = base64.b64encode(f.read()).decode('utf-8')

#     character_3_style = f"""
#         <style>
#         [data-testid="stMarkdownContainer"] {{
#             position: fixed;
#             left: 5%;
#             bottom: 25%;
#             z-index: 1;
#             height: 300px;
#             width: 300px;
#             background-image: url('data:image/gif;base64,{image_data_3}');
#             background-size: contain;
#             background-repeat: no-repeat;
#         }}
#         </style>
#     """

#     third_character_container.markdown(character_3_style, unsafe_allow_html=True)
#     # speaks(text,'three')
#     speak(text)
#     third_character_container.empty()


# # display_and_speak_third_character("Hello there, I am the third character. I will now appear, speak and then disappear.")



# #---recorder----

# import speechtotext as stt
# from audio_recorder_streamlit import audio_recorder
# import speech_recognition as sr
# import streamlit as st
# from io import BytesIO


# recorder_style=f"""
# <style>
# [data-testid="column"] {{
#     position: fixed;
#     top:80%;
#     left: 50%;
#     z-index: 1;
#     background:rgb(0,0,0);
#     width:38px;
# }}
# </style>
# """

# st.markdown(recorder_style, unsafe_allow_html=True)



# #---func for speech to text--------
# def record_query():
#     r = sr.Recognizer()

#     col1, col2, col3 = st.columns((6, 1, 6))
#     with col2:
#         audio_bytes = audio_recorder(text='', recording_color='94FFD8', neutral_color="FFC700")

#     if audio_bytes:
#         audio_wav = BytesIO(audio_bytes)
#         with sr.AudioFile(audio_wav) as source:
#             audio_data = r.record(source)

#         try:
#             text = r.recognize_google(audio_data)
#             return text
#         except sr.UnknownValueError:
#             # st.write("Sorry, I couldn't understand you.")
#             return 'no speech captured 1'
#         except sr.RequestError as e:
#             # st.write(f"Could not request results from Google Speech Recognition service; {e}")
#             return 'no speech captured 2'

#     return 'no speech captured 3'


# # question=record_query()
# # st.write('recorded----',question)


# # def spacy_lemmatize(text):
# #     doc = nlp(text)
# #     return ' '.join([token.lemma_ for token in doc])

# # import spacy
# # nlp = spacy.load("en_core_web_sm")

# # model=pickle.load(open('sentiment.pkl','rb'))
# # sent=model.predict([question])
# # st.write('sentiment---->', sent)

# if 'first_run' not in st.session_state:
#     st.session_state['first_run'] = True
#     # speaks("Welcome i am first fairy", 'one')  # This will only run on the initial script execution
#     speaks('welcome i am first fairy')

# def check_which_fairy(sent, response):
#     if sent=='neutral':
#         speaks(response)
#     elif sent=='negative':
#         display_and_speak_second_character(response)
#     else:
#         display_and_speak_third_character(response)





# # def starting():
    
# #     question=record_query()
# #     st.write('recorded----',question)
# #     #--will do sentimnet anylsis
# #     sent='positive'
# #     #--get response from fine tuned model
# #     response='this is the response a b c d e f g h i j k l '
# #     check_which_fairy(sent,response)

# # starting()

# def starting():
#     question = record_query()
#     st.write('recorded----', question)
#     # --will do sentiment analysis
#     sent = 'positive'
#     # --get response from fine-tuned model
#     response = 'this is the response a b c d e f g h i j k l '
#     check_which_fairy(sent, response)

# Move the call to starting() outside the script body
# if __name__ == "__main__":
#     if st.button("Start"):
#         starting()








import streamlit as st
import base64
import pyttsx3
import speechtotext as stt
import json
import threading
import pickle
from audio import textToSpeech as tts




path='images/new-bg.gif'

file_ = open(path, "rb")
contents = file_.read()
data_url = base64.b64encode(contents).decode("utf-8")
file_.close()

path_character_talking = 'images/2-talking-unscreen.gif'  
path_character_listening = 'images/listening1-unscreen.gif'


is_speaking = False

page_bg = f"""
<style>
[data-testid="stApp"] {{
    opacity: 0.8;
    background-color: #d5d9c7;
    background-image: url('data:image/gif;base64,{data_url}');
    background-repeat: no-repeat;
    background-size: cover;
    background-attachment: fixed;
}}
[data-testid='stHeader']{{ 
    background: rgba(0,0,0,0); 
}}
[data-testid="stButton"] {{
    position: fixed;
    top:80%;
    left: 70%  !important;
    transform: translateX(-50%);
    z-index: 1;
}}
</style>
"""

image_char = f"""
<style>
[data-testid="stImage"] {{
    position:absolute;
    z-index: 1;
    width:100px;
    right:90% !important;
    padding-top:100px;
    padding-right:200px;
}}
</style>
"""


st.markdown(page_bg,unsafe_allow_html=True)

st.markdown(image_char,unsafe_allow_html=True)




#----------------------footer-------------
from htbuilder import HtmlElement, div, ul, li, br, hr, a, p, img, styles, classes, fonts
from htbuilder.units import percent, px
from htbuilder.funcs import rgba, rgb


def image(src_as_string, **style):
    return img(src=src_as_string, style=styles(**style))


def link(link, text, **style):
    return a(_href=link, _target="_blank", style=styles(**style))(text)


def layout(*args):

    style = """
    <style>
      # MainMenu {visibility: hidden;}
      footer {visibility: hidden;}
     
    </style>
    """

    style_div = styles(
        position="fixed",
        left=0,
        bottom=0,
        margin=px(0, 0, 0, 0),
        width=percent(100),
        color="white",
        text_align="center",
        justify_content='center',
        height="auto",
        opacity=1,
    )

    style_hr = styles(
        display="block",
        margin=px(0, 0, 0, 0),
        border_style="inset",
        border_width=px(2)
    )

    body = p()
    foot = div(
        style=style_div
    )(
        hr(
            style=style_hr
        ),
        body
    )

    st.markdown(style, unsafe_allow_html=True)

    for arg in args:
        if isinstance(arg, str):
            body(arg)

        elif isinstance(arg, HtmlElement):
            body(arg)

    st.markdown(str(foot), unsafe_allow_html=True)


# def footer():
#     myargs = [
#         link('https://gurman-02.github.io/about-me-fairy-talk/','About Me'),
#         "&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;",
#         "Made in ",
#         image('https://avatars3.githubusercontent.com/u/45109972?s=400&v=4',
#               width=px(25), height=px(25)),
#         " with ❤️ by Gurman ",
#         "&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;",
#         # 'Gurman',
#         # br(),
#         # link("https://buymeacoffee.com/chrischross", image('https://i.imgur.com/thJhzOO.png')),
#         # link('dashboard','Statistics')
#     ]
#     layout(*myargs)
# footer()



#-------recorder-------

import speechtotext as stt
from audio_recorder_streamlit import audio_recorder
import speech_recognition as sr
import streamlit as st
from io import BytesIO
from sentiment import sentPrediction
import time
from response import getResponse


recorder_style=f"""
<style>
[data-testid="column"] {{
    position: fixed;
    top:80%;
    left: 50%;
    z-index: 1;
    background:rgb(0,0,0);
    width:38px;
}}
</style>
"""

st.markdown(recorder_style, unsafe_allow_html=True)




#---------------------first character--------------------

character_image = st.image(path_character_listening, use_column_width=True)

def switch_character_gif(is_speaking):
    if is_speaking:
        character_image.image(path_character_talking, use_column_width=True)
    else:
        character_image.image(path_character_listening, use_column_width=True)

def on_finish():
    global is_speaking
    is_speaking = False
    switch_character_gif(is_speaking)


# def welcome():
#     global is_speaking 
#     is_speaking=True
#     switch_character_gif(is_speaking)
#     tts("Welcome to the enchanted realm! I am your whimsical fairy guide. Here amidst the magical wonder, your curiosity will find endless delight! Let's embark on this journey together")
#     on_finish()


# welcome()

if 'welcome_played' not in st.session_state:
    st.session_state.welcome_played = False

def welcome():
    if not st.session_state.welcome_played:
        global is_speaking
        is_speaking = True
        switch_character_gif(is_speaking)
        tts("Welcome to the enchanted realm! I am your whimsical fairy guide. Here amidst the magical wonder, your curiosity will find endless delight! Let's embark on this journey together")
        on_finish()
        st.session_state.welcome_played = True

welcome()


# #----------------second character--------------------


second_character_container = st.markdown("", unsafe_allow_html=True)

def display_and_speak_second_character(text):
    image2 = 'images/Untitled-design-5--unscreen.gif'
    with open(image2, 'rb') as f:
        image_data_2 = base64.b64encode(f.read()).decode('utf-8')

    character_2_style = f"""
    <div id="second-character-container" style="
        position: fixed;
        top: 10%;
        left: 57%;
        transform: rotate(35deg);
        z-index: 1;
        height: 150px;
        width: 220px;
        background-image: url('data:image/gif;base64,{image_data_2}');
        background-size: cover;
    "></div>
    """
    # character_2_style = f"""
    # <div id="second-character-container" style="
    #     position: fixed;
    #     top: 14.5%;
    #     left: 57%;
    #     transform: rotate(30deg);
    #     z-index: 1;
    #     height: 100px;
    #     width: 200px;
    #     background-image: url('data:image/gif;base64,{image_data_2}');
    #     background-size: cover;
    # "></div>
    # """

   
    second_character_container.markdown(character_2_style, unsafe_allow_html=True)
    # speaks(text,'two')
    time.sleep(2)
    tts(text)
    second_character_container.markdown("", unsafe_allow_html=True)


# display_and_speak_second_character("Hello, I am the second character.")







# #3rd charcater-----------------


third_character_container = st.empty()

def display_and_speak_third_character(text):
    image3 = 'fairy3.gif'
    with open(image3, 'rb') as f:
        image_data_3 = base64.b64encode(f.read()).decode('utf-8')

    character_3_style = f"""
        <style>
        [data-testid="stMarkdownContainer"] {{
            position: fixed;
            left: 5%;
            bottom: 25%;
            z-index: 1;
            height: 300px;
            width: 300px;
            background-image: url('data:image/gif;base64,{image_data_3}');
            background-size: contain;
            background-repeat: no-repeat;
        }}
        </style>
    """

    third_character_container.markdown(character_3_style, unsafe_allow_html=True)
    time.sleep(2)
    # speaks(text,'three')
    tts(text)
    third_character_container.empty()


# display_and_speak_third_character("Hello there, I am the third character. I will now appear, speak and then disappear.")








#---func for speech to text--------
def record_query():
    r = sr.Recognizer()

    col1, col2, col3 = st.columns((6, 1, 6))
    with col2:
        audio_bytes = audio_recorder(text='', recording_color='94FFD8', neutral_color="FFC700")

    if audio_bytes:
        audio_wav = BytesIO(audio_bytes)
        with sr.AudioFile(audio_wav) as source:
            audio_data = r.record(source)

        try:
            text = r.recognize_google(audio_data)
            return text
        except sr.UnknownValueError:
            # st.write("Sorry, I couldn't understand you.")
            return 'no speech captured'
        except sr.RequestError as e:
            # st.write(f"Could not request results from Google Speech Recognition service; {e}")
            return 'no speech captured'

    return 'no speech captured'




def check_which_fairy(sent, response):
    if sent=='neutral':
        global is_speaking
        is_speaking=True
        switch_character_gif(is_speaking)
        tts(response)
        on_finish()
    elif sent=='positive':
        display_and_speak_second_character(response)
    else:
        display_and_speak_third_character(response)






def starting():
    question = record_query()
    print('recorded----', question)
    #sentiment analysis
    sent = sentPrediction(question)
    print('sentiment--', sent)
    # --get response from fine-tuned model
    if not question=='no speech captured':
        response = getResponse(question)
        check_which_fairy(sent, response)



starting()










#--------footer------------
def footer():
    myargs = [
        link('https://gurman-02.github.io/about-me-fairy-talk/','About Me'),
        "&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;",
        "Made in ",
        image('https://avatars3.githubusercontent.com/u/45109972?s=400&v=4',
              width=px(25), height=px(25)),
        " with ❤️ by Gurman ",
        "&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;",
        # 'Gurman',
        # br(),
        # link("https://buymeacoffee.com/chrischross", image('https://i.imgur.com/thJhzOO.png')),
        # link('dashboard','Statistics')
    ]
    layout(*myargs)
footer()