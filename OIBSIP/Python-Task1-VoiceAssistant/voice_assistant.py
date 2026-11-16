
import datetime
import webbrowser
import speech_recognition as sr
import pyttsx3


# Initialize speech engine
engine = pyttsx3.init()
engine.setProperty("rate", 160)
engine.setProperty("volume", 1.0)


def speak(message):
    print("Assistant:", message)
    engine.say(message)
    engine.runAndWait()


def greet_user():
    hour = datetime.datetime.now().hour

    if hour < 12:
        speak("Good morning!")
    elif hour < 18:
        speak("Good afternoon!")
    else:
        speak("Good evening!")

    speak("Hello! I am your Python Voice Assistant.")
    speak("How can I help you?")


def listen():
    recognizer = sr.Recognizer()

    with sr.Microphone() as source:
        print("Listening...")
        recognizer.adjust_for_ambient_noise(source, duration=1)
        audio = recognizer.listen(source)

    try:
        command = recognizer.recognize_google(audio)
        print("You:", command)
        return command.lower()

    except sr.UnknownValueError:
        speak("Sorry, I could not understand.")
        return ""

    except sr.RequestError:
        speak("Speech service is unavailable. Check your internet.")
        return ""


def process_command(command):

    if "hello" in command:
        speak("Hello! Nice to meet you.")

    elif "time" in command:
        current_time = datetime.datetime.now().strftime("%I:%M %p")
        speak("The current time is " + current_time)

    elif "date" in command:
        today = datetime.datetime.now().strftime("%d-%m-%Y")
        speak("Today's date is " + today)

    elif "google" in command:
        speak("Opening Google.")
        webbrowser.open("https://www.google.com")

    elif "your name" in command:
        speak("My name is Python Voice Assistant.")

    elif "bye" in command or "exit" in command:
        speak("Goodbye! Have a nice day.")
        return False

    else:
        speak("Sorry, I did not understand your command.")

    return True


def main():
    greet_user()

    while True:
        command = listen()

        if command:
            if not process_command(command):
                break


if __name__ == "__main__":
    main()
