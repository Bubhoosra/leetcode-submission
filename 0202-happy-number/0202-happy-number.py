
def square(x):
    s=0
    while(x!=0):
        rem=x%10
        s+=rem*rem
        x=x//10
    return s
class Solution:
    def isHappy(self, n: int) -> bool:
        # if n%2==0:
        #     return False
        # else:
        #     return True
        t=[]
        while(1):
            n=square(n)
            if n==1:
                return True
            if n in t:
                return False
            else:
                t.append(n)
            
       