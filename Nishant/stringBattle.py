def stringBattle_1Letter(factor):
    if not isinstance(factor, int or float):
        raise TypeError
    myString = input("Type in your opponent's text: ")
    if not isinstance(myString, str):
        raise TypeError
    newLength = len(myString[1:]) + factor
    newStr = myString[0] + (newLength * myString[1:])
    return newStr

print(stringBattle_1Letter(5))
