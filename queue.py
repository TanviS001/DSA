# Initialization of queue
queue = []
elt=int(input())

# Adding data elements in the queue
for i in range(elt):
  num=int(input())
  queue.append(num)
print(queue)

# Removing data elements from the queue
queue.pop(0)
print(queue)
