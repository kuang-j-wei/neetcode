class Codec:
    def serialize(self, root) -> str:
        """
        To turn this into a string, we could use a ',' as the delimiter.

        And we will use DFS to traverse the tree, so that in deserialize
        we can trace children back to their parents.

        Time Complexity: O(n)
            Every node is visited once
        Space Complexity: O(n)
            The stack holding all the children nodes can grow up to O(n)
            in an unbalanced tree. The `res` string itself can also grow
            to O(n) space
        """
        stack = [root]
        res = ""

        while stack:
            curr = stack.pop()

            if curr:
                res += f"{curr.val},"
                stack.append(curr.right)
                stack.append(curr.left)
            else:
                res += "None,"
        return res


    def deserialize(self, data):
        """
        There needs to be a recursive function, where whenever we
        encounter a None value, we know that we've reached the leaf node
        and thus can return back to the parent to trace another
        direction. And we continuously iterate through a list of int
        values and None that are supplied by the `data` string,
        separated by delimiter ','

        Time Complexity: O(n)
            Splitting by "," also takes O(n) as we are iterating through
            the entire string which covers the length of the tree. Then
            the recursive dfs also is iterating through every node once,
            which is another O(n) operation
        Space Complexity: O(n)
            The list `vals` can take up O(n) and then the recursive
            stack by `dfs` would take up to O(h) which in its worst case
            would be O(n) though best case is O(log(n)), but that's
            still dominated by the O(n) taken up by the list `vals`
        """
        def dfs():
            """
            This `dfs` function sets the tree structure recursively. Its
            base case is if the node retrieved is None, then return None
            as we don't have subsequent children that we need to set.

            Otherwise, for this newly retrieved node, we recursively set
            its left subtree and right subtree, by calling the dfs
            function itself, which would then recursively builds up
            the subtree until the end node None is reached, then
            returning the entire subtree structure upwards through the
            recursive stack.
            """

            curr = get_node()
            if curr is None:
                return None
            else:
                curr.left = dfs()
                curr.right = dfs()
            return curr

        def get_node():
            """
            The job of this function is to iterate through the list
            `vals` and construct valid TreeNodes, and increment the
            index counter every time. So whenever this function gets
            called, the next TreeNode with its value set according to
            `vals` gets returned
            """
            nonlocal child_node_idx
            val = vals[child_node_idx]
            child_node_val = vals[child_node_idx]
            child_node = TreeNode(int(child_node_val)) if child_node_val != 'None' else None
            child_node_idx += 1
            return child_node

        vals = data.split(",")[:-1]
        root = TreeNode(int(vals[0])) if vals[0] != 'None' else None

        if not vals or vals[0] == '':
            return None
        elif len(vals) == 1:
            return root
        else:
            child_node_idx = 0
            return dfs()


# Your Codec object will be instantiated and called as such:
# ser = Codec()
# deser = Codec()
# ans = deser.deserialize(ser.serialize(root))

