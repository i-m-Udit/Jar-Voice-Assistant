# 🤖 Jar — Voice Assistant

A Python-based voice assistant that listens for your voice, understands commands, and performs tasks like opening websites, playing music, telling jokes, reading news, and searching the web — all hands-free.

---

## 💡 Features

- 🎙️ Wake word activation — say **"Jar"** to activate
- 🌐 Open websites by voice — Google, YouTube, Instagram, GitHub, LinkedIn and more
- 🎵 Play music from a custom playlist
- 😂 Tell jokes
- 📰 Read the latest news headlines
- 🔍 Search anything on Google by voice
- 💻 Open apps like VS Code
- ⏸️ Pause music and skip YouTube ads
- 🤖 Optional ChatGPT integration for open-ended questions

---

## 🛠️ Tech Stack

- **Python**
- `pyttsx3` — text to speech
- `SpeechRecognition` — voice input
- `pyautogui` — GUI automation
- `pyperclip` — clipboard control
- `pyjokes` — random jokes
- `requests` — API calls
- `webbrowser` — browser control
- `openai` — ChatGPT integration (optional)
- **NewsAPI** — for live news headlines

---

## ⚙️ Setup & Installation

**1. Clone the repository**
```bash
git clone https://github.com/yourusername/jar-voice-assistant.git
cd jar-voice-assistant
```

**2. Install dependencies**
```bash
pip install pyttsx3 SpeechRecognition pyautogui pyperclip pyjokes requests openai
```

**3. Add your API keys**

- Get a free API key from [newsapi.org](https://newsapi.org) and paste it in `main.py` where it says `api_key`
- (Optional) Add your OpenAI API key in the `aiProcess()` function for ChatGPT support

**4. Set up your music playlist**

Create a `musicPlaylist.py` file in the same folder with your songs:
```python
songs = {
    "believer": "https://www.youtube.com/watch?v=...",
    "thunder": "https://www.youtube.com/watch?v=...",
}
```

**5. Run**
```bash
python main.py
```

---

## 🚀 How to Use

1. Run the script
2. Say **"Jar"** to wake it up
3. Give a command — for example:
   - *"Open YouTube"*
   - *"Tell me a joke"*
   - *"What's the news"*
   - *"Play Believer"*
   - *"Search how to learn Python"*
4. Say **"Stop"** or **"Exit"** to shut it down

---

## 📁 Project Structure

```
jar-voice-assistant/
├── main.py           ← main assistant logic
├── musicPlaylist.py  ← your custom music links
└── README.md
```

---

## ⚠️ Note

Some features like opening VS Code and clicking specific screen coordinates are configured for my personal setup. You may need to adjust the `pyautogui` coordinates in `main.py` to match your screen resolution.

---

## 🙋‍♂️ Author

Built by **Udit** — a data science and ML enthusiast.

*This was my first major Python project — built to go beyond the basics and work with real APIs, voice recognition, and automation.*
