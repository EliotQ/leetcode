class Solution:
    def generateMatrix(self, n: int) -> List[List[int]]:
        matrix = [[n*n]*n for _ in range(n)]

        left, right, top, bottom = 0, n, 0, n
        cur_num = 1
        while(True):
            for col in range(left, right):
                matrix[top][col] = cur_num
                cur_num += 1
            top += 1
            if top >= bottom:
                break

            for row in range(top, bottom):
                matrix[row][right-1] = cur_num
                cur_num += 1
            right -= 1
            if right <= left:
                break

            for col in range(right - 1, left - 1, -1):
                matrix[bottom - 1][col] = cur_num
                cur_num += 1
            bottom -= 1
            if top >= bottom:
                break

            for row in range(bottom - 1, top - 1, -1):
                matrix[row][left] = cur_num
                cur_num += 1
            left += 1
            if right <= left:
                break
        return matrix

# Comment: 按照步骤进行填充即可，不用额外判断是否越界，因为每次填充完都会判断是否越界。
# 区间取法：左闭右开，即[left, right)， [top, bottom)， 
# 因此1）在填充right和bottom时需要减1。
# 2）在从右到左和从下到上反向填充时，在range()中，为了不取到right和bottom，起点需要减一。为了取到left和top，终点需要减一。

# 时间复杂度：O(n^2) 
# 空间复杂度：O(n^2)