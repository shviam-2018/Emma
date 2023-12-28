#all needed import
import pyttsx3
import speech_recognition as sr
import datetime
import wikipedia
import webbrowser
import os

#defining all veribal 
engine = pyttsx3.init("sapi5")
voices = engine.getProperty("voices")
engine.setProperty("voice",voices[0].id)
#defining audio and wishme 
def speak(audio):
    engine.say(audio)
    engine.runAndWait()
    
def wishme():
    hour = int(datetime.datetime.now().hour)
    if hour>=0 and hour<12:
        print("Good morning!")
        speak("Good morning!")
    elif hour>=12 and hour<18:
        print("Good afternoon")
        speak("Good afternoon!")
    else:
        print("Good evening!")
        speak("Good evening!")
        
    print("I am Emma sir. Please tell me how can I assist you today.")  
    speak("I am Emma sir. Please tell me how can I assist you today.")
    
#wishme() # call the wishme() function
    
def takecommand():
# it takes microphone input and ruterns string output
    noise_reduction = 0.3
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("listening...")
        r.pause_threshold = 1
        audio = r.listen(source)
        
    try: 
        print("recognizing...")
        query = r.recognize_google(audio, language="en-us")
        print(f"userside {query}\n")
        
    except Exception as e:
        print("say that agein please...")
        return "None"
    return query    

if __name__=="__main__":
    wishme()
    while True:
        query = takecommand().lower()
        
    #logich og exucuting task besced on query
        if "wikipedia" in query:
            speak("serching wikipedia...")
            query = query.replace("wikipedia", "")
            results = wikipedia.summary(query, sentences=2)
            speak("According to wikepedia")
            print(results)
            speak(results)

        elif "youtube" in query:
            webbrowser.open("https://www.youtube.com/")

elif "google" in query:
    webbrowser.open("https://www.google.com/")

elif "email" in query:
    webbrowser.open("https://mail.google.com/")

elif "search" in query:
    webbrowser.open("https://www.google.com/search?q=" + query)

elif "chat gpt" in query:
    webbrowser.open("https://chat.openai.com/chat")

elif "study" in query:
    webbrowser.open("https://www.youtube.com/watch?v=irqbmMNs2Bo&t=3404s&ab_channel=ApnaCollege")

elif "music" in query:
    webbrowser.open("https://open.spotify.com/")

elif "news" in query:
    webbrowser.open("https://www.bbc.com/news")

elif "weather" in query:
    webbrowser.open("https://weather.com/")

elif "calendar" in query:
    webbrowser.open("https://calendar.google.com/")

elif "recipe" in query:
    webbrowser.open("https://www.allrecipes.com/")  

elif "learn a language" in query:
    webbrowser.open("https://www.duolingo.com/")  

else:
    print("I am sorry but i cant seem to help you with that.")
    speak("I am sorry but i cant seem to help you with that.")