def to_roman(num):
    romanAnswer = ''

    romanValues = {
        'M': 1000,
        'CM': 900,
        'D': 500,
        'CD': 400,
        'C': 100,
        'LC': 90,
        'L': 50,
        'XL': 40,
        'X': 10,
        'IX': 9,
        'V': 5,
        'IV': 4,
        'I': 1
    }
    for key in romanValues:
        while num >= romanValues[key]:
            romanAnswer += key
            num -= romanValues[key]
    
    return romanAnswer
