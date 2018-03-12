from queue import PriorityQueue


class Task():
    def __init__(self, sort_key=255, data=""):
        self.sort_key = sort_key
        self.data = data
    def __lt__(self, other):
        return self.sort_key < other.sort_key

    def __str__(self):
        return "Task> sort_key: {}, data: {}".format(self.sort_key, self.data)

if __name__ == '__main__':
    queue = PriorityQueue()
    queue.put(Task(i, "") for i in range(10))

    print("Success")
