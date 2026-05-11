class Solution:
    def kidsWithCandies(self, candies: List[int], extraCandies: int) -> List[bool]:
        max_candies = max(candies)
        i = 0
        result = []
        while i < len(candies):
            if candies[i] + extraCandies >= max_candies:
                result.append(True)
            else:
                result.append(False)
            i += 1
        return result