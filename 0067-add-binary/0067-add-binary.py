class Solution:
    def addBinary(self, a: str, b: str) -> str:
        i=len(a)
        j=len(b)
        if i<j:
            a=str(0)*(j-i)+a
        elif i>j:
            b=str(0)*(i-j)+b
        print(a,b)
        s=""
        c=0
        i=len(a)-1
        while(i>-1):
            if a[i]=="1" and b[i]=="1":
                if c==1:
                    s="1"+s
                    c=1
                else:
                    s="0"+s
                    c=1
            elif a[i]=="1" and b[i]=="0":
                if c==1:
                    s="0"+s
                    c=1
                else:
                    s="1"+s
            elif a[i]=="0" and b[i]=="1":
                if c==1:
                    s="0"+s
                    c=1
                else:
                    s="1"+s
            elif a[i]=="0" and b[i]=="0":
                if c==1:
                    s="1"+s
                    c=0
                else:
                    s="0"+s
                
            print(s)
            i-=1
        if c==1:
            s="1"+s
        return s
            


        print(a,b)


        