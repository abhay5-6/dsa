class Solution:
    def reverseWords(self, s: str) -> str:
        res = s.split()
        ans = ""

        for i in range(len(res) - 1, -1, -1):
            ans += " " + res[i]

        return ans.strip()