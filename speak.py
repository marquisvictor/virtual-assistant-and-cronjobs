import pyttsx3
import datetime

engine = pyttsx3.init()
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[11].id)
engine.say("Good morning Boss Victor. What do you need me to do for you sir?")
engine.runAndWait()