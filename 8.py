### a recursive function to remove all vowels from a input of a string
def RemoveVowels(string):
    if len(string)== 0:
        return string
    elif string[0] in "AEIOUaeiou":
        return RemoveVowels(string[1:])
    else:
        return string[0]+RemoveVowels(string[1:])
