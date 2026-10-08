class Solution:
    def removeOuterParentheses(self, s: str) -> str:
        stack=[]
        ans=[]
        for c in s:
            if c=='(':
                if stack:
                    ans.append(c)
                stack.append(c)
            else:
                stack.pop()
                if stack:
                    ans.append(c)
        return ''.join(ans)