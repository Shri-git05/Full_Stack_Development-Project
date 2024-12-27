import speech_recognition as sr
import pyttsx3
from googletrans import Translator

def recognize_speech_from_mic(language_code="en-US"):
    recognizer = sr.Recognizer()
    mic = sr.Microphone()

    try:
        # Listen to the microphone
        with mic as source:
            print("Adjusting for ambient noise... Please wait.")
            recognizer.adjust_for_ambient_noise(source)  # Calibrate for ambient noise
            print("Listening for speech...")
            audio = recognizer.listen(source)  # Listen to the speech
        
        # Recognize speech using Google Web Speech API
        print("Recognizing...")
        recognized_text = recognizer.recognize_google(audio, language=language_code)
        return recognized_text
    
    except sr.UnknownValueError:
        return None  # Couldn't understand the audio
    except sr.RequestError as e:
        return f"Error with speech recognition service: {e}"
    
def text_to_speech(text):
    engine = pyttsx3.init()  # Initialize the pyttsx3 engine
    engine.say(text)  # Pass the text to the engine to be spoken
    engine.runAndWait()
    
def translate_text(text, target_language='en'):  # Default to Spanish
    translator = Translator()
    translated = translator.translate(text, dest=target_language)
    return translated.text
