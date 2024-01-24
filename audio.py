import pyaudio
import time
import audioop
from math import log10
import pyautogui


p = pyaudio.PyAudio()
WIDTH = 2
RATE = int(p.get_default_input_device_info()['defaultSampleRate'])
DEVICE = p.get_default_input_device_info()['index']
alpha = 0.5  
rms = 1

def callback(in_data, frame_count, time_info, status):
    global rms
    rms = audioop.rms(in_data, WIDTH)
    
    rms = (1 - alpha) * rms + alpha * rms
    
    db = 20 * log10(rms)

# Variables à déterminer

    # Variables claquement de doigts
    seuil_micro_min = 70
    seuil_micro_max = 90
    x_micro,y_micro = 50,50
    
    # Variables souffle sur la caméra
    seuil_souffle = 120
    x_camera, y_camera = 50,50
    
    if db > seuil_micro_min and db < seuil_micro_max:
        pyautogui.moveTo(x_micro, y_micro)
        pyautogui.click()
    
    elif db > seuil_souffle :
        pyautogui.moveTo(x_camera,y_camera)
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
        time.sleep(0.1)

except KeyboardInterrupt:
    stream.stop_stream()
    stream.close()
    p.terminate()


p.terminate()

