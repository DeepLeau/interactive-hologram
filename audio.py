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

# Les variables seuil, x et y sont à changer selon tes besoins, x et y = coordonnées de la position où tu veux mettre la souris et seuil c'est le seuil à partir du quel tu considères que ca fasse un claquement de doigts

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
        time.sleep(0.1)  

except KeyboardInterrupt:
    stream.stop_stream()
    stream.close()
    p.terminate()


p.terminate()

