class OpenHashing:
    def __init__(self, size):
        self.size = size
        self.hash_table = [[] for _ in range(size)]

    def hash_function(self, key):
        return key % self.size

    def insert(self, key, value):
        index = self.hash_function(key)
        self.hash_table[index].append((key, value))

    def search(self, key):
        index = self.hash_function(key)
        for k, v in self.hash_table[index]:
            if k == key:
                return v
        return None

# Contoh penggunaan:
open_hash_table = OpenHashing(10)
open_hash_table.insert(5, 'Lima')
open_hash_table.insert(15, 'Lima Belas')
open_hash_table.insert(25, 'Dua Puluh Lima')

print("Open Hashing:")
print(open_hash_table.search(5))  # Output: Lima
print(open_hash_table.search(15))  # Output: Lima Belas
print(open_hash_table.search(25))  # Output: Dua Puluh Lima

class ClosedHashing:
    def __init__(self, size):
        self.size = size
        self.hash_table = [None] * size

    def hash_function(self, key):
        return key % self.size

    def insert(self, key, value):
        index = self.hash_function(key)
        while self.hash_table[index] is not None:
            index = (index + 1) % self.size
        self.hash_table[index] = (key, value)

    def search(self, key):
        index = self.hash_function(key)
        initial_index = index
        while self.hash_table[index] is not None:
            k, v = self.hash_table[index]
            if k == key:
                return v
            index = (index + 1) % self.size
            if index == initial_index:
                break
        return None

# Contoh penggunaan:
closed_hash_table = ClosedHashing(10)
closed_hash_table.insert(5, 'Lima')
closed_hash_table.insert(15, 'Lima Belas')
closed_hash_table.insert(25, 'Dua Puluh Lima')

print("\nClosed Hashing:")
print(closed_hash_table.search(5))  # Output: Lima
print(closed_hash_table.search(15))  # Output: Lima Belas
print(closed_hash_table.search(25))  # Output: Dua Puluh Lima
