def two_sum(numbers, target):
    """
    accepts a array of numbers and a target number
    returns a tuple of two numbers having sum equal to target
    """
    for i in range(0,len(numbers)):
        if(numbers[i] < target):
            temp = target - numbers[i]
            if temp in numbers:
                if(i != numbers.index(temp)):
                    return (i,numbers.index(temp))

s1 = [1,2,3]
print(two_sum(s1,4))
print(two_sum([1234,5678,9012], 14690))
