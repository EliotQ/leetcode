class Solution:
    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:
        nums = sorted(nums)
        n = len(nums)
        ans = []

        pointer1 = 0
        while(pointer1 < n - 3):
            if pointer1 > 0 and nums[pointer1] == nums[pointer1 - 1]:
                pointer1 += 1
                continue
            pointer2 = pointer1 + 1
            while(pointer2 < n - 2):
                if pointer2 > pointer1 + 1 and nums[pointer2] == nums[pointer2 - 1]:
                    pointer2 += 1
                    continue
                pointer3 = pointer2 + 1
                pointer4 = n - 1
                while(pointer3 < pointer4):
                    res = nums[pointer1] + nums[pointer2] + nums[pointer3] + nums[pointer4]
                    if res < target:
                        pointer3 += 1
                        while(pointer3 < pointer4 - 1 and nums[pointer3] == nums[pointer3 - 1]):
                            pointer3 += 1
                    elif res > target:
                        pointer4 -= 1
                        while(pointer3 < pointer4 - 1 and nums[pointer4] == nums[pointer4 + 1]):
                            pointer4 -= 1
                    else:
                        ans.append([nums[pointer1], nums[pointer2], nums[pointer3], nums[pointer4]])
                        
                        pointer3 += 1
                        while(pointer3 < pointer4 - 1 and nums[pointer3] == nums[pointer3 - 1]):
                            pointer3 += 1

                        pointer4 -= 1
                        while(pointer3 < pointer4 - 1 and nums[pointer4] == nums[pointer4 + 1]):
                            pointer4 -= 1
                pointer2 += 1
            pointer1 += 1
        return ans

# Comment:
# 与target=0的情况不同，target不为0时，不能直接判断nums[pointer1]是否大于target，因为右边的三个数可能小于0，使得和小于或等于target，所以不能直接break
# 即以下条件是错误的：
#            if nums[pointer1] > target:
#                break

# 时间复杂度：O(n^3)
# 空间复杂度：O(n)，排序的空间复杂度 （不考虑返回值的空间复杂度，返回值的空间复杂度为O(n^4)，最坏情况下为C(n,4)，即O(n^4)）