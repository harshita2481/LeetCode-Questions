class Solution:
    def minSumSquareDiff(self, nums1: list[int], nums2: list[int], k1: int, k2: int) -> int:
        d = [abs(a - b) for a, b in zip(nums1, nums2)]
        k = k1 + k2
        if sum(d) <= k:
            return 0

        mx = max(d)
        freq = [0] * (mx + 1)
        for x in d:
            freq[x] += 1

        cnt = 0                      # elements currently at level v (after shaving above)
        for v in range(mx, 0, -1):
            cnt += freq[v]
            if cnt == 0:
                continue
            if k >= cnt:
                k -= cnt             # lower all cnt elements from v to v-1
            else:
                # k elements go to v-1, the other cnt-k stay at v
                total = (cnt - k) * v * v + k * (v - 1) * (v - 1)
                total += sum(freq[u] * u * u for u in range(v))  # untouched lower values
                return total
        return 0