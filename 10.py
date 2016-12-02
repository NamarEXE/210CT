### the following function finds the largest accending subsequence

def subseq(array):
    largestsubsequence=[]
    
### the while loop ends when the whole list has been checked
    while len(array)!=1:
        countsubsequence=[(array[0])]
        
# while the next element is larger than the previous,add the next element to the countsubsequence and deletes the first element in the original array so the loop can repeat and compare the next item
        while array[0]<array[1]:
            countsubsequence.append(array[1])
            del array[0]

            #allows while loop to end once list becomes too small
            if len(array)==1:
                array=[5,4]
        #if the next element is not higher deletes the first and the next element now becomes the first
        if array[0]>array[1]:
            del array[0]
### if the countsubsequence is larger than largestsubsequence it gets stored as the largestsubsequence
        if len(countsubsequence)>len(largestsubsequence):
            largestsubsequence=countsubsequence

    print(largestsubsequence)



