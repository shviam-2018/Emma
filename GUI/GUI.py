import pygame
import sys
import pyttsx3
import speech_recognition as sr
import datetime
import wikipedia
import webbrowser
import os

# Pygame initialization
pygame.init()

screen_width = 800
screen_height = 600

screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("Emma")

# Loading assets
emma_image = pygame.image.load("assets/Emma(idol).png")
emma_image = pygame.transform.scale(emma_image, (100, 150))
emma_rect = emma_image.get_rect()
x_pos = (screen_width - emma_rect.width) // 2
y_pos = (screen_height - emma_rect.height) // 2

microphone_button = pygame.image.load("assets/microphone_button.png")
microphone_button = pygame.transform.scale(microphone_button, (50, 50))
microphone_rect = microphone_button.get_rect()
microphone_x_pos = (screen_width - microphone_rect.width) // 2
microphone_y_pos = y_pos + emma_rect.height + 10

# Speech recognition initialization
engine = pyttsx3.init("sapi5")
voices = engine.getProperty("voices")
engine.setProperty("voice", voices[0].id)

# Message rectangle
message_rect = pygame.Rect(10, screen_height - 60, screen_width - 20, 50)
message_font = pygame.font.Font(None, 36)
message_text = ""

def speak(audio):
    engine.say(audio)
    engine.runAndWait()

def wishme():
    hour = int(datetime.datetime.now().hour)
    if 0 <= hour < 12:
        message_text = "Good morning! I am Emma. Please tell me how can I assist you today."
        speak(message_text)
    elif 12 <= hour < 18:
        message_text = "Good afternoon! I am Emma. Please tell me how can I assist you today."
        speak(message_text)
    else:
        message_text = "Good evening! I am Emma. Please tell me how can I assist you today."
        speak(message_text)
        
def takecommand():
    noise_reduction = 0.3
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        r.pause_threshold = 1
        audio = r.listen(source)

    try:
        print("Recognizing...")
        query = r.recognize_google(audio, language="en-us")
        print(f"User said: {query}\n")
        return query
    except Exception as e:
        print("Say that again please...")
        return "None"

if __name__ == "__main__":
    wishme()
    run = True
    while run:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False

        screen.fill((255, 255, 255))
        screen.blit(emma_image, (x_pos, y_pos))
        screen.blit(microphone_button, (microphone_x_pos, microphone_y_pos))

        # Draw the message rectangle
        pygame.draw.rect(screen, (200, 200, 200), message_rect)
        pygame.draw.rect(screen, (0, 0, 0), message_rect, 2)

        # Display the message text in the rectangle
        message_surface = message_font.render(message_text, True, (0, 0, 0))
        screen.blit(message_surface, (message_rect.x + 10, message_rect.y + 10))

        pygame.display.flip()

        query = takecommand().lower()

        if "wikipedia" in query:
            speak("searching Wikipedia...")
            query = query.replace("wikipedia", "")
            results = wikipedia.summary(query, sentences=2)
            speak("According to Wikipedia")
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
        # Add your other logic here for handling different queries

# Quit the game
pygame.quit()
sys.exit()
