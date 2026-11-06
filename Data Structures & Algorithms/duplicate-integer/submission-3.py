class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        # freq = Counter(nums)

        # for num, fq in freq.items():
        #     if fq>1:
        #         return True
        
        # return False

        seen = set()

        for num in nums:
            if num in seen:
                return True
            seen.add(num)

        return False
