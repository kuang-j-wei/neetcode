# Arrays
## Static Arrays
* A contiguous set of values
* `1 byte = 8 bits`
* Integer takes 32 bits of space, 4 bytes
* Characters take 8 bits of space, 1 byte

## Dynamic Arrays
Static arrays have to have a pre-defined size

* Pushing is an O(1) operation (adding a value)
* Popping is a O(1) operation (take a value from the end)
* When we run out of space, we need to copy original value to a new array, that's usually twice the size (memory space), which is O(n)
  * This is a middle ground between not having wasted space, and not always having to O(n)
* Because of the copying and doubling action, we know that for any array of size n, we will at most take 2n operations to create; thus O(2n) ~ O(n)
  * Because 1 -> 2 -> 4 -> 8; but the action before 8 is 1 + 2 + 4 = 7, which is smaller than 7
  * So at most it's n+n (8+8)
  * Thus at most we will take 2n operations
* Amortized time complexity is O(1) because it's pretty infrequent that we need to add more space
* Inserting or removing in the middle is still O(n)


## Stacks
Last in first out (LIFO).

* Push (O(1))
* Pop (O(1))
* Peek/Top (O(1))

Since the out order is reverse of the in order, it can be used to **reverse sequences**, such a s a string.

# Linked Lists
## Singly Linked Lists
* A `ListNode` will need to have `value` and `next` (a pointer)
* We point `next` to another `ListNode`
* Unlike arrays where they values are stored in the same order in memory, a linked list doesn't need to be saved in the same order in memory
* Normally we will keep a pointer to always point at the Head and the Tail of a linked list
* Adding to beginning or end is O(1)
* If you have a reference to a node in the middle it will be O(1)
* But if we need to "search" for an element it will be O(n)
* To access a random element without a specific pointer to it, it will also be O(n)
* To remove a node at the end, it will be O(n) because we need to traverse from `head` to know who precedes `tail`
* (for array it is always O(n) because we have to copy over the remainder)

### Linked List Traversal
```
cur = ListNode1
while cur:
    cur = cur.next
```
This take O(n)

We usually will keep a `head` and a `tail` pointer.


## Doubly Linked Lists
We have double pointers. `next` and `prev`

### Appending a new node
To append a new node
```
tail.next = NewNode
NewNode.prev = tail
tail = tail.next
```

### Deleting from the tail
Compared to a singly linked list, removing the last node can be done at O(1), because we don't have to traverse from `head` to the end to know who precedes `tail`

```
node2 = tail.prev
node2.next = null
tail = node2
```

* So deleting a node at the end is O(1), which means that both append and remove from the end is O(1), so we satisfy a `stack` requirement
* But unlike a stack, we can't access a random element at O(1), instead we still need to traverse at O(n); so we don't implement `stack`'s using doubly linked lists

### Array vs Linked List
||Arrays|LinkedLists
|---|---|---|
|Access i-th element|O(1)|O(n)|
|Insert Remove end|O(1)|O(1)|
|Insert/Remove middle|O(n)|O(1)*|

*for us to remove in the middle, we have to arrive at that point, which still would take O(n) anyway

So overall, **arrays are still better for most cases because the advantage in insert/remove is handicapped by the O(n) of i-th element access anyway**


## Queues
* Differ from a stack in that it's FIFO
The main requirement is enqueue and dequeue both need to be O(1)

This can be achieved with linked lists.

Could be done with arrays too, but you would need to shift data as we enqueue and dequeue so that would take O(n)

# Recursion
Recursion calls itself until a base case is reached.
## Factorial (single branch)
* Recursive solution - think of factorial's definition, and the base case definition.
```
def factorial(n):
    if n == 1:
        return 1
    return n * factorial(n - 1)
```
* Complexity
  * O(n) in time
  * O(n) in space (each function call needs its memory to put the function on hold)

* Iterative solution
```
def factorial(n):
    res = 1
    for i in range(1, n+1, 1):
        res *= i
    return res
```
* Complexity
    * O(n) in time
    * O(1) in space
 
## Fibonacci Sequence (two branches)
```
def fibonacci(n):
    if n <= 1:
        return 1
    return fibonacci(n - 1) + fibonacci(n - 2)
```
Since from the top each node splits into 2, we need to do 2 * 2 * 2 * ... operations. And the depth is at most from n all the way down to 1/0, in decrement of 1. Therefore the depth is at most n, thus the time complexity is O($2^n$)
```
        [ 5 ]
         /    \
      [4]     [3]
      /\        /\
  [3] [2]     [2] [1]
  /\    /\     /\ 
[2][1] [1][0] [1][0]
/\
[1][0]
```
* Complexity
  * O($2^n$) in time
    * Because at each layer there are twice more calls
  * O(n) in space
    * Because it's determined by the deepest point of the recursion, and the maximum stack depth is just n
  

# Sorting
|Algorithms|Time Complexity|Space Complexity
|---|---|---|
|InsertionSort (stable) |$O(n^2)$|$O(1)$|
|MergeSort (stable) |$O(n\log{n})$|$O(n)$|
|QuickSort (unstable) |$O(n\log{n})$ to $O(n^2)$|$O(1)$|
|BucketSort (unstable) |$O(n)$|$O(1)$|

## Insertion Sort
* **How it works**:
  * Like a window function
  * First start from just itself - by definition it's already sorted
  * Then a window of two, is the last smaller than its previous one? Swap, and step to previous index
  * Continue...
  * We will always check until we either
    * Hit the first position 
    * Comparison has failed (i.e. the previous number indeed is smaller)
* **Time Complexity**
  * $O(n^2)$ in the worst case and $O(n)$ in the best case
  * Because the number of operations goes like 1 -> 2 -> 3 -> 4, to summing them all, it's equal to a half a square, so we are bounded by $\frac{n^2}{2}$, so we get $O(n^2)$
* **Space Complexity**
  * O(1) because no additional structure is used
* **Stability**: It is stable because if there is a tie, the original relative position will be preserved (because nothing gets moved when it's a tie)

## Merge Sort
* **How it works**:
  * Break by sub-problems by half, until we reach just two individual sub-problems each with a length 1
  * We then merge back up and individually compare the size by using two pointers iterating through each sub list
  * Since we are halving each time, the total "depth" will be $\log{n}$
  * At each layer, we will need to compare n numbers because each element will be iterated over once
* **Time Complexity**
  * $O(n\log{n})$
  * Because there is a depth of $log(n)$ as we recursively split the array in half,
  * and at each layer the merging act itself will take at worst $O(n)$ time as we iterate through the two left and right sub-arrays
* **Space Complexity**
  * $O(\log(n) + n) = O(n)$
  * Because log(n) memory stack, then we need to copy the sub-arrays at each merge step, which in total will take up n in space
* **Stability**: Stable

## Quick Sort
* **How it works**:
  * We pick a pivot value (naively, we just pick the last value)
  * Then we start two pointers at the first position in the sub-array that's left to it
  * One pointer will be noting, if we find a value that's less than the pivot value, this is the position that we are going to put the smaller value in
  * The other pointer is just iterating to the right until we hit the pivot value
  * Is this value less than the pivot value? If yes, we swap to the first pointer; we then advance both the first and second pointer
  * If this value is not less than the pivot value, we do nothing, and only advance the second pointer
  * Lastly, we then put the pivot value into the position of the first pointer
* **Time Complexity**
  * $O(n\log{n})$ on average because we would have a depth of $log(n)$ from the splits, and at each layer we need to at worst compare n values
* **Space Complexity**
  * $O(1)$ because all modifications are done in place
* **Stability**:
  * When there is a tie, the ordering isn't guaranteed


## Bucket Sort
* **How it works**:
  * Iterate over the array once, and count how many times each unique value appear
  * Then simply replace the original arrays based on how many times each unique value has appeared (do it in order, of course)
* **Time Complexity**
  * $O(n)$ (really it's $2n$) because we iterate once to count how many times values appear
  * Then another iteration to replace the values
* **Space Complexity**
  * $O(k)$ where $k$ is the number of unique values
* **Stability**
  * No
  * We just count how many times a value appear
  * We then replace the array based on how many times a value appear
  * The ordering is entirely irrelevant

# Binary Search
## Search Array
* Works if an array is already sorted
* We would calculate the mid point, and see if the target value is greater or smaller, we then search either the right or left
* This makes our search time only $O(\log{n})$ since the depth is $2^x = n$ so $x = log(n)$ is the depth
* It's also possible that the value is simply not in the array, in which case we would just have `L`, `R`, and `mid` all pointing at the same element
* When `L` finally becomes bigger than `R`, that's how we know the element doesn't exist (because even the last pointer itself isn't equal), and we can exit the loop

## Search Range
* When ask to search in a range, especially when given some arbitrary function to determine eligibility, this is typically a binary search problem
* By always going to the mid point we divide and conquer, and will be able to reach a worse case of $\log{n}$, instead of needing to traverse through all eligible numbers


# Trees
## Binary Tree
* Will always have leaf nodes, which are nodes with no children
* Can't have cycles
* Sharing the same parent means they are sibling nodes
* Height: the longest path to a descendant leaf node from this current node
* Depth is the longest path to the root
```
class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None
```
## Binary Search Trees (BST)
### Time complexity
* $O(\log{n})$ for search, insert and deletion
### Definition
* All nodes in the left subtree have to be less than their root node
  * (generally binary search trees do not have duplicates)
* This property has to hold for every single node/subtree
* Search Time Complexity: $O(\log{n})$ for a balanced tree (left and right height subtrees always have equal height or at most a diff of 1)
* But strictly it's $O(h)$ where $h$ is the height of the tree
* Main advantage over sorted arrays: *insertion and deletion is done in $O(\log{n})$ instead of $O(n)$*
  