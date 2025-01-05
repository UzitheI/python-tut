#double ended queue


from collections import deque


queue=deque()


queue.append(3)

queue.append(5)
print(queue)


#popped from the left at constant time

queue.popleft()

print(queue)


#or we can add value to the left

queue.appendleft(5)


print(queue)

#to pop from the right side

queue.pop()

print(queue)

