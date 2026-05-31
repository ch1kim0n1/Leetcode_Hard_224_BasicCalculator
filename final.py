class Solution:
    def calculate(self, s: str) -> int:
        ans = 0
        sign = 1
        stack = [1]
        i = 0
        n = len(s)

        while i < n:
            ch = s[i]

            if ch.isdigit():
                num = 0
                while i < n and s[i].isdigit():
                    num = num * 10 + int(s[i])
                    i += 1
                ans += sign * num
                continue

            elif ch == '+':
                sign = stack[-1]

            elif ch == '-':
                sign = -stack[-1]

            elif ch == '(':
                stack.append(sign)

            elif ch == ')':
                stack.pop()

            i += 1

        return ans
