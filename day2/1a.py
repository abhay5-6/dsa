"""
class Solution:
    def removeOuterParentheses(self, s: str) -> str:
        curr=0
        flag=False
        sub=[]
        for i in range(len(s)):
            if s[i]=="(":
                curr+=1
            else:
                curr-=1
            if curr>0:
                while True:
                    sub.append(i)
                    flag=False
                if curr==0:
                    sub.append(i)
                    flag=True
            then i will remove all the indexes present in sub this rough implemntation
"""
class Solution:
    def removeOuterParentheses(self, s: str) -> str:
        curr = 0
        ans = []

        for ch in s:
            if ch == "(":
                curr += 1
                if curr > 1:
                    ans.append(ch)
            else:
                curr -= 1
                if curr > 0:
                    ans.append(ch)

        return "".join(ans)

