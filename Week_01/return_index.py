def twoSum(nums, target):
        set_dict = {}
        for index, num in enumerate(nums):
            if (target - num) in set_dict.keys():
                return [set_dict.get(target - num), index]
            set_dict[num] = index

if __name__ == '__main__':
    print(twoSum(nums = [2, 11, 7, 15], target = 9))
