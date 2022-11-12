from time import sleep, perf_counter
from threading import Thread

 
wt = [23,31,29,44,53,38,63,85,89,82]

val = [92,57,49,68,60,43,67,84,87,72]

W = 165

n = len(val)

K = [[0 for x in range(W + 1)] for x in range(n + 1)]
canGet = True
 
def getK():
    while(not canGet):
        pass
    return K


def setK(i,j,value):
    canGet = False
    K[i][j] =value
    canGet = True
    return

def loopKnap(W, wt, val, init,i):
    for w in range(init,W + 1):
        if i == 0 or w == 0:
            setK(i,w,0)
        elif wt[i-1] <= w:
            setK(i,w,max(val[i-1]
                        + getK()[i-1][w-wt[i-1]], 
                            getK()[i-1][w]))
        else:
            setK(i,w,getK()[i-1][w])
    return

def knapSack(W, wt, val, n):
    
    start_time = perf_counter()

    for i in range(n + 1):       
        t1 = Thread(target=loopKnap,args=(W//2, wt, val,0, i))
        t2 = Thread(target=loopKnap,args=(W, wt, val,W//2, i))
        t1.start()
        t2.start()
        t1.join()
        t2.join()
    end_time = perf_counter()
    print(f'Tempo para completar {end_time- start_time} ms.')
    
    return K[n][W]
 
 


print(knapSack(W, wt, val, n))


