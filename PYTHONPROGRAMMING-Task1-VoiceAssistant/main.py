# # import speech_recognition as sr
# # import pyttsx3
# # import datetime
# # import webbrowser

# # # 1. Initialize text-to-speech engine
# # engine = pyttsx3.init()

# # def speak(text):
# #     engine.say(text)
# #     engine.runAndWait()

# # # 2. Listen to user voice input
# # # def listen():
# #     # recognizer = sr.Recognizer()
# #     # with sr.Microphone() as source:
# #         # print("Listening...")
# #         # recognizer.adjust_for_ambient_noise(source)
# #         # audio = recognizer.listen(source)

# #     # try:
# #         # command = recognizer.recognize_google(audio).lower()
# #         # print(f"You said: {command}")
# #         # return command
# #     # except sr.UnknownValueError:
# #         # speak("Sorry, I didn't catch that. Could you repeat?")
# #         # return ""
# #     # except sr.RequestError:
# #         # speak("Speech service is down.")
# #         # return ""
# # import numpy as np
# # import sounddevice as sd
# # import speech_recognition as sr


# # def listen():
# #     recognizer = sr.Recognizer()
# #     sample_rate = 16000
# #     duration = 5  # Record length in seconds

# #     print("Listening...")
# #     # Record audio directly via sounddevice
# #     audio_data = sd.rec(
# #         int(duration * sample_rate), samplerate=sample_rate, channels=1, dtype="int16"
# #     )
# #     sd.wait()

# #     # Convert recorded numpy array into SpeechRecognition AudioData
# #     audio_bytes = audio_data.tobytes()
# #     audio = sr.AudioData(audio_bytes, sample_rate, 2)

# #     try:
# #         command = recognizer.recognize_google(audio).lower()
# #         print(f"You said: {command}")
# #         return command
# #     except sr.UnknownValueError:
# #         speak("Sorry, I didn't catch that. Could you repeat?")
# #         return ""
# #     except sr.RequestError:
# #         speak("Speech service is down.")
# #         return ""

# # # 3. Main assistant logic
# # def run_assistant():
# #     command = listen()
    
# #     if "hello" in command:
# #         speak("Hello! How can I assist you today?")
# #     elif "time" in command:
# #         current_time = datetime.datetime.now().strftime("%I:%M %p")
# #         speak(f"The current time is {current_time}")
# #     elif "search" in command:
# #         query = command.replace("search", "").strip()
# #         speak(f"Searching for {query}")
# #         webbrowser.open(f"https://www.google.com/search?q={query}")

# # run_assistant()
# import datetime
# import webbrowser
# import numpy as np
# import pyttsx3
# import speech_recognition as sr
# import sounddevice as sd

# # Initialize text-to-speech engine
# engine = pyttsx3.init()

# def speak(text):
#     print(f"Assistant: {text}")
#     engine.say(text)
#     engine.runAndWait()

# def listen():
#     recognizer = sr.Recognizer()
#     sample_rate = 44100
#     duration = 5  # Listens for 5 seconds

#     speak("Listening... Speak now!")
    
#     # Record audio directly from mic via sounddevice
#     audio_data = sd.rec(int(duration * sample_rate), samplerate=sample_rate, channels=1, dtype='int16')
#     sd.wait()

#     # Convert audio into SpeechRecognition format
#     audio_bytes = audio_data.tobytes()
#     audio = sr.AudioData(audio_bytes, sample_rate, 2)

#     try:
#         command = recognizer.recognize_google(audio).lower()
#         print(f"You said: {command}")
#         return command
#     except sr.UnknownValueError:
#         speak("Sorry, I didn't catch that. Could you repeat?")
#         return ""
#     except sr.RequestError:
#         speak("Speech service is currently down.")
#         return ""

# def run_assistant():
#     command = listen()

#     if "hello" in command or "hi" in command:
#         speak("Hello! How can I assist you today?")
#     elif "time" in command:
#         current_time = datetime.datetime.now().strftime("%I:%M %p")
#         speak(f"The current time is {current_time}")
#     elif "date" in command:
#         current_date = datetime.datetime.now().strftime("%B %d, %Y")
#         speak(f"Today's date is {current_date}")
#     elif "search" in command:
#         query = command.replace("search", "").strip()
#         if query:
#             speak(f"Searching Google for {query}")
#             webbrowser.open(f"https://www.google.com/search?q={query}")
#         else:
#             speak("What would you like me to search for?")
#     elif command:
#         speak("I heard you, but I don't know that command yet.")

# if __name__ == "__main__":
#     run_assistant()
import datetime
import webbrowser
import numpy as np
import pyttsx3
import speech_recognition as sr
import sounddevice as sd

# Initialize text-to-speech engine
engine = pyttsx3.init()

def speak(text):
    print(f"Assistant: {text}")
    engine.say(text)
    engine.runAndWait()

def listen():
    recognizer = sr.Recognizer()
    sample_rate = 44100
    duration = 5  # Listens for 5 seconds

    print("\nListening... Speak now!")
    
    # Record audio directly from mic via sounddevice
    audio_data = sd.rec(int(duration * sample_rate), samplerate=sample_rate, channels=1, dtype='int16')
    sd.wait()

    # Convert audio into SpeechRecognition format
    audio_bytes = audio_data.tobytes()
    audio = sr.AudioData(audio_bytes, sample_rate, 2)

    try:
        command = recognizer.recognize_google(audio).lower()
        print(f"You said: {command}")
        return command
    except sr.UnknownValueError:
        speak("Sorry, I didn't catch that. Could you repeat?")
        return ""
    except sr.RequestError:
        speak("Speech service is currently down.")
        return ""

def run_assistant():
    speak("Voice assistant activated.")
    
    while True:
        command = listen()

        if "hello" in command or "hi" in command:
            speak("Hello! How can I assist you today?")
        elif "time" in command:
            current_time = datetime.datetime.now().strftime("%I:%M %p")
            speak(f"The current time is {current_time}")
        elif "date" in command:
            current_date = datetime.datetime.now().strftime("%B %d, %Y")
            speak(f"Today's date is {current_date}")
        elif "search" in command:
            query = command.replace("search", "").strip()
            if query:
                speak(f"Searching Google for {query}")
                webbrowser.open(f"https://www.google.com/search?q={query}")
            else:
                speak("What would you like me to search for?")
        elif "stop" in command or "exit" in command or "bye" in command:
            speak("Goodbye!")
            break
        elif command:
            speak("I heard you, but I don't know that command yet.")

if __name__ == "__main__":
    run_assistant()