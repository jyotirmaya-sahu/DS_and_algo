class QuickUnion:
    def __init__(self, n):
        self.id = [i for i in range(0, n)]
        self.sz = [1 for i in range(0, n)]
    
    def root(self, p):
        currNode = p
        while (self.id[currNode] != currNode):
            currNode = self.id[currNode]
        
        return currNode
    def find(self, p, q):

        return "Yes" if self.root(p) == self.root(q) else "NO"

    def height(self, p):
        currNode = p
        height = 0;
        while (self.id[currNode] != currNode):
            currNode = self.id[p]
            height += 1
        return height

    def union(self, p, q):
        rootOfP = self.root(p)
        rootOfQ = self.root(q)
        print(self.sz[rootOfP])
        print(self.sz[rootOfQ])
        if (self.sz[rootOfP] <= self.sz[rootOfQ]):
            self.id[rootOfP] = rootOfQ
            self.sz[rootOfQ] += self.sz[rootOfP]
        else:
            self.id[rootOfQ] = rootOfP
            self.sz[rootOfP] += self.sz[rootOfQ]


qu = QuickUnion(8)
print(qu.sz)
qu.union(2, 5)
print(qu.id)
print(qu.sz)
qu.union(4, 3)
print(qu.id)
print(qu.sz)
print(qu.find(2, 3))
qu.union(2, 3)
print(qu.id)
print(qu.sz)
print(qu.root(2))
print(qu.root(3))
