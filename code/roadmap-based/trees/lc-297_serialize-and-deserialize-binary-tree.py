# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Codec:
    def serialize(self, root) -> str:
        """
        To turn this into a string, we could use a ',' as the delimiter.

        And we will use DFS to traverse the tree, so that in deserialize
        we can trace children back to their parents.

        :type root: TreeNode
        :rtype: str
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


        :type data: str
        :rtype: TreeNode
        """
        def dfs(curr):
            """
            The job of this function is to iterate through all the
            values. And if the current value is None, return None.
            Otherwise, continue to recursively build up the left and
            right subtrees
            """
            nonlocal child_node_idx

            child_node = get_node(child_node_idx)
            if child_node is None:
                return None
            else:
                child_node_idx += 1
                child_node = get_node(child_node_idx)
                curr.left = dfs(child_node)

                child_node_idx += 1
                child_node = get_node(child_node_idx)
                curr.right = dfs(child_node)
            return curr

        def get_node(child_node_idx):
            val = vals[child_node_idx]
            child_node_val = vals[child_node_idx]
            child_node = TreeNode(int(child_node_val)) if child_node_val != 'None' else None
            return child_node

        vals = data.split(",")[:-1]
        root = TreeNode(int(vals[0])) if vals[0] != 'None' else None

        if len(vals) == 1:
            return root
        else:
            child_node_idx = 1
            return dfs(root)


# Your Codec object will be instantiated and called as such:
# ser = Codec()
# deser = Codec()
# ans = deser.deserialize(ser.serialize(root))

