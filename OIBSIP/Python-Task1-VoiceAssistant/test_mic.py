import speech_recognition as sr

recognizer = sr.Recognizer()

print("Speak now...")

try:
    with sr.Microphone() as source:
        recognizer.adjust_for_ambient_noise(source, duration=2)
        print("Listening...")
        audio = recognizer.listen(
            source, timeout=10, phrase_time_limit=5
        )

    text = recognizer.recognize_google(audio)
    print("You said:", text)

except Exception as error:
    print("Error:", error)