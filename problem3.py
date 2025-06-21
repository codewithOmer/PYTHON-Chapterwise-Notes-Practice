# Install an external module and use it to perform anoperation of your interest.

# type pip install pyttsx3 in terminal and copy the usage for google

import pyttsx3
engine = pyttsx3.init()
engine.say("my name is mohammed omer")
engine.runAndWait()