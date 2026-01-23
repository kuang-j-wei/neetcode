from collections import deque


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
        We can for example, use BFS to describe the tree
        :type root: TreeNode
        :rtype: str
        """
        queue = deque([root])
        res = ""

        while queue:
            for _ in range(len(queue)):
                curr = queue.popleft()
                
                res += f"{curr.val}," if curr else f"None,"
                
                if curr is not None:
                    queue.append(curr.left)
                    queue.append(curr.right)   
        return res 


    def deserialize(self, data):
        """
        :type data: str
        :rtype: TreeNode
        """
        nodes = data.split(",")[:-1]
        root = TreeNode(int(nodes[0])) if nodes[0] != 'None' else None
        curr = root


        for i in range(1, len(nodes), 2):
            node_left = TreeNode(int(nodes[i])) if nodes[i] != 'None' else None 
            node_right = TreeNode(int(nodes[i + 1])) if nodes[i + 1] != 'None' else None 

            curr.left = node_left
            curr.right = node_right 

            curr = node_left if node_left is not None else node_right
        return root


# Your Codec object will be instantiated and called as such:
# ser = Codec()
# deser = Codec()
# ans = deser.deserialize(ser.serialize(root))

