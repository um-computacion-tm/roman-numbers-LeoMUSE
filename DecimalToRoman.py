def decimalToRoman(num):
    m = ["", "M"]
    c = ["", "C", "CC", "CCC", "CD", "D", "DC", "DCC", "DCCC", "CM"]
    x = ["", "X", "XX", "XXX", "XL", "L", "LX", "LXX", "LXXX", "XC"]
    i = ["", "I", "II", "III", "IV", "V", "VI", "VII", "VIII", "IX"]

    mil = m [num // 1000]
    cien = c [(num % 1000) // 100]
    diez = x [(num % 100) // 10]
    uno = i [num % 10]
  
    resultado = (mil + cien + diez + uno)
  
    return resultado

if __name__ == '__main__':
    pass
