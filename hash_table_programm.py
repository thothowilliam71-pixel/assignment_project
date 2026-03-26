class HashTable:
    def __init__(self, size=10):
        self.size = size
        self.table = [[] for _ in range(size)]
    def hash_function(self, key):
        return key % self.size
    def insert(self, reg_no, name):
        index = self.hash_function(reg_no)
        self.table[index].append((reg_no, name))
    def display(self):
        for i, bucket in enumerate(self.table):
            print(f"Index {i}: {bucket}")
ht = HashTable()
ht.insert(101, "John")
ht.insert(111, "Mary")
ht.insert(121, "Alex")
ht.display()