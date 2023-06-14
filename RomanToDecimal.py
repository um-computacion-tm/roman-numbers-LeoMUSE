def romanToDecimal(num):
    romanAndDecimal = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
    decimal = 0
    newNum = 0
    
    for numeral in num:
        oldNum = romanAndDecimal[numeral]
        decimal += oldNum
        
        if newNum < oldNum:
            decimal -= 2 * newNum
        
        newNum = oldNum
        
    return decimal
    
if __name__ == '__main__':
    pass
