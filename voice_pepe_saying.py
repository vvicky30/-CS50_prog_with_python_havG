# here first we have to install 'pyaudio' liberary 
# this liberary  provides Python bindings for PortAudio v19, the cross-platform audio I/O library. With PyAudio, you can easily use Python to play and record audio on a variety of platforms, such as GNU/Linux, Microsoft Windows, and Apple macOS.
# pip install pyaudio
# then we going to install SpeechRecognition liberary of python 

"""
The reason we install PyAudio even though we're not directly going to use it in the Python script is 
because the SpeechRecognition library uses PyAudio under the hood to handle the audio stream from the microphone.

When we use the SpeechRecognition library, particularly with the line with sr.Microphone() as source:, 
PyAudio is implicitly utilized to open the default microphone device and capture audio data continuously until the recording is stopped. 
This audio data is then processed by the SpeechRecognition library to perform the speech-to-text conversion.

Here’s a breakdown of the roles each component plays in the process:

PyAudio: This library provides Python bindings for PortAudio, the cross-platform audio I/O library. 
It allows Python programs to record and play audio on a variety of platforms. 
In the context of our script, PyAudio is responsible for interfacing with the system's audio hardware to capture microphone input.

SpeechRecognition: This library provides easy-to-use abstractions to convert speech into text. 
It leverages various engines and APIs, including Google Web Speech API, Microsoft Bing Voice Recognition, and others. 
When you call recognizer.listen(source), where source is obtained via sr.Microphone(), 
SpeechRecognition internally uses PyAudio to manage the microphone stream.
Without PyAudio installed, attempting to run a script that uses sr.Microphone() will result in an error 
because SpeechRecognition cannot access the audio hardware to perform its function. 
Hence, PyAudio is a necessary dependency for recording audio through the microphone when using the SpeechRecognition library in Python.

"""
import speech_recognition as sr 

def main():
    listen_then_recognize()
    
    
    
def listen_then_recognize():
    # first of all here we're going to make recognizer through initializing it with recognizer's constructor
    recogniser = sr.Recognizer() # this creates a recognizer instance
    
    #now we're going to take audio-input stream by acessing the system's default microphone
    '''
    Using the with statement in Python, particularly when working with resources like files or hardware devices, 
    it ensures that the resource is properly managed and released when it's no longer needed. 
    In the context of the SpeechRecognition library and the Microphone instance, using the with statement ensures proper initialization and cleanup of the microphone resource.

    Here's why the with statement is used when working with the default microphone:

    Resource Management: When you create a Microphone instance using sr.Microphone(), you're essentially accessing an audio input device (microphone). 
    This device is a system resource that needs to be properly managed. The with statement ensures that the Microphone instance is properly initialized before the indented block is executed 
    and that it's properly released afterward.
    
    Context Manager: The Microphone class is designed to act as a context manager in Python. This means it implements the __enter__() and __exit__() methods, 
    allowing it to be used with the 'with' statement. When you enter the with block, the __enter__() method of the Microphone class is called, which initializes the microphone resource. 
    When you exit the with block, the __exit__() method is called, which releases the microphone resource.
    Error Handling: The with statement also provides a built-in mechanism for error handling and cleanup. If an exception occurs within the with block, 
    the __exit__() method of the context manager (in this case, the Microphone instance) is still called, allowing for proper cleanup of resources, such as releasing the microphone.
    '''
    with sr.Microphone() as source:
        print("we're currently using your Default microphone \n Listening...Go ahead!!")
        
        #adjusting the recogniser sensitivity to ambient noise
        recogniser.adjust_for_ambient_noise(source)
        #now going to record audio from microphone 
        audio = recogniser.listen(source)
    try:
         # Using Google Web Speech API to recognize the audio and transcribe it 
        text = recogniser.recognize_google(audio)
        print("you said: "+ text)
    except sr.UnknownValueError:
        print("Google Speech Recognition could not understand you ..please try again")
    except sr.RequestError as e:
        print(f"Could not request results from Google Speech Recognition service; {e}")
        
        
if __name__ == "__main__":
    main()

'''
we're unusually going to encounter error like this:"ModuleNotFoundError: No module named 'disutils'" generally disutils module installed bydefault in python. 
but distutils package is removed in python version 3.12
It was deprecated in Python 3.10 by PEP 632 “Deprecate distutils module”. For projects still using distutils and cannot be updated to something else, 
the setuptools project can be installed: it still provides distutils.
Explanation and workaround:
Python 3.12 Release document mentions :
gh-95299: Do not pre-install setuptools in virtual environments created with venv. 
This means that distutils, setuptools, pkg_resources, and easy_install will no longer available by default; 
to access these:
run pip install setuptools (in the activated virtual environment only.) 
'''
