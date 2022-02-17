# -*- coding: utf-8 -*-

"""
tworzenie testu jednostkowego
1. zaimportowanie unitest
2. zdefiniowanie funkcji do testowania
3. stworzenie przypadku testowego używając klasy unitest.TestCase
4. zdefiniowanie testu jako metody klasy TestCase
5. call assert function
6. assert function wysoła błąd assertionError jeżeli otrzymamy błąd
5. wywołaj funkcję main() z modułu unitest
"""

import unittest


def add(x, y):
    return x + y


class SimpleTest(unittest.TestCase):
    
    def test_add(self):
        self.assertEqual(add(3, 4), 7, msg = 'Powinno być 7')

if __name__ == '__main__':
    unittest.main()        