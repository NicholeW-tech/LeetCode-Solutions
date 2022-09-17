class Solution:
    def checkIfExist(self, arr: List[int]) -> bool:
        i = 0
        while i < len(arr):
            for j in range(len(arr)):
                if i == j:
                    j += 1
                elif arr[i] == arr[j] * 2:
                    return True
            i += 1