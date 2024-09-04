import speech_recognition as sr

recognizer = sr.Recognizer()

mic = sr.Microphone()

with mic as source:

    audio = recognizer.listen(source)

text = recognizer.recognize_google(audio, language = 'es-CO')

print(f'Has dicho: {text}')
print(type(audio)) #aca sabremos cual es el tipo de dato que se esta manejando

