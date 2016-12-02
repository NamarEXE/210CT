### function works out the factorial and counts the trailing zeros in it.
def trailing0s(factorialNumber):

###works out the answer of the factorial
    nextnumber=2
    answer=1
    while factorialNumber>=nextnumber:
        answer=answer*nextnumber
        nextnumber=nextnumber+1
    
### count the number of trailing 0s in the answer with the variable count
    answerstring=str(answer)
    count=0
    while answerstring[-1]=="0":
        count=count+1
        answerstring=answerstring[:-1]
        
    print("the number of trailing 0s is "+str(count))
    
