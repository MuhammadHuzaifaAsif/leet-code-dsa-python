class Solution(object):
    def threeSum(self, nums): 
        nums.sort()
        print(nums)
        result=[]
        numlen=len(nums)
        for a in range(0,numlen-2):
            if a > 0 and nums[a] == nums[a - 1]:
                continue
            q=a+1
            r=numlen-1
            while(q<r):
                sum=nums[a]+nums[q]+nums[r]
                if sum==0:
                    result.append([nums[a], nums[q], nums[r]])
                    q += 1
                    r -= 1
                    
                    while q<r and nums[q]==nums[q-1]:
                        q+=1
                elif sum>0:
                    r-=1
                elif sum<0:
                    q+=1
            
        return result 
    

       
        