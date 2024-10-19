queue = []
elt=int(input())

for i in range(elt):
  num=int(input())
  queue.append(num)
print(queue)

queue.pop(0)
print(queue)
