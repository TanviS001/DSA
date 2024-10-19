stack = []
elt=int(input())

for i in range(elt):
  num=int(input())
  stack.append(num)
print(stack)

stack.pop()
print(stack)
