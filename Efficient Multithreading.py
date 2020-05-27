import time
import threading

def f1(x):
    print ('x: ',x)
    time.sleep(10)
    
    
def f2(x):
    print ('x_square: ',x*x)
    time.sleep(2)

if __name__=="__main__":
    t = time.time()
    for i in range(5):
        t1= threading.Thread(target=f1, args=(i,))
        t2= threading.Thread(target=f2, args=(i,))

        t1.start()
        t2.start()

    print("done in : ",time.time()-t)
