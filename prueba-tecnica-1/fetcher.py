import asyncio
import json
import websockets
import time

from math import sqrt
from datetime import datetime


class Fetcher:
    def __init__(self):
        self.uri = 'ws://209.126.82.146:8080/'
        self.struck = {
            '_max_number': 0,
            'min_number': 2e32,
            'first_number': 0,
            'last_number': 0,
            'number_of_prime_numbers': 0,
            'number_of_even_numbers': 0,
            'number_of_odd_numbers': 0
        }

    async def main(self):
        counter = 0
        try:
            async with websockets.connect(self.get_uri(), ping_interval=None) as websocket:
                while True:
                    struck = self.get_structure()
                    while True:
                        packet = await websocket.recv()
                        try:
                            packet = json.loads(packet)
                        except  ValueError as e:
                            print("Cannot parse response to json {}".format(packet))
                            break
                        a = packet['a']
                        b = packet['b']
                        struck['_max_number'] = struck['_max_number'] if b < struck['_max_number'] else b
                        struck['min_number'] = struck['min_number'] if b > struck['min_number'] else b
                        if a == 1:
                            struck['first_number'] = b
                        if a == 100:
                            struck['last_number'] = b

                        struck['number_of_prime_numbers'] += self.is_prime(b)

                        if (b % 2) == 0:
                            struck['number_of_even_numbers'] +=1
                        else:
                            struck['number_of_odd_numbers'] += 1
                        
                        
                        #print(packet, type(packet), datetime.now())
                        counter += 1
                        if counter >= 100:
                            break
                        time.sleep(0.1)
                    print(struck)
                    counter = 0
                    time.sleep(60)
        except (OSError, ConnectionRefusedError) as e:
            print("Cannot connect to {} - {}".format(uri, e))

    def get_structure(self):
        return self.struck

    def get_uri(self):
        return self.uri

    def is_prime(self, n):
        prime_flag = 0
        if not isinstance(n, int):
            return prime_flag
        if(n > 1):
            for i in range(2, n):
                if (n % i) == 0:
                    prime_flag = 1
                    break
        return prime_flag

    def start(self):
        asyncio.get_event_loop().run_until_complete(self.main())