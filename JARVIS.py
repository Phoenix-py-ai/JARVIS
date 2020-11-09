import pyttsx3
import speech_recognition as sr
import datetime
import wikipedia
import webbrowser
import time
import os
import sys
import urllib
import random
import smtplib
from googlesearch import search


engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
#print(voices[0].id)
engine.setProperty('voice', voices[0].id)

chromedir = "C:/Program Files/Google/Chrome Beta/Application/chrome.exe %s"
def speak(audio):
    engine.say(audio)
    engine.runAndWait()

def wishMe():
    hour = int(datetime.datetime.now().hour)
    if hour>=0 and hour<12:
        speak("Good Morning!")

    elif hour>=12 and hour<17:
        speak("Good Afternoon!")

    else:
        speak("Good Evening!")
    
    speak("I am Jarvis. How May I Help You.")


def WishMyFriends():
    hour = int(datetime.datetime.now().hour)
    if hour>=0 and hour<12:
        speak("Good Morning!")

    elif hour>=12 and hour<17:
        speak("Good Afternoon!")

    else:
        speak("Good Evening!")



def takeCommand():
    # It takes mic input from the user and returns str output.

    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        r.pause_threshold = 0.8
        audio = r.listen(source)

    try:
        print("Recognizing...")
        query = r.recognize_google(audio, language='en-in')
        print(f"User said: {query}\n")

    except Exception as e:
        #print(e)
        speak("Sorry sir. I failed to recognize it. Can you please say that again for me")
        return "None"
    return query

def sendEmail(to,content):
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.ehlo()
    server.starttls()
    server.login('hasancr200707@gmail.com', 'hasan@1305')
    server.sendmail('hasancr200707@gmail.com', to, content)
    server.close()

if __name__ == "__main__":
    wishMe()
    while True:
        query = takeCommand().lower()
        #Logic for executing tasks
        if 'wikipedia' in query:
            speak('Searching Wikipedia...')
            query = query.replace("Wikipedia", "")
            results = wikipedia.summary(query, sentences=2)
            speak("According to Wikipedia")
            speak(results)
            print(results)

        elif 'open youtube' in query:
            webbrowser.get(chromedir).open("youtube.com")

        elif 'open google' in query:
            webbrowser.get(chromedir).open('www.google.com')

        elif 'open classroom' in query:
            webbrowser.get(chromedir).open("classroom.google.com/u/1/h")

        elif 'open indian super league' in query:
            webbrowser.get(chromedir).open("www.google.com/search?q=isl+2020-21&oq=is&aqs=chrome.0.69i59l2j69i57j69i59j46i131i433j69i61l3.1751j0j7&sourceid=chrome&ie=UTF-8")

        elif 'play music' in query:
            music_dir = 'C:\\Users\\hasan\\Music'
            songs = os.listdir(music_dir)
            os.startfile(os.path.join(music_dir, songs[0]))

        elif 'play videos' in query:
            videos_dir = 'C:\\Users\\hasan\\Downloads\\Video'
            videos = os.listdir(videos_dir)
            os.startfile(os.path.join(videos_dir, videos[0]))

        elif 'play documentries' in query:
            documentries_dir = 'C:\\Users\\hasan\\Videos\\Documentaries'
            documentries = os.listdir(documentries_dir)
            os.startfile(os.path.join(documentries_dir, documentries[0]))

        elif 'show screenshots' in query:
            screenshots_dir = 'C:\\Users\\hasan\\Pictures\\Screenshots'
            screenshots = os.listdir(screenshots_dir)
            os.startfile(os.path.join(screenshots_dir, screenshots[0]))

        elif 'time' in query:
            strTime = datetime.datetime.now().strftime("%H:%M:%S")
            speak(f"Sir, the time is {strTime}")

        elif 'open code' in query:
            codePath = "C:\\Users\\hasan\\AppData\\Local\\Programs\\Microsoft VS Code\\Code.exe"
            os.startfile(codePath)
        
        elif 'open chrome' in query:
            chromePath = "C:/Program Files/Google/Chrome Beta/Application/chrome.exe"
            os.startfile(chromePath)

        elif 'open powerpoint' in query:
            powerpointPath = "C:/Program Files/Microsoft Office/root/Office16/POWERPNT.EXE"
            os.startfile(powerpointPath)

        elif 'open word' in query:
            wordPath = "C:/Program Files/Microsoft Office/root/Office16/WINWORD.EXE"
            os.startfile(wordPath)

        elif 'date' in query:
            strTime = datetime.datetime.now().strftime("%Y/%m/%d")
            speak(f"the date is {strTime}")

        elif 'email to karan' in query:
            try:
                speak("What should I send?")
                content = takeCommand()
                to = "karanwin10@gmail.com"
                sendEmail(to,content)
                speak("Email has been sent!")
            except Exception as e:
                print(e)
                speak("Sorry, I can't send this Email at the moment. Try again please.")

        elif 'open edge' in query:
            edgePath = "C:/Program Files (x86)/Microsoft/Edge/Application/msedge.exe"
            os.startfile(edgePath)

        elif 'open idm' in query:
            idmPath = "C:/Program Files (x86)/Internet Download Manager/IDMan.exe"
            os.startfile(idmPath)

        elif 'open studio' in query:
            studioPath = "C:/Program Files/Android/Android Studio/bin/studio64.exe"
            os.startfile(studioPath)

        elif 'open kaspersky' in query:
            kpskyPath = "C:/Program Files (x86)/Kaspersky Lab/Kaspersky Total Security 21.2/avpui.exe"
            os.startfile(kpskyPath)

        elif 'open excel' in query:
            excelPath = "C:/Program Files/Microsoft Office/root/Office16/EXCEL.EXE"
            os.startfile(excelPath)

        elif 'say hi to my friend' in query:
            WishMyFriends()
            speak("Hello I am JARVIS. I am an AI or Artificial Intelligence totally made by sir. The full abbreviation of my name is Just a Rather Very Intelligent System. It is a pleasure meeting you.")

        elif 'introduce yourself' in query:
            speak("Me, JARVIS. As I said I was made by Hasan Sir. I am inspired from the JARVIS that Tony Stark made in Iron Man. I can do anything and I can control this PC. I try to help sir as much as I can.")

        elif 'goodbye' in query:
            speak("Goodbye sir.")
            quit()

        
        else:
            print("Searching Google...")
            speak('Searching Google...')
            query = query.replace("google", "")
            chrome_path = r'C:\Program Files (x86)\Google\Chrome\Application\chrome.exe %s'
            for url in search(query, tld="co.in", num=1, stop = 1, pause = 2):
                webbrowser.open("https://google.com/search?q=%s" % query)
            print("This is what I found according to your search")
            speak("This is what I found according to your search")