class Solution:
    def nextPermutation(self, nums: 'List[int]') -> 'None':
        """
        Do not return anything, modify nums in-place instead.
        """
        #124875
        if not nums or len(nums)==1:
            return
        else:
            r=len(nums)-1
            while r>=0 and nums[r-1]>=nums[r]:
                r=r-1
            if r==0:
                nums.reverse()
            else:
                cur=r-1
                right=len(nums)-1
                while cur<right and nums[cur]>=nums[right]:
                    right-=1
                nums[cur],nums[right]=nums[right],nums[cur]
                nums[cur+1:]=nums[cur+1:][::-1]
        
