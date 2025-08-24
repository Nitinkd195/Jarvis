from datetime import datetime
import speak as s

def get_greeting():
    # Get the current time
    current_time = datetime.now().time()

    # Define time ranges for greetings
    morning_start = current_time.replace(hour=5, minute=0, second=0, microsecond=0)
    afternoon_start = current_time.replace(hour=12, minute=0, second=0, microsecond=0)
    evening_start = current_time.replace(hour=17, minute=0, second=0, microsecond=0)
    night_start = current_time.replace(hour=20, minute=0, second=0, microsecond=0)

    # Determine the greeting based on the time
    if morning_start <= current_time < afternoon_start:

        return print("Good Morning nitin!") , s.speak("Good morning nitin")

    elif afternoon_start <= current_time < evening_start:
        return print("Good Afternoon nitin!") , s.speak("Good Afternoon nitin ")
    elif evening_start <= current_time < night_start:
        return print("Good Evening nitin!") , s.speak("Good Evening nitin")
    else:
        return print("Good Night nitin!") , s.speak("Good Night nitin")


# Usage
"""greeting_message = get_greeting()
print(greeting_message)"""
if __name__ =='__main__':
    get_greeting()
