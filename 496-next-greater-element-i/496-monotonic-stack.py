class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        result = dict(zip(nums2, [-1]*len(nums2)))
        stack = [0]

        for i in range(1, len(nums2)):
            if nums2[i] <= nums2[stack[-1]]:
                stack.append(i)
            else:
                while len(stack) > 0 and nums2[i] > nums2[stack[-1]]:
                    result[nums2[stack[-1]]] = nums2[i]
                    stack.pop()
                stack.append(i)
        
        ans = []
        for num in nums1:
            ans.append(result[num])
        return ans

# Comment:
# This solution uses a monotonic stack to find the next greater element for each element in nums1.
# It iterates through nums2 and maintains a stack of indices of elements that are yet to find the next greater element.
# If an element is lower than or equal to the element at the top of the stack, it is added to the stack.
# If an element is higher than the element at the top of the stack, it means the next greater element has been found.
# In this case, the function pops elements from the stack and calculates the next greater element for each popped element.
# The result is stored in a dictionary with the element as the key and the next greater element as the value.
# Finally, the function iterates through nums1 and retrieves the next greater element for each element from the dictionary.

# Time complexity: O(n+m), where n is the length of nums1 and m is the length of nums2
# Space complexity: O(m), where m is the length of nums2

