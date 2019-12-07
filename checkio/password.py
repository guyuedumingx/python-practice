def checkio(data: str) -> bool:
    wordlong = False
    number = False
    upper = False
    lower = False
    if (len(data) < 10):
        return False 
    for i in list(data):
        if (str.isdigit(i)):
            number = True
        if (str.isupper(i)):
            upper = True
        if (str.islower(i)):
            lower = True
    if (number and lower and upper):
        return True
    else:
        return False

#Some hints
#Just check all conditions


if __name__ == '__main__':
    #These "asserts" using only for self-checking and not necessary for auto-testing
    assert checkio('A1213pokl') == False, "1st example"
    assert checkio('bAse730onE4') == True, "2nd example"
    assert checkio('asasasasasasasaas') == False, "3rd example"
    assert checkio('QWERTYqwerty') == False, "4th example"
    assert checkio('123456123456') == False, "5th example"
    assert checkio('QwErTy911poqqqq') == True, "6th example"
    print("Coding complete? Click 'Check' to review your tests and earn cool rewards!")
