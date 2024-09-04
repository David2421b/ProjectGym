import ollama
import speech_recognition as sr

def chatOllama(mensaje):
    response = ollama.generate(model = "llama3.1:latest", prompt = mensaje)
    return response['response']

recognize = sr.Recognizer()

mic = sr.Microphone()

with mic as source:
    audio = recognize.listen(source)

text = recognize.recognize_google(audio, language = 'ES')

print(f"tu pregunta fue: {text} \n")

print(chatOllama(text))
