import math

from matplotlib.pyplot import xcorr
from cache import Cache, time_sample
import heapq
from make_graph import make_graph

m = 1024
n = 65536

x = [r * 0.5 for r in range(13)]
vars = ["FIFO", "LRU"]

fifo_mus = []
lru_mus = []

# model both FIFO and LRU
for trials in range(10):
    for mode in vars:
        print(" ")
        print(f"{mode} TESTS")
        y = []
        for k in range(1):
            # time limit in range [10^1, 10^6]
            t_limit = 10 ** 6

            cache = Cache(m, is_fifo=(mode=="FIFO"))
            timeline = []

            # Sample distribution for each element and add them to timeline
            for i in range(n):

                # insert into priority queue maintaining time order
                heapq.heappush(timeline, (time_sample(1 / float(i+1)), i))

            # hit/miss metrics
            hits = 0.0
            trials = 0.0
            
            while True:
                # effectively jump to time t, which is the event at the front of the priority queue
                (t, i) = heapq.heappop(timeline)

                if (t > t_limit):
                    break

                hits += cache.getResource(i)
                trials += 1

                heapq.heappush(timeline, (time_sample(1 / float(i+1)) + t, i))

            # getting points to plot
            y.append(100 * hits / trials)
            if mode == "FIFO":
                fifo_mus.append(100 * hits / trials)
            else:
                lru_mus.append(100 * hits / trials)

            if(k == 0): 
                print(f"Cache hits: {hits}.")
                print(f"Total trials: {trials}.")
                print(f"Cache hit ratio: {100* hits / trials}%")
                print("------------")

        #make_graph(x, y, f"{mode} Cache")

print(fifo_mus)
print(lru_mus)

