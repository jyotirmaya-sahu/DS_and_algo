class QuickUnion:
    def __init__(self, n):
        self.id = [i for i in range(0, n)]
    
    def root(self, p):
        currNode = p
        while (self.id[currNode] != currNode):
            currNode = self.id[currNode]
        
        return currNode
    def find(self, p, q):
        return "Yes" if self.root(p) == self.root(q) else "NO"

    def union(self, p, q):
        rootOfP = self.root(p)
        rootOfQ = self.root(q)
        self.id[rootOfP] = rootOfQ

qu = QuickUnion(8)
qu.union(2, 5)
qu.union(2, 3)
print(qu.id)
print(qu.find(3, 5))
