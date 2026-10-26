class Solution(object):
    def rotate(self, nums, k):
        l=len(nums)
        k = k%l
        list=nums[::-1]
        l=len(nums)
        # print(list)
        final=list[0:k][::-1]+list[k:l][::-1]
        nums[:]=final
        print(nums)
                