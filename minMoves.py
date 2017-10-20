def minMoves(nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        step=0
        _max=max(nums)
        _min=min(nums)
        diff=_max-_min
        while diff!=0:
            step+=diff
            nums[nums.index(max(nums))]-=diff
            _max=max(nums)
            _min=min(nums)
            diff=_max-_min
        return step
print minMoves([1,3,4,5])
def minMoves2(nums):
	return sum(nums) - len(nums)*min(nums)