class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

def main():
    new1 = Node(10)
    new2 = Node(20)

    new1.next = new2
    print(f"Node 1 data: {new1.data}")
    print(f"Node 2 data: {new2.data}")

if __name__ == "__main__":
    main()
