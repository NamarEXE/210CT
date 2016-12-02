### checks if the input value is prime or not the index entered by the user must always be 2
def Prime(n,index):
    prime=True
    if n == 0 or n == 1:
        prime=False
        return prime
    elif index<n:
        remainder=n%index
        if remainder == 0:
            prime=False
            return prime
        elif remainder>=1:
            prime = True
            return(Prime(n,index+1))
    return prime
    
