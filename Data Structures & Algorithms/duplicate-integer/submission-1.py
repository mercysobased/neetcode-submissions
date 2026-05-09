class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        Visto = set()
        for n in nums:
            if n in Visto:
                return True
            Visto.add(n)
        return False