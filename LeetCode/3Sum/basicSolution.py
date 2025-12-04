def threeSum(self, nums: List[int]) -> List[List[int]]:
        l1 = []
        for i in range(len(nums)):
            for j in range(i+1, len(nums)):
                if -(nums[i] + nums[j]) in nums[j:] and nums.index(-(nums[i] + nums[j])) != j and nums.index(-(nums[i] + nums[j])) != i:
                    if (sorted([nums[i], nums[j], nums[nums.index(-(nums[i] + nums[j]))]])) not in l1:
                        l1.append(sorted(([nums[i], nums[j], nums[nums.index(-(nums[i] + nums[j]))]])))
        return l1
