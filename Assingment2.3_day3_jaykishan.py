
# print prime numbers between till 
for j in range(1,201): 
    j=int(input("enter number between:"))
    if j>1:
        for i in range(2,j):
            if (j%i)==0:
                print(j,"is not prime number")
                break
            else:
                print(j,"is prime number")
                break
              
         
