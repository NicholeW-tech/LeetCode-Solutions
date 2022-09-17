class Solution:
    def heightChecker(self, heights: List[int]) -> int:
        i = 0
        expected = heights.copy()
        expected.sort()
        indices = 0
        
        while i < len(heights):
            if heights[i] != expected[i]:
                indices += 1
            i +=1
        
        return indices
