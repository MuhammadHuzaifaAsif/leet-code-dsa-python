        for i in digits:
            for existingcombination in result:


            temp_list=[]
            result=temp_list
                for letter in phone_map[i]:
                    temp_list.append(existingcombination+letter)
        return result            
        phone_map={"1":[],"2":['a','b','c'],"3":['d','e','f'],"4":['g','h','i'],"5":['j','k','l'],"6":
        ['m','n','o'],"7":['p','q','r','s'],"8":['t','u','v'],"9":['w','x','y','z']}
    def letterCombinations(self, digits):
        result=[""]
class Solution(object):
