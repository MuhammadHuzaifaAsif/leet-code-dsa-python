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
                for letter in r:
                    if(r[letter]>m[letter]):
                        return False
                    else:
                        return True
            else:
                return False


        

       
