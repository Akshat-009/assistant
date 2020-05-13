import pyttsx3
import datetime
import speech_recognition as sr
import wikipedia 
import webbrowser
import os
import smtplib
def sendmail(to,content):
    server=smtplib.SMTP('smtp.gmail.com',587)
    server.ehlo()
    server.starttls()
    server.login("emailid","password")
    server.sendmail(to,content)
    server.close()
ne=pyttsx3.init("sapi5")
voices=ne.getProperty("voices")
ne.setProperty('voice',voices[1].id)
def speak(audio):
    ne.say(audio)
    ne.runAndWait()
def welcome():
    speak("mera naa jarvis hai aapki khidmat mein haazir hu")
def takecommand():
    r=sr.Recognizer()
    with sr.Microphone() as source:
        print("listening ....")
        r.pause_threshold=1
        audio=r.listen(source)
    try:
        print("recognizing")
        query=r.recognize_google(audio,language="en-in")
        print(f"user said {query}")
    except Exception as e:
        print(e)
    return query
if __name__ == "__main__":
    welcome()
    takecommand()
    query=takecommand().lower()

    if "wikipedia" in query:
        speak("searching Wikipedia")
        query=query.replace("wikipedia","")
        result=wikipedia.summary(query,sentence=2)
        print(result)
        speak(result)
    elif "open google" in query:
        speak("open google")
        webbrowser.open("www.google.com")
    elif "open youtube" in query:
        speak("open youtube")
        webbrowser.open("www.youtube.com")
    elif "open facebook" in query:
        speak("open google")
        webbrowser.open("www.facebook.com")
    elif "open code" in query:
        codepath="#"
        os.startfile(codepath)
    elif "send email" in query:
        speak("to whom")
        to=takecommand().lower()
        speak("what should I write")
        content=takecommand().lower()
        sendmail(to,content)
        speak("sent")