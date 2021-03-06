In a binary tree, the root node is at depth 0, and children of each depth k node are at depth k+1.

Two nodes of a binary tree are cousins if they have the same depth, but have different parents.

We are given the root of a binary tree with unique values, and the values x and y of two different nodes in the tree.

Return true if and only if the nodes corresponding to the values x and y are cousins.

Example 1:


Input: root = [1,2,3,4], x = 4, y = 3
Output: false
Example 2:


Input: root = [1,2,3,null,4,null,5], x = 5, y = 4
Output: true
Example 3:



Input: root = [1,2,3,null,4], x = 2, y = 3
Output: false
 

Note:

The number of nodes in the tree will be between 2 and 100.
Each node has a unique integer value from 1 to 100.





# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

#TreeNode{val: 1, left: TreeNode{val: 2, left: TreeNode{val: 4, left: None, right: None}, right: None}, right:   # TreeNode{val: 3, left: None, right: None}}

class Solution:
    def isCousins(self, root: TreeNode, x: int, y: int) -> bool:
        
        depth=0
        parent=None
        m=[]   #for X info             
        n=[]   #for Y info
        ele=self.PreorderTraversal(root)
        print(ele)
        if root==None:
            return False
        self.dfs(root,x,y,depth,parent,m,n)
        return m[0][0]==n[0][0] and m[0][1]!=n[0][1]    #checking if the cousins have same depth and different parents
        
    def PreorderTraversal(self, r):
        res = []
        if r:
            res.append(r.val)
            res = res + self.PreorderTraversal(r.left)
            res = res + self.PreorderTraversal(r.right)
        return res
    
    
    def dfs(self,root,x,y,depth,parent,m,n):
        if root==None:
            return False
        if root.val==x:
            m.append((depth,parent))
        if root.val==y:
            n.append((depth,parent))
        print('value=',root.val,'  depth:',depth,'  parent:',parent)
        self.dfs(root.left,x,y,depth+1,root,m,n)
        self.dfs(root.right,x,y,depth+1,root,m,n)
        

 
