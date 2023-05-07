class QuickFind:
    def __init__(self, items):
        self.ids = [i for i in range(0, items)]
    
    def connected(self, p, q):
        return self.ids[p] == self.ids[q]

    def union(self, p, q):
        if (p >= len(self.ids) or q >= len(self.ids)):
            return
        
        if (self.ids[p] == self.ids[q]):
            return
        
        p_id = self.ids[p]
        for i in range(0, len(self.ids)):
            if (p_id == self.ids[i]):
                self.ids[i] = self.ids[q]


qf  = QuickFind(8)
qf.union(1,3)
qf.union(5,3)
qf.union(2,7)
print(qf.ids)
qf.union(3, 7)
print(qf.ids)