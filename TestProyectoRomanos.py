import unittest

from DecimalToRoman import decimalToRoman
from RomanToDecimal import romanToDecimal

#DecimalToRoman

class TestsProyectoRomanos(unittest.TestCase):
    def test_1(self):
        resultado = decimalToRoman(1)
        self.assertEqual(resultado, 'I')

    def test_2(self):
        resultado = decimalToRoman(2)
        self.assertEqual(resultado, 'II')

    def test_4(self):
        resultado = decimalToRoman(4)
        self.assertEqual(resultado, 'IV')

    def test_8(self):
        resultado = decimalToRoman(8)
        self.assertEqual(resultado, 'VIII')

    def test_16(self):
        resultado = decimalToRoman(16)
        self.assertEqual(resultado, 'XVI')

    def test_32(self):
        resultado = decimalToRoman(32)
        self.assertEqual(resultado, 'XXXII')
    
    def test_64(self):
        resultado = decimalToRoman(64)
        self.assertEqual(resultado, 'LXIV')

    def test_128(self):
        resultado = decimalToRoman(128)
        self.assertEqual(resultado, 'CXXVIII')

    def test_256(self):
        resultado = decimalToRoman(256)
        self.assertEqual(resultado, 'CCLVI')

    def test_512(self):
        resultado = decimalToRoman(512)
        self.assertEqual(resultado, 'DXII')

    def test_1024(self):
        resultado = decimalToRoman(1024)
        self.assertEqual(resultado, 'MXXIV')

#RomanToDecimal

    def test_I(self):
        resultado = romanToDecimal('I')
        self.assertEqual(resultado, 1)

    def test_II(self):
        resultado = romanToDecimal('II')
        self.assertEqual(resultado, 2)

    def test_III(self):
        resultado = romanToDecimal('III')
        self.assertEqual(resultado, 3)

    def test_V(self):
        resultado = romanToDecimal('V')
        self.assertEqual(resultado, 5)

    def test_X(self):
        resultado = romanToDecimal("X")
        self.assertEqual(resultado, 10)

    def test_VI(self):
        resultado = romanToDecimal('VI')
        self.assertEqual(resultado, 6)

    def test_VII(self):
        resultado = romanToDecimal('VII')
        self.assertEqual(resultado, 7)

    def test_IV(self):
        resultado = romanToDecimal('IV')
        self.assertEqual(resultado, 4)

    def test_IX(self):
        resultado = romanToDecimal('IX')
        self.assertEqual(resultado, 9)

    def test_XI(self):
        resultado = romanToDecimal('XI')
        self.assertEqual(resultado, 11)

    def test_XIV(self):
        resultado = romanToDecimal('XIV')
        self.assertEqual(resultado, 14)
    
    def test_CDXLIV(self):
        resultado = romanToDecimal('CDXLIV')
        self.assertEqual(resultado, 444)
    
    def test_DCLXVI(self):
        resultado = romanToDecimal('DCLXVI')
        self.assertEqual(resultado, 666)
    
if __name__ == '__main__':
    unittest.main()