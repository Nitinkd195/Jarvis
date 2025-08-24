import pyttsx3

# Initialize the pyttsx3 engine
engine = pyttsx3.init('sapi5')

# Select a voice (female voice if available)
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[0].id)  # Change index if another voice is better

# Adjust the speaking rate (lower for slower speech)
engine.setProperty('rate', 150)  # Default is ~200 words per minute

# Adjust the volume (optional, range: 0.0 to 1.0)
engine.setProperty('volume', 1.0)  # Set to maximum

def speak(command):
    """
    Speaks the given text in a clear and natural-sounding way.
    """
    # Add natural pauses or emphasis in the text as needed
    command = command.replace(',', ', ').replace('...', '... ')
    engine.say(command)
    engine.runAndWait()

if __name__ == '__main__':
    speak()
    # Test the voice assistant





