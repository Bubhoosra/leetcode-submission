# def gcd(a,b):
#     if b==0:
#         return a
#     return gcd(b,a%b)
def reversal(nums,left,right):
    while(left<right):
        temp=nums[left]
        nums[left]=nums[right]
        nums[right]=temp
        left+=1
        right-=1

class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        n=len(nums)
        if n==1 or k==0 or n==k:
            return nums
        
        
        reversal(nums,0,n-1)
        reversal(nums,0,(k-1)%n)
        reversal(nums,(k)%n,n-1)
        # else:
        #     while(k!=0):
        #         x=nums[0]
        #         nums[:]=nums[1:]
        #         nums.append(x)
        #         k-=1


        return nums

        # N=len(nums)
        # k=k%N
        # gn=gcd(k,N)
        # if gn<k:
        #     gn=k
        # print(gn)
        # for i in range(gn):
        #     temp=nums[i]
        #     j=i
        #     while(j<N):
        #         nums[j]=nums[(j+k)%N]
        #         j+=k
        #     j-=k
        #     nums[j]=temp
        #     print(nums)
        # if gn==1 and N%2!=0:
        #     x=nums[0]
        #     nums[:]=nums[1:]
        #     nums.append(x)

        return nums

        """
        Do not return anything, modify nums in-place instead.
        """
        # l=[]
        # n=len(nums)
        # for i in range(0,len(nums)):
        #     idx=(n+i-k)%n
        #     h=nums[idx]
        #     l.append(h)
        # nums[:]=l[:]
        # return nums
        
            
        
            
        