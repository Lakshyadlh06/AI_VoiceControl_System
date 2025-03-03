#pip install SpeechRecognition
#pip install pyttsx3
#pip install pywhatkit
#pip install wikipedia

import speech_recognition as sr
import pyttsx3
import pywhatkit
import wikipedia
import datetime

r= sr.Recognizer()
phone_numbers = {"ravi":"1234567890","raja":"9999988888","kumar":"7777777777"}
bank_account_numbers = {"tt":"123456789","mm":"7412568932"}

def speak(command):
    engine = pyttsx3.init()
    voices = engine.getProperty('voices')
    engine.setProperty('voice',voices[1].id)
    engine.say(command)
    engine.runAndWait()

def commands():
    try:
        with sr.Microphone() as source:
            r.adjust_for_ambient_noise(source)
            print('Listening... Ask now...')
            audioin = r.listen(source)
            my_text = r.recognize_google(audioin)
            my_text = my_text.lower()
            print(my_text)
            #speak(my_text)

            # ask to play song
            if 'play' in my_text:
                my_text = my_text.replace('play','')
                speak('playing' + my_text)
                pywhatkit.playonyt(my_text)

            # ask date
            elif 'date' in my_text:
                today = datetime.date.today()
                speak(today)

            # ask time
            elif 'time' in my_text:
                timenow = datetime.datetime.now().strftime('%H:%M')
                speak(timenow)

            # ask details about any person
            elif "who is" in my_text:
                person = my_text.replace('who is','')
                info = wikipedia.summary(person,1)
                speak(info)

            # ask phone numbers
            elif "phone number" in my_text:
                names = list(phone_numbers)
                print(names)
                for name in names:
                    if name in my_text:
                        print(name + "phone number is " + phone_numbers[name])
                        speak(name + "phone number is " + phone_numbers[name])

            # ask personal bank account numbers
            elif "account number" in my_text:
                banks = list(bank_account_numbers)
                for bank in banks:
                    if bank in my_text:
                        print(bank + " bank acoount number is  " + bank_account_numbers[bank])
                        speak(bank + " bank acoount number is  " + bank_account_numbers[bank])

            # if not recognized
            else:
                speak("Please ask correct question")
    except:
        print('Error in capturing microphone...')        
while True:
    commands()