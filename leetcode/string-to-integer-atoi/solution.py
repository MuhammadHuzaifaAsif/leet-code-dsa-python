            i+=1
        while(i<leng and s[i].isdigit()):
            digit=ord(s[i])-ord('0')
            result = (result * 10) + digit
        elif(i<leng and s[i]=='+'):
            i+=1
        result=sign*result
        max=2147483647
        min=-2147483648
        if(result<min):
            return min
        elif(result>max):
            return max

        return result
        
