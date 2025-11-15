stock_prices = {"march 6":310.0,
                "march 7":320.0,
                "march 8":410.0,
                "march 9":500.0,
                "march 11":610.0,}




class HashTable:
    def __init__(self):
        self.MAX = 100
        self.arr = [None for i in range(self.MAX)]
    def get_hash(self,key):
        h = 0
        for char in key:
            h += ord(char)
        return h % 100
    def add(self,key,val):
        h=self.get_hash(key)
        self.arr[h] =val
    def get(self, key):
        h=self.get_hash(key)
        return self.arr[h]
t = HashTable()
print(t.get_hash('march 6'))
t.add('march 6',130)
print(t.get('march 6'))
#or
class HashTable:
    def __init__(self):
        self.MAX = 100
        self.arr = [None for i in range(self.MAX)]
    def get_hash(self,key):
        h = 0
        for char in key:
            h += ord(char)
        return h % 100
    def __setitem__(self,key,val):
        h=self.get_hash(key)
        self.arr[h] =val
    def __getitem__(self, key):
        h=self.get_hash(key)
        return self.arr[h]
t = HashTable()
print(t.get_hash('march 10'))
t['march 10']=140
print(t['march 10'])