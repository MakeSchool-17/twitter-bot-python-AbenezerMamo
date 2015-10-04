import node

class HashTable:
    def __init__(self):
        self.hashtable = []
        while len(self.hashtable) < 10:
            self.hashtable.append(LinkedList())
        self.size = 0

    def set(self, key, data):
        index_key = hash(key) % len(self.hashtable) # Bucket index
        self.hashtable[index_key].insert([key, data])
        self.size += 1


    def get(self, key):
        index_key = hash(key) % len(self.hashtable)
        return self.hashtable[index_key].return_data(key)

    def update(self, key, data):
        index_key = hash(key) % len(self.hashtable)
        self.hashtable[index_key].find(key).data[1] = data


    def get_keys(self):
        pass

    def get_values(self):
        pass
