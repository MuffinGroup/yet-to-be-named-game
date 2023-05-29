import time

def start_timer():
    start_time = time.time()
    print("Das Spiel hat begonnen!")
    
    while True:
        elapsed_time = time.time() - start_time
        minutes = int(elapsed_time // 60)
        seconds = int(elapsed_time % 60)
        milliseconds = int((elapsed_time * 1000) % 1000)
        
        # Formatierung der Zeit in HH:MM:SS.mmm
        time_format = "{:02d}:{:02d}:{:03d}".format(minutes, seconds, milliseconds)
        
        # Ausgabe der aktuellen Zeit
        print("Verstrichene Zeit:", time_format)
        
        # Verzögerung von 1 Millisekunde, um den Prozessor nicht zu überlasten
        time.sleep(0.001)

# Beispielaufruf
start_timer()
