class Queue:
    def __init__(self):
        self.queue = []

    def push(self, item):
        self.queue.append(item)

    def pop(self):
        if not self.queue:
            return None
        return self.queue.pop(0)

    def peek(self):
        if not self.queue:
            return None
        return self.queue[0]

    def is_empty(self):
        return len(self.queue) == 0

    def size(self):
        return len(self.queue)


queue = Queue()
queue.push(10)
queue.push(20)
queue.push(30)

print(queue.peek())
print(queue.pop())
print(queue.pop())
print(queue.pop())
print(queue.pop())
