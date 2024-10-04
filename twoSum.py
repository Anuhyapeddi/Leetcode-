def twoSum(self, nums, target):
  mydict = dict() # {}

  for i in range(len(nums)):
      diff = target - nums[i]
      if diff in mydict.keys():
          return i, mydict[diff]
      else:
          mydict[nums[i]] = i
