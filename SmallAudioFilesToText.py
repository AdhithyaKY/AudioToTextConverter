import speech_recognition as sr

filename = "test1.wav"


#list microphones 
for index, name in enumerate(sr.Microphone.list_microphone_names()):
    print("Microphone with name \"{1}\" found for `Microphone(device_index={0})`".format(index,name))
#initialize recognizer

recognizer = sr.Recognizer()

#open audio file, load audio into memory, and convert from speech to text using google API.
with sr.AudioFile(filename) as source:
    audio_data = recognizer.record(source)
    result_text = recognizer.recognize_google(audio_data)
    print(result_text)
