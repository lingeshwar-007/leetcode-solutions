class Solution:
    def minAddToMakeValid(self, s: str) -> int:
        lst=[]
        c=0
        for i in range(len(s)):
            if s[i]=='(':
                lst.append(s[i])
            else:
                if lst and lst.pop()=='(':
                    continue
                else:
                    c+=1
        return c+len(lst)
