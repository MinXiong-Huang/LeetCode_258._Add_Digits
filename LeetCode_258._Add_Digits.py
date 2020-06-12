class Solution(object):
    def addDigits(self, num):
        """
        :type num: int
        :rtype: int
        """
        answer=0
        while num>0:
            answer+=int(num%10)
            num=int(num/10)

            if num==0 and answer>9:
                num=int(answer)
                answer=0
        return answer

#Example
s=Solution()
s.addDigits(38)