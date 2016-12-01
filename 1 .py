import random

### the following function shuffles the given array input
###the array must be created first,before its used as the input for the function

def Shuffle(array):
    CopyOfArray=array
    NewArray=[]
    size=(len(array))

### the following loop removes random elements from copy inserting into new randomised list 
    
    while (size != 0):
        randomnumber=(random.randint(0,size))
        element=(CopyOfArray[randomnumber-1])
        NewArray.append(element)
        del CopyOfArray[randomnumber-1]
        size=(len(CopyOfArray))
        
    print("the following is the randomised list")
    return NewArray

# the rational behind the implementation:
# creates a copy of the original list
# remove a random element from the copy and insert this element
# into a new list
# once the copy of the list has no more elements remaining in it
# all elements have been added to the new list and are now in a new order which is random
# therefor we have created a copy of the orinal list in a random order
