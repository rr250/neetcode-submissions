class Solution:
    def checkValidString(self, s: str) -> bool:
        from functools import lru_cache

        @lru_cache(None)
        def dfs(i, bal):
            # bal = current open-parenthesis balance

            # If balance negative, invalid.
            if bal < 0:
                return False

            # End of string: valid iff balance zero.
            if i == len(s):
                return bal == 0

            ch = s[i]

            if ch == '(':
                return dfs(i + 1, bal + 1)
            if ch == ')':
                return dfs(i + 1, bal - 1)

            # ch == '*': try all 3 interpretations
            # as '(', as ')', as empty
            return (
                dfs(i + 1, bal + 1) or  # treat '*' as '('
                dfs(i + 1, bal - 1) or  # treat '*' as ')'
                dfs(i + 1, bal)         # treat '*' as ''
            )

        return dfs(0, 0)
