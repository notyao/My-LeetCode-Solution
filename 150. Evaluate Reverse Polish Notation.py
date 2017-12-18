class Solution:
    def evalRPN(self, tokens):
        """
        :type tokens: List[str]
        :rtype: int
        """

        stack = []
        for t in tokens:
            if t not in ["+", "-", "*", "/"]:
                stack.append(int(t))
            else:
                if len(stack) > 1:
                    first, second = stack.pop(), stack.pop()
                else:
                    return stack.pop()

            if t == "+":
                stack.append(second + first)
            if t == "-":
                stack.append(second - first)
            if t == "*":
                stack.append(second * first)
            if t == "/":
                stack.append(int(second / first))
        return stack.pop()
