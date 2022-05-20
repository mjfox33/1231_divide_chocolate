from re import A


class Solution:
    def maximizeSweetness(self, sweetness: list[int], k: int) -> int:
        left = 1
        right = sum(sweetness) // (k+1)
        while left < right:
            mid = left + (right - left + 1) // 2
            current = cuts = 0
            for curr_sweet in sweetness:
                current += curr_sweet
                if current >= mid:
                    cuts += 1
                    current = 0
            if cuts > k:
                left = mid
            else:
                right = mid - 1
        return right

