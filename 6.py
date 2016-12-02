### the following function reverses the input of a string
def ReverseStr(string):
    SplitStr=string.split()
    length=len(SplitStr)
    newstring=""
    i=1
    
    while i<=length:
        nextword=SplitStr[-i]
        newstring +=str(nextword)
        newstring +=" "
        i += 1
    print(newstring)

    
