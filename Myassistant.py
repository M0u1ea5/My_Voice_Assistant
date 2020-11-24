import speech_recognition as sr
import pyttsx3
import webbrowser
import time


r=sr.Recognizer()

delay=1


def url():
    webbrowser.open(text,new=1)
    

with sr.Microphone() as source:
    print('HELLO Boss')
    time.sleep(2)
    print('waiting for your commmand..')
    r.adjust_for_ambient_noise(source, duration=0.2)
    time.sleep(delay)
    print('[talk now]...')
    audio=r.listen(source)
    print('processing please wait...')
    text=r.recognize_google(audio)
    print(f'opening.... {text}')
    time.sleep(delay)
    url()

    
    


        
        
