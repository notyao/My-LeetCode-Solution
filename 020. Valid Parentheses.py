class Solution:
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        stack = []
        for i in s:
            if i == "(":
                stack.append(")")
            if i == "[":
                stack.append("]")
            if i == "{":
                stack.append("}")
            elif len(stack)==0 or stack.pop() != i:
                return False
        return stack
