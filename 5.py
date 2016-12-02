#the folling function adds 2 matrices together
def matricesAdd(A,B):
    answer=[]
    #checks dimensions of matrices match
    if len(A) == len(B) and len((A[0])) == len((B[0])):

        # following code goes through matrix adding both matrices together
        for i in range(len(A)):
            row=[]
            for x in range(len(A[0])):
                row.append((A[i][x]+B[i][x]))
            answer.append(row)
            
    print(answer)



#the following function subtracts matrices B from A
def matricesSub(A,B):
    answer=[]

    #checks dimensions of matrices match
    if len(A) == len(B) and len((A[0])) == len((B[0])):

# following code goes through matrix subtracting matrix b from from matrix a
        for i in range(len(A)):
            row=[]
            for x in range(len(A[0])):
                row.append((A[i][x]-B[i][x]))
            answer.append(row)
    print(answer)



#the following function muliplies matrices A and B                              
def matricesMult(A,B):
    answer=[]

    #checks dimensions of matrices
    if len(A)==len(B[0]) and len((A[0]))==len(B):
        
        for x in range(len(A)):
            row=[]
            for y in range(len(B[0])):
                Entry4Matrix=0
                for z in range(len(B)):
                    Entry4Matrix += (A[x][z] * B[z][y])
                row.append(Entry4Matrix)
            answer.append(row)
    print(answer)
            
                
