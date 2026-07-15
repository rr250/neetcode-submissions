class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        i=len(digits)-1
        carry=0
        add=1
        while(i>=0):
            if i!= len(digits)-1:
                add=0
            d=digits[i]+add+carry
            if(d>=10):
                d%=10
                carry=1
            else:
                carry=0
            digits[i]=d
            i-=1
        if(carry!=0):
            return [carry]+digits
        return digits
        