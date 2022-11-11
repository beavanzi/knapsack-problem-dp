from time import sleep, perf_counter
from threading import Thread

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
K = [[0 for x in range(W + 1)] for x in range(n + 1)]
isReady = [[False for x in range(W + 1)] for x in range(n + 1)]
 
def getK():
    return K

def getIsReady():
    return isReady

def setK(i,j,value):
    K[i][j] =value
    isReady[i][j] =True
    return

def loopKnap(W, wt, val, init,n):
    for i in range(init,n + 1):
        for w in range(W + 1):
            if i == 0 or w == 0:
                setK(i,w,0)
                K[i][w] = 0  
            elif wt[i-1] <= w:
                isReady = getIsReady()
                while(not(isReady[i-1][w-wt[i-1]] and isReady[i-1][w])):
                    isReady = getIsReady()
                    pass
                setK(i,w,max(val[i-1]
                          + K[i-1][w-wt[i-1]], 
                              K[i-1][w]))
            else:
                isReady = getIsReady()
                while(not(isReady[i-1][w])):
                    isReady = getIsReady()
                    pass
                setK(i,w,getK()[i-1][w])
    return

def knapSack(W, wt, val, n):
    t1 = Thread(target=loopKnap,args=(W, wt, val,0, n//2))
    t2 = Thread(target=loopKnap,args=(W, wt, val,n//2, n))
    # start the threads
    t1.start()
    t2.start()
    # wait for the threads to complete
    t1.join()
    t2.join()
    return K[n][W]
 
 
start_time = perf_counter()


print(knapSack(W, wt, val, n))

end_time = perf_counter()
print(f'It took {end_time- start_time} ms to complete.')
