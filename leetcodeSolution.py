class Solution:
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
    print a.generateParenthesis(3)
            
