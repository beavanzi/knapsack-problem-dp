
from time import sleep, perf_counter
def knapSack(W, wt, val, n):
    K = [[0 for x in range(W + 1)] for x in range(n + 1)]
    
    start_time = perf_counter()
    for i in range(n + 1):
        for w in range(W + 1):
            if i == 0 or w == 0:
                K[i][w] = 0
            elif wt[i-1] <= w:
                K[i][w] = max(val[i-1]
                          + K[i-1][w-wt[i-1]], 
                              K[i-1][w])
            else:
                K[i][w] = K[i-1][w]
    end_time = perf_counter()
    print(f'Tempo para completar {end_time- start_time} ms.')
 
    return K[n][W]
 
wt = [23,31,29,44,53,38,63,85,89,82]

val = [92,57,49,68,60,43,67,84,87,72]
W = 165
n = len(val)


print(knapSack(W, wt, val, n))


