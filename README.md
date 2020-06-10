# Multithreading vs MultiProcessing
Multithreading and multiprocessing are used to optimised and parallelised workflow to speed up performance.

### Rule of thumb
I/O bound job → multithreading.<br>
`from multiprocessing.dummy import Pool as Threadpool`<br>
CPU bound job → multiprocessing.<br>
`from multiprocessing import pool`

### Multiprocessing
Multiprocessing runs the processes in separated memory space. Therefore memory is allocated to each process when spawn. 
This is the overhead of multiprocess, and it takes longer to spawn as compare to multithread. 
Modern computer these days should have plenty of RAM to overcome this issue. 
The below code is to run `f(x)` 10 times, simultaneously. 
Keep in mind that each process is running independently from each other because we have cloned `f(x)` to each memory space.

```
from multiprocessing import Pool
def f(x):
    while True:
        x = x+1
  
if __name__ =='__main__':
    p = Pool(processes=10)
    p.map(f, range(10))
    p.close()
```

You can create as many `processes` as you like to utilise all CPUs fully.

### Multithreading
Multithreading runs parallel tasks on shared memory space. 
The advantage of shared memory space is to reduce overhead. 
This means both threads can read from the same object without creating a duplicate copy.
However, precautions have to be taken when writing an object back into memory. 
Below code is to run `f1(x)` and `f2(x)` in parallel. Both functions read from the same object `arr`.

```
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
```
<p align="center">
  <img />
![]((/resource/multithreading_withwait.png)
</p>

We can see that `x` and `x_square` spawned next to each other at `t=0`. 
Then `x_square` has gone ahead to do the calculation without waiting for `x`. 
Of course, there is a better way of doing multithreading, if pending for `t1` to complete is not necessary.
We simply removed the `t1.join()` and `t2.join()` and wrote the loop in the main area.

```
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
```
<p align="center">
  <img />
  ![](/resource/multithreading_withoutwait.png)
</p>


The limitation of multithreading is subject to the global interpreter lock (GIL). 
You can create as many tasks as you like in multithreading, but it will only max out 1 CPU. 
Below code is duplicating the example from multiprocessing. 
We used `Threadpool` instead of `pool` this time.
Keep in mind that this is a wrong coding practice because we are overwriting `x` in the shared memory space.
This is to illustrate your CPU usage is maxing out at 8%(in my case).

```
from multiprocessing.dummy import Pool as Threadpool
def f(x):
    while True:
        x = x+1
    
if __name__=="__main__":
    p = Threadpool(10)
    p.map(f,range(10))
    p.close()
```
### Conclusion
Multithreading is used for input and output (I/O) bound process. 
For example, we are waiting for user input, downloading data from the internet, etc.
We try to saturate the CPU by giving it more task to handle.

Multiprocessing is used for CPU bound process. For example, calculate PI eight times. 
Each CPU is acting as an independent worker who can perform the calculation separately.


<h6 align="center">
&copy; Quantuary 2020
</h6>
