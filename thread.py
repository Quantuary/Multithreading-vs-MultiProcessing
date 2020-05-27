# Threading only utilised 1 CORE #
# Create more threads will not help when a single CORE max out #

import time
import threading

def f1(x):
    for n in x:
        print ('x: ',n)
        time.sleep(10)
    
    
def f2(x):
    for n in x:
        print ('x_square: ',n*n)
        time.sleep(2)

if __name__=="__main__":
    arr = range(5)
    t = time.time()
    
    t1= threading.Thread(target=f1, args=(arr,))
    t2= threading.Thread(target=f2, args=(arr,))

    t1.start()
    t2.start()

    t1.join() #ensure task is completed before moving to next step
    t2.join()

    print("done in : ",time.time()-t)
