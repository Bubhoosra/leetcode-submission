class Solution:
    def reverseVowels(self, s: str) -> str:
        p=""
        for i in s:
            if i in "aeiouAEIOU":
                p+=i
        # print(p)
        j=len(p)-1
        l=list(s)
        for i in range(len(s)):
             if l[i] in "aeiouAEIOU":
                l[i]=p[j]
                #  print(s)
                j-=1
                #  print(p[j])
        return "".join(l)