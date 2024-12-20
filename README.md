# Speech-Engine  
Speech-Engine is a Python module designed for speech recognition, combining the functionalities of the `speech_recognition` library and the Vosk model. It provides a streamlined interface to capture and process audio input from a microphone and convert it into meaningful text.

## Models Used  

### 1. `speech_recognition` Model  
The `speech_recognition` model is used to capture audio input from a microphone. It utilizes the `.listen()` method from its `Recognizer` class to obtain audio data in real-time.  

### 2. Vosk Model  
The Vosk model is employed for offline speech recognition. It utilizes two key classes:  

#### **`Model` Class**  
The `Model` class is used to load the Vosk model for offline speech recognition.  
- The model files need to be specified when creating an instance of the `Model` class.  
- Ensure that the model folder is located at the correct file path, and replace single backslashes (`\`) with double backslashes (`\\`) in the path.

#### **`KaldiRecognizer` Class**  
The `KaldiRecognizer` class processes audio waveforms and converts them into text.  
- Use the `.AcceptWaveForm()` method to process the waveform data.  
- The `.result()` method fetches the recognized text.  
- Any redundant strings in the output are filtered by processing the result string to extract only the necessary text.  

## Recognition Class  
The `Recognition` class is the primary interface of the module, providing two core functions:  

### **`take_command()`**  
This function uses the `speech_recognition` model to capture audio input from a microphone and convert it into a waveform.  
- **Returns**: The captured audio waveform, ready for further processing.  

### **`recognize_command()`**  
This function processes the waveform input and converts it into meaningful text using the Vosk model.  
- **Returns**: A filtered string containing only the necessary information for further operations.  
- Internally uses the `KaldiRecognizer` class with `.AcceptWaveForm()` and `.result()` methods.  

## Testing  
### Prerequisites  
1. **Download Vosk Model**  
   Before testing, download the Vosk model for Indian English from [alphacephei.com](https://alphacephei.com/vosk/models).  
   > *Note*: This repository does not include the model folder due to size constraints. Ensure that the downloaded folder is placed in the correct directory.  

2. **Setup**  
   - Create a Python file in the same directory as the module.  
   - Import the `Recognition` class:  
     ```python  
     from speechEngine import Recognition  
     ```  

### Example  
Here’s a quick example to test the module:  
```python  
# Import the Recognition class  
from speech engine import Recognition  

# Create an instance of the Recognition class  
recognizer = Recognition()  

# Capture audio from the microphone  
waveform = recognizer.take_command()  

# Recognize and process the captured audio  
recognized_text = recognizer.recognize_command(waveform)  

# Print the recognized text  
print(recognized_text)  
```  

## Features  
- Offline speech recognition using the Vosk model.  
- Simple and intuitive interface for audio capture and processing.  
- Customizable for different languages and models.  

## Contributing  
Contributions are welcome! Feel free to fork this repository, submit pull requests, or open issues for feature requests and bug fixes.  
