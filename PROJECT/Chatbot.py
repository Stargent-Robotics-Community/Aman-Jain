#!/usr/bin/env python
# coding: utf-8

# In[ ]:



import pyttsx3 as pp
import speech_recognition as sr 
import datetime 
import webbrowser
 

engine = pp.init()
voices = engine.getProperty('voices')

engine.setProperty('voice', voices[0].id)
def speak(input):
    engine.say(input)
    engine.runAndWait()

# speak('aman') #testing
def wishme():
    hour = int(datetime.datetime.now().hour)
    if hour >=0 and hour <12:
        speak("Hello, good morning")
    elif hour>=12 and hour <18:
        speak("Hello, good afternoon")
    else:
        speak("Hello, Good evening")
    speak("hey, i am your robot, what is your good name")


# wishme()
 
def tc():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print('listening...')
        r.adjust_for_ambient_noise(source)
        r.pause_threshold = 1
        audio = r.listen(source)
    try: 
        print('Recognizing..')
        resp = r.recognize_google(audio)
        print(resp)
    except Exception as e:
        print('can you please repeat again')
        return 'None'
    return resp

def sendEmail(to,content):
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.ehlo()
    server.starttls()
    server.login(' ','######')
    server.sendmail(' ', to, content)
    server.close()

# tc() #testing

wishme()
# for name 
name = tc()
speak(f'hey {name}, please tell me aman how can i help you')


while True:
    resp = tc().lower()
    # to search anything on wikipedia
    if 'Wikipedia' in resp:
        speak("searching wikipedia..")
        resp = resp.replace("Wikipedia", "")
        results = wikipedia.summary(resp, sentences =2)
        speak('According to wikipedia')
        print(results)
        speak(results)
    # opening some web applications
    elif 'google' in resp:
        webbrowser.open('google.com')
    elif 'open facebook' in resp:
        webbrowser.open('facebook.com')
    elif 'open youtube' in resp:
        webbrowser.open('youtube.com')
    elif 'open whatsapp' in resp:
        webbrowser.open('whatsapp.com')
    elif 'time' in resp:
        strtime = datetime.datetime.now().strftime('%H:%M:%S')
        speak(f'Sir, time is :{strtime}')
    # to open an app in the pc
    elif 'open zoom' in resp:
        OpenZoom = 'C:\\Users\\aman\\AppData\\Roaming\\Zoom\\bin\\Zoom.exe'  #target of zoom in properties
        os.startfile(OpenZoom)
        
    elif 'email' in resp:
        try:
            content = tc()
            to = "hi.jainaman@gmail.com"
            sendEmail(to, content)
            speak("Email has been sent, aman please check")
        except Exception as e:
            speak('Soo sorry aman, i am not able to send this email')
    else:
        # say anything or exit, quit such keywords to stop chatbot
        last_note = 'thank you, and feel free to ask anything'
        speak(last_note)   
        print(last_note) 
        break
        


# In[ ]:





# In[ ]:




