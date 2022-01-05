import random
import threading

mylist = [random.randint(1, 100000000) for i in range(1000000)]
mins = []
n = 4
workers = []

def calc_min(li):
    minimun = li[0]
    for x in li:
        if x < minimun:
            minimun = x
    mins.append(minimun)

chunk_list = [mylist[(i*len(mylist))//n:((i+1)*len(mylist))//n] for i in range(n)]

for chunk in chunk_list:
    workers.append(threading.Thread(target=calc_min(chunk)))

for worker in workers:
    worker.start()
for worker in workers:
    worker.join()

print(f'Global minimun: {min(mins)}')
