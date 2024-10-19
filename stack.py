# Initialization of stack
stack = []
elt=int(input())

# Adding data elements in the stack
for i in range(elt):
  num=int(input())
  stack.append(num)
print(stack)

# Removing data elements from the stack
stack.pop()
print(stack)
