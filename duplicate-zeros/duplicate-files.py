class Solution(object):
    def duplicateZeros(self, arr):
        """
        :type arr: List[int]
        :rtype: None Do not return anything, modify arr in-place instead.
        """
        left = 0
        
        while left < len(arr):
            if arr[left]  == 0:
                index= left +1
                arr.insert(index, 0)
                left +=2
                arr.pop()
            else:
                left+=1
