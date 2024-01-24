import pyaudio
import time
import audioop
from math import log10
import pyautogui


p = pyaudio.PyAudio()
WIDTH = 2
RATE = int(p.get_default_input_device_info()['defaultSampleRate'])
DEVICE = p.get_default_input_device_info()['index']
alpha = 0.5  # Facteur de lissage (entre 0 et 1)
rms = 1

def callback(in_data, frame_count, time_info, status):
    global rms
    rms = audioop.rms(in_data, WIDTH)
    
    rms = (1 - alpha) * rms + alpha * rms
    
    db = 20 * log10(rms)

# A définir !!

    seuil = 70
    x,y = 50,50
    
    if db > seuil:
        pyautogui.moveTo(x, y)
        pyautogui.click()

    print(f"Décibels: {db}")
    
    return in_data, pyaudio.paContinue

stream = p.open(format=p.get_format_from_width(WIDTH),
                input_device_index=DEVICE,
                channels=1,
                rate=RATE,
                input=True,
                output=False,
                stream_callback=callback)

stream.start_stream()

try:
    while stream.is_active():
        time.sleep(0.1)  # Vous pouvez ajuster l'intervalle de temps si nécessaire

except KeyboardInterrupt:
    # Arrêtez le flux lorsqu'une interruption clavier se produit
    stream.stop_stream()
    stream.close()
    p.terminate()


p.terminate()

