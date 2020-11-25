import speech_recognition as sr
import pyttsx3
import webbrowser
import time
import datetime


r=sr.Recognizer()

delay=1

amazon_url='https://www.amazon.in'
instagram_url='https://www.instagram.com'
linkedin_url='https://www.linkedin.com/feed'
gmail_url='https://mail.google.com/mail'
weather_url='https://openweathermap.org/city/1264527'


def url():
    webbrowser.open(f'{text}.com',new=1)
    time.sleep(2)
    print('if you are not satisfied with the results try saying with extensions.')
    
def Time():
    now=datetime.datetime.now()
    print(now.strftime('the TIME is  %H:%M:%S'))

def Date():
    now=datetime.datetime.now()
    print(now.strftime('today is %Y-%m-%d '))
    
def amazon():
    webbrowser.open(amazon_url,new=2)

def instagram():
    webbrowser.open(instagram_url,new=3)

def linkedin():
    webbrowser.open(linkedin_url,new=4)

def gmail():
    webbrowser.open(gmail_url,new=5)

def Weather():
    webbrowser.open(weather_url,new=6)


with sr.Microphone() as source:

    print('HELLO Boss')
    time.sleep(2)
    print('waiting for your commmand..')
    r.adjust_for_ambient_noise(source, duration=0.2)
    time.sleep(delay)
    print('[talk now]...')
    audio=r.listen(source)
    print('processing please wait...')
    text=r.recognize_google(audio).lower()
    print(f'opening.... {text}')
    time.sleep(delay)

    try:
        if text=='display time' or text=='show time' or text =='time' or text=="what's the time" :
            Time()

        elif text=='display date' or text=='show date' or text =='date' or text=="what today's date":
            Date()
            
        elif text=='open amazon' or text=='amazon' or text=='search amazon':
            amazon()

        elif text=='open instagram' or text=='instagram' or text=='search instagram':
            instagram()

        elif text=='open linkedin' or text=='linkedin' or text=='search linkedin':
            linkedin()

        elif text=='open gmail' or text=='gmail' or text=='search gmail':
            gmail()

        elif text=='open instagram' or text=='instagram' or text=='search instagram':
            instagram()

        elif text==" display today's weather " or text=="display today weather" or text=='weather'or text=='show weather' or text=="what's the weather":
            Weather()

        else:  
            url()

    except:
        print("sorry i didn't get that TRY AGAIN....")
        
