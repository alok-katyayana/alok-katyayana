class HashTable:
    def __init__(self, size = 99989):
        self.data_map = [None] * size

    def __hash(self, key):
        my_hash = 0
        for letter in str(key):
            my_hash = (my_hash + ord(letter) * 97) 

        return my_hash % len(self.data_map)

    def print_table(self):
        for i, val in enumerate(self.data_map):
            if val is not None:
                print(i, ": ", val)

    def set_item(self, key, value):
        index = self.__hash(key)

        if self.data_map[index] is None:
            self.data_map[index] = []
            self.data_map[index].append([key, value])
            return True
        for i in range(len(self.data_map[index])):
            if (self.data_map[index][i][0] == key):
                self.data_map[index][i][1] = value
                return True


        self.data_map[index].append([key, value])
        return True

    def get_keys(self):
        inel = []
        vals = [v for v in self.data_map if v is not None]
        for elm in vals:
            inel.extend(elm)
        print(inel)
        keys = [elm[0] for elm in inel]

        return keys

    def get_item(self, key):
        index = self.__hash(key)
        
        if self.data_map[index] is None:
            return None
        ans_ = map(lambda x : (x[0], x[1]) if x[0] == key else None,
                self.data_map[index])
       
        ans = [val for val in ans_ if val is not None]
         
        return list(ans)[0]




if __name__ == "__main__":
    vals = ["Hello", "World", 1, 56, "bhai", "klk"]
     
    ht = HashTable(3);
    ht.print_table();

    ht.set_item("masala", 101)
    ht.set_item("pan", 34)
    ht.set_item("Chuna", 34)
    ht.set_item("Cigrate", 34)
    ht.set_item("Lighter", 34)

    ht.print_table()
    ht.set_item("Lighter", 100)
    ht.print_table()

    print(ht.get_item("pan"))

    print(ht.get_keys())
