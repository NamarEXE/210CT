def BinaryS(Array, Low, High):
    length=len(Array)

    if length == 1:
        if Array[0] <= High and Array[0] >= Low:
            print(True)
        if Array[0] < Low or Array[0] > High:
            print(False)

    elif length==2:
        if (Array[0] <= High and Array[0] >= Low) or (Array[1] <= High and Array[1] >= Low):
            print(True)
        else:
            print(False)

#checks if middle element is within intervals
    elif Array[((length-1)//2)] <= High and Array[((length//2)-1)] >= Low:
        print(True)

# if middle element is less than the higher interval value discards upper half of array and recalls function
    elif Array[((length-1)//2)] < High:
        midpoint=(length//2)
        Array=Array[midpoint:]
        BinaryS(Array, Low, High)

# if middle element is more than the lower interval value discards lower half of array and recalls function          
    elif Array[((length-1)//2)] > Low:
        midpoint=(length//2)
        Array=Array[:midpoint]
        BinaryS(Array, Low, High)
          
    else:
        print(False)



    
