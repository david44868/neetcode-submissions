class Solution:
    def replaceElements(self, arr: List[int]) -> List[int]:
        
        curr = arr[-1]
        arr[-1] = -1

        for x in range(len(arr) - 2, -1, -1):
            temp = arr[x]            
            arr[x] = curr
            curr = max(temp, curr)
        
        return arr