class Solution(object):
    def longestPalindrome(self, s):
        final_string=""
        
        if not s:
            return ""
        else:
            for j in range(len(s)):
                temp_final_string=""
                for i in s[j:]:
                    temp_final_string+=i
                    if(temp_final_string[::-1]==temp_final_string):
                        if len(temp_final_string) > len(final_string):
                            final_string=temp_final_string
        return final_string



        