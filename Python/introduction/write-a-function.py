def is_leap(year):
    leap = False
    '''
    Tahun yang habis dibagi empat disebut tahun kabisat, kecuali tahun
    itu habis dibagi 100, terkecuali lagi tahun yang habis dibagi 400.
    '''
    if year % 400 == 0 :
        leap = True
    elif year % 100 == 0 :
        leap = False
    elif year % 4 == 0 :
        leap = True
    
    return leap

year = int(input())
print(is_leap(year))