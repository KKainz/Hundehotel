import unittest
from hundehotel.hotel import Hund


class HundeTest(unittest.TestCase):

   # @classmethod
   # def setUpClass(cls) -> None:
   #   print("Einmal isgesamt aufgerufen zum initialisieren")
   #   pass

    # @classmethod
    # def tearDownClass(cls) -> None:
    #   print("Einmal insgesamt aufgerufen am Ende meines Tests")
    #   pass

    def setUp(self) -> None:
        self.hund = Hund("Kommissar Rex", 10, ['semmel', 'extrawurst'])
        print("einmal vor jedem test")
        pass

    # def tearDown(self) -> None:
    #    print("einmal nach jedem Test")
    #    pass

    def test_allergie_positiv(self):
        # hier teste ich meine funktionalität
        erg = self.hund.ist_allergisch("semmel")
        # und dann überprüfe ichj die korrektheit meines ergebnisses
        self.assertTrue(erg, "positive Allergie erkannt")

    def test_allergie_negativ(self):
       erg = self.hund.ist_allergisch("brot")
       self.assertFalse(erg, "keine Allergie erkann")



if __name__ == '__main__':
    unittest.main()
