import speech_recognition as sr
import pyttsx3
import webbrowser
import time
import datetime
import speedtest
import pywhatkit
import wikipedia

r = sr.Recognizer()
engine = pyttsx3.init()
voices = engine.getProperty('voices')
engine.setProperty('voice',voices[1].id)
engine.say('Hey boss')
engine.say('i am your jarvis')
engine.say('try saying something')
engine.runAndWait()

amazon_url = 'https://www.amazon.in'
instagram_url = 'https://www.instagram.com'
linkedin_url = 'https://www.linkedin.com/feed'
gmail_url = 'https://mail.google.com/mail/u/0/#inbox'
weather_url = 'https://openweathermap.org/city/1264527'

def bot(command):
    if command == 'hi jarvis' or command == 'hello jarvis' or command == 'hey jarvis':
        talk('hello boss')
        talk('how was your day  boss')
    elif command == 'good':
        talk('good to hear boss')
        talk('how can i help you ')

def web(website):
    talk('analyzing results for '+ website)
    webbrowser.open(f'{website}.com',new = 1)

def amazon():
    talk('opening amazon')
    webbrowser.open(amazon_url,new=2)

def instagram():
    talk('opening instagram' )
    webbrowser.open(instagram_url,new=3)

def linkedin():
    talk('opening likedin')
    webbrowser.open(linkedin_url,new=4)

def email():
    talk('opening email')
    webbrowser.open(gmail_url,new=5)

def Weather():
    talk('forcasting weather')
    webbrowser.open(weather_url,new=6)

def voice(): 
    with sr.Microphone() as source:
        print('[listening].....')
        voice = r.listen(source)
        text = r.recognize_google(voice)
        text = text.lower()
    return text

def talk(text):
    engine.say(text)
    engine.runAndWait() 

def run_jarvis():
    command = voice()
    
    if 'play' in command:
        songs = command.replace('play','')
        talk('playing '+ songs)
        pywhatkit.playonyt(songs)
    
    elif 'hello jarvis' in command or 'hi jarvis' in command or 'hey jarvis'in command :
        bot(command)
    
    elif 'good' in command:
        bot(command)
    
    elif 'time' in command:
        time = datetime.datetime.now().strftime('%I:%M %p')
        talk('The time is '+ time)
    
    elif 'date' in command:
        date=datetime.datetime.now().strftime('%Y-%m-%d')
        print(date)
        talk('today is ' + date)

    elif 'who is' in command:
        wiki = command.replace('who is','')
        about = wikipedia.summary(wiki,1)
        print(about)
        talk(about)
    
    elif 'search' in command or 'what is' in command  or 'when' in command :
        website = command.replace('search','')
        web(website)
    
    elif 'amazon' in command:
        amazon()

    elif 'instagram' in command:
        instagram()
    
    elif 'linkedin' in command:
        linkedin()

    elif 'email' in command or 'gmail' in command:
        gmail()

    elif 'weather' in command :
        Weather()

    elif 'no' in command  or 'nope' in command:
        stop()

    else:
        talk('sorry i did not get that try again ')

end = True
while end:
    def stop():
        talk('ok boss')
    run_jarvis()
    time.sleep(6)
    engine.say('if you need anything wake me up boss')
    engine.runAndWait()
