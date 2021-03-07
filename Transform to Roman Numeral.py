"""
Transform to Roman Numeral

Write a code that can convert integers to Roman numerals from 1 through 1000.

Example:

I = 1
IV = 4
V = 5
IX = 9
X = 10
XI = 11
L = 50
C = 100
D = 500
M = 1000

"""

def transformToRoman(num):
    table= {
        1000: 'M',
        900: 'CM',
        500: 'D',
        400: 'CD',
        100: 'C',
        90: 'XC',
        50: 'L',
        40: 'XL',
        10: 'X',
        9: 'IX',
        5: 'V',
        4: 'IV',
        1: 'I'
    }

    sol = ''
    for key in table:
        while(True):
            if key > num:
                break
            num -= key
            sol += table[key]
    return sol
