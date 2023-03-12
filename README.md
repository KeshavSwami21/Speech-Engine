# Speech-Engine
it is a module in which there is a class named recognition it uses speech_recognition model and vosk model

# speech_recognition model
it is used to take input from microphone by using .listen() meathod from its Recognizer class

# vosk model
it is used to recognize the wave form audio we used two class from it:

->Model class:

we used it to create a model from which we can recognize the audio offline with the files in our system.The location of file must be added to Model class constructor to make model.

the folder which is added must be in the exact location and "\" must be replaced by "\\" in the path

->KaldiRecognizer class:

it is the recognizer which we use to recognize what the audio is saying. We used AcceptWaveForm() to recognize the wave file then use result() to fetch the recognized text

but text have some redundent string so we remove it by traversing the string and gets the recognized text only

# Recognition Class
In this class we have two different functions take_command() and recognize_command()

# take_command()
In this function we used speech_recognition model it is used to just take input from the microphone and convert it to wave form so kaldi can recognize it

it returns the wave form of the input from microphone

# recognize_command()
as the name suggest recognize the audio in wave form and returns the its output in form of string and returns a filtered string with only neccessary info to make further searching faster it uses class KaldiRecognizer() and meathod .AcceptWaveForm() and .result()


# Testing
to test it first make sure you download the model file for indian eng from https://alphacephei.com/vosk/models i was not able to upload the folder directly on git hub so make sure you download it first

then create a python file in same directory and import the Recognize class as : 

from speechEngine import Recognize

then create an object for Recognize class and and use the meathod above the output from take_command() will serve as input for recognize_command()
