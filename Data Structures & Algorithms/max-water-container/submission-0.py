class Solution:
    def maxArea(self, heights: List[int]) -> int:
        
        if len(heights) <= 1:
            return 0

        l, r = 0, len(heights) - 1
        l_max, r_max = heights[0], heights[len(heights) - 1]
        max_water = (r - l) * min(l_max, r_max)

        while l < r:
            if l_max < r_max:
                l += 1
                l_max = max(l_max, heights[l])
                max_water = max(max_water, (r - l) * min(l_max, r_max))
            else:
                r -= 1
                r_max = max(r_max, heights[r])
                max_water = max(max_water, (r - l) * min(l_max, r_max))
        
        return max_water