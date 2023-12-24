import simpleaudio
import os
import threading
import sys
import time

def resource_path(relative_path):
    if hasattr(sys, '_MEIPASS'):
        return os.path.join(sys._MEIPASS, relative_path)
    return os.path.join(os.path.abspath("."), relative_path)

wav1_obj = simpleaudio.WaveObject.from_wave_file((resource_path("./sounds/chime.wav")))


class ChimeRing():
    def __init__(self, filename=resource_path("./sounds/chime.wav")) -> None:
        self.wav_obj = simpleaudio.WaveObject.from_wave_file(filename)
    
    def chime(self, count, delay=0.5):
        thread = threading.Thread(target=self.__chime, args=[count, delay])
        thread.start()

    def __chime(self, count, delay):
        for _ in range(count):
            play_obj = self.wav_obj.play()
            time.sleep(delay)
        play_obj.wait_done()


if __name__ == '__main__':
    # chime(2)
    c = ChimeRing()
    c.chime(3)