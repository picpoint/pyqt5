import random

numbers = '1234567890'
res = ""

for i in range(1, 8):
    rand_numb = random.choice(numbers)
    print(rand_numb)
    res += rand_numb 


print(res)