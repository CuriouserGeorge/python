def is_prime(num):
    x = True
    if num == 1:
        return False
    
    for i in range(2,num):
        print(i)
        y = num % i
    	print(y)
        if y > 0:
            x = False
    return x
  	
