from functools import lru_cache
class Solution:
    def checkValidString(self, s: str) -> bool:
        @lru_cache(None)
        def checkParenthesis(b, h):
            h=list(h)
            # print('rec', b,h)
            c=b
            for a in b:
                # print(a,'|',b,'|',c,'|',h)
                if a == '(':
                    h.append(a)
                if a == ')':
                    if len(h)==0:
                        return False
                    else:
                        h.pop()
                if a == '*':
                    x1 = checkParenthesis(c[1:], tuple(h+['(']))
                    x2=False
                    if len(h)>0:
                        x2 = checkParenthesis(c[1:], tuple(h[:len(h)-1]))
                    x3 = checkParenthesis(c[1:], tuple(h))
                    return x1 or x2 or x3
                c=c[1:]
            if len(h)==0:
                return True
            else:
                return False
        
        return checkParenthesis(s, tuple([]))
        

                 
        