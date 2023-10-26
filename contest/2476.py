class Solution:
    def closestNodes(self, root: Optional[TreeNode], queries: List[int]) -> List[List[int]]:
        lst=[]
        def inorder(root):
            if root!=None:
                inorder(root.left)
                lst.append(root.val)
                inorder(root.right)
        inorder(root)

        
        def getceil(nums,n):
            left=0
            right=len(nums)-1
            ceil=-1
            floor=-1
            while left<=right:
                mid=(left+right)//2
                if nums[mid]==n:
                    return [nums[mid],nums[mid]]
                elif n<nums[mid]:
                    ceil=nums[mid]
                    right=mid-1
                else:
                    left=mid+1
                    floor=nums[mid]
            return [floor,ceil]
        return [getceil(lst,i) for i in queries]
        