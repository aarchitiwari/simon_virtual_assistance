import time

import speech_recognition as sr
import pyttsx3
import pywhatkit
import datetime
import wikipedia
import pyjokes
import wolframalpha
import webbrowser
from ecapture import ecapture as ec

listener = sr.Recognizer()
engine = pyttsx3.init()


def talk(text):
    engine.say(text)
    engine.runAndWait()


def take_command():
    try:
        with sr.Microphone() as source:
            # talk("Hii, What Can i do for you")
            print('Listening...')
            voice = listener.listen(source)
            command = listener.recognize_google(voice)
            command = command.lower()
            if 'symon' in command:
                command = command.replace('symon', '')
                print(command)
    except:
        pass
    return command

def wishMe():
    hour =datetime.datetime.now().hour
    if hour>=0 and hour<12:
        talk("Hello, Good Morning. How may I help you")
        print("Hello, Good Morning")
    elif hour>=12 and hour<18:
        talk("Hello, Good Afternoon. How may I help you")
        print("Hello, Good Afternoon")
    else:
        talk("Hello, Good Evening. How may I help you")
        print("Hello, Good Evening")


def run_symon():
    command = take_command()
    print(command)
    if 'play' in command:
        song = command.replace('play', '')
        talk('playing ' + song)
        pywhatkit.playonyt(song)
    elif 'time' in command:
        time = datetime.datetime.now().strftime('%I:%M %p')
        talk('Current time is ' + time)
    elif 'who the heck is' in command:
        person = command.replace('who the heck is', '')
        info = wikipedia.summary(person, 1)
        print(info)
        talk(info)
    elif 'date' in command:
        talk('sorry, I have a headache')
    elif 'are you single' in command:
        talk('I am in a relationship with wifi')

    elif 'joke' in command:
        talk(pyjokes.get_joke())
        print(pyjokes.get_joke())
    elif 'ask' in command:
        talk('I can answer computational and geographical questions')
        question = take_command()
        app_id = "tanvigh45@gmail.com"
        client = wolframalpha.Client('R2K75H-7ELALHR35X')
        res = client.query(question)
        answer = next(res.results).text
        talk(answer)
        print(answer)
    elif 'information' in command:
        talk('Searching Wikipedia.....')
        command = command.replace("Wikipedia", "")
        results = wikipedia.summary(command, sentences=3)
        talk('According to Wikipedia')
        print(results)
        talk(results)
    elif 'news' in command:
        news = webbrowser.open_new_tab("https://m.timesofindia.com/")
        talk("Here are some of the Headlines from Times of india, Happy Reading")
        print(news)
    elif 'search' in command:
        command = command.replace("search", "")
        webbrowser.open_new_tab(command)
    elif 'Open youtube' in command:
        webbrowser.open_new_tab("https://www.youtube.com/")
        talk("youtube is open now")
    elif 'open google' in command:
        webbrowser.open_new_tab('https://google.com/')
        talk('Google is open now')
    elif 'open gmail' in command:
        webbrowser.open_new_tab("https://mail.google.com/mail/")
        talk("Gmail is open now")
    elif 'name' in command:
        talk("My name is symon")
        print("My name is symon")
    elif 'who are you' and 'what can you do' in command:
        talk('I am Symon, Your personal assistant. I am programmed to minor tasks like playing Song, Predict time, Search Wikipedia and answer computational question.')
        print('I am Symon, Your personal assistant. I am programmed to minor tasks like playing Song, Predict time, Search Wikipedia and answer computational question.')
    elif 'made' or 'created' in command or 'discovered' in command:
        talk('I was build by "Aarchi Tiwari"')
        print('I was build by "Aarchi Tiwari"')
    else:
        talk('Please say the command again.')


while True:
    wishMe()
    run_symon()
    time.sleep(56)