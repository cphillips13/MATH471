#Use fixed point iteration to find a value of x in [1,2] such that 
# 2sin(pix)+x = 0

import math

results = [1.5]

func = lambda x: -2*math.sin(math.pi*x)

error = 10**-5
eI = 1

iter = 0
while(eI > error):
    results.append(func(results[iter]))
    eI = abs(results[iter+1]-results[iter])
    iter = iter+1

print(results)

