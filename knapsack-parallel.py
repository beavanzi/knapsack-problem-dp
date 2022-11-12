
from time import sleep, perf_counter
from threading import Thread

def loopKnap(W, wt, val, init,i,K):
    for w in range(init,W + 1):
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
    
    
    start_time = perf_counter()

    for i in range(n + 1):
       
        t1 = Thread(target=loopKnap,args=(W//2, wt, val,0, i,K))
        t2 = Thread(target=loopKnap,args=(W, wt, val,W//2, i,K))
        
        # start the threads
        t1.start()
        t2.start()

        # wait for the threads to complete
        t1.join()
        t2.join()
    end_time = perf_counter()
    print(f'Tempo para completar {end_time- start_time} ms.')

    
    return K[n][W]
 
 
wt = [382745,
799601,
909247,
729069,
467902,
 44328,
 34610,
698150,
823460,
903959,
853665,
551830,
610856,
670702,
488960,
951111,
323046,
446298,
931161,
 31385,
496951,
264724,
224916,
169684,]

val = [825594,
1677009,
1676628,
1523970,
 943972,
  97426,
  69666,
1296457,
1679693,
1902996,
1844992,
1049289,
1252836,
1319836,
 953277,
2067538,
 675367,
 853655,
1826027,
  65731,
 901489,
 577243,
 466257,
 369261,]
W = 6404180
n = len(val)
# Driver code
start_time = perf_counter()

print(knapSack(W, wt, val, n))

end_time = perf_counter()
print(f'It took {end_time-start_time} ms to complete.')
