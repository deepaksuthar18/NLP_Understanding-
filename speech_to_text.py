import speech_recognition as sr
import pyttsx3


# speech to text

r = sr.Recognizer()
with sr.Microphone() as source:
    print("Please say something:")
    audio = r.listen(source)
    text = r.recognize_google(audio)
    print("You said: " + text)
    
# text to speech
engine = pyttsx3.init()
engine.say(text)
engine.runAndWait()