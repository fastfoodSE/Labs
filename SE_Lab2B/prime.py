prime = []
def PrimeNumber(x):
	if(type(x) != int):
		raise TypeError("Please pass an integer as a parameter")
	if(x < 0):
		raise Exception("Please pass a positive integer")

	if(x < 2):
		raise Exception("Invalid input, input should be an integer greater than one to produce the prime number")
	
	i = 0
	while(i < x):
		if(i ==2 or i ==3):
			prime.append(i)
		elif(i == 1 or i == 0):
			pass
		else:
			half_number = int(i/2)+1
			for divisor in range(2,half_number):
				
				if(i%divisor==0):
					break
				
				if(divisor == half_number-1):
					prime.append(i)
					print(prime)			
		i +=1
	
	return prime

n = len(prime)
print(n)
	
