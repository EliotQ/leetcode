class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        from collections import defaultdict
        magazine_dict = defaultdict(int)

        for char in magazine:
            magazine_dict[char] += 1
        
        for char in ransomNote:
            if magazine_dict[char] < 1:
                return False
            magazine_dict[char] -= 1
        return True

# Comment:
# 使用哈希表记录magazine中每个字符的数量，然后遍历ransomNote，若存在则减，直到不存在或结束。
# 时间复杂度：O(n)
# 空间复杂度：O(n)