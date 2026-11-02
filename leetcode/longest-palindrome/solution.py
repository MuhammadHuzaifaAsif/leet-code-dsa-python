class Solution(object):
    def longestPalindrome(self, s):
        count=Counter(s)
        print(count)
        total=0
        hasodd=False
        for char,count in count.items():
            print(char,count)
            if count%2==0:
                total+=count
            elif count%2==1:
                total+=count-1
                hasodd=True
        if hasodd:
            total+=1
        return total

        
        