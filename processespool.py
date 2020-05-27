# multiprocessing will utilised all COREs #
from multiprocessing import Pool

def f(x):
    while True:
        x = x+1
  
if __name__ =='__main__':
    p = Pool(processes=10)
    p.map(f, range(10))
    p.close()

