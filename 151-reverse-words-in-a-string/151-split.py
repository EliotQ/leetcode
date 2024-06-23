class Solution:
    def reverseWords(self, s: str) -> str:
        word_list = s.strip().split()
        revered_word_list = word_list[::-1]
        return ' '.join(revered_word_list)

# Comment：
# 时间复杂度：O(n)
# 空间复杂度: O(n)