import speech_recognition as sr
import speak as s

def takeCommand():
    # It takes microphone input from the user and returns string output
    recognizer = sr.Recognizer()

    # Use microphone as the source of input
    with sr.Microphone() as source:
        # print("Adjusting for ambient noise...")
        # s.speak("Adjusting for ambient noise...")

        recognizer.adjust_for_ambient_noise(source)  # Optional, helps improve accuracy
        print("Listening ....")
        s.speak("Listening ....")

        audio_data = recognizer.listen(source)  # Record the audio

        try:
            # Recognize speech using Google's speech recognition
            print("Recognizing speech...")
            command = recognizer.recognize_google(audio_data)
            print("You said:", command)
            s.speak(f"You said {command}")

        except sr.UnknownValueError:
            print("Could not understand the audio.")
            s.speak("Could not understand the audio.")
        except sr.RequestError as e:
            print(f"Could not request results; {e}")
            s.speak(f"Could not request results; {e}")
            return command

if __name__=='__main__':
    takeCommand()



