class Solution:
    def findContentChildren(self, g: List[int], s: List[int]) -> int:
        g.sort()
        s.sort()
        count = 0
        while(s):
            while(g and g[-1] > s[-1]):
                g.pop()
            if not g:
                break
            
            g.pop()
            s.pop()
            count += 1
        return count

# Complexity Analysis
# The time complexity for this approach is O(nlogn) where n is the length of the list g or s.
# The space complexity for this approach is O(1) since we are not using any extra space.