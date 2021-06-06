class Solution:
    def search(self, nums: List[int], target: int) -> int:
        low_track = 0
        high_track = len(nums) - 1
        while low_track <= high_track:
            mid = (low_track + high_track) // 2
            if nums[mid]==target:
                return mid
            if nums[mid]>target:
                high_track = mid - 1
            else:
                low_track = mid + 1
        return -1
        
        
