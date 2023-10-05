def to_roman(num):
    romanAnswer = ''

    roman_values = {
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
    priority_list = list(roman_values.keys())

    for key in priority_list:
        while num >= roman_values[key]:
            romanAnswer += key
            num -= roman_values[key]
    
    return romanAnswer


