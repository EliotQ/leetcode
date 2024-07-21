class Solution:
    def candy(self, ratings: List[int]) -> int:
        candy_vec = [1]*len(ratings)

        for i in range(1, len(ratings)):
            if ratings[i] > ratings[i-1]:
                candy_vec[i] = candy_vec[i - 1] + 1
        
        for i in range(len(ratings) - 2, -1, -1):
            if ratings[i] > ratings[i+1]:
                candy_vec[i] = max(candy_vec[i], candy_vec[i+1] + 1)
        
        result = sum(candy_vec)
        return result

# Comment:
# In this solution, we first assign 1 candy to each child.
# Then from left to right, we assign more candies to the children with higher ratings than their left neighbors.
# Then from right to left, we assign more candies to the children with higher ratings than their right neighbors.
# Finally, we return the sum of the candies assigned to the children.

# ?The proof of the correctness of this solution can be explored if have time.