class Solution:
    def maxSlidingWindow(self, nums, k):
        dq = [0] * len(nums)
        front = 0
        back = 0
        ans = []
        for i in range(len(nums)):
            while front < back and dq[front] <= i - k:
                front += 1
            while front < back and nums[dq[back - 1]] <= nums[i]:
                back -= 1
            dq[back] = i
            back += 1
            if i >= k - 1:
                ans.append(nums[dq[front]])
        return ans
            