class Solution:
    # @param {integer[]} nums
    # @return {void} Do not return anything, modify nums in-place instead.
    def nextPermutation(self, nums):
        """
        Implement next permutation, which rearranges numbers into the lexicographically next greater permutation of numbers.
        If such arrangement is not possible, it must rearrange it as the lowest possible order (ie, sorted in ascending order).
        The replacement must be in-place, do not allocate extra memory.
        Here are some examples. Inputs are in the left-hand column and its corresponding outputs are in the right-hand column.
        1,2,3 -> 1,3,2
        3,2,1 -> 1,2,3
        1,1,5 -> 1,5,1
        2, 3, 1 -> 3, 1, 2
        1, 3, 2 -> 3, 2, 1
        """
        # 1, 2, 3 -> 1, 3, 2
        # 1, 3, 2 -> 2, 1, 3
        # 1, 4, 5, 5, 7, 6, 5,  4, 
        i = len(nums) - 1
        while i > 0 and nums[i - 1] >= nums[i]: i = i - 1

        if i > 0:
            k = len(nums) - 1
            while k > i and nums[k] <= nums[i - 1]: k = k - 1
            nums[k], nums[i - 1] = nums[i - 1], nums[k]
        j, k = i, len(nums) - 1
        while j < k:
            nums[j], nums[k] = nums[k], nums[j]
            j = j + 1
            k = k -  1
        
    # @param {integer} n
    # @return {integer}
    def countDigitOne(self, n):
        """ Given an integer n, count the total number of digit 1
        appearing in all non-negative integers less than or equal to n.
        For example:
        Given n = 13,
        Return 6, because digit 1 occurred in the following numbers: 1, 10, 11, 12, 13.
        """
        count = 0
        factor = 1
        while factor < n:
            count = count + (n/factor + 8) /10 * factor  + (1 if n/factor%10 == 1 else 0) * (n%factor + 1)
            factor = factor * 10
        return count
                
        
    # @param {integer[]} height
    # @return {integer}
    def maxArea(self, height):
        """Given n non-negative integers a1, a2, ..., an, where each represents a
        point at coordinate (i, ai). n vertical lines are drawn such that the two
        endpoints of line i is at (i, ai) and (i, 0). Find two lines, which together
        with x-axis forms a container, such that the container contains the most water.
        """
        i, j = 0, len(height) - 1
        area = 0
        while i < j:
            h = min(height[i], height[j])
            area = max(area, h * (i - j))
            while height[i] <= h and i < j: i = i + 1
            while height[j] <= h and i < j: j = j - 1
        return area
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
    #print a.maxProduct([2,3,-2,4])
    b = [ 1, 3, 2]
    a.nextPermutation(b)
    print b
    b = [ 2, 3, 1]
    a.nextPermutation(b)
    print b
    #print a.countDigitOne(8192)
    #print a.generateParenthesis(3)
            
