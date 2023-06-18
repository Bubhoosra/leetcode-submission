class Solution:
    def replaceDigits(self, s: str) -> str:
        i=1
        while(i<len(s)):
            # print(ord(s[i]))
            s=s.replace(s[i],chr(int(s[i])+ord(s[i-1])),1)
            i+=2
        return s
