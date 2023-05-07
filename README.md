# Algorithims
1. [Union Find](#union-find)

# Union Find {#union-find}
## Problem Statement
given set of connected points/object, we have to decide whether two points are connected or not.

Note:
> A set of connected object or points is called as a component.mark

Applications of this Algo:
- friends in social network
- computers in network
- minimum spanning tree algo also uses this
- Percolation


There will be two main methods to be implemented.
1. find query: checks if two objects are in the same component or not.
2. union command - merge two components in to one.

```
    Initial -> {0} {1 4 5} {2 3 6 7}
    union(2,5)
    after union -> {0} {1 2 3 4 5 6 7}
```

Algos to solve:
1. Quick Find
2. quick Union
3. weighted Quick Union

## Quick Find
we will denote all n objects as index of array size of n.
the value of each index, contains its connected object.

- to find_connected(p, q) = check if p and q have same value.
- Union = to merge components containing p and q, change all entires whose value equals to arr[p] to arr[q]

```
    id  = [0, 1, 1, 8, 8, 0, 0, 1, 8, 8]
    union(6,1)
    id = [1, 1, 1, 8, 8, 1, 1, 1, 8, 8]
```
- initialize - N
- Union - N
- Find -  1 constant time

### Defect in Quickfind
- Union id too expensive
- Takes N^2^ array access to process sequence of N union commands on N object.

## Quick Union
- instead of storing the connected objects as array, we will treat them as tree.
- so in this implementation id[i] is parent of i
- Root of is `id[id[....id[i].....]]`

- Find : check if p and q have same root
- union: To merge components containing p and q, set the id of the p's root to the id if the q's root

### defects
- trees can get too tall
- find operation can be too expensive

## weighted Quick Union
- Keep track of the size of the tree.
- put small tree below large table
- balance by linking root of smaller tree to root of large tree
- depth of any node in the tree is atmost ill be `lg N`

## weighted Quick Union with path compression
- make the node to point the root, which will faltten the tree.
