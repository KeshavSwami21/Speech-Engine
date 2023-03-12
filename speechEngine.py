import speech_recognition as sr
from vosk import KaldiRecognizer,Model

class Recognition:
    '''
    this class is used to convert speech through microphone to text
    '''
    def take_command(self):
        # this function takes input from microphone and convert it to wave form
        r = sr.Recognizer()
        with sr.Microphone() as source:
            # Listen for audio input from the microphone
            r.pause_threshold=1.2
            audio = r.listen(source)
            # Convert the audio input to a format that Kaldi can process
            audio_data = audio.get_raw_data(convert_rate=16000, convert_width=2)
        return audio_data
    
    def recognize_command(self,audio):
        # this takes wave form audio in input and return the recognized text
        model = Model("E:\\inovatex\\vosk-model-small-en-in-0.4")
        rec = KaldiRecognizer(model,16000)
        rec.AcceptWaveform(audio)
        text = rec.Result()
        s=''
        b=False
        if text:
            #the below code is used to make the string contain only recognised string and nothing extra
            for i in text:
                if i == ':':
                    b=True
                    continue
                if b == True and i!="}":
                    s+=i
            return s
        else:
            return False


       




