class Solution(object):
    def reverseBits(self, n):
        answer=""
        fanswer=0
        j=0
        range=0
        while(n!=0 and range<=32):
            rem=n%2
            answer=str(rem)+answer
            n=n//2
        print(answer)
        data=list(answer)
        print(data)
        reversedata=data[::-1]


        for i in reversedata:
  # print(i)
            fdata=int(i)*2**j
            j+=1
            fanswer=fdata+fanswer
            range+=1
        return fanswer              