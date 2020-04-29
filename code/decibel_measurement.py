import pyaudio
import numpy as np
import LED_control as LED
import time
CHUNK = 2**10
RATE = 16000

p = pyaudio.PyAudio()

stream = p.open(
            format = pyaudio.paInt16,
            channels=8,
            rate = RATE,
            input = True,
            frames_per_buffer = CHUNK,
            input_device_index=2
        )
try:
    while(True):
        data = np.fromstring(stream.read(CHUNK), dtype = np.int16)
        decibel = int(np.average(np.abs(data)))
        print(decibel);
        stream.stop_stream()
        if decibel > 1500:
            LED.think(3)
        stream.start_stream()
except KeyboardInterrupt:
    pass

stream.stop_stream()
stream.close()
p.terminate()
