class pairelements:
    def twosum(self, nums, target):
        lookup = {}
        for i, num in enumerate(nums):
            if target - num in lookup:
                return(lookup[target - num], i)
            lookup[num] = i
value = int(input("enter the value of which's sum you want to 70"))
print("index1=%d index2=%d" %
      pairelements().twosum((10, 20, 30, 40, 50, 60, 70), value))