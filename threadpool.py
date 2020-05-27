# Create more threads will not help when a single CORE max out #
from multiprocessing.dummy import Pool as Threadpool

def f(x):
    while True:
        x = x+1
    
if __name__=="__main__":

    p = Threadpool(10)
    p.map(f,range(10))
    p.close()
   
