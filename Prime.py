def isPrime(num):
    if num%1==0 and num%num==0 and num>1:
       for i in range(2,100):
           
            if num%i!=0 and num!=num:
                return True
            else:
                return False
    else:
        return False
for i in range(1, 20):
	if isPrime(i + 1):
			print(i + 1, end=" ")
