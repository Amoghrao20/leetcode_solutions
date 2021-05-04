class Solution:
    def maxArea(self, height: List[int]) -> int:
        left=0
        right=len(height)-1
        maxi=0
        for i in range(len(height)):
            if height[left]>height[right]:
                if ((right-left)*height[right])>maxi:
                    maxi=(right-left)*height[right]
                right=right-1
            else:
                if ((right-left)*height[left])>maxi:
                    maxi=(right-left)*height[left]
                left=left+1
        return maxi
