class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        num_stack = []
        for token in tokens:
            if token == '+':
                a = num_stack.pop()
                b = num_stack.pop()
                num_stack.append(a + b)
            elif token == '/':
               a = num_stack.pop()
               b = num_stack.pop()
               num_stack.append(int(float(b) / a)) 
            elif token == '-':
                a = num_stack.pop()
                b = num_stack.pop()
                num_stack.append(b - a)
            elif token == '*':
                a = num_stack.pop()
                b = num_stack.pop()
                num_stack.append(a * b)
            else: 
                num_stack.append(int(token))
        return num_stack[0]