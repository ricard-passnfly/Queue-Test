import random, time
from heapq import heappush, heappop

def timefunc(method):
    def timed(*args, **kw):
        ts = time.time()
        result = method(*args, **kw)
        te = time.time()

        if 'log_time' in kw:
            name = kw.get('log_name', method.__name__.upper())
            kw['log_time'][name] = int((te - ts) * 1000)
        else:
            print ('%r  %2.2f ms' % \
                  (method.__name__, (te - ts) * 1000))
        return result

    return timed

class Task():
    def __init__(self, sort_key=255, data=""):
        self.sort_key = sort_key
        self.data = data
    def __lt__(self, other):
        return self.sort_key < other.sort_key

    def __str__(self):
        return "Task> sort_key: {}, data: {}".format(self.sort_key, self.data)


if __name__ == '__main__':
    heap = []

    @timefunc
    def createheap():
        for i in range(15):
            heappush(heap, Task(random.randint(0, 255), i))


    @timefunc
    def func():
        for i in range(1):
            print(heappop(heap))

    createheap()
    # func()

    print(heap)

    pass


