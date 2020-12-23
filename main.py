# import speech_recognition as sr
# import pyaudio

# listener = sr.Recognizer()

# try:
#     with sr.Microphone() as source:
#         print("LISTENING YOU DUMB FUCK")
#         # voice = listener.listen(source)
#         # command = listener.recognize_google(voice)
#         # print(command)
# except:
#     pass

# # p = pyaudio.PyAudio()

from ctypes import CFUNCTYPE, cdll, c_char_p, c_int, c_char_p, c_int, c_char_p
from contextlib import contextmanager
import pyaudio
import speech_recognition as sr

ERROR_HANDLER_FUNC = CFUNCTYPE(None, c_char_p, c_int, c_char_p, c_int,
                               c_char_p)


def py_error_handler(filename, line, function, err, fmt):
    pass


c_error_handler = ERROR_HANDLER_FUNC(py_error_handler)


@contextmanager
def noalsaerr():
    asound = cdll.LoadLibrary('libasound.so')
    asound.snd_lib_error_set_handler(c_error_handler)
    yield
    asound.snd_lib_error_set_handler(None)


listener = sr.Recognizer()

with noalsaerr():
    try:
        with sr.Microphone() as source:
            print("listening you dumb fuck...")
            voice = listener.listen(source)
            command = listener.recognize_google(voice)
            command = command.lower()
            if 'alexa' in command:
                command = command.replace('alexa', '')
                print(command)
    except:
        pass
