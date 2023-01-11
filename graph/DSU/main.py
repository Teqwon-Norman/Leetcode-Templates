"""
Disjoint Set Union Class
"""

class DSU:
    def __init__(self):
        self.parents = {}
        self.size = {}

    def find(self, v: int) -> int:
        if v not in self.parents:
            self.parents[v] = v
            self.size[v] = 1
        
        while self.parents[v] != v:
            self.parents[v] = self.parents[ self.parents[v] ]
            v = self.parents[v]
        return v

    def union(self, a: int, b: int) -> None:
        a = self.find(a)
        b = self.find(b)

        if a != b and self.size[a] < self.size[b]:
            a, b = b, a
        
        self.parents[b] = a
        self.size[a] += self.size[b]
