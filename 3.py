### the following function finds the highest perfect square which is below the input value 

def HighestPerfectSQ(inputValue):

### the loop iterates until the NexthighestSQ goes over the input value at which stage we take the previous highest square
    highestSQ=1
    NexthighestSQ=4
    index=1
    while NexthighestSQ<=inputValue:
        highestSQ=index**2
        index=index+1
        NexthighestSQ=index**2
    print(highestSQ)
