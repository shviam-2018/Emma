# Emma - Python Voice Assistant

Emma is a Python-based voice assistant that utilizes various libraries to provide a range of functionalities through voice commands. This project uses pyttsx3 for text-to-speech conversion, speech_recognition for recognizing voice commands, wikipedia for searching Wikipedia, webbrowser for opening web pages, and os for system-related operations.

## Features

### 1. WishMe Functionality
Emma greets the user based on the time of day - "Good morning," "Good afternoon," or "Good evening."

### 2. Voice Interaction
Emma interacts with the user through voice commands, making it a hands-free experience.

### 3. Web Search
Searches Wikipedia for user-provided queries, summarizes the results, and reads them out loud.

### 4. Web Browser Commands
Opens popular websites directly from the browser based on user commands:
- **YouTube:** Opens [YouTube](https://www.youtube.com/)
- **Google:** Opens [Google](https://www.google.com/)
- **Email:** Opens [Gmail](https://mail.google.com/)
- **Search:** Performs a Google search based on the user's query
- **Chat GPT:** Opens the [OpenAI Chat GPT](https://chat.openai.com/chat) website
- **Study Time:** Opens a study-related video on [YouTube](https://www.youtube.com/watch?v=irqbmMNs2Bo&t=3404s&ab_channel=ApnaCollege)
- **Music:** Opens [Spotify](https://open.spotify.com/)

### 5. Additional Functionalities
- **News:** Opens [BBC News](https://www.bbc.com/news)
- **Weather:** Opens [Weather.com](https://weather.com/)
- **Calendar:** Opens [Google Calendar](https://calendar.google.com/)
- **Recipe:** Explores recipes on [AllRecipes](https://www.allrecipes.com/)
- **Learn a Language:** Opens [Duolingo](https://www.duolingo.com/)

### 6. Apology for Unrecognized Commands
If Emma fails to understand a command, it politely apologizes.

## Prerequisites

- **Python 3.x**
- Install required Python packages using: `pip install pyttsx3 speechrecognition wikipedia`

## Usage

1. **Run the Script:**
   - Execute the Python script to start Emma, your voice assistant.
   
2. **Voice Interaction:**
   - Emma will greet you and wait for your command.
   
3. **Speak Commands:**
   - Issue voice commands, and Emma will respond accordingly.

## Note

- Ensure your microphone is functional for voice commands.
- Emma may not comprehend certain commands, and it will apologize if it can't respond.

Feel free to customize the code to add more functionalities or adapt it to your preferences.
