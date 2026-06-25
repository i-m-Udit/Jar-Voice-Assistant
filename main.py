import pyttsx3
import speech_recognition as sr
import webbrowser
import openai
import pyjokes
import pyautogui
import pyperclip
import time
import requests

sr1 = sr.Recognizer()
jar = pyttsx3.init()

def speak(text):
    jar.say(text)
    jar.runAndWait()

def jokes():
    joke = pyjokes.get_joke()
    print(joke)
    speak(joke)

def news():
    try:
        api_key = "92f1bd8c21bf47b09b45ba014fc54c5f"

        url = f"https://newsapi.org/v2/everything?q=india&sortBy=publishedAt&pageSize=5&language=en&apiKey={api_key}"

        response = requests.get(url)
        data = response.json()
        articles = data["articles"]

        news_list = []
        for article in articles[0:5]:
            news_list.append(article["title"])

        return news_list
    
    except Exception as e :
        print(e)

def last_option(command):
    webbrowser.open_new_tab("https://google.com")
    time.sleep(1.75)

    pyautogui.leftClick(728,296 , duration=1.75)

    pyperclip.copy(command)

    pyautogui.hotkey('ctrl' , 'v')

    pyautogui.hotkey('enter')

def aiProcess(command):
    #you can do this if you have active open ai api key
    client = openai(
    api_key="your_api_key",
    )
    completion = client.chat.completions.create(
    model="gpt-3.5-turbo",
    messages=[
        {"role":"system" , "content":"You are a virtual assistant named jar , skilled in general tasks like Alexa , Google cloud"},
        {"role":"user" , "content":command}
    ]
    )
    print(completion.choices[0].message.content)

def commands(c):
    print(f"🐞[DEBUG] : Recieved :{c} ")
    c=c.lower()

    if "open google" in c:
        webbrowser.open("https://google.com")
        speak("Opening Google")

    elif "open facebook" in c:
        webbrowser.open("https://facebook.com")
        speak("Opening Facebook")
# 827 531
    elif "open amazon" in c:
        webbrowser.open("https://amazon.com")
        speak("Opening Amazon")

    elif "open instagram" in c:
        webbrowser.open("https://instagram.com")
        speak("Opening Instagram")

    elif "open youtube" in c:
        webbrowser.open("https://youtube.com")
        speak("Opening YouTube")

    elif "open chat gpt" in c:
        speak("Opening ChatGPT")
        webbrowser.open("https://chatgpt.com")

    elif "open linked in" in c:
        webbrowser.open("https://linkedin.com")
        speak("Opening LinkedIn")

    elif "open github" in c:
        webbrowser.open("https://www.github.com")
        speak("Opening github")

    elif "close" in c :
        pyautogui.hotkey('alt' , 'f4')
        speak("Window closed")

    elif "open" in c and "code" in c:
        speak("opening visual studio code")
        pyautogui.leftClick(644 , 738)  # --> this is for my personal use 

    elif "play" in c:
        from musicPlaylist import songs
        words = c.split()
        for word in words:
            if word.lower() in songs:
                webbrowser.open(songs[word])
                speak("🎵Playing music!")
            else:
                pass
        else:
            print("Error in playing music")

    elif "joke" in c:
        jokes()

    elif "pdf" in c and "python" in c:
        webbrowser.open_new_tab("https://www.codewithharry.com/notes")
        time.sleep(3)
        pyautogui.leftClick(145 , 669)
        speak("Here is your python pdf!")

    elif "news" in c:
        for item in news(): #running through the func so that news can be told one by one as a variable item
            print(item) 
            speak(item)

    elif "pause" in c and "music" in c:
        pyautogui.hotkey('space')
        speak("Paused")
        print("Music paused")

    elif "skip" in c and "ad" in c:
        pyautogui.leftClick(827 , 531)

    
    else:
        speak("Sorry! i am unable to tell that but i am searching the web.")
        last_option(c)  

speak("Jar is starting , say jar to activate jar.")  

jarvis_active = False
if __name__ == "__main__":
    while True:
        print(" 🎧 Jar is listening")


        try:
            with sr.Microphone() as source:

                # sr1.adjust_for_ambient_noise(source) i am not using it this is optional
                audio = sr1.listen(source , phrase_time_limit=3 , timeout=3)
                recognize_audio = sr1.recognize_google(audio)
                print("🧏 Heard" , recognize_audio)

                if jarvis_active == False and "jar" in recognize_audio.lower():
                    jarvis_active = True
                    speak("Jarvis Activated")
                    print("🎬Jarvis active")
                    continue

                if jarvis_active == True:

                    print("👂Jarvis active!!!!!!!!!!")

                    if "stop" in recognize_audio.lower() or "exit" in recognize_audio.lower():
                        print("⛔Stopping Jarvis")
                        speak ("Stopping Jarvis")
                        break

                    else:
                        
                        commands(recognize_audio)
                        jarvis_active = False

        except Exception as e:
            print(e)
