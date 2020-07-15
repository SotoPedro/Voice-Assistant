import speech_recognition as sr
import webbrowser
import time
import playsound
import os
import random
from gtts import gTTS
from time import ctime

r = sr.Recognizer()

def recordAudio(ask=False):
    with sr.Microphone() as source:        
        if ask:
            Jarvis_Speak(ask)
        audio = r.listen(source)
        voice_data = ''
        try: 
            voice_data = r.recognize_google(audio)            
        except sr.UnknownValueError:
            Jarvis_Speak('Sorry, I did not get that')
        except sr.RequestError:
            Jarvis_Speak('Sorry, my speech service is down')
        return voice_data

def Jarvis_Speak(audio_string):
    tts = gTTS(text=audio_string,lang='en') #change the language whenever i want
    r = random.randint(1,1000000)
    audio_file = 'auido-dash' + str(r) + '.mp3'
    tts.save(audio_file)
    playsound.playsound(audio_file)
    print(audio_string)
    os.remove(audio_file)


def respond(voice_data): 
    if 'what is your name' in voice_data:
        Jarvis_Speak('My name is Jarvis')
    if 'what time is it' in voice_data:
        Jarvis_Speak(ctime())
    if 'search' in voice_data:
        search = recordAudio('What do you want to search for?')
        url = 'https://google.com/search?q=' + search
        webbrowser.get().open(url)
        Jarvis_Speak('Here is what i found for ' + search)
    if 'find location' in voice_data:
        location = recordAudio('What place are you looking for?')
        url = 'https://google.nl/maps/place/' + location + '/&amp;'
        webbrowser.get().open(url)
        Jarvis_Speak('Here is the location of ' + location)
    if 'play a video' in voice_data:
        video = recordAudio('What is title of the video?')
        url = 'https://www.youtube.com/watch?v='+video
        webbrowser.get().open(url)
        Jarvis_Speak('Here is the video of ' + video)
    if 'exit' in voice_data:
        Jarvis_Speak('Thank you, see u later')
        exit()
    


time.sleep(1)
Jarvis_Speak('How can i help you?')
while 1:        
    voice_data = recordAudio()
    respond(voice_data)



