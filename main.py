import speech_recognition as sr
import pyttsx3
import pywhatkit #web scrapping
import datetime
import wikipedia
import pyjokes
listener = sr.Recognizer()  # It creates a Recognizer object, which is used to recognize speech.
engine = pyttsx3.init()  # is used to initialize the text-to-speech (TTS) engine provided by the pyttsx3 library. This initializes a TTS engine instance that you can use to convert text into speech.
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[1].id)


def talk(text):
    engine.say(text)
    engine.runAndWait()


def take_command():
    try:
        with sr.Microphone() as source:  # This creates a context manager using a microphone as the audio source. This means it will listen to audio from your computer's microphone.

            print("Listening....")
            voice = listener.listen(source)  # It listens to audio from the microphone source and stores the audio data in the voice variable.

            command = listener.recognize_google(voice)  # It uses Google's speech recognition service to convert the audio data in voice into text. The recognized text is stored in the command variable.

            command = command.lower()

            if 'friday' in command:
                command = command.replace('friday', '')#remove friday from command so it will be searched without the word  friday
                talk(command)

    except:  # is used to catch and ignore any exceptions that may occur during the process.
        pass

    return command


def run_edith():
    command = take_command()

    if 'play ' in command:
        song=command.replace('play','')
        talk('playing'+song)
        pywhatkit.playonyt(song)

    elif 'time' in command:
        time=datetime.datetime.now().strftime('%I:%M %p')
        talk('the time is '+time)

    elif 'search' in command:
        ans=command.replace('search','')
        info=wikipedia.summary(ans,1)
        talk(info)
        print(info)
    elif 'who are you' in command:
        talk("i am your voice assistant ")
    elif 'joke' in command:
        ans=pyjokes.get_joke()
        talk(ans)
        print(ans)



run_edith()
