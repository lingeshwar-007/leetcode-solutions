class Solution:
    def reverseDegree(self, s: str) -> int:
        dic={chr(97+i): 26-i for i in range(26)}
        sum=0
        for i in range(len(s)):
            sum+=(dic[s[i]]*(i+1))
        return sum
