# TODO: to parallel this code.
from time import sleep, perf_counter
from threading import Thread

def loopKnap(W, wt, val, init,n,K):
    for i in range(init,n + 1):
        for w in range(W + 1):
            if i == 0 or w == 0:
                K[i][w] = 0
            elif wt[i-1] <= w:
                K[i][w] = max(val[i-1]
                          + K[i-1][w-wt[i-1]], 
                              K[i-1][w])
            else:
                K[i][w] = K[i-1][w]
    return

def knapSack(W, wt, val, n):
    K = [[0 for x in range(W + 1)] for x in range(n + 1)]
 
    t1 = Thread(target=loopKnap,args=(W, wt, val,0, n//2,K))
    t2 = Thread(target=loopKnap,args=(W, wt, val,n//2, n,K))
 
        # start the threads
    t1.start()
    t2.start()

    # wait for the threads to complete
    t1.join()
    t2.join()

    
    return K[n][W]
 
 
start_time = perf_counter()
val = [60, 100, 120]
wt = [10, 20, 30]
W = 50
n = len(val)
print(knapSack(W, wt, val, n))

end_time = perf_counter()
print(f'It took {end_time- start_time} ms to complete.')
