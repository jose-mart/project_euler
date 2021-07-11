num = 999

def sumDivisibleBy(n : int) -> float:
    p = int(num / n)
    return n*(p*(p+1))/2

print(sumDivisibleBy(3) + sumDivisibleBy(5) - sumDivisibleBy(15))