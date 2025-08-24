import speech_recognition as sr
import datetime
import webbrowser
import speak as s
import wikipedia
import os
#import weather1 as w



""" from gif_player import main

gif_list = ["JARVIS-master/Jarvis/utils/images/initiating.gif", "JARVIS-master/Jarvis/utils/images/loading.gif", "JARVIS-master/Jarvis/utils/images/program_load.gif"]
main(gif_list) """

# Greeting function
def get_greeting():
    hour = int(datetime.datetime.now().hour)
    if 0 <= hour < 12:
        return "Good Morning!"
    elif 12 <= hour < 18:
        return "Good Afternoon!"
    else:
        return "Good Evening!"


# Take Command function
def takeCommand():
    recognizer = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        recognizer.pause_threshold = 1
        try:
            audio = recognizer.listen(source)
            print("Recognizing...")
            query = recognizer.recognize_google(audio, language='en-in')
            print(f"User said: {query}\n")
        except Exception as e:
            print("Say that again please...")
            return "None"
        return query.lower()


# Main function
def jarvis():
    greeting = get_greeting()
    s.speak(greeting)
    s.speak("I am Neetic Sir, How may I help you?")

    while True:
        query = takeCommand()
        if query == "none":
            continue

        # Logic for executing tasks based on query
        if 'wikipedia' in query:
            s.speak('Searching Wikipedia...')
            query = query.replace("wikipedia", "")
            results = wikipedia.summary(query, sentences=2)
            s.speak("According to Wikipedia")
            print(results)
            s.speak(results)

        elif 'play music' in query or "play song" in query:
            s.speak("Here you go with music")
            # music_dir = "G:\\Song"
            music_dir = "C:\\Users\\GAURAV\\Music"
            songs = os.listdir(music_dir)
            print(songs)
            #random = os.startfile(os.path.join(music_dir, songs[1]))

        elif 'how are you' in query:
            s.speak("I am fine, Thank you")
            s.speak("How are you, Sir")

        elif 'fine' in query or "good" in query:
            s.speak("It's good to know that your fine")

        elif "who made you" in query or "who created you" in query:
            s.speak("I have been created by nitin and ")

        elif 'the time' in query:
            strtime = datetime.datetime.now().strftime("%H:%M:%S")
            s.speak(f"Sir, the time is {strtime}")

        elif 'search' in query or 'play' in query:
            query = query.replace("search", "")
            query = query.replace("play", "")
            webbrowser.open(query)

        #elif "weather" in query:
            #w.weather()


        elif 'lock window' in query:
            s.speak("locking the device")
            #ctypes.windll.user32.LockWorkStation()
        elif 'shutdown system' in query:
            s.speak("Hold On a Sec ! Your system is on its way to shut down")
            #subprocess.call('shutdown / p /f')

        elif 'open chatgpt' in query:
            webbrowser.open("https://chat.openai.com/")

        elif 'open google' in query:
            webbrowser.open("https://google.com")

        elif 'open instagram' in query:
            webbrowser.open("https://instagram.com")

        elif 'open whatsapp' in query:
            webbrowser.open("https://web.whatsapp.com/")

        elif 'notepad' in query:
            os.startfile("notepad.exe")

        elif 'word' in query:
            os.startfile("winword.exe")

        elif 'powerpoint' in query:
            os.startfile("powerpnt.exe")

        elif 'excel' in query:
            os.startfile("excel.exe")

        elif 'open' in query:
            # Extract the app/website name from the query
            app_name = query.replace('open', '').strip().lower()

            # Generate the URL dynamically
            url = f"https://www.{app_name}.com"

            try:
                # Attempt to open the generated URL
                webbrowser.open(url)
                s.speak(f"Opening {app_name}")
            except Exception as e:
                # Handle any errors gracefully
                s.speak(f"Sorry, I couldn't open {app_name}. Please try again.")


        elif 'exit' in query or 'quit' in query:
            s.speak("Goodbye Sir. Have a great day!")
            break

        else:
            print("No command recognized. Please try again.")
            s.speak("I didn't catch that. Please repeat.")


if __name__ == "__main__":
    jarvis()
