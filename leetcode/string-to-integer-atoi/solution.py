class Solution(object):
    def myAtoi(self, s):
        i=0
        leng=len(s)
        result=0
        sign=1
        while(i<leng and s[i]==' '):
            i+=1
        if(i<leng and s[i]=='-'):
            sign=-1
            i+=1
        elif(i<leng and s[i]=='+'):
            i+=1
        while(i<leng and s[i].isdigit()):
            digit=ord(s[i])-ord('0')
            result = (result * 10) + digit
            i+=1
        result=sign*result
        max=2147483647
        min=-2147483648
        if(result<min):
            return min
        elif(result>max):
            return max

        return result
        