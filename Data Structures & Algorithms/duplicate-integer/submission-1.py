class Solution:
    def hasDuplicate(self,nums):
        var = set()
        for i in nums:
            if i in var:
                return True
            var.add(i)
        return False