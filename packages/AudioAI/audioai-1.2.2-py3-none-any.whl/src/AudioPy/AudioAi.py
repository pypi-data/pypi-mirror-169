import speech_recognition as speech
import os 
from pydub import AudioSegment
from pydub.silence import split_on_silence

audioFilename = ""

def SetAudioFileName (name):
    audioFilename = name
    
def StartShortAudioToText():
    r = speech.Recognizer()
    with speech.AudioFile(audioFilename) as source:
        audio_data = r.record(source)
        text = r.recognize_google(audio_data)
        print(text)

def StartLongAudioToText():
    r = speech.Recognizer()
    sound = AudioSegment.from_wav(audioFilename)  
    chunks = split_on_silence(sound,
        min_silence_len = 500,
        silence_thresh = sound.dBFS-14,
        keep_silence=500,
    )
    folder_name = "audio-chunks"
    if not os.path.isdir(folder_name):
        os.mkdir(folder_name)
    whole_text = ""
    for i, audio_chunk in enumerate(chunks, start=1):
        chunk_filename = os.path.join(folder_name, f"chunk{i}.wav")
        audio_chunk.export(chunk_filename, format="wav")
        with speech.AudioFile(chunk_filename) as source:
            audio_listened = r.record(source)
            try:
                text = r.recognize_google(audio_listened)
            except speech.UnknownValueError as e:
                print("Error:", str(e))
            else:
                text = f"{text.capitalize()}. "
                print(chunk_filename, ":", text)
                whole_text += text
                
def UseMicrophone():
    r = speech.Recognizer()
    with speech.Microphone() as source:
        audio_data = r.record(source, duration=3)
        print("Recognizing...")
        text = r.recognize_google(audio_data)
        print(text)