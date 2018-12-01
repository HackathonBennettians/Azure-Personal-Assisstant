import speech_recognition as sr
import os
from googlesearch import search
import webbrowser
import ssl

ssl._create_default_https_context = ssl._create_unverified_context

r = sr.Recognizer()

with sr.Microphone() as source:
    print("What can i do for you?")
    audio = r.listen(source)

    print("I think you said :\n" + r.recognize_google(audio))

input =  r.recognize_google(audio)+ '.app'
input1 = r.recognize_google(audio)
if('search' not in input):
    location = os.listdir('/Applications/')

    for i in location:
        if (input == i):
            os.system("open /Applications/'" + input + "'")


else:
    input2 = input1.split('search ')[1]
    for url in search(input2):
        print(input2)
        print(url)
        webbrowser.open_new(url)
        break

