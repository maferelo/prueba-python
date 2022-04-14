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
                    struck = self.get_new_structure()
                    while True:
                        packet = await websocket.recv()
                        try:
                            packet = json.loads(packet)
                        except  ValueError as e:
                            print("Cannot parse response to json {}".format(packet))
                            break
                        struck = self.update_struck(struck, packet)
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

    def get_new_structure(self):
        return self.struck.copy()

    def get_uri(self):
        return self.uri

    def update_struck(self, struck, packet):
        a = packet['a']
        b = packet['b']
        struck['_max_number'] = struck['_max_number'] if b < struck['_max_number'] else b
        struck['min_number'] = struck['min_number'] if b > struck['min_number'] else b
        if a == 1:
            struck['first_number'] = b
        if a == 100:
            struck['last_number'] = b

        struck['number_of_prime_numbers'] += 1 if self.is_prime(b) else 0

        if (b % 2) == 0:
            struck['number_of_even_numbers'] +=1
        else:
            struck['number_of_odd_numbers'] += 1
        
        return struck

    def is_prime(self, n):
        if isinstance(n, int):
            """Returns True if n is prime."""
            # AKS primality test
            if n == 2:
                return True
            if n == 3:
                return True
            if n % 2 == 0:
                return False
            if n % 3 == 0:
                return False

            i = 5
            w = 2

            while i * i <= n:
                if n % i == 0:
                    return False

                i += w
                w = 6 - w

            return True
        else:
            return False

    def start(self):
        asyncio.get_event_loop().run_until_complete(self.main())

if __name__ == '__main__':
    fetcher = Fetcher()
    fetcher.start()