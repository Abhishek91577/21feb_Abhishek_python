def sumdiv(number):
    divisors=[1]
    for i in range(2,number):
        if (number%i)==0:
            divisors.append(i)
            return sum(divisors)
print(sumdiv(8))
print(sumdiv(12))

