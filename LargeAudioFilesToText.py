import speech_recognition as sr
import os
from pydub import AudioSegment
from pydub.silence import split_on_silence

recognizer = sr.Recognizer()

#Split audio file into segments and apply speech recognition
def transribeLargeAudioFile(pathToAudioFile):
    #open large audio file with pydub
    audio = AudioSegment.from_wav(pathToAudioFile)

    #split audio file wherever there is a silence of 500miliseconds or more
    segments = split_on_silence(audio, min_silence_len=500, silence_thresh=audio.dBFS-14, keep_silence=500)

    segmentedAudioFolder = "segmented-audio"
    
    #create directory to store the audio segments
    if not os.path.isdir(segmentedAudioFolder):
        os.mkdir(segmentedAudioFolder)
    
    transcribedAudio = ""

    #process the segments of audio
    for index, segment in enumerate(segments, start=1):
        #export the audio segment and save it in created directory
        segmentFileName = os.path.join(segmentedAudioFolder, f"segment{index}.wav")
        segment.export(segmentFileName, format="wav");

        #use recognizer on the segment and try to convert it to text
        with sr.AudioFile(segmentFileName) as source:
            currentSegment = recognizer.record(source)
            try:
                text = recognizer.recognize_google(currentSegment)
            except sr.UnknownValueError as exception:
                print("Error:", str(exception))
            else:
                text = f"{text.capitalize()}. "
                print(segmentFileName, ":", text)
                transcribedAudio += text
        
    return transcribedAudio

transribeLargeAudioFile("test2.wav")