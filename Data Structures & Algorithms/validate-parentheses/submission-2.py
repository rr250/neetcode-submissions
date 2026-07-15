class Solution:
    def isValid(self, s: str) -> bool:
        l=[]
        m={")":"(", "}":"{", "]":"["}
        for a in s:
            if a in ["(", "{", "["]:
                l+=[a]
            else:
                if len(l)>0 and m[a]==l[-1]:
                    l.pop()
                else:
                    return False
        if len(l) != 0:
            return False
        return True

        