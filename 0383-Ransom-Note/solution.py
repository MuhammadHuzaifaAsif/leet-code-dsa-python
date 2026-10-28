from collections import Counter
class Solution(object):
    # ransomNote = "aa", magazine = "ab"
    def canConstruct(self, ransomNote, magazine):
        bool=""
        new_var=""
        ran=len(ransomNote)
        mag=len(magazine)
        if(mag<ran):
            return False
        else:
            r=Counter(ransomNote)
            m=Counter(magazine)
            if(r==m):
                return True
            else:
                return False


        

       
