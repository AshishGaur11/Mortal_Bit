
import speech_recognition 
import pyttsx3

engine = pyttsx3.init()
recognizer = speech_recognition.Recognizer()
with speech_recognition.Microphone() as source:
    print("say it")
    audio = recognizer.listen(source)
    words = recognizer.recognize_google(audio)
    
    if "Hello" or "Hey" or "How are you" in words:
        engine.say("google is nice to let us there")
        engine.runAndWait()
    else:
        print("huh")

