class Solution:
    def maxDepth(self, s: str) -> int:
        depth=0
        maxdepth=0
        for c in s:
            if c=='(':
                depth+=1
                if depth>maxdepth:
                    maxdepth=depth
            elif c==')':
                depth-=1
        return maxdepth