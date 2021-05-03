prime_numbers = []


for i in range(1, 100):
    #if prime_numbers == []:
     #   prime_numbers.append(i)
    count = 0
    if i % i == 0:
        count += 1
    for x in prime_numbers:
        if i % x == 0 :
            count += 1
    
    if count <= 2 and i != 1: 
        prime_numbers.append(i)
            
        

print(f"Prime number list: {prime_numbers}")