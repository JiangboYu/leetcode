class Solution:
    # @descrip Problem: Find the contiguous subarray within an array (containing at least one number) which has the largest product.
    #For example, given the array [2,3,-2,4],
    #the contiguous subarray [2,3] has the largest product = 6.

    # @param {integer[]} nums
    # @return {integer}
    def maxProduct(self, nums):
        #Dynamic solution
        #For each state, knowledge need to be maintained including
        #  1. current max_p
        #  2. current min_p
        # max_p would tract the max product when num > 0
        # min_p would tract the max product when num < 0
        max_p, min_p, max_product = nums[0], nums[0], nums[0]
        for num in nums[1:]:
            tmp = max_p
            max_p = max(max_p * num, num, min_p * num)
            min_p = min(tmp * num, num, min_p * num)
            max_product = max(max_product, max_p)
        return max_product
        
    def generateParenthesis(self, n):
        def generate(p, left, right, paren = []):
            if left: generate( p + '(', left - 1, right, paren)
            if right > left: generate(p + ')', left, right - 1, paren)
            if not right: paren += p,
            return paren
            
    def Parenthesis(self, list_Parenthesis, candidate, left, right):
        if right == 0:
            list_Parenthesis.append(candidate)
            return
        if left < right:
            self.Parenthesis(list_Parenthesis, candidate + ')', left, right - 1)
        if left > 0:
            self.Parenthesis(list_Parenthesis, candidate + '(', left - 1, right)
    # @return {string[]}
    def generateParenthesis(self, n):
        list_Parenthesis = []
        candidate = ''
        self.Parenthesis(list_Parenthesis, candidate,  n, n)
        return list_Parenthesis
if __name__ == "__main__":    
    a = Solution()
    print a.maxProduct([2,3,-2,4])
    #print a.generateParenthesis(3)
            
