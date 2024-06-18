# Arrays
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
Last in first out.

* Push (O(1))
* Pop (O(1))
* Peek/Top (O(1))

Since the out order is reverse of the in order, it can be used to **reverse sequences**, such a s a string.

## Linked Lists
* A `ListNode` will need to have `value` and `next` (a pointer)
* We point `next` to another `ListNode`
* Unlike arrays where they values are stored in the same order in memory, a linked list doesn't need to be saved in the same order in memory
* Normally we will keep a pointer to always point at the Head and the Tail of a linked list
* Adding to beginning or end is O(1)
* If you have a reference to a node in the middle it will be O(1)
* But if we need to "search" for an element it will be O(n)
* To access a random element without a specific pointer to it, it will also be O(n)
