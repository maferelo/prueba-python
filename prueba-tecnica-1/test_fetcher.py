import unittest

from fetcher import Fetcher

class TestFetcher(unittest.TestCase):

    def test_fetcher_is_prime(self):
        fetcher = Fetcher()
        for n in (1,2,3,5,7):
            self.assertEqual(fetcher.is_prime(n), True)
        for n in (4,6,9,10):
            self.assertEqual(fetcher.is_prime(n), False)
        self.assertEqual(fetcher.is_prime("n"), False)
    
    def test_fetcher_get_uri(self):
        fetcher = Fetcher()
        uri = 'ws://209.126.82.146:8080/'
        self.assertEqual(fetcher.get_uri(), uri)

if __name__ == '__main__':
    unittest.main()