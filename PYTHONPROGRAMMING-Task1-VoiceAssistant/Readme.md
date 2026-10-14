# Python Voice Assistant

A simple, voice-controlled desktop assistant written in Python. It listens to your microphone, converts your speech to text using Google's speech recognition, and replies out loud using a text-to-speech engine.

## Features

- **Greetings**: say "hello" or "hi" and the assistant greets you back
- **Time**: say "time" to hear the current time
- **Date**: say "date" to hear today's date
- **Web search**: say "search <your query>" to open a Google search in your browser
- **Exit**: say "stop", "exit" or "bye" to shut the assistant down
- Continuous listening loop, so you can give several commands in one session

## Requirements

- Python 3.8 or newer
- A working microphone
- An internet connection (the Google speech recognition service is online)

### Python packages

| Package | Purpose |
|---|---|
| `SpeechRecognition` | Converts recorded audio to text |
| `pyttsx3` | Offline text-to-speech |
| `sounddevice` | Records audio from the microphone |
| `numpy` | Required by `sounddevice` for audio arrays |

## Installation

1. Clone or download this project.
2. (Optional) Create a virtual environment:

   ```bash
   python -m venv venv
   source venv/bin/activate      # Windows: venv\Scripts\activate
   ```

3. Install the dependencies:

   ```bash
   pip install SpeechRecognition pyttsx3 sounddevice numpy
   ```

> **Linux users:** you may also need `sudo apt install espeak libportaudio2` for `pyttsx3` and `sounddevice` to work.

## Usage

Run the script (replace `main.py` with your file name):

```bash
python main.py
```

The assistant says "Voice assistant activated." and then listens for 5 seconds at a time. Speak after you see `Listening... Speak now!` in the terminal.

### Example commands

| You say | Assistant does |
|---|---|
| "Hello" / "Hi" | Greets you |
| "What time is it" | Tells you the current time |
| "What's the date" | Tells you today's date |
| "Search python tutorials" | Opens Google results for "python tutorials" |
| "Stop" / "Exit" / "Bye" | Says goodbye and quits |

## How It Works

1. `speak(text)` prints the text and speaks it aloud with `pyttsx3`.
2. `listen()` records 5 seconds of audio with `sounddevice`, wraps it in a `speech_recognition.AudioData` object, and sends it to Google's recognizer. It returns the recognized text in lowercase.
3. `run_assistant()` loops forever, calling `listen()` and matching keywords in the result to decide what to do, until you say a stop word.

## Configuration

You can tweak these values inside `listen()`:

- `sample_rate = 44100`: audio sampling rate in Hz
- `duration = 5`: how many seconds to listen per command

## Troubleshooting

- **"Sorry, I didn't catch that"**: speak clearly, closer to the mic, or increase `duration`.
- **"Speech service is currently down"**: check your internet connection.
- **No audio input or `PortAudio` errors**: make sure a microphone is connected and selected as the default input device. Run `python -m sounddevice` to list available devices.
- **No voice output**: confirm your system volume is on and `pyttsx3` has a speech engine available (SAPI5 on Windows, NSSpeechSynthesizer on macOS, eSpeak on Linux).

## Possible Improvements

- Add a wake word (e.g. "hey assistant") so it only responds when called
- Add more commands: open apps, play music, tell jokes, weather
- Replace the fixed 5-second window with silence detection
- Use an offline recognizer such as Vosk for use without internet

## License

This project is free to use and modify for personal and educational purposes.
