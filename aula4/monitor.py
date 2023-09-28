import tago
import time
from threading import *

class Monitor():

    def __init__(self, obj):
        self.t1 =Thread(target=self.rodar,daemon=True)
        self.t1.start()
        self.tanque = obj

    
    def rodar(self):
        while True:
            TOKEN = 'da14bbf1-442d-4715-abee-68e7056b408c'
            my_device = tago.Device(TOKEN)
            filter = {
                    'variable': 'nivel',
                    'query': 'last_value',
                    'end_date': '2023-12-25 23:33:22',
                    'start_date': '2021-12-20 23:33:22'
            }
            result = my_device.find(filter)
            # Notificar o tanque
            self.tanque.updateTanque( float(result['result'][0]['value']) )
            time.sleep(5)