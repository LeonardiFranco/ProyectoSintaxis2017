class Env():
    def __init__(self, n):
        self.table = {}
        self.prev = n

    def put(self, w, i):
        self.table[w]=i

    def get(self, w):
        e = self
        while e:
            found = e.table.get(w)
            if found:
                return found
            e = e.prev
        return None