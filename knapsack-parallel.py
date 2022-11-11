
from time import sleep, perf_counter
from threading import Thread

def loopKnap(W, wt, val, init,n,K,isReady):
    for i in range(init,n + 1):
        for w in range(W + 1):
            if i == 0 or w == 0:
                K[i][w] = 0
                isReady[i][w]=True
            elif wt[i-1] <= w:
                while(not(isReady[i-1][w-wt[i-1]] and isReady[i-1][w])):
                    pass
                K[i][w] = max(val[i-1]
                          + K[i-1][w-wt[i-1]], 
                              K[i-1][w])
                isReady[i][w]=True
            else:
                while(not(isReady[i-1][w])):
                    pass
                K[i][w] = K[i-1][w]
                isReady[i][w]=True
    return

def knapSack(W, wt, val, n):
    K = [[0 for x in range(W + 1)] for x in range(n + 1)]
    isReady = [[False for x in range(W + 1)] for x in range(n + 1)]
 
    t1 = Thread(target=loopKnap,args=(W, wt, val,0, n//2,K,isReady))
    t2 = Thread(target=loopKnap,args=(W, wt, val,(n//2)+1, n,K,isReady))
    start_time = perf_counter()


        # start the threads
    t1.start()
    t2.start()

    # wait for the threads to complete
    t1.join()
    t2.join()
    end_time = perf_counter()
    print(f'It took {end_time-start_time} ms to complete.')

    
    return K[n][W]
 
 
val = [60, 100, 120]
wt = [10, 20, 30]
W = 50
n = len(val)
# Driver code
start_time = perf_counter()

print(knapSack(W, wt, val, n))

end_time = perf_counter()
print(f'It took {end_time-start_time} ms to complete.')
