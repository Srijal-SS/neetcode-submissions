class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        freq = Counter(nums)

        for num, fq in freq.items():
            if fq>1:
                return True
        
        return False
