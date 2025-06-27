class Solution:
    def countSmaller(self, nums):
        arr = [(num, idx) for idx, num in enumerate(nums)]
        result = [0] * len(nums)
        
        def merge_sort(arr):
            if len(arr) <= 1:
                return arr
            
            mid = len(arr) // 2
            left = merge_sort(arr[:mid])
            right = merge_sort(arr[mid:])
            return merge(left, right)
        
        def merge(left, right):
            merged = []
            i = j = 0
            while i < len(left) and j < len(right):
                if left[i][0] > right[j][0]:
                    merged.append(right[j])
                    j += 1
                else:
                    result[left[i][1]] += j
                    merged.append(left[i])
                    i += 1
            
            while i < len(left):
                result[left[i][1]] += j
                merged.append(left[i])
                i += 1
            
            while j < len(right):
                merged.append(right[j])
                j += 1
            
            return merged
        
        merge_sort(arr)
        return result