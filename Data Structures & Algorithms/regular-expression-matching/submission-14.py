class Solution:
    def isMatch(self, s: str, p: str) -> bool:
        return self.match(s, p, 0, 0)
    
    def match(self, s: str, p: str, s_idx: int, p_idx: int) -> bool:
        # Base case: pattern exhausted
        if p_idx == len(p):
            return s_idx == len(s)
        
        # Check if current characters match
        curr_match = s_idx < len(s) and (p[p_idx] == s[s_idx] or p[p_idx] == '.')
        
        # Check if next character is '*'
        if p_idx + 1 < len(p) and p[p_idx + 1] == '*':
            # Option 1: Match 0 occurrences of 'char*' (skip it)
            if self.match(s, p, s_idx, p_idx + 2):
                return True
            
            # Option 2: Match 1+ occurrences (if current char matches)
            if curr_match and self.match(s, p, s_idx + 1, p_idx):
                return True
            
            return False
        
        # Regular character: must match current and rest must match
        return curr_match and self.match(s, p, s_idx + 1, p_idx + 1)
