import math
def is_prime(n:int):
    """
    return true if n is prime, Otherwise False
    """
    temp = [2,3]
    if n in temp:
        return True
    if n%2 == 0 or n%3 == 0 or n < 0:
        return False
    if(n+1)%6 == 0 or (n-1)%6 == 0:
        sq = math.ceil(math.sqrt(n))
        j = int(sq//6)
        if(sq == math.ceil(math.sqrt(n))):
            j += 1
        for i in range(1,j+1):
            if n % (6*i - 1) == 0:
                return False
            if n % (6*i + 1) == 0:
                return False
        return True
    return False



Plist = [119311, 109621, 147571, 103289, 124753, 103483, 189517, 178249, 130681, 108193, 124541, 126923, 135977, 189239, 159463]
for i in Plist:
    print(is_prime(i))

