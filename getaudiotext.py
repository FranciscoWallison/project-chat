#pinheirocfc@gmail.com
#Orientacoes em: https://youtu.be/vjXsa0I_dtc

#Essenciais
#pip install SpeechRecognition

#Extras
#pip install pipwin
#pipwin install pyaudio
#pip install pydub

#sudo apt update
#sudo apt install ffmpeg

import speech_recognition as sr
from pydub import AudioSegment
import os

directory = os.path.abspath('.') + "/audios/16327880741157603-audio.mp3"# current directory
# convert mp3 file to wav  
sound = AudioSegment.from_mp3(directory)
sound.export(directory.replace(".mp3",".wav"), format="wav")

def reconhecer_fala():    
    microfone = sr.Recognizer() #Habilita o microfone
    sample_audio = sr.AudioFile(directory.replace(".mp3",".wav"))

    with sample_audio as source:
        audio_text = microfone.record(source)
        try:
            print(microfone.recognize_google(audio_text,language='pt-BR'))
        except:
            print("Não entendi o que você disse!")
reconhecer_fala()